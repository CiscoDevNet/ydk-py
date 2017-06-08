


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'Organizations.Organization.Modules.Module.Classification' : {
        'meta_info' : _MetaInfoClass('Organizations.Organization.Modules.Module.Classification',
            False, 
            [
            _MetaInfoClassMember('category', REFERENCE_IDENTITY_CLASS, 'Module_Category_BaseIdentity' , 'ydk.models.ietf.openconfig_catalog_types', 'Module_Category_BaseIdentity', 
                [], [], 
                '''                Categorization of the module based on identities defined
                or used by the publishing organizations.
                ''',
                'category',
                'openconfig-module-catalog', False),
            _MetaInfoClassMember('deployment-status', REFERENCE_IDENTITY_CLASS, 'Module_Status_TypeIdentity' , 'ydk.models.ietf.openconfig_catalog_types', 'Module_Status_TypeIdentity', 
                [], [], 
                '''                Deployment status of the module -- experimental,
                standards-track, production, etc.
                ''',
                'deployment_status',
                'openconfig-module-catalog', False),
            _MetaInfoClassMember('subcategory', REFERENCE_IDENTITY_CLASS, 'Module_Subcategory_BaseIdentity' , 'ydk.models.ietf.openconfig_catalog_types', 'Module_Subcategory_BaseIdentity', 
                [], [], 
                '''                Sub-categorization of the module based on identities
                defined or used by the publishing organizations.
                ''',
                'subcategory',
                'openconfig-module-catalog', False),
            ],
            'openconfig-module-catalog',
            'classification',
            _yang_ns._namespaces['openconfig-module-catalog'],
        'ydk.models.ietf.openconfig_module_catalog'
        ),
    },
    'Organizations.Organization.Modules.Module.Dependencies' : {
        'meta_info' : _MetaInfoClass('Organizations.Organization.Modules.Module.Dependencies',
            False, 
            [
            _MetaInfoClassMember('required-module', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                List of references to modules that are imported by the
                current module.  This list should reflect all of the 'import'
                statements in the module.
                ''',
                'required_module',
                'openconfig-module-catalog', False),
            ],
            'openconfig-module-catalog',
            'dependencies',
            _yang_ns._namespaces['openconfig-module-catalog'],
        'ydk.models.ietf.openconfig_module_catalog'
        ),
    },
    'Organizations.Organization.Modules.Module.Access' : {
        'meta_info' : _MetaInfoClass('Organizations.Organization.Modules.Module.Access',
            False, 
            [
            _MetaInfoClassMember('md5-hash', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Optional MD5 hash of the module file.  If specified, the
                hash may be used by users to validate data integrity
                ''',
                'md5_hash',
                'openconfig-module-catalog', False),
            _MetaInfoClassMember('uri', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                URI where module can be downloaded.  Modules may be
                made available from the catalog maintainer, or directly
                from the publisher
                ''',
                'uri',
                'openconfig-module-catalog', False),
            ],
            'openconfig-module-catalog',
            'access',
            _yang_ns._namespaces['openconfig-module-catalog'],
        'ydk.models.ietf.openconfig_module_catalog'
        ),
    },
    'Organizations.Organization.Modules.Module.Submodules.Submodule.Access' : {
        'meta_info' : _MetaInfoClass('Organizations.Organization.Modules.Module.Submodules.Submodule.Access',
            False, 
            [
            _MetaInfoClassMember('md5-hash', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Optional MD5 hash of the module file.  If specified, the
                hash may be used by users to validate data integrity
                ''',
                'md5_hash',
                'openconfig-module-catalog', False),
            _MetaInfoClassMember('uri', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                URI where module can be downloaded.  Modules may be
                made available from the catalog maintainer, or directly
                from the publisher
                ''',
                'uri',
                'openconfig-module-catalog', False),
            ],
            'openconfig-module-catalog',
            'access',
            _yang_ns._namespaces['openconfig-module-catalog'],
        'ydk.models.ietf.openconfig_module_catalog'
        ),
    },
    'Organizations.Organization.Modules.Module.Submodules.Submodule' : {
        'meta_info' : _MetaInfoClass('Organizations.Organization.Modules.Module.Submodules.Submodule',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the submodule as indicated by its top-level
                'submodule' statement
                ''',
                'name',
                'openconfig-module-catalog', True),
            _MetaInfoClassMember('access', REFERENCE_CLASS, 'Access' , 'ydk.models.ietf.openconfig_module_catalog', 'Organizations.Organization.Modules.Module.Submodules.Submodule.Access', 
                [], [], 
                '''                Container for data pertaining to retrieval and usage of the
                module
                ''',
                'access',
                'openconfig-module-catalog', False),
            ],
            'openconfig-module-catalog',
            'submodule',
            _yang_ns._namespaces['openconfig-module-catalog'],
        'ydk.models.ietf.openconfig_module_catalog'
        ),
    },
    'Organizations.Organization.Modules.Module.Submodules' : {
        'meta_info' : _MetaInfoClass('Organizations.Organization.Modules.Module.Submodules',
            False, 
            [
            _MetaInfoClassMember('submodule', REFERENCE_LIST, 'Submodule' , 'ydk.models.ietf.openconfig_module_catalog', 'Organizations.Organization.Modules.Module.Submodules.Submodule', 
                [], [], 
                '''                List of submodules included by a module.  All submodules
                specified by 'include' statements in the module should be
                included in this list.
                ''',
                'submodule',
                'openconfig-module-catalog', False),
            ],
            'openconfig-module-catalog',
            'submodules',
            _yang_ns._namespaces['openconfig-module-catalog'],
        'ydk.models.ietf.openconfig_module_catalog'
        ),
    },
    'Organizations.Organization.Modules.Module' : {
        'meta_info' : _MetaInfoClass('Organizations.Organization.Modules.Module',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the module or bundle.  For modules, this
                should reflect the 'module' or 'submodule'
                statement in the YANG module file.
                
                For bundles, this is the canonical name for the overall
                bundle of modules which is to be released together.
                This name should be consistent over multiple
                releases
                ''',
                'name',
                'openconfig-module-catalog', True),
            _MetaInfoClassMember('version', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                For individual modules, this is the version number, e.g.,
                a semantic version.  The version may be the same as the date
                indicated in the module revision statement.
                
                For bundles, this is a semantic version number for the
                overall bundle. This version is to be defined as per the
                approach specified in the OpenConfig semantic version
                guidance - and is of the form x.y.z, where x is the major
                version, y is the minor version, and z is the patch level
                ''',
                'version',
                'openconfig-module-catalog', True),
            _MetaInfoClassMember('access', REFERENCE_CLASS, 'Access' , 'ydk.models.ietf.openconfig_module_catalog', 'Organizations.Organization.Modules.Module.Access', 
                [], [], 
                '''                Container for data pertaining to retrieval and usage of the
                module
                ''',
                'access',
                'openconfig-module-catalog', False),
            _MetaInfoClassMember('classification', REFERENCE_CLASS, 'Classification' , 'ydk.models.ietf.openconfig_module_catalog', 'Organizations.Organization.Modules.Module.Classification', 
                [], [], 
                '''                Container for data describing the module's classification
                ''',
                'classification',
                'openconfig-module-catalog', False),
            _MetaInfoClassMember('dependencies', REFERENCE_CLASS, 'Dependencies' , 'ydk.models.ietf.openconfig_module_catalog', 'Organizations.Organization.Modules.Module.Dependencies', 
                [], [], 
                '''                Data about dependencies of the module
                ''',
                'dependencies',
                'openconfig-module-catalog', False),
            _MetaInfoClassMember('namespace', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Published namespace of module, i.e., defined by the
                'namespace' 
                ''',
                'namespace',
                'openconfig-module-catalog', False),
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Published prefix of the module
                ''',
                'prefix',
                'openconfig-module-catalog', False),
            _MetaInfoClassMember('revision', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Date in the revision statement of the module
                ''',
                'revision',
                'openconfig-module-catalog', False),
            _MetaInfoClassMember('submodules', REFERENCE_CLASS, 'Submodules' , 'ydk.models.ietf.openconfig_module_catalog', 'Organizations.Organization.Modules.Module.Submodules', 
                [], [], 
                '''                Data for the submodules belonging to a submodule. If the
                module does not have any submodules, this container
                should be empty.
                ''',
                'submodules',
                'openconfig-module-catalog', False),
            _MetaInfoClassMember('summary', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Summary description of the module
                ''',
                'summary',
                'openconfig-module-catalog', False),
            ],
            'openconfig-module-catalog',
            'module',
            _yang_ns._namespaces['openconfig-module-catalog'],
        'ydk.models.ietf.openconfig_module_catalog'
        ),
    },
    'Organizations.Organization.Modules' : {
        'meta_info' : _MetaInfoClass('Organizations.Organization.Modules',
            False, 
            [
            _MetaInfoClassMember('module', REFERENCE_LIST, 'Module' , 'ydk.models.ietf.openconfig_module_catalog', 'Organizations.Organization.Modules.Module', 
                [], [], 
                '''                List of published modules from the organization
                ''',
                'module',
                'openconfig-module-catalog', False),
            ],
            'openconfig-module-catalog',
            'modules',
            _yang_ns._namespaces['openconfig-module-catalog'],
        'ydk.models.ietf.openconfig_module_catalog'
        ),
    },
    'Organizations.Organization.ReleaseBundles.ReleaseBundle.Members.Member' : {
        'meta_info' : _MetaInfoClass('Organizations.Organization.ReleaseBundles.ReleaseBundle.Members.Member',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Identifier for the bundle member
                ''',
                'id',
                'openconfig-module-catalog', True),
            _MetaInfoClassMember('compatible-versions', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                A list of semantic version specification of the versions
                of the specified module or release bundle which are
                compatible when building this version of the bundle.
                
                Version specifications may be added when changes are made
                to a module within a bundle, and this does not affect the
                interaction between it and other modules. It is expected
                that backwards compatible changes to an individual module or
                member bundle do not affect the compatibility of that
                with other members, and hence wildcard matches are allowed
                within this list.
                ''',
                'compatible_versions',
                'openconfig-module-catalog', False),
            _MetaInfoClassMember('module', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the module set which is included in this bundle -
                for example, 'openconfig-bgp'
                ''',
                'module',
                'openconfig-module-catalog', False),
            _MetaInfoClassMember('publisher', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reference to the name of the publishing organization
                ''',
                'publisher',
                'openconfig-module-catalog', False),
            _MetaInfoClassMember('release-bundle', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the module set which is included in this bundle -
                for example, 'openconfig-bgp'
                ''',
                'release_bundle',
                'openconfig-module-catalog', False),
            _MetaInfoClassMember('type', REFERENCE_IDENTITY_CLASS, 'Catalog_Member_TypeIdentity' , 'ydk.models.ietf.openconfig_catalog_types', 'Catalog_Member_TypeIdentity', 
                [], [], 
                '''                The type of member that is to be included within the
                release bundle. Release bundles may include modules and
                other release bundles.  Both member modules and member
                bundles should specify the list of compatible versions.
                ''',
                'type',
                'openconfig-module-catalog', False),
            ],
            'openconfig-module-catalog',
            'member',
            _yang_ns._namespaces['openconfig-module-catalog'],
        'ydk.models.ietf.openconfig_module_catalog'
        ),
    },
    'Organizations.Organization.ReleaseBundles.ReleaseBundle.Members' : {
        'meta_info' : _MetaInfoClass('Organizations.Organization.ReleaseBundles.ReleaseBundle.Members',
            False, 
            [
            _MetaInfoClassMember('member', REFERENCE_LIST, 'Member' , 'ydk.models.ietf.openconfig_module_catalog', 'Organizations.Organization.ReleaseBundles.ReleaseBundle.Members.Member', 
                [], [], 
                '''                A set of modules or bundles which are part of the bundle
                of models. For example, if 'ietf-yang-types' were to be
                specified within the bundle, then this would refer to the
                individual entry within the module catalogue. If the type
                of the entry is set to bundle, then for example,
                openconfig-bgp could be referenced - which itself consists
                of separate modules.
                ''',
                'member',
                'openconfig-module-catalog', False),
            ],
            'openconfig-module-catalog',
            'members',
            _yang_ns._namespaces['openconfig-module-catalog'],
        'ydk.models.ietf.openconfig_module_catalog'
        ),
    },
    'Organizations.Organization.ReleaseBundles.ReleaseBundle' : {
        'meta_info' : _MetaInfoClass('Organizations.Organization.ReleaseBundles.ReleaseBundle',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the module or bundle.  For modules, this
                should reflect the 'module' or 'submodule'
                statement in the YANG module file.
                
                For bundles, this is the canonical name for the overall
                bundle of modules which is to be released together.
                This name should be consistent over multiple
                releases
                ''',
                'name',
                'openconfig-module-catalog', True),
            _MetaInfoClassMember('version', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                For individual modules, this is the version number, e.g.,
                a semantic version.  The version may be the same as the date
                indicated in the module revision statement.
                
                For bundles, this is a semantic version number for the
                overall bundle. This version is to be defined as per the
                approach specified in the OpenConfig semantic version
                guidance - and is of the form x.y.z, where x is the major
                version, y is the minor version, and z is the patch level
                ''',
                'version',
                'openconfig-module-catalog', True),
            _MetaInfoClassMember('members', REFERENCE_CLASS, 'Members' , 'ydk.models.ietf.openconfig_module_catalog', 'Organizations.Organization.ReleaseBundles.ReleaseBundle.Members', 
                [], [], 
                '''                List of bundle members which make up this release bundle. A
                member is defined as an individual YANG module specified
                in the YANG catalogue, or another release
                bundle which can be used to group multiple YANG
                models together.
                ''',
                'members',
                'openconfig-module-catalog', False),
            ],
            'openconfig-module-catalog',
            'release-bundle',
            _yang_ns._namespaces['openconfig-module-catalog'],
        'ydk.models.ietf.openconfig_module_catalog'
        ),
    },
    'Organizations.Organization.ReleaseBundles' : {
        'meta_info' : _MetaInfoClass('Organizations.Organization.ReleaseBundles',
            False, 
            [
            _MetaInfoClassMember('release-bundle', REFERENCE_LIST, 'ReleaseBundle' , 'ydk.models.ietf.openconfig_module_catalog', 'Organizations.Organization.ReleaseBundles.ReleaseBundle', 
                [], [], 
                '''                List of release bundles - sets of modules and/or
                bundles which are interoperable
                ''',
                'release_bundle',
                'openconfig-module-catalog', False),
            ],
            'openconfig-module-catalog',
            'release-bundles',
            _yang_ns._namespaces['openconfig-module-catalog'],
        'ydk.models.ietf.openconfig_module_catalog'
        ),
    },
    'Organizations.Organization.FeatureBundles.FeatureBundle.ReleaseBundle' : {
        'meta_info' : _MetaInfoClass('Organizations.Organization.FeatureBundles.FeatureBundle.ReleaseBundle',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the module set which is included in this bundle -
                for example, 'openconfig-bgp'
                ''',
                'name',
                'openconfig-module-catalog', False),
            _MetaInfoClassMember('publisher', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reference to the name of the publishing organization
                ''',
                'publisher',
                'openconfig-module-catalog', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Version of the referenced release bundle
                ''',
                'version',
                'openconfig-module-catalog', False),
            ],
            'openconfig-module-catalog',
            'release-bundle',
            _yang_ns._namespaces['openconfig-module-catalog'],
        'ydk.models.ietf.openconfig_module_catalog'
        ),
    },
    'Organizations.Organization.FeatureBundles.FeatureBundle.FeatureBundles_.FeatureBundle_' : {
        'meta_info' : _MetaInfoClass('Organizations.Organization.FeatureBundles.FeatureBundle.FeatureBundles_.FeatureBundle_',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the referenced feature bundle
                ''',
                'name',
                'openconfig-module-catalog', True),
            _MetaInfoClassMember('publisher', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Publisher of the referenced feature bundle
                ''',
                'publisher',
                'openconfig-module-catalog', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Version of the referenced feature bundle
                ''',
                'version',
                'openconfig-module-catalog', False),
            ],
            'openconfig-module-catalog',
            'feature-bundle',
            _yang_ns._namespaces['openconfig-module-catalog'],
        'ydk.models.ietf.openconfig_module_catalog'
        ),
    },
    'Organizations.Organization.FeatureBundles.FeatureBundle.FeatureBundles_' : {
        'meta_info' : _MetaInfoClass('Organizations.Organization.FeatureBundles.FeatureBundle.FeatureBundles_',
            False, 
            [
            _MetaInfoClassMember('feature-bundle', REFERENCE_LIST, 'FeatureBundle_' , 'ydk.models.ietf.openconfig_module_catalog', 'Organizations.Organization.FeatureBundles.FeatureBundle.FeatureBundles_.FeatureBundle_', 
                [], [], 
                '''                The list of feature bundles included in the current
                feature bundle.
                ''',
                'feature_bundle',
                'openconfig-module-catalog', False),
            ],
            'openconfig-module-catalog',
            'feature-bundles',
            _yang_ns._namespaces['openconfig-module-catalog'],
        'ydk.models.ietf.openconfig_module_catalog'
        ),
    },
    'Organizations.Organization.FeatureBundles.FeatureBundle' : {
        'meta_info' : _MetaInfoClass('Organizations.Organization.FeatureBundles.FeatureBundle',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the module or bundle.  For modules, this
                should reflect the 'module' or 'submodule'
                statement in the YANG module file.
                
                For bundles, this is the canonical name for the overall
                bundle of modules which is to be released together.
                This name should be consistent over multiple
                releases
                ''',
                'name',
                'openconfig-module-catalog', True),
            _MetaInfoClassMember('version', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                For individual modules, this is the version number, e.g.,
                a semantic version.  The version may be the same as the date
                indicated in the module revision statement.
                
                For bundles, this is a semantic version number for the
                overall bundle. This version is to be defined as per the
                approach specified in the OpenConfig semantic version
                guidance - and is of the form x.y.z, where x is the major
                version, y is the minor version, and z is the patch level
                ''',
                'version',
                'openconfig-module-catalog', True),
            _MetaInfoClassMember('feature-bundles', REFERENCE_CLASS, 'FeatureBundles_' , 'ydk.models.ietf.openconfig_module_catalog', 'Organizations.Organization.FeatureBundles.FeatureBundle.FeatureBundles_', 
                [], [], 
                '''                Enclosing container for the list of included feature
                bundles.  Feature bundles may be composed from other
                smaller feature units
                ''',
                'feature_bundles',
                'openconfig-module-catalog', False),
            _MetaInfoClassMember('path', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                The list of schema paths included in the feature.  The
                paths specify subtrees, i.e., all data underneath the
                specified path are included in the feature.
                ''',
                'path',
                'openconfig-module-catalog', False),
            _MetaInfoClassMember('release-bundle', REFERENCE_CLASS, 'ReleaseBundle' , 'ydk.models.ietf.openconfig_module_catalog', 'Organizations.Organization.FeatureBundles.FeatureBundle.ReleaseBundle', 
                [], [], 
                '''                Data to identify the release bundle from which the feature
                paths should be specified.  If the feature crosses
                release bundles, a new release bundle should be
                created to support the feature bundle.
                ''',
                'release_bundle',
                'openconfig-module-catalog', False),
            ],
            'openconfig-module-catalog',
            'feature-bundle',
            _yang_ns._namespaces['openconfig-module-catalog'],
        'ydk.models.ietf.openconfig_module_catalog'
        ),
    },
    'Organizations.Organization.FeatureBundles' : {
        'meta_info' : _MetaInfoClass('Organizations.Organization.FeatureBundles',
            False, 
            [
            _MetaInfoClassMember('feature-bundle', REFERENCE_LIST, 'FeatureBundle' , 'ydk.models.ietf.openconfig_module_catalog', 'Organizations.Organization.FeatureBundles.FeatureBundle', 
                [], [], 
                '''                List of feature bundles
                ''',
                'feature_bundle',
                'openconfig-module-catalog', False),
            ],
            'openconfig-module-catalog',
            'feature-bundles',
            _yang_ns._namespaces['openconfig-module-catalog'],
        'ydk.models.ietf.openconfig_module_catalog'
        ),
    },
    'Organizations.Organization.Implementations.Implementation.FeatureBundles.FeatureBundle' : {
        'meta_info' : _MetaInfoClass('Organizations.Organization.Implementations.Implementation.FeatureBundles.FeatureBundle',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the referenced feature bundle
                ''',
                'name',
                'openconfig-module-catalog', True),
            _MetaInfoClassMember('version', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Version of the referenced feature bundle
                ''',
                'version',
                'openconfig-module-catalog', True),
            _MetaInfoClassMember('publisher', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Publisher of the referenced feature bundle
                ''',
                'publisher',
                'openconfig-module-catalog', False),
            ],
            'openconfig-module-catalog',
            'feature-bundle',
            _yang_ns._namespaces['openconfig-module-catalog'],
        'ydk.models.ietf.openconfig_module_catalog'
        ),
    },
    'Organizations.Organization.Implementations.Implementation.FeatureBundles' : {
        'meta_info' : _MetaInfoClass('Organizations.Organization.Implementations.Implementation.FeatureBundles',
            False, 
            [
            _MetaInfoClassMember('feature-bundle', REFERENCE_LIST, 'FeatureBundle' , 'ydk.models.ietf.openconfig_module_catalog', 'Organizations.Organization.Implementations.Implementation.FeatureBundles.FeatureBundle', 
                [], [], 
                '''                List of feature bundles supported by the implementation
                ''',
                'feature_bundle',
                'openconfig-module-catalog', False),
            ],
            'openconfig-module-catalog',
            'feature-bundles',
            _yang_ns._namespaces['openconfig-module-catalog'],
        'ydk.models.ietf.openconfig_module_catalog'
        ),
    },
    'Organizations.Organization.Implementations.Implementation' : {
        'meta_info' : _MetaInfoClass('Organizations.Organization.Implementations.Implementation',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                An identifier for the implementation, provided by the
                implementor.  This id should uniquely identify a specific
                implementation of the module, e.g., based on the vendor,
                platform, and platform version.
                ''',
                'id',
                'openconfig-module-catalog', True),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A text summary of important information about the
                implementation
                ''',
                'description',
                'openconfig-module-catalog', False),
            _MetaInfoClassMember('feature-bundles', REFERENCE_CLASS, 'FeatureBundles' , 'ydk.models.ietf.openconfig_module_catalog', 'Organizations.Organization.Implementations.Implementation.FeatureBundles', 
                [], [], 
                '''                Enclosing container for the list of feature bundles
                ''',
                'feature_bundles',
                'openconfig-module-catalog', False),
            _MetaInfoClassMember('platform', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the platform on which the implementation
                is available -- this could be the model name of a network
                device, a server OS, etc.
                ''',
                'platform',
                'openconfig-module-catalog', False),
            _MetaInfoClassMember('platform-version', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Implementor-defined version name or number of the
                module implementation, corresponding to the platform.
                This could be the firmware version of a network device
                such as a router, OS version, or other server platform
                version.
                ''',
                'platform_version',
                'openconfig-module-catalog', False),
            _MetaInfoClassMember('reference', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                A URI (preferred) or text reference to more detailed
                information about the implementation.
                ''',
                'reference',
                'openconfig-module-catalog', False, [
                    _MetaInfoClassMember('reference', ATTRIBUTE, 'str' , None, None, 
                        [], [], 
                        '''                        A URI (preferred) or text reference to more detailed
                        information about the implementation.
                        ''',
                        'reference',
                        'openconfig-module-catalog', False),
                    _MetaInfoClassMember('reference', ATTRIBUTE, 'str' , None, None, 
                        [], [], 
                        '''                        A URI (preferred) or text reference to more detailed
                        information about the implementation.
                        ''',
                        'reference',
                        'openconfig-module-catalog', False),
                ]),
            _MetaInfoClassMember('status', REFERENCE_IDENTITY_CLASS, 'Implementation_Status_TypeIdentity' , 'ydk.models.ietf.openconfig_catalog_types', 'Implementation_Status_TypeIdentity', 
                [], [], 
                '''                Indicates the status of the implementation, e.g.,
                complete, partial, in-progress, etc.  Implementors
                may define additional values for the base identity
                ''',
                'status',
                'openconfig-module-catalog', False),
            ],
            'openconfig-module-catalog',
            'implementation',
            _yang_ns._namespaces['openconfig-module-catalog'],
        'ydk.models.ietf.openconfig_module_catalog'
        ),
    },
    'Organizations.Organization.Implementations' : {
        'meta_info' : _MetaInfoClass('Organizations.Organization.Implementations',
            False, 
            [
            _MetaInfoClassMember('implementation', REFERENCE_LIST, 'Implementation' , 'ydk.models.ietf.openconfig_module_catalog', 'Organizations.Organization.Implementations.Implementation', 
                [], [], 
                '''                List of available implementations, keyed by an identifier
                provided by either the implementor or the module
                maintainer.  Such a key avoids needing a complex composite
                key to uniquely identify an implementation.
                ''',
                'implementation',
                'openconfig-module-catalog', False),
            ],
            'openconfig-module-catalog',
            'implementations',
            _yang_ns._namespaces['openconfig-module-catalog'],
        'ydk.models.ietf.openconfig_module_catalog'
        ),
    },
    'Organizations.Organization' : {
        'meta_info' : _MetaInfoClass('Organizations.Organization',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the maintaining organization -- the name should be
                supplied in the official format used by the organization.
                Standards Body examples:
                 IETF, IEEE, MEF, ONF, etc.
                Commercial entity examples:
                 AT&T, Facebook, <Vendor>
                Name of industry forum examples:
                 OpenConfig, OpenDaylight, ON.Lab
                ''',
                'name',
                'openconfig-module-catalog', True),
            _MetaInfoClassMember('contact', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Contact information for the publishing organization (web
                site, email address, etc.)
                ''',
                'contact',
                'openconfig-module-catalog', False),
            _MetaInfoClassMember('feature-bundles', REFERENCE_CLASS, 'FeatureBundles' , 'ydk.models.ietf.openconfig_module_catalog', 'Organizations.Organization.FeatureBundles', 
                [], [], 
                '''                Enclosing container for the list of feature bundles
                ''',
                'feature_bundles',
                'openconfig-module-catalog', False),
            _MetaInfoClassMember('implementations', REFERENCE_CLASS, 'Implementations' , 'ydk.models.ietf.openconfig_module_catalog', 'Organizations.Organization.Implementations', 
                [], [], 
                '''                Container for module implementation information
                ''',
                'implementations',
                'openconfig-module-catalog', False),
            _MetaInfoClassMember('modules', REFERENCE_CLASS, 'Modules' , 'ydk.models.ietf.openconfig_module_catalog', 'Organizations.Organization.Modules', 
                [], [], 
                '''                Modules published by this organization
                ''',
                'modules',
                'openconfig-module-catalog', False),
            _MetaInfoClassMember('release-bundles', REFERENCE_CLASS, 'ReleaseBundles' , 'ydk.models.ietf.openconfig_module_catalog', 'Organizations.Organization.ReleaseBundles', 
                [], [], 
                '''                List of release bundles
                ''',
                'release_bundles',
                'openconfig-module-catalog', False),
            _MetaInfoClassMember('type', REFERENCE_IDENTITY_CLASS, 'Organization_TypeIdentity' , 'ydk.models.ietf.openconfig_catalog_types', 'Organization_TypeIdentity', 
                [], [], 
                '''                Type of the publishing organization
                ''',
                'type',
                'openconfig-module-catalog', False),
            ],
            'openconfig-module-catalog',
            'organization',
            _yang_ns._namespaces['openconfig-module-catalog'],
        'ydk.models.ietf.openconfig_module_catalog'
        ),
    },
    'Organizations' : {
        'meta_info' : _MetaInfoClass('Organizations',
            False, 
            [
            _MetaInfoClassMember('organization', REFERENCE_LIST, 'Organization' , 'ydk.models.ietf.openconfig_module_catalog', 'Organizations.Organization', 
                [], [], 
                '''                List of organizations publishing YANG modules or
                module bundles
                ''',
                'organization',
                'openconfig-module-catalog', False),
            ],
            'openconfig-module-catalog',
            'organizations',
            _yang_ns._namespaces['openconfig-module-catalog'],
        'ydk.models.ietf.openconfig_module_catalog'
        ),
    },
}
_meta_table['Organizations.Organization.Modules.Module.Submodules.Submodule.Access']['meta_info'].parent =_meta_table['Organizations.Organization.Modules.Module.Submodules.Submodule']['meta_info']
_meta_table['Organizations.Organization.Modules.Module.Submodules.Submodule']['meta_info'].parent =_meta_table['Organizations.Organization.Modules.Module.Submodules']['meta_info']
_meta_table['Organizations.Organization.Modules.Module.Classification']['meta_info'].parent =_meta_table['Organizations.Organization.Modules.Module']['meta_info']
_meta_table['Organizations.Organization.Modules.Module.Dependencies']['meta_info'].parent =_meta_table['Organizations.Organization.Modules.Module']['meta_info']
_meta_table['Organizations.Organization.Modules.Module.Access']['meta_info'].parent =_meta_table['Organizations.Organization.Modules.Module']['meta_info']
_meta_table['Organizations.Organization.Modules.Module.Submodules']['meta_info'].parent =_meta_table['Organizations.Organization.Modules.Module']['meta_info']
_meta_table['Organizations.Organization.Modules.Module']['meta_info'].parent =_meta_table['Organizations.Organization.Modules']['meta_info']
_meta_table['Organizations.Organization.ReleaseBundles.ReleaseBundle.Members.Member']['meta_info'].parent =_meta_table['Organizations.Organization.ReleaseBundles.ReleaseBundle.Members']['meta_info']
_meta_table['Organizations.Organization.ReleaseBundles.ReleaseBundle.Members']['meta_info'].parent =_meta_table['Organizations.Organization.ReleaseBundles.ReleaseBundle']['meta_info']
_meta_table['Organizations.Organization.ReleaseBundles.ReleaseBundle']['meta_info'].parent =_meta_table['Organizations.Organization.ReleaseBundles']['meta_info']
_meta_table['Organizations.Organization.FeatureBundles.FeatureBundle.FeatureBundles_.FeatureBundle_']['meta_info'].parent =_meta_table['Organizations.Organization.FeatureBundles.FeatureBundle.FeatureBundles_']['meta_info']
_meta_table['Organizations.Organization.FeatureBundles.FeatureBundle.ReleaseBundle']['meta_info'].parent =_meta_table['Organizations.Organization.FeatureBundles.FeatureBundle']['meta_info']
_meta_table['Organizations.Organization.FeatureBundles.FeatureBundle.FeatureBundles_']['meta_info'].parent =_meta_table['Organizations.Organization.FeatureBundles.FeatureBundle']['meta_info']
_meta_table['Organizations.Organization.FeatureBundles.FeatureBundle']['meta_info'].parent =_meta_table['Organizations.Organization.FeatureBundles']['meta_info']
_meta_table['Organizations.Organization.Implementations.Implementation.FeatureBundles.FeatureBundle']['meta_info'].parent =_meta_table['Organizations.Organization.Implementations.Implementation.FeatureBundles']['meta_info']
_meta_table['Organizations.Organization.Implementations.Implementation.FeatureBundles']['meta_info'].parent =_meta_table['Organizations.Organization.Implementations.Implementation']['meta_info']
_meta_table['Organizations.Organization.Implementations.Implementation']['meta_info'].parent =_meta_table['Organizations.Organization.Implementations']['meta_info']
_meta_table['Organizations.Organization.Modules']['meta_info'].parent =_meta_table['Organizations.Organization']['meta_info']
_meta_table['Organizations.Organization.ReleaseBundles']['meta_info'].parent =_meta_table['Organizations.Organization']['meta_info']
_meta_table['Organizations.Organization.FeatureBundles']['meta_info'].parent =_meta_table['Organizations.Organization']['meta_info']
_meta_table['Organizations.Organization.Implementations']['meta_info'].parent =_meta_table['Organizations.Organization']['meta_info']
_meta_table['Organizations.Organization']['meta_info'].parent =_meta_table['Organizations']['meta_info']
