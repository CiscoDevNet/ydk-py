


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'SetC3plAccountFeatureType_Enum' : _MetaInfoEnum('SetC3plAccountFeatureType_Enum', 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB',
        {
            'queueing':'QUEUEING',
            'wred':'WRED',
            'police':'POLICE',
        }, 'CISCO-CLASS-BASED-QOS-MIB', _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB']),
    'QueueMechanism_Enum' : _MetaInfoEnum('QueueMechanism_Enum', 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB',
        {
            'precedence':'PRECEDENCE',
            'dscp':'DSCP',
            'discardClass':'DISCARDCLASS',
            'qosGroup':'QOSGROUP',
            'atmClp':'ATMCLP',
            'mplsExp':'MPLSEXP',
        }, 'CISCO-CLASS-BASED-QOS-MIB', _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB']),
    'TrafficShapingLimit_Enum' : _MetaInfoEnum('TrafficShapingLimit_Enum', 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB',
        {
            'average':'AVERAGE',
            'peak':'PEAK',
        }, 'CISCO-CLASS-BASED-QOS-MIB', _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB']),
    'PoliceAction_Enum' : _MetaInfoEnum('PoliceAction_Enum', 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB',
        {
            'transmit':'TRANSMIT',
            'setIpDSCP':'SETIPDSCP',
            'setIpPrecedence':'SETIPPRECEDENCE',
            'setQosGroup':'SETQOSGROUP',
            'drop':'DROP',
            'setMplsExp':'SETMPLSEXP',
            'setAtmClp':'SETATMCLP',
            'setFrDe':'SETFRDE',
            'setL2Cos':'SETL2COS',
            'setDiscardClass':'SETDISCARDCLASS',
            'setMplsExpTopMost':'SETMPLSEXPTOPMOST',
            'setIpDscpTunnel':'SETIPDSCPTUNNEL',
            'setIpPrecedenceTunnel':'SETIPPRECEDENCETUNNEL',
            'setL2CosInner':'SETL2COSINNER',
            'unconfigured':'UNCONFIGURED',
            'setDei':'SETDEI',
            'setDeiImposition':'SETDEIIMPOSITION',
            'setSrpPriority':'SETSRPPRIORITY',
        }, 'CISCO-CLASS-BASED-QOS-MIB', _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB']),
    'CbQosEBType_Enum' : _MetaInfoEnum('CbQosEBType_Enum', 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB',
        {
            'typeNone':'TYPENONE',
            'typeCorvil':'TYPECORVIL',
        }, 'CISCO-CLASS-BASED-QOS-MIB', _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB']),
    'TrafficDirection_Enum' : _MetaInfoEnum('TrafficDirection_Enum', 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB',
        {
            'input':'INPUT',
            'output':'OUTPUT',
        }, 'CISCO-CLASS-BASED-QOS-MIB', _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB']),
    'CbQosTMSetType_Enum' : _MetaInfoEnum('CbQosTMSetType_Enum', 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB',
        {
            'none':'NONE',
            'ipDscp':'IPDSCP',
            'ipPrecedence':'IPPRECEDENCE',
            'qosGroup':'QOSGROUP',
            'l2Cos':'L2COS',
            'mplsExpImp':'MPLSEXPIMP',
            'mplsExpTop':'MPLSEXPTOP',
        }, 'CISCO-CLASS-BASED-QOS-MIB', _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB']),
    'QosMatchInfo_Enum' : _MetaInfoEnum('QosMatchInfo_Enum', 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB',
        {
            'none':'NONE',
            'matchNot':'MATCHNOT',
        }, 'CISCO-CLASS-BASED-QOS-MIB', _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB']),
    'CbQosQueueUnitType_Enum' : _MetaInfoEnum('CbQosQueueUnitType_Enum', 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB',
        {
            'packets':'PACKETS',
            'cells':'CELLS',
            'bytes':'BYTES',
            'ms':'MS',
            'us':'US',
            'percentage':'PERCENTAGE',
        }, 'CISCO-CLASS-BASED-QOS-MIB', _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB']),
    'IPHCOption_Enum' : _MetaInfoEnum('IPHCOption_Enum', 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB',
        {
            'rtp':'RTP',
            'tcp':'TCP',
            'bothRtpTcp':'BOTHRTPTCP',
        }, 'CISCO-CLASS-BASED-QOS-MIB', _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB']),
    'QosObjectType_Enum' : _MetaInfoEnum('QosObjectType_Enum', 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB',
        {
            'policymap':'POLICYMAP',
            'classmap':'CLASSMAP',
            'matchStatement':'MATCHSTATEMENT',
            'queueing':'QUEUEING',
            'randomDetect':'RANDOMDETECT',
            'trafficShaping':'TRAFFICSHAPING',
            'police':'POLICE',
            'set':'SET',
            'compression':'COMPRESSION',
            'ipslaMeasure':'IPSLAMEASURE',
            'account':'ACCOUNT',
        }, 'CISCO-CLASS-BASED-QOS-MIB', _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB']),
    'InterfaceType_Enum' : _MetaInfoEnum('InterfaceType_Enum', 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB',
        {
            'mainInterface':'MAININTERFACE',
            'subInterface':'SUBINTERFACE',
            'frDLCI':'FRDLCI',
            'atmPVC':'ATMPVC',
            'controlPlane':'CONTROLPLANE',
            'vlanPort':'VLANPORT',
            'evc':'EVC',
        }, 'CISCO-CLASS-BASED-QOS-MIB', _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB']),
    'QosClassInfo_Enum' : _MetaInfoEnum('QosClassInfo_Enum', 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB',
        {
            'none':'NONE',
            'matchAll':'MATCHALL',
            'matchAny':'MATCHANY',
        }, 'CISCO-CLASS-BASED-QOS-MIB', _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB']),
    'REDMechanism_Enum' : _MetaInfoEnum('REDMechanism_Enum', 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB',
        {
            'precedence':'PRECEDENCE',
            'dscp':'DSCP',
            'discardClass':'DISCARDCLASS',
            'l2Cos':'L2COS',
            'atmClp':'ATMCLP',
            'mplsExp':'MPLSEXP',
            'redDefault':'REDDEFAULT',
            'redUserDefault':'REDUSERDEFAULT',
            'dei':'DEI',
        }, 'CISCO-CLASS-BASED-QOS-MIB', _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB']),
    'CbQosRateType_Enum' : _MetaInfoEnum('CbQosRateType_Enum', 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB',
        {
            'bps':'BPS',
            'percentage':'PERCENTAGE',
            'cps':'CPS',
            'perThousand':'PERTHOUSAND',
            'perMillion':'PERMILLION',
        }, 'CISCO-CLASS-BASED-QOS-MIB', _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB']),
    'QueueingBandwidthUnits_Enum' : _MetaInfoEnum('QueueingBandwidthUnits_Enum', 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB',
        {
            'kbps':'KBPS',
            'percentage':'PERCENTAGE',
            'percentageRemaining':'PERCENTAGEREMAINING',
            'ratioRemaining':'RATIOREMAINING',
            'perThousand':'PERTHOUSAND',
            'perMillion':'PERMILLION',
        }, 'CISCO-CLASS-BASED-QOS-MIB', _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB']),
    'CISCOCLASSBASEDQOSMIB.CbQosATMPVCPolicyTable.CbQosATMPVCPolicyEntry' : {
        'meta_info' : _MetaInfoClass('CISCOCLASSBASEDQOSMIB.CbQosATMPVCPolicyTable.CbQosATMPVCPolicyEntry',
            False, 
            [
            _MetaInfoClassMember('cbQosAtmVCI', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                ''',
                'cbqosatmvci',
                'CISCO-CLASS-BASED-QOS-MIB', True),
            _MetaInfoClassMember('cbQosAtmVPI', ATTRIBUTE, 'int' , None, None, 
                [(0, 4095)], [], 
                '''                ''',
                'cbqosatmvpi',
                'CISCO-CLASS-BASED-QOS-MIB', True),
            _MetaInfoClassMember('cbQosPolicyDirection', REFERENCE_ENUM_CLASS, 'TrafficDirection_Enum' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'TrafficDirection_Enum', 
                [], [], 
                '''                ''',
                'cbqospolicydirection',
                'CISCO-CLASS-BASED-QOS-MIB', True),
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'ifindex',
                'CISCO-CLASS-BASED-QOS-MIB', True),
            _MetaInfoClassMember('cbQosATMPolicyIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                An arbitrary (system-assigned) index for all
                Service Policies.
                
                This is identical to cbQosPolicyIndex.
                ''',
                'cbqosatmpolicyindex',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            ],
            'CISCO-CLASS-BASED-QOS-MIB',
            'cbQosATMPVCPolicyEntry',
            _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB'],
        'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB'
        ),
    },
    'CISCOCLASSBASEDQOSMIB.CbQosATMPVCPolicyTable' : {
        'meta_info' : _MetaInfoClass('CISCOCLASSBASEDQOSMIB.CbQosATMPVCPolicyTable',
            False, 
            [
            _MetaInfoClassMember('cbQosATMPVCPolicyEntry', REFERENCE_LIST, 'CbQosATMPVCPolicyEntry' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CISCOCLASSBASEDQOSMIB.CbQosATMPVCPolicyTable.CbQosATMPVCPolicyEntry', 
                [], [], 
                '''                Using ifIndex, VPI, VCI, and Direction, each unique
                index combination translates to a service policy that 
                is attached to a ATM VC, for particular traffic direction.
                ''',
                'cbqosatmpvcpolicyentry',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            ],
            'CISCO-CLASS-BASED-QOS-MIB',
            'cbQosATMPVCPolicyTable',
            _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB'],
        'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB'
        ),
    },
    'CISCOCLASSBASEDQOSMIB.CbQosC3plAccountCfgTable.CbQosC3plAccountCfgEntry' : {
        'meta_info' : _MetaInfoClass('CISCOCLASSBASEDQOSMIB.CbQosC3plAccountCfgTable.CbQosC3plAccountCfgEntry',
            False, 
            [
            _MetaInfoClassMember('cbQosConfigIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ''',
                'cbqosconfigindex',
                'CISCO-CLASS-BASED-QOS-MIB', True),
            _MetaInfoClassMember('cbQosC3plAccountFeatureType', REFERENCE_ENUM_CLASS, 'SetC3plAccountFeatureType_Enum' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'SetC3plAccountFeatureType_Enum', 
                [], [], 
                '''                The feature type is used to indicated different drop
                statistics.
                ''',
                'cbqosc3placcountfeaturetype',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            ],
            'CISCO-CLASS-BASED-QOS-MIB',
            'cbQosC3plAccountCfgEntry',
            _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB'],
        'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB'
        ),
    },
    'CISCOCLASSBASEDQOSMIB.CbQosC3plAccountCfgTable' : {
        'meta_info' : _MetaInfoClass('CISCOCLASSBASEDQOSMIB.CbQosC3plAccountCfgTable',
            False, 
            [
            _MetaInfoClassMember('cbQosC3plAccountCfgEntry', REFERENCE_LIST, 'CbQosC3plAccountCfgEntry' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CISCOCLASSBASEDQOSMIB.CbQosC3plAccountCfgTable.CbQosC3plAccountCfgEntry', 
                [], [], 
                '''                Each entry in this table describes configuration
                information about a c3pl account action. The information
                includes: feature type.
                
                This table contains configuration information only,
                no statistics associated with it. Therefore, it is indexed
                by the cbQosConfigIndex of each C3pl Account Action.
                ''',
                'cbqosc3placcountcfgentry',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            ],
            'CISCO-CLASS-BASED-QOS-MIB',
            'cbQosC3plAccountCfgTable',
            _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB'],
        'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB'
        ),
    },
    'CISCOCLASSBASEDQOSMIB.CbQosC3plAccountStatsTable.CbQosC3plAccountStatsEntry' : {
        'meta_info' : _MetaInfoClass('CISCOCLASSBASEDQOSMIB.CbQosC3plAccountStatsTable.CbQosC3plAccountStatsEntry',
            False, 
            [
            _MetaInfoClassMember('cbQosC3plAccountFeatureType', REFERENCE_ENUM_CLASS, 'SetC3plAccountFeatureType_Enum' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'SetC3plAccountFeatureType_Enum', 
                [], [], 
                '''                ''',
                'cbqosc3placcountfeaturetype',
                'CISCO-CLASS-BASED-QOS-MIB', True),
            _MetaInfoClassMember('cbQosObjectsIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ''',
                'cbqosobjectsindex',
                'CISCO-CLASS-BASED-QOS-MIB', True),
            _MetaInfoClassMember('cbQosPolicyIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ''',
                'cbqospolicyindex',
                'CISCO-CLASS-BASED-QOS-MIB', True),
            _MetaInfoClassMember('cbQosC3plAccountDropByte', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The lower 32 bits count of bytes dropped when
                the number of packets in the associated queue was
                greater than the minimum threshold and less than the
                maximum threshold.
                ''',
                'cbqosc3placcountdropbyte',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosC3plAccountDropByte64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The 64 bits count of bytes dropped when the number of
                packets in the associated queue was greater
                than the minimum threshold and less than the
                maximum threshold.
                ''',
                'cbqosc3placcountdropbyte64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosC3plAccountDropByteOverflow', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The upper 32 bits count of bytes dropped when the
                number of packets in the associated queue was greater
                than the minimum threshold and less than the
                maximum threshold.
                ''',
                'cbqosc3placcountdropbyteoverflow',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosC3plAccountDropPkt', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The lower 32 bits count of packets dropped when
                the number of packets in the associated queue was
                greater than the minimum threshold and less than the
                maximum threshold.
                ''',
                'cbqosc3placcountdroppkt',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosC3plAccountDropPkt64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The 64 bits count of packets dropped when the number
                of packets in the associated queue was greater
                than the minimum threshold and less than the
                maximum threshold.
                ''',
                'cbqosc3placcountdroppkt64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosC3plAccountDropPktOverflow', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The upper 32 bits count of packets dropped when the
                number of packets in the associated queue was greater
                than the minimum threshold and less than the
                maximum threshold.
                ''',
                'cbqosc3placcountdroppktoverflow',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosC3plAccountTailDropByte', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The lower 32 bits count of bytes dropped when the
                number of packets in the associated queue was greater
                than the maximum threshold.
                ''',
                'cbqosc3placcounttaildropbyte',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosC3plAccountTailDropByte64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The 64 bits count of bytes dropped when the number of
                packets in the associated queue was greater
                than the maximum threshold.
                ''',
                'cbqosc3placcounttaildropbyte64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosC3plAccountTailDropByteOverflow', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The upper 32 bits count of bytes dropped when the
                number of packets in the associated queue was greater
                than the maximum threshold.
                ''',
                'cbqosc3placcounttaildropbyteoverflow',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosC3plAccountTailDropPkt', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The lower 32 bits count of packets dropped when the
                number of packets in the associated queue was greater
                than the maximum threshold.
                ''',
                'cbqosc3placcounttaildroppkt',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosC3plAccountTailDropPkt64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The 64 bits count of packets dropped when the number
                of packets in the associated queue was greater
                than the maximum threshold.
                ''',
                'cbqosc3placcounttaildroppkt64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosC3plAccountTailDropPktOverflow', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The upper 32 bits count of packets dropped when the
                number of packets in the associated queue was greater
                than the maximum threshold.
                ''',
                'cbqosc3placcounttaildroppktoverflow',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            ],
            'CISCO-CLASS-BASED-QOS-MIB',
            'cbQosC3plAccountStatsEntry',
            _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB'],
        'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB'
        ),
    },
    'CISCOCLASSBASEDQOSMIB.CbQosC3plAccountStatsTable' : {
        'meta_info' : _MetaInfoClass('CISCOCLASSBASEDQOSMIB.CbQosC3plAccountStatsTable',
            False, 
            [
            _MetaInfoClassMember('cbQosC3plAccountStatsEntry', REFERENCE_LIST, 'CbQosC3plAccountStatsEntry' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CISCOCLASSBASEDQOSMIB.CbQosC3plAccountStatsTable.CbQosC3plAccountStatsEntry', 
                [], [], 
                '''                Each entry in this table describes the statistical
                information about C3pl Account Action. Account action
                specific information you can find in this table are :
                queueing drop pkt/byte counters, wred drop pkt/byte
                counters, police pkt/byte counters.
                
                This table contains statistical information only,
                no configuration information associated with it.
                Therefore, it is indexed by the instance specific IDs,
                such as cbQosPolicyIndex, cbQosObjectsIndex, and
                cbQosC3plAccountFeatureType.
                ''',
                'cbqosc3placcountstatsentry',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            ],
            'CISCO-CLASS-BASED-QOS-MIB',
            'cbQosC3plAccountStatsTable',
            _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB'],
        'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB'
        ),
    },
    'CISCOCLASSBASEDQOSMIB.CbQosCMCfgTable.CbQosCMCfgEntry' : {
        'meta_info' : _MetaInfoClass('CISCOCLASSBASEDQOSMIB.CbQosCMCfgTable.CbQosCMCfgEntry',
            False, 
            [
            _MetaInfoClassMember('cbQosConfigIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ''',
                'cbqosconfigindex',
                'CISCO-CLASS-BASED-QOS-MIB', True),
            _MetaInfoClassMember('cbQosCMDesc', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                Description of the Classmap.
                ''',
                'cbqoscmdesc',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosCMInfo', REFERENCE_ENUM_CLASS, 'QosClassInfo_Enum' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'QosClassInfo_Enum', 
                [], [], 
                '''                Match all vs Match any in a given class.
                ''',
                'cbqoscminfo',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosCMName', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                Name of the Classmap.
                ''',
                'cbqoscmname',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            ],
            'CISCO-CLASS-BASED-QOS-MIB',
            'cbQosCMCfgEntry',
            _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB'],
        'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB'
        ),
    },
    'CISCOCLASSBASEDQOSMIB.CbQosCMCfgTable' : {
        'meta_info' : _MetaInfoClass('CISCOCLASSBASEDQOSMIB.CbQosCMCfgTable',
            False, 
            [
            _MetaInfoClassMember('cbQosCMCfgEntry', REFERENCE_LIST, 'CbQosCMCfgEntry' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CISCOCLASSBASEDQOSMIB.CbQosCMCfgTable.CbQosCMCfgEntry', 
                [], [], 
                '''                Each entry in this table describes configuration information
                about a classmap. The information includes: Name, and it's
                description and whether it is a Match-All or Match-Any
                class. This table contains configuration information only,
                no statistics associated with it. Therefore, it is indexed
                by the cbQosConfigIndex of each ClassMap.
                ''',
                'cbqoscmcfgentry',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            ],
            'CISCO-CLASS-BASED-QOS-MIB',
            'cbQosCMCfgTable',
            _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB'],
        'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB'
        ),
    },
    'CISCOCLASSBASEDQOSMIB.CbQosCMStatsTable.CbQosCMStatsEntry' : {
        'meta_info' : _MetaInfoClass('CISCOCLASSBASEDQOSMIB.CbQosCMStatsTable.CbQosCMStatsEntry',
            False, 
            [
            _MetaInfoClassMember('cbQosObjectsIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ''',
                'cbqosobjectsindex',
                'CISCO-CLASS-BASED-QOS-MIB', True),
            _MetaInfoClassMember('cbQosPolicyIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ''',
                'cbqospolicyindex',
                'CISCO-CLASS-BASED-QOS-MIB', True),
            _MetaInfoClassMember('cbQosCMDropBitRate', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The bit rate of the drops per class as the result of
                all features that can produce drops 
                (e.g., police, random detect, etc.).
                ''',
                'cbqoscmdropbitrate',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosCMDropBitRate64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The bit rate of the drops per class as the result of
                all features that can produce drops 
                (e.g., police, random detect, etc.). This object is a
                64-bit version of cbQosCMDropBitRate.
                ''',
                'cbqoscmdropbitrate64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosCMDropByte', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The lower 32 bits counter of dropped bytes per class
                as the result of all features that can produce drops 
                (e.g., police, random detect, etc.).
                ''',
                'cbqoscmdropbyte',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosCMDropByte64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The 64 bits counter of dropped bytes per class as the
                result of all features that can produce drops 
                 (e.g., police, random detect, etc.).
                ''',
                'cbqoscmdropbyte64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosCMDropByteOverflow', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The upper 32 bits counter of dropped bytes per class
                as the result of all features that can produce drops 
                (e.g., police, random detect, etc.).
                ''',
                'cbqoscmdropbyteoverflow',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosCMDropPkt', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The lower 32 bits counter of dropped pkts per class
                as the result of all features that can produce drops 
                (e.g., police, random detect, etc.).
                ''',
                'cbqoscmdroppkt',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosCMDropPkt64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The 64 bits counter of dropped pkts per class as
                the result of all features that can produce drops 
                 (e.g., police, random detect, etc.).
                ''',
                'cbqoscmdroppkt64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosCMDropPktOverflow', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The upper 32 bits counter of dropped pkts per class
                as the result of all features that can produce drops 
                (e.g., police, random detect, etc.).
                ''',
                'cbqoscmdroppktoverflow',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosCMFragmentByte', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The lower 32 bits counter for aggregate fragment bytes
                ''',
                'cbqoscmfragmentbyte',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosCMFragmentByte64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The 64 bits counter for aggregate fragment bytes
                ''',
                'cbqoscmfragmentbyte64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosCMFragmentByteOverflow', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The upper 32 bits counter for aggregate fragment bytes
                ''',
                'cbqoscmfragmentbyteoverflow',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosCMFragmentPkt', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The lower 32 bits counter for aggregate fragment pkts
                ''',
                'cbqoscmfragmentpkt',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosCMFragmentPkt64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The 64 bits counter for aggregate fragment pkts
                ''',
                'cbqoscmfragmentpkt64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosCMFragmentPktOverflow', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The upper 32 bits counter for aggregate fragment pkts
                ''',
                'cbqoscmfragmentpktoverflow',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosCMNoBufDropPkt', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The lower 32 bits drop packet count which occured due
                to a lack of SRAM buffers during output processing on 
                an interface.
                ''',
                'cbqoscmnobufdroppkt',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosCMNoBufDropPkt64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The 64 bits drop packet count which occured due to a
                lack of SRAM buffers during output processing on an 
                interface.
                ''',
                'cbqoscmnobufdroppkt64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosCMNoBufDropPktOverflow', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The upper 32 bits drop packet count which occured
                due to a lack of SRAM buffers during output processing 
                on an interface.
                ''',
                'cbqoscmnobufdroppktoverflow',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosCMPostPolicyBitRate', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The bit rate of the traffic after executing QoS
                policies.
                ''',
                'cbqoscmpostpolicybitrate',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosCMPostPolicyBitRate64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The bit rate of the traffic after executing QoS
                policies. This object is a 64-bit version of
                cbQosCMPostPolicyBitRate.
                ''',
                'cbqoscmpostpolicybitrate64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosCMPostPolicyByte', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The lower 32 bits count of outbound octets after executing
                QoS policies.
                ''',
                'cbqoscmpostpolicybyte',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosCMPostPolicyByte64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The 64 bits count of outbound octets after executing
                QoS policies.
                ''',
                'cbqoscmpostpolicybyte64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosCMPostPolicyByteOverflow', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The upper 32 bits count of outbound octets after executing
                QoS policies.
                ''',
                'cbqoscmpostpolicybyteoverflow',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosCMPrePolicyBitRate', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The bit rate of the traffic prior to executing any QoS
                policies.
                ''',
                'cbqoscmprepolicybitrate',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosCMPrePolicyBitRate64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The bit rate of the traffic prior to executing any QoS
                policies.This object is a 64-bit version of
                cbQosCMPrePolicyBitRate.
                ''',
                'cbqoscmprepolicybitrate64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosCMPrePolicyByte', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The lower 32 bits count of inbound octets prior to
                executing any QoS policies.
                ''',
                'cbqoscmprepolicybyte',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosCMPrePolicyByte64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The 64 bits count of inbound octets prior to executing
                any QoS policies.
                ''',
                'cbqoscmprepolicybyte64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosCMPrePolicyByteOverflow', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The upper 32 bits count of inbound octets prior to
                executing any QoS policies.
                ''',
                'cbqoscmprepolicybyteoverflow',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosCMPrePolicyPkt', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The lower 32 bits count of inbound packets prior to
                executing any QoS policies.
                ''',
                'cbqoscmprepolicypkt',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosCMPrePolicyPkt64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The 64 bits count of inbound packets prior to executing
                any QoS policies.
                ''',
                'cbqoscmprepolicypkt64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosCMPrePolicyPktOverflow', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The upper 32 bits count of inbound packets prior to
                executing any QoS policies.
                ''',
                'cbqoscmprepolicypktoverflow',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            ],
            'CISCO-CLASS-BASED-QOS-MIB',
            'cbQosCMStatsEntry',
            _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB'],
        'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB'
        ),
    },
    'CISCOCLASSBASEDQOSMIB.CbQosCMStatsTable' : {
        'meta_info' : _MetaInfoClass('CISCOCLASSBASEDQOSMIB.CbQosCMStatsTable',
            False, 
            [
            _MetaInfoClassMember('cbQosCMStatsEntry', REFERENCE_LIST, 'CbQosCMStatsEntry' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CISCOCLASSBASEDQOSMIB.CbQosCMStatsTable.CbQosCMStatsEntry', 
                [], [], 
                '''                Each entry in this table describes the statistical
                information about ClassMap. ClassMap specific information
                you can find in this table are : pre/post policy pkt/byte
                counts, bit rates, drop pkt/bytes and no buffer drops.
                
                This table contains statistical information only,
                no configuration information associated with it. Therefore, 
                it is indexed by the instance specific IDs, such as 
                cbQosPolicyIndex and cbQosObjectsIndex.
                ''',
                'cbqoscmstatsentry',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            ],
            'CISCO-CLASS-BASED-QOS-MIB',
            'cbQosCMStatsTable',
            _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB'],
        'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB'
        ),
    },
    'CISCOCLASSBASEDQOSMIB.CbQosEBCfgTable.CbQosEBCfgEntry' : {
        'meta_info' : _MetaInfoClass('CISCOCLASSBASEDQOSMIB.CbQosEBCfgTable.CbQosEBCfgEntry',
            False, 
            [
            _MetaInfoClassMember('cbQosConfigIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ''',
                'cbqosconfigindex',
                'CISCO-CLASS-BASED-QOS-MIB', True),
            _MetaInfoClassMember('cbQosEBCfgDelayTarget', ATTRIBUTE, 'int' , None, None, 
                [(50, 1000000)], [], 
                '''                One-in-Number target indicating that no more than
                one packet in (this) number will exceed the delay 
                threshold specified by cbQosEBCfgDelayThreshold.
                ''',
                'cbqosebcfgdelaytarget',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosEBCfgDelayThreshold', ATTRIBUTE, 'int' , None, None, 
                [(16, 1000)], [], 
                '''                The time in milliseconds for the delay threshold.
                ''',
                'cbqosebcfgdelaythreshold',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosEBCfgDropTarget', ATTRIBUTE, 'int' , None, None, 
                [(50, 1000000)], [], 
                '''                One-in-Number target indicating that no more than
                one packet in (this) number will be dropped.
                ''',
                'cbqosebcfgdroptarget',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosEBCfgMechanism', REFERENCE_ENUM_CLASS, 'CbQosEBType_Enum' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CbQosEBType_Enum', 
                [], [], 
                '''                Bandwidth estimate algorithm type.
                ''',
                'cbqosebcfgmechanism',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            ],
            'CISCO-CLASS-BASED-QOS-MIB',
            'cbQosEBCfgEntry',
            _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB'],
        'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB'
        ),
    },
    'CISCOCLASSBASEDQOSMIB.CbQosEBCfgTable' : {
        'meta_info' : _MetaInfoClass('CISCOCLASSBASEDQOSMIB.CbQosEBCfgTable',
            False, 
            [
            _MetaInfoClassMember('cbQosEBCfgEntry', REFERENCE_LIST, 'CbQosEBCfgEntry' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CISCOCLASSBASEDQOSMIB.CbQosEBCfgTable.CbQosEBCfgEntry', 
                [], [], 
                '''                Each entry in this table describes configuration
                information about Estimate Bandwidth. It includes: 
                drop target, delay target and delay threshold.
                
                This table contains configuration information only.
                It is indexed by the cbQosConfigIndex.
                ''',
                'cbqosebcfgentry',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            ],
            'CISCO-CLASS-BASED-QOS-MIB',
            'cbQosEBCfgTable',
            _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB'],
        'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB'
        ),
    },
    'CISCOCLASSBASEDQOSMIB.CbQosEBStatsTable.CbQosEBStatsEntry' : {
        'meta_info' : _MetaInfoClass('CISCOCLASSBASEDQOSMIB.CbQosEBStatsTable.CbQosEBStatsEntry',
            False, 
            [
            _MetaInfoClassMember('cbQosObjectsIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ''',
                'cbqosobjectsindex',
                'CISCO-CLASS-BASED-QOS-MIB', True),
            _MetaInfoClassMember('cbQosPolicyIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ''',
                'cbqospolicyindex',
                'CISCO-CLASS-BASED-QOS-MIB', True),
            _MetaInfoClassMember('cbQosEBStatsCorvilCTD', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The Corvil CTD value defined by CbQosEBCtd.
                ''',
                'cbqosebstatscorvilctd',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosEBStatsCorvilEBStatus', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Boolean to indicate if Corvil EB is ready.
                true  - Bandwidth estimate is available.
                false - Bandwidth estimate is not available.
                ''',
                'cbqosebstatscorvilebstatus',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosEBStatsCorvilEBValue', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The current Corvil EB bandwidth value.
                ''',
                'cbqosebstatscorvilebvalue',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            ],
            'CISCO-CLASS-BASED-QOS-MIB',
            'cbQosEBStatsEntry',
            _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB'],
        'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB'
        ),
    },
    'CISCOCLASSBASEDQOSMIB.CbQosEBStatsTable' : {
        'meta_info' : _MetaInfoClass('CISCOCLASSBASEDQOSMIB.CbQosEBStatsTable',
            False, 
            [
            _MetaInfoClassMember('cbQosEBStatsEntry', REFERENCE_LIST, 'CbQosEBStatsEntry' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CISCOCLASSBASEDQOSMIB.CbQosEBStatsTable.CbQosEBStatsEntry', 
                [], [], 
                '''                Each entry in this table describes Estimate Bandwidth
                related statistical information.
                ''',
                'cbqosebstatsentry',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            ],
            'CISCO-CLASS-BASED-QOS-MIB',
            'cbQosEBStatsTable',
            _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB'],
        'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB'
        ),
    },
    'CISCOCLASSBASEDQOSMIB.CbQosFrameRelayPolicyTable.CbQosFrameRelayPolicyEntry' : {
        'meta_info' : _MetaInfoClass('CISCOCLASSBASEDQOSMIB.CbQosFrameRelayPolicyTable.CbQosFrameRelayPolicyEntry',
            False, 
            [
            _MetaInfoClassMember('cbQosFrDLCI', ATTRIBUTE, 'int' , None, None, 
                [(0, 1023)], [], 
                '''                ''',
                'cbqosfrdlci',
                'CISCO-CLASS-BASED-QOS-MIB', True),
            _MetaInfoClassMember('cbQosPolicyDirection', REFERENCE_ENUM_CLASS, 'TrafficDirection_Enum' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'TrafficDirection_Enum', 
                [], [], 
                '''                ''',
                'cbqospolicydirection',
                'CISCO-CLASS-BASED-QOS-MIB', True),
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'ifindex',
                'CISCO-CLASS-BASED-QOS-MIB', True),
            _MetaInfoClassMember('cbQosFRPolicyIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                An arbitrary (system-assigned) index for all
                Service Policies.
                
                This is identical to cbQosPolicyIndex.
                ''',
                'cbqosfrpolicyindex',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            ],
            'CISCO-CLASS-BASED-QOS-MIB',
            'cbQosFrameRelayPolicyEntry',
            _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB'],
        'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB'
        ),
    },
    'CISCOCLASSBASEDQOSMIB.CbQosFrameRelayPolicyTable' : {
        'meta_info' : _MetaInfoClass('CISCOCLASSBASEDQOSMIB.CbQosFrameRelayPolicyTable',
            False, 
            [
            _MetaInfoClassMember('cbQosFrameRelayPolicyEntry', REFERENCE_LIST, 'CbQosFrameRelayPolicyEntry' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CISCOCLASSBASEDQOSMIB.CbQosFrameRelayPolicyTable.CbQosFrameRelayPolicyEntry', 
                [], [], 
                '''                Using ifIndex, FR DLCI, and Direction, each unique
                index combination translates to a service policy that 
                is attached to a FR DLCI, for particular traffic direction.
                ''',
                'cbqosframerelaypolicyentry',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            ],
            'CISCO-CLASS-BASED-QOS-MIB',
            'cbQosFrameRelayPolicyTable',
            _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB'],
        'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB'
        ),
    },
    'CISCOCLASSBASEDQOSMIB.CbQosIPHCCfgTable.CbQosIPHCCfgEntry' : {
        'meta_info' : _MetaInfoClass('CISCOCLASSBASEDQOSMIB.CbQosIPHCCfgTable.CbQosIPHCCfgEntry',
            False, 
            [
            _MetaInfoClassMember('cbQosConfigIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ''',
                'cbqosconfigindex',
                'CISCO-CLASS-BASED-QOS-MIB', True),
            _MetaInfoClassMember('cbQosIPHCCfgEnabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Boolean to indicate if IPHC is enabled for policy class.
                ''',
                'cbqosiphccfgenabled',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosIPHCCfgOption', REFERENCE_ENUM_CLASS, 'IPHCOption_Enum' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'IPHCOption_Enum', 
                [], [], 
                '''                The configured IP header compression option.
                The value is defined by IPHCOption.
                ''',
                'cbqosiphccfgoption',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            ],
            'CISCO-CLASS-BASED-QOS-MIB',
            'cbQosIPHCCfgEntry',
            _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB'],
        'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB'
        ),
    },
    'CISCOCLASSBASEDQOSMIB.CbQosIPHCCfgTable' : {
        'meta_info' : _MetaInfoClass('CISCOCLASSBASEDQOSMIB.CbQosIPHCCfgTable',
            False, 
            [
            _MetaInfoClassMember('cbQosIPHCCfgEntry', REFERENCE_LIST, 'CbQosIPHCCfgEntry' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CISCOCLASSBASEDQOSMIB.CbQosIPHCCfgTable.CbQosIPHCCfgEntry', 
                [], [], 
                '''                Each entry in this table describes configuration
                information about IP Header compression. This
                includes the compression option of UDP/RTP header,
                TCP header or both.
                
                This table contains configuration information only,
                no statistics associated with it. Therefore, it is
                indexed by cbQosConfigIndex.
                ''',
                'cbqosiphccfgentry',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            ],
            'CISCO-CLASS-BASED-QOS-MIB',
            'cbQosIPHCCfgTable',
            _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB'],
        'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB'
        ),
    },
    'CISCOCLASSBASEDQOSMIB.CbQosIPHCStatsTable.CbQosIPHCStatsEntry' : {
        'meta_info' : _MetaInfoClass('CISCOCLASSBASEDQOSMIB.CbQosIPHCStatsTable.CbQosIPHCStatsEntry',
            False, 
            [
            _MetaInfoClassMember('cbQosObjectsIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ''',
                'cbqosobjectsindex',
                'CISCO-CLASS-BASED-QOS-MIB', True),
            _MetaInfoClassMember('cbQosPolicyIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ''',
                'cbqospolicyindex',
                'CISCO-CLASS-BASED-QOS-MIB', True),
            _MetaInfoClassMember('cbQosIPHCRtpCmprsOutPkt', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The lower 32 bits count of outbound compressed
                UDP/RTP packets.
                ''',
                'cbqosiphcrtpcmprsoutpkt',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosIPHCRtpCmprsOutPkt64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The 64 bits count of outbound compressed
                UDP/RTP packets.
                ''',
                'cbqosiphcrtpcmprsoutpkt64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosIPHCRtpCmprsOutPktOverflow', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The upper 32 bits count of outbound compressed
                UDP/RTP packets.
                ''',
                'cbqosiphcrtpcmprsoutpktoverflow',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosIPHCRtpFullHdrSentPkt', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The lower 32 bits count of total full header UDP/RTP packets
                sent out.
                ''',
                'cbqosiphcrtpfullhdrsentpkt',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosIPHCRtpFullHdrSentPkt64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The 64 bits count of total fullheader UDP/RTP packets sent
                out.
                ''',
                'cbqosiphcrtpfullhdrsentpkt64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosIPHCRtpFullHdrSentPktOverflow', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The upper 32 bits count of total full header UDP/RTP packets
                sent out.
                ''',
                'cbqosiphcrtpfullhdrsentpktoverflow',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosIPHCRtpSavedByte', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The lower 32 bits count of UDP/RTP bytes that
                saved due to IPHC.
                ''',
                'cbqosiphcrtpsavedbyte',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosIPHCRtpSavedByte64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The 64 bits count of UDP/RTP bytes that saved
                due to IPHC.
                ''',
                'cbqosiphcrtpsavedbyte64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosIPHCRtpSavedByteOverflow', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The upper 32 bits count of UDP/RTP bytes that
                saved due to IPHC.
                ''',
                'cbqosiphcrtpsavedbyteoverflow',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosIPHCRtpSentByte', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The lower 32 bits count of outbound UDP/RTP
                bytes.
                ''',
                'cbqosiphcrtpsentbyte',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosIPHCRtpSentByte64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The 64 bits count of outbound UDP/RTP bytes.
                ''',
                'cbqosiphcrtpsentbyte64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosIPHCRtpSentByteOverflow', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The upper 32 bits count of outbound UDP/RTP
                bytes.
                ''',
                'cbqosiphcrtpsentbyteoverflow',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosIPHCRtpSentByteRate', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The 32 bits count of outbound UDP/RTP byte rate.
                ''',
                'cbqosiphcrtpsentbyterate',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosIPHCRtpSentPkt', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The lower 32 bits count of outbound UDP/RTP packets.
                ''',
                'cbqosiphcrtpsentpkt',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosIPHCRtpSentPkt64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The 64 bits count of outbound UDP/RTP packets.
                ''',
                'cbqosiphcrtpsentpkt64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosIPHCRtpSentPktOverflow', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The upper 32 bits count of outbound UDP/RTP packets.
                ''',
                'cbqosiphcrtpsentpktoverflow',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosIPHCTcpCmprsOutPkt', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The lower 32 bits count of outbound compressed
                TCP packets.
                ''',
                'cbqosiphctcpcmprsoutpkt',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosIPHCTcpCmprsOutPkt64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The 64 bits count of outbound compressed TCP
                packets.
                ''',
                'cbqosiphctcpcmprsoutpkt64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosIPHCTcpCmprsOutPktOverflow', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The upper 32 bits count of outbound compressed
                TCP packets.
                ''',
                'cbqosiphctcpcmprsoutpktoverflow',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosIPHCTcpFullHdrSentPkt', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The lower 32 bits count of total fullheader TCP packets sent
                out.
                ''',
                'cbqosiphctcpfullhdrsentpkt',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosIPHCTcpFullHdrSentPkt64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The 64 bits count of total fullheader TCP packets sent out.
                ''',
                'cbqosiphctcpfullhdrsentpkt64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosIPHCTcpFullHdrSentPktOverflow', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The upper 32 bits count of total fullheader TCP packets sent
                out.
                ''',
                'cbqosiphctcpfullhdrsentpktoverflow',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosIPHCTcpSavedByte', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The lower 32 bits count of TCP bytes that saved
                due to IPHC.
                ''',
                'cbqosiphctcpsavedbyte',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosIPHCTcpSavedByte64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The 64 bits count of TCP bytes that saved due
                to IPHC.
                ''',
                'cbqosiphctcpsavedbyte64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosIPHCTcpSavedByteOverflow', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The upper 32 bits count of TCP bytes that saved
                due to IPHC.
                ''',
                'cbqosiphctcpsavedbyteoverflow',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosIPHCTcpSentByte', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The lower 32 bits count of outbound TCP bytes.
                ''',
                'cbqosiphctcpsentbyte',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosIPHCTcpSentByte64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The 64 bits count of outbound TCP bytes.
                ''',
                'cbqosiphctcpsentbyte64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosIPHCTcpSentByteOverflow', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The upper 32 bits count of outbound TCP bytes.
                ''',
                'cbqosiphctcpsentbyteoverflow',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosIPHCTcpSentByteRate', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The 32 bits count of outbound TCP byte rate.
                ''',
                'cbqosiphctcpsentbyterate',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosIPHCTcpSentPkt', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The lower 32 bits count of outbound TCP packets.
                ''',
                'cbqosiphctcpsentpkt',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosIPHCTcpSentPkt64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The 64 bits count of outbound TCP packets.
                ''',
                'cbqosiphctcpsentpkt64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosIPHCTcpSentPktOverflow', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The upper 32 bits count of outbound TCP packets.
                ''',
                'cbqosiphctcpsentpktoverflow',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            ],
            'CISCO-CLASS-BASED-QOS-MIB',
            'cbQosIPHCStatsEntry',
            _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB'],
        'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB'
        ),
    },
    'CISCOCLASSBASEDQOSMIB.CbQosIPHCStatsTable' : {
        'meta_info' : _MetaInfoClass('CISCOCLASSBASEDQOSMIB.CbQosIPHCStatsTable',
            False, 
            [
            _MetaInfoClassMember('cbQosIPHCStatsEntry', REFERENCE_LIST, 'CbQosIPHCStatsEntry' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CISCOCLASSBASEDQOSMIB.CbQosIPHCStatsTable.CbQosIPHCStatsEntry', 
                [], [], 
                '''                Each entry in this table describes statistical
                information about IP Header compression.
                
                This table contains statistical information only,
                no configuration information associated with it.
                Therefore, it is indexed by the instance specific IDs,
                namely cbQosPolicyIndex and cbQosObjectsIndex.
                ''',
                'cbqosiphcstatsentry',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            ],
            'CISCO-CLASS-BASED-QOS-MIB',
            'cbQosIPHCStatsTable',
            _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB'],
        'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB'
        ),
    },
    'CISCOCLASSBASEDQOSMIB.CbQosInterfacePolicyTable.CbQosInterfacePolicyEntry' : {
        'meta_info' : _MetaInfoClass('CISCOCLASSBASEDQOSMIB.CbQosInterfacePolicyTable.CbQosInterfacePolicyEntry',
            False, 
            [
            _MetaInfoClassMember('cbQosPolicyDirection', REFERENCE_ENUM_CLASS, 'TrafficDirection_Enum' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'TrafficDirection_Enum', 
                [], [], 
                '''                ''',
                'cbqospolicydirection',
                'CISCO-CLASS-BASED-QOS-MIB', True),
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'ifindex',
                'CISCO-CLASS-BASED-QOS-MIB', True),
            _MetaInfoClassMember('cbQosIFPolicyIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                An arbitrary (system-assigned) index for all
                Service Policies. 
                
                This is identical to cbQosPolicyIndex.
                ''',
                'cbqosifpolicyindex',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            ],
            'CISCO-CLASS-BASED-QOS-MIB',
            'cbQosInterfacePolicyEntry',
            _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB'],
        'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB'
        ),
    },
    'CISCOCLASSBASEDQOSMIB.CbQosInterfacePolicyTable' : {
        'meta_info' : _MetaInfoClass('CISCOCLASSBASEDQOSMIB.CbQosInterfacePolicyTable',
            False, 
            [
            _MetaInfoClassMember('cbQosInterfacePolicyEntry', REFERENCE_LIST, 'CbQosInterfacePolicyEntry' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CISCOCLASSBASEDQOSMIB.CbQosInterfacePolicyTable.CbQosInterfacePolicyEntry', 
                [], [], 
                '''                Using ifIndex and Direction, each unique index pair
                translates to a service policy that is attached to a 
                main/sub interface, for particular traffic direction.
                ''',
                'cbqosinterfacepolicyentry',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            ],
            'CISCO-CLASS-BASED-QOS-MIB',
            'cbQosInterfacePolicyTable',
            _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB'],
        'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB'
        ),
    },
    'CISCOCLASSBASEDQOSMIB.CbQosMatchStmtCfgTable.CbQosMatchStmtCfgEntry' : {
        'meta_info' : _MetaInfoClass('CISCOCLASSBASEDQOSMIB.CbQosMatchStmtCfgTable.CbQosMatchStmtCfgEntry',
            False, 
            [
            _MetaInfoClassMember('cbQosConfigIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ''',
                'cbqosconfigindex',
                'CISCO-CLASS-BASED-QOS-MIB', True),
            _MetaInfoClassMember('cbQosMatchStmtInfo', REFERENCE_ENUM_CLASS, 'QosMatchInfo_Enum' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'QosMatchInfo_Enum', 
                [], [], 
                '''                Match vs Match Not in a given class.
                ''',
                'cbqosmatchstmtinfo',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosMatchStmtName', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                Name of the Match Statement.
                ''',
                'cbqosmatchstmtname',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            ],
            'CISCO-CLASS-BASED-QOS-MIB',
            'cbQosMatchStmtCfgEntry',
            _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB'],
        'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB'
        ),
    },
    'CISCOCLASSBASEDQOSMIB.CbQosMatchStmtCfgTable' : {
        'meta_info' : _MetaInfoClass('CISCOCLASSBASEDQOSMIB.CbQosMatchStmtCfgTable',
            False, 
            [
            _MetaInfoClassMember('cbQosMatchStmtCfgEntry', REFERENCE_LIST, 'CbQosMatchStmtCfgEntry' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CISCOCLASSBASEDQOSMIB.CbQosMatchStmtCfgTable.CbQosMatchStmtCfgEntry', 
                [], [], 
                '''                Each entry in this table describes configuration information
                about a MatchStatement. The information includes: Name, 
                and whether it is a Match or Match-Not
                statement. This table contains configuration information 
                only, no statistics associated with it. Therefore, it is 
                indexed by the cbQosConfigIndex of each MatchStatement.
                ''',
                'cbqosmatchstmtcfgentry',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            ],
            'CISCO-CLASS-BASED-QOS-MIB',
            'cbQosMatchStmtCfgTable',
            _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB'],
        'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB'
        ),
    },
    'CISCOCLASSBASEDQOSMIB.CbQosMatchStmtStatsTable.CbQosMatchStmtStatsEntry' : {
        'meta_info' : _MetaInfoClass('CISCOCLASSBASEDQOSMIB.CbQosMatchStmtStatsTable.CbQosMatchStmtStatsEntry',
            False, 
            [
            _MetaInfoClassMember('cbQosObjectsIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ''',
                'cbqosobjectsindex',
                'CISCO-CLASS-BASED-QOS-MIB', True),
            _MetaInfoClassMember('cbQosPolicyIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ''',
                'cbqospolicyindex',
                'CISCO-CLASS-BASED-QOS-MIB', True),
            _MetaInfoClassMember('cbQosMatchPrePolicyBitRate', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The bit rate of the traffic prior to executing any QoS
                policies.
                ''',
                'cbqosmatchprepolicybitrate',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosMatchPrePolicyByte', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The lower 32 bits count of inbound octets prior to
                executing any QoS policies.
                ''',
                'cbqosmatchprepolicybyte',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosMatchPrePolicyByte64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The 64 bits count of inbound octets prior to executing
                any QoS policies.
                ''',
                'cbqosmatchprepolicybyte64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosMatchPrePolicyByteOverflow', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The upper 32 bits count of inbound octets prior to
                executing any QoS policies.
                ''',
                'cbqosmatchprepolicybyteoverflow',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosMatchPrePolicyPkt', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The lower 32 bits count of inbound packets prior to
                executing any QoS policies.
                ''',
                'cbqosmatchprepolicypkt',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosMatchPrePolicyPkt64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The 64 bits count of inbound packets prior to executing
                any QoS policies.
                ''',
                'cbqosmatchprepolicypkt64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosMatchPrePolicyPktOverflow', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The upper 32 bits count of inbound packets prior to
                executing any QoS policies.
                ''',
                'cbqosmatchprepolicypktoverflow',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            ],
            'CISCO-CLASS-BASED-QOS-MIB',
            'cbQosMatchStmtStatsEntry',
            _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB'],
        'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB'
        ),
    },
    'CISCOCLASSBASEDQOSMIB.CbQosMatchStmtStatsTable' : {
        'meta_info' : _MetaInfoClass('CISCOCLASSBASEDQOSMIB.CbQosMatchStmtStatsTable',
            False, 
            [
            _MetaInfoClassMember('cbQosMatchStmtStatsEntry', REFERENCE_LIST, 'CbQosMatchStmtStatsEntry' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CISCOCLASSBASEDQOSMIB.CbQosMatchStmtStatsTable.CbQosMatchStmtStatsEntry', 
                [], [], 
                '''                Each entry in this table describes the statistical
                information about Match Statement. Match Statement specific 
                information you can find in this table are : 
                Pre policy pkt/byte counters, and bit rates.
                
                This table contains statistical information only,
                no configuration information associated with it. Therefore, 
                it is indexed by the instance specific IDs, such as 
                cbQosPolicyIndex and cbQosObjectsIndex.
                ''',
                'cbqosmatchstmtstatsentry',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            ],
            'CISCO-CLASS-BASED-QOS-MIB',
            'cbQosMatchStmtStatsTable',
            _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB'],
        'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB'
        ),
    },
    'CISCOCLASSBASEDQOSMIB.CbQosMeasureIPSLACfgTable.CbQosMeasureIPSLACfgEntry' : {
        'meta_info' : _MetaInfoClass('CISCOCLASSBASEDQOSMIB.CbQosMeasureIPSLACfgTable.CbQosMeasureIPSLACfgEntry',
            False, 
            [
            _MetaInfoClassMember('cbQosConfigIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ''',
                'cbqosconfigindex',
                'CISCO-CLASS-BASED-QOS-MIB', True),
            _MetaInfoClassMember('cbQosMeasureIPSLACfgGroupIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                An arbitrary (system-assigned) index for each
                instance of IPSLAs measure action. The index is unique
                for each instance for a particular class in particular
                policy-map. For example consider following configuration:
                     policy-map p1
                        class c1
                          measure type ip-sla group g1
                          measure type ip-sla group g2
                        class c2
                          measure type ip-sla group g3
                
                In this case the cbQosMeasureIPSLACfgGroupIndex value
                for first measure action instance under class c1 will be 1,
                for second instance it will be 1, and so on. The value
                for the index will start over again from 1 for class c2.
                ''',
                'cbqosmeasureipslacfggroupindex',
                'CISCO-CLASS-BASED-QOS-MIB', True),
            _MetaInfoClassMember('cbQosMeasureIPSLACfgGroupName', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                IPSLAs auto group name. Group is an aggregation of
                operations sharing the same type, for example udp-jitter
                type, with common characteristics like frequency,
                interval etc.  Groups are formed by policies dictated
                either by customer, or by service level or any other
                requirements.
                ''',
                'cbqosmeasureipslacfggroupname',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            ],
            'CISCO-CLASS-BASED-QOS-MIB',
            'cbQosMeasureIPSLACfgEntry',
            _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB'],
        'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB'
        ),
    },
    'CISCOCLASSBASEDQOSMIB.CbQosMeasureIPSLACfgTable' : {
        'meta_info' : _MetaInfoClass('CISCOCLASSBASEDQOSMIB.CbQosMeasureIPSLACfgTable',
            False, 
            [
            _MetaInfoClassMember('cbQosMeasureIPSLACfgEntry', REFERENCE_LIST, 'CbQosMeasureIPSLACfgEntry' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CISCOCLASSBASEDQOSMIB.CbQosMeasureIPSLACfgTable.CbQosMeasureIPSLACfgEntry', 
                [], [], 
                '''                Each entry describes configuration information about
                one instance of IPSLAs measure action in the policy map.
                The table is indexed by the cbQosConfigIndex and
                cbQosMeasureIPSLACfgGroupIndex.
                ''',
                'cbqosmeasureipslacfgentry',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            ],
            'CISCO-CLASS-BASED-QOS-MIB',
            'cbQosMeasureIPSLACfgTable',
            _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB'],
        'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB'
        ),
    },
    'CISCOCLASSBASEDQOSMIB.CbQosObjectsTable.CbQosObjectsEntry' : {
        'meta_info' : _MetaInfoClass('CISCOCLASSBASEDQOSMIB.CbQosObjectsTable.CbQosObjectsEntry',
            False, 
            [
            _MetaInfoClassMember('cbQosObjectsIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                An arbitrary (system-assigned) instance specific
                index for cbQosObjectsEntry.
                ''',
                'cbqosobjectsindex',
                'CISCO-CLASS-BASED-QOS-MIB', True),
            _MetaInfoClassMember('cbQosPolicyIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ''',
                'cbqospolicyindex',
                'CISCO-CLASS-BASED-QOS-MIB', True),
            _MetaInfoClassMember('cbQosConfigIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                An arbitrary (system-assigned) config (instance
                independent) index for each Object. Each objects having
                the same configuration share the same config index.
                ''',
                'cbqosconfigindex',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosObjectsType', REFERENCE_ENUM_CLASS, 'QosObjectType_Enum' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'QosObjectType_Enum', 
                [], [], 
                '''                The type of the QoS object.
                ''',
                'cbqosobjectstype',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosParentObjectsIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The parent instance index of a QoS object.
                
                For a ClassMap, the parent index would be the index of 
                the attached PolicyMap.
                
                For a Match Statement, the parent index would be the 
                index of the ClassMap that uses this Match Statement.
                
                For an action, the parent index would be the 
                index of the ClassMap that applies such Action.
                
                For a non-hierarchical PolicyMap, the parent would be 
                the logical interface to which the policy is attached,
                thus the parent index would be 0.
                
                For a hierarchical PolicyMap, the parent index would 
                be the index of the ClassMap to which the nested 
                policy is attached.
                ''',
                'cbqosparentobjectsindex',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            ],
            'CISCO-CLASS-BASED-QOS-MIB',
            'cbQosObjectsEntry',
            _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB'],
        'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB'
        ),
    },
    'CISCOCLASSBASEDQOSMIB.CbQosObjectsTable' : {
        'meta_info' : _MetaInfoClass('CISCOCLASSBASEDQOSMIB.CbQosObjectsTable',
            False, 
            [
            _MetaInfoClassMember('cbQosObjectsEntry', REFERENCE_LIST, 'CbQosObjectsEntry' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CISCOCLASSBASEDQOSMIB.CbQosObjectsTable.CbQosObjectsEntry', 
                [], [], 
                '''                A QoS object entry. Objects covered in this table are
                PolicyMap, ClassMap, Match Statements, and Actions.
                Each entry is indexed by system-generated cbQosPolicyIndex,
                and cbQosObjectsIndex, which represents a runtime instance 
                of a QoS object. In conjunction with the 
                cbQosParentObjectsIndex, a management station can 
                determine the hierarchical relationship of those QoS 
                objects. Given that classmaps and service policies can 
                be nested entites, each entry in this table represents a 
                unique instance of such object. Each runtime object 
                instance has a corresponding config object, which contains
                the configuration information of such QoS object. The
                config object is indexed by cbQosConfigIndex.
                ''',
                'cbqosobjectsentry',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            ],
            'CISCO-CLASS-BASED-QOS-MIB',
            'cbQosObjectsTable',
            _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB'],
        'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB'
        ),
    },
    'CISCOCLASSBASEDQOSMIB.CbQosPoliceActionCfgTable.CbQosPoliceActionCfgEntry' : {
        'meta_info' : _MetaInfoClass('CISCOCLASSBASEDQOSMIB.CbQosPoliceActionCfgTable.CbQosPoliceActionCfgEntry',
            False, 
            [
            _MetaInfoClassMember('cbQosConfigIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ''',
                'cbqosconfigindex',
                'CISCO-CLASS-BASED-QOS-MIB', True),
            _MetaInfoClassMember('cbQosPoliceActionCfgIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                An arbitrary (system-assigned) index for police
                actions that are defined by a police configuration.
                ''',
                'cbqospoliceactioncfgindex',
                'CISCO-CLASS-BASED-QOS-MIB', True),
            _MetaInfoClassMember('cbQosPoliceActionCfgConform', REFERENCE_ENUM_CLASS, 'PoliceAction_Enum' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'PoliceAction_Enum', 
                [], [], 
                '''                Action to be taken when the traffic exceeds the
                conform and exceed token buckets.
                ''',
                'cbqospoliceactioncfgconform',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceActionCfgConformSetValue', ATTRIBUTE, 'int' , None, None, 
                [(0, 99)], [], 
                '''                New packet attribute values for each packet set by
                police action defined in cbQosPoliceActionCfgConform.
                This object will be set to zero if the corresponding
                police action does not require a set value, such as 
                no action, drop action or transmit action.
                ''',
                'cbqospoliceactioncfgconformsetvalue',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceActionCfgExceed', REFERENCE_ENUM_CLASS, 'PoliceAction_Enum' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'PoliceAction_Enum', 
                [], [], 
                '''                Action to be taken when the traffic exceeds the
                conform and exceed token buckets.
                ''',
                'cbqospoliceactioncfgexceed',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceActionCfgExceedSetValue', ATTRIBUTE, 'int' , None, None, 
                [(0, 99)], [], 
                '''                New packet attribute values for each packet set by
                police action defined in cbQosPoliceActionCfgExceed.
                This object will be set to zero if the corresponding
                police action does not require a set value, such as 
                no action, drop action or transmit action.
                ''',
                'cbqospoliceactioncfgexceedsetvalue',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceActionCfgViolate', REFERENCE_ENUM_CLASS, 'PoliceAction_Enum' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'PoliceAction_Enum', 
                [], [], 
                '''                Action to be taken when the traffic exceeds the
                conform and exceed token buckets.
                ''',
                'cbqospoliceactioncfgviolate',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceActionCfgViolateSetValue', ATTRIBUTE, 'int' , None, None, 
                [(0, 99)], [], 
                '''                New packet attribute values for each packet set by
                police action defined in cbQosPoliceActionCfgViolate.
                This object will be set to zero if the corresponding
                police action does not require a set value, such as 
                no action, drop action or transmit action.
                ''',
                'cbqospoliceactioncfgviolatesetvalue',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            ],
            'CISCO-CLASS-BASED-QOS-MIB',
            'cbQosPoliceActionCfgEntry',
            _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB'],
        'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB'
        ),
    },
    'CISCOCLASSBASEDQOSMIB.CbQosPoliceActionCfgTable' : {
        'meta_info' : _MetaInfoClass('CISCOCLASSBASEDQOSMIB.CbQosPoliceActionCfgTable',
            False, 
            [
            _MetaInfoClassMember('cbQosPoliceActionCfgEntry', REFERENCE_LIST, 'CbQosPoliceActionCfgEntry' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CISCOCLASSBASEDQOSMIB.CbQosPoliceActionCfgTable.CbQosPoliceActionCfgEntry', 
                [], [], 
                '''                Each entry in this table describes configuration information
                about Actions for one Police.  The table holds Police 
                action specific configuration parameters.
                This table is a sub-table for cbQosPoliceCfgTable. There is
                a 1-to-1 association between one entry here and one entry in 
                cbQosPoliceCfgTable. 
                This table contains configuration information only,
                no statistics associated with it. 
                This table has two indices. The first is cbQosConfigIndex 
                which is drived directly from cbQosPoliceCfgTable to keep the
                1-to-1 mapping nature between two tables. 
                The second is cbQosPoliceActionCfgIndex used to reference 
                the actual actions configured. The maximum number of actions
                supported is determined by the system, which is 5 currently.
                ''',
                'cbqospoliceactioncfgentry',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            ],
            'CISCO-CLASS-BASED-QOS-MIB',
            'cbQosPoliceActionCfgTable',
            _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB'],
        'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB'
        ),
    },
    'CISCOCLASSBASEDQOSMIB.CbQosPoliceCfgTable.CbQosPoliceCfgEntry' : {
        'meta_info' : _MetaInfoClass('CISCOCLASSBASEDQOSMIB.CbQosPoliceCfgTable.CbQosPoliceCfgEntry',
            False, 
            [
            _MetaInfoClassMember('cbQosConfigIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ''',
                'cbqosconfigindex',
                'CISCO-CLASS-BASED-QOS-MIB', True),
            _MetaInfoClassMember('cbQosPoliceCfgBurstCell', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The amount of traffic, in cells, in excess of the
                committed policing rate that will be permitted by
                the policing feature.
                ''',
                'cbqospolicecfgburstcell',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceCfgBurstSize', ATTRIBUTE, 'int' , None, None, 
                [(1000, 512000000)], [], 
                '''                The amount of traffic, in bytes, in excess of the
                committed policing rate that will be permitted by 
                the policing feature.
                
                cbQosPoliceCfgBurstSize object is superseded by
                cbQosPoliceCfgBurstSize64.
                ''',
                'cbqospolicecfgburstsize',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceCfgBurstSize64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                This object indicated the amount of traffic, in bytes, in
                excess of the committed policing rate that will be permitted by 
                the policing feature. 
                
                If a device implements cbQosPoliceCfgBurstSize64, then
                it should not implement cbQosPoliceCfgBurstSize.
                ''',
                'cbqospolicecfgburstsize64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceCfgBurstTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The amount of traffic time, in ms, in excess of the
                committed policing rate that will be permitted by
                the policing feature.  The milli-second value is
                internally converted to bytes by using the bandwidth
                that is available for the class.
                ''',
                'cbqospolicecfgbursttime',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceCfgCdvt', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The ATM Cell Delay Variation Tolerance value.
                ''',
                'cbqospolicecfgcdvt',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceCfgCellPir', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The peak policing rate in cells/second.  Its value is
                valid only when cbQosPoliceCfgRateType equals to 3.
                ''',
                'cbqospolicecfgcellpir',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceCfgCellRate', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The committed policing rate in cells/second.  Its value
                is valid only when cbQosPoliceCfgRateType equals to 3.
                ''',
                'cbqospolicecfgcellrate',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceCfgConditional', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object is use to depict weather police is configured
                as a conditioniler policer or not
                ''',
                'cbqospolicecfgconditional',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceCfgConformAction', REFERENCE_ENUM_CLASS, 'PoliceAction_Enum' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'PoliceAction_Enum', 
                [], [], 
                '''                Action to be taken when the traffic is within the
                configured rate, that is, the traffic rate is 
                conforming.
                
                cbQosPoliceCfgConformAction object is superseded by
                cbQosPoliceActionCfgConform.
                ''',
                'cbqospolicecfgconformaction',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceCfgConformColor', ATTRIBUTE, 'str' , None, None, 
                [], ['\\p{IsBasicLatin}{0,255}'], 
                '''                The Classmap name used in AF color-aware mode to
                specify the conform-color for the incoming packets
                which was marked by the previous node.
                
                At least conform-color must be specified.  If only 
                conform-color is specified, all other packets are
                assumed to be marked exceed.
                
                See RFC 2697, A Single Rate Three Color Marker.
                See RFC 2698, A Two Rate Three Color Marker.
                ''',
                'cbqospolicecfgconformcolor',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceCfgConformSetValue', ATTRIBUTE, 'int' , None, None, 
                [(1, 99)], [], 
                '''                New packet attribute values for each packets that
                conforms to the configured Police rate.
                
                cbQosPoliceCfgConformSetValue object is superseded by
                cbQosPoliceActionCfgConformSetValue.
                ''',
                'cbqospolicecfgconformsetvalue',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceCfgExceedAction', REFERENCE_ENUM_CLASS, 'PoliceAction_Enum' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'PoliceAction_Enum', 
                [], [], 
                '''                Action to be taken when the traffic exceeds the
                configured rate, that is, the traffic is 
                non-conforming.
                
                cbQosPoliceCfgExceedAction object is superseded by
                cbQosPoliceActionCfgExceed.
                ''',
                'cbqospolicecfgexceedaction',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceCfgExceedColor', ATTRIBUTE, 'str' , None, None, 
                [], ['\\p{IsBasicLatin}{0,255}'], 
                '''                The Classmap name used in AF color-aware mode to
                specify the exceed-color for the incoming packets
                which was marked by the previous node.
                
                If both conform-color and exceed-color are specified,
                all other packets are assumed to be marked violate.
                Violate-color configuration is not needed.
                ''',
                'cbqospolicecfgexceedcolor',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceCfgExceedSetValue', ATTRIBUTE, 'int' , None, None, 
                [(1, 99)], [], 
                '''                New packet attribute values for each packets that
                conforms to the configured Police rate.
                
                cbQosPoliceCfgExceedSetValue object is superseded by
                cbQosPoliceActionCfgExceedSetValue.
                ''',
                'cbqospolicecfgexceedsetvalue',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceCfgExtBurstCell', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The amount of traffic, in cells, in excess of the
                burst limit, which may be conditionally permitted
                by the policing feature. The probability that the
                traffic is not permitted increases as the received
                burst size increases.
                ''',
                'cbqospolicecfgextburstcell',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceCfgExtBurstSize', ATTRIBUTE, 'int' , None, None, 
                [(1000, 512000000)], [], 
                '''                The amount of traffic, in bytes, in excess of the
                burst limit, which may be conditionally permitted 
                by the policing feature. The probability that the 
                traffic is not permitted increases as the received 
                burst size increases.
                
                cbQosPoliceCfgExtBurstSize object is superseded by
                cbQosPoliceCfgExtBurstSize64.
                ''',
                'cbqospolicecfgextburstsize',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceCfgExtBurstSize64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                This object indicated the amount of traffic, in bytes, in
                excess of the burst limit, which may be conditionally permitted 
                by the policing feature. The probability that the 
                traffic is not permitted increases as the received 
                burst size increases. 
                
                If a device implements cbQosPoliceCfgBurstSize64, then
                it should not implement cbQosPoliceCfgBurstSize.
                ''',
                'cbqospolicecfgextburstsize64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceCfgExtBurstTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The amount of traffic time, in ms, in excess of the
                burst limit, which may be conditionally permitted
                by the policing feature. The probability that the
                traffic is not permitted increases as the received
                burst size increases.  The milli-second value is 
                internally converted to bytes by using the bandwidth
                that is available for the class.
                ''',
                'cbqospolicecfgextbursttime',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceCfgPercentPirValue', ATTRIBUTE, 'int' , None, None, 
                [(0, 100)], [], 
                '''                The peak policing rate in percentage. Its value is
                valid only when cbQosPoliceCfgRateType equals to 2.
                ''',
                'cbqospolicecfgpercentpirvalue',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceCfgPercentRateValue', ATTRIBUTE, 'int' , None, None, 
                [(0, 100)], [], 
                '''                The committed policing rate in percentage.  Its value
                is valid only when cbQosPoliceCfgRateType equals to 2.
                ''',
                'cbqospolicecfgpercentratevalue',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceCfgPir', ATTRIBUTE, 'int' , None, None, 
                [(8000, 2000000000)], [], 
                '''                The committed policing rate. This is the peak
                rate permitted by two rate policing.
                
                cbQosPoliceCfgPir object is superseded by cbQosPoliceCfgPir64.
                ''',
                'cbqospolicecfgpir',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceCfgPir64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                This object indicates the committed policing rate. This is the
                peak rate permitted by two rate policing. 
                
                If a device implements cbQosPoliceCfgPir64, then
                it should not implement cbQosPoliceCfgPir.
                ''',
                'cbqospolicecfgpir64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceCfgRate', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The committed policing rate. This is the sustained
                rate permitted by policing.
                
                If a committed policing rate greater than 4294967295
                is configurable on the system, then the configured
                rate is available in cbQosPoliceCfgRate64.
                ''',
                'cbqospolicecfgrate',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceCfgRate64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The committed policing rate. This is the sustained
                rate permitted by policing.
                ''',
                'cbqospolicecfgrate64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceCfgRateType', REFERENCE_ENUM_CLASS, 'CbQosRateType_Enum' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CbQosRateType_Enum', 
                [], [], 
                '''                The rate type that configured for CIR & PIR.
                1 means rates are configured in bps.
                2 means rates are configured in percentage.
                3 means rates are configured in cps.
                4 means rates are configured in parts per-thousand.
                5 means rates are configured in parts per-million.
                ''',
                'cbqospolicecfgratetype',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceCfgViolateAction', REFERENCE_ENUM_CLASS, 'PoliceAction_Enum' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'PoliceAction_Enum', 
                [], [], 
                '''                Action to be taken when the traffic exceeds the
                conform and exceed token buckets.
                
                cbQosPoliceCfgViolateAction object is superseded by
                cbQosPoliceActionCfgViolate.
                ''',
                'cbqospolicecfgviolateaction',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceCfgViolateSetValue', ATTRIBUTE, 'int' , None, None, 
                [(1, 99)], [], 
                '''                New packet attribute values for each packets that
                conforms to the Police violate action. The packet
                attibute values depend on the action that is taken
                for the particular packet. For example, if the 
                action was to set the dscp value, this entry describes
                the value it is set to. 
                
                cbQosPoliceCfgViolateSetValue object is superseded by
                cbQosPoliceActionCfgViolateSetValue.
                ''',
                'cbqospolicecfgviolatesetvalue',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            ],
            'CISCO-CLASS-BASED-QOS-MIB',
            'cbQosPoliceCfgEntry',
            _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB'],
        'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB'
        ),
    },
    'CISCOCLASSBASEDQOSMIB.CbQosPoliceCfgTable' : {
        'meta_info' : _MetaInfoClass('CISCOCLASSBASEDQOSMIB.CbQosPoliceCfgTable',
            False, 
            [
            _MetaInfoClassMember('cbQosPoliceCfgEntry', REFERENCE_LIST, 'CbQosPoliceCfgEntry' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CISCOCLASSBASEDQOSMIB.CbQosPoliceCfgTable.CbQosPoliceCfgEntry', 
                [], [], 
                '''                Each entry in this table describes configuration information
                about a Police Action.  The table holds Policy 
                configuration parameters, such as rate, burst size, and 
                actions based on traffic rates.
                
                This table contains configuration information only,
                no statistics associated with it. Therefore, it is indexed
                by the cbQosConfigIndex.
                ''',
                'cbqospolicecfgentry',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            ],
            'CISCO-CLASS-BASED-QOS-MIB',
            'cbQosPoliceCfgTable',
            _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB'],
        'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB'
        ),
    },
    'CISCOCLASSBASEDQOSMIB.CbQosPoliceColorStatsTable.CbQosPoliceColorStatsEntry' : {
        'meta_info' : _MetaInfoClass('CISCOCLASSBASEDQOSMIB.CbQosPoliceColorStatsTable.CbQosPoliceColorStatsEntry',
            False, 
            [
            _MetaInfoClassMember('cbQosObjectsIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ''',
                'cbqosobjectsindex',
                'CISCO-CLASS-BASED-QOS-MIB', True),
            _MetaInfoClassMember('cbQosPolicyIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ''',
                'cbqospolicyindex',
                'CISCO-CLASS-BASED-QOS-MIB', True),
            _MetaInfoClassMember('cbQosPoliceCfmColorCfmBitRate', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The bit rate of conform color class conform rate.
                ''',
                'cbqospolicecfmcolorcfmbitrate',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceCfmColorCfmByte64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The 64 bits count of bytes which are marked as
                Conform-Color by previous node and treated as
                conforming by the policing feature on this node.
                ''',
                'cbqospolicecfmcolorcfmbyte64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceCfmColorCfmPkt64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The 64 bits count of packets which are marked as
                Conform-Color by previous node and treated as
                conforming by the policing feature on this node.
                ''',
                'cbqospolicecfmcolorcfmpkt64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceCfmColorExdBitRate', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The bit rate of conform color class exceed rate.
                ''',
                'cbqospolicecfmcolorexdbitrate',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceCfmColorExdByte64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The 64 bits count of bytes which are marked as
                Conform-Color by previous node and treated as
                exceeding by the policing feature on this node.
                ''',
                'cbqospolicecfmcolorexdbyte64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceCfmColorExdPkt64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The 64 bits count of packets which are marked as
                Conform-Color by previous node and treated as
                exceeding by the policing feature on this node.
                ''',
                'cbqospolicecfmcolorexdpkt64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceCfmColorVltBitRate', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The bit rate of conform color class violate rate.
                ''',
                'cbqospolicecfmcolorvltbitrate',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceCfmColorVltByte64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The 64 bits count of bytes which are marked as
                Conform-Color by previous node and treated as
                violating by the policing feature on this node.
                ''',
                'cbqospolicecfmcolorvltbyte64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceCfmColorVltPkt64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The 64 bits count of packets which are marked as
                Conform-Color by previous node and treated as
                violating by the policing feature on this node.
                ''',
                'cbqospolicecfmcolorvltpkt64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceExdColorExdBitRate', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The bit rate of exceed color class exceed rate.
                ''',
                'cbqospoliceexdcolorexdbitrate',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceExdColorExdByte64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The 64 bits count of bytes which are marked as
                Exceed-Color by previous node and treated as
                exceeding by the policing feature on this node.
                ''',
                'cbqospoliceexdcolorexdbyte64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceExdColorExdPkt64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The 64 bits count of packets which are marked as
                Exceed-Color by previous node and treated as
                exceeding by the policing feature on this node.
                ''',
                'cbqospoliceexdcolorexdpkt64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceExdColorVltBitRate', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The bit rate of exceed color class violate rate.
                ''',
                'cbqospoliceexdcolorvltbitrate',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceExdColorVltByte64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The 64 bits count of bytes which are marked as
                Exceed-Color by previous node and treated as
                violating by the policing feature on this node.
                ''',
                'cbqospoliceexdcolorvltbyte64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceExdColorVltPkt64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The 64 bits count of packets which are marked as
                Exceed-Color by previous node and treated as
                violating by the policing feature on this node.
                ''',
                'cbqospoliceexdcolorvltpkt64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceVltColorVltBitRate', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The bit rate of violate color class violate rate.
                ''',
                'cbqospolicevltcolorvltbitrate',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceVltColorVltByte64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The 64 bits count of bytes which are marked as
                Violate-Color by previous node and treated as
                violating by the policing feature on this node.
                ''',
                'cbqospolicevltcolorvltbyte64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceVltColorVltPkt64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The 64 bits count of packets which are marked as
                Violate-Color by previous node and treated as
                violating by the policing feature on this node.
                ''',
                'cbqospolicevltcolorvltpkt64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            ],
            'CISCO-CLASS-BASED-QOS-MIB',
            'cbQosPoliceColorStatsEntry',
            _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB'],
        'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB'
        ),
    },
    'CISCOCLASSBASEDQOSMIB.CbQosPoliceColorStatsTable' : {
        'meta_info' : _MetaInfoClass('CISCOCLASSBASEDQOSMIB.CbQosPoliceColorStatsTable',
            False, 
            [
            _MetaInfoClassMember('cbQosPoliceColorStatsEntry', REFERENCE_LIST, 'CbQosPoliceColorStatsEntry' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CISCOCLASSBASEDQOSMIB.CbQosPoliceColorStatsTable.CbQosPoliceColorStatsEntry', 
                [], [], 
                '''                Each entry in this table describes the statistical
                information about Police Action for Two Rate Color
                Aware Marker.
                
                This table contains statistical information only,
                no configuration information associated with it.
                Therefore, it is indexed by the instance specific IDs,
                such as cbQosPolicyIndex and cbQosObjectsIndex.
                ''',
                'cbqospolicecolorstatsentry',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            ],
            'CISCO-CLASS-BASED-QOS-MIB',
            'cbQosPoliceColorStatsTable',
            _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB'],
        'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB'
        ),
    },
    'CISCOCLASSBASEDQOSMIB.CbQosPoliceStatsTable.CbQosPoliceStatsEntry' : {
        'meta_info' : _MetaInfoClass('CISCOCLASSBASEDQOSMIB.CbQosPoliceStatsTable.CbQosPoliceStatsEntry',
            False, 
            [
            _MetaInfoClassMember('cbQosObjectsIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ''',
                'cbqosobjectsindex',
                'CISCO-CLASS-BASED-QOS-MIB', True),
            _MetaInfoClassMember('cbQosPolicyIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ''',
                'cbqospolicyindex',
                'CISCO-CLASS-BASED-QOS-MIB', True),
            _MetaInfoClassMember('cbQosPoliceConformedBitRate', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The bit rate of conforming traffic.
                ''',
                'cbqospoliceconformedbitrate',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceConformedBitRate64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The bit rate of conforming traffic.
                This object is a 64-bit version of
                cbQosPoliceConformedBitRate.
                ''',
                'cbqospoliceconformedbitrate64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceConformedByte', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The lower 32 bits count of octets treated as
                conforming by the policing feature.
                ''',
                'cbqospoliceconformedbyte',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceConformedByte64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The 64 bits count of octets treated as conforming
                by the policing feature.
                ''',
                'cbqospoliceconformedbyte64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceConformedByteOverflow', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The upper 32 bits count of octets treated as
                conforming by the policing feature.
                ''',
                'cbqospoliceconformedbyteoverflow',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceConformedPkt', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The lower 32 bits count of packets treated as
                conforming by the policing feature.
                ''',
                'cbqospoliceconformedpkt',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceConformedPkt64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The 64 bits count of packets treated as conforming
                by the policing feature.
                ''',
                'cbqospoliceconformedpkt64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceConformedPktOverflow', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The upper 32 bits count of packets treated as
                conforming by the policing feature.
                ''',
                'cbqospoliceconformedpktoverflow',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceExceededBitRate', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The bit rate of the non-conforming traffic.
                ''',
                'cbqospoliceexceededbitrate',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceExceededBitRate64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The bit rate of non-conforming traffic.
                This object is a 64-bit version of
                cbQosPoliceExceededBitRate.
                ''',
                'cbqospoliceexceededbitrate64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceExceededByte', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The lower 32 bits count of octets treated as
                non-conforming by the policing feature.
                ''',
                'cbqospoliceexceededbyte',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceExceededByte64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The 64 bits count of octets treated as
                non-conforming by the policing feature.
                ''',
                'cbqospoliceexceededbyte64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceExceededByteOverflow', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The upper 32 bits count of octets treated as
                non-conforming by the policing feature.
                ''',
                'cbqospoliceexceededbyteoverflow',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceExceededPkt', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The 32 bits count of packets treated as
                non-conforming by the policing feature.
                ''',
                'cbqospoliceexceededpkt',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceExceededPkt64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The 64 bits count of packets treated as
                non-conforming by the policing feature.
                ''',
                'cbqospoliceexceededpkt64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceExceededPktOverflow', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The upper 32 bits count of packets treated as
                non-conforming by the policing feature.
                ''',
                'cbqospoliceexceededpktoverflow',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceViolatedBitRate', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The bit rate of the violating traffic.
                ''',
                'cbqospoliceviolatedbitrate',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceViolatedBitRate64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The bit rate of the violating traffic.
                This object is a 64-bit version of
                cbQosPoliceViolatedBitRate.
                ''',
                'cbqospoliceviolatedbitrate64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceViolatedByte', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The lower 32 bits count of octets treated as
                violated by the policing feature.
                ''',
                'cbqospoliceviolatedbyte',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceViolatedByte64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The 64 bits count of octets treated as
                violated by the policing feature.
                ''',
                'cbqospoliceviolatedbyte64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceViolatedByteOverflow', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The upper 32 bits count of octets treated as
                violated by the policing feature.
                ''',
                'cbqospoliceviolatedbyteoverflow',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceViolatedPkt', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The 32 bits count of packets treated as
                violated by the policing feature.
                ''',
                'cbqospoliceviolatedpkt',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceViolatedPkt64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The 64 bits count of packets treated as
                violated by the policing feature.
                ''',
                'cbqospoliceviolatedpkt64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceViolatedPktOverflow', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The upper 32 bits count of packets treated as
                violated by the policing feature.
                ''',
                'cbqospoliceviolatedpktoverflow',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            ],
            'CISCO-CLASS-BASED-QOS-MIB',
            'cbQosPoliceStatsEntry',
            _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB'],
        'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB'
        ),
    },
    'CISCOCLASSBASEDQOSMIB.CbQosPoliceStatsTable' : {
        'meta_info' : _MetaInfoClass('CISCOCLASSBASEDQOSMIB.CbQosPoliceStatsTable',
            False, 
            [
            _MetaInfoClassMember('cbQosPoliceStatsEntry', REFERENCE_LIST, 'CbQosPoliceStatsEntry' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CISCOCLASSBASEDQOSMIB.CbQosPoliceStatsTable.CbQosPoliceStatsEntry', 
                [], [], 
                '''                Each entry in this table describes the statistical
                information about Police Action. Police Action specific 
                information you can find in this table are : 
                Conformed/Exceeded pkt/byte counters,  bit rates.
                
                This table contains statistical information only,
                no configuration information associated with it. 
                Therefore, it is indexed by the instance specific IDs, 
                such as cbQosPolicyIndex and cbQosObjectsIndex.
                ''',
                'cbqospolicestatsentry',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            ],
            'CISCO-CLASS-BASED-QOS-MIB',
            'cbQosPoliceStatsTable',
            _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB'],
        'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB'
        ),
    },
    'CISCOCLASSBASEDQOSMIB.CbQosPolicyMapCfgTable.CbQosPolicyMapCfgEntry' : {
        'meta_info' : _MetaInfoClass('CISCOCLASSBASEDQOSMIB.CbQosPolicyMapCfgTable.CbQosPolicyMapCfgEntry',
            False, 
            [
            _MetaInfoClassMember('cbQosConfigIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ''',
                'cbqosconfigindex',
                'CISCO-CLASS-BASED-QOS-MIB', True),
            _MetaInfoClassMember('cbQosPolicyMapDesc', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                Description of the PolicyMap.
                ''',
                'cbqospolicymapdesc',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPolicyMapName', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                Name of the Policymap.
                ''',
                'cbqospolicymapname',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            ],
            'CISCO-CLASS-BASED-QOS-MIB',
            'cbQosPolicyMapCfgEntry',
            _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB'],
        'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB'
        ),
    },
    'CISCOCLASSBASEDQOSMIB.CbQosPolicyMapCfgTable' : {
        'meta_info' : _MetaInfoClass('CISCOCLASSBASEDQOSMIB.CbQosPolicyMapCfgTable',
            False, 
            [
            _MetaInfoClassMember('cbQosPolicyMapCfgEntry', REFERENCE_LIST, 'CbQosPolicyMapCfgEntry' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CISCOCLASSBASEDQOSMIB.CbQosPolicyMapCfgTable.CbQosPolicyMapCfgEntry', 
                [], [], 
                '''                Each entry in this table describes configuration information
                about a policymap. The information includes: Name, and it's
                description. This table contains configuration information 
                only, no statistics associated with it. Therefore, it is 
                indexed by the cbQosConfigIndex of each PolicyMap.
                ''',
                'cbqospolicymapcfgentry',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            ],
            'CISCO-CLASS-BASED-QOS-MIB',
            'cbQosPolicyMapCfgTable',
            _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB'],
        'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB'
        ),
    },
    'CISCOCLASSBASEDQOSMIB.CbQosQueueingCfgTable.CbQosQueueingCfgEntry' : {
        'meta_info' : _MetaInfoClass('CISCOCLASSBASEDQOSMIB.CbQosQueueingCfgTable.CbQosQueueingCfgEntry',
            False, 
            [
            _MetaInfoClassMember('cbQosConfigIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ''',
                'cbqosconfigindex',
                'CISCO-CLASS-BASED-QOS-MIB', True),
            _MetaInfoClassMember('cbQosQueueingCfgAggregateQLimit', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Maximum allowed queue size for all the individual
                queues associated with this class. When the queue size
                exceed this value, the packets will be dropped.
                ''',
                'cbqosqueueingcfgaggregateqlimit',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosQueueingCfgAggregateQSize', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Maximum number of packets that can be held in all the
                individual queues associated with this class
                before packets are dropped. 
                cbQosQueueingCfgAggregateQSize object is superseded by 
                cbQosQueueingCfgAggregateQLimit.
                ''',
                'cbqosqueueingcfgaggregateqsize',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosQueueingCfgAggrQLimitTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Maximum allowed queue size in milli-seconds for all
                individual queues associated with this class.  It
                is internally converted to bytes by using the
                bandwidth that is available for the class.
                ''',
                'cbqosqueueingcfgaggrqlimittime',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosQueueingCfgBandwidth', ATTRIBUTE, 'int' , None, None, 
                [(0, 2000000)], [], 
                '''                The type of bandwidth configuration value represented by this
                object is indicated by the value of
                cbQosQueueingCfgBandwidthUnits for this entry. 
                
                If the cbQosQueueingCfgBandwidthUnits value is 'kbps(1)' or 
                'percentage(2)', this object represents the configured  
                bandwidth allocated to this traffic class.In the case of a  
                bandwidth policy, this value represents a minimum bandwidth  
                guarantee for the traffic class. In the case of a priority  
                policy, this value represents the maximum rate at which  
                priority service is guaranteed. 
                
                If the cbQosQueueingCfgBandwidthUnits value is  
                'percentageRemaining(3)', this object represents the  
                the percentage of the unallocated bandwidth to allocate to 
                this class.  If the cbQosQueueingCfgBandwidthUnits value is  
                'ratioRemaining(4)', this object represents the ratio value, 
                relative to other class' configured ratio values, used to  
                determine the portion of the unallocated bandwidth to apply to 
                this class.
                
                cbQosQueueingCfgBandwidth object is superseded by
                cbQosQueueingCfgBandwidth64.
                ''',
                'cbqosqueueingcfgbandwidth',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosQueueingCfgBandwidth64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                This object indicates the guaranteed bandwidth for a particular
                traffic class.
                
                The type of bandwidth configuration value represented by this
                object is indicated by the value of
                cbQosQueueingCfgBandwidthUnits. 
                
                If the cbQosQueueingCfgBandwidthUnits value is 'kbps(1)' or 
                'percentage(2)', this object represents the configured  
                bandwidth allocated to this traffic class.In the case of a  
                bandwidth policy, this value represents a minimum bandwidth  
                guarantee for the traffic class. In the case of a priority  
                policy, this value represents the maximum rate at which  
                priority service is guaranteed. 
                
                If the cbQosQueueingCfgBandwidthUnits value is  
                'percentageRemaining(3)', this object represents the  
                the percentage of the unallocated bandwidth to allocate to 
                this class.  If the cbQosQueueingCfgBandwidthUnits value is  
                'ratioRemaining(4)', this object represents the ratio value, 
                relative to other class' configured ratio values, used to  
                determine the portion of the unallocated bandwidth to apply to 
                this class.
                
                If a device implements cbQosQueueingCfgBandwidth64, it should
                not implement cbQosQueueingCfgBandwidth.
                ''',
                'cbqosqueueingcfgbandwidth64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosQueueingCfgBandwidthUnits', REFERENCE_ENUM_CLASS, 'QueueingBandwidthUnits_Enum' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'QueueingBandwidthUnits_Enum', 
                [], [], 
                '''                Units of the accompanying cbQosQueueingCfgbandwidth
                parameter
                ''',
                'cbqosqueueingcfgbandwidthunits',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosQueueingCfgDynamicQNumber', ATTRIBUTE, 'int' , None, None, 
                [(1, 32768)], [], 
                '''                Number of dynamic queues supported when
                flow-based fair-queue is in use.
                ''',
                'cbqosqueueingcfgdynamicqnumber',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosQueueingCfgFlowEnabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Boolean to indicate if flow-based fair-queue is
                enabled for this class.
                ''',
                'cbqosqueueingcfgflowenabled',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosQueueingCfgIndividualQSize', ATTRIBUTE, 'int' , None, None, 
                [(1, 32768)], [], 
                '''                Maximum number of packets that can be held in an
                individual Flow-based fair-queue associated with this 
                class before it drops packets (once the AggregateQSize
                has been reached).
                
                This field only makes sense in the context of 
                Flow-based fair-queueing.
                
                cbQosQueueingCfgIndividualQSize object is superseded by
                cbQosQueueingCfgIndividualQSize64.
                ''',
                'cbqosqueueingcfgindividualqsize',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosQueueingCfgIndividualQSize64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Maximum number of packets that can be held in an
                individual Flow-based fair-queue associated with this 
                class before it drops packets (once the AggregateQSize
                has been reached).
                
                If a device implements cbQosQueueingCfgIndividualQSize64, then
                it should not implement cbQosQueueingCfgIndividualQSize.
                ''',
                'cbqosqueueingcfgindividualqsize64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosQueueingCfgPrioBurstSize', ATTRIBUTE, 'int' , None, None, 
                [(32, 64000000)], [], 
                '''                In the priority queue, this is the number of bytes
                allowed in a single burst. 
                This parameter only makes sense if Priority is enabled
                ''',
                'cbqosqueueingcfgprioburstsize',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosQueueingCfgPriorityEnabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Boolean to indicate if low latency queueing
                (priority) is enabled for this class.
                ''',
                'cbqosqueueingcfgpriorityenabled',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosQueueingCfgPriorityLevel', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The priority level of the queue into which packets matching
                this  class are queued into. A larger priority level indicates
                higher  priority.
                ''',
                'cbqosqueueingcfgprioritylevel',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosQueueingCfgQLimitUnits', REFERENCE_ENUM_CLASS, 'CbQosQueueUnitType_Enum' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CbQosQueueUnitType_Enum', 
                [], [], 
                '''                Represents the unit type of
                cbQosQueueingCfgAggregateQLimit object.
                ''',
                'cbqosqueueingcfgqlimitunits',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            ],
            'CISCO-CLASS-BASED-QOS-MIB',
            'cbQosQueueingCfgEntry',
            _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB'],
        'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB'
        ),
    },
    'CISCOCLASSBASEDQOSMIB.CbQosQueueingCfgTable' : {
        'meta_info' : _MetaInfoClass('CISCOCLASSBASEDQOSMIB.CbQosQueueingCfgTable',
            False, 
            [
            _MetaInfoClassMember('cbQosQueueingCfgEntry', REFERENCE_LIST, 'CbQosQueueingCfgEntry' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CISCOCLASSBASEDQOSMIB.CbQosQueueingCfgTable.CbQosQueueingCfgEntry', 
                [], [], 
                '''                Each entry in this table describes configuration
                information about a queueing action. The information 
                includes: Bandwidth, Units, Flow Enabled, Priority Enabled, 
                and Q size.
                
                This table contains configuration information only,
                no statistics associated with it. Therefore, it is indexed
                by the cbQosConfigIndex of each Queueing Action.
                ''',
                'cbqosqueueingcfgentry',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            ],
            'CISCO-CLASS-BASED-QOS-MIB',
            'cbQosQueueingCfgTable',
            _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB'],
        'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB'
        ),
    },
    'CISCOCLASSBASEDQOSMIB.CbQosQueueingClassCfgTable.CbQosQueueingClassCfgEntry' : {
        'meta_info' : _MetaInfoClass('CISCOCLASSBASEDQOSMIB.CbQosQueueingClassCfgTable.CbQosQueueingClassCfgEntry',
            False, 
            [
            _MetaInfoClassMember('cbQosConfigIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ''',
                'cbqosconfigindex',
                'CISCO-CLASS-BASED-QOS-MIB', True),
            _MetaInfoClassMember('cbQosQlimitWeightValue', ATTRIBUTE, 'int' , None, None, 
                [(0, 63)], [], 
                '''                This object depict the weight value configured for
                weighted Queue-limit.
                The Weight value is IP precedence or IP DSCP of this entry.
                ''',
                'cbqosqlimitweightvalue',
                'CISCO-CLASS-BASED-QOS-MIB', True),
            _MetaInfoClassMember('cbQosQueueingClassConfigIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                This objects depict the config index for Weighted  Queue limit
                configured.
                ''',
                'cbqosqueueingclassconfigindex',
                'CISCO-CLASS-BASED-QOS-MIB', True),
            _MetaInfoClassMember('cbQosQueueingClassCfgQLimitWeight', REFERENCE_ENUM_CLASS, 'QueueMechanism_Enum' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'QueueMechanism_Enum', 
                [], [], 
                '''                This objects depict the weight value for Weighted Queue limit
                configured
                i.e(precedence,dscp,qos-group,atm-clp,discard-class,mplsExp)    
                
                .
                ''',
                'cbqosqueueingclasscfgqlimitweight',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosQueueingClassCfgThreshold', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object is used to depict the Threshold value for the
                Weighted Queue Limit.
                ''',
                'cbqosqueueingclasscfgthreshold',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosQueueingClassCfgThresholdUnit', REFERENCE_ENUM_CLASS, 'CbQosQueueUnitType_Enum' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CbQosQueueUnitType_Enum', 
                [], [], 
                '''                This object is used to depict the Threshold Unit for the
                Weighted Queue Limit
                ''',
                'cbqosqueueingclasscfgthresholdunit',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            ],
            'CISCO-CLASS-BASED-QOS-MIB',
            'cbQosQueueingClassCfgEntry',
            _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB'],
        'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB'
        ),
    },
    'CISCOCLASSBASEDQOSMIB.CbQosQueueingClassCfgTable' : {
        'meta_info' : _MetaInfoClass('CISCOCLASSBASEDQOSMIB.CbQosQueueingClassCfgTable',
            False, 
            [
            _MetaInfoClassMember('cbQosQueueingClassCfgEntry', REFERENCE_LIST, 'CbQosQueueingClassCfgEntry' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CISCOCLASSBASEDQOSMIB.CbQosQueueingClassCfgTable.CbQosQueueingClassCfgEntry', 
                [], [], 
                '''                Each entry in this table describes configuration
                information about a weighted queueing action. The information
                includes: Threshold value, Units and wieght Type
                (ip,dscp,mplsExp)
                
                This table contains configuration information only,
                no statistics associated with it. Therefore, it is indexed
                by the cbQosConfigIndex(which refers to cbQosConfigIndex of
                cbQosQueueingCfgEntry) and cbQosQueueingClassConfigIndex
                cbQosQlimitWeightValue  
                i.e(prec,dscp,discard-class,qos-group,atm-clp,
                mplsExp) of each Weighted Queueing Action.
                ''',
                'cbqosqueueingclasscfgentry',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            ],
            'CISCO-CLASS-BASED-QOS-MIB',
            'cbQosQueueingClassCfgTable',
            _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB'],
        'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB'
        ),
    },
    'CISCOCLASSBASEDQOSMIB.CbQosQueueingStatsTable.CbQosQueueingStatsEntry' : {
        'meta_info' : _MetaInfoClass('CISCOCLASSBASEDQOSMIB.CbQosQueueingStatsTable.CbQosQueueingStatsEntry',
            False, 
            [
            _MetaInfoClassMember('cbQosObjectsIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ''',
                'cbqosobjectsindex',
                'CISCO-CLASS-BASED-QOS-MIB', True),
            _MetaInfoClassMember('cbQosPolicyIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ''',
                'cbqospolicyindex',
                'CISCO-CLASS-BASED-QOS-MIB', True),
            _MetaInfoClassMember('cbQosQueueingCurrentQDepth', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The current depth of the queue.
                ''',
                'cbqosqueueingcurrentqdepth',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosQueueingCurrentQDepthPkt', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The current number of packets
                sitting in the queue
                ''',
                'cbqosqueueingcurrentqdepthpkt',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosQueueingDiscardByte', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The lower 32 bits count of octets, associated with
                this class, that were dropped by queueing.
                ''',
                'cbqosqueueingdiscardbyte',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosQueueingDiscardByte64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The count of octets, associated with this class,
                that were dropped by queueing.
                ''',
                'cbqosqueueingdiscardbyte64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosQueueingDiscardByteOverflow', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The upper 32 bit count of octets, associated with
                this class, that were dropped by queueing.
                ''',
                'cbqosqueueingdiscardbyteoverflow',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosQueueingDiscardPkt', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of packets, associated with this class,
                that were dropped by queueing.
                ''',
                'cbqosqueueingdiscardpkt',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosQueueingDiscardPkt64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The number of packets, associated with this class,
                that were dropped by queueing.
                ''',
                'cbqosqueueingdiscardpkt64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosQueueingDiscardPktOverflow', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The upper 32 bits count of packets, associated with
                this class, that were dropped by queueing.
                ''',
                'cbqosqueueingdiscardpktoverflow',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosQueueingMaxQDepth', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The maximum depth of the queue.
                ''',
                'cbqosqueueingmaxqdepth',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosQueueingMaxQDepthPkt', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The maximum depth of the queue in packets.
                ''',
                'cbqosqueueingmaxqdepthpkt',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosQueueingTransmitByte64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The count of octets, associated with this class,
                that were transmitted by queueing.
                ''',
                'cbqosqueueingtransmitbyte64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosQueueingTransmitPkt64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The number of packets, associated with this class,
                that were transmitted by queueing.
                ''',
                'cbqosqueueingtransmitpkt64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            ],
            'CISCO-CLASS-BASED-QOS-MIB',
            'cbQosQueueingStatsEntry',
            _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB'],
        'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB'
        ),
    },
    'CISCOCLASSBASEDQOSMIB.CbQosQueueingStatsTable' : {
        'meta_info' : _MetaInfoClass('CISCOCLASSBASEDQOSMIB.CbQosQueueingStatsTable',
            False, 
            [
            _MetaInfoClassMember('cbQosQueueingStatsEntry', REFERENCE_LIST, 'CbQosQueueingStatsEntry' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CISCOCLASSBASEDQOSMIB.CbQosQueueingStatsTable.CbQosQueueingStatsEntry', 
                [], [], 
                '''                Each entry in this table describes the statistical
                information about queueing action. Queueing action specific 
                information you can find in this table are : 
                various Q depth, and discard pkt/byte counters.
                
                This table contains statistical information only,
                no configuration information associated with it. 
                Therefore, it is indexed by the instance specific IDs, 
                such as cbQosPolicyIndex and cbQosObjectsIndex.
                ''',
                'cbqosqueueingstatsentry',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            ],
            'CISCO-CLASS-BASED-QOS-MIB',
            'cbQosQueueingStatsTable',
            _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB'],
        'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB'
        ),
    },
    'CISCOCLASSBASEDQOSMIB.CbQosREDCfgTable.CbQosREDCfgEntry' : {
        'meta_info' : _MetaInfoClass('CISCOCLASSBASEDQOSMIB.CbQosREDCfgTable.CbQosREDCfgEntry',
            False, 
            [
            _MetaInfoClassMember('cbQosConfigIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ''',
                'cbqosconfigindex',
                'CISCO-CLASS-BASED-QOS-MIB', True),
            _MetaInfoClassMember('cbQosREDCfgDscpPrec', REFERENCE_ENUM_CLASS, 'REDMechanism_Enum' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'REDMechanism_Enum', 
                [], [], 
                '''                The Classification mechanism used by RED
                ''',
                'cbqosredcfgdscpprec',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosREDCfgECNEnabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Boolean to indicate if explicit congestion notification
                enabled for this class.
                ''',
                'cbqosredcfgecnenabled',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosREDCfgExponWeight', ATTRIBUTE, 'int' , None, None, 
                [(1, 16)], [], 
                '''                The decay factor for the queue average calculation.
                The decay factor is equal to raising 2 to the power 
                of N, where N could be up to 16. 
                The smaller the number, the faster it decays.
                ''',
                'cbqosredcfgexponweight',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosREDCfgMeanQsize', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                The average queue size, computed and used by the WRED
                algorithm.
                cbQosREDCfgMeanQsize object is superseded by 
                cbQosREDMeanQsize.
                ''',
                'cbqosredcfgmeanqsize',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            ],
            'CISCO-CLASS-BASED-QOS-MIB',
            'cbQosREDCfgEntry',
            _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB'],
        'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB'
        ),
    },
    'CISCOCLASSBASEDQOSMIB.CbQosREDCfgTable' : {
        'meta_info' : _MetaInfoClass('CISCOCLASSBASEDQOSMIB.CbQosREDCfgTable',
            False, 
            [
            _MetaInfoClassMember('cbQosREDCfgEntry', REFERENCE_LIST, 'CbQosREDCfgEntry' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CISCOCLASSBASEDQOSMIB.CbQosREDCfgTable.CbQosREDCfgEntry', 
                [], [], 
                '''                Each entry in this table describes configuration
                information about a WRED Action.  The table holds global 
                (per traffic class) configuration like: Expon Weight
                and Mean Q size.
                
                This table contains configuration information only,
                no statistics associated with it. Therefore, it is indexed
                by the cbQosConfigIndex of each WRED Action.
                ''',
                'cbqosredcfgentry',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            ],
            'CISCO-CLASS-BASED-QOS-MIB',
            'cbQosREDCfgTable',
            _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB'],
        'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB'
        ),
    },
    'CISCOCLASSBASEDQOSMIB.CbQosREDClassCfgTable.CbQosREDClassCfgEntry' : {
        'meta_info' : _MetaInfoClass('CISCOCLASSBASEDQOSMIB.CbQosREDClassCfgTable.CbQosREDClassCfgEntry',
            False, 
            [
            _MetaInfoClassMember('cbQosConfigIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ''',
                'cbqosconfigindex',
                'CISCO-CLASS-BASED-QOS-MIB', True),
            _MetaInfoClassMember('cbQosREDValue', ATTRIBUTE, 'int' , None, None, 
                [(0, 63)], [], 
                '''                The IP precedence or IP DSCP of this entry.
                ''',
                'cbqosredvalue',
                'CISCO-CLASS-BASED-QOS-MIB', True),
            _MetaInfoClassMember('cbQosREDCfgMaxThreshold', ATTRIBUTE, 'int' , None, None, 
                [(1, 32768)], [], 
                '''                Maximum threshold in number of packets. When the
                average queue length exceeds this number, WRED drops 
                all packets with the specified IP precedence.
                cbQosREDCfgMaxThreshold object is superseded by 
                cbQosREDClassCfgMaxThreshold.
                ''',
                'cbqosredcfgmaxthreshold',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosREDCfgMinThreshold', ATTRIBUTE, 'int' , None, None, 
                [(1, 32768)], [], 
                '''                Minimum threshold in number of packets. When the
                average queue length reaches this number, WRED begins 
                to drop packets with the specified IP precedence.
                cbQosREDCfgMinThreshold object is superseded by 
                cbQosREDClassCfgMinThreshold.
                ''',
                'cbqosredcfgminthreshold',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosREDCfgPktDropProb', ATTRIBUTE, 'int' , None, None, 
                [(1, 65536)], [], 
                '''                Denominator for the fraction of packets dropped when
                the average queue depth is MaxDepthThreshold. For 
                example, if the denominator is 10, one out of every 10
                packets is dropped when the average queue is at the 
                MaxDepthThreshold.
                ''',
                'cbqosredcfgpktdropprob',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosREDClassCfgMaxThreshold', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The maximum WRED threshold value. When the average
                queue length exceeds this number, WRED drops all 
                packets according to REDMechanism specificed
                in cbQosREDCfgDscpPrec.
                ''',
                'cbqosredclasscfgmaxthreshold',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosREDClassCfgMaxThresholdTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The maximum WRED threshold value specified in
                milli-seconds.  The milli-second value is internally
                converted to bytes by using the bandwidth that
                is available for the class.
                ''',
                'cbqosredclasscfgmaxthresholdtime',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosREDClassCfgMaxThresholdUnit', REFERENCE_ENUM_CLASS, 'CbQosQueueUnitType_Enum' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CbQosQueueUnitType_Enum', 
                [], [], 
                '''                Represents the unit type to measure the RED Maximum thresholds.
                The objects covered is cbQosREDClassCfgMaxThreshold
                ''',
                'cbqosredclasscfgmaxthresholdunit',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosREDClassCfgMinThreshold', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The minimum WRED threshold value. When the average
                queue length reaches this number, WRED begins to 
                drop packets according to REDMechanism specificed
                in cbQosREDCfgDscpPrec.
                ''',
                'cbqosredclasscfgminthreshold',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosREDClassCfgMinThresholdTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The minimum WRED threshold value specified in
                milli-seconds.  The milli-second value is internally
                converted to bytes by using the bandwidth that
                is available for the class.
                ''',
                'cbqosredclasscfgminthresholdtime',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosREDClassCfgMinThresholdUnit', REFERENCE_ENUM_CLASS, 'CbQosQueueUnitType_Enum' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CbQosQueueUnitType_Enum', 
                [], [], 
                '''                Represents the unit type to measure the RED Minimum thresholds.
                The objects covered is cbQosREDClassCfgMinThreshold
                ''',
                'cbqosredclasscfgminthresholdunit',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosREDClassCfgThresholdUnit', REFERENCE_ENUM_CLASS, 'CbQosQueueUnitType_Enum' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CbQosQueueUnitType_Enum', 
                [], [], 
                '''                Represents the unit type to measure the RED thresholds.
                The objects covered are cbQosREDClassCfgMinThreshold
                and cbQosREDClassCfgMaxThreshold
                cbQosREDClassCfgThresholdUnit object is superseded by 
                cbQosREDClassCfgMinThreshold, cbQosREDClassCfgMaxThreshold.
                ''',
                'cbqosredclasscfgthresholdunit',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            ],
            'CISCO-CLASS-BASED-QOS-MIB',
            'cbQosREDClassCfgEntry',
            _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB'],
        'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB'
        ),
    },
    'CISCOCLASSBASEDQOSMIB.CbQosREDClassCfgTable' : {
        'meta_info' : _MetaInfoClass('CISCOCLASSBASEDQOSMIB.CbQosREDClassCfgTable',
            False, 
            [
            _MetaInfoClassMember('cbQosREDClassCfgEntry', REFERENCE_LIST, 'CbQosREDClassCfgEntry' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CISCOCLASSBASEDQOSMIB.CbQosREDClassCfgTable.CbQosREDClassCfgEntry', 
                [], [], 
                '''                Each entry in this table describes configuration information
                about a WRED Action.  The table holds the per IP precedence
                based WRED configuration parameters. 
                
                This table contains configuration information only,
                no statistics associated with it. Therefore, it is indexed
                by the cbQosConfigIndex and cbQosREDValue 
                of each WRED Action.
                ''',
                'cbqosredclasscfgentry',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            ],
            'CISCO-CLASS-BASED-QOS-MIB',
            'cbQosREDClassCfgTable',
            _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB'],
        'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB'
        ),
    },
    'CISCOCLASSBASEDQOSMIB.CbQosREDClassStatsTable.CbQosREDClassStatsEntry' : {
        'meta_info' : _MetaInfoClass('CISCOCLASSBASEDQOSMIB.CbQosREDClassStatsTable.CbQosREDClassStatsEntry',
            False, 
            [
            _MetaInfoClassMember('cbQosObjectsIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ''',
                'cbqosobjectsindex',
                'CISCO-CLASS-BASED-QOS-MIB', True),
            _MetaInfoClassMember('cbQosPolicyIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ''',
                'cbqospolicyindex',
                'CISCO-CLASS-BASED-QOS-MIB', True),
            _MetaInfoClassMember('cbQosREDValue', ATTRIBUTE, 'int' , None, None, 
                [(0, 63)], [], 
                '''                ''',
                'cbqosredvalue',
                'CISCO-CLASS-BASED-QOS-MIB', True),
            _MetaInfoClassMember('cbQosREDECNMarkByte', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The lower 32 bits count of bytes ecn marked when
                the number of packets in the associated queue was 
                greater than the minimum threshold and less than the
                maximum threshold.
                ''',
                'cbqosredecnmarkbyte',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosREDECNMarkByte64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The 64 bits count of bytes ecn marked when the
                number of packets in the associated queue was 
                greater than the minimum threshold and less than the
                maximum threshold.
                ''',
                'cbqosredecnmarkbyte64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosREDECNMarkByteOverflow', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The upper 32 bits count of bytes ecn marked when
                the number of packets in the associated queue was 
                greater than the minimum threshold and less than the
                maximum threshold.
                ''',
                'cbqosredecnmarkbyteoverflow',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosREDECNMarkPkt', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The lower 32 bits count of packets ecn marked when
                the number of packets in the associated queue was 
                greater than the minimum threshold and less than the
                maximum threshold.
                ''',
                'cbqosredecnmarkpkt',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosREDECNMarkPkt64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The 64 bits count of packets ecn marked when the
                number of packets in the associated queue was 
                greater than the minimum threshold and less than 
                the maximum threshold.
                ''',
                'cbqosredecnmarkpkt64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosREDECNMarkPktOverflow', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The upper 32 bits count of packets ecn marked when the
                number of packets in the associated queue was greater
                than the minimum threshold and less than the
                maximum threshold.
                ''',
                'cbqosredecnmarkpktoverflow',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosREDMeanQSize', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The average queue size computed and used by the
                WRED algorithm.
                ''',
                'cbqosredmeanqsize',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosREDMeanQSizeUnits', REFERENCE_ENUM_CLASS, 'CbQosQueueUnitType_Enum' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CbQosQueueUnitType_Enum', 
                [], [], 
                '''                Represents the unit type of cbQosREDMeanQSize
                object.
                ''',
                'cbqosredmeanqsizeunits',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosREDRandomDropByte', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The lower 32 bits count of bytes dropped when
                the number of packets in the associated queue was 
                greater than the minimum threshold and less than the
                maximum threshold.
                ''',
                'cbqosredrandomdropbyte',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosREDRandomDropByte64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The 64 bits count of bytes dropped when the number of
                packets in the associated queue was greater
                than the minimum threshold and less than the
                maximum threshold.
                ''',
                'cbqosredrandomdropbyte64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosREDRandomDropByteOverflow', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The upper 32 bits count of bytes dropped when the
                number of packets in the associated queue was greater
                than the minimum threshold and less than the
                maximum threshold.
                ''',
                'cbqosredrandomdropbyteoverflow',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosREDRandomDropPkt', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The lower 32 bits count of packets dropped when
                the number of packets in the associated queue was 
                greater than the minimum threshold and less than the
                maximum threshold.
                ''',
                'cbqosredrandomdroppkt',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosREDRandomDropPkt64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The 64 bits count of packets dropped when the number
                of packets in the associated queue was greater 
                than the minimum threshold and less than the
                maximum threshold.
                ''',
                'cbqosredrandomdroppkt64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosREDRandomDropPktOverflow', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The upper 32 bits count of packets dropped when the
                number of packets in the associated queue was greater
                than the minimum threshold and less than the
                maximum threshold.
                ''',
                'cbqosredrandomdroppktoverflow',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosREDTailDropByte', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The lower 32 bits count of bytes dropped when the
                number of packets in the associated queue was greater
                than the maximum threshold.
                ''',
                'cbqosredtaildropbyte',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosREDTailDropByte64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The 64 bits count of bytes dropped when the number of
                packets in the associated queue was greater
                than the maximum threshold.
                ''',
                'cbqosredtaildropbyte64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosREDTailDropByteOverflow', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The upper 32 bits count of bytes dropped when the
                number of packets in the associated queue was greater
                than the maximum threshold.
                ''',
                'cbqosredtaildropbyteoverflow',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosREDTailDropPkt', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The lower 32 bits count of packets dropped when the
                number of packets in the associated queue was greater
                than the maximum threshold.
                ''',
                'cbqosredtaildroppkt',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosREDTailDropPkt64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The 64 bits count of packets dropped when the number
                of packets in the associated queue was greater
                than the maximum threshold.
                ''',
                'cbqosredtaildroppkt64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosREDTailDropPktOverflow', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The upper 32 bits count of packets dropped when the
                number of packets in the associated queue was greater
                than the maximum threshold.
                ''',
                'cbqosredtaildroppktoverflow',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosREDTransmitByte', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The lower 32 bits count of octets trasmitted.
                ''',
                'cbqosredtransmitbyte',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosREDTransmitByte64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The 64 bits count of octets transmitted.
                ''',
                'cbqosredtransmitbyte64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosREDTransmitByteOverflow', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The upper 32 bits count of octets transmitted.
                ''',
                'cbqosredtransmitbyteoverflow',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosREDTransmitPkt', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The lower 32 bits count of bytes trasmitted.
                ''',
                'cbqosredtransmitpkt',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosREDTransmitPkt64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The 64 bits count of packets transmitted.
                ''',
                'cbqosredtransmitpkt64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosREDTransmitPktOverflow', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The upper 32 bits count of bytes transmitted.
                ''',
                'cbqosredtransmitpktoverflow',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            ],
            'CISCO-CLASS-BASED-QOS-MIB',
            'cbQosREDClassStatsEntry',
            _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB'],
        'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB'
        ),
    },
    'CISCOCLASSBASEDQOSMIB.CbQosREDClassStatsTable' : {
        'meta_info' : _MetaInfoClass('CISCOCLASSBASEDQOSMIB.CbQosREDClassStatsTable',
            False, 
            [
            _MetaInfoClassMember('cbQosREDClassStatsEntry', REFERENCE_LIST, 'CbQosREDClassStatsEntry' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CISCOCLASSBASEDQOSMIB.CbQosREDClassStatsTable.CbQosREDClassStatsEntry', 
                [], [], 
                '''                Each entry in this table describes the statistical
                information about per Precedence WRED Action. per Precedence
                WRED Action specific information you can find in this table 
                are : Random pkt/byte counters, and Tail drop pkt/byte 
                counters.
                
                This table contains per Precedence/dscp based statistical 
                information only, no configuration information associated 
                with it.  Therefore, it is indexed by the instance specific 
                IDs, and a per Precedence identifier: 
                cbQosPolicyIndex, cbQosObjectsIndex and cbQosREDValue.
                ''',
                'cbqosredclassstatsentry',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            ],
            'CISCO-CLASS-BASED-QOS-MIB',
            'cbQosREDClassStatsTable',
            _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB'],
        'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB'
        ),
    },
    'CISCOCLASSBASEDQOSMIB.CbQosServicePolicyTable.CbQosServicePolicyEntry' : {
        'meta_info' : _MetaInfoClass('CISCOCLASSBASEDQOSMIB.CbQosServicePolicyTable.CbQosServicePolicyEntry',
            False, 
            [
            _MetaInfoClassMember('cbQosPolicyIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                An arbitrary (system-assigned) index for all
                service policies (PolicyMap that has been attached
                to a given logical interface).
                ''',
                'cbqospolicyindex',
                'CISCO-CLASS-BASED-QOS-MIB', True),
            _MetaInfoClassMember('cbQosAtmVCI', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                VCI for the ATMVC to which this service is attached.
                This field only make sense if the service policy is
                attached to a ATM VC.
                ''',
                'cbqosatmvci',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosAtmVPI', ATTRIBUTE, 'int' , None, None, 
                [(0, 4095)], [], 
                '''                VPI for the ATMVC to which this service is attached.
                This field only make sense if the service policy is
                attached to a ATM VC.
                ''',
                'cbqosatmvpi',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosEntityIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 2147483647)], [], 
                '''                In cases where the policy is attached to an entity
                e.g. control-plane, this object represents the
                entity physical index of the entity to which the
                policy has been attached. A value zero may be 
                returned if the policy is not attached to a physical
                entity or the entPhysicalTable is not supported on 
                the SNMP agent.
                ''',
                'cbqosentityindex',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosEVC', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                for the EVC to which this service is attached.
                This field only make sense if the service policy is
                attached to an EVC.
                ''',
                'cbqosevc',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosFrDLCI', ATTRIBUTE, 'int' , None, None, 
                [(0, 1023)], [], 
                '''                DLCI for the FRVC to which this service is attached.
                This field only make sense if the service policy is
                attached to a Frame Relay DLCI.
                ''',
                'cbqosfrdlci',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosIfIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ifIndex for the interface to which this service
                is attached. This field makes sense only if the
                logical interface has a snmp ifIndex. For e.g. the
                value of this field is meaningless when the
                cbQosIfType is controlPlane.
                ''',
                'cbqosifindex',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosIfType', REFERENCE_ENUM_CLASS, 'InterfaceType_Enum' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'InterfaceType_Enum', 
                [], [], 
                '''                This describes the logical interface/media type to
                which this service policy is attached.
                ''',
                'cbqosiftype',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosParentPolicyIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The value refering to service-policy index of a virtual
                interface on which PolicyMap applied directly. Value set would
                imply the entry is for a physical interface which is a member
                of a virtual interface. Value zero implies the entry is for a 
                interface on which PolicyMap applied directly.
                ''',
                'cbqosparentpolicyindex',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPolicyDirection', REFERENCE_ENUM_CLASS, 'TrafficDirection_Enum' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'TrafficDirection_Enum', 
                [], [], 
                '''                This indicates the direction of traffic for which
                this service policy is applied.
                ''',
                'cbqospolicydirection',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPolicyDiscontinuityTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The value of sysUpTime on the most recent occasion at which
                any one or more objects of cbQosServicePolicyEntry table for a
                given instance suffered a discontinuity. If no such
                discontinuities have occurred since the last re-initialization
                of the local management subsystem, this object contains a zero
                value.
                ''',
                'cbqospolicydiscontinuitytime',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosVlanIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                If the service policy is attached to a particular
                vlan on a trunk or multi-vlan access port, then this
                object specifies the corresponding VLAN. In all other
                cases the value of this object is '0'.
                ''',
                'cbqosvlanindex',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            ],
            'CISCO-CLASS-BASED-QOS-MIB',
            'cbQosServicePolicyEntry',
            _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB'],
        'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB'
        ),
    },
    'CISCOCLASSBASEDQOSMIB.CbQosServicePolicyTable' : {
        'meta_info' : _MetaInfoClass('CISCOCLASSBASEDQOSMIB.CbQosServicePolicyTable',
            False, 
            [
            _MetaInfoClassMember('cbQosServicePolicyEntry', REFERENCE_LIST, 'CbQosServicePolicyEntry' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CISCOCLASSBASEDQOSMIB.CbQosServicePolicyTable.CbQosServicePolicyEntry', 
                [], [], 
                '''                Each entry in this table describes to which a logical
                interface a given policymap is attached.  Depending on 
                the logical interface/media type, some fields may have
                meaningful values, and some may not.  Please see each
                individual descriptions.
                ''',
                'cbqosservicepolicyentry',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            ],
            'CISCO-CLASS-BASED-QOS-MIB',
            'cbQosServicePolicyTable',
            _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB'],
        'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB'
        ),
    },
    'CISCOCLASSBASEDQOSMIB.CbQosSetCfgTable.CbQosSetCfgEntry' : {
        'meta_info' : _MetaInfoClass('CISCOCLASSBASEDQOSMIB.CbQosSetCfgTable.CbQosSetCfgEntry',
            False, 
            [
            _MetaInfoClassMember('cbQosConfigIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ''',
                'cbqosconfigindex',
                'CISCO-CLASS-BASED-QOS-MIB', True),
            _MetaInfoClassMember('cbQosSetCfgDei', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether the DEI bit is set in the topmost 802.1ad
                header.
                ''',
                'cbqossetcfgdei',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosSetCfgDeiImposition', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether the DEI bit is set in the imposed 802.1ad
                header.
                ''',
                'cbqossetcfgdeiimposition',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosSetCfgDiscardClassValue', ATTRIBUTE, 'int' , None, None, 
                [(0, 7)], [], 
                '''                The Discard Class value at which the packet
                is being set by the packet marking feature.
                ''',
                'cbqossetcfgdiscardclassvalue',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosSetCfgFeature', REFERENCE_BITS, 'SetFeatureType_Bits' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'SetFeatureType_Bits', 
                [], [], 
                '''                The bit-wise position of each packet marking feature.
                ''',
                'cbqossetcfgfeature',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosSetCfgFrDe', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The Discard Eligibility (DE) bit is used to indicate that a
                frame has lower importance than other frames. The DE bit is part
                of the Address field in the Frame Relay frame header.
                    DTE devices can set the value of the DE bit of a frame to 1
                to indicate that the frame has lower importance than other
                frames. When the network becomes congested, DCE devices will
                discard frames with the DE bit set before discarding those that
                do not. This reduces the likelihood of critical data being
                dropped by Frame Relay DCE devices during periods of
                congestion.
                ''',
                'cbqossetcfgfrde',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosSetCfgFrFecnBecn', ATTRIBUTE, 'int' , None, None, 
                [(0, 99)], [], 
                '''                This is a configurable parameter in percentage of the
                queue size.  When the current queue size out of the
                queue limit is greater than this parameter, both 
                Frame Relay FECN and BECN bits will be set for
                Frame Relay congestion notification mechanism.
                ''',
                'cbqossetcfgfrfecnbecn',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosSetCfgIpDSCPTunnelValue', ATTRIBUTE, 'int' , None, None, 
                [(0, 63)], [], 
                '''                The IP DSCP value at which the packet is being set
                by the packet marking feature.
                ''',
                'cbqossetcfgipdscptunnelvalue',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosSetCfgIpDSCPValue', ATTRIBUTE, 'int' , None, None, 
                [(0, 63)], [], 
                '''                The IP DSCP value at which the packet is being set
                by the packet marking feature.
                ''',
                'cbqossetcfgipdscpvalue',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosSetCfgIpPrecedenceTunnelValue', ATTRIBUTE, 'int' , None, None, 
                [(0, 7)], [], 
                '''                The IP precedence value at which the packet is being
                set by the packet marking feature.
                ''',
                'cbqossetcfgipprecedencetunnelvalue',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosSetCfgIpPrecedenceValue', ATTRIBUTE, 'int' , None, None, 
                [(0, 7)], [], 
                '''                The IP precedence value at which the packet is being
                set by the packet marking feature.
                ''',
                'cbqossetcfgipprecedencevalue',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosSetCfgL2CosInnerValue', ATTRIBUTE, 'int' , None, None, 
                [(0, 7)], [], 
                '''                The value to be set in the 802.1p priority field in the inner
                802.1q VLAN tag (QinQ).  This object is applicable when
                cbQosSetCfgFeature has the 'l2CosInner' bit set.
                ''',
                'cbqossetcfgl2cosinnervalue',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosSetCfgL2CosValue', ATTRIBUTE, 'int' , None, None, 
                [(0, 7)], [], 
                '''                The Layer 2 Cos value at which the packet is being
                set by the packet marking feature.
                ''',
                'cbqossetcfgl2cosvalue',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosSetCfgMplsExpTopMostValue', ATTRIBUTE, 'int' , None, None, 
                [(0, 7)], [], 
                '''                The MPLS experimental value on the topmost label
                at which the packet is being set by the packet marking
                feature.
                ''',
                'cbqossetcfgmplsexptopmostvalue',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosSetCfgMplsExpValue', ATTRIBUTE, 'int' , None, None, 
                [(0, 7)], [], 
                '''                The MPLS experimental value at which the packet
                is being set by the packet marking feature.
                ''',
                'cbqossetcfgmplsexpvalue',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosSetCfgQosGroupValue', ATTRIBUTE, 'int' , None, None, 
                [(0, 99)], [], 
                '''                The QoS Group number at which the packet is being
                set by the packet marking feature.
                ''',
                'cbqossetcfgqosgroupvalue',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosSetCfgSrpPriority', ATTRIBUTE, 'int' , None, None, 
                [(0, 7)], [], 
                '''                The SRP Priority value at which the packet is being set
                by the packet marking feature.  The higher the value the
                higher the priority.  SRP is a Cisco developed protocol.
                RFC 2892: The Cisco SRP MAC Layer Protocol.
                ''',
                'cbqossetcfgsrppriority',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            ],
            'CISCO-CLASS-BASED-QOS-MIB',
            'cbQosSetCfgEntry',
            _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB'],
        'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB'
        ),
    },
    'CISCOCLASSBASEDQOSMIB.CbQosSetCfgTable' : {
        'meta_info' : _MetaInfoClass('CISCOCLASSBASEDQOSMIB.CbQosSetCfgTable',
            False, 
            [
            _MetaInfoClassMember('cbQosSetCfgEntry', REFERENCE_LIST, 'CbQosSetCfgEntry' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CISCOCLASSBASEDQOSMIB.CbQosSetCfgTable.CbQosSetCfgEntry', 
                [], [], 
                '''                Each entry in this table describes configuration information
                about a Packet Marking Action.  The table holds Packet
                Marking configuration parameters, such as type of packet
                marking and values being set to.
                
                This table contains configuration information only,
                no statistics associated with it. Therefore, it is indexed
                by the cbQosConfigIndex.
                ''',
                'cbqossetcfgentry',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            ],
            'CISCO-CLASS-BASED-QOS-MIB',
            'cbQosSetCfgTable',
            _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB'],
        'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB'
        ),
    },
    'CISCOCLASSBASEDQOSMIB.CbQosSetStatsTable.CbQosSetStatsEntry' : {
        'meta_info' : _MetaInfoClass('CISCOCLASSBASEDQOSMIB.CbQosSetStatsTable.CbQosSetStatsEntry',
            False, 
            [
            _MetaInfoClassMember('cbQosObjectsIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ''',
                'cbqosobjectsindex',
                'CISCO-CLASS-BASED-QOS-MIB', True),
            _MetaInfoClassMember('cbQosPolicyIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ''',
                'cbqospolicyindex',
                'CISCO-CLASS-BASED-QOS-MIB', True),
            _MetaInfoClassMember('cbQosSetAtmClpPkt64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The 64 bits count of packets whose ATM CLP Bit is
                marked by Set feature.
                ''',
                'cbqossetatmclppkt64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosSetDiscardClassPkt64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The 64 bits count of packets whose Discard Class field
                is marked by Set feature.
                ''',
                'cbqossetdiscardclasspkt64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosSetDscpPkt64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The 64 bits count of packets whose DSCP field is
                marked by Set feature.
                ''',
                'cbqossetdscppkt64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosSetDscpTunnelPkt64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The 64 bits count of packets whose DSCP Tunnel field is
                marked by Set feature.
                ''',
                'cbqossetdscptunnelpkt64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosSetFrDePkt64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The 64 bits count of packets whose Frame Relay DE Bit
                is marked by Set feature.
                ''',
                'cbqossetfrdepkt64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosSetFrFecnBecnPkt64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The 64 bits count of packets whose Frame Relay FECN
                BECN field is marked by Set feature.
                ''',
                'cbqossetfrfecnbecnpkt64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosSetL2CosPkt64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The 64 bits count of packets whose Layer 2 Cos field is
                marked by Set feature.
                ''',
                'cbqossetl2cospkt64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosSetMplsExpImpositionPkt64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The 64 bits count of packets whose MPLS Experimental
                Imposition field is marked by Set feature.
                ''',
                'cbqossetmplsexpimpositionpkt64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosSetMplsExpTopMostPkt64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The 64 bits count of packets whose MPLS Experimental
                TopMost field is marked by Set feature.
                ''',
                'cbqossetmplsexptopmostpkt64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosSetPrecedencePkt64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The 64 bits count of packets whose Precedence field is
                marked by Set feature.
                ''',
                'cbqossetprecedencepkt64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosSetPrecedenceTunnelPkt64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The 64 bits count of packets whose Precedence Tunnel
                field is marked by Set feature.
                ''',
                'cbqossetprecedencetunnelpkt64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosSetQosGroupPkt64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The 64 bits count of packets whose Qos Group field is
                marked by Set feature.
                ''',
                'cbqossetqosgrouppkt64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosSetSrpPriorityPkt64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The 64 bits count of packets whose SRP Priority field
                is marked by Set feature.
                ''',
                'cbqossetsrpprioritypkt64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            ],
            'CISCO-CLASS-BASED-QOS-MIB',
            'cbQosSetStatsEntry',
            _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB'],
        'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB'
        ),
    },
    'CISCOCLASSBASEDQOSMIB.CbQosSetStatsTable' : {
        'meta_info' : _MetaInfoClass('CISCOCLASSBASEDQOSMIB.CbQosSetStatsTable',
            False, 
            [
            _MetaInfoClassMember('cbQosSetStatsEntry', REFERENCE_LIST, 'CbQosSetStatsEntry' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CISCOCLASSBASEDQOSMIB.CbQosSetStatsTable.CbQosSetStatsEntry', 
                [], [], 
                '''                Each entry in this table describes the packets that
                marked by each marking type.
                
                This table contains statistical information only,
                no configuration information associated with it.
                Therefore, it is indexed by the instance specific
                IDs, namely cbQosPolicyIndex and cbQosObjectsIndex.
                ''',
                'cbqossetstatsentry',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            ],
            'CISCO-CLASS-BASED-QOS-MIB',
            'cbQosSetStatsTable',
            _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB'],
        'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB'
        ),
    },
    'CISCOCLASSBASEDQOSMIB.CbQosTSCfgTable.CbQosTSCfgEntry' : {
        'meta_info' : _MetaInfoClass('CISCOCLASSBASEDQOSMIB.CbQosTSCfgTable.CbQosTSCfgEntry',
            False, 
            [
            _MetaInfoClassMember('cbQosConfigIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ''',
                'cbqosconfigindex',
                'CISCO-CLASS-BASED-QOS-MIB', True),
            _MetaInfoClassMember('cbQosTSCfgAdaptiveEnabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object indicates is adaptive traffic-shaping
                has been enabled.
                ''',
                'cbqostscfgadaptiveenabled',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosTSCfgAdaptiveRate', ATTRIBUTE, 'int' , None, None, 
                [(8000, 154400000)], [], 
                '''                This object represents the current adaptive traffic
                shaping rate.
                ''',
                'cbqostscfgadaptiverate',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosTSCfgBurstSize', ATTRIBUTE, 'int' , None, None, 
                [(256, 154400000)], [], 
                '''                The amount of traffic, in bits, in excess of the
                committed traffic-shaping rate that will be
                instantaneously permitted by this feature.
                
                cbQosTSCfgBurstSize object is superseded by cbQosTSCfgBurstSize64.
                ''',
                'cbqostscfgburstsize',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosTSCfgBurstSize64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                This object indicates the the amount of traffic, in bits, in
                excess of the committed traffic-shaping rate that will be
                instantaneously permitted by this feature.
                
                If a device implements cbQosTSCfgBurstSize64, then
                it should not implement cbQosTSCfgBurstSize.
                ''',
                'cbqostscfgburstsize64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosTSCfgBurstTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The amount of traffic, in ms, in excess of the
                committed traffic-shaping rate that will be
                instantaneously permitted by this feature.
                The milli-second value is internally converted to
                bits by using the bandwidth that is available for
                the class.
                ''',
                'cbqostscfgbursttime',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosTSCfgExtBurstSize', ATTRIBUTE, 'int' , None, None, 
                [(0, 154400000)], [], 
                '''                The amount of traffic, in bits, in excess of the
                burst limit, which may be conditionally permitted
                by traffic-shaping feature.
                
                cbQosTSCfgExtBurstSize object is superseded by
                cbQosTSCfgExtBurstSize64.
                ''',
                'cbqostscfgextburstsize',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosTSCfgExtBurstSize64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                This object indicates the amount of traffic, in bits, in excess
                of the burst limit, which may be conditionally permitted
                by traffic-shaping feature. 
                
                If a device implements cbQosTSCfgExtBurstSize64, then
                it should not implement cbQosTSCfgExtBurstSize.
                ''',
                'cbqostscfgextburstsize64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosTSCfgExtBurstTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The amount of traffic, in ms, in excess of the
                burst limit, which may be conditionnally permitted
                by traffic-shaping feature.
                The milli-second value is internally converted to
                bits by using the bandwidth that is available for
                the class.
                ''',
                'cbqostscfgextbursttime',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosTSCfgLimitType', REFERENCE_ENUM_CLASS, 'TrafficShapingLimit_Enum' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'TrafficShapingLimit_Enum', 
                [], [], 
                '''                This object indicates if traffic-shaping is limiting
                traffic based on the peak rate or the average rate.
                ''',
                'cbqostscfglimittype',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosTSCfgPercentRateValue', ATTRIBUTE, 'int' , None, None, 
                [(0, 100)], [], 
                '''                The committed traffic-shaping rate in percentage.
                Its value is valid only when cbQosTSCfgRateType 
                equals to 2.
                ''',
                'cbqostscfgpercentratevalue',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosTSCfgRate', ATTRIBUTE, 'int' , None, None, 
                [(0, 2147483647)], [], 
                '''                The committed traffic-shaping rate.  This is the
                sustained rate permitted by the traffic-shaping.
                ''',
                'cbqostscfgrate',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosTSCfgRate64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The committed shape rate. This is the sustained
                rate permitted by shaping. This object represents 
                the 64 bit value of object cbQosTSCfgRate
                ''',
                'cbqostscfgrate64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosTSCfgRateType', REFERENCE_ENUM_CLASS, 'CbQosRateType_Enum' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CbQosRateType_Enum', 
                [], [], 
                '''                The rate type that configured for traffic-shaping.
                1 means rate is configured in bps.
                2 means rate is configured in percentage.
                4 means rates are configured in parts per-thousand.
                5 means rates are configured in parts per-million.
                ''',
                'cbqostscfgratetype',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            ],
            'CISCO-CLASS-BASED-QOS-MIB',
            'cbQosTSCfgEntry',
            _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB'],
        'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB'
        ),
    },
    'CISCOCLASSBASEDQOSMIB.CbQosTSCfgTable' : {
        'meta_info' : _MetaInfoClass('CISCOCLASSBASEDQOSMIB.CbQosTSCfgTable',
            False, 
            [
            _MetaInfoClassMember('cbQosTSCfgEntry', REFERENCE_LIST, 'CbQosTSCfgEntry' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CISCOCLASSBASEDQOSMIB.CbQosTSCfgTable.CbQosTSCfgEntry', 
                [], [], 
                '''                Each entry in this table describes configuration information
                about a traffic-shaping Action.  The table holds Traffic
                Shaping configuration parameters, such as rate, burst size, 
                and Shaping types.
                
                This table contains configuration information only,
                no statistics associated with it. Therefore, it is indexed
                by the cbQosConfigIndex.
                ''',
                'cbqostscfgentry',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            ],
            'CISCO-CLASS-BASED-QOS-MIB',
            'cbQosTSCfgTable',
            _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB'],
        'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB'
        ),
    },
    'CISCOCLASSBASEDQOSMIB.CbQosTSStatsTable.CbQosTSStatsEntry' : {
        'meta_info' : _MetaInfoClass('CISCOCLASSBASEDQOSMIB.CbQosTSStatsTable.CbQosTSStatsEntry',
            False, 
            [
            _MetaInfoClassMember('cbQosObjectsIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ''',
                'cbqosobjectsindex',
                'CISCO-CLASS-BASED-QOS-MIB', True),
            _MetaInfoClassMember('cbQosPolicyIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ''',
                'cbqospolicyindex',
                'CISCO-CLASS-BASED-QOS-MIB', True),
            _MetaInfoClassMember('cbQosTSStatsActive', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object indicates the current traffic-shaping
                state. When traffic-shaping is enabled and the traffic 
                rate exceeds the shape rate, traffic-shaping
                is considered to be active.  Otherwise, it is 
                considered inactive.
                ''',
                'cbqostsstatsactive',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosTSStatsCurrentQSize', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object indicates the current traffic-shaping
                queue depth in packets.
                ''',
                'cbqostsstatscurrentqsize',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosTSStatsDelayedByte', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object represents the lower 32 bits counter of
                octets that have been delayed.
                ''',
                'cbqostsstatsdelayedbyte',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosTSStatsDelayedByte64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                This object represents the 64 bits counter of
                octets that have been delayed.
                ''',
                'cbqostsstatsdelayedbyte64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosTSStatsDelayedByteOverflow', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object represents the upper 32 bits counter of
                octets that have been delayed.
                ''',
                'cbqostsstatsdelayedbyteoverflow',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosTSStatsDelayedPkt', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object represents the lower 32 bits counter of
                packets that have been delayed.
                ''',
                'cbqostsstatsdelayedpkt',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosTSStatsDelayedPkt64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                This object represents the 64 bits counter of
                packets that have been delayed.
                ''',
                'cbqostsstatsdelayedpkt64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosTSStatsDelayedPktOverflow', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object represents the upper 32 bits counter of
                packets that have been delayed.
                ''',
                'cbqostsstatsdelayedpktoverflow',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosTSStatsDropByte', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object represents the lower 32 bits counter of
                octets that have been dropped during shaping.
                ''',
                'cbqostsstatsdropbyte',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosTSStatsDropByte64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                This object represents the 64 bits counter of
                octets that have been dropped during shaping.
                ''',
                'cbqostsstatsdropbyte64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosTSStatsDropByteOverflow', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object represents the upper 32 bits counter of
                octets that have been dropped during shaping.
                ''',
                'cbqostsstatsdropbyteoverflow',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosTSStatsDropPkt', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object represents the lower 32 bits counter of
                packets that have been dropped during shaping.
                ''',
                'cbqostsstatsdroppkt',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosTSStatsDropPkt64', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                This object represents the 64 bits counter of
                packets that have been dropped during shaping.
                ''',
                'cbqostsstatsdroppkt64',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosTSStatsDropPktOverflow', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object represents the upper 32 bits counter of
                packets that have been dropped during shaping.
                ''',
                'cbqostsstatsdroppktoverflow',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            ],
            'CISCO-CLASS-BASED-QOS-MIB',
            'cbQosTSStatsEntry',
            _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB'],
        'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB'
        ),
    },
    'CISCOCLASSBASEDQOSMIB.CbQosTSStatsTable' : {
        'meta_info' : _MetaInfoClass('CISCOCLASSBASEDQOSMIB.CbQosTSStatsTable',
            False, 
            [
            _MetaInfoClassMember('cbQosTSStatsEntry', REFERENCE_LIST, 'CbQosTSStatsEntry' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CISCOCLASSBASEDQOSMIB.CbQosTSStatsTable.CbQosTSStatsEntry', 
                [], [], 
                '''                Each entry in this table describes the statistical
                information about traffic-shaping Action. Traffic-shaping 
                Action specific information you can find in this table are : 
                various delay/drop pkt/byte counters, state of feature,
                and Q size.
                
                This table contains statistical information only,
                no configuration information associated with it. 
                Therefore, it is indexed by the instance specific IDs, 
                such as cbQosPolicyIndex and cbQosObjectsIndex.
                ''',
                'cbqostsstatsentry',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            ],
            'CISCO-CLASS-BASED-QOS-MIB',
            'cbQosTSStatsTable',
            _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB'],
        'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB'
        ),
    },
    'CISCOCLASSBASEDQOSMIB.CbQosTableMapCfgTable.CbQosTableMapCfgEntry.CbQosTableMapCfgBehavior_Enum' : _MetaInfoEnum('CbQosTableMapCfgBehavior_Enum', 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB',
        {
            'value':'VALUE',
            'copy':'COPY',
            'ignore':'IGNORE',
        }, 'CISCO-CLASS-BASED-QOS-MIB', _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB']),
    'CISCOCLASSBASEDQOSMIB.CbQosTableMapCfgTable.CbQosTableMapCfgEntry' : {
        'meta_info' : _MetaInfoClass('CISCOCLASSBASEDQOSMIB.CbQosTableMapCfgTable.CbQosTableMapCfgEntry',
            False, 
            [
            _MetaInfoClassMember('cbQosTableMapCfgIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                An arbitrary (system-assigned) index for tablemap.
                ''',
                'cbqostablemapcfgindex',
                'CISCO-CLASS-BASED-QOS-MIB', True),
            _MetaInfoClassMember('cbQosTableMapCfgBehavior', REFERENCE_ENUM_CLASS, 'CbQosTableMapCfgBehavior_Enum' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CISCOCLASSBASEDQOSMIB.CbQosTableMapCfgTable.CbQosTableMapCfgEntry.CbQosTableMapCfgBehavior_Enum', 
                [], [], 
                '''                The behavior of a tablemap.
                value(1)    Always set to-value to be a configurable
                            default value <0-99> which is defined in
                            cbQosTableMapCfgDftValue.
                
                copy(2)     Always copy from-value to to-value in case
                            the from-value is not found in the tablemap.
                            This is the default behavior for a tablemap.
                
                ignore(3)   Ignore to set to-value when from-value
                            is not found in the tablemap.
                ''',
                'cbqostablemapcfgbehavior',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosTableMapCfgDftValue', ATTRIBUTE, 'int' , None, None, 
                [(0, 99)], [], 
                '''                The configurable default value used when
                cbQosTableMapCfgBehavior is value(1).
                ''',
                'cbqostablemapcfgdftvalue',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosTableMapCfgName', ATTRIBUTE, 'str' , None, None, 
                [], ['\\p{IsBasicLatin}{0,255}'], 
                '''                Name of the tablemap.
                ''',
                'cbqostablemapcfgname',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            ],
            'CISCO-CLASS-BASED-QOS-MIB',
            'cbQosTableMapCfgEntry',
            _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB'],
        'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB'
        ),
    },
    'CISCOCLASSBASEDQOSMIB.CbQosTableMapCfgTable' : {
        'meta_info' : _MetaInfoClass('CISCOCLASSBASEDQOSMIB.CbQosTableMapCfgTable',
            False, 
            [
            _MetaInfoClassMember('cbQosTableMapCfgEntry', REFERENCE_LIST, 'CbQosTableMapCfgEntry' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CISCOCLASSBASEDQOSMIB.CbQosTableMapCfgTable.CbQosTableMapCfgEntry', 
                [], [], 
                '''                Each entry in this table describes configuration
                information about a tablemap name, behavior and default
                value.  Each cbQosTableMapCfgName is a unique character
                string in QOS.  This table contains configuration
                information only, no statistics associated with it.
                ''',
                'cbqostablemapcfgentry',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            ],
            'CISCO-CLASS-BASED-QOS-MIB',
            'cbQosTableMapCfgTable',
            _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB'],
        'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB'
        ),
    },
    'CISCOCLASSBASEDQOSMIB.CbQosTableMapSetCfgTable.CbQosTableMapSetCfgEntry' : {
        'meta_info' : _MetaInfoClass('CISCOCLASSBASEDQOSMIB.CbQosTableMapSetCfgTable.CbQosTableMapSetCfgEntry',
            False, 
            [
            _MetaInfoClassMember('cbQosConfigIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ''',
                'cbqosconfigindex',
                'CISCO-CLASS-BASED-QOS-MIB', True),
            _MetaInfoClassMember('cbQosTMSetIpDscpFromType', REFERENCE_ENUM_CLASS, 'CbQosTMSetType_Enum' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CbQosTMSetType_Enum', 
                [], [], 
                '''                The packet marking type whose value will be converted
                to a to-value based on a pre-configured table-map.  The
                to-value will then be used to set IpDSCP.
                ''',
                'cbqostmsetipdscpfromtype',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosTMSetIpDscpMapName', ATTRIBUTE, 'str' , None, None, 
                [], ['\\p{IsBasicLatin}{0,255}'], 
                '''                The name of a pre-configured table-map used to convert
                and set IpDSCP value.
                ''',
                'cbqostmsetipdscpmapname',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosTMSetIpPrecedenceFromType', REFERENCE_ENUM_CLASS, 'CbQosTMSetType_Enum' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CbQosTMSetType_Enum', 
                [], [], 
                '''                The packet marking type whose value will be converted
                to a to-value based on a pre-configured table-map.  The
                to-value will then be used to set IpPrecedence.
                ''',
                'cbqostmsetipprecedencefromtype',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosTMSetIpPrecedenceMapName', ATTRIBUTE, 'str' , None, None, 
                [], ['\\p{IsBasicLatin}{0,255}'], 
                '''                The name of a pre-configured table-map used to convert
                and set IpPrecedence value.
                ''',
                'cbqostmsetipprecedencemapname',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosTMSetL2CosFromType', REFERENCE_ENUM_CLASS, 'CbQosTMSetType_Enum' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CbQosTMSetType_Enum', 
                [], [], 
                '''                The packet marking type whose value will be converted
                to a to-value based on a pre-configured table-map.  The
                to-value will then be used to set L2Cos.
                ''',
                'cbqostmsetl2cosfromtype',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosTMSetL2CosMapName', ATTRIBUTE, 'str' , None, None, 
                [], ['\\p{IsBasicLatin}{0,255}'], 
                '''                The name of a pre-configured table-map used to convert
                and set L2Cos value.
                ''',
                'cbqostmsetl2cosmapname',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosTMSetMplsExpImpFromType', REFERENCE_ENUM_CLASS, 'CbQosTMSetType_Enum' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CbQosTMSetType_Enum', 
                [], [], 
                '''                The packet marking type whose value will be converted
                to a to-value based on a pre-configured table-map.  The
                to-value will then be used to set MplsExpImposition.
                ''',
                'cbqostmsetmplsexpimpfromtype',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosTMSetMplsExpImpMapName', ATTRIBUTE, 'str' , None, None, 
                [], ['\\p{IsBasicLatin}{0,255}'], 
                '''                The name of a pre-configured table-map used to convert
                and set MplsExpImposition value.
                ''',
                'cbqostmsetmplsexpimpmapname',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosTMSetMplsExpTopFromType', REFERENCE_ENUM_CLASS, 'CbQosTMSetType_Enum' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CbQosTMSetType_Enum', 
                [], [], 
                '''                The packet marking type whose value will be converted
                to a to-value based on a pre-configured table-map.  The
                to-value will then be used to set MplsExpTopMost.
                ''',
                'cbqostmsetmplsexptopfromtype',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosTMSetMplsExpTopMapName', ATTRIBUTE, 'str' , None, None, 
                [], ['\\p{IsBasicLatin}{0,255}'], 
                '''                The name of a pre-configured table-map used to convert
                and set MplsExpTopMost value.
                ''',
                'cbqostmsetmplsexptopmapname',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosTMSetQosGroupFromType', REFERENCE_ENUM_CLASS, 'CbQosTMSetType_Enum' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CbQosTMSetType_Enum', 
                [], [], 
                '''                The packet marking type whose value will be converted
                to a to-value based on a pre-configured table-map.  The
                to-value will then be used to set QosGroup.
                ''',
                'cbqostmsetqosgroupfromtype',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosTMSetQosGroupMapName', ATTRIBUTE, 'str' , None, None, 
                [], ['\\p{IsBasicLatin}{0,255}'], 
                '''                The name of a pre-configured table-map used to convert
                and set QosGroup value.
                ''',
                'cbqostmsetqosgroupmapname',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            ],
            'CISCO-CLASS-BASED-QOS-MIB',
            'cbQosTableMapSetCfgEntry',
            _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB'],
        'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB'
        ),
    },
    'CISCOCLASSBASEDQOSMIB.CbQosTableMapSetCfgTable' : {
        'meta_info' : _MetaInfoClass('CISCOCLASSBASEDQOSMIB.CbQosTableMapSetCfgTable',
            False, 
            [
            _MetaInfoClassMember('cbQosTableMapSetCfgEntry', REFERENCE_LIST, 'CbQosTableMapSetCfgEntry' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CISCOCLASSBASEDQOSMIB.CbQosTableMapSetCfgTable.CbQosTableMapSetCfgEntry', 
                [], [], 
                '''                Each entry in this table describes configuration
                information for an Enhanced Packet Marking Action.
                The enhanced packet marking action uses a pre-configured
                table-map to do the from-value to to-value conversion.
                The packet marking to-type and from-type relationship
                can be established by using the table-map.
                Following is an example:
                cbQosTMSetIpDscpFromType == qosGroup(3)
                cbQosTMSetIpDscpMapName == 'MyTableMap',
                it means that table-map 'MyTableMap' will be used to
                convert the QosGroup value and the converted value will
                be used to set IpDSCP.
                
                cbQosConfigIndex is drived directly from
                cbQosSetCfgTable to keep the 1-to-1 mapping between
                two tables.  This table contains configuration
                information only, no statistics associated with it.
                ''',
                'cbqostablemapsetcfgentry',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            ],
            'CISCO-CLASS-BASED-QOS-MIB',
            'cbQosTableMapSetCfgTable',
            _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB'],
        'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB'
        ),
    },
    'CISCOCLASSBASEDQOSMIB.CbQosTableMapValueCfgTable.CbQosTableMapValueCfgEntry' : {
        'meta_info' : _MetaInfoClass('CISCOCLASSBASEDQOSMIB.CbQosTableMapValueCfgTable.CbQosTableMapValueCfgEntry',
            False, 
            [
            _MetaInfoClassMember('cbQosTableMapCfgIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ''',
                'cbqostablemapcfgindex',
                'CISCO-CLASS-BASED-QOS-MIB', True),
            _MetaInfoClassMember('cbQosTableMapValueCfgFrom', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This is the from-value in the tablemap.  If
                cbQosTableMapCfgBehavior equals to either copy(2) or
                ignore(3), when the content in the from-type(e.g.,
                cbQosTMSetIpDscpFromType) equals to this value, the
                value in the to-type(e.g., IpDscp) will be set to
                cbQosTableMapValueCfgTo.  Each tablemap can configure
                multiple from-value/to-value pairs.
                ''',
                'cbqostablemapvaluecfgfrom',
                'CISCO-CLASS-BASED-QOS-MIB', True),
            _MetaInfoClassMember('cbQosTableMapValueCfgTo', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This is the to-value in the tablemap.  Its usage is
                described in cbQosTableMapValueCfgFrom.
                ''',
                'cbqostablemapvaluecfgto',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            ],
            'CISCO-CLASS-BASED-QOS-MIB',
            'cbQosTableMapValueCfgEntry',
            _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB'],
        'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB'
        ),
    },
    'CISCOCLASSBASEDQOSMIB.CbQosTableMapValueCfgTable' : {
        'meta_info' : _MetaInfoClass('CISCOCLASSBASEDQOSMIB.CbQosTableMapValueCfgTable',
            False, 
            [
            _MetaInfoClassMember('cbQosTableMapValueCfgEntry', REFERENCE_LIST, 'CbQosTableMapValueCfgEntry' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CISCOCLASSBASEDQOSMIB.CbQosTableMapValueCfgTable.CbQosTableMapValueCfgEntry', 
                [], [], 
                '''                Each entry in this table specifies a from-value to
                to-value conversion pair for a given tablemap.
                This table contains configuration information only,
                no statistics associated with it.
                ''',
                'cbqostablemapvaluecfgentry',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            ],
            'CISCO-CLASS-BASED-QOS-MIB',
            'cbQosTableMapValueCfgTable',
            _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB'],
        'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB'
        ),
    },
    'CISCOCLASSBASEDQOSMIB' : {
        'meta_info' : _MetaInfoClass('CISCOCLASSBASEDQOSMIB',
            False, 
            [
            _MetaInfoClassMember('cbQosATMPVCPolicyTable', REFERENCE_CLASS, 'CbQosATMPVCPolicyTable' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CISCOCLASSBASEDQOSMIB.CbQosATMPVCPolicyTable', 
                [], [], 
                '''                This table describes the policies that are attached to a
                ATM PVC.
                ''',
                'cbqosatmpvcpolicytable',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosC3plAccountCfgTable', REFERENCE_CLASS, 'CbQosC3plAccountCfgTable' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CISCOCLASSBASEDQOSMIB.CbQosC3plAccountCfgTable', 
                [], [], 
                '''                This table specifies C3pl Account Action configuration
                information
                ''',
                'cbqosc3placcountcfgtable',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosC3plAccountStatsTable', REFERENCE_CLASS, 'CbQosC3plAccountStatsTable' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CISCOCLASSBASEDQOSMIB.CbQosC3plAccountStatsTable', 
                [], [], 
                '''                This table specifies C3pl Account Action related
                statistics information.
                ''',
                'cbqosc3placcountstatstable',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosCMCfgTable', REFERENCE_CLASS, 'CbQosCMCfgTable' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CISCOCLASSBASEDQOSMIB.CbQosCMCfgTable', 
                [], [], 
                '''                This table specifies ClassMap configuration information
                ''',
                'cbqoscmcfgtable',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosCMStatsTable', REFERENCE_CLASS, 'CbQosCMStatsTable' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CISCOCLASSBASEDQOSMIB.CbQosCMStatsTable', 
                [], [], 
                '''                This table specifies ClassMap related Statistical
                information.
                ''',
                'cbqoscmstatstable',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosEBCfgTable', REFERENCE_CLASS, 'CbQosEBCfgTable' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CISCOCLASSBASEDQOSMIB.CbQosEBCfgTable', 
                [], [], 
                '''                This table specifies Estimate Bandwidth related
                configuration information.
                ''',
                'cbqosebcfgtable',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosEBStatsTable', REFERENCE_CLASS, 'CbQosEBStatsTable' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CISCOCLASSBASEDQOSMIB.CbQosEBStatsTable', 
                [], [], 
                '''                This table specifies Estimate Bandwidth related
                statistical information.
                ''',
                'cbqosebstatstable',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosFrameRelayPolicyTable', REFERENCE_CLASS, 'CbQosFrameRelayPolicyTable' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CISCOCLASSBASEDQOSMIB.CbQosFrameRelayPolicyTable', 
                [], [], 
                '''                This table describes the service polices that are
                attached to Frame Relay DLCIs.
                ''',
                'cbqosframerelaypolicytable',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosInterfacePolicyTable', REFERENCE_CLASS, 'CbQosInterfacePolicyTable' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CISCOCLASSBASEDQOSMIB.CbQosInterfacePolicyTable', 
                [], [], 
                '''                This table describes the service polices that are
                attached to main and sub interfaces.
                ''',
                'cbqosinterfacepolicytable',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosIPHCCfgTable', REFERENCE_CLASS, 'CbQosIPHCCfgTable' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CISCOCLASSBASEDQOSMIB.CbQosIPHCCfgTable', 
                [], [], 
                '''                This table specifies IP Header Compression
                configuration information.
                ''',
                'cbqosiphccfgtable',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosIPHCStatsTable', REFERENCE_CLASS, 'CbQosIPHCStatsTable' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CISCOCLASSBASEDQOSMIB.CbQosIPHCStatsTable', 
                [], [], 
                '''                This table specifies IP Header Compression
                statistical information.
                ''',
                'cbqosiphcstatstable',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosMatchStmtCfgTable', REFERENCE_CLASS, 'CbQosMatchStmtCfgTable' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CISCOCLASSBASEDQOSMIB.CbQosMatchStmtCfgTable', 
                [], [], 
                '''                This table specifies ClassMap configuration information
                ''',
                'cbqosmatchstmtcfgtable',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosMatchStmtStatsTable', REFERENCE_CLASS, 'CbQosMatchStmtStatsTable' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CISCOCLASSBASEDQOSMIB.CbQosMatchStmtStatsTable', 
                [], [], 
                '''                This table specifies Match Statement related statistical
                information.
                ''',
                'cbqosmatchstmtstatstable',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosMeasureIPSLACfgTable', REFERENCE_CLASS, 'CbQosMeasureIPSLACfgTable' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CISCOCLASSBASEDQOSMIB.CbQosMeasureIPSLACfgTable', 
                [], [], 
                '''                This table specifies configuration information for measure type
                IPSLA action. The measure action relates the policy class to a
                specific IPSLAs auto group. Configuration of measure action of
                type IPSLA results in automatic generation of IPSLAs synthetic
                test operations when the policy is attached to interface. The
                operations are created according to the characteristics
                specified and to the destinations specified in IPSLA auto group.
                The IPSLAs sythentic test operations measure network statistics
                such as latency, packet loss and jitter.
                This table is to be used only for retrieving the measure
                action configuration information.
                ''',
                'cbqosmeasureipslacfgtable',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosObjectsTable', REFERENCE_CLASS, 'CbQosObjectsTable' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CISCOCLASSBASEDQOSMIB.CbQosObjectsTable', 
                [], [], 
                '''                This table specifies QoS objects (classmap, policymap,
                match statements, and actions) hierarchy. This table also 
                provide relationship between each PolicyIndex/ObjectsIndex 
                pair and the ConfigIndex. ConfigIndex is essential for 
                querying any configuration tables.
                ''',
                'cbqosobjectstable',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceActionCfgTable', REFERENCE_CLASS, 'CbQosPoliceActionCfgTable' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CISCOCLASSBASEDQOSMIB.CbQosPoliceActionCfgTable', 
                [], [], 
                '''                This table specifies Police Action configuration
                information.
                ''',
                'cbqospoliceactioncfgtable',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceCfgTable', REFERENCE_CLASS, 'CbQosPoliceCfgTable' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CISCOCLASSBASEDQOSMIB.CbQosPoliceCfgTable', 
                [], [], 
                '''                This table specifies Police Action configuration
                information.
                ''',
                'cbqospolicecfgtable',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceColorStatsTable', REFERENCE_CLASS, 'CbQosPoliceColorStatsTable' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CISCOCLASSBASEDQOSMIB.CbQosPoliceColorStatsTable', 
                [], [], 
                '''                This table specifies Police Action related Statistical
                information for two rate color aware marker.
                ''',
                'cbqospolicecolorstatstable',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPoliceStatsTable', REFERENCE_CLASS, 'CbQosPoliceStatsTable' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CISCOCLASSBASEDQOSMIB.CbQosPoliceStatsTable', 
                [], [], 
                '''                This table specifies Police Action related Statistical
                information.
                ''',
                'cbqospolicestatstable',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosPolicyMapCfgTable', REFERENCE_CLASS, 'CbQosPolicyMapCfgTable' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CISCOCLASSBASEDQOSMIB.CbQosPolicyMapCfgTable', 
                [], [], 
                '''                This table specifies Policymap configuration information
                ''',
                'cbqospolicymapcfgtable',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosQueueingCfgTable', REFERENCE_CLASS, 'CbQosQueueingCfgTable' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CISCOCLASSBASEDQOSMIB.CbQosQueueingCfgTable', 
                [], [], 
                '''                This table specifies Queueing Action configuration
                information
                ''',
                'cbqosqueueingcfgtable',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosQueueingClassCfgTable', REFERENCE_CLASS, 'CbQosQueueingClassCfgTable' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CISCOCLASSBASEDQOSMIB.CbQosQueueingClassCfgTable', 
                [], [], 
                '''                This table specifies the configuration information for weighted
                queue limit action per IP precedence basis.
                ''',
                'cbqosqueueingclasscfgtable',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosQueueingStatsTable', REFERENCE_CLASS, 'CbQosQueueingStatsTable' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CISCOCLASSBASEDQOSMIB.CbQosQueueingStatsTable', 
                [], [], 
                '''                This table specifies Queueing Action related Statistical
                information.
                ''',
                'cbqosqueueingstatstable',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosREDCfgTable', REFERENCE_CLASS, 'CbQosREDCfgTable' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CISCOCLASSBASEDQOSMIB.CbQosREDCfgTable', 
                [], [], 
                '''                This table specifies WRED Action configuration
                information
                ''',
                'cbqosredcfgtable',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosREDClassCfgTable', REFERENCE_CLASS, 'CbQosREDClassCfgTable' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CISCOCLASSBASEDQOSMIB.CbQosREDClassCfgTable', 
                [], [], 
                '''                This table specifies WRED Action configuration
                information on a per IP precedence basis.
                ''',
                'cbqosredclasscfgtable',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosREDClassStatsTable', REFERENCE_CLASS, 'CbQosREDClassStatsTable' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CISCOCLASSBASEDQOSMIB.CbQosREDClassStatsTable', 
                [], [], 
                '''                This table specifies per Precedence WRED Action related
                Statistical information.
                ''',
                'cbqosredclassstatstable',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosServicePolicyTable', REFERENCE_CLASS, 'CbQosServicePolicyTable' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CISCOCLASSBASEDQOSMIB.CbQosServicePolicyTable', 
                [], [], 
                '''                This table describes the logical interfaces/media types
                and the policymap that are attached to it.
                ''',
                'cbqosservicepolicytable',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosSetCfgTable', REFERENCE_CLASS, 'CbQosSetCfgTable' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CISCOCLASSBASEDQOSMIB.CbQosSetCfgTable', 
                [], [], 
                '''                This table specifies Packet Marking Action configuration
                information.
                ''',
                'cbqossetcfgtable',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosSetStatsTable', REFERENCE_CLASS, 'CbQosSetStatsTable' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CISCOCLASSBASEDQOSMIB.CbQosSetStatsTable', 
                [], [], 
                '''                This table specifies packet marking statistical
                information.
                ''',
                'cbqossetstatstable',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosTableMapCfgTable', REFERENCE_CLASS, 'CbQosTableMapCfgTable' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CISCOCLASSBASEDQOSMIB.CbQosTableMapCfgTable', 
                [], [], 
                '''                This table specifies Table Map basic configuration
                information.
                ''',
                'cbqostablemapcfgtable',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosTableMapSetCfgTable', REFERENCE_CLASS, 'CbQosTableMapSetCfgTable' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CISCOCLASSBASEDQOSMIB.CbQosTableMapSetCfgTable', 
                [], [], 
                '''                This table specifies enhanced packet marking
                configuration using a pre-defined tablemap.
                ''',
                'cbqostablemapsetcfgtable',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosTableMapValueCfgTable', REFERENCE_CLASS, 'CbQosTableMapValueCfgTable' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CISCOCLASSBASEDQOSMIB.CbQosTableMapValueCfgTable', 
                [], [], 
                '''                This table specifies the from-value to to-value
                conversion pairs for a tablemap.
                ''',
                'cbqostablemapvaluecfgtable',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosTSCfgTable', REFERENCE_CLASS, 'CbQosTSCfgTable' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CISCOCLASSBASEDQOSMIB.CbQosTSCfgTable', 
                [], [], 
                '''                This table specifies traffic-shaping Action configuration
                information.
                ''',
                'cbqostscfgtable',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            _MetaInfoClassMember('cbQosTSStatsTable', REFERENCE_CLASS, 'CbQosTSStatsTable' , 'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB', 'CISCOCLASSBASEDQOSMIB.CbQosTSStatsTable', 
                [], [], 
                '''                This table specifies traffic-shaping Action related
                Statistical information.
                ''',
                'cbqostsstatstable',
                'CISCO-CLASS-BASED-QOS-MIB', False),
            ],
            'CISCO-CLASS-BASED-QOS-MIB',
            'CISCO-CLASS-BASED-QOS-MIB',
            _yang_ns._namespaces['CISCO-CLASS-BASED-QOS-MIB'],
        'ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB'
        ),
    },
}
_meta_table['CISCOCLASSBASEDQOSMIB.CbQosATMPVCPolicyTable.CbQosATMPVCPolicyEntry']['meta_info'].parent =_meta_table['CISCOCLASSBASEDQOSMIB.CbQosATMPVCPolicyTable']['meta_info']
_meta_table['CISCOCLASSBASEDQOSMIB.CbQosC3plAccountCfgTable.CbQosC3plAccountCfgEntry']['meta_info'].parent =_meta_table['CISCOCLASSBASEDQOSMIB.CbQosC3plAccountCfgTable']['meta_info']
_meta_table['CISCOCLASSBASEDQOSMIB.CbQosC3plAccountStatsTable.CbQosC3plAccountStatsEntry']['meta_info'].parent =_meta_table['CISCOCLASSBASEDQOSMIB.CbQosC3plAccountStatsTable']['meta_info']
_meta_table['CISCOCLASSBASEDQOSMIB.CbQosCMCfgTable.CbQosCMCfgEntry']['meta_info'].parent =_meta_table['CISCOCLASSBASEDQOSMIB.CbQosCMCfgTable']['meta_info']
_meta_table['CISCOCLASSBASEDQOSMIB.CbQosCMStatsTable.CbQosCMStatsEntry']['meta_info'].parent =_meta_table['CISCOCLASSBASEDQOSMIB.CbQosCMStatsTable']['meta_info']
_meta_table['CISCOCLASSBASEDQOSMIB.CbQosEBCfgTable.CbQosEBCfgEntry']['meta_info'].parent =_meta_table['CISCOCLASSBASEDQOSMIB.CbQosEBCfgTable']['meta_info']
_meta_table['CISCOCLASSBASEDQOSMIB.CbQosEBStatsTable.CbQosEBStatsEntry']['meta_info'].parent =_meta_table['CISCOCLASSBASEDQOSMIB.CbQosEBStatsTable']['meta_info']
_meta_table['CISCOCLASSBASEDQOSMIB.CbQosFrameRelayPolicyTable.CbQosFrameRelayPolicyEntry']['meta_info'].parent =_meta_table['CISCOCLASSBASEDQOSMIB.CbQosFrameRelayPolicyTable']['meta_info']
_meta_table['CISCOCLASSBASEDQOSMIB.CbQosIPHCCfgTable.CbQosIPHCCfgEntry']['meta_info'].parent =_meta_table['CISCOCLASSBASEDQOSMIB.CbQosIPHCCfgTable']['meta_info']
_meta_table['CISCOCLASSBASEDQOSMIB.CbQosIPHCStatsTable.CbQosIPHCStatsEntry']['meta_info'].parent =_meta_table['CISCOCLASSBASEDQOSMIB.CbQosIPHCStatsTable']['meta_info']
_meta_table['CISCOCLASSBASEDQOSMIB.CbQosInterfacePolicyTable.CbQosInterfacePolicyEntry']['meta_info'].parent =_meta_table['CISCOCLASSBASEDQOSMIB.CbQosInterfacePolicyTable']['meta_info']
_meta_table['CISCOCLASSBASEDQOSMIB.CbQosMatchStmtCfgTable.CbQosMatchStmtCfgEntry']['meta_info'].parent =_meta_table['CISCOCLASSBASEDQOSMIB.CbQosMatchStmtCfgTable']['meta_info']
_meta_table['CISCOCLASSBASEDQOSMIB.CbQosMatchStmtStatsTable.CbQosMatchStmtStatsEntry']['meta_info'].parent =_meta_table['CISCOCLASSBASEDQOSMIB.CbQosMatchStmtStatsTable']['meta_info']
_meta_table['CISCOCLASSBASEDQOSMIB.CbQosMeasureIPSLACfgTable.CbQosMeasureIPSLACfgEntry']['meta_info'].parent =_meta_table['CISCOCLASSBASEDQOSMIB.CbQosMeasureIPSLACfgTable']['meta_info']
_meta_table['CISCOCLASSBASEDQOSMIB.CbQosObjectsTable.CbQosObjectsEntry']['meta_info'].parent =_meta_table['CISCOCLASSBASEDQOSMIB.CbQosObjectsTable']['meta_info']
_meta_table['CISCOCLASSBASEDQOSMIB.CbQosPoliceActionCfgTable.CbQosPoliceActionCfgEntry']['meta_info'].parent =_meta_table['CISCOCLASSBASEDQOSMIB.CbQosPoliceActionCfgTable']['meta_info']
_meta_table['CISCOCLASSBASEDQOSMIB.CbQosPoliceCfgTable.CbQosPoliceCfgEntry']['meta_info'].parent =_meta_table['CISCOCLASSBASEDQOSMIB.CbQosPoliceCfgTable']['meta_info']
_meta_table['CISCOCLASSBASEDQOSMIB.CbQosPoliceColorStatsTable.CbQosPoliceColorStatsEntry']['meta_info'].parent =_meta_table['CISCOCLASSBASEDQOSMIB.CbQosPoliceColorStatsTable']['meta_info']
_meta_table['CISCOCLASSBASEDQOSMIB.CbQosPoliceStatsTable.CbQosPoliceStatsEntry']['meta_info'].parent =_meta_table['CISCOCLASSBASEDQOSMIB.CbQosPoliceStatsTable']['meta_info']
_meta_table['CISCOCLASSBASEDQOSMIB.CbQosPolicyMapCfgTable.CbQosPolicyMapCfgEntry']['meta_info'].parent =_meta_table['CISCOCLASSBASEDQOSMIB.CbQosPolicyMapCfgTable']['meta_info']
_meta_table['CISCOCLASSBASEDQOSMIB.CbQosQueueingCfgTable.CbQosQueueingCfgEntry']['meta_info'].parent =_meta_table['CISCOCLASSBASEDQOSMIB.CbQosQueueingCfgTable']['meta_info']
_meta_table['CISCOCLASSBASEDQOSMIB.CbQosQueueingClassCfgTable.CbQosQueueingClassCfgEntry']['meta_info'].parent =_meta_table['CISCOCLASSBASEDQOSMIB.CbQosQueueingClassCfgTable']['meta_info']
_meta_table['CISCOCLASSBASEDQOSMIB.CbQosQueueingStatsTable.CbQosQueueingStatsEntry']['meta_info'].parent =_meta_table['CISCOCLASSBASEDQOSMIB.CbQosQueueingStatsTable']['meta_info']
_meta_table['CISCOCLASSBASEDQOSMIB.CbQosREDCfgTable.CbQosREDCfgEntry']['meta_info'].parent =_meta_table['CISCOCLASSBASEDQOSMIB.CbQosREDCfgTable']['meta_info']
_meta_table['CISCOCLASSBASEDQOSMIB.CbQosREDClassCfgTable.CbQosREDClassCfgEntry']['meta_info'].parent =_meta_table['CISCOCLASSBASEDQOSMIB.CbQosREDClassCfgTable']['meta_info']
_meta_table['CISCOCLASSBASEDQOSMIB.CbQosREDClassStatsTable.CbQosREDClassStatsEntry']['meta_info'].parent =_meta_table['CISCOCLASSBASEDQOSMIB.CbQosREDClassStatsTable']['meta_info']
_meta_table['CISCOCLASSBASEDQOSMIB.CbQosServicePolicyTable.CbQosServicePolicyEntry']['meta_info'].parent =_meta_table['CISCOCLASSBASEDQOSMIB.CbQosServicePolicyTable']['meta_info']
_meta_table['CISCOCLASSBASEDQOSMIB.CbQosSetCfgTable.CbQosSetCfgEntry']['meta_info'].parent =_meta_table['CISCOCLASSBASEDQOSMIB.CbQosSetCfgTable']['meta_info']
_meta_table['CISCOCLASSBASEDQOSMIB.CbQosSetStatsTable.CbQosSetStatsEntry']['meta_info'].parent =_meta_table['CISCOCLASSBASEDQOSMIB.CbQosSetStatsTable']['meta_info']
_meta_table['CISCOCLASSBASEDQOSMIB.CbQosTSCfgTable.CbQosTSCfgEntry']['meta_info'].parent =_meta_table['CISCOCLASSBASEDQOSMIB.CbQosTSCfgTable']['meta_info']
_meta_table['CISCOCLASSBASEDQOSMIB.CbQosTSStatsTable.CbQosTSStatsEntry']['meta_info'].parent =_meta_table['CISCOCLASSBASEDQOSMIB.CbQosTSStatsTable']['meta_info']
_meta_table['CISCOCLASSBASEDQOSMIB.CbQosTableMapCfgTable.CbQosTableMapCfgEntry']['meta_info'].parent =_meta_table['CISCOCLASSBASEDQOSMIB.CbQosTableMapCfgTable']['meta_info']
_meta_table['CISCOCLASSBASEDQOSMIB.CbQosTableMapSetCfgTable.CbQosTableMapSetCfgEntry']['meta_info'].parent =_meta_table['CISCOCLASSBASEDQOSMIB.CbQosTableMapSetCfgTable']['meta_info']
_meta_table['CISCOCLASSBASEDQOSMIB.CbQosTableMapValueCfgTable.CbQosTableMapValueCfgEntry']['meta_info'].parent =_meta_table['CISCOCLASSBASEDQOSMIB.CbQosTableMapValueCfgTable']['meta_info']
_meta_table['CISCOCLASSBASEDQOSMIB.CbQosATMPVCPolicyTable']['meta_info'].parent =_meta_table['CISCOCLASSBASEDQOSMIB']['meta_info']
_meta_table['CISCOCLASSBASEDQOSMIB.CbQosC3plAccountCfgTable']['meta_info'].parent =_meta_table['CISCOCLASSBASEDQOSMIB']['meta_info']
_meta_table['CISCOCLASSBASEDQOSMIB.CbQosC3plAccountStatsTable']['meta_info'].parent =_meta_table['CISCOCLASSBASEDQOSMIB']['meta_info']
_meta_table['CISCOCLASSBASEDQOSMIB.CbQosCMCfgTable']['meta_info'].parent =_meta_table['CISCOCLASSBASEDQOSMIB']['meta_info']
_meta_table['CISCOCLASSBASEDQOSMIB.CbQosCMStatsTable']['meta_info'].parent =_meta_table['CISCOCLASSBASEDQOSMIB']['meta_info']
_meta_table['CISCOCLASSBASEDQOSMIB.CbQosEBCfgTable']['meta_info'].parent =_meta_table['CISCOCLASSBASEDQOSMIB']['meta_info']
_meta_table['CISCOCLASSBASEDQOSMIB.CbQosEBStatsTable']['meta_info'].parent =_meta_table['CISCOCLASSBASEDQOSMIB']['meta_info']
_meta_table['CISCOCLASSBASEDQOSMIB.CbQosFrameRelayPolicyTable']['meta_info'].parent =_meta_table['CISCOCLASSBASEDQOSMIB']['meta_info']
_meta_table['CISCOCLASSBASEDQOSMIB.CbQosIPHCCfgTable']['meta_info'].parent =_meta_table['CISCOCLASSBASEDQOSMIB']['meta_info']
_meta_table['CISCOCLASSBASEDQOSMIB.CbQosIPHCStatsTable']['meta_info'].parent =_meta_table['CISCOCLASSBASEDQOSMIB']['meta_info']
_meta_table['CISCOCLASSBASEDQOSMIB.CbQosInterfacePolicyTable']['meta_info'].parent =_meta_table['CISCOCLASSBASEDQOSMIB']['meta_info']
_meta_table['CISCOCLASSBASEDQOSMIB.CbQosMatchStmtCfgTable']['meta_info'].parent =_meta_table['CISCOCLASSBASEDQOSMIB']['meta_info']
_meta_table['CISCOCLASSBASEDQOSMIB.CbQosMatchStmtStatsTable']['meta_info'].parent =_meta_table['CISCOCLASSBASEDQOSMIB']['meta_info']
_meta_table['CISCOCLASSBASEDQOSMIB.CbQosMeasureIPSLACfgTable']['meta_info'].parent =_meta_table['CISCOCLASSBASEDQOSMIB']['meta_info']
_meta_table['CISCOCLASSBASEDQOSMIB.CbQosObjectsTable']['meta_info'].parent =_meta_table['CISCOCLASSBASEDQOSMIB']['meta_info']
_meta_table['CISCOCLASSBASEDQOSMIB.CbQosPoliceActionCfgTable']['meta_info'].parent =_meta_table['CISCOCLASSBASEDQOSMIB']['meta_info']
_meta_table['CISCOCLASSBASEDQOSMIB.CbQosPoliceCfgTable']['meta_info'].parent =_meta_table['CISCOCLASSBASEDQOSMIB']['meta_info']
_meta_table['CISCOCLASSBASEDQOSMIB.CbQosPoliceColorStatsTable']['meta_info'].parent =_meta_table['CISCOCLASSBASEDQOSMIB']['meta_info']
_meta_table['CISCOCLASSBASEDQOSMIB.CbQosPoliceStatsTable']['meta_info'].parent =_meta_table['CISCOCLASSBASEDQOSMIB']['meta_info']
_meta_table['CISCOCLASSBASEDQOSMIB.CbQosPolicyMapCfgTable']['meta_info'].parent =_meta_table['CISCOCLASSBASEDQOSMIB']['meta_info']
_meta_table['CISCOCLASSBASEDQOSMIB.CbQosQueueingCfgTable']['meta_info'].parent =_meta_table['CISCOCLASSBASEDQOSMIB']['meta_info']
_meta_table['CISCOCLASSBASEDQOSMIB.CbQosQueueingClassCfgTable']['meta_info'].parent =_meta_table['CISCOCLASSBASEDQOSMIB']['meta_info']
_meta_table['CISCOCLASSBASEDQOSMIB.CbQosQueueingStatsTable']['meta_info'].parent =_meta_table['CISCOCLASSBASEDQOSMIB']['meta_info']
_meta_table['CISCOCLASSBASEDQOSMIB.CbQosREDCfgTable']['meta_info'].parent =_meta_table['CISCOCLASSBASEDQOSMIB']['meta_info']
_meta_table['CISCOCLASSBASEDQOSMIB.CbQosREDClassCfgTable']['meta_info'].parent =_meta_table['CISCOCLASSBASEDQOSMIB']['meta_info']
_meta_table['CISCOCLASSBASEDQOSMIB.CbQosREDClassStatsTable']['meta_info'].parent =_meta_table['CISCOCLASSBASEDQOSMIB']['meta_info']
_meta_table['CISCOCLASSBASEDQOSMIB.CbQosServicePolicyTable']['meta_info'].parent =_meta_table['CISCOCLASSBASEDQOSMIB']['meta_info']
_meta_table['CISCOCLASSBASEDQOSMIB.CbQosSetCfgTable']['meta_info'].parent =_meta_table['CISCOCLASSBASEDQOSMIB']['meta_info']
_meta_table['CISCOCLASSBASEDQOSMIB.CbQosSetStatsTable']['meta_info'].parent =_meta_table['CISCOCLASSBASEDQOSMIB']['meta_info']
_meta_table['CISCOCLASSBASEDQOSMIB.CbQosTSCfgTable']['meta_info'].parent =_meta_table['CISCOCLASSBASEDQOSMIB']['meta_info']
_meta_table['CISCOCLASSBASEDQOSMIB.CbQosTSStatsTable']['meta_info'].parent =_meta_table['CISCOCLASSBASEDQOSMIB']['meta_info']
_meta_table['CISCOCLASSBASEDQOSMIB.CbQosTableMapCfgTable']['meta_info'].parent =_meta_table['CISCOCLASSBASEDQOSMIB']['meta_info']
_meta_table['CISCOCLASSBASEDQOSMIB.CbQosTableMapSetCfgTable']['meta_info'].parent =_meta_table['CISCOCLASSBASEDQOSMIB']['meta_info']
_meta_table['CISCOCLASSBASEDQOSMIB.CbQosTableMapValueCfgTable']['meta_info'].parent =_meta_table['CISCOCLASSBASEDQOSMIB']['meta_info']
