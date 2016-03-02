


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'IanaInterfaceType_Identity' : {
        'meta_info' : _MetaInfoClass('IanaInterfaceType_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'iana-interface-type',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'A12MppSwitch_Identity' : {
        'meta_info' : _MetaInfoClass('A12MppSwitch_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'a12MppSwitch',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Aal2_Identity' : {
        'meta_info' : _MetaInfoClass('Aal2_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'aal2',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Aal5_Identity' : {
        'meta_info' : _MetaInfoClass('Aal5_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'aal5',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'ActelisMetaLOOP_Identity' : {
        'meta_info' : _MetaInfoClass('ActelisMetaLOOP_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'actelisMetaLOOP',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Adsl2_Identity' : {
        'meta_info' : _MetaInfoClass('Adsl2_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'adsl2',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Adsl2plus_Identity' : {
        'meta_info' : _MetaInfoClass('Adsl2plus_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'adsl2plus',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Adsl_Identity' : {
        'meta_info' : _MetaInfoClass('Adsl_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'adsl',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Aflane8023_Identity' : {
        'meta_info' : _MetaInfoClass('Aflane8023_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'aflane8023',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Aflane8025_Identity' : {
        'meta_info' : _MetaInfoClass('Aflane8025_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'aflane8025',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'AluELP_Identity' : {
        'meta_info' : _MetaInfoClass('AluELP_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'aluELP',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'AluEponLogicalLink_Identity' : {
        'meta_info' : _MetaInfoClass('AluEponLogicalLink_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'aluEponLogicalLink',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'AluEponOnu_Identity' : {
        'meta_info' : _MetaInfoClass('AluEponOnu_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'aluEponOnu',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'AluEponPhysicalUni_Identity' : {
        'meta_info' : _MetaInfoClass('AluEponPhysicalUni_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'aluEponPhysicalUni',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'AluEpon_Identity' : {
        'meta_info' : _MetaInfoClass('AluEpon_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'aluEpon',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'AluGponOnu_Identity' : {
        'meta_info' : _MetaInfoClass('AluGponOnu_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'aluGponOnu',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'AluGponPhysicalUni_Identity' : {
        'meta_info' : _MetaInfoClass('AluGponPhysicalUni_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'aluGponPhysicalUni',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Arap_Identity' : {
        'meta_info' : _MetaInfoClass('Arap_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'arap',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'ArcnetPlus_Identity' : {
        'meta_info' : _MetaInfoClass('ArcnetPlus_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'arcnetPlus',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Arcnet_Identity' : {
        'meta_info' : _MetaInfoClass('Arcnet_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'arcnet',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Async_Identity' : {
        'meta_info' : _MetaInfoClass('Async_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'async',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'AtmDxi_Identity' : {
        'meta_info' : _MetaInfoClass('AtmDxi_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'atmDxi',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'AtmFuni_Identity' : {
        'meta_info' : _MetaInfoClass('AtmFuni_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'atmFuni',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'AtmIma_Identity' : {
        'meta_info' : _MetaInfoClass('AtmIma_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'atmIma',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'AtmLogical_Identity' : {
        'meta_info' : _MetaInfoClass('AtmLogical_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'atmLogical',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'AtmRadio_Identity' : {
        'meta_info' : _MetaInfoClass('AtmRadio_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'atmRadio',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'AtmSubInterface_Identity' : {
        'meta_info' : _MetaInfoClass('AtmSubInterface_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'atmSubInterface',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'AtmVciEndPt_Identity' : {
        'meta_info' : _MetaInfoClass('AtmVciEndPt_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'atmVciEndPt',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'AtmVirtual_Identity' : {
        'meta_info' : _MetaInfoClass('AtmVirtual_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'atmVirtual',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Atm_Identity' : {
        'meta_info' : _MetaInfoClass('Atm_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'atm',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Atmbond_Identity' : {
        'meta_info' : _MetaInfoClass('Atmbond_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'atmbond',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'AviciOpticalEther_Identity' : {
        'meta_info' : _MetaInfoClass('AviciOpticalEther_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'aviciOpticalEther',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'BasicISDN_Identity' : {
        'meta_info' : _MetaInfoClass('BasicISDN_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'basicISDN',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Bgppolicyaccounting_Identity' : {
        'meta_info' : _MetaInfoClass('Bgppolicyaccounting_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'bgppolicyaccounting',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Bits_Identity' : {
        'meta_info' : _MetaInfoClass('Bits_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'bits',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Bridge_Identity' : {
        'meta_info' : _MetaInfoClass('Bridge_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'bridge',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Bsc_Identity' : {
        'meta_info' : _MetaInfoClass('Bsc_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'bsc',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'CableDownstreamRfPort_Identity' : {
        'meta_info' : _MetaInfoClass('CableDownstreamRfPort_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'cableDownstreamRfPort',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'CapwapDot11Bss_Identity' : {
        'meta_info' : _MetaInfoClass('CapwapDot11Bss_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'capwapDot11Bss',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'CapwapDot11Profile_Identity' : {
        'meta_info' : _MetaInfoClass('CapwapDot11Profile_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'capwapDot11Profile',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'CapwapWtpVirtualRadio_Identity' : {
        'meta_info' : _MetaInfoClass('CapwapWtpVirtualRadio_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'capwapWtpVirtualRadio',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'CblVectaStar_Identity' : {
        'meta_info' : _MetaInfoClass('CblVectaStar_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'cblVectaStar',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'CctEmul_Identity' : {
        'meta_info' : _MetaInfoClass('CctEmul_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'cctEmul',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Ces_Identity' : {
        'meta_info' : _MetaInfoClass('Ces_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'ces',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Channel_Identity' : {
        'meta_info' : _MetaInfoClass('Channel_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'channel',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'CiscoISLvlan_Identity' : {
        'meta_info' : _MetaInfoClass('CiscoISLvlan_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'ciscoISLvlan',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Cnr_Identity' : {
        'meta_info' : _MetaInfoClass('Cnr_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'cnr',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Coffee_Identity' : {
        'meta_info' : _MetaInfoClass('Coffee_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'coffee',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'CompositeLink_Identity' : {
        'meta_info' : _MetaInfoClass('CompositeLink_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'compositeLink',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Dcn_Identity' : {
        'meta_info' : _MetaInfoClass('Dcn_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'dcn',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'DdnX25_Identity' : {
        'meta_info' : _MetaInfoClass('DdnX25_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'ddnX25',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'DigitalPowerline_Identity' : {
        'meta_info' : _MetaInfoClass('DigitalPowerline_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'digitalPowerline',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'DigitalWrapperOverheadChannel_Identity' : {
        'meta_info' : _MetaInfoClass('DigitalWrapperOverheadChannel_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'digitalWrapperOverheadChannel',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Dlsw_Identity' : {
        'meta_info' : _MetaInfoClass('Dlsw_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'dlsw',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'DocsCableDownstream_Identity' : {
        'meta_info' : _MetaInfoClass('DocsCableDownstream_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'docsCableDownstream',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'DocsCableMCmtsDownstream_Identity' : {
        'meta_info' : _MetaInfoClass('DocsCableMCmtsDownstream_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'docsCableMCmtsDownstream',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'DocsCableMaclayer_Identity' : {
        'meta_info' : _MetaInfoClass('DocsCableMaclayer_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'docsCableMaclayer',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'DocsCableUpstreamChannel_Identity' : {
        'meta_info' : _MetaInfoClass('DocsCableUpstreamChannel_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'docsCableUpstreamChannel',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'DocsCableUpstreamRfPort_Identity' : {
        'meta_info' : _MetaInfoClass('DocsCableUpstreamRfPort_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'docsCableUpstreamRfPort',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'DocsCableUpstream_Identity' : {
        'meta_info' : _MetaInfoClass('DocsCableUpstream_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'docsCableUpstream',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Ds0Bundle_Identity' : {
        'meta_info' : _MetaInfoClass('Ds0Bundle_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'ds0Bundle',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Ds0_Identity' : {
        'meta_info' : _MetaInfoClass('Ds0_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'ds0',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Ds1FDL_Identity' : {
        'meta_info' : _MetaInfoClass('Ds1FDL_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'ds1FDL',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Ds1_Identity' : {
        'meta_info' : _MetaInfoClass('Ds1_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'ds1',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Ds3_Identity' : {
        'meta_info' : _MetaInfoClass('Ds3_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'ds3',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Dtm_Identity' : {
        'meta_info' : _MetaInfoClass('Dtm_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'dtm',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'DvbAsiIn_Identity' : {
        'meta_info' : _MetaInfoClass('DvbAsiIn_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'dvbAsiIn',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'DvbAsiOut_Identity' : {
        'meta_info' : _MetaInfoClass('DvbAsiOut_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'dvbAsiOut',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'DvbRccDownstream_Identity' : {
        'meta_info' : _MetaInfoClass('DvbRccDownstream_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'dvbRccDownstream',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'DvbRccMacLayer_Identity' : {
        'meta_info' : _MetaInfoClass('DvbRccMacLayer_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'dvbRccMacLayer',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'DvbRccUpstream_Identity' : {
        'meta_info' : _MetaInfoClass('DvbRccUpstream_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'dvbRccUpstream',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'DvbRcsMacLayer_Identity' : {
        'meta_info' : _MetaInfoClass('DvbRcsMacLayer_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'dvbRcsMacLayer',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'DvbRcsTdma_Identity' : {
        'meta_info' : _MetaInfoClass('DvbRcsTdma_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'dvbRcsTdma',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'DvbTdm_Identity' : {
        'meta_info' : _MetaInfoClass('DvbTdm_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'dvbTdm',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'E1_Identity' : {
        'meta_info' : _MetaInfoClass('E1_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'e1',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Econet_Identity' : {
        'meta_info' : _MetaInfoClass('Econet_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'econet',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Eon_Identity' : {
        'meta_info' : _MetaInfoClass('Eon_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'eon',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Eplrs_Identity' : {
        'meta_info' : _MetaInfoClass('Eplrs_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'eplrs',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Escon_Identity' : {
        'meta_info' : _MetaInfoClass('Escon_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'escon',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Ethernet3Mbit_Identity' : {
        'meta_info' : _MetaInfoClass('Ethernet3Mbit_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'ethernet3Mbit',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'EthernetCsmacd_Identity' : {
        'meta_info' : _MetaInfoClass('EthernetCsmacd_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'ethernetCsmacd',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'FastEtherFX_Identity' : {
        'meta_info' : _MetaInfoClass('FastEtherFX_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'fastEtherFX',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'FastEther_Identity' : {
        'meta_info' : _MetaInfoClass('FastEther_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'fastEther',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Fast_Identity' : {
        'meta_info' : _MetaInfoClass('Fast_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'fast',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'FcipLink_Identity' : {
        'meta_info' : _MetaInfoClass('FcipLink_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'fcipLink',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Fddi_Identity' : {
        'meta_info' : _MetaInfoClass('Fddi_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'fddi',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'FibreChannel_Identity' : {
        'meta_info' : _MetaInfoClass('FibreChannel_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'fibreChannel',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'FrDlciEndPt_Identity' : {
        'meta_info' : _MetaInfoClass('FrDlciEndPt_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'frDlciEndPt',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'FrForward_Identity' : {
        'meta_info' : _MetaInfoClass('FrForward_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'frForward',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'FrameRelayInterconnect_Identity' : {
        'meta_info' : _MetaInfoClass('FrameRelayInterconnect_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'frameRelayInterconnect',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'FrameRelayMPI_Identity' : {
        'meta_info' : _MetaInfoClass('FrameRelayMPI_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'frameRelayMPI',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'FrameRelayService_Identity' : {
        'meta_info' : _MetaInfoClass('FrameRelayService_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'frameRelayService',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'FrameRelay_Identity' : {
        'meta_info' : _MetaInfoClass('FrameRelay_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'frameRelay',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Frf16MfrBundle_Identity' : {
        'meta_info' : _MetaInfoClass('Frf16MfrBundle_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'frf16MfrBundle',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'G703at2mb_Identity' : {
        'meta_info' : _MetaInfoClass('G703at2mb_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'g703at2mb',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'G703at64k_Identity' : {
        'meta_info' : _MetaInfoClass('G703at64k_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'g703at64k',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'G9981_Identity' : {
        'meta_info' : _MetaInfoClass('G9981_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'g9981',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'G9982_Identity' : {
        'meta_info' : _MetaInfoClass('G9982_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'g9982',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'G9983_Identity' : {
        'meta_info' : _MetaInfoClass('G9983_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'g9983',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Gfp_Identity' : {
        'meta_info' : _MetaInfoClass('Gfp_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'gfp',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'GigabitEthernet_Identity' : {
        'meta_info' : _MetaInfoClass('GigabitEthernet_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'gigabitEthernet',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Gpon_Identity' : {
        'meta_info' : _MetaInfoClass('Gpon_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'gpon',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Gr303IDT_Identity' : {
        'meta_info' : _MetaInfoClass('Gr303IDT_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'gr303IDT',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Gr303RDT_Identity' : {
        'meta_info' : _MetaInfoClass('Gr303RDT_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'gr303RDT',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Gtp_Identity' : {
        'meta_info' : _MetaInfoClass('Gtp_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'gtp',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'H323Gatekeeper_Identity' : {
        'meta_info' : _MetaInfoClass('H323Gatekeeper_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'h323Gatekeeper',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'H323Proxy_Identity' : {
        'meta_info' : _MetaInfoClass('H323Proxy_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'h323Proxy',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Hdh1822_Identity' : {
        'meta_info' : _MetaInfoClass('Hdh1822_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'hdh1822',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Hdlc_Identity' : {
        'meta_info' : _MetaInfoClass('Hdlc_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'hdlc',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Hdsl2_Identity' : {
        'meta_info' : _MetaInfoClass('Hdsl2_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'hdsl2',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Hiperlan2_Identity' : {
        'meta_info' : _MetaInfoClass('Hiperlan2_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'hiperlan2',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'HippiInterface_Identity' : {
        'meta_info' : _MetaInfoClass('HippiInterface_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'hippiInterface',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Hippi_Identity' : {
        'meta_info' : _MetaInfoClass('Hippi_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'hippi',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Homepna_Identity' : {
        'meta_info' : _MetaInfoClass('Homepna_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'homepna',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'HostPad_Identity' : {
        'meta_info' : _MetaInfoClass('HostPad_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'hostPad',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Hssi_Identity' : {
        'meta_info' : _MetaInfoClass('Hssi_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'hssi',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Hyperchannel_Identity' : {
        'meta_info' : _MetaInfoClass('Hyperchannel_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'hyperchannel',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Ibm370parChan_Identity' : {
        'meta_info' : _MetaInfoClass('Ibm370parChan_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'ibm370parChan',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Idsl_Identity' : {
        'meta_info' : _MetaInfoClass('Idsl_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'idsl',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Ieee1394_Identity' : {
        'meta_info' : _MetaInfoClass('Ieee1394_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'ieee1394',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Ieee80211_Identity' : {
        'meta_info' : _MetaInfoClass('Ieee80211_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'ieee80211',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Ieee80212_Identity' : {
        'meta_info' : _MetaInfoClass('Ieee80212_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'ieee80212',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Ieee802154_Identity' : {
        'meta_info' : _MetaInfoClass('Ieee802154_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'ieee802154',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Ieee80216WMAN_Identity' : {
        'meta_info' : _MetaInfoClass('Ieee80216WMAN_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'ieee80216WMAN',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Ieee8023adLag_Identity' : {
        'meta_info' : _MetaInfoClass('Ieee8023adLag_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'ieee8023adLag',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'IfGsn_Identity' : {
        'meta_info' : _MetaInfoClass('IfGsn_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'if-gsn',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'IfPwType_Identity' : {
        'meta_info' : _MetaInfoClass('IfPwType_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'ifPwType',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'IfVfiType_Identity' : {
        'meta_info' : _MetaInfoClass('IfVfiType_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'ifVfiType',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Ilan_Identity' : {
        'meta_info' : _MetaInfoClass('Ilan_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'ilan',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Imt_Identity' : {
        'meta_info' : _MetaInfoClass('Imt_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'imt',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Infiniband_Identity' : {
        'meta_info' : _MetaInfoClass('Infiniband_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'infiniband',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Interleave_Identity' : {
        'meta_info' : _MetaInfoClass('Interleave_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'interleave',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'IpForward_Identity' : {
        'meta_info' : _MetaInfoClass('IpForward_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'ipForward',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'IpOverAtm_Identity' : {
        'meta_info' : _MetaInfoClass('IpOverAtm_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'ipOverAtm',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'IpOverCdlc_Identity' : {
        'meta_info' : _MetaInfoClass('IpOverCdlc_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'ipOverCdlc',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'IpOverClaw_Identity' : {
        'meta_info' : _MetaInfoClass('IpOverClaw_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'ipOverClaw',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'IpSwitch_Identity' : {
        'meta_info' : _MetaInfoClass('IpSwitch_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'ipSwitch',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Ip_Identity' : {
        'meta_info' : _MetaInfoClass('Ip_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'ip',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Isdn_Identity' : {
        'meta_info' : _MetaInfoClass('Isdn_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'isdn',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Isdns_Identity' : {
        'meta_info' : _MetaInfoClass('Isdns_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'isdns',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Isdnu_Identity' : {
        'meta_info' : _MetaInfoClass('Isdnu_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'isdnu',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Iso88022llc_Identity' : {
        'meta_info' : _MetaInfoClass('Iso88022llc_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'iso88022llc',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Iso88023Csmacd_Identity' : {
        'meta_info' : _MetaInfoClass('Iso88023Csmacd_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'iso88023Csmacd',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Iso88024TokenBus_Identity' : {
        'meta_info' : _MetaInfoClass('Iso88024TokenBus_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'iso88024TokenBus',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Iso88025CRFPInt_Identity' : {
        'meta_info' : _MetaInfoClass('Iso88025CRFPInt_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'iso88025CRFPInt',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Iso88025Dtr_Identity' : {
        'meta_info' : _MetaInfoClass('Iso88025Dtr_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'iso88025Dtr',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Iso88025Fiber_Identity' : {
        'meta_info' : _MetaInfoClass('Iso88025Fiber_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'iso88025Fiber',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Iso88025TokenRing_Identity' : {
        'meta_info' : _MetaInfoClass('Iso88025TokenRing_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'iso88025TokenRing',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Iso88026Man_Identity' : {
        'meta_info' : _MetaInfoClass('Iso88026Man_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'iso88026Man',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Isup_Identity' : {
        'meta_info' : _MetaInfoClass('Isup_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'isup',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'L2vlan_Identity' : {
        'meta_info' : _MetaInfoClass('L2vlan_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'l2vlan',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'L3ipvlan_Identity' : {
        'meta_info' : _MetaInfoClass('L3ipvlan_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'l3ipvlan',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'L3ipxvlan_Identity' : {
        'meta_info' : _MetaInfoClass('L3ipxvlan_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'l3ipxvlan',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Lapb_Identity' : {
        'meta_info' : _MetaInfoClass('Lapb_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'lapb',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Lapd_Identity' : {
        'meta_info' : _MetaInfoClass('Lapd_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'lapd',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Lapf_Identity' : {
        'meta_info' : _MetaInfoClass('Lapf_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'lapf',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Linegroup_Identity' : {
        'meta_info' : _MetaInfoClass('Linegroup_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'linegroup',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Lmp_Identity' : {
        'meta_info' : _MetaInfoClass('Lmp_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'lmp',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'LocalTalk_Identity' : {
        'meta_info' : _MetaInfoClass('LocalTalk_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'localTalk',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'MacSecControlledIF_Identity' : {
        'meta_info' : _MetaInfoClass('MacSecControlledIF_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'macSecControlledIF',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'MacSecUncontrolledIF_Identity' : {
        'meta_info' : _MetaInfoClass('MacSecUncontrolledIF_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'macSecUncontrolledIF',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'MediaMailOverIp_Identity' : {
        'meta_info' : _MetaInfoClass('MediaMailOverIp_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'mediaMailOverIp',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'MfSigLink_Identity' : {
        'meta_info' : _MetaInfoClass('MfSigLink_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'mfSigLink',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Miox25_Identity' : {
        'meta_info' : _MetaInfoClass('Miox25_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'miox25',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'MocaVersion1_Identity' : {
        'meta_info' : _MetaInfoClass('MocaVersion1_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'mocaVersion1',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Modem_Identity' : {
        'meta_info' : _MetaInfoClass('Modem_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'modem',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Mpc_Identity' : {
        'meta_info' : _MetaInfoClass('Mpc_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'mpc',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'MpegTransport_Identity' : {
        'meta_info' : _MetaInfoClass('MpegTransport_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'mpegTransport',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'MplsTunnel_Identity' : {
        'meta_info' : _MetaInfoClass('MplsTunnel_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'mplsTunnel',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Mpls_Identity' : {
        'meta_info' : _MetaInfoClass('Mpls_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'mpls',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Msdsl_Identity' : {
        'meta_info' : _MetaInfoClass('Msdsl_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'msdsl',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Mvl_Identity' : {
        'meta_info' : _MetaInfoClass('Mvl_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'mvl',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Myrinet_Identity' : {
        'meta_info' : _MetaInfoClass('Myrinet_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'myrinet',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Nfas_Identity' : {
        'meta_info' : _MetaInfoClass('Nfas_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'nfas',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Nsip_Identity' : {
        'meta_info' : _MetaInfoClass('Nsip_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'nsip',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'OpticalChannelGroup_Identity' : {
        'meta_info' : _MetaInfoClass('OpticalChannelGroup_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'opticalChannelGroup',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'OpticalChannel_Identity' : {
        'meta_info' : _MetaInfoClass('OpticalChannel_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'opticalChannel',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'OpticalTransport_Identity' : {
        'meta_info' : _MetaInfoClass('OpticalTransport_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'opticalTransport',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Other_Identity' : {
        'meta_info' : _MetaInfoClass('Other_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'other',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'OtnOdu_Identity' : {
        'meta_info' : _MetaInfoClass('OtnOdu_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'otnOdu',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'OtnOtu_Identity' : {
        'meta_info' : _MetaInfoClass('OtnOtu_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'otnOtu',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Para_Identity' : {
        'meta_info' : _MetaInfoClass('Para_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'para',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'PdnEtherLoop1_Identity' : {
        'meta_info' : _MetaInfoClass('PdnEtherLoop1_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'pdnEtherLoop1',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'PdnEtherLoop2_Identity' : {
        'meta_info' : _MetaInfoClass('PdnEtherLoop2_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'pdnEtherLoop2',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Pip_Identity' : {
        'meta_info' : _MetaInfoClass('Pip_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'pip',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Plc_Identity' : {
        'meta_info' : _MetaInfoClass('Plc_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'plc',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Pon155_Identity' : {
        'meta_info' : _MetaInfoClass('Pon155_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'pon155',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Pon622_Identity' : {
        'meta_info' : _MetaInfoClass('Pon622_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'pon622',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Pos_Identity' : {
        'meta_info' : _MetaInfoClass('Pos_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'pos',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'PppMultilinkBundle_Identity' : {
        'meta_info' : _MetaInfoClass('PppMultilinkBundle_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'pppMultilinkBundle',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Ppp_Identity' : {
        'meta_info' : _MetaInfoClass('Ppp_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'ppp',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'PrimaryISDN_Identity' : {
        'meta_info' : _MetaInfoClass('PrimaryISDN_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'primaryISDN',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'PropAtm_Identity' : {
        'meta_info' : _MetaInfoClass('PropAtm_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'propAtm',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'PropBWAp2Mp_Identity' : {
        'meta_info' : _MetaInfoClass('PropBWAp2Mp_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'propBWAp2Mp',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'PropCnls_Identity' : {
        'meta_info' : _MetaInfoClass('PropCnls_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'propCnls',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'PropDocsWirelessDownstream_Identity' : {
        'meta_info' : _MetaInfoClass('PropDocsWirelessDownstream_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'propDocsWirelessDownstream',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'PropDocsWirelessMaclayer_Identity' : {
        'meta_info' : _MetaInfoClass('PropDocsWirelessMaclayer_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'propDocsWirelessMaclayer',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'PropDocsWirelessUpstream_Identity' : {
        'meta_info' : _MetaInfoClass('PropDocsWirelessUpstream_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'propDocsWirelessUpstream',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'PropMultiplexor_Identity' : {
        'meta_info' : _MetaInfoClass('PropMultiplexor_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'propMultiplexor',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'PropPointToPointSerial_Identity' : {
        'meta_info' : _MetaInfoClass('PropPointToPointSerial_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'propPointToPointSerial',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'PropVirtual_Identity' : {
        'meta_info' : _MetaInfoClass('PropVirtual_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'propVirtual',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'PropWirelessP2P_Identity' : {
        'meta_info' : _MetaInfoClass('PropWirelessP2P_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'propWirelessP2P',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Proteon10Mbit_Identity' : {
        'meta_info' : _MetaInfoClass('Proteon10Mbit_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'proteon10Mbit',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Proteon80Mbit_Identity' : {
        'meta_info' : _MetaInfoClass('Proteon80Mbit_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'proteon80Mbit',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Q2931_Identity' : {
        'meta_info' : _MetaInfoClass('Q2931_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'q2931',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Qam_Identity' : {
        'meta_info' : _MetaInfoClass('Qam_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'qam',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Qllc_Identity' : {
        'meta_info' : _MetaInfoClass('Qllc_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'qllc',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'RadioMAC_Identity' : {
        'meta_info' : _MetaInfoClass('RadioMAC_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'radioMAC',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Radsl_Identity' : {
        'meta_info' : _MetaInfoClass('Radsl_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'radsl',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'ReachDSL_Identity' : {
        'meta_info' : _MetaInfoClass('ReachDSL_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'reachDSL',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Regular1822_Identity' : {
        'meta_info' : _MetaInfoClass('Regular1822_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'regular1822',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Rfc1483_Identity' : {
        'meta_info' : _MetaInfoClass('Rfc1483_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'rfc1483',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Rfc877x25_Identity' : {
        'meta_info' : _MetaInfoClass('Rfc877x25_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'rfc877x25',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Rpr_Identity' : {
        'meta_info' : _MetaInfoClass('Rpr_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'rpr',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Rs232_Identity' : {
        'meta_info' : _MetaInfoClass('Rs232_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'rs232',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Rsrb_Identity' : {
        'meta_info' : _MetaInfoClass('Rsrb_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'rsrb',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Sdlc_Identity' : {
        'meta_info' : _MetaInfoClass('Sdlc_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'sdlc',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Sdsl_Identity' : {
        'meta_info' : _MetaInfoClass('Sdsl_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'sdsl',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Shdsl_Identity' : {
        'meta_info' : _MetaInfoClass('Shdsl_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'shdsl',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'SipSig_Identity' : {
        'meta_info' : _MetaInfoClass('SipSig_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'sipSig',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'SipTg_Identity' : {
        'meta_info' : _MetaInfoClass('SipTg_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'sipTg',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Sip_Identity' : {
        'meta_info' : _MetaInfoClass('Sip_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'sip',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'SixToFour_Identity' : {
        'meta_info' : _MetaInfoClass('SixToFour_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'sixToFour',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Slip_Identity' : {
        'meta_info' : _MetaInfoClass('Slip_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'slip',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'SmdsDxi_Identity' : {
        'meta_info' : _MetaInfoClass('SmdsDxi_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'smdsDxi',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'SmdsIcip_Identity' : {
        'meta_info' : _MetaInfoClass('SmdsIcip_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'smdsIcip',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'SoftwareLoopback_Identity' : {
        'meta_info' : _MetaInfoClass('SoftwareLoopback_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'softwareLoopback',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'SonetOverheadChannel_Identity' : {
        'meta_info' : _MetaInfoClass('SonetOverheadChannel_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'sonetOverheadChannel',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'SonetPath_Identity' : {
        'meta_info' : _MetaInfoClass('SonetPath_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'sonetPath',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'SonetVT_Identity' : {
        'meta_info' : _MetaInfoClass('SonetVT_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'sonetVT',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Sonet_Identity' : {
        'meta_info' : _MetaInfoClass('Sonet_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'sonet',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Srp_Identity' : {
        'meta_info' : _MetaInfoClass('Srp_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'srp',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Ss7SigLink_Identity' : {
        'meta_info' : _MetaInfoClass('Ss7SigLink_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'ss7SigLink',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'StackToStack_Identity' : {
        'meta_info' : _MetaInfoClass('StackToStack_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'stackToStack',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'StarLan_Identity' : {
        'meta_info' : _MetaInfoClass('StarLan_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'starLan',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Tdlc_Identity' : {
        'meta_info' : _MetaInfoClass('Tdlc_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'tdlc',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'TeLink_Identity' : {
        'meta_info' : _MetaInfoClass('TeLink_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'teLink',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'TermPad_Identity' : {
        'meta_info' : _MetaInfoClass('TermPad_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'termPad',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Tr008_Identity' : {
        'meta_info' : _MetaInfoClass('Tr008_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'tr008',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'TranspHdlc_Identity' : {
        'meta_info' : _MetaInfoClass('TranspHdlc_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'transpHdlc',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Tunnel_Identity' : {
        'meta_info' : _MetaInfoClass('Tunnel_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'tunnel',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Ultra_Identity' : {
        'meta_info' : _MetaInfoClass('Ultra_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'ultra',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Usb_Identity' : {
        'meta_info' : _MetaInfoClass('Usb_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'usb',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'V11_Identity' : {
        'meta_info' : _MetaInfoClass('V11_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'v11',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'V35_Identity' : {
        'meta_info' : _MetaInfoClass('V35_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'v35',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'V36_Identity' : {
        'meta_info' : _MetaInfoClass('V36_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'v36',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'V37_Identity' : {
        'meta_info' : _MetaInfoClass('V37_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'v37',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Vdsl2_Identity' : {
        'meta_info' : _MetaInfoClass('Vdsl2_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'vdsl2',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Vdsl_Identity' : {
        'meta_info' : _MetaInfoClass('Vdsl_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'vdsl',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'VirtualIpAddress_Identity' : {
        'meta_info' : _MetaInfoClass('VirtualIpAddress_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'virtualIpAddress',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'VirtualTg_Identity' : {
        'meta_info' : _MetaInfoClass('VirtualTg_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'virtualTg',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'VmwareNicTeam_Identity' : {
        'meta_info' : _MetaInfoClass('VmwareNicTeam_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'vmwareNicTeam',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'VmwareVirtualNic_Identity' : {
        'meta_info' : _MetaInfoClass('VmwareVirtualNic_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'vmwareVirtualNic',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'VoiceDID_Identity' : {
        'meta_info' : _MetaInfoClass('VoiceDID_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'voiceDID',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'VoiceEBS_Identity' : {
        'meta_info' : _MetaInfoClass('VoiceEBS_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'voiceEBS',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'VoiceEMFGD_Identity' : {
        'meta_info' : _MetaInfoClass('VoiceEMFGD_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'voiceEMFGD',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'VoiceEM_Identity' : {
        'meta_info' : _MetaInfoClass('VoiceEM_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'voiceEM',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'VoiceEncap_Identity' : {
        'meta_info' : _MetaInfoClass('VoiceEncap_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'voiceEncap',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'VoiceFGDEANA_Identity' : {
        'meta_info' : _MetaInfoClass('VoiceFGDEANA_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'voiceFGDEANA',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'VoiceFGDOS_Identity' : {
        'meta_info' : _MetaInfoClass('VoiceFGDOS_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'voiceFGDOS',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'VoiceFXO_Identity' : {
        'meta_info' : _MetaInfoClass('VoiceFXO_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'voiceFXO',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'VoiceFXS_Identity' : {
        'meta_info' : _MetaInfoClass('VoiceFXS_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'voiceFXS',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'VoiceOverAtm_Identity' : {
        'meta_info' : _MetaInfoClass('VoiceOverAtm_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'voiceOverAtm',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'VoiceOverCable_Identity' : {
        'meta_info' : _MetaInfoClass('VoiceOverCable_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'voiceOverCable',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'VoiceOverFrameRelay_Identity' : {
        'meta_info' : _MetaInfoClass('VoiceOverFrameRelay_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'voiceOverFrameRelay',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'VoiceOverIp_Identity' : {
        'meta_info' : _MetaInfoClass('VoiceOverIp_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'voiceOverIp',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'WwanPP2_Identity' : {
        'meta_info' : _MetaInfoClass('WwanPP2_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'wwanPP2',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'WwanPP_Identity' : {
        'meta_info' : _MetaInfoClass('WwanPP_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'wwanPP',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'X213_Identity' : {
        'meta_info' : _MetaInfoClass('X213_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'x213',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'X25huntGroup_Identity' : {
        'meta_info' : _MetaInfoClass('X25huntGroup_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'x25huntGroup',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'X25mlp_Identity' : {
        'meta_info' : _MetaInfoClass('X25mlp_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'x25mlp',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'X25ple_Identity' : {
        'meta_info' : _MetaInfoClass('X25ple_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'x25ple',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'X86Laps_Identity' : {
        'meta_info' : _MetaInfoClass('X86Laps_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'x86Laps',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
}
