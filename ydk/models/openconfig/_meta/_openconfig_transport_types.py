


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'EthernetPmdType_Identity' : {
        'meta_info' : _MetaInfoClass('EthernetPmdType_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'ethernet-pmd-type',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'FiberConnectorType_Identity' : {
        'meta_info' : _MetaInfoClass('FiberConnectorType_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'fiber-connector-type',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'LogicalElementProtocolType_Identity' : {
        'meta_info' : _MetaInfoClass('LogicalElementProtocolType_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'logical-element-protocol-type',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'OtnApplicationCode_Identity' : {
        'meta_info' : _MetaInfoClass('OtnApplicationCode_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'otn-application-code',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'SonetApplicationCode_Identity' : {
        'meta_info' : _MetaInfoClass('SonetApplicationCode_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'sonet-application-code',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'TransceiverFormFactorType_Identity' : {
        'meta_info' : _MetaInfoClass('TransceiverFormFactorType_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'transceiver-form-factor-type',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'TributaryProtocolType_Identity' : {
        'meta_info' : _MetaInfoClass('TributaryProtocolType_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'tributary-protocol-type',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'TributaryRateClassType_Identity' : {
        'meta_info' : _MetaInfoClass('TributaryRateClassType_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'tributary-rate-class-type',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'CFP2_Identity' : {
        'meta_info' : _MetaInfoClass('CFP2_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'CFP2',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'CFP4_Identity' : {
        'meta_info' : _MetaInfoClass('CFP4_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'CFP4',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'CFP_Identity' : {
        'meta_info' : _MetaInfoClass('CFP_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'CFP',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth100GBASECLR4_Identity' : {
        'meta_info' : _MetaInfoClass('Eth100GBASECLR4_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'eth-100GBASE-CLR4',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth100GBASECR4_Identity' : {
        'meta_info' : _MetaInfoClass('Eth100GBASECR4_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'eth-100GBASE-CR4',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth100GBASECWDM4_Identity' : {
        'meta_info' : _MetaInfoClass('Eth100GBASECWDM4_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'eth-100GBASE-CWDM4',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth100GBASEER4_Identity' : {
        'meta_info' : _MetaInfoClass('Eth100GBASEER4_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'eth-100GBASE-ER4',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth100GBASELR4_Identity' : {
        'meta_info' : _MetaInfoClass('Eth100GBASELR4_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'eth-100GBASE-LR4',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth100GBASEPSM4_Identity' : {
        'meta_info' : _MetaInfoClass('Eth100GBASEPSM4_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'eth-100GBASE-PSM4',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth100GBASESR10_Identity' : {
        'meta_info' : _MetaInfoClass('Eth100GBASESR10_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'eth-100GBASE-SR10',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth100GBASESR4_Identity' : {
        'meta_info' : _MetaInfoClass('Eth100GBASESR4_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'eth-100GBASE-SR4',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth100G_ACC_Identity' : {
        'meta_info' : _MetaInfoClass('Eth100G_ACC_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'eth-100G_ACC',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth100G_AOC_Identity' : {
        'meta_info' : _MetaInfoClass('Eth100G_AOC_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'eth-100G_AOC',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth10GBASEER_Identity' : {
        'meta_info' : _MetaInfoClass('Eth10GBASEER_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'eth-10GBASE-ER',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth10GBASELRM_Identity' : {
        'meta_info' : _MetaInfoClass('Eth10GBASELRM_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'eth-10GBASE-LRM',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth10GBASELR_Identity' : {
        'meta_info' : _MetaInfoClass('Eth10GBASELR_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'eth-10GBASE-LR',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth10GBASESR_Identity' : {
        'meta_info' : _MetaInfoClass('Eth10GBASESR_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'eth-10GBASE-SR',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth10GBASEZR_Identity' : {
        'meta_info' : _MetaInfoClass('Eth10GBASEZR_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'eth-10GBASE-ZR',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth40GBASECR4_Identity' : {
        'meta_info' : _MetaInfoClass('Eth40GBASECR4_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'eth-40GBASE-CR4',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth40GBASEER4_Identity' : {
        'meta_info' : _MetaInfoClass('Eth40GBASEER4_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'eth-40GBASE-ER4',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth40GBASELR4_Identity' : {
        'meta_info' : _MetaInfoClass('Eth40GBASELR4_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'eth-40GBASE-LR4',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth40GBASEPSM4_Identity' : {
        'meta_info' : _MetaInfoClass('Eth40GBASEPSM4_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'eth-40GBASE-PSM4',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth40GBASESR4_Identity' : {
        'meta_info' : _MetaInfoClass('Eth40GBASESR4_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'eth-40GBASE-SR4',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth4x10GBASELR_Identity' : {
        'meta_info' : _MetaInfoClass('Eth4x10GBASELR_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'eth-4x10GBASE-LR',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth4x10GBASESR_Identity' : {
        'meta_info' : _MetaInfoClass('Eth4x10GBASESR_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'eth-4x10GBASE-SR',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'EthUndefined_Identity' : {
        'meta_info' : _MetaInfoClass('EthUndefined_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'eth-undefined',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'LcConnector_Identity' : {
        'meta_info' : _MetaInfoClass('LcConnector_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'lc-connector',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'MpoConnector_Identity' : {
        'meta_info' : _MetaInfoClass('MpoConnector_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'mpo-connector',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'NonPluggable_Identity' : {
        'meta_info' : _MetaInfoClass('NonPluggable_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'non-pluggable',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Other_Identity' : {
        'meta_info' : _MetaInfoClass('Other_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'other',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'OtnUndefined_Identity' : {
        'meta_info' : _MetaInfoClass('OtnUndefined_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'otn-undefined',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'P1L12D1_Identity' : {
        'meta_info' : _MetaInfoClass('P1L12D1_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'P1L1-2D1',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'P1L12D2_Identity' : {
        'meta_info' : _MetaInfoClass('P1L12D2_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'P1L1-2D2',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'P1S12D2_Identity' : {
        'meta_info' : _MetaInfoClass('P1S12D2_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'P1S1-2D2',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Prot100GE_Identity' : {
        'meta_info' : _MetaInfoClass('Prot100GE_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'prot-100GE',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Prot100G_MLG_Identity' : {
        'meta_info' : _MetaInfoClass('Prot100G_MLG_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'prot-100G_MLG',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Prot10GE_LAN_Identity' : {
        'meta_info' : _MetaInfoClass('Prot10GE_LAN_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'prot-10GE_LAN',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Prot10GE_WAN_Identity' : {
        'meta_info' : _MetaInfoClass('Prot10GE_WAN_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'prot-10GE_WAN',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Prot1GE_Identity' : {
        'meta_info' : _MetaInfoClass('Prot1GE_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'prot-1GE',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Prot40GE_Identity' : {
        'meta_info' : _MetaInfoClass('Prot40GE_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'prot-40GE',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'ProtEthernet_Identity' : {
        'meta_info' : _MetaInfoClass('ProtEthernet_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'prot-ethernet',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'ProtOC192_Identity' : {
        'meta_info' : _MetaInfoClass('ProtOC192_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'prot-OC192',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'ProtOC48_Identity' : {
        'meta_info' : _MetaInfoClass('ProtOC48_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'prot-OC48',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'ProtOC768_Identity' : {
        'meta_info' : _MetaInfoClass('ProtOC768_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'prot-OC768',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'ProtODU2_Identity' : {
        'meta_info' : _MetaInfoClass('ProtODU2_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'prot-ODU2',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'ProtODU2e_Identity' : {
        'meta_info' : _MetaInfoClass('ProtODU2e_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'prot-ODU2e',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'ProtODU3_Identity' : {
        'meta_info' : _MetaInfoClass('ProtODU3_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'prot-ODU3',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'ProtODU4_Identity' : {
        'meta_info' : _MetaInfoClass('ProtODU4_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'prot-ODU4',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'ProtOTU1e_Identity' : {
        'meta_info' : _MetaInfoClass('ProtOTU1e_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'prot-OTU1e',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'ProtOTU2_Identity' : {
        'meta_info' : _MetaInfoClass('ProtOTU2_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'prot-OTU2',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'ProtOTU2e_Identity' : {
        'meta_info' : _MetaInfoClass('ProtOTU2e_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'prot-OTU2e',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'ProtOTU3_Identity' : {
        'meta_info' : _MetaInfoClass('ProtOTU3_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'prot-OTU3',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'ProtOTU4_Identity' : {
        'meta_info' : _MetaInfoClass('ProtOTU4_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'prot-OTU4',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'ProtOTUCn_Identity' : {
        'meta_info' : _MetaInfoClass('ProtOTUCn_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'prot-OTUCn',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'ProtOtn_Identity' : {
        'meta_info' : _MetaInfoClass('ProtOtn_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'prot-otn',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'ProtSTM16_Identity' : {
        'meta_info' : _MetaInfoClass('ProtSTM16_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'prot-STM16',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'ProtSTM256_Identity' : {
        'meta_info' : _MetaInfoClass('ProtSTM256_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'prot-STM256',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'ProtSTM64_Identity' : {
        'meta_info' : _MetaInfoClass('ProtSTM64_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'prot-STM64',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'QSFP28_Identity' : {
        'meta_info' : _MetaInfoClass('QSFP28_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'QSFP28',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'QSFP_Identity' : {
        'meta_info' : _MetaInfoClass('QSFP_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'QSFP',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'SFP_Identity' : {
        'meta_info' : _MetaInfoClass('SFP_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'SFP',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'SFP_plus_Identity' : {
        'meta_info' : _MetaInfoClass('SFP_plus_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'SFP_plus',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'ScConnector_Identity' : {
        'meta_info' : _MetaInfoClass('ScConnector_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'sc-connector',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'SonetUndefined_Identity' : {
        'meta_info' : _MetaInfoClass('SonetUndefined_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'sonet-undefined',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'TribRate100G_Identity' : {
        'meta_info' : _MetaInfoClass('TribRate100G_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'trib-rate-100G',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'TribRate10G_Identity' : {
        'meta_info' : _MetaInfoClass('TribRate10G_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'trib-rate-10G',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'TribRate1G_Identity' : {
        'meta_info' : _MetaInfoClass('TribRate1G_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'trib-rate-1G',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'TribRate2__DOT__5G_Identity' : {
        'meta_info' : _MetaInfoClass('TribRate2__DOT__5G_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'trib-rate-2.5G',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'TribRate40G_Identity' : {
        'meta_info' : _MetaInfoClass('TribRate40G_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'trib-rate-40G',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'VSR20003R2_Identity' : {
        'meta_info' : _MetaInfoClass('VSR20003R2_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'VSR2000-3R2',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'VSR20003R3_Identity' : {
        'meta_info' : _MetaInfoClass('VSR20003R3_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'VSR2000-3R3',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'VSR20003R5_Identity' : {
        'meta_info' : _MetaInfoClass('VSR20003R5_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'VSR2000-3R5',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'X2_Identity' : {
        'meta_info' : _MetaInfoClass('X2_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'X2',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'XFP_Identity' : {
        'meta_info' : _MetaInfoClass('XFP_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'XFP',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
}
