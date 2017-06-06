


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'OriginEnum' : _MetaInfoEnum('OriginEnum', 'ydk.models.cisco_ios_xe.pim',
        {
            'other-origin':'other_origin',
            'pim-request':'pim_request',
            'ssm-request':'ssm_request',
            'fixed':'fixed',
            'embedded':'embedded',
            'static':'static',
            'config-ssm':'config_ssm',
            'auto-rp':'auto_rp',
            'bsr':'bsr',
            'msdp':'msdp',
        }, 'pim', _yang_ns._namespaces['pim']),
    'PimModeEnum' : _MetaInfoEnum('PimModeEnum', 'ydk.models.cisco_ios_xe.pim',
        {
            'sparse':'sparse',
            'dense':'dense',
            'sparse-dense':'sparse_dense',
            'dm-proxy':'dm_proxy',
            'none':'none',
        }, 'pim', _yang_ns._namespaces['pim']),
    'RouteProtocolTypeEnum' : _MetaInfoEnum('RouteProtocolTypeEnum', 'ydk.models.cisco_ios_xe.pim',
        {
            'other':'other',
            'local':'local',
            'netmgmt':'netmgmt',
            'icmp':'icmp',
            'egp':'egp',
            'ggp':'ggp',
            'hello':'hello',
            'rip':'rip',
            'isIs':'isIs',
            'esIs':'esIs',
            'ciscoIgrp':'ciscoIgrp',
            'bbnSpfIgp':'bbnSpfIgp',
            'ospf':'ospf',
            'bgp':'bgp',
            'idpr':'idpr',
            'ciscoEigrp':'ciscoEigrp',
            'dvmrp':'dvmrp',
        }, 'pim', _yang_ns._namespaces['pim']),
    'MrouteProtocolTypeEnum' : _MetaInfoEnum('MrouteProtocolTypeEnum', 'ydk.models.cisco_ios_xe.pim',
        {
            'other':'other',
            'local':'local',
            'netmgmt':'netmgmt',
            'dvmrp':'dvmrp',
            'mospf':'mospf',
            'pimSparseDense':'pimSparseDense',
            'cbt':'cbt',
            'pimSparseMode':'pimSparseMode',
            'pimDenseMode':'pimDenseMode',
            'igmpOnly':'igmpOnly',
            'bgmp':'bgmp',
            'msdp':'msdp',
        }, 'pim', _yang_ns._namespaces['pim']),
    'GroupToRpMappingModeIdentity' : {
        'meta_info' : _MetaInfoClass('GroupToRpMappingModeIdentity',
            False, 
            [
            ],
            'pim',
            'group-to-rp-mapping-mode',
            _yang_ns._namespaces['pim'],
        'ydk.models.cisco_ios_xe.pim'
        ),
    },
    'SmMappingModeIdentity' : {
        'meta_info' : _MetaInfoClass('SmMappingModeIdentity',
            False, 
            [
            ],
            'pim',
            'sm-mapping-mode',
            _yang_ns._namespaces['pim'],
        'ydk.models.cisco_ios_xe.pim'
        ),
    },
    'DmMappingModeIdentity' : {
        'meta_info' : _MetaInfoClass('DmMappingModeIdentity',
            False, 
            [
            ],
            'pim',
            'dm-mapping-mode',
            _yang_ns._namespaces['pim'],
        'ydk.models.cisco_ios_xe.pim'
        ),
    },
    'PimBidirMappingModeIdentity' : {
        'meta_info' : _MetaInfoClass('PimBidirMappingModeIdentity',
            False, 
            [
            ],
            'pim',
            'pim-bidir-mapping-mode',
            _yang_ns._namespaces['pim'],
        'ydk.models.cisco_ios_xe.pim'
        ),
    },
    'SsmMappingModeIdentity' : {
        'meta_info' : _MetaInfoClass('SsmMappingModeIdentity',
            False, 
            [
            ],
            'pim',
            'ssm-mapping-mode',
            _yang_ns._namespaces['pim'],
        'ydk.models.cisco_ios_xe.pim'
        ),
    },
    'OtherMappingModeIdentity' : {
        'meta_info' : _MetaInfoClass('OtherMappingModeIdentity',
            False, 
            [
            ],
            'pim',
            'other-mapping-mode',
            _yang_ns._namespaces['pim'],
        'ydk.models.cisco_ios_xe.pim'
        ),
    },
    'AsmMappingModeIdentity' : {
        'meta_info' : _MetaInfoClass('AsmMappingModeIdentity',
            False, 
            [
            ],
            'pim',
            'asm-mapping-mode',
            _yang_ns._namespaces['pim'],
        'ydk.models.cisco_ios_xe.pim'
        ),
    },
}
