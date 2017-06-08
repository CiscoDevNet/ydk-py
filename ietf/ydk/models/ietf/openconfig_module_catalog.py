""" openconfig_module_catalog 

This module provides a schema for cataloging and descrbing
YANG models published across various organizations.  The catalog
contains several categories of data\:

\* organizations \-\- entities that publish and/or maintain
 individual YANG modules or groups of modules

\* modules \-\- information regarding individual YANG modules,
 including their versions, dependencies, submodules, and how
 to access them

\* release bundles \-\- groups of modules that are compatible and
 consistent with each other (as determined by the publisher of
 of the bundle).  The release bundle does not necessarily
 correspond to a functional area, e.g., it could the entire
 set of modules published by an organization

\* feature bundles \-\- sets of schema paths across a
 release bundle that provide a specific set of functionality

\* implementations \-\- information about available module and/or
 bundle implementations and their status

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class Organizations(object):
    """
    List of organizations owning modules
    
    .. attribute:: organization
    
    	List of organizations publishing YANG modules or module bundles
    	**type**\: list of    :py:class:`Organization <ydk.models.ietf.openconfig_module_catalog.Organizations.Organization>`
    
    

    """

    _prefix = 'oc-cat'
    _revision = '2017-03-08'

    def __init__(self):
        self.organization = YList()
        self.organization.parent = self
        self.organization.name = 'organization'


    class Organization(object):
        """
        List of organizations publishing YANG modules or
        module bundles
        
        .. attribute:: name  <key>
        
        	Name of the maintaining organization \-\- the name should be supplied in the official format used by the organization. Standards Body examples\:  IETF, IEEE, MEF, ONF, etc. Commercial entity examples\:  AT&T, Facebook, <Vendor> Name of industry forum examples\:  OpenConfig, OpenDaylight, ON.Lab
        	**type**\:  str
        
        .. attribute:: contact
        
        	Contact information for the publishing organization (web site, email address, etc.)
        	**type**\:  str
        
        .. attribute:: feature_bundles
        
        	Enclosing container for the list of feature bundles
        	**type**\:   :py:class:`FeatureBundles <ydk.models.ietf.openconfig_module_catalog.Organizations.Organization.FeatureBundles>`
        
        .. attribute:: implementations
        
        	Container for module implementation information
        	**type**\:   :py:class:`Implementations <ydk.models.ietf.openconfig_module_catalog.Organizations.Organization.Implementations>`
        
        .. attribute:: modules
        
        	Modules published by this organization
        	**type**\:   :py:class:`Modules <ydk.models.ietf.openconfig_module_catalog.Organizations.Organization.Modules>`
        
        .. attribute:: release_bundles
        
        	List of release bundles
        	**type**\:   :py:class:`ReleaseBundles <ydk.models.ietf.openconfig_module_catalog.Organizations.Organization.ReleaseBundles>`
        
        .. attribute:: type
        
        	Type of the publishing organization
        	**type**\:   :py:class:`Organization_TypeIdentity <ydk.models.ietf.openconfig_catalog_types.Organization_TypeIdentity>`
        
        

        """

        _prefix = 'oc-cat'
        _revision = '2017-03-08'

        def __init__(self):
            self.parent = None
            self.name = None
            self.contact = None
            self.feature_bundles = Organizations.Organization.FeatureBundles()
            self.feature_bundles.parent = self
            self.implementations = Organizations.Organization.Implementations()
            self.implementations.parent = self
            self.modules = Organizations.Organization.Modules()
            self.modules.parent = self
            self.release_bundles = Organizations.Organization.ReleaseBundles()
            self.release_bundles.parent = self
            self.type = None


        class Modules(object):
            """
            Modules published by this organization
            
            .. attribute:: module
            
            	List of published modules from the organization
            	**type**\: list of    :py:class:`Module <ydk.models.ietf.openconfig_module_catalog.Organizations.Organization.Modules.Module>`
            
            

            """

            _prefix = 'oc-cat'
            _revision = '2017-03-08'

            def __init__(self):
                self.parent = None
                self.module = YList()
                self.module.parent = self
                self.module.name = 'module'


            class Module(object):
                """
                List of published modules from the organization
                
                .. attribute:: name  <key>
                
                	The name of the module or bundle.  For modules, this should reflect the 'module' or 'submodule' statement in the YANG module file.  For bundles, this is the canonical name for the overall bundle of modules which is to be released together. This name should be consistent over multiple releases
                	**type**\:  str
                
                .. attribute:: version  <key>
                
                	For individual modules, this is the version number, e.g., a semantic version.  The version may be the same as the date indicated in the module revision statement.  For bundles, this is a semantic version number for the overall bundle. This version is to be defined as per the approach specified in the OpenConfig semantic version guidance \- and is of the form x.y.z, where x is the major version, y is the minor version, and z is the patch level
                	**type**\:  str
                
                .. attribute:: access
                
                	Container for data pertaining to retrieval and usage of the module
                	**type**\:   :py:class:`Access <ydk.models.ietf.openconfig_module_catalog.Organizations.Organization.Modules.Module.Access>`
                
                .. attribute:: classification
                
                	Container for data describing the module's classification
                	**type**\:   :py:class:`Classification <ydk.models.ietf.openconfig_module_catalog.Organizations.Organization.Modules.Module.Classification>`
                
                .. attribute:: dependencies
                
                	Data about dependencies of the module
                	**type**\:   :py:class:`Dependencies <ydk.models.ietf.openconfig_module_catalog.Organizations.Organization.Modules.Module.Dependencies>`
                
                .. attribute:: namespace
                
                	Published namespace of module, i.e., defined by the 'namespace' 
                	**type**\:  str
                
                .. attribute:: prefix
                
                	Published prefix of the module
                	**type**\:  str
                
                .. attribute:: revision
                
                	Date in the revision statement of the module
                	**type**\:  str
                
                .. attribute:: submodules
                
                	Data for the submodules belonging to a submodule. If the module does not have any submodules, this container should be empty
                	**type**\:   :py:class:`Submodules <ydk.models.ietf.openconfig_module_catalog.Organizations.Organization.Modules.Module.Submodules>`
                
                .. attribute:: summary
                
                	Summary description of the module
                	**type**\:  str
                
                

                """

                _prefix = 'oc-cat'
                _revision = '2017-03-08'

                def __init__(self):
                    self.parent = None
                    self.name = None
                    self.version = None
                    self.access = Organizations.Organization.Modules.Module.Access()
                    self.access.parent = self
                    self.classification = Organizations.Organization.Modules.Module.Classification()
                    self.classification.parent = self
                    self.dependencies = Organizations.Organization.Modules.Module.Dependencies()
                    self.dependencies.parent = self
                    self.namespace = None
                    self.prefix = None
                    self.revision = None
                    self.submodules = Organizations.Organization.Modules.Module.Submodules()
                    self.submodules.parent = self
                    self.summary = None


                class Classification(object):
                    """
                    Container for data describing the module's classification
                    
                    .. attribute:: category
                    
                    	Categorization of the module based on identities defined or used by the publishing organizations
                    	**type**\:   :py:class:`Module_Category_BaseIdentity <ydk.models.ietf.openconfig_catalog_types.Module_Category_BaseIdentity>`
                    
                    .. attribute:: deployment_status
                    
                    	Deployment status of the module \-\- experimental, standards\-track, production, etc
                    	**type**\:   :py:class:`Module_Status_TypeIdentity <ydk.models.ietf.openconfig_catalog_types.Module_Status_TypeIdentity>`
                    
                    .. attribute:: subcategory
                    
                    	Sub\-categorization of the module based on identities defined or used by the publishing organizations
                    	**type**\:   :py:class:`Module_Subcategory_BaseIdentity <ydk.models.ietf.openconfig_catalog_types.Module_Subcategory_BaseIdentity>`
                    
                    

                    """

                    _prefix = 'oc-cat'
                    _revision = '2017-03-08'

                    def __init__(self):
                        self.parent = None
                        self.category = None
                        self.deployment_status = None
                        self.subcategory = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-module-catalog:classification'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.category is not None:
                            return True

                        if self.deployment_status is not None:
                            return True

                        if self.subcategory is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _openconfig_module_catalog as meta
                        return meta._meta_table['Organizations.Organization.Modules.Module.Classification']['meta_info']


                class Dependencies(object):
                    """
                    Data about dependencies of the module
                    
                    .. attribute:: required_module
                    
                    	List of references to modules that are imported by the current module.  This list should reflect all of the 'import' statements in the module
                    	**type**\:  list of str
                    
                    	**refers to**\:  :py:class:`name <ydk.models.ietf.openconfig_module_catalog.Organizations.Organization.Modules.Module>`
                    
                    

                    """

                    _prefix = 'oc-cat'
                    _revision = '2017-03-08'

                    def __init__(self):
                        self.parent = None
                        self.required_module = YLeafList()
                        self.required_module.parent = self
                        self.required_module.name = 'required_module'

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-module-catalog:dependencies'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.required_module is not None:
                            for child in self.required_module:
                                if child is not None:
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _openconfig_module_catalog as meta
                        return meta._meta_table['Organizations.Organization.Modules.Module.Dependencies']['meta_info']


                class Access(object):
                    """
                    Container for data pertaining to retrieval and usage of the
                    module
                    
                    .. attribute:: md5_hash
                    
                    	Optional MD5 hash of the module file.  If specified, the hash may be used by users to validate data integrity
                    	**type**\:  str
                    
                    .. attribute:: uri
                    
                    	URI where module can be downloaded.  Modules may be made available from the catalog maintainer, or directly from the publisher
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'oc-cat'
                    _revision = '2017-03-08'

                    def __init__(self):
                        self.parent = None
                        self.md5_hash = None
                        self.uri = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-module-catalog:access'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.md5_hash is not None:
                            return True

                        if self.uri is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _openconfig_module_catalog as meta
                        return meta._meta_table['Organizations.Organization.Modules.Module.Access']['meta_info']


                class Submodules(object):
                    """
                    Data for the submodules belonging to a submodule. If the
                    module does not have any submodules, this container
                    should be empty.
                    
                    .. attribute:: submodule
                    
                    	List of submodules included by a module.  All submodules specified by 'include' statements in the module should be included in this list
                    	**type**\: list of    :py:class:`Submodule <ydk.models.ietf.openconfig_module_catalog.Organizations.Organization.Modules.Module.Submodules.Submodule>`
                    
                    

                    """

                    _prefix = 'oc-cat'
                    _revision = '2017-03-08'

                    def __init__(self):
                        self.parent = None
                        self.submodule = YList()
                        self.submodule.parent = self
                        self.submodule.name = 'submodule'


                    class Submodule(object):
                        """
                        List of submodules included by a module.  All submodules
                        specified by 'include' statements in the module should be
                        included in this list.
                        
                        .. attribute:: name  <key>
                        
                        	Name of the submodule as indicated by its top\-level 'submodule' statement
                        	**type**\:  str
                        
                        .. attribute:: access
                        
                        	Container for data pertaining to retrieval and usage of the module
                        	**type**\:   :py:class:`Access <ydk.models.ietf.openconfig_module_catalog.Organizations.Organization.Modules.Module.Submodules.Submodule.Access>`
                        
                        

                        """

                        _prefix = 'oc-cat'
                        _revision = '2017-03-08'

                        def __init__(self):
                            self.parent = None
                            self.name = None
                            self.access = Organizations.Organization.Modules.Module.Submodules.Submodule.Access()
                            self.access.parent = self


                        class Access(object):
                            """
                            Container for data pertaining to retrieval and usage of the
                            module
                            
                            .. attribute:: md5_hash
                            
                            	Optional MD5 hash of the module file.  If specified, the hash may be used by users to validate data integrity
                            	**type**\:  str
                            
                            .. attribute:: uri
                            
                            	URI where module can be downloaded.  Modules may be made available from the catalog maintainer, or directly from the publisher
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'oc-cat'
                            _revision = '2017-03-08'

                            def __init__(self):
                                self.parent = None
                                self.md5_hash = None
                                self.uri = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/openconfig-module-catalog:access'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.md5_hash is not None:
                                    return True

                                if self.uri is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ietf._meta import _openconfig_module_catalog as meta
                                return meta._meta_table['Organizations.Organization.Modules.Module.Submodules.Submodule.Access']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.name is None:
                                raise YPYModelError('Key property name is None')

                            return self.parent._common_path +'/openconfig-module-catalog:submodule[openconfig-module-catalog:name = ' + str(self.name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.name is not None:
                                return True

                            if self.access is not None and self.access._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ietf._meta import _openconfig_module_catalog as meta
                            return meta._meta_table['Organizations.Organization.Modules.Module.Submodules.Submodule']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-module-catalog:submodules'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.submodule is not None:
                            for child_ref in self.submodule:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _openconfig_module_catalog as meta
                        return meta._meta_table['Organizations.Organization.Modules.Module.Submodules']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.name is None:
                        raise YPYModelError('Key property name is None')
                    if self.version is None:
                        raise YPYModelError('Key property version is None')

                    return self.parent._common_path +'/openconfig-module-catalog:module[openconfig-module-catalog:name = ' + str(self.name) + '][openconfig-module-catalog:version = ' + str(self.version) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.name is not None:
                        return True

                    if self.version is not None:
                        return True

                    if self.access is not None and self.access._has_data():
                        return True

                    if self.classification is not None and self.classification._has_data():
                        return True

                    if self.dependencies is not None and self.dependencies._has_data():
                        return True

                    if self.namespace is not None:
                        return True

                    if self.prefix is not None:
                        return True

                    if self.revision is not None:
                        return True

                    if self.submodules is not None and self.submodules._has_data():
                        return True

                    if self.summary is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _openconfig_module_catalog as meta
                    return meta._meta_table['Organizations.Organization.Modules.Module']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/openconfig-module-catalog:modules'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.module is not None:
                    for child_ref in self.module:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _openconfig_module_catalog as meta
                return meta._meta_table['Organizations.Organization.Modules']['meta_info']


        class ReleaseBundles(object):
            """
            List of release bundles
            
            .. attribute:: release_bundle
            
            	List of release bundles \- sets of modules and/or bundles which are interoperable
            	**type**\: list of    :py:class:`ReleaseBundle <ydk.models.ietf.openconfig_module_catalog.Organizations.Organization.ReleaseBundles.ReleaseBundle>`
            
            

            """

            _prefix = 'oc-cat'
            _revision = '2017-03-08'

            def __init__(self):
                self.parent = None
                self.release_bundle = YList()
                self.release_bundle.parent = self
                self.release_bundle.name = 'release_bundle'


            class ReleaseBundle(object):
                """
                List of release bundles \- sets of modules and/or
                bundles which are interoperable
                
                .. attribute:: name  <key>
                
                	The name of the module or bundle.  For modules, this should reflect the 'module' or 'submodule' statement in the YANG module file.  For bundles, this is the canonical name for the overall bundle of modules which is to be released together. This name should be consistent over multiple releases
                	**type**\:  str
                
                .. attribute:: version  <key>
                
                	For individual modules, this is the version number, e.g., a semantic version.  The version may be the same as the date indicated in the module revision statement.  For bundles, this is a semantic version number for the overall bundle. This version is to be defined as per the approach specified in the OpenConfig semantic version guidance \- and is of the form x.y.z, where x is the major version, y is the minor version, and z is the patch level
                	**type**\:  str
                
                .. attribute:: members
                
                	List of bundle members which make up this release bundle. A member is defined as an individual YANG module specified in the YANG catalogue, or another release bundle which can be used to group multiple YANG models together
                	**type**\:   :py:class:`Members <ydk.models.ietf.openconfig_module_catalog.Organizations.Organization.ReleaseBundles.ReleaseBundle.Members>`
                
                

                """

                _prefix = 'oc-cat'
                _revision = '2017-03-08'

                def __init__(self):
                    self.parent = None
                    self.name = None
                    self.version = None
                    self.members = Organizations.Organization.ReleaseBundles.ReleaseBundle.Members()
                    self.members.parent = self


                class Members(object):
                    """
                    List of bundle members which make up this release bundle. A
                    member is defined as an individual YANG module specified
                    in the YANG catalogue, or another release
                    bundle which can be used to group multiple YANG
                    models together.
                    
                    .. attribute:: member
                    
                    	A set of modules or bundles which are part of the bundle of models. For example, if 'ietf\-yang\-types' were to be specified within the bundle, then this would refer to the individual entry within the module catalogue. If the type of the entry is set to bundle, then for example, openconfig\-bgp could be referenced \- which itself consists of separate modules
                    	**type**\: list of    :py:class:`Member <ydk.models.ietf.openconfig_module_catalog.Organizations.Organization.ReleaseBundles.ReleaseBundle.Members.Member>`
                    
                    

                    """

                    _prefix = 'oc-cat'
                    _revision = '2017-03-08'

                    def __init__(self):
                        self.parent = None
                        self.member = YList()
                        self.member.parent = self
                        self.member.name = 'member'


                    class Member(object):
                        """
                        A set of modules or bundles which are part of the bundle
                        of models. For example, if 'ietf\-yang\-types' were to be
                        specified within the bundle, then this would refer to the
                        individual entry within the module catalogue. If the type
                        of the entry is set to bundle, then for example,
                        openconfig\-bgp could be referenced \- which itself consists
                        of separate modules.
                        
                        .. attribute:: id  <key>
                        
                        	Identifier for the bundle member
                        	**type**\:  str
                        
                        .. attribute:: compatible_versions
                        
                        	A list of semantic version specification of the versions of the specified module or release bundle which are compatible when building this version of the bundle.  Version specifications may be added when changes are made to a module within a bundle, and this does not affect the interaction between it and other modules. It is expected that backwards compatible changes to an individual module or member bundle do not affect the compatibility of that with other members, and hence wildcard matches are allowed within this list
                        	**type**\:  list of str
                        
                        .. attribute:: module
                        
                        	Name of the module set which is included in this bundle \- for example, 'openconfig\-bgp'
                        	**type**\:  str
                        
                        	**refers to**\:  :py:class:`name <ydk.models.ietf.openconfig_module_catalog.Organizations.Organization.Modules.Module>`
                        
                        .. attribute:: publisher
                        
                        	Reference to the name of the publishing organization
                        	**type**\:  str
                        
                        	**refers to**\:  :py:class:`name <ydk.models.ietf.openconfig_module_catalog.Organizations.Organization>`
                        
                        .. attribute:: release_bundle
                        
                        	Name of the module set which is included in this bundle \- for example, 'openconfig\-bgp'
                        	**type**\:  str
                        
                        	**refers to**\:  :py:class:`name <ydk.models.ietf.openconfig_module_catalog.Organizations.Organization.ReleaseBundles.ReleaseBundle>`
                        
                        .. attribute:: type
                        
                        	The type of member that is to be included within the release bundle. Release bundles may include modules and other release bundles.  Both member modules and member bundles should specify the list of compatible versions
                        	**type**\:   :py:class:`Catalog_Member_TypeIdentity <ydk.models.ietf.openconfig_catalog_types.Catalog_Member_TypeIdentity>`
                        
                        

                        """

                        _prefix = 'oc-cat'
                        _revision = '2017-03-08'

                        def __init__(self):
                            self.parent = None
                            self.id = None
                            self.compatible_versions = YLeafList()
                            self.compatible_versions.parent = self
                            self.compatible_versions.name = 'compatible_versions'
                            self.module = None
                            self.publisher = None
                            self.release_bundle = None
                            self.type = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.id is None:
                                raise YPYModelError('Key property id is None')

                            return self.parent._common_path +'/openconfig-module-catalog:member[openconfig-module-catalog:id = ' + str(self.id) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.id is not None:
                                return True

                            if self.compatible_versions is not None:
                                for child in self.compatible_versions:
                                    if child is not None:
                                        return True

                            if self.module is not None:
                                return True

                            if self.publisher is not None:
                                return True

                            if self.release_bundle is not None:
                                return True

                            if self.type is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ietf._meta import _openconfig_module_catalog as meta
                            return meta._meta_table['Organizations.Organization.ReleaseBundles.ReleaseBundle.Members.Member']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-module-catalog:members'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.member is not None:
                            for child_ref in self.member:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _openconfig_module_catalog as meta
                        return meta._meta_table['Organizations.Organization.ReleaseBundles.ReleaseBundle.Members']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.name is None:
                        raise YPYModelError('Key property name is None')
                    if self.version is None:
                        raise YPYModelError('Key property version is None')

                    return self.parent._common_path +'/openconfig-module-catalog:release-bundle[openconfig-module-catalog:name = ' + str(self.name) + '][openconfig-module-catalog:version = ' + str(self.version) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.name is not None:
                        return True

                    if self.version is not None:
                        return True

                    if self.members is not None and self.members._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _openconfig_module_catalog as meta
                    return meta._meta_table['Organizations.Organization.ReleaseBundles.ReleaseBundle']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/openconfig-module-catalog:release-bundles'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.release_bundle is not None:
                    for child_ref in self.release_bundle:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _openconfig_module_catalog as meta
                return meta._meta_table['Organizations.Organization.ReleaseBundles']['meta_info']


        class FeatureBundles(object):
            """
            Enclosing container for the list of feature bundles
            
            .. attribute:: feature_bundle
            
            	List of feature bundles
            	**type**\: list of    :py:class:`FeatureBundle <ydk.models.ietf.openconfig_module_catalog.Organizations.Organization.FeatureBundles.FeatureBundle>`
            
            

            """

            _prefix = 'oc-cat'
            _revision = '2017-03-08'

            def __init__(self):
                self.parent = None
                self.feature_bundle = YList()
                self.feature_bundle.parent = self
                self.feature_bundle.name = 'feature_bundle'


            class FeatureBundle(object):
                """
                List of feature bundles
                
                .. attribute:: name  <key>
                
                	The name of the module or bundle.  For modules, this should reflect the 'module' or 'submodule' statement in the YANG module file.  For bundles, this is the canonical name for the overall bundle of modules which is to be released together. This name should be consistent over multiple releases
                	**type**\:  str
                
                .. attribute:: version  <key>
                
                	For individual modules, this is the version number, e.g., a semantic version.  The version may be the same as the date indicated in the module revision statement.  For bundles, this is a semantic version number for the overall bundle. This version is to be defined as per the approach specified in the OpenConfig semantic version guidance \- and is of the form x.y.z, where x is the major version, y is the minor version, and z is the patch level
                	**type**\:  str
                
                .. attribute:: feature_bundles
                
                	Enclosing container for the list of included feature bundles.  Feature bundles may be composed from other smaller feature units
                	**type**\:   :py:class:`FeatureBundles_ <ydk.models.ietf.openconfig_module_catalog.Organizations.Organization.FeatureBundles.FeatureBundle.FeatureBundles_>`
                
                .. attribute:: path
                
                	The list of schema paths included in the feature.  The paths specify subtrees, i.e., all data underneath the specified path are included in the feature
                	**type**\:  list of str
                
                .. attribute:: release_bundle
                
                	Data to identify the release bundle from which the feature paths should be specified.  If the feature crosses release bundles, a new release bundle should be created to support the feature bundle
                	**type**\:   :py:class:`ReleaseBundle <ydk.models.ietf.openconfig_module_catalog.Organizations.Organization.FeatureBundles.FeatureBundle.ReleaseBundle>`
                
                

                """

                _prefix = 'oc-cat'
                _revision = '2017-03-08'

                def __init__(self):
                    self.parent = None
                    self.name = None
                    self.version = None
                    self.feature_bundles = Organizations.Organization.FeatureBundles.FeatureBundle.FeatureBundles_()
                    self.feature_bundles.parent = self
                    self.path = YLeafList()
                    self.path.parent = self
                    self.path.name = 'path'
                    self.release_bundle = Organizations.Organization.FeatureBundles.FeatureBundle.ReleaseBundle()
                    self.release_bundle.parent = self


                class ReleaseBundle(object):
                    """
                    Data to identify the release bundle from which the feature
                    paths should be specified.  If the feature crosses
                    release bundles, a new release bundle should be
                    created to support the feature bundle.
                    
                    .. attribute:: name
                    
                    	Name of the module set which is included in this bundle \- for example, 'openconfig\-bgp'
                    	**type**\:  str
                    
                    	**refers to**\:  :py:class:`name <ydk.models.ietf.openconfig_module_catalog.Organizations.Organization.ReleaseBundles.ReleaseBundle>`
                    
                    .. attribute:: publisher
                    
                    	Reference to the name of the publishing organization
                    	**type**\:  str
                    
                    	**refers to**\:  :py:class:`name <ydk.models.ietf.openconfig_module_catalog.Organizations.Organization>`
                    
                    .. attribute:: version
                    
                    	Version of the referenced release bundle
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'oc-cat'
                    _revision = '2017-03-08'

                    def __init__(self):
                        self.parent = None
                        self.name = None
                        self.publisher = None
                        self.version = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-module-catalog:release-bundle'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.name is not None:
                            return True

                        if self.publisher is not None:
                            return True

                        if self.version is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _openconfig_module_catalog as meta
                        return meta._meta_table['Organizations.Organization.FeatureBundles.FeatureBundle.ReleaseBundle']['meta_info']


                class FeatureBundles_(object):
                    """
                    Enclosing container for the list of included feature
                    bundles.  Feature bundles may be composed from other
                    smaller feature units
                    
                    .. attribute:: feature_bundle
                    
                    	The list of feature bundles included in the current feature bundle
                    	**type**\: list of    :py:class:`FeatureBundle_ <ydk.models.ietf.openconfig_module_catalog.Organizations.Organization.FeatureBundles.FeatureBundle.FeatureBundles_.FeatureBundle_>`
                    
                    

                    """

                    _prefix = 'oc-cat'
                    _revision = '2017-03-08'

                    def __init__(self):
                        self.parent = None
                        self.feature_bundle = YList()
                        self.feature_bundle.parent = self
                        self.feature_bundle.name = 'feature_bundle'


                    class FeatureBundle_(object):
                        """
                        The list of feature bundles included in the current
                        feature bundle.
                        
                        .. attribute:: name  <key>
                        
                        	Name of the referenced feature bundle
                        	**type**\:  str
                        
                        	**refers to**\:  :py:class:`name <ydk.models.ietf.openconfig_module_catalog.Organizations.Organization.FeatureBundles.FeatureBundle>`
                        
                        .. attribute:: publisher
                        
                        	Publisher of the referenced feature bundle
                        	**type**\:  str
                        
                        	**refers to**\:  :py:class:`name <ydk.models.ietf.openconfig_module_catalog.Organizations.Organization>`
                        
                        .. attribute:: version
                        
                        	Version of the referenced feature bundle
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'oc-cat'
                        _revision = '2017-03-08'

                        def __init__(self):
                            self.parent = None
                            self.name = None
                            self.publisher = None
                            self.version = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.name is None:
                                raise YPYModelError('Key property name is None')

                            return self.parent._common_path +'/openconfig-module-catalog:feature-bundle[openconfig-module-catalog:name = ' + str(self.name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.name is not None:
                                return True

                            if self.publisher is not None:
                                return True

                            if self.version is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ietf._meta import _openconfig_module_catalog as meta
                            return meta._meta_table['Organizations.Organization.FeatureBundles.FeatureBundle.FeatureBundles_.FeatureBundle_']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-module-catalog:feature-bundles'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.feature_bundle is not None:
                            for child_ref in self.feature_bundle:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _openconfig_module_catalog as meta
                        return meta._meta_table['Organizations.Organization.FeatureBundles.FeatureBundle.FeatureBundles_']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.name is None:
                        raise YPYModelError('Key property name is None')
                    if self.version is None:
                        raise YPYModelError('Key property version is None')

                    return self.parent._common_path +'/openconfig-module-catalog:feature-bundle[openconfig-module-catalog:name = ' + str(self.name) + '][openconfig-module-catalog:version = ' + str(self.version) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.name is not None:
                        return True

                    if self.version is not None:
                        return True

                    if self.feature_bundles is not None and self.feature_bundles._has_data():
                        return True

                    if self.path is not None:
                        for child in self.path:
                            if child is not None:
                                return True

                    if self.release_bundle is not None and self.release_bundle._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _openconfig_module_catalog as meta
                    return meta._meta_table['Organizations.Organization.FeatureBundles.FeatureBundle']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/openconfig-module-catalog:feature-bundles'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.feature_bundle is not None:
                    for child_ref in self.feature_bundle:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _openconfig_module_catalog as meta
                return meta._meta_table['Organizations.Organization.FeatureBundles']['meta_info']


        class Implementations(object):
            """
            Container for module implementation information
            
            .. attribute:: implementation
            
            	List of available implementations, keyed by an identifier provided by either the implementor or the module maintainer.  Such a key avoids needing a complex composite key to uniquely identify an implementation
            	**type**\: list of    :py:class:`Implementation <ydk.models.ietf.openconfig_module_catalog.Organizations.Organization.Implementations.Implementation>`
            
            

            """

            _prefix = 'oc-cat'
            _revision = '2017-03-08'

            def __init__(self):
                self.parent = None
                self.implementation = YList()
                self.implementation.parent = self
                self.implementation.name = 'implementation'


            class Implementation(object):
                """
                List of available implementations, keyed by an identifier
                provided by either the implementor or the module
                maintainer.  Such a key avoids needing a complex composite
                key to uniquely identify an implementation.
                
                .. attribute:: id  <key>
                
                	An identifier for the implementation, provided by the implementor.  This id should uniquely identify a specific implementation of the module, e.g., based on the vendor, platform, and platform version
                	**type**\:  str
                
                .. attribute:: description
                
                	A text summary of important information about the implementation
                	**type**\:  str
                
                .. attribute:: feature_bundles
                
                	Enclosing container for the list of feature bundles
                	**type**\:   :py:class:`FeatureBundles <ydk.models.ietf.openconfig_module_catalog.Organizations.Organization.Implementations.Implementation.FeatureBundles>`
                
                .. attribute:: platform
                
                	Name of the platform on which the implementation is available \-\- this could be the model name of a network device, a server OS, etc
                	**type**\:  str
                
                .. attribute:: platform_version
                
                	Implementor\-defined version name or number of the module implementation, corresponding to the platform. This could be the firmware version of a network device such as a router, OS version, or other server platform version
                	**type**\:  str
                
                .. attribute:: reference
                
                	A URI (preferred) or text reference to more detailed information about the implementation
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                
                ----
                	**type**\:  str
                
                
                ----
                .. attribute:: status
                
                	Indicates the status of the implementation, e.g., complete, partial, in\-progress, etc.  Implementors may define additional values for the base identity
                	**type**\:   :py:class:`Implementation_Status_TypeIdentity <ydk.models.ietf.openconfig_catalog_types.Implementation_Status_TypeIdentity>`
                
                

                """

                _prefix = 'oc-cat'
                _revision = '2017-03-08'

                def __init__(self):
                    self.parent = None
                    self.id = None
                    self.description = None
                    self.feature_bundles = Organizations.Organization.Implementations.Implementation.FeatureBundles()
                    self.feature_bundles.parent = self
                    self.platform = None
                    self.platform_version = None
                    self.reference = None
                    self.status = None


                class FeatureBundles(object):
                    """
                    Enclosing container for the list of feature bundles
                    
                    .. attribute:: feature_bundle
                    
                    	List of feature bundles supported by the implementation
                    	**type**\: list of    :py:class:`FeatureBundle <ydk.models.ietf.openconfig_module_catalog.Organizations.Organization.Implementations.Implementation.FeatureBundles.FeatureBundle>`
                    
                    

                    """

                    _prefix = 'oc-cat'
                    _revision = '2017-03-08'

                    def __init__(self):
                        self.parent = None
                        self.feature_bundle = YList()
                        self.feature_bundle.parent = self
                        self.feature_bundle.name = 'feature_bundle'


                    class FeatureBundle(object):
                        """
                        List of feature bundles supported by the implementation
                        
                        .. attribute:: name  <key>
                        
                        	Name of the referenced feature bundle
                        	**type**\:  str
                        
                        	**refers to**\:  :py:class:`name <ydk.models.ietf.openconfig_module_catalog.Organizations.Organization.FeatureBundles.FeatureBundle>`
                        
                        .. attribute:: version  <key>
                        
                        	Version of the referenced feature bundle
                        	**type**\:  str
                        
                        .. attribute:: publisher
                        
                        	Publisher of the referenced feature bundle
                        	**type**\:  str
                        
                        	**refers to**\:  :py:class:`name <ydk.models.ietf.openconfig_module_catalog.Organizations.Organization>`
                        
                        

                        """

                        _prefix = 'oc-cat'
                        _revision = '2017-03-08'

                        def __init__(self):
                            self.parent = None
                            self.name = None
                            self.version = None
                            self.publisher = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.name is None:
                                raise YPYModelError('Key property name is None')
                            if self.version is None:
                                raise YPYModelError('Key property version is None')

                            return self.parent._common_path +'/openconfig-module-catalog:feature-bundle[openconfig-module-catalog:name = ' + str(self.name) + '][openconfig-module-catalog:version = ' + str(self.version) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.name is not None:
                                return True

                            if self.version is not None:
                                return True

                            if self.publisher is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ietf._meta import _openconfig_module_catalog as meta
                            return meta._meta_table['Organizations.Organization.Implementations.Implementation.FeatureBundles.FeatureBundle']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-module-catalog:feature-bundles'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.feature_bundle is not None:
                            for child_ref in self.feature_bundle:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _openconfig_module_catalog as meta
                        return meta._meta_table['Organizations.Organization.Implementations.Implementation.FeatureBundles']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.id is None:
                        raise YPYModelError('Key property id is None')

                    return self.parent._common_path +'/openconfig-module-catalog:implementation[openconfig-module-catalog:id = ' + str(self.id) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.id is not None:
                        return True

                    if self.description is not None:
                        return True

                    if self.feature_bundles is not None and self.feature_bundles._has_data():
                        return True

                    if self.platform is not None:
                        return True

                    if self.platform_version is not None:
                        return True

                    if self.reference is not None:
                        return True

                    if self.status is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _openconfig_module_catalog as meta
                    return meta._meta_table['Organizations.Organization.Implementations.Implementation']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/openconfig-module-catalog:implementations'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.implementation is not None:
                    for child_ref in self.implementation:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _openconfig_module_catalog as meta
                return meta._meta_table['Organizations.Organization.Implementations']['meta_info']

        @property
        def _common_path(self):
            if self.name is None:
                raise YPYModelError('Key property name is None')

            return '/openconfig-module-catalog:organizations/openconfig-module-catalog:organization[openconfig-module-catalog:name = ' + str(self.name) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.name is not None:
                return True

            if self.contact is not None:
                return True

            if self.feature_bundles is not None and self.feature_bundles._has_data():
                return True

            if self.implementations is not None and self.implementations._has_data():
                return True

            if self.modules is not None and self.modules._has_data():
                return True

            if self.release_bundles is not None and self.release_bundles._has_data():
                return True

            if self.type is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _openconfig_module_catalog as meta
            return meta._meta_table['Organizations.Organization']['meta_info']

    @property
    def _common_path(self):

        return '/openconfig-module-catalog:organizations'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.organization is not None:
            for child_ref in self.organization:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _openconfig_module_catalog as meta
        return meta._meta_table['Organizations']['meta_info']


