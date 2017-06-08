""" openconfig_catalog_types 

This module defines types and identities used by the OpenConfig
YANG module catalog model.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class Implementation_Status_TypeIdentity(object):
    """
    Indications of the status of a module's implementation on a
    device or server
    
    

    """

    _prefix = 'oc-cat-types'
    _revision = '2017-03-08'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _openconfig_catalog_types as meta
        return meta._meta_table['Implementation_Status_TypeIdentity']['meta_info']


class Module_Status_TypeIdentity(object):
    """
    Indicates the deployment status of the module
    
    

    """

    _prefix = 'oc-cat-types'
    _revision = '2017-03-08'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _openconfig_catalog_types as meta
        return meta._meta_table['Module_Status_TypeIdentity']['meta_info']


class Module_Category_BaseIdentity(object):
    """
    Base identity for the module category.  It is expected that
    publishing organizations will define additional derived
    identities to describe their categorization scheme.
    
    

    """

    _prefix = 'oc-cat-types'
    _revision = '2017-03-08'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _openconfig_catalog_types as meta
        return meta._meta_table['Module_Category_BaseIdentity']['meta_info']


class Catalog_Member_TypeIdentity(object):
    """
    Base identity for elements in the catalog
    
    

    """

    _prefix = 'oc-cat-types'
    _revision = '2017-03-08'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _openconfig_catalog_types as meta
        return meta._meta_table['Catalog_Member_TypeIdentity']['meta_info']


class Module_Subcategory_BaseIdentity(object):
    """
    Base identity for the module subcategory.  It is expected that
    publishing organizations will define additional derived
    identities to describe their categorization scheme.
    
    

    """

    _prefix = 'oc-cat-types'
    _revision = '2017-03-08'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _openconfig_catalog_types as meta
        return meta._meta_table['Module_Subcategory_BaseIdentity']['meta_info']


class Organization_TypeIdentity(object):
    """
    Publishing organization type for the set of modules
    
    

    """

    _prefix = 'oc-cat-types'
    _revision = '2017-03-08'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _openconfig_catalog_types as meta
        return meta._meta_table['Organization_TypeIdentity']['meta_info']


class CompleteIdentity(Implementation_Status_TypeIdentity):
    """
    Implementation is complete and fully supports the model
    
    

    """

    _prefix = 'oc-cat-types'
    _revision = '2017-03-08'

    def __init__(self):
        Implementation_Status_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _openconfig_catalog_types as meta
        return meta._meta_table['CompleteIdentity']['meta_info']


class CommercialIdentity(Organization_TypeIdentity):
    """
    Commercial entity, company, etc.
    
    

    """

    _prefix = 'oc-cat-types'
    _revision = '2017-03-08'

    def __init__(self):
        Organization_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _openconfig_catalog_types as meta
        return meta._meta_table['CommercialIdentity']['meta_info']


class PlannedIdentity(Implementation_Status_TypeIdentity):
    """
    Implementation is planned
    
    

    """

    _prefix = 'oc-cat-types'
    _revision = '2017-03-08'

    def __init__(self):
        Implementation_Status_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _openconfig_catalog_types as meta
        return meta._meta_table['PlannedIdentity']['meta_info']


class In_ProgressIdentity(Implementation_Status_TypeIdentity):
    """
    Implementation is in progress
    
    

    """

    _prefix = 'oc-cat-types'
    _revision = '2017-03-08'

    def __init__(self):
        Implementation_Status_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _openconfig_catalog_types as meta
        return meta._meta_table['In_ProgressIdentity']['meta_info']


class ProductionIdentity(Module_Status_TypeIdentity):
    """
    Module is suitable for use in production, or has been
    deployed in production
    
    

    """

    _prefix = 'oc-cat-types'
    _revision = '2017-03-08'

    def __init__(self):
        Module_Status_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _openconfig_catalog_types as meta
        return meta._meta_table['ProductionIdentity']['meta_info']


class Release_BundleIdentity(Catalog_Member_TypeIdentity):
    """
    Release bundle elements in the catalog
    
    

    """

    _prefix = 'oc-cat-types'
    _revision = '2017-03-08'

    def __init__(self):
        Catalog_Member_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _openconfig_catalog_types as meta
        return meta._meta_table['Release_BundleIdentity']['meta_info']


class ModuleIdentity(Catalog_Member_TypeIdentity):
    """
    Module elements in the catalog
    
    

    """

    _prefix = 'oc-cat-types'
    _revision = '2017-03-08'

    def __init__(self):
        Catalog_Member_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _openconfig_catalog_types as meta
        return meta._meta_table['ModuleIdentity']['meta_info']


class StandardsIdentity(Organization_TypeIdentity):
    """
    Standards development organization (SDO) publisher type
    
    

    """

    _prefix = 'oc-cat-types'
    _revision = '2017-03-08'

    def __init__(self):
        Organization_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _openconfig_catalog_types as meta
        return meta._meta_table['StandardsIdentity']['meta_info']


class IndividualIdentity(Organization_TypeIdentity):
    """
    For modules published by an individual
    
    

    """

    _prefix = 'oc-cat-types'
    _revision = '2017-03-08'

    def __init__(self):
        Organization_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _openconfig_catalog_types as meta
        return meta._meta_table['IndividualIdentity']['meta_info']


class Feature_BundleIdentity(Catalog_Member_TypeIdentity):
    """
    Feature bundle elements in the catalog
    
    

    """

    _prefix = 'oc-cat-types'
    _revision = '2017-03-08'

    def __init__(self):
        Catalog_Member_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _openconfig_catalog_types as meta
        return meta._meta_table['Feature_BundleIdentity']['meta_info']


class Ietf_Model_LayerIdentity(Module_Category_BaseIdentity):
    """
    Describes layering of models based on their abstraction
    level as defined by IETF model classification proposals
    
    

    """

    _prefix = 'oc-cat-types'
    _revision = '2017-03-08'

    def __init__(self):
        Module_Category_BaseIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _openconfig_catalog_types as meta
        return meta._meta_table['Ietf_Model_LayerIdentity']['meta_info']


class Ietf_Network_ElementIdentity(Ietf_Model_LayerIdentity):
    """
    Network element\-layer model as defined by IETF classification
    proposal
    
    

    """

    _prefix = 'oc-cat-types'
    _revision = '2017-03-08'

    def __init__(self):
        Ietf_Model_LayerIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _openconfig_catalog_types as meta
        return meta._meta_table['Ietf_Network_ElementIdentity']['meta_info']


class PartialIdentity(Implementation_Status_TypeIdentity):
    """
    Implementation is complete, but only supports the model
    partially
    
    

    """

    _prefix = 'oc-cat-types'
    _revision = '2017-03-08'

    def __init__(self):
        Implementation_Status_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _openconfig_catalog_types as meta
        return meta._meta_table['PartialIdentity']['meta_info']


class IndustryIdentity(Organization_TypeIdentity):
    """
    Industry forum or other industry group
    
    

    """

    _prefix = 'oc-cat-types'
    _revision = '2017-03-08'

    def __init__(self):
        Organization_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _openconfig_catalog_types as meta
        return meta._meta_table['IndustryIdentity']['meta_info']


class ExperimentalIdentity(Module_Status_TypeIdentity):
    """
    Module should be considered experimental, not deployed in
    production settings
    
    

    """

    _prefix = 'oc-cat-types'
    _revision = '2017-03-08'

    def __init__(self):
        Module_Status_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _openconfig_catalog_types as meta
        return meta._meta_table['ExperimentalIdentity']['meta_info']


class Ietf_Model_TypeIdentity(Module_Subcategory_BaseIdentity):
    """
    IETF proposed classification dimension of YANG model types as
    standard YANG models, vendor\-specific, or user\-specific YANG
    models and extensions
    
    

    """

    _prefix = 'oc-cat-types'
    _revision = '2017-03-08'

    def __init__(self):
        Module_Subcategory_BaseIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _openconfig_catalog_types as meta
        return meta._meta_table['Ietf_Model_TypeIdentity']['meta_info']


class Ietf_Type_StandardIdentity(Ietf_Model_TypeIdentity):
    """
    Models published by standards\-defining organizations (SDOs)
    
    

    """

    _prefix = 'oc-cat-types'
    _revision = '2017-03-08'

    def __init__(self):
        Ietf_Model_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _openconfig_catalog_types as meta
        return meta._meta_table['Ietf_Type_StandardIdentity']['meta_info']


class Ietf_Network_ServiceIdentity(Ietf_Model_LayerIdentity):
    """
    Service\-layer model as defined by IETF classification
    proposal
    
    

    """

    _prefix = 'oc-cat-types'
    _revision = '2017-03-08'

    def __init__(self):
        Ietf_Model_LayerIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _openconfig_catalog_types as meta
        return meta._meta_table['Ietf_Network_ServiceIdentity']['meta_info']


class Ietf_Type_UserIdentity(Ietf_Model_TypeIdentity):
    """
    Developed by organizations that operate YANG\-based
    infrastructure including devices and orchestrators.
    The intent of these models is to express the specific needs
    for a certain implementation, above and beyond what is provided
    by vendors
    
    

    """

    _prefix = 'oc-cat-types'
    _revision = '2017-03-08'

    def __init__(self):
        Ietf_Model_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _openconfig_catalog_types as meta
        return meta._meta_table['Ietf_Type_UserIdentity']['meta_info']


class Ietf_Type_VendorIdentity(Ietf_Model_TypeIdentity):
    """
    Developed by organizations (e.g., vendors) with the intent
    to support a specific set of implementations under control of
    that organization
    
    

    """

    _prefix = 'oc-cat-types'
    _revision = '2017-03-08'

    def __init__(self):
        Ietf_Model_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _openconfig_catalog_types as meta
        return meta._meta_table['Ietf_Type_VendorIdentity']['meta_info']


