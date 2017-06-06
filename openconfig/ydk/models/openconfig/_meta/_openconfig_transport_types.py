


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'AdminStateTypeEnum' : _MetaInfoEnum('AdminStateTypeEnum', 'ydk.models.openconfig.openconfig_transport_types',
        {
            'ENABLED':'ENABLED',
            'DISABLED':'DISABLED',
            'MAINT':'MAINT',
        }, 'openconfig-transport-types', _yang_ns._namespaces['openconfig-transport-types']),
    'LoopbackModeTypeEnum' : _MetaInfoEnum('LoopbackModeTypeEnum', 'ydk.models.openconfig.openconfig_transport_types',
        {
            'NONE':'NONE',
            'FACILITY':'FACILITY',
            'TERMINAL':'TERMINAL',
        }, 'openconfig-transport-types', _yang_ns._namespaces['openconfig-transport-types']),
    'Tributary_Rate_Class_TypeIdentity' : {
        'meta_info' : _MetaInfoClass('Tributary_Rate_Class_TypeIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'TRIBUTARY_RATE_CLASS_TYPE',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Tributary_Protocol_TypeIdentity' : {
        'meta_info' : _MetaInfoClass('Tributary_Protocol_TypeIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'TRIBUTARY_PROTOCOL_TYPE',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Ethernet_Pmd_TypeIdentity' : {
        'meta_info' : _MetaInfoClass('Ethernet_Pmd_TypeIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'ETHERNET_PMD_TYPE',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Fiber_Connector_TypeIdentity' : {
        'meta_info' : _MetaInfoClass('Fiber_Connector_TypeIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'FIBER_CONNECTOR_TYPE',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Otn_Application_CodeIdentity' : {
        'meta_info' : _MetaInfoClass('Otn_Application_CodeIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'OTN_APPLICATION_CODE',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Optical_ChannelIdentity' : {
        'meta_info' : _MetaInfoClass('Optical_ChannelIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'OPTICAL_CHANNEL',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Transceiver_Form_Factor_TypeIdentity' : {
        'meta_info' : _MetaInfoClass('Transceiver_Form_Factor_TypeIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'TRANSCEIVER_FORM_FACTOR_TYPE',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Logical_Element_Protocol_TypeIdentity' : {
        'meta_info' : _MetaInfoClass('Logical_Element_Protocol_TypeIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'LOGICAL_ELEMENT_PROTOCOL_TYPE',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Sonet_Application_CodeIdentity' : {
        'meta_info' : _MetaInfoClass('Sonet_Application_CodeIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'SONET_APPLICATION_CODE',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth_4X10Gbase_LrIdentity' : {
        'meta_info' : _MetaInfoClass('Eth_4X10Gbase_LrIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'ETH_4X10GBASE_LR',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth_10Gbase_SrIdentity' : {
        'meta_info' : _MetaInfoClass('Eth_10Gbase_SrIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'ETH_10GBASE_SR',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Prot_Otu3Identity' : {
        'meta_info' : _MetaInfoClass('Prot_Otu3Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'PROT_OTU3',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Prot_Otu4Identity' : {
        'meta_info' : _MetaInfoClass('Prot_Otu4Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'PROT_OTU4',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth_100Gbase_Sr4Identity' : {
        'meta_info' : _MetaInfoClass('Eth_100Gbase_Sr4Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'ETH_100GBASE_SR4',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Prot_Oc768Identity' : {
        'meta_info' : _MetaInfoClass('Prot_Oc768Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'PROT_OC768',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Prot_Oc48Identity' : {
        'meta_info' : _MetaInfoClass('Prot_Oc48Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'PROT_OC48',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Prot_10Ge_WanIdentity' : {
        'meta_info' : _MetaInfoClass('Prot_10Ge_WanIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'PROT_10GE_WAN',
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
    'Eth_100Gbase_Sr10Identity' : {
        'meta_info' : _MetaInfoClass('Eth_100Gbase_Sr10Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'ETH_100GBASE_SR10',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Prot_1GeIdentity' : {
        'meta_info' : _MetaInfoClass('Prot_1GeIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'PROT_1GE',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Otn_UndefinedIdentity' : {
        'meta_info' : _MetaInfoClass('Otn_UndefinedIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'OTN_UNDEFINED',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth_100Gbase_Lr4Identity' : {
        'meta_info' : _MetaInfoClass('Eth_100Gbase_Lr4Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'ETH_100GBASE_LR4',
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
    'Prot_Odu4Identity' : {
        'meta_info' : _MetaInfoClass('Prot_Odu4Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'PROT_ODU4',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Prot_Stm256Identity' : {
        'meta_info' : _MetaInfoClass('Prot_Stm256Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'PROT_STM256',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Prot_10Ge_LanIdentity' : {
        'meta_info' : _MetaInfoClass('Prot_10Ge_LanIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'PROT_10GE_LAN',
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
    'Eth_100Gbase_Clr4Identity' : {
        'meta_info' : _MetaInfoClass('Eth_100Gbase_Clr4Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'ETH_100GBASE_CLR4',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth_40Gbase_Lr4Identity' : {
        'meta_info' : _MetaInfoClass('Eth_40Gbase_Lr4Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'ETH_40GBASE_LR4',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth_10Gbase_ZrIdentity' : {
        'meta_info' : _MetaInfoClass('Eth_10Gbase_ZrIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'ETH_10GBASE_ZR',
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
    'Eth_4X10Gbase_SrIdentity' : {
        'meta_info' : _MetaInfoClass('Eth_4X10Gbase_SrIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'ETH_4X10GBASE_SR',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth_100Gbase_Cr4Identity' : {
        'meta_info' : _MetaInfoClass('Eth_100Gbase_Cr4Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'ETH_100GBASE_CR4',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Vsr2000_3R5Identity' : {
        'meta_info' : _MetaInfoClass('Vsr2000_3R5Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'VSR2000_3R5',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Prot_100G_MlgIdentity' : {
        'meta_info' : _MetaInfoClass('Prot_100G_MlgIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'PROT_100G_MLG',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Prot_Odu3Identity' : {
        'meta_info' : _MetaInfoClass('Prot_Odu3Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'PROT_ODU3',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Trib_Rate_2__Dot__5GIdentity' : {
        'meta_info' : _MetaInfoClass('Trib_Rate_2__Dot__5GIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'TRIB_RATE_2.5G',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth_40Gbase_Cr4Identity' : {
        'meta_info' : _MetaInfoClass('Eth_40Gbase_Cr4Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'ETH_40GBASE_CR4',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Lc_ConnectorIdentity' : {
        'meta_info' : _MetaInfoClass('Lc_ConnectorIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'LC_CONNECTOR',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth_100G_AocIdentity' : {
        'meta_info' : _MetaInfoClass('Eth_100G_AocIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'ETH_100G_AOC',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Prot_Oc192Identity' : {
        'meta_info' : _MetaInfoClass('Prot_Oc192Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'PROT_OC192',
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
    'Trib_Rate_10GIdentity' : {
        'meta_info' : _MetaInfoClass('Trib_Rate_10GIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'TRIB_RATE_10G',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth_100G_AccIdentity' : {
        'meta_info' : _MetaInfoClass('Eth_100G_AccIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'ETH_100G_ACC',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth_40Gbase_Sr4Identity' : {
        'meta_info' : _MetaInfoClass('Eth_40Gbase_Sr4Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'ETH_40GBASE_SR4',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Prot_OtucnIdentity' : {
        'meta_info' : _MetaInfoClass('Prot_OtucnIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'PROT_OTUCN',
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
            'SFP_PLUS',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Trib_Rate_40GIdentity' : {
        'meta_info' : _MetaInfoClass('Trib_Rate_40GIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'TRIB_RATE_40G',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Trib_Rate_1GIdentity' : {
        'meta_info' : _MetaInfoClass('Trib_Rate_1GIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'TRIB_RATE_1G',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Prot_OtnIdentity' : {
        'meta_info' : _MetaInfoClass('Prot_OtnIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'PROT_OTN',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth_100Gbase_Er4Identity' : {
        'meta_info' : _MetaInfoClass('Eth_100Gbase_Er4Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'ETH_100GBASE_ER4',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth_100Gbase_Psm4Identity' : {
        'meta_info' : _MetaInfoClass('Eth_100Gbase_Psm4Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'ETH_100GBASE_PSM4',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth_100Gbase_Cwdm4Identity' : {
        'meta_info' : _MetaInfoClass('Eth_100Gbase_Cwdm4Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'ETH_100GBASE_CWDM4',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'P1S1_2D2Identity' : {
        'meta_info' : _MetaInfoClass('P1S1_2D2Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'P1S1_2D2',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Prot_40GeIdentity' : {
        'meta_info' : _MetaInfoClass('Prot_40GeIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'PROT_40GE',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Prot_Odu2EIdentity' : {
        'meta_info' : _MetaInfoClass('Prot_Odu2EIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'PROT_ODU2E',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Prot_Otu1EIdentity' : {
        'meta_info' : _MetaInfoClass('Prot_Otu1EIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'PROT_OTU1E',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'P1L1_2D1Identity' : {
        'meta_info' : _MetaInfoClass('P1L1_2D1Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'P1L1_2D1',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth_40Gbase_Psm4Identity' : {
        'meta_info' : _MetaInfoClass('Eth_40Gbase_Psm4Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'ETH_40GBASE_PSM4',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Vsr2000_3R3Identity' : {
        'meta_info' : _MetaInfoClass('Vsr2000_3R3Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'VSR2000_3R3',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'P1L1_2D2Identity' : {
        'meta_info' : _MetaInfoClass('P1L1_2D2Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'P1L1_2D2',
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
    'Trib_Rate_100GIdentity' : {
        'meta_info' : _MetaInfoClass('Trib_Rate_100GIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'TRIB_RATE_100G',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Prot_EthernetIdentity' : {
        'meta_info' : _MetaInfoClass('Prot_EthernetIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'PROT_ETHERNET',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth_10Gbase_LrIdentity' : {
        'meta_info' : _MetaInfoClass('Eth_10Gbase_LrIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'ETH_10GBASE_LR',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Vsr2000_3R2Identity' : {
        'meta_info' : _MetaInfoClass('Vsr2000_3R2Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'VSR2000_3R2',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Prot_Stm64Identity' : {
        'meta_info' : _MetaInfoClass('Prot_Stm64Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'PROT_STM64',
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
    'Eth_40Gbase_Er4Identity' : {
        'meta_info' : _MetaInfoClass('Eth_40Gbase_Er4Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'ETH_40GBASE_ER4',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Prot_100GeIdentity' : {
        'meta_info' : _MetaInfoClass('Prot_100GeIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'PROT_100GE',
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
            'OTHER',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Prot_Stm16Identity' : {
        'meta_info' : _MetaInfoClass('Prot_Stm16Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'PROT_STM16',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Mpo_ConnectorIdentity' : {
        'meta_info' : _MetaInfoClass('Mpo_ConnectorIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'MPO_CONNECTOR',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth_10Gbase_LrmIdentity' : {
        'meta_info' : _MetaInfoClass('Eth_10Gbase_LrmIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'ETH_10GBASE_LRM',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth_10Gbase_ErIdentity' : {
        'meta_info' : _MetaInfoClass('Eth_10Gbase_ErIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'ETH_10GBASE_ER',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Sonet_UndefinedIdentity' : {
        'meta_info' : _MetaInfoClass('Sonet_UndefinedIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'SONET_UNDEFINED',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Prot_Otu2EIdentity' : {
        'meta_info' : _MetaInfoClass('Prot_Otu2EIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'PROT_OTU2E',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Prot_Otu2Identity' : {
        'meta_info' : _MetaInfoClass('Prot_Otu2Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'PROT_OTU2',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Prot_Odu2Identity' : {
        'meta_info' : _MetaInfoClass('Prot_Odu2Identity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'PROT_ODU2',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Non_PluggableIdentity' : {
        'meta_info' : _MetaInfoClass('Non_PluggableIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'NON_PLUGGABLE',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Sc_ConnectorIdentity' : {
        'meta_info' : _MetaInfoClass('Sc_ConnectorIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'SC_CONNECTOR',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Cfp2_AcoIdentity' : {
        'meta_info' : _MetaInfoClass('Cfp2_AcoIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'CFP2_ACO',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
    'Eth_UndefinedIdentity' : {
        'meta_info' : _MetaInfoClass('Eth_UndefinedIdentity',
            False, 
            [
            ],
            'openconfig-transport-types',
            'ETH_UNDEFINED',
            _yang_ns._namespaces['openconfig-transport-types'],
        'ydk.models.openconfig.openconfig_transport_types'
        ),
    },
}
