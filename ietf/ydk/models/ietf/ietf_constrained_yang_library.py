""" ietf_constrained_yang_library 

This module contains the list of YANG modules and submodules
implemented by a server.

Copyright (c) 2016 IETF Trust and the persons identified as
authors of the code.  All rights reserved.

Redistribution and use in source and binary forms, with or
without modification, is permitted pursuant to, and subject
to the license terms contained in, the Simplified BSD License
set forth in Section 4.c of the IETF Trust's Legal Provisions
Relating to IETF Documents
(http\://trustee.ietf.org/license\-info).

This version of this YANG module is part of RFC XXXX; see
the RFC itself for full legal notices.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class ModuleSetIdentity(object):
    """
    Base identity from which shared module\-set identifiers
    are derived.
    
    

    """

    _prefix = 'lib'
    _revision = '2017-01-20'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_constrained_yang_library as meta
        return meta._meta_table['ModuleSetIdentity']['meta_info']


class ModulesState(object):
    """
    Contains information about the different data models
    implemented by the server.
    
    .. attribute:: module
    
    	Each entry represents one revision of one module currently supported by the server
    	**type**\: list of    :py:class:`Module <ydk.models.ietf.ietf_constrained_yang_library.ModulesState.Module>`
    
    .. attribute:: module_set_id
    
    	Identifier representing the current set of modules and submodules listed in the 'module' list. This identifier is server\-specific when implemented as unit32 or shared between multiple servers when implemented as identityref. The server MUST change the value of this leaf each time the content of the 'module' list instance change
    	**type**\: one of the below types:
    
    	**type**\:  int
    
    	**range:** 0..4294967295
    
    	**mandatory**\: True
    
    
    ----
    	**type**\:   :py:class:`ModuleSetIdentity <ydk.models.ietf.ietf_constrained_yang_library.ModuleSetIdentity>`
    
    	**mandatory**\: True
    
    
    ----
    

    """

    _prefix = 'lib'
    _revision = '2017-01-20'

    def __init__(self):
        self.module = YList()
        self.module.parent = self
        self.module.name = 'module'
        self.module_set_id = None


    class Module(object):
        """
        Each entry represents one revision of one module
        currently supported by the server.
        
        .. attribute:: revision  <key>
        
        	Revision date assigned to this module or submodule. A zero\-length binary string is used if no revision statement is present in the YANG module or submodule
        	**type**\:  str
        
        	**length:** 4
        
        .. attribute:: sid  <key>
        
        	SID assigned to this module or submodule
        	**type**\:  int
        
        	**range:** 0..18446744073709551615
        
        	**mandatory**\: True
        
        .. attribute:: conformance_type
        
        	Indicates the type of conformance the server is claiming for the YANG module identified by this entry
        	**type**\:   :py:class:`ConformanceTypeEnum <ydk.models.ietf.ietf_constrained_yang_library.ModulesState.Module.ConformanceTypeEnum>`
        
        	**mandatory**\: True
        
        .. attribute:: deviation
        
        	List of YANG deviation modules used by this server to modify the conformance of the module associated with this entry.  Note that the same module can be used for deviations for multiple modules, so the same entry MAY appear within multiple 'module' entries.  The deviation module MUST be present in the 'module' list, with the same sid and revision values. The 'conformance\-type' value will be 'implement' for the deviation module
        	**type**\: list of    :py:class:`Deviation <ydk.models.ietf.ietf_constrained_yang_library.ModulesState.Module.Deviation>`
        
        .. attribute:: feature
        
        	List of YANG features from this module that are supported by the server, regardless whether they are defined in the module or in any included submodule
        	**type**\:  list of int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: submodule
        
        	Each entry represents one submodule within the parent module
        	**type**\: list of    :py:class:`Submodule <ydk.models.ietf.ietf_constrained_yang_library.ModulesState.Module.Submodule>`
        
        

        """

        _prefix = 'lib'
        _revision = '2017-01-20'

        def __init__(self):
            self.parent = None
            self.revision = None
            self.sid = None
            self.conformance_type = None
            self.deviation = YList()
            self.deviation.parent = self
            self.deviation.name = 'deviation'
            self.feature = YLeafList()
            self.feature.parent = self
            self.feature.name = 'feature'
            self.submodule = YList()
            self.submodule.parent = self
            self.submodule.name = 'submodule'

        class ConformanceTypeEnum(Enum):
            """
            ConformanceTypeEnum

            Indicates the type of conformance the server is claiming

            for the YANG module identified by this entry.

            .. data:: implement = 0

            	Indicates that the server implements one or more

            	protocol-accessible objects defined in the YANG

            	module identified in this entry.  This includes

            	deviation statements defined in the module.

            	For YANG version 1.1 modules, there is at most one

            	module entry with conformance type 'implement' for a

            	particular module, since YANG 1.1 requires that

            	at most one revision of a module is implemented.

            	For YANG version 1 modules, there SHOULD NOT be more

            	than one module entry for a particular module.

            .. data:: import_ = 1

            	Indicates that the server imports reusable definitions

            	from the specified revision of the module, but does

            	not implement any protocol accessible objects from

            	this revision.

            	Multiple module entries for the same module MAY

            	exist. This can occur if multiple modules import the

            	same module, but specify different revision-dates in

            	the import statements.

            """

            implement = 0

            import_ = 1


            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_constrained_yang_library as meta
                return meta._meta_table['ModulesState.Module.ConformanceTypeEnum']



        class Deviation(object):
            """
            List of YANG deviation modules used by this server
            to modify the conformance of the module associated
            with this entry.  Note that the same module can be
            used for deviations for multiple modules, so the
            same entry MAY appear within multiple 'module' entries.
            
            The deviation module MUST be present in the 'module'
            list, with the same sid and revision values.
            The 'conformance\-type' value will be 'implement' for
            the deviation module.
            
            .. attribute:: revision  <key>
            
            	Revision date assigned to this module or submodule. A zero\-length binary string is used if no revision statement is present in the YANG module or submodule
            	**type**\:  str
            
            	**length:** 4
            
            .. attribute:: sid  <key>
            
            	SID assigned to this module or submodule
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**mandatory**\: True
            
            

            """

            _prefix = 'lib'
            _revision = '2017-01-20'

            def __init__(self):
                self.parent = None
                self.revision = None
                self.sid = None

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')
                if self.revision is None:
                    raise YPYModelError('Key property revision is None')
                if self.sid is None:
                    raise YPYModelError('Key property sid is None')

                return self.parent._common_path +'/ietf-constrained-yang-library:deviation[ietf-constrained-yang-library:revision = ' + str(self.revision) + '][ietf-constrained-yang-library:sid = ' + str(self.sid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.revision is not None:
                    return True

                if self.sid is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_constrained_yang_library as meta
                return meta._meta_table['ModulesState.Module.Deviation']['meta_info']


        class Submodule(object):
            """
            Each entry represents one submodule within the
            parent module.
            
            .. attribute:: revision  <key>
            
            	Revision date assigned to this module or submodule. A zero\-length binary string is used if no revision statement is present in the YANG module or submodule
            	**type**\:  str
            
            	**length:** 4
            
            .. attribute:: sid  <key>
            
            	SID assigned to this module or submodule
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**mandatory**\: True
            
            

            """

            _prefix = 'lib'
            _revision = '2017-01-20'

            def __init__(self):
                self.parent = None
                self.revision = None
                self.sid = None

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')
                if self.revision is None:
                    raise YPYModelError('Key property revision is None')
                if self.sid is None:
                    raise YPYModelError('Key property sid is None')

                return self.parent._common_path +'/ietf-constrained-yang-library:submodule[ietf-constrained-yang-library:revision = ' + str(self.revision) + '][ietf-constrained-yang-library:sid = ' + str(self.sid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.revision is not None:
                    return True

                if self.sid is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_constrained_yang_library as meta
                return meta._meta_table['ModulesState.Module.Submodule']['meta_info']

        @property
        def _common_path(self):
            if self.revision is None:
                raise YPYModelError('Key property revision is None')
            if self.sid is None:
                raise YPYModelError('Key property sid is None')

            return '/ietf-constrained-yang-library:modules-state/ietf-constrained-yang-library:module[ietf-constrained-yang-library:revision = ' + str(self.revision) + '][ietf-constrained-yang-library:sid = ' + str(self.sid) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.revision is not None:
                return True

            if self.sid is not None:
                return True

            if self.conformance_type is not None:
                return True

            if self.deviation is not None:
                for child_ref in self.deviation:
                    if child_ref._has_data():
                        return True

            if self.feature is not None:
                for child in self.feature:
                    if child is not None:
                        return True

            if self.submodule is not None:
                for child_ref in self.submodule:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_constrained_yang_library as meta
            return meta._meta_table['ModulesState.Module']['meta_info']

    @property
    def _common_path(self):

        return '/ietf-constrained-yang-library:modules-state'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.module is not None:
            for child_ref in self.module:
                if child_ref._has_data():
                    return True

        if self.module_set_id is not None:
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_constrained_yang_library as meta
        return meta._meta_table['ModulesState']['meta_info']


