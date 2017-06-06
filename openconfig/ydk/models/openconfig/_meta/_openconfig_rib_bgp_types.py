


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'Bgp_Not_Selected_BestpathIdentity' : {
        'meta_info' : _MetaInfoClass('Bgp_Not_Selected_BestpathIdentity',
            False, 
            [
            ],
            'openconfig-rib-bgp-types',
            'BGP_NOT_SELECTED_BESTPATH',
            _yang_ns._namespaces['openconfig-rib-bgp-types'],
        'ydk.models.openconfig.openconfig_rib_bgp_types'
        ),
    },
    'Invalid_Route_ReasonIdentity' : {
        'meta_info' : _MetaInfoClass('Invalid_Route_ReasonIdentity',
            False, 
            [
            ],
            'openconfig-rib-bgp-types',
            'INVALID_ROUTE_REASON',
            _yang_ns._namespaces['openconfig-rib-bgp-types'],
        'ydk.models.openconfig.openconfig_rib_bgp_types'
        ),
    },
    'Bgp_Not_Selected_PolicyIdentity' : {
        'meta_info' : _MetaInfoClass('Bgp_Not_Selected_PolicyIdentity',
            False, 
            [
            ],
            'openconfig-rib-bgp-types',
            'BGP_NOT_SELECTED_POLICY',
            _yang_ns._namespaces['openconfig-rib-bgp-types'],
        'ydk.models.openconfig.openconfig_rib_bgp_types'
        ),
    },
    'Nexthop_Cost_HigherIdentity' : {
        'meta_info' : _MetaInfoClass('Nexthop_Cost_HigherIdentity',
            False, 
            [
            ],
            'openconfig-rib-bgp-types',
            'NEXTHOP_COST_HIGHER',
            _yang_ns._namespaces['openconfig-rib-bgp-types'],
        'ydk.models.openconfig.openconfig_rib_bgp_types'
        ),
    },
    'Invalid_As_LoopIdentity' : {
        'meta_info' : _MetaInfoClass('Invalid_As_LoopIdentity',
            False, 
            [
            ],
            'openconfig-rib-bgp-types',
            'INVALID_AS_LOOP',
            _yang_ns._namespaces['openconfig-rib-bgp-types'],
        'ydk.models.openconfig.openconfig_rib_bgp_types'
        ),
    },
    'Invalid_ConfedIdentity' : {
        'meta_info' : _MetaInfoClass('Invalid_ConfedIdentity',
            False, 
            [
            ],
            'openconfig-rib-bgp-types',
            'INVALID_CONFED',
            _yang_ns._namespaces['openconfig-rib-bgp-types'],
        'ydk.models.openconfig.openconfig_rib_bgp_types'
        ),
    },
    'Invalid_OriginatorIdentity' : {
        'meta_info' : _MetaInfoClass('Invalid_OriginatorIdentity',
            False, 
            [
            ],
            'openconfig-rib-bgp-types',
            'INVALID_ORIGINATOR',
            _yang_ns._namespaces['openconfig-rib-bgp-types'],
        'ydk.models.openconfig.openconfig_rib_bgp_types'
        ),
    },
    'Local_Pref_LowerIdentity' : {
        'meta_info' : _MetaInfoClass('Local_Pref_LowerIdentity',
            False, 
            [
            ],
            'openconfig-rib-bgp-types',
            'LOCAL_PREF_LOWER',
            _yang_ns._namespaces['openconfig-rib-bgp-types'],
        'ydk.models.openconfig.openconfig_rib_bgp_types'
        ),
    },
    'Higher_Router_IdIdentity' : {
        'meta_info' : _MetaInfoClass('Higher_Router_IdIdentity',
            False, 
            [
            ],
            'openconfig-rib-bgp-types',
            'HIGHER_ROUTER_ID',
            _yang_ns._namespaces['openconfig-rib-bgp-types'],
        'ydk.models.openconfig.openconfig_rib_bgp_types'
        ),
    },
    'Origin_Type_HigherIdentity' : {
        'meta_info' : _MetaInfoClass('Origin_Type_HigherIdentity',
            False, 
            [
            ],
            'openconfig-rib-bgp-types',
            'ORIGIN_TYPE_HIGHER',
            _yang_ns._namespaces['openconfig-rib-bgp-types'],
        'ydk.models.openconfig.openconfig_rib_bgp_types'
        ),
    },
    'Higher_Peer_AddressIdentity' : {
        'meta_info' : _MetaInfoClass('Higher_Peer_AddressIdentity',
            False, 
            [
            ],
            'openconfig-rib-bgp-types',
            'HIGHER_PEER_ADDRESS',
            _yang_ns._namespaces['openconfig-rib-bgp-types'],
        'ydk.models.openconfig.openconfig_rib_bgp_types'
        ),
    },
    'Invalid_Cluster_LoopIdentity' : {
        'meta_info' : _MetaInfoClass('Invalid_Cluster_LoopIdentity',
            False, 
            [
            ],
            'openconfig-rib-bgp-types',
            'INVALID_CLUSTER_LOOP',
            _yang_ns._namespaces['openconfig-rib-bgp-types'],
        'ydk.models.openconfig.openconfig_rib_bgp_types'
        ),
    },
    'As_Path_LongerIdentity' : {
        'meta_info' : _MetaInfoClass('As_Path_LongerIdentity',
            False, 
            [
            ],
            'openconfig-rib-bgp-types',
            'AS_PATH_LONGER',
            _yang_ns._namespaces['openconfig-rib-bgp-types'],
        'ydk.models.openconfig.openconfig_rib_bgp_types'
        ),
    },
    'Rejected_Import_PolicyIdentity' : {
        'meta_info' : _MetaInfoClass('Rejected_Import_PolicyIdentity',
            False, 
            [
            ],
            'openconfig-rib-bgp-types',
            'REJECTED_IMPORT_POLICY',
            _yang_ns._namespaces['openconfig-rib-bgp-types'],
        'ydk.models.openconfig.openconfig_rib_bgp_types'
        ),
    },
    'Med_HigherIdentity' : {
        'meta_info' : _MetaInfoClass('Med_HigherIdentity',
            False, 
            [
            ],
            'openconfig-rib-bgp-types',
            'MED_HIGHER',
            _yang_ns._namespaces['openconfig-rib-bgp-types'],
        'ydk.models.openconfig.openconfig_rib_bgp_types'
        ),
    },
    'Prefer_ExternalIdentity' : {
        'meta_info' : _MetaInfoClass('Prefer_ExternalIdentity',
            False, 
            [
            ],
            'openconfig-rib-bgp-types',
            'PREFER_EXTERNAL',
            _yang_ns._namespaces['openconfig-rib-bgp-types'],
        'ydk.models.openconfig.openconfig_rib_bgp_types'
        ),
    },
}
