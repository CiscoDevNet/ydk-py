


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'Implementation_Status_TypeIdentity' : {
        'meta_info' : _MetaInfoClass('Implementation_Status_TypeIdentity',
            False, 
            [
            ],
            'openconfig-catalog-types',
            'IMPLEMENTATION_STATUS_TYPE',
            _yang_ns._namespaces['openconfig-catalog-types'],
        'ydk.models.ietf.openconfig_catalog_types'
        ),
    },
    'Module_Status_TypeIdentity' : {
        'meta_info' : _MetaInfoClass('Module_Status_TypeIdentity',
            False, 
            [
            ],
            'openconfig-catalog-types',
            'MODULE_STATUS_TYPE',
            _yang_ns._namespaces['openconfig-catalog-types'],
        'ydk.models.ietf.openconfig_catalog_types'
        ),
    },
    'Module_Category_BaseIdentity' : {
        'meta_info' : _MetaInfoClass('Module_Category_BaseIdentity',
            False, 
            [
            ],
            'openconfig-catalog-types',
            'MODULE_CATEGORY_BASE',
            _yang_ns._namespaces['openconfig-catalog-types'],
        'ydk.models.ietf.openconfig_catalog_types'
        ),
    },
    'Catalog_Member_TypeIdentity' : {
        'meta_info' : _MetaInfoClass('Catalog_Member_TypeIdentity',
            False, 
            [
            ],
            'openconfig-catalog-types',
            'CATALOG_MEMBER_TYPE',
            _yang_ns._namespaces['openconfig-catalog-types'],
        'ydk.models.ietf.openconfig_catalog_types'
        ),
    },
    'Module_Subcategory_BaseIdentity' : {
        'meta_info' : _MetaInfoClass('Module_Subcategory_BaseIdentity',
            False, 
            [
            ],
            'openconfig-catalog-types',
            'MODULE_SUBCATEGORY_BASE',
            _yang_ns._namespaces['openconfig-catalog-types'],
        'ydk.models.ietf.openconfig_catalog_types'
        ),
    },
    'Organization_TypeIdentity' : {
        'meta_info' : _MetaInfoClass('Organization_TypeIdentity',
            False, 
            [
            ],
            'openconfig-catalog-types',
            'ORGANIZATION_TYPE',
            _yang_ns._namespaces['openconfig-catalog-types'],
        'ydk.models.ietf.openconfig_catalog_types'
        ),
    },
    'CompleteIdentity' : {
        'meta_info' : _MetaInfoClass('CompleteIdentity',
            False, 
            [
            ],
            'openconfig-catalog-types',
            'COMPLETE',
            _yang_ns._namespaces['openconfig-catalog-types'],
        'ydk.models.ietf.openconfig_catalog_types'
        ),
    },
    'CommercialIdentity' : {
        'meta_info' : _MetaInfoClass('CommercialIdentity',
            False, 
            [
            ],
            'openconfig-catalog-types',
            'COMMERCIAL',
            _yang_ns._namespaces['openconfig-catalog-types'],
        'ydk.models.ietf.openconfig_catalog_types'
        ),
    },
    'PlannedIdentity' : {
        'meta_info' : _MetaInfoClass('PlannedIdentity',
            False, 
            [
            ],
            'openconfig-catalog-types',
            'PLANNED',
            _yang_ns._namespaces['openconfig-catalog-types'],
        'ydk.models.ietf.openconfig_catalog_types'
        ),
    },
    'In_ProgressIdentity' : {
        'meta_info' : _MetaInfoClass('In_ProgressIdentity',
            False, 
            [
            ],
            'openconfig-catalog-types',
            'IN_PROGRESS',
            _yang_ns._namespaces['openconfig-catalog-types'],
        'ydk.models.ietf.openconfig_catalog_types'
        ),
    },
    'ProductionIdentity' : {
        'meta_info' : _MetaInfoClass('ProductionIdentity',
            False, 
            [
            ],
            'openconfig-catalog-types',
            'PRODUCTION',
            _yang_ns._namespaces['openconfig-catalog-types'],
        'ydk.models.ietf.openconfig_catalog_types'
        ),
    },
    'Release_BundleIdentity' : {
        'meta_info' : _MetaInfoClass('Release_BundleIdentity',
            False, 
            [
            ],
            'openconfig-catalog-types',
            'RELEASE_BUNDLE',
            _yang_ns._namespaces['openconfig-catalog-types'],
        'ydk.models.ietf.openconfig_catalog_types'
        ),
    },
    'ModuleIdentity' : {
        'meta_info' : _MetaInfoClass('ModuleIdentity',
            False, 
            [
            ],
            'openconfig-catalog-types',
            'MODULE',
            _yang_ns._namespaces['openconfig-catalog-types'],
        'ydk.models.ietf.openconfig_catalog_types'
        ),
    },
    'StandardsIdentity' : {
        'meta_info' : _MetaInfoClass('StandardsIdentity',
            False, 
            [
            ],
            'openconfig-catalog-types',
            'STANDARDS',
            _yang_ns._namespaces['openconfig-catalog-types'],
        'ydk.models.ietf.openconfig_catalog_types'
        ),
    },
    'IndividualIdentity' : {
        'meta_info' : _MetaInfoClass('IndividualIdentity',
            False, 
            [
            ],
            'openconfig-catalog-types',
            'INDIVIDUAL',
            _yang_ns._namespaces['openconfig-catalog-types'],
        'ydk.models.ietf.openconfig_catalog_types'
        ),
    },
    'Feature_BundleIdentity' : {
        'meta_info' : _MetaInfoClass('Feature_BundleIdentity',
            False, 
            [
            ],
            'openconfig-catalog-types',
            'FEATURE_BUNDLE',
            _yang_ns._namespaces['openconfig-catalog-types'],
        'ydk.models.ietf.openconfig_catalog_types'
        ),
    },
    'Ietf_Model_LayerIdentity' : {
        'meta_info' : _MetaInfoClass('Ietf_Model_LayerIdentity',
            False, 
            [
            ],
            'openconfig-catalog-types',
            'IETF_MODEL_LAYER',
            _yang_ns._namespaces['openconfig-catalog-types'],
        'ydk.models.ietf.openconfig_catalog_types'
        ),
    },
    'Ietf_Network_ElementIdentity' : {
        'meta_info' : _MetaInfoClass('Ietf_Network_ElementIdentity',
            False, 
            [
            ],
            'openconfig-catalog-types',
            'IETF_NETWORK_ELEMENT',
            _yang_ns._namespaces['openconfig-catalog-types'],
        'ydk.models.ietf.openconfig_catalog_types'
        ),
    },
    'PartialIdentity' : {
        'meta_info' : _MetaInfoClass('PartialIdentity',
            False, 
            [
            ],
            'openconfig-catalog-types',
            'PARTIAL',
            _yang_ns._namespaces['openconfig-catalog-types'],
        'ydk.models.ietf.openconfig_catalog_types'
        ),
    },
    'IndustryIdentity' : {
        'meta_info' : _MetaInfoClass('IndustryIdentity',
            False, 
            [
            ],
            'openconfig-catalog-types',
            'INDUSTRY',
            _yang_ns._namespaces['openconfig-catalog-types'],
        'ydk.models.ietf.openconfig_catalog_types'
        ),
    },
    'ExperimentalIdentity' : {
        'meta_info' : _MetaInfoClass('ExperimentalIdentity',
            False, 
            [
            ],
            'openconfig-catalog-types',
            'EXPERIMENTAL',
            _yang_ns._namespaces['openconfig-catalog-types'],
        'ydk.models.ietf.openconfig_catalog_types'
        ),
    },
    'Ietf_Model_TypeIdentity' : {
        'meta_info' : _MetaInfoClass('Ietf_Model_TypeIdentity',
            False, 
            [
            ],
            'openconfig-catalog-types',
            'IETF_MODEL_TYPE',
            _yang_ns._namespaces['openconfig-catalog-types'],
        'ydk.models.ietf.openconfig_catalog_types'
        ),
    },
    'Ietf_Type_StandardIdentity' : {
        'meta_info' : _MetaInfoClass('Ietf_Type_StandardIdentity',
            False, 
            [
            ],
            'openconfig-catalog-types',
            'IETF_TYPE_STANDARD',
            _yang_ns._namespaces['openconfig-catalog-types'],
        'ydk.models.ietf.openconfig_catalog_types'
        ),
    },
    'Ietf_Network_ServiceIdentity' : {
        'meta_info' : _MetaInfoClass('Ietf_Network_ServiceIdentity',
            False, 
            [
            ],
            'openconfig-catalog-types',
            'IETF_NETWORK_SERVICE',
            _yang_ns._namespaces['openconfig-catalog-types'],
        'ydk.models.ietf.openconfig_catalog_types'
        ),
    },
    'Ietf_Type_UserIdentity' : {
        'meta_info' : _MetaInfoClass('Ietf_Type_UserIdentity',
            False, 
            [
            ],
            'openconfig-catalog-types',
            'IETF_TYPE_USER',
            _yang_ns._namespaces['openconfig-catalog-types'],
        'ydk.models.ietf.openconfig_catalog_types'
        ),
    },
    'Ietf_Type_VendorIdentity' : {
        'meta_info' : _MetaInfoClass('Ietf_Type_VendorIdentity',
            False, 
            [
            ],
            'openconfig-catalog-types',
            'IETF_TYPE_VENDOR',
            _yang_ns._namespaces['openconfig-catalog-types'],
        'ydk.models.ietf.openconfig_catalog_types'
        ),
    },
}
