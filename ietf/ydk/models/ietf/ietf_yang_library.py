""" ietf_yang_library 

This module contains monitoring information about the YANG
modules and submodules that are used within a YANG\-based
server.
Copyright (c) 2016 IETF Trust and the persons identified as
authors of the code.  All rights reserved.
Redistribution and use in source and binary forms, with or
without modification, is permitted pursuant to, and subject
to the license terms contained in, the Simplified BSD License
set forth in Section 4.c of the IETF Trust's Legal Provisions
Relating to IETF Documents
(http\://trustee.ietf.org/license\-info).
This version of this YANG module is part of RFC 7895; see
the RFC itself for full legal notices.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class ModulesState(Entity):
    """
    Contains YANG module monitoring information.
    
    .. attribute:: module_set_id
    
    	Contains a server\-specific identifier representing the current set of modules and submodules.  The server MUST change the value of this leaf if the information represented by the 'module' list instances has changed
    	**type**\: str
    
    	**mandatory**\: True
    
    .. attribute:: module
    
    	Each entry represents one revision of one module currently supported by the server
    	**type**\: list of  		 :py:class:`Module <ydk.models.ietf.ietf_yang_library.ModulesState.Module>`
    
    

    """

    _prefix = 'yanglib'
    _revision = '2016-06-21'

    def __init__(self):
        super(ModulesState, self).__init__()
        self._top_entity = None

        self.yang_name = "modules-state"
        self.yang_parent_name = "ietf-yang-library"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([("module", ("module", ModulesState.Module))])
        self._leafs = OrderedDict([
            ('module_set_id', YLeaf(YType.str, 'module-set-id')),
        ])
        self.module_set_id = None

        self.module = YList(self)
        self._segment_path = lambda: "ietf-yang-library:modules-state"

    def __setattr__(self, name, value):
        self._perform_setattr(ModulesState, ['module_set_id'], name, value)


    class Module(Entity):
        """
        Each entry represents one revision of one module
        currently supported by the server.
        
        .. attribute:: name  (key)
        
        	The YANG module or submodule name
        	**type**\: str
        
        	**pattern:** [a\-zA\-Z\_][a\-zA\-Z0\-9\\\-\_.]\*
        
        .. attribute:: revision  (key)
        
        	The YANG module or submodule revision date. A zero\-length string is used if no revision statement is present in the YANG module or submodule
        	**type**\: union of the below types:
        
        		**type**\: str
        
        			**pattern:** \\d{4}\-\\d{2}\-\\d{2}
        
        		**type**\: str
        
        			**length:** 0
        
        .. attribute:: schema
        
        	Contains a URL that represents the YANG schema resource for this module or submodule. This leaf will only be present if there is a URL available for retrieval of the schema for this entry
        	**type**\: str
        
        .. attribute:: namespace
        
        	The XML namespace identifier for this module
        	**type**\: str
        
        	**mandatory**\: True
        
        .. attribute:: feature
        
        	List of YANG feature names from this module that are supported by the server, regardless of whether they are defined in the module or any included submodule
        	**type**\: list of str
        
        	**pattern:** [a\-zA\-Z\_][a\-zA\-Z0\-9\\\-\_.]\*
        
        .. attribute:: deviation
        
        	List of YANG deviation module names and revisions used by this server to modify the conformance of the module associated with this entry.  Note that the same module can be used for deviations for multiple modules, so the same entry MAY appear within multiple 'module' entries. The deviation module MUST be present in the 'module' list, with the same name and revision values. The 'conformance\-type' value will be 'implement' for the deviation module
        	**type**\: list of  		 :py:class:`Deviation <ydk.models.ietf.ietf_yang_library.ModulesState.Module.Deviation>`
        
        .. attribute:: conformance_type
        
        	Indicates the type of conformance the server is claiming for the YANG module identified by this entry
        	**type**\:  :py:class:`ConformanceType <ydk.models.ietf.ietf_yang_library.ModulesState.Module.ConformanceType>`
        
        	**mandatory**\: True
        
        .. attribute:: submodule
        
        	Each entry represents one submodule within the parent module
        	**type**\: list of  		 :py:class:`Submodule <ydk.models.ietf.ietf_yang_library.ModulesState.Module.Submodule>`
        
        

        """

        _prefix = 'yanglib'
        _revision = '2016-06-21'

        def __init__(self):
            super(ModulesState.Module, self).__init__()

            self.yang_name = "module"
            self.yang_parent_name = "modules-state"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['name','revision']
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("deviation", ("deviation", ModulesState.Module.Deviation)), ("submodule", ("submodule", ModulesState.Module.Submodule))])
            self._leafs = OrderedDict([
                ('name', YLeaf(YType.str, 'name')),
                ('revision', YLeaf(YType.str, 'revision')),
                ('schema', YLeaf(YType.str, 'schema')),
                ('namespace', YLeaf(YType.str, 'namespace')),
                ('feature', YLeafList(YType.str, 'feature')),
                ('conformance_type', YLeaf(YType.enumeration, 'conformance-type')),
            ])
            self.name = None
            self.revision = None
            self.schema = None
            self.namespace = None
            self.feature = []
            self.conformance_type = None

            self.deviation = YList(self)
            self.submodule = YList(self)
            self._segment_path = lambda: "module" + "[name='" + str(self.name) + "']" + "[revision='" + str(self.revision) + "']"
            self._absolute_path = lambda: "ietf-yang-library:modules-state/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(ModulesState.Module, ['name', 'revision', 'schema', 'namespace', 'feature', 'conformance_type'], name, value)

        class ConformanceType(Enum):
            """
            ConformanceType (Enum Class)

            Indicates the type of conformance the server is claiming

            for the YANG module identified by this entry.

            .. data:: implement = 0

            	Indicates that the server implements one or more

            	protocol-accessible objects defined in the YANG module

            	identified in this entry.  This includes deviation

            	statements defined in the module.

            	For YANG version 1.1 modules, there is at most one

            	module entry with conformance type 'implement' for a

            	particular module name, since YANG 1.1 requires that,

            	at most, one revision of a module is implemented.

            	For YANG version 1 modules, there SHOULD NOT be more

            	than one module entry for a particular module name.

            .. data:: import_ = 1

            	Indicates that the server imports reusable definitions

            	from the specified revision of the module but does

            	not implement any protocol-accessible objects from

            	this revision.

            	Multiple module entries for the same module name MAY

            	exist.  This can occur if multiple modules import the

            	same module but specify different revision dates in

            	the import statements.

            """

            implement = Enum.YLeaf(0, "implement")

            import_ = Enum.YLeaf(1, "import")



        class Deviation(Entity):
            """
            List of YANG deviation module names and revisions
            used by this server to modify the conformance of
            the module associated with this entry.  Note that
            the same module can be used for deviations for
            multiple modules, so the same entry MAY appear
            within multiple 'module' entries.
            The deviation module MUST be present in the 'module'
            list, with the same name and revision values.
            The 'conformance\-type' value will be 'implement' for
            the deviation module.
            
            .. attribute:: name  (key)
            
            	The YANG module or submodule name
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z\_][a\-zA\-Z0\-9\\\-\_.]\*
            
            .. attribute:: revision  (key)
            
            	The YANG module or submodule revision date. A zero\-length string is used if no revision statement is present in the YANG module or submodule
            	**type**\: union of the below types:
            
            		**type**\: str
            
            			**pattern:** \\d{4}\-\\d{2}\-\\d{2}
            
            		**type**\: str
            
            			**length:** 0
            
            

            """

            _prefix = 'yanglib'
            _revision = '2016-06-21'

            def __init__(self):
                super(ModulesState.Module.Deviation, self).__init__()

                self.yang_name = "deviation"
                self.yang_parent_name = "module"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = ['name','revision']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('name', YLeaf(YType.str, 'name')),
                    ('revision', YLeaf(YType.str, 'revision')),
                ])
                self.name = None
                self.revision = None
                self._segment_path = lambda: "deviation" + "[name='" + str(self.name) + "']" + "[revision='" + str(self.revision) + "']"

            def __setattr__(self, name, value):
                self._perform_setattr(ModulesState.Module.Deviation, ['name', 'revision'], name, value)


        class Submodule(Entity):
            """
            Each entry represents one submodule within the
            parent module.
            
            .. attribute:: name  (key)
            
            	The YANG module or submodule name
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z\_][a\-zA\-Z0\-9\\\-\_.]\*
            
            .. attribute:: revision  (key)
            
            	The YANG module or submodule revision date. A zero\-length string is used if no revision statement is present in the YANG module or submodule
            	**type**\: union of the below types:
            
            		**type**\: str
            
            			**pattern:** \\d{4}\-\\d{2}\-\\d{2}
            
            		**type**\: str
            
            			**length:** 0
            
            .. attribute:: schema
            
            	Contains a URL that represents the YANG schema resource for this module or submodule. This leaf will only be present if there is a URL available for retrieval of the schema for this entry
            	**type**\: str
            
            

            """

            _prefix = 'yanglib'
            _revision = '2016-06-21'

            def __init__(self):
                super(ModulesState.Module.Submodule, self).__init__()

                self.yang_name = "submodule"
                self.yang_parent_name = "module"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = ['name','revision']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('name', YLeaf(YType.str, 'name')),
                    ('revision', YLeaf(YType.str, 'revision')),
                    ('schema', YLeaf(YType.str, 'schema')),
                ])
                self.name = None
                self.revision = None
                self.schema = None
                self._segment_path = lambda: "submodule" + "[name='" + str(self.name) + "']" + "[revision='" + str(self.revision) + "']"

            def __setattr__(self, name, value):
                self._perform_setattr(ModulesState.Module.Submodule, ['name', 'revision', 'schema'], name, value)

    def clone_ptr(self):
        self._top_entity = ModulesState()
        return self._top_entity

