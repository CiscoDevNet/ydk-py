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
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class ModulesState(Entity):
    """
    Contains YANG module monitoring information.
    
    .. attribute:: module
    
    	Each entry represents one revision of one module currently supported by the server
    	**type**\: list of    :py:class:`Module <ydk.models.ietf.ietf_yang_library.ModulesState.Module>`
    
    .. attribute:: module_set_id
    
    	Contains a server\-specific identifier representing the current set of modules and submodules.  The server MUST change the value of this leaf if the information represented by the 'module' list instances has changed
    	**type**\:  str
    
    	**mandatory**\: True
    
    

    """

    _prefix = 'yanglib'
    _revision = '2016-06-21'

    def __init__(self):
        super(ModulesState, self).__init__()
        self._top_entity = None

        self.yang_name = "modules-state"
        self.yang_parent_name = "ietf-yang-library"

        self.module_set_id = YLeaf(YType.str, "module-set-id")

        self.module = YList(self)

    def __setattr__(self, name, value):
        self._check_monkey_patching_error(name, value)
        with _handle_type_error():
            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                    "Please use list append or extend method."
                                    .format(value))
            if isinstance(value, Enum.YLeaf):
                value = value.name
            if name in ("module_set_id") and name in self.__dict__:
                if isinstance(value, YLeaf):
                    self.__dict__[name].set(value.get())
                elif isinstance(value, YLeafList):
                    super(ModulesState, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(ModulesState, self).__setattr__(name, value)


    class Module(Entity):
        """
        Each entry represents one revision of one module
        currently supported by the server.
        
        .. attribute:: name  <key>
        
        	The YANG module or submodule name
        	**type**\:  str
        
        	**pattern:** [a\-zA\-Z\_][a\-zA\-Z0\-9\\\-\_.]\*
        
        .. attribute:: revision  <key>
        
        	The YANG module or submodule revision date. A zero\-length string is used if no revision statement is present in the YANG module or submodule
        	**type**\: one of the below types:
        
        	**type**\:  str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}
        
        
        ----
        	**type**\:  str
        
        	**length:** 0
        
        
        ----
        .. attribute:: conformance_type
        
        	Indicates the type of conformance the server is claiming for the YANG module identified by this entry
        	**type**\:   :py:class:`ConformanceType <ydk.models.ietf.ietf_yang_library.ModulesState.Module.ConformanceType>`
        
        	**mandatory**\: True
        
        .. attribute:: deviation
        
        	List of YANG deviation module names and revisions used by this server to modify the conformance of the module associated with this entry.  Note that the same module can be used for deviations for multiple modules, so the same entry MAY appear within multiple 'module' entries.  The deviation module MUST be present in the 'module' list, with the same name and revision values. The 'conformance\-type' value will be 'implement' for the deviation module
        	**type**\: list of    :py:class:`Deviation <ydk.models.ietf.ietf_yang_library.ModulesState.Module.Deviation>`
        
        .. attribute:: feature
        
        	List of YANG feature names from this module that are supported by the server, regardless of whether they are defined in the module or any included submodule
        	**type**\:  list of str
        
        	**pattern:** [a\-zA\-Z\_][a\-zA\-Z0\-9\\\-\_.]\*
        
        .. attribute:: namespace
        
        	The XML namespace identifier for this module
        	**type**\:  str
        
        	**mandatory**\: True
        
        .. attribute:: schema
        
        	Contains a URL that represents the YANG schema resource for this module or submodule.  This leaf will only be present if there is a URL available for retrieval of the schema for this entry
        	**type**\:  str
        
        .. attribute:: submodule
        
        	Each entry represents one submodule within the parent module
        	**type**\: list of    :py:class:`Submodule <ydk.models.ietf.ietf_yang_library.ModulesState.Module.Submodule>`
        
        

        """

        _prefix = 'yanglib'
        _revision = '2016-06-21'

        def __init__(self):
            super(ModulesState.Module, self).__init__()

            self.yang_name = "module"
            self.yang_parent_name = "modules-state"

            self.name = YLeaf(YType.str, "name")

            self.revision = YLeaf(YType.str, "revision")

            self.conformance_type = YLeaf(YType.enumeration, "conformance-type")

            self.feature = YLeafList(YType.str, "feature")

            self.namespace = YLeaf(YType.str, "namespace")

            self.schema = YLeaf(YType.str, "schema")

            self.deviation = YList(self)
            self.submodule = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("name",
                            "revision",
                            "conformance_type",
                            "feature",
                            "namespace",
                            "schema") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(ModulesState.Module, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(ModulesState.Module, self).__setattr__(name, value)

        class ConformanceType(Enum):
            """
            ConformanceType

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
            
            .. attribute:: name  <key>
            
            	The YANG module or submodule name
            	**type**\:  str
            
            	**pattern:** [a\-zA\-Z\_][a\-zA\-Z0\-9\\\-\_.]\*
            
            .. attribute:: revision  <key>
            
            	The YANG module or submodule revision date. A zero\-length string is used if no revision statement is present in the YANG module or submodule
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            	**pattern:** \\d{4}\-\\d{2}\-\\d{2}
            
            
            ----
            	**type**\:  str
            
            	**length:** 0
            
            
            ----
            

            """

            _prefix = 'yanglib'
            _revision = '2016-06-21'

            def __init__(self):
                super(ModulesState.Module.Deviation, self).__init__()

                self.yang_name = "deviation"
                self.yang_parent_name = "module"

                self.name = YLeaf(YType.str, "name")

                self.revision = YLeaf(YType.str, "revision")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("name",
                                "revision") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(ModulesState.Module.Deviation, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(ModulesState.Module.Deviation, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.name.is_set or
                    self.revision.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.name.yfilter != YFilter.not_set or
                    self.revision.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "deviation" + "[name='" + self.name.get() + "']" + "[revision='" + self.revision.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.name.get_name_leafdata())
                if (self.revision.is_set or self.revision.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.revision.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "name" or name == "revision"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "name"):
                    self.name = value
                    self.name.value_namespace = name_space
                    self.name.value_namespace_prefix = name_space_prefix
                if(value_path == "revision"):
                    self.revision = value
                    self.revision.value_namespace = name_space
                    self.revision.value_namespace_prefix = name_space_prefix


        class Submodule(Entity):
            """
            Each entry represents one submodule within the
            parent module.
            
            .. attribute:: name  <key>
            
            	The YANG module or submodule name
            	**type**\:  str
            
            	**pattern:** [a\-zA\-Z\_][a\-zA\-Z0\-9\\\-\_.]\*
            
            .. attribute:: revision  <key>
            
            	The YANG module or submodule revision date. A zero\-length string is used if no revision statement is present in the YANG module or submodule
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            	**pattern:** \\d{4}\-\\d{2}\-\\d{2}
            
            
            ----
            	**type**\:  str
            
            	**length:** 0
            
            
            ----
            .. attribute:: schema
            
            	Contains a URL that represents the YANG schema resource for this module or submodule.  This leaf will only be present if there is a URL available for retrieval of the schema for this entry
            	**type**\:  str
            
            

            """

            _prefix = 'yanglib'
            _revision = '2016-06-21'

            def __init__(self):
                super(ModulesState.Module.Submodule, self).__init__()

                self.yang_name = "submodule"
                self.yang_parent_name = "module"

                self.name = YLeaf(YType.str, "name")

                self.revision = YLeaf(YType.str, "revision")

                self.schema = YLeaf(YType.str, "schema")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("name",
                                "revision",
                                "schema") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(ModulesState.Module.Submodule, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(ModulesState.Module.Submodule, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.name.is_set or
                    self.revision.is_set or
                    self.schema.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.name.yfilter != YFilter.not_set or
                    self.revision.yfilter != YFilter.not_set or
                    self.schema.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "submodule" + "[name='" + self.name.get() + "']" + "[revision='" + self.revision.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.name.get_name_leafdata())
                if (self.revision.is_set or self.revision.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.revision.get_name_leafdata())
                if (self.schema.is_set or self.schema.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.schema.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "name" or name == "revision" or name == "schema"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "name"):
                    self.name = value
                    self.name.value_namespace = name_space
                    self.name.value_namespace_prefix = name_space_prefix
                if(value_path == "revision"):
                    self.revision = value
                    self.revision.value_namespace = name_space
                    self.revision.value_namespace_prefix = name_space_prefix
                if(value_path == "schema"):
                    self.schema = value
                    self.schema.value_namespace = name_space
                    self.schema.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.deviation:
                if (c.has_data()):
                    return True
            for c in self.submodule:
                if (c.has_data()):
                    return True
            for leaf in self.feature.getYLeafs():
                if (leaf.yfilter != YFilter.not_set):
                    return True
            return (
                self.name.is_set or
                self.revision.is_set or
                self.conformance_type.is_set or
                self.namespace.is_set or
                self.schema.is_set)

        def has_operation(self):
            for c in self.deviation:
                if (c.has_operation()):
                    return True
            for c in self.submodule:
                if (c.has_operation()):
                    return True
            for leaf in self.feature.getYLeafs():
                if (leaf.is_set):
                    return True
            return (
                self.yfilter != YFilter.not_set or
                self.name.yfilter != YFilter.not_set or
                self.revision.yfilter != YFilter.not_set or
                self.conformance_type.yfilter != YFilter.not_set or
                self.feature.yfilter != YFilter.not_set or
                self.namespace.yfilter != YFilter.not_set or
                self.schema.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "module" + "[name='" + self.name.get() + "']" + "[revision='" + self.revision.get() + "']" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "ietf-yang-library:modules-state/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                leaf_name_data.append(self.name.get_name_leafdata())
            if (self.revision.is_set or self.revision.yfilter != YFilter.not_set):
                leaf_name_data.append(self.revision.get_name_leafdata())
            if (self.conformance_type.is_set or self.conformance_type.yfilter != YFilter.not_set):
                leaf_name_data.append(self.conformance_type.get_name_leafdata())
            if (self.namespace.is_set or self.namespace.yfilter != YFilter.not_set):
                leaf_name_data.append(self.namespace.get_name_leafdata())
            if (self.schema.is_set or self.schema.yfilter != YFilter.not_set):
                leaf_name_data.append(self.schema.get_name_leafdata())

            leaf_name_data.extend(self.feature.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "deviation"):
                for c in self.deviation:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = ModulesState.Module.Deviation()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.deviation.append(c)
                return c

            if (child_yang_name == "submodule"):
                for c in self.submodule:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = ModulesState.Module.Submodule()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.submodule.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "deviation" or name == "submodule" or name == "name" or name == "revision" or name == "conformance-type" or name == "feature" or name == "namespace" or name == "schema"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "name"):
                self.name = value
                self.name.value_namespace = name_space
                self.name.value_namespace_prefix = name_space_prefix
            if(value_path == "revision"):
                self.revision = value
                self.revision.value_namespace = name_space
                self.revision.value_namespace_prefix = name_space_prefix
            if(value_path == "conformance-type"):
                self.conformance_type = value
                self.conformance_type.value_namespace = name_space
                self.conformance_type.value_namespace_prefix = name_space_prefix
            if(value_path == "feature"):
                self.feature.append(value)
            if(value_path == "namespace"):
                self.namespace = value
                self.namespace.value_namespace = name_space
                self.namespace.value_namespace_prefix = name_space_prefix
            if(value_path == "schema"):
                self.schema = value
                self.schema.value_namespace = name_space
                self.schema.value_namespace_prefix = name_space_prefix

    def has_data(self):
        for c in self.module:
            if (c.has_data()):
                return True
        return self.module_set_id.is_set

    def has_operation(self):
        for c in self.module:
            if (c.has_operation()):
                return True
        return (
            self.yfilter != YFilter.not_set or
            self.module_set_id.yfilter != YFilter.not_set)

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "ietf-yang-library:modules-state" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()
        if (self.module_set_id.is_set or self.module_set_id.yfilter != YFilter.not_set):
            leaf_name_data.append(self.module_set_id.get_name_leafdata())

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "module"):
            for c in self.module:
                segment = c.get_segment_path()
                if (segment_path == segment):
                    return c
            c = ModulesState.Module()
            c.parent = self
            local_reference_key = "ydk::seg::%s" % segment_path
            self._local_refs[local_reference_key] = c
            self.module.append(c)
            return c

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "module" or name == "module-set-id"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        if(value_path == "module-set-id"):
            self.module_set_id = value
            self.module_set_id.value_namespace = name_space
            self.module_set_id.value_namespace_prefix = name_space_prefix

    def clone_ptr(self):
        self._top_entity = ModulesState()
        return self._top_entity

