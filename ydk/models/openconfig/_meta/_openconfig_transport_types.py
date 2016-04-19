


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
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
    'Cfp2_Identity' : {
        'meta_info' : _MetaInfoClass('Cfp2_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'CFP2',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Cfp4_Identity' : {
        'meta_info' : _MetaInfoClass('Cfp4_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'CFP4',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Cfp_Identity' : {
        'meta_info' : _MetaInfoClass('Cfp_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'CFP',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth100G_Acc_Identity' : {
        'meta_info' : _MetaInfoClass('Eth100G_Acc_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'eth-100G_ACC',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth100G_Aoc_Identity' : {
        'meta_info' : _MetaInfoClass('Eth100G_Aoc_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'eth-100G_AOC',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth100GbaseClr4_Identity' : {
        'meta_info' : _MetaInfoClass('Eth100GbaseClr4_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'eth-100GBASE-CLR4',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth100GbaseCr4_Identity' : {
        'meta_info' : _MetaInfoClass('Eth100GbaseCr4_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'eth-100GBASE-CR4',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth100GbaseCwdm4_Identity' : {
        'meta_info' : _MetaInfoClass('Eth100GbaseCwdm4_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'eth-100GBASE-CWDM4',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth100GbaseEr4_Identity' : {
        'meta_info' : _MetaInfoClass('Eth100GbaseEr4_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'eth-100GBASE-ER4',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth100GbaseLr4_Identity' : {
        'meta_info' : _MetaInfoClass('Eth100GbaseLr4_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'eth-100GBASE-LR4',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth100GbasePsm4_Identity' : {
        'meta_info' : _MetaInfoClass('Eth100GbasePsm4_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'eth-100GBASE-PSM4',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth100GbaseSr10_Identity' : {
        'meta_info' : _MetaInfoClass('Eth100GbaseSr10_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'eth-100GBASE-SR10',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth100GbaseSr4_Identity' : {
        'meta_info' : _MetaInfoClass('Eth100GbaseSr4_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'eth-100GBASE-SR4',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth10GbaseEr_Identity' : {
        'meta_info' : _MetaInfoClass('Eth10GbaseEr_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'eth-10GBASE-ER',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth10GbaseLr_Identity' : {
        'meta_info' : _MetaInfoClass('Eth10GbaseLr_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'eth-10GBASE-LR',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth10GbaseLrm_Identity' : {
        'meta_info' : _MetaInfoClass('Eth10GbaseLrm_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'eth-10GBASE-LRM',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth10GbaseSr_Identity' : {
        'meta_info' : _MetaInfoClass('Eth10GbaseSr_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'eth-10GBASE-SR',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth10GbaseZr_Identity' : {
        'meta_info' : _MetaInfoClass('Eth10GbaseZr_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'eth-10GBASE-ZR',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth40GbaseCr4_Identity' : {
        'meta_info' : _MetaInfoClass('Eth40GbaseCr4_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'eth-40GBASE-CR4',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth40GbaseEr4_Identity' : {
        'meta_info' : _MetaInfoClass('Eth40GbaseEr4_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'eth-40GBASE-ER4',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth40GbaseLr4_Identity' : {
        'meta_info' : _MetaInfoClass('Eth40GbaseLr4_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'eth-40GBASE-LR4',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth40GbasePsm4_Identity' : {
        'meta_info' : _MetaInfoClass('Eth40GbasePsm4_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'eth-40GBASE-PSM4',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth40GbaseSr4_Identity' : {
        'meta_info' : _MetaInfoClass('Eth40GbaseSr4_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'eth-40GBASE-SR4',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth4X10GbaseLr_Identity' : {
        'meta_info' : _MetaInfoClass('Eth4X10GbaseLr_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'eth-4x10GBASE-LR',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth4X10GbaseSr_Identity' : {
        'meta_info' : _MetaInfoClass('Eth4X10GbaseSr_Identity',
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
    'Prot100G_Mlg_Identity' : {
        'meta_info' : _MetaInfoClass('Prot100G_Mlg_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'prot-100G_MLG',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Prot100Ge_Identity' : {
        'meta_info' : _MetaInfoClass('Prot100Ge_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'prot-100GE',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Prot10Ge_Lan_Identity' : {
        'meta_info' : _MetaInfoClass('Prot10Ge_Lan_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'prot-10GE_LAN',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Prot10Ge_Wan_Identity' : {
        'meta_info' : _MetaInfoClass('Prot10Ge_Wan_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'prot-10GE_WAN',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Prot1Ge_Identity' : {
        'meta_info' : _MetaInfoClass('Prot1Ge_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'prot-1GE',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Prot40Ge_Identity' : {
        'meta_info' : _MetaInfoClass('Prot40Ge_Identity',
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
    'ProtOc192_Identity' : {
        'meta_info' : _MetaInfoClass('ProtOc192_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'prot-OC192',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'ProtOc48_Identity' : {
        'meta_info' : _MetaInfoClass('ProtOc48_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'prot-OC48',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'ProtOc768_Identity' : {
        'meta_info' : _MetaInfoClass('ProtOc768_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'prot-OC768',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'ProtOdu2E_Identity' : {
        'meta_info' : _MetaInfoClass('ProtOdu2E_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'prot-ODU2e',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'ProtOdu2_Identity' : {
        'meta_info' : _MetaInfoClass('ProtOdu2_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'prot-ODU2',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'ProtOdu3_Identity' : {
        'meta_info' : _MetaInfoClass('ProtOdu3_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'prot-ODU3',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'ProtOdu4_Identity' : {
        'meta_info' : _MetaInfoClass('ProtOdu4_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'prot-ODU4',
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
    'ProtOtu1E_Identity' : {
        'meta_info' : _MetaInfoClass('ProtOtu1E_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'prot-OTU1e',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'ProtOtu2E_Identity' : {
        'meta_info' : _MetaInfoClass('ProtOtu2E_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'prot-OTU2e',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'ProtOtu2_Identity' : {
        'meta_info' : _MetaInfoClass('ProtOtu2_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'prot-OTU2',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'ProtOtu3_Identity' : {
        'meta_info' : _MetaInfoClass('ProtOtu3_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'prot-OTU3',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'ProtOtu4_Identity' : {
        'meta_info' : _MetaInfoClass('ProtOtu4_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'prot-OTU4',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'ProtOtucn_Identity' : {
        'meta_info' : _MetaInfoClass('ProtOtucn_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'prot-OTUCn',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'ProtStm16_Identity' : {
        'meta_info' : _MetaInfoClass('ProtStm16_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'prot-STM16',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'ProtStm256_Identity' : {
        'meta_info' : _MetaInfoClass('ProtStm256_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'prot-STM256',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'ProtStm64_Identity' : {
        'meta_info' : _MetaInfoClass('ProtStm64_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'prot-STM64',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Qsfp28_Identity' : {
        'meta_info' : _MetaInfoClass('Qsfp28_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'QSFP28',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Qsfp_Identity' : {
        'meta_info' : _MetaInfoClass('Qsfp_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'QSFP',
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
    'Sfp_Identity' : {
        'meta_info' : _MetaInfoClass('Sfp_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'SFP',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Sfp_Plus_Identity' : {
        'meta_info' : _MetaInfoClass('Sfp_Plus_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'SFP_plus',
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
    'TribRate2__Dot__5G_Identity' : {
        'meta_info' : _MetaInfoClass('TribRate2__Dot__5G_Identity',
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
    'Vsr20003R2_Identity' : {
        'meta_info' : _MetaInfoClass('Vsr20003R2_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'VSR2000-3R2',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Vsr20003R3_Identity' : {
        'meta_info' : _MetaInfoClass('Vsr20003R3_Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'VSR2000-3R3',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Vsr20003R5_Identity' : {
        'meta_info' : _MetaInfoClass('Vsr20003R5_Identity',
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
    'Xfp_Identity' : {
        'meta_info' : _MetaInfoClass('Xfp_Identity',
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
