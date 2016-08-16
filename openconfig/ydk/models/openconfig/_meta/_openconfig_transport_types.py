


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'EthernetPmdTypeIdentity' : {
        'meta_info' : _MetaInfoClass('EthernetPmdTypeIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'ethernet-pmd-type',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'OtnApplicationCodeIdentity' : {
        'meta_info' : _MetaInfoClass('OtnApplicationCodeIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'otn-application-code',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'SonetApplicationCodeIdentity' : {
        'meta_info' : _MetaInfoClass('SonetApplicationCodeIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'sonet-application-code',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'TransceiverFormFactorTypeIdentity' : {
        'meta_info' : _MetaInfoClass('TransceiverFormFactorTypeIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'transceiver-form-factor-type',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'LogicalElementProtocolTypeIdentity' : {
        'meta_info' : _MetaInfoClass('LogicalElementProtocolTypeIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'logical-element-protocol-type',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'TributaryProtocolTypeIdentity' : {
        'meta_info' : _MetaInfoClass('TributaryProtocolTypeIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'tributary-protocol-type',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'TributaryRateClassTypeIdentity' : {
        'meta_info' : _MetaInfoClass('TributaryRateClassTypeIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'tributary-rate-class-type',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'FiberConnectorTypeIdentity' : {
        'meta_info' : _MetaInfoClass('FiberConnectorTypeIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'fiber-connector-type',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'ProtOc192Identity' : {
        'meta_info' : _MetaInfoClass('ProtOc192Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'prot-OC192',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Cfp2Identity' : {
        'meta_info' : _MetaInfoClass('Cfp2Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'CFP2',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Prot100G_MlgIdentity' : {
        'meta_info' : _MetaInfoClass('Prot100G_MlgIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'prot-100G_MLG',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth100GbaseEr4Identity' : {
        'meta_info' : _MetaInfoClass('Eth100GbaseEr4Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'eth-100GBASE-ER4',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Cfp4Identity' : {
        'meta_info' : _MetaInfoClass('Cfp4Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'CFP4',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth100G_AocIdentity' : {
        'meta_info' : _MetaInfoClass('Eth100G_AocIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'eth-100G_AOC',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth10GbaseLrmIdentity' : {
        'meta_info' : _MetaInfoClass('Eth10GbaseLrmIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'eth-10GBASE-LRM',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'ProtOdu4Identity' : {
        'meta_info' : _MetaInfoClass('ProtOdu4Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'prot-ODU4',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'P1L12D2Identity' : {
        'meta_info' : _MetaInfoClass('P1L12D2Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'P1L1-2D2',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Qsfp28Identity' : {
        'meta_info' : _MetaInfoClass('Qsfp28Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'QSFP28',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Prot10Ge_LanIdentity' : {
        'meta_info' : _MetaInfoClass('Prot10Ge_LanIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'prot-10GE_LAN',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth10GbaseErIdentity' : {
        'meta_info' : _MetaInfoClass('Eth10GbaseErIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'eth-10GBASE-ER',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Sfp_PlusIdentity' : {
        'meta_info' : _MetaInfoClass('Sfp_PlusIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'SFP_plus',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth100GbaseCr4Identity' : {
        'meta_info' : _MetaInfoClass('Eth100GbaseCr4Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'eth-100GBASE-CR4',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'P1L12D1Identity' : {
        'meta_info' : _MetaInfoClass('P1L12D1Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'P1L1-2D1',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'SfpIdentity' : {
        'meta_info' : _MetaInfoClass('SfpIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'SFP',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'ProtOtu4Identity' : {
        'meta_info' : _MetaInfoClass('ProtOtu4Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'prot-OTU4',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth40GbaseEr4Identity' : {
        'meta_info' : _MetaInfoClass('Eth40GbaseEr4Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'eth-40GBASE-ER4',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth100GbasePsm4Identity' : {
        'meta_info' : _MetaInfoClass('Eth100GbasePsm4Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'eth-100GBASE-PSM4',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth40GbaseCr4Identity' : {
        'meta_info' : _MetaInfoClass('Eth40GbaseCr4Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'eth-40GBASE-CR4',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'SonetUndefinedIdentity' : {
        'meta_info' : _MetaInfoClass('SonetUndefinedIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'sonet-undefined',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth100GbaseClr4Identity' : {
        'meta_info' : _MetaInfoClass('Eth100GbaseClr4Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'eth-100GBASE-CLR4',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Prot10Ge_WanIdentity' : {
        'meta_info' : _MetaInfoClass('Prot10Ge_WanIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'prot-10GE_WAN',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'ProtStm64Identity' : {
        'meta_info' : _MetaInfoClass('ProtStm64Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'prot-STM64',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth100GbaseCwdm4Identity' : {
        'meta_info' : _MetaInfoClass('Eth100GbaseCwdm4Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'eth-100GBASE-CWDM4',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'ProtOc48Identity' : {
        'meta_info' : _MetaInfoClass('ProtOc48Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'prot-OC48',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'NonPluggableIdentity' : {
        'meta_info' : _MetaInfoClass('NonPluggableIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'non-pluggable',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth100G_AccIdentity' : {
        'meta_info' : _MetaInfoClass('Eth100G_AccIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'eth-100G_ACC',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Prot1GeIdentity' : {
        'meta_info' : _MetaInfoClass('Prot1GeIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'prot-1GE',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth40GbaseSr4Identity' : {
        'meta_info' : _MetaInfoClass('Eth40GbaseSr4Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'eth-40GBASE-SR4',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth40GbasePsm4Identity' : {
        'meta_info' : _MetaInfoClass('Eth40GbasePsm4Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'eth-40GBASE-PSM4',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'OtherIdentity' : {
        'meta_info' : _MetaInfoClass('OtherIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'other',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'TribRate40GIdentity' : {
        'meta_info' : _MetaInfoClass('TribRate40GIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'trib-rate-40G',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'X2Identity' : {
        'meta_info' : _MetaInfoClass('X2Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'X2',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'XfpIdentity' : {
        'meta_info' : _MetaInfoClass('XfpIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'XFP',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth10GbaseSrIdentity' : {
        'meta_info' : _MetaInfoClass('Eth10GbaseSrIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'eth-10GBASE-SR',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'EthUndefinedIdentity' : {
        'meta_info' : _MetaInfoClass('EthUndefinedIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'eth-undefined',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'TribRate10GIdentity' : {
        'meta_info' : _MetaInfoClass('TribRate10GIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'trib-rate-10G',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth100GbaseSr4Identity' : {
        'meta_info' : _MetaInfoClass('Eth100GbaseSr4Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'eth-100GBASE-SR4',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'OtnUndefinedIdentity' : {
        'meta_info' : _MetaInfoClass('OtnUndefinedIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'otn-undefined',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'TribRate1GIdentity' : {
        'meta_info' : _MetaInfoClass('TribRate1GIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'trib-rate-1G',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth100GbaseLr4Identity' : {
        'meta_info' : _MetaInfoClass('Eth100GbaseLr4Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'eth-100GBASE-LR4',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'TribRate2__Dot__5GIdentity' : {
        'meta_info' : _MetaInfoClass('TribRate2__Dot__5GIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'trib-rate-2.5G',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Prot100GeIdentity' : {
        'meta_info' : _MetaInfoClass('Prot100GeIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'prot-100GE',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'ProtStm256Identity' : {
        'meta_info' : _MetaInfoClass('ProtStm256Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'prot-STM256',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'LcConnectorIdentity' : {
        'meta_info' : _MetaInfoClass('LcConnectorIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'lc-connector',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'ProtOdu3Identity' : {
        'meta_info' : _MetaInfoClass('ProtOdu3Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'prot-ODU3',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'ProtOc768Identity' : {
        'meta_info' : _MetaInfoClass('ProtOc768Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'prot-OC768',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth4X10GbaseSrIdentity' : {
        'meta_info' : _MetaInfoClass('Eth4X10GbaseSrIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'eth-4x10GBASE-SR',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth4X10GbaseLrIdentity' : {
        'meta_info' : _MetaInfoClass('Eth4X10GbaseLrIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'eth-4x10GBASE-LR',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth10GbaseZrIdentity' : {
        'meta_info' : _MetaInfoClass('Eth10GbaseZrIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'eth-10GBASE-ZR',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'ProtOtu2EIdentity' : {
        'meta_info' : _MetaInfoClass('ProtOtu2EIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'prot-OTU2e',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'ScConnectorIdentity' : {
        'meta_info' : _MetaInfoClass('ScConnectorIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'sc-connector',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Vsr20003R2Identity' : {
        'meta_info' : _MetaInfoClass('Vsr20003R2Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'VSR2000-3R2',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'ProtOdu2Identity' : {
        'meta_info' : _MetaInfoClass('ProtOdu2Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'prot-ODU2',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'ProtEthernetIdentity' : {
        'meta_info' : _MetaInfoClass('ProtEthernetIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'prot-ethernet',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Prot40GeIdentity' : {
        'meta_info' : _MetaInfoClass('Prot40GeIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'prot-40GE',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'ProtOtu3Identity' : {
        'meta_info' : _MetaInfoClass('ProtOtu3Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'prot-OTU3',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'ProtOtu2Identity' : {
        'meta_info' : _MetaInfoClass('ProtOtu2Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'prot-OTU2',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Vsr20003R5Identity' : {
        'meta_info' : _MetaInfoClass('Vsr20003R5Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'VSR2000-3R5',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'QsfpIdentity' : {
        'meta_info' : _MetaInfoClass('QsfpIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'QSFP',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'ProtStm16Identity' : {
        'meta_info' : _MetaInfoClass('ProtStm16Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'prot-STM16',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'ProtOtnIdentity' : {
        'meta_info' : _MetaInfoClass('ProtOtnIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'prot-otn',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'ProtOdu2EIdentity' : {
        'meta_info' : _MetaInfoClass('ProtOdu2EIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'prot-ODU2e',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth40GbaseLr4Identity' : {
        'meta_info' : _MetaInfoClass('Eth40GbaseLr4Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'eth-40GBASE-LR4',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Vsr20003R3Identity' : {
        'meta_info' : _MetaInfoClass('Vsr20003R3Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'VSR2000-3R3',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'ProtOtu1EIdentity' : {
        'meta_info' : _MetaInfoClass('ProtOtu1EIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'prot-OTU1e',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'ProtOtucnIdentity' : {
        'meta_info' : _MetaInfoClass('ProtOtucnIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'prot-OTUCn',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth100GbaseSr10Identity' : {
        'meta_info' : _MetaInfoClass('Eth100GbaseSr10Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'eth-100GBASE-SR10',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth10GbaseLrIdentity' : {
        'meta_info' : _MetaInfoClass('Eth10GbaseLrIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'eth-10GBASE-LR',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'P1S12D2Identity' : {
        'meta_info' : _MetaInfoClass('P1S12D2Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'P1S1-2D2',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'MpoConnectorIdentity' : {
        'meta_info' : _MetaInfoClass('MpoConnectorIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'mpo-connector',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'TribRate100GIdentity' : {
        'meta_info' : _MetaInfoClass('TribRate100GIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'trib-rate-100G',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'CfpIdentity' : {
        'meta_info' : _MetaInfoClass('CfpIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'CFP',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
}
