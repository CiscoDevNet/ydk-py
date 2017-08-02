""" ietf_netconf 

NETCONF Protocol Data Types and Protocol Operations.

Copyright (c) 2011 IETF Trust and the persons identified as
the document authors.  All rights reserved.

Redistribution and use in source and binary forms, with or
without modification, is permitted pursuant to, and subject
to the license terms contained in, the Simplified BSD License
set forth in Section 4.c of the IETF Trust's Legal Provisions
Relating to IETF Documents
(http\://trustee.ietf.org/license\-info).

This version of this YANG module is part of RFC 6241; see
the RFC itself for full legal notices.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class EditOperationType(Enum):
    """
    EditOperationType

    NETCONF 'operation' attribute values

    .. data:: merge = 0

    	The configuration data identified by the

    	element containing this attribute is merged

    	with the configuration at the corresponding

    	level in the configuration datastore identified

    	by the target parameter.

    .. data:: replace = 1

    	The configuration data identified by the element

    	containing this attribute replaces any related

    	configuration in the configuration datastore

    	identified by the target parameter.  If no such

    	configuration data exists in the configuration

    	datastore, it is created.  Unlike a

    	<copy-config> operation, which replaces the

    	entire target configuration, only the configuration

    	actually present in the config parameter is affected.

    .. data:: create = 2

    	The configuration data identified by the element

    	containing this attribute is added to the

    	configuration if and only if the configuration

    	data does not already exist in the configuration

    	datastore.  If the configuration data exists, an

    	<rpc-error> element is returned with an

    	<error-tag> value of 'data-exists'.

    .. data:: delete = 3

    	The configuration data identified by the element

    	containing this attribute is deleted from the

    	configuration if and only if the configuration

    	data currently exists in the configuration

    	datastore.  If the configuration data does not

    	exist, an <rpc-error> element is returned with

    	an <error-tag> value of 'data-missing'.

    .. data:: remove = 4

    	The configuration data identified by the element

    	containing this attribute is deleted from the

    	configuration if the configuration

    	data currently exists in the configuration

    	datastore.  If the configuration data does not

    	exist, the 'remove' operation is silently ignored

    	by the server.

    """

    merge = Enum.YLeaf(0, "merge")

    replace = Enum.YLeaf(1, "replace")

    create = Enum.YLeaf(2, "create")

    delete = Enum.YLeaf(3, "delete")

    remove = Enum.YLeaf(4, "remove")


class ErrorSeverityType(Enum):
    """
    ErrorSeverityType

    NETCONF Error Severity

    .. data:: error = 0

    	Error severity

    .. data:: warning = 1

    	Warning severity

    """

    error = Enum.YLeaf(0, "error")

    warning = Enum.YLeaf(1, "warning")


class ErrorTagType(Enum):
    """
    ErrorTagType

    NETCONF Error Tag

    .. data:: in_use = 0

    	The request requires a resource that

    	already is in use.

    .. data:: invalid_value = 1

    	The request specifies an unacceptable value for one

    	or more parameters.

    .. data:: too_big = 2

    	The request or response (that would be generated) is

    	too large for the implementation to handle.

    .. data:: missing_attribute = 3

    	An expected attribute is missing.

    .. data:: bad_attribute = 4

    	An attribute value is not correct; e.g., wrong type,

    	out of range, pattern mismatch.

    .. data:: unknown_attribute = 5

    	An unexpected attribute is present.

    .. data:: missing_element = 6

    	An expected element is missing.

    .. data:: bad_element = 7

    	An element value is not correct; e.g., wrong type,

    	out of range, pattern mismatch.

    .. data:: unknown_element = 8

    	An unexpected element is present.

    .. data:: unknown_namespace = 9

    	An unexpected namespace is present.

    .. data:: access_denied = 10

    	Access to the requested protocol operation or

    	data model is denied because authorization failed.

    .. data:: lock_denied = 11

    	Access to the requested lock is denied because the

    	lock is currently held by another entity.

    .. data:: resource_denied = 12

    	Request could not be completed because of

    	insufficient resources.

    .. data:: rollback_failed = 13

    	Request to roll back some configuration change (via

    	rollback-on-error or <discard-changes> operations)

    	was not completed for some reason.

    .. data:: data_exists = 14

    	Request could not be completed because the relevant

    	data model content already exists.  For example,

    	a 'create' operation was attempted on data that

    	already exists.

    .. data:: data_missing = 15

    	Request could not be completed because the relevant

    	data model content does not exist.  For example,

    	a 'delete' operation was attempted on

    	data that does not exist.

    .. data:: operation_not_supported = 16

    	Request could not be completed because the requested

    	operation is not supported by this implementation.

    .. data:: operation_failed = 17

    	Request could not be completed because the requested

    	operation failed for some reason not covered by

    	any other error condition.

    .. data:: partial_operation = 18

    	This error-tag is obsolete, and SHOULD NOT be sent

    	by servers conforming to this document.

    .. data:: malformed_message = 19

    	A message could not be handled because it failed to

    	be parsed correctly.  For example, the message is not

    	well-formed XML or it uses an invalid character set.

    """

    in_use = Enum.YLeaf(0, "in-use")

    invalid_value = Enum.YLeaf(1, "invalid-value")

    too_big = Enum.YLeaf(2, "too-big")

    missing_attribute = Enum.YLeaf(3, "missing-attribute")

    bad_attribute = Enum.YLeaf(4, "bad-attribute")

    unknown_attribute = Enum.YLeaf(5, "unknown-attribute")

    missing_element = Enum.YLeaf(6, "missing-element")

    bad_element = Enum.YLeaf(7, "bad-element")

    unknown_element = Enum.YLeaf(8, "unknown-element")

    unknown_namespace = Enum.YLeaf(9, "unknown-namespace")

    access_denied = Enum.YLeaf(10, "access-denied")

    lock_denied = Enum.YLeaf(11, "lock-denied")

    resource_denied = Enum.YLeaf(12, "resource-denied")

    rollback_failed = Enum.YLeaf(13, "rollback-failed")

    data_exists = Enum.YLeaf(14, "data-exists")

    data_missing = Enum.YLeaf(15, "data-missing")

    operation_not_supported = Enum.YLeaf(16, "operation-not-supported")

    operation_failed = Enum.YLeaf(17, "operation-failed")

    partial_operation = Enum.YLeaf(18, "partial-operation")

    malformed_message = Enum.YLeaf(19, "malformed-message")



class GetConfig(Entity):
    """
    Retrieve all or part of a specified configuration.
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.ietf.ietf_netconf.GetConfig.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:   :py:class:`Output <ydk.models.ietf.ietf_netconf.GetConfig.Output>`
    
    

    """

    _prefix = 'nc'
    _revision = '2011-06-01'

    def __init__(self):
        super(GetConfig, self).__init__()
        self._top_entity = None

        self.yang_name = "get-config"
        self.yang_parent_name = "ietf-netconf"

        self.input = GetConfig.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")

        self.output = GetConfig.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._children_yang_names.add("output")


    class Input(Entity):
        """
        
        
        .. attribute:: filter
        
        	Subtree or XPath filter to use
        	**type**\:  anyxml
        
        .. attribute:: source
        
        	Particular configuration to retrieve
        	**type**\:   :py:class:`Source <ydk.models.ietf.ietf_netconf.GetConfig.Input.Source>`
        
        .. attribute:: with_defaults
        
        	The explicit defaults processing mode requested
        	**type**\:   :py:class:`WithDefaultsMode <ydk.models.ietf.ietf_netconf_with_defaults.WithDefaultsMode>`
        
        

        """

        _prefix = 'nc'
        _revision = '2011-06-01'

        def __init__(self):
            super(GetConfig.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "get-config"

            self.filter = YLeaf(YType.str, "filter")

            self.with_defaults = YLeaf(YType.enumeration, "ietf-netconf-with-defaults:with-defaults")

            self.source = GetConfig.Input.Source()
            self.source.parent = self
            self._children_name_map["source"] = "source"
            self._children_yang_names.add("source")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("filter",
                            "with_defaults") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(GetConfig.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(GetConfig.Input, self).__setattr__(name, value)


        class Source(Entity):
            """
            Particular configuration to retrieve.
            
            .. attribute:: candidate
            
            	The candidate configuration is the config source
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: running
            
            	The running configuration is the config source
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: startup
            
            	The startup configuration is the config source. This is optional\-to\-implement on the server because not all servers will support filtering for this datastore
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'nc'
            _revision = '2011-06-01'

            def __init__(self):
                super(GetConfig.Input.Source, self).__init__()

                self.yang_name = "source"
                self.yang_parent_name = "input"

                self.candidate = YLeaf(YType.empty, "candidate")

                self.running = YLeaf(YType.empty, "running")

                self.startup = YLeaf(YType.empty, "startup")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("candidate",
                                "running",
                                "startup") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(GetConfig.Input.Source, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(GetConfig.Input.Source, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.candidate.is_set or
                    self.running.is_set or
                    self.startup.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.candidate.yfilter != YFilter.not_set or
                    self.running.yfilter != YFilter.not_set or
                    self.startup.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "source" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "ietf-netconf:get-config/input/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.candidate.is_set or self.candidate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.candidate.get_name_leafdata())
                if (self.running.is_set or self.running.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.running.get_name_leafdata())
                if (self.startup.is_set or self.startup.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.startup.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "candidate" or name == "running" or name == "startup"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "candidate"):
                    self.candidate = value
                    self.candidate.value_namespace = name_space
                    self.candidate.value_namespace_prefix = name_space_prefix
                if(value_path == "running"):
                    self.running = value
                    self.running.value_namespace = name_space
                    self.running.value_namespace_prefix = name_space_prefix
                if(value_path == "startup"):
                    self.startup = value
                    self.startup.value_namespace = name_space
                    self.startup.value_namespace_prefix = name_space_prefix

        def has_data(self):
            return (
                self.filter.is_set or
                self.with_defaults.is_set or
                (self.source is not None and self.source.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.filter.yfilter != YFilter.not_set or
                self.with_defaults.yfilter != YFilter.not_set or
                (self.source is not None and self.source.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "ietf-netconf:get-config/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.filter.is_set or self.filter.yfilter != YFilter.not_set):
                leaf_name_data.append(self.filter.get_name_leafdata())
            if (self.with_defaults.is_set or self.with_defaults.yfilter != YFilter.not_set):
                leaf_name_data.append(self.with_defaults.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "source"):
                if (self.source is None):
                    self.source = GetConfig.Input.Source()
                    self.source.parent = self
                    self._children_name_map["source"] = "source"
                return self.source

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "source" or name == "filter" or name == "with-defaults"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "filter"):
                self.filter = value
                self.filter.value_namespace = name_space
                self.filter.value_namespace_prefix = name_space_prefix
            if(value_path == "with-defaults"):
                self.with_defaults = value
                self.with_defaults.value_namespace = name_space
                self.with_defaults.value_namespace_prefix = name_space_prefix


    class Output(Entity):
        """
        
        
        .. attribute:: data
        
        	Copy of the source datastore subset that matched the filter criteria (if any).  An empty data container indicates that the request did not produce any results
        	**type**\:  anyxml
        
        

        """

        _prefix = 'nc'
        _revision = '2011-06-01'

        def __init__(self):
            super(GetConfig.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "get-config"

            self.data = YLeaf(YType.str, "data")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("data") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(GetConfig.Output, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(GetConfig.Output, self).__setattr__(name, value)

        def has_data(self):
            return self.data.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.data.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "output" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "ietf-netconf:get-config/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.data.is_set or self.data.yfilter != YFilter.not_set):
                leaf_name_data.append(self.data.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "data"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "data"):
                self.data = value
                self.data.value_namespace = name_space
                self.data.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (
            (self.input is not None and self.input.has_data()) or
            (self.output is not None and self.output.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()) or
            (self.output is not None and self.output.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "ietf-netconf:get-config" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "input"):
            if (self.input is None):
                self.input = GetConfig.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        if (child_yang_name == "output"):
            if (self.output is None):
                self.output = GetConfig.Output()
                self.output.parent = self
                self._children_name_map["output"] = "output"
            return self.output

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "input" or name == "output"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = GetConfig()
        return self._top_entity

class EditConfig(Entity):
    """
    The <edit\-config> operation loads all or part of a specified
    configuration to the specified target configuration.
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.ietf.ietf_netconf.EditConfig.Input>`
    
    

    """

    _prefix = 'nc'
    _revision = '2011-06-01'

    def __init__(self):
        super(EditConfig, self).__init__()
        self._top_entity = None

        self.yang_name = "edit-config"
        self.yang_parent_name = "ietf-netconf"

        self.input = EditConfig.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")


    class Input(Entity):
        """
        
        
        .. attribute:: config
        
        	Inline Config content
        	**type**\:  anyxml
        
        .. attribute:: default_operation
        
        	The default operation to use
        	**type**\:   :py:class:`DefaultOperation <ydk.models.ietf.ietf_netconf.EditConfig.Input.DefaultOperation>`
        
        	**default value**\: merge
        
        .. attribute:: error_option
        
        	The error option to use
        	**type**\:   :py:class:`ErrorOption <ydk.models.ietf.ietf_netconf.EditConfig.Input.ErrorOption>`
        
        	**default value**\: stop-on-error
        
        .. attribute:: target
        
        	Particular configuration to edit
        	**type**\:   :py:class:`Target <ydk.models.ietf.ietf_netconf.EditConfig.Input.Target>`
        
        .. attribute:: test_option
        
        	The test option to use
        	**type**\:   :py:class:`TestOption <ydk.models.ietf.ietf_netconf.EditConfig.Input.TestOption>`
        
        	**default value**\: test-then-set
        
        .. attribute:: url
        
        	URL\-based config content
        	**type**\:  str
        
        

        """

        _prefix = 'nc'
        _revision = '2011-06-01'

        def __init__(self):
            super(EditConfig.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "edit-config"

            self.config = YLeaf(YType.str, "config")

            self.default_operation = YLeaf(YType.enumeration, "default-operation")

            self.error_option = YLeaf(YType.enumeration, "error-option")

            self.test_option = YLeaf(YType.enumeration, "test-option")

            self.url = YLeaf(YType.str, "url")

            self.target = EditConfig.Input.Target()
            self.target.parent = self
            self._children_name_map["target"] = "target"
            self._children_yang_names.add("target")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("config",
                            "default_operation",
                            "error_option",
                            "test_option",
                            "url") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(EditConfig.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(EditConfig.Input, self).__setattr__(name, value)

        class DefaultOperation(Enum):
            """
            DefaultOperation

            The default operation to use.

            .. data:: merge = 0

            	The default operation is merge.

            .. data:: replace = 1

            	The default operation is replace.

            .. data:: none = 2

            	There is no default operation.

            """

            merge = Enum.YLeaf(0, "merge")

            replace = Enum.YLeaf(1, "replace")

            none = Enum.YLeaf(2, "none")


        class ErrorOption(Enum):
            """
            ErrorOption

            The error option to use.

            .. data:: stop_on_error = 0

            	The server will stop on errors.

            .. data:: continue_on_error = 1

            	The server may continue on errors.

            .. data:: rollback_on_error = 2

            	The server will roll back on errors.

            	This value can only be used if the 'rollback-on-error'

            	feature is supported.

            """

            stop_on_error = Enum.YLeaf(0, "stop-on-error")

            continue_on_error = Enum.YLeaf(1, "continue-on-error")

            rollback_on_error = Enum.YLeaf(2, "rollback-on-error")


        class TestOption(Enum):
            """
            TestOption

            The test option to use.

            .. data:: test_then_set = 0

            	The server will test and then set if no errors.

            .. data:: set = 1

            	The server will set without a test first.

            .. data:: test_only = 2

            	The server will only test and not set, even

            	if there are no errors.

            """

            test_then_set = Enum.YLeaf(0, "test-then-set")

            set = Enum.YLeaf(1, "set")

            test_only = Enum.YLeaf(2, "test-only")



        class Target(Entity):
            """
            Particular configuration to edit.
            
            .. attribute:: candidate
            
            	The candidate configuration is the config target
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: running
            
            	The running configuration is the config source
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'nc'
            _revision = '2011-06-01'

            def __init__(self):
                super(EditConfig.Input.Target, self).__init__()

                self.yang_name = "target"
                self.yang_parent_name = "input"

                self.candidate = YLeaf(YType.empty, "candidate")

                self.running = YLeaf(YType.empty, "running")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("candidate",
                                "running") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(EditConfig.Input.Target, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(EditConfig.Input.Target, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.candidate.is_set or
                    self.running.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.candidate.yfilter != YFilter.not_set or
                    self.running.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "target" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "ietf-netconf:edit-config/input/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.candidate.is_set or self.candidate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.candidate.get_name_leafdata())
                if (self.running.is_set or self.running.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.running.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "candidate" or name == "running"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "candidate"):
                    self.candidate = value
                    self.candidate.value_namespace = name_space
                    self.candidate.value_namespace_prefix = name_space_prefix
                if(value_path == "running"):
                    self.running = value
                    self.running.value_namespace = name_space
                    self.running.value_namespace_prefix = name_space_prefix

        def has_data(self):
            return (
                self.config.is_set or
                self.default_operation.is_set or
                self.error_option.is_set or
                self.test_option.is_set or
                self.url.is_set or
                (self.target is not None and self.target.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.config.yfilter != YFilter.not_set or
                self.default_operation.yfilter != YFilter.not_set or
                self.error_option.yfilter != YFilter.not_set or
                self.test_option.yfilter != YFilter.not_set or
                self.url.yfilter != YFilter.not_set or
                (self.target is not None and self.target.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "ietf-netconf:edit-config/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.config.is_set or self.config.yfilter != YFilter.not_set):
                leaf_name_data.append(self.config.get_name_leafdata())
            if (self.default_operation.is_set or self.default_operation.yfilter != YFilter.not_set):
                leaf_name_data.append(self.default_operation.get_name_leafdata())
            if (self.error_option.is_set or self.error_option.yfilter != YFilter.not_set):
                leaf_name_data.append(self.error_option.get_name_leafdata())
            if (self.test_option.is_set or self.test_option.yfilter != YFilter.not_set):
                leaf_name_data.append(self.test_option.get_name_leafdata())
            if (self.url.is_set or self.url.yfilter != YFilter.not_set):
                leaf_name_data.append(self.url.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "target"):
                if (self.target is None):
                    self.target = EditConfig.Input.Target()
                    self.target.parent = self
                    self._children_name_map["target"] = "target"
                return self.target

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "target" or name == "config" or name == "default-operation" or name == "error-option" or name == "test-option" or name == "url"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "config"):
                self.config = value
                self.config.value_namespace = name_space
                self.config.value_namespace_prefix = name_space_prefix
            if(value_path == "default-operation"):
                self.default_operation = value
                self.default_operation.value_namespace = name_space
                self.default_operation.value_namespace_prefix = name_space_prefix
            if(value_path == "error-option"):
                self.error_option = value
                self.error_option.value_namespace = name_space
                self.error_option.value_namespace_prefix = name_space_prefix
            if(value_path == "test-option"):
                self.test_option = value
                self.test_option.value_namespace = name_space
                self.test_option.value_namespace_prefix = name_space_prefix
            if(value_path == "url"):
                self.url = value
                self.url.value_namespace = name_space
                self.url.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.input is not None and self.input.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "ietf-netconf:edit-config" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "input"):
            if (self.input is None):
                self.input = EditConfig.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "input"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = EditConfig()
        return self._top_entity

class CopyConfig(Entity):
    """
    Create or replace an entire configuration datastore with the
    contents of another complete configuration datastore.
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.ietf.ietf_netconf.CopyConfig.Input>`
    
    

    """

    _prefix = 'nc'
    _revision = '2011-06-01'

    def __init__(self):
        super(CopyConfig, self).__init__()
        self._top_entity = None

        self.yang_name = "copy-config"
        self.yang_parent_name = "ietf-netconf"

        self.input = CopyConfig.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")


    class Input(Entity):
        """
        
        
        .. attribute:: source
        
        	Particular configuration to copy from
        	**type**\:   :py:class:`Source <ydk.models.ietf.ietf_netconf.CopyConfig.Input.Source>`
        
        .. attribute:: target
        
        	Particular configuration to copy to
        	**type**\:   :py:class:`Target <ydk.models.ietf.ietf_netconf.CopyConfig.Input.Target>`
        
        .. attribute:: with_defaults
        
        	The explicit defaults processing mode requested
        	**type**\:   :py:class:`WithDefaultsMode <ydk.models.ietf.ietf_netconf_with_defaults.WithDefaultsMode>`
        
        

        """

        _prefix = 'nc'
        _revision = '2011-06-01'

        def __init__(self):
            super(CopyConfig.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "copy-config"

            self.with_defaults = YLeaf(YType.enumeration, "ietf-netconf-with-defaults:with-defaults")

            self.source = CopyConfig.Input.Source()
            self.source.parent = self
            self._children_name_map["source"] = "source"
            self._children_yang_names.add("source")

            self.target = CopyConfig.Input.Target()
            self.target.parent = self
            self._children_name_map["target"] = "target"
            self._children_yang_names.add("target")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("with_defaults") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CopyConfig.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CopyConfig.Input, self).__setattr__(name, value)


        class Target(Entity):
            """
            Particular configuration to copy to.
            
            .. attribute:: candidate
            
            	The candidate configuration is the config target
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: running
            
            	The running configuration is the config target. This is optional\-to\-implement on the server
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: startup
            
            	The startup configuration is the config target
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: url
            
            	The URL\-based configuration is the config target
            	**type**\:  str
            
            

            """

            _prefix = 'nc'
            _revision = '2011-06-01'

            def __init__(self):
                super(CopyConfig.Input.Target, self).__init__()

                self.yang_name = "target"
                self.yang_parent_name = "input"

                self.candidate = YLeaf(YType.empty, "candidate")

                self.running = YLeaf(YType.empty, "running")

                self.startup = YLeaf(YType.empty, "startup")

                self.url = YLeaf(YType.str, "url")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("candidate",
                                "running",
                                "startup",
                                "url") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CopyConfig.Input.Target, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CopyConfig.Input.Target, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.candidate.is_set or
                    self.running.is_set or
                    self.startup.is_set or
                    self.url.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.candidate.yfilter != YFilter.not_set or
                    self.running.yfilter != YFilter.not_set or
                    self.startup.yfilter != YFilter.not_set or
                    self.url.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "target" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "ietf-netconf:copy-config/input/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.candidate.is_set or self.candidate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.candidate.get_name_leafdata())
                if (self.running.is_set or self.running.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.running.get_name_leafdata())
                if (self.startup.is_set or self.startup.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.startup.get_name_leafdata())
                if (self.url.is_set or self.url.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.url.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "candidate" or name == "running" or name == "startup" or name == "url"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "candidate"):
                    self.candidate = value
                    self.candidate.value_namespace = name_space
                    self.candidate.value_namespace_prefix = name_space_prefix
                if(value_path == "running"):
                    self.running = value
                    self.running.value_namespace = name_space
                    self.running.value_namespace_prefix = name_space_prefix
                if(value_path == "startup"):
                    self.startup = value
                    self.startup.value_namespace = name_space
                    self.startup.value_namespace_prefix = name_space_prefix
                if(value_path == "url"):
                    self.url = value
                    self.url.value_namespace = name_space
                    self.url.value_namespace_prefix = name_space_prefix


        class Source(Entity):
            """
            Particular configuration to copy from.
            
            .. attribute:: candidate
            
            	The candidate configuration is the config source
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: config
            
            	Inline Config content\: <config> element.  Represents an entire configuration datastore, not a subset of the running datastore
            	**type**\:  anyxml
            
            .. attribute:: running
            
            	The running configuration is the config source
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: startup
            
            	The startup configuration is the config source
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: url
            
            	The URL\-based configuration is the config source
            	**type**\:  str
            
            

            """

            _prefix = 'nc'
            _revision = '2011-06-01'

            def __init__(self):
                super(CopyConfig.Input.Source, self).__init__()

                self.yang_name = "source"
                self.yang_parent_name = "input"

                self.candidate = YLeaf(YType.empty, "candidate")

                self.config = YLeaf(YType.str, "config")

                self.running = YLeaf(YType.empty, "running")

                self.startup = YLeaf(YType.empty, "startup")

                self.url = YLeaf(YType.str, "url")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("candidate",
                                "config",
                                "running",
                                "startup",
                                "url") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CopyConfig.Input.Source, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CopyConfig.Input.Source, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.candidate.is_set or
                    self.config.is_set or
                    self.running.is_set or
                    self.startup.is_set or
                    self.url.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.candidate.yfilter != YFilter.not_set or
                    self.config.yfilter != YFilter.not_set or
                    self.running.yfilter != YFilter.not_set or
                    self.startup.yfilter != YFilter.not_set or
                    self.url.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "source" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "ietf-netconf:copy-config/input/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.candidate.is_set or self.candidate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.candidate.get_name_leafdata())
                if (self.config.is_set or self.config.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.config.get_name_leafdata())
                if (self.running.is_set or self.running.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.running.get_name_leafdata())
                if (self.startup.is_set or self.startup.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.startup.get_name_leafdata())
                if (self.url.is_set or self.url.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.url.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "candidate" or name == "config" or name == "running" or name == "startup" or name == "url"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "candidate"):
                    self.candidate = value
                    self.candidate.value_namespace = name_space
                    self.candidate.value_namespace_prefix = name_space_prefix
                if(value_path == "config"):
                    self.config = value
                    self.config.value_namespace = name_space
                    self.config.value_namespace_prefix = name_space_prefix
                if(value_path == "running"):
                    self.running = value
                    self.running.value_namespace = name_space
                    self.running.value_namespace_prefix = name_space_prefix
                if(value_path == "startup"):
                    self.startup = value
                    self.startup.value_namespace = name_space
                    self.startup.value_namespace_prefix = name_space_prefix
                if(value_path == "url"):
                    self.url = value
                    self.url.value_namespace = name_space
                    self.url.value_namespace_prefix = name_space_prefix

        def has_data(self):
            return (
                self.with_defaults.is_set or
                (self.source is not None and self.source.has_data()) or
                (self.target is not None and self.target.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.with_defaults.yfilter != YFilter.not_set or
                (self.source is not None and self.source.has_operation()) or
                (self.target is not None and self.target.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "ietf-netconf:copy-config/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.with_defaults.is_set or self.with_defaults.yfilter != YFilter.not_set):
                leaf_name_data.append(self.with_defaults.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "source"):
                if (self.source is None):
                    self.source = CopyConfig.Input.Source()
                    self.source.parent = self
                    self._children_name_map["source"] = "source"
                return self.source

            if (child_yang_name == "target"):
                if (self.target is None):
                    self.target = CopyConfig.Input.Target()
                    self.target.parent = self
                    self._children_name_map["target"] = "target"
                return self.target

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "source" or name == "target" or name == "with-defaults"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "with-defaults"):
                self.with_defaults = value
                self.with_defaults.value_namespace = name_space
                self.with_defaults.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.input is not None and self.input.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "ietf-netconf:copy-config" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "input"):
            if (self.input is None):
                self.input = CopyConfig.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "input"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CopyConfig()
        return self._top_entity

class DeleteConfig(Entity):
    """
    Delete a configuration datastore.
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.ietf.ietf_netconf.DeleteConfig.Input>`
    
    

    """

    _prefix = 'nc'
    _revision = '2011-06-01'

    def __init__(self):
        super(DeleteConfig, self).__init__()
        self._top_entity = None

        self.yang_name = "delete-config"
        self.yang_parent_name = "ietf-netconf"

        self.input = DeleteConfig.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")


    class Input(Entity):
        """
        
        
        .. attribute:: target
        
        	Particular configuration to delete
        	**type**\:   :py:class:`Target <ydk.models.ietf.ietf_netconf.DeleteConfig.Input.Target>`
        
        

        """

        _prefix = 'nc'
        _revision = '2011-06-01'

        def __init__(self):
            super(DeleteConfig.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "delete-config"

            self.target = DeleteConfig.Input.Target()
            self.target.parent = self
            self._children_name_map["target"] = "target"
            self._children_yang_names.add("target")


        class Target(Entity):
            """
            Particular configuration to delete.
            
            .. attribute:: startup
            
            	The startup configuration is the config target
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: url
            
            	The URL\-based configuration is the config target
            	**type**\:  str
            
            

            """

            _prefix = 'nc'
            _revision = '2011-06-01'

            def __init__(self):
                super(DeleteConfig.Input.Target, self).__init__()

                self.yang_name = "target"
                self.yang_parent_name = "input"

                self.startup = YLeaf(YType.empty, "startup")

                self.url = YLeaf(YType.str, "url")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("startup",
                                "url") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(DeleteConfig.Input.Target, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(DeleteConfig.Input.Target, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.startup.is_set or
                    self.url.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.startup.yfilter != YFilter.not_set or
                    self.url.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "target" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "ietf-netconf:delete-config/input/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.startup.is_set or self.startup.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.startup.get_name_leafdata())
                if (self.url.is_set or self.url.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.url.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "startup" or name == "url"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "startup"):
                    self.startup = value
                    self.startup.value_namespace = name_space
                    self.startup.value_namespace_prefix = name_space_prefix
                if(value_path == "url"):
                    self.url = value
                    self.url.value_namespace = name_space
                    self.url.value_namespace_prefix = name_space_prefix

        def has_data(self):
            return (self.target is not None and self.target.has_data())

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.target is not None and self.target.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "ietf-netconf:delete-config/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "target"):
                if (self.target is None):
                    self.target = DeleteConfig.Input.Target()
                    self.target.parent = self
                    self._children_name_map["target"] = "target"
                return self.target

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "target"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.input is not None and self.input.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "ietf-netconf:delete-config" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "input"):
            if (self.input is None):
                self.input = DeleteConfig.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "input"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = DeleteConfig()
        return self._top_entity

class Lock(Entity):
    """
    The lock operation allows the client to lock the configuration
    system of a device.
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.ietf.ietf_netconf.Lock.Input>`
    
    

    """

    _prefix = 'nc'
    _revision = '2011-06-01'

    def __init__(self):
        super(Lock, self).__init__()
        self._top_entity = None

        self.yang_name = "lock"
        self.yang_parent_name = "ietf-netconf"

        self.input = Lock.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")


    class Input(Entity):
        """
        
        
        .. attribute:: target
        
        	Particular configuration to lock
        	**type**\:   :py:class:`Target <ydk.models.ietf.ietf_netconf.Lock.Input.Target>`
        
        

        """

        _prefix = 'nc'
        _revision = '2011-06-01'

        def __init__(self):
            super(Lock.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "lock"

            self.target = Lock.Input.Target()
            self.target.parent = self
            self._children_name_map["target"] = "target"
            self._children_yang_names.add("target")


        class Target(Entity):
            """
            Particular configuration to lock.
            
            .. attribute:: candidate
            
            	The candidate configuration is the config target
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: running
            
            	The running configuration is the config target
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: startup
            
            	The startup configuration is the config target
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'nc'
            _revision = '2011-06-01'

            def __init__(self):
                super(Lock.Input.Target, self).__init__()

                self.yang_name = "target"
                self.yang_parent_name = "input"

                self.candidate = YLeaf(YType.empty, "candidate")

                self.running = YLeaf(YType.empty, "running")

                self.startup = YLeaf(YType.empty, "startup")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("candidate",
                                "running",
                                "startup") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Lock.Input.Target, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Lock.Input.Target, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.candidate.is_set or
                    self.running.is_set or
                    self.startup.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.candidate.yfilter != YFilter.not_set or
                    self.running.yfilter != YFilter.not_set or
                    self.startup.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "target" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "ietf-netconf:lock/input/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.candidate.is_set or self.candidate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.candidate.get_name_leafdata())
                if (self.running.is_set or self.running.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.running.get_name_leafdata())
                if (self.startup.is_set or self.startup.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.startup.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "candidate" or name == "running" or name == "startup"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "candidate"):
                    self.candidate = value
                    self.candidate.value_namespace = name_space
                    self.candidate.value_namespace_prefix = name_space_prefix
                if(value_path == "running"):
                    self.running = value
                    self.running.value_namespace = name_space
                    self.running.value_namespace_prefix = name_space_prefix
                if(value_path == "startup"):
                    self.startup = value
                    self.startup.value_namespace = name_space
                    self.startup.value_namespace_prefix = name_space_prefix

        def has_data(self):
            return (self.target is not None and self.target.has_data())

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.target is not None and self.target.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "ietf-netconf:lock/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "target"):
                if (self.target is None):
                    self.target = Lock.Input.Target()
                    self.target.parent = self
                    self._children_name_map["target"] = "target"
                return self.target

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "target"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.input is not None and self.input.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "ietf-netconf:lock" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "input"):
            if (self.input is None):
                self.input = Lock.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "input"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Lock()
        return self._top_entity

class Unlock(Entity):
    """
    The unlock operation is used to release a configuration lock,
    previously obtained with the 'lock' operation.
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.ietf.ietf_netconf.Unlock.Input>`
    
    

    """

    _prefix = 'nc'
    _revision = '2011-06-01'

    def __init__(self):
        super(Unlock, self).__init__()
        self._top_entity = None

        self.yang_name = "unlock"
        self.yang_parent_name = "ietf-netconf"

        self.input = Unlock.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")


    class Input(Entity):
        """
        
        
        .. attribute:: target
        
        	Particular configuration to unlock
        	**type**\:   :py:class:`Target <ydk.models.ietf.ietf_netconf.Unlock.Input.Target>`
        
        

        """

        _prefix = 'nc'
        _revision = '2011-06-01'

        def __init__(self):
            super(Unlock.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "unlock"

            self.target = Unlock.Input.Target()
            self.target.parent = self
            self._children_name_map["target"] = "target"
            self._children_yang_names.add("target")


        class Target(Entity):
            """
            Particular configuration to unlock.
            
            .. attribute:: candidate
            
            	The candidate configuration is the config target
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: running
            
            	The running configuration is the config target
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: startup
            
            	The startup configuration is the config target
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'nc'
            _revision = '2011-06-01'

            def __init__(self):
                super(Unlock.Input.Target, self).__init__()

                self.yang_name = "target"
                self.yang_parent_name = "input"

                self.candidate = YLeaf(YType.empty, "candidate")

                self.running = YLeaf(YType.empty, "running")

                self.startup = YLeaf(YType.empty, "startup")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("candidate",
                                "running",
                                "startup") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Unlock.Input.Target, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Unlock.Input.Target, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.candidate.is_set or
                    self.running.is_set or
                    self.startup.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.candidate.yfilter != YFilter.not_set or
                    self.running.yfilter != YFilter.not_set or
                    self.startup.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "target" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "ietf-netconf:unlock/input/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.candidate.is_set or self.candidate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.candidate.get_name_leafdata())
                if (self.running.is_set or self.running.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.running.get_name_leafdata())
                if (self.startup.is_set or self.startup.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.startup.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "candidate" or name == "running" or name == "startup"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "candidate"):
                    self.candidate = value
                    self.candidate.value_namespace = name_space
                    self.candidate.value_namespace_prefix = name_space_prefix
                if(value_path == "running"):
                    self.running = value
                    self.running.value_namespace = name_space
                    self.running.value_namespace_prefix = name_space_prefix
                if(value_path == "startup"):
                    self.startup = value
                    self.startup.value_namespace = name_space
                    self.startup.value_namespace_prefix = name_space_prefix

        def has_data(self):
            return (self.target is not None and self.target.has_data())

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.target is not None and self.target.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "ietf-netconf:unlock/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "target"):
                if (self.target is None):
                    self.target = Unlock.Input.Target()
                    self.target.parent = self
                    self._children_name_map["target"] = "target"
                return self.target

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "target"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.input is not None and self.input.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "ietf-netconf:unlock" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "input"):
            if (self.input is None):
                self.input = Unlock.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "input"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Unlock()
        return self._top_entity

class Get(Entity):
    """
    Retrieve running configuration and device state information.
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.ietf.ietf_netconf.Get.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:   :py:class:`Output <ydk.models.ietf.ietf_netconf.Get.Output>`
    
    

    """

    _prefix = 'nc'
    _revision = '2011-06-01'

    def __init__(self):
        super(Get, self).__init__()
        self._top_entity = None

        self.yang_name = "get"
        self.yang_parent_name = "ietf-netconf"

        self.input = Get.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")

        self.output = Get.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._children_yang_names.add("output")


    class Input(Entity):
        """
        
        
        .. attribute:: filter
        
        	This parameter specifies the portion of the system configuration and state data to retrieve
        	**type**\:  anyxml
        
        .. attribute:: with_defaults
        
        	The explicit defaults processing mode requested
        	**type**\:   :py:class:`WithDefaultsMode <ydk.models.ietf.ietf_netconf_with_defaults.WithDefaultsMode>`
        
        

        """

        _prefix = 'nc'
        _revision = '2011-06-01'

        def __init__(self):
            super(Get.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "get"

            self.filter = YLeaf(YType.str, "filter")

            self.with_defaults = YLeaf(YType.enumeration, "ietf-netconf-with-defaults:with-defaults")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("filter",
                            "with_defaults") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Get.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Get.Input, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.filter.is_set or
                self.with_defaults.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.filter.yfilter != YFilter.not_set or
                self.with_defaults.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "ietf-netconf:get/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.filter.is_set or self.filter.yfilter != YFilter.not_set):
                leaf_name_data.append(self.filter.get_name_leafdata())
            if (self.with_defaults.is_set or self.with_defaults.yfilter != YFilter.not_set):
                leaf_name_data.append(self.with_defaults.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "filter" or name == "with-defaults"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "filter"):
                self.filter = value
                self.filter.value_namespace = name_space
                self.filter.value_namespace_prefix = name_space_prefix
            if(value_path == "with-defaults"):
                self.with_defaults = value
                self.with_defaults.value_namespace = name_space
                self.with_defaults.value_namespace_prefix = name_space_prefix


    class Output(Entity):
        """
        
        
        .. attribute:: data
        
        	Copy of the running datastore subset and/or state data that matched the filter criteria (if any). An empty data container indicates that the request did not produce any results
        	**type**\:  anyxml
        
        

        """

        _prefix = 'nc'
        _revision = '2011-06-01'

        def __init__(self):
            super(Get.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "get"

            self.data = YLeaf(YType.str, "data")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("data") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Get.Output, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Get.Output, self).__setattr__(name, value)

        def has_data(self):
            return self.data.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.data.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "output" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "ietf-netconf:get/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.data.is_set or self.data.yfilter != YFilter.not_set):
                leaf_name_data.append(self.data.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "data"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "data"):
                self.data = value
                self.data.value_namespace = name_space
                self.data.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (
            (self.input is not None and self.input.has_data()) or
            (self.output is not None and self.output.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()) or
            (self.output is not None and self.output.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "ietf-netconf:get" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "input"):
            if (self.input is None):
                self.input = Get.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        if (child_yang_name == "output"):
            if (self.output is None):
                self.output = Get.Output()
                self.output.parent = self
                self._children_name_map["output"] = "output"
            return self.output

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "input" or name == "output"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Get()
        return self._top_entity

class CloseSession(Entity):
    """
    Request graceful termination of a NETCONF session.
    
    

    """

    _prefix = 'nc'
    _revision = '2011-06-01'

    def __init__(self):
        super(CloseSession, self).__init__()
        self._top_entity = None

        self.yang_name = "close-session"
        self.yang_parent_name = "ietf-netconf"

    def has_data(self):
        return False

    def has_operation(self):
        return self.yfilter != YFilter.not_set

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "ietf-netconf:close-session" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        return None

    def has_leaf_or_child_of_name(self, name):
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CloseSession()
        return self._top_entity

class KillSession(Entity):
    """
    Force the termination of a NETCONF session.
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.ietf.ietf_netconf.KillSession.Input>`
    
    

    """

    _prefix = 'nc'
    _revision = '2011-06-01'

    def __init__(self):
        super(KillSession, self).__init__()
        self._top_entity = None

        self.yang_name = "kill-session"
        self.yang_parent_name = "ietf-netconf"

        self.input = KillSession.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")


    class Input(Entity):
        """
        
        
        .. attribute:: session_id
        
        	Particular session to kill
        	**type**\:  int
        
        	**range:** 1..4294967295
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'nc'
        _revision = '2011-06-01'

        def __init__(self):
            super(KillSession.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "kill-session"

            self.session_id = YLeaf(YType.uint32, "session-id")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("session_id") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(KillSession.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(KillSession.Input, self).__setattr__(name, value)

        def has_data(self):
            return self.session_id.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.session_id.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "ietf-netconf:kill-session/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.session_id.is_set or self.session_id.yfilter != YFilter.not_set):
                leaf_name_data.append(self.session_id.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "session-id"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "session-id"):
                self.session_id = value
                self.session_id.value_namespace = name_space
                self.session_id.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.input is not None and self.input.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "ietf-netconf:kill-session" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "input"):
            if (self.input is None):
                self.input = KillSession.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "input"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = KillSession()
        return self._top_entity

class Commit(Entity):
    """
    Commit the candidate configuration as the device's new
    current configuration.
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.ietf.ietf_netconf.Commit.Input>`
    
    

    """

    _prefix = 'nc'
    _revision = '2011-06-01'

    def __init__(self):
        super(Commit, self).__init__()
        self._top_entity = None

        self.yang_name = "commit"
        self.yang_parent_name = "ietf-netconf"

        self.input = Commit.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")


    class Input(Entity):
        """
        
        
        .. attribute:: confirm_timeout
        
        	The timeout interval for a confirmed commit
        	**type**\:  int
        
        	**range:** 1..4294967295
        
        	**units**\: seconds
        
        	**default value**\: 600
        
        .. attribute:: confirmed
        
        	Requests a confirmed commit
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: persist
        
        	This parameter is used to make a confirmed commit persistent.  A persistent confirmed commit is not aborted if the NETCONF session terminates.  The only way to abort a persistent confirmed commit is to let the timer expire, or to use the <cancel\-commit> operation.  The value of this parameter is a token that must be given in the 'persist\-id' parameter of <commit> or <cancel\-commit> operations in order to confirm or cancel the persistent confirmed commit.  The token should be a random string
        	**type**\:  str
        
        .. attribute:: persist_id
        
        	This parameter is given in order to commit a persistent confirmed commit.  The value must be equal to the value given in the 'persist' parameter to the <commit> operation. If it does not match, the operation fails with an 'invalid\-value' error
        	**type**\:  str
        
        

        """

        _prefix = 'nc'
        _revision = '2011-06-01'

        def __init__(self):
            super(Commit.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "commit"

            self.confirm_timeout = YLeaf(YType.uint32, "confirm-timeout")

            self.confirmed = YLeaf(YType.empty, "confirmed")

            self.persist = YLeaf(YType.str, "persist")

            self.persist_id = YLeaf(YType.str, "persist-id")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("confirm_timeout",
                            "confirmed",
                            "persist",
                            "persist_id") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Commit.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Commit.Input, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.confirm_timeout.is_set or
                self.confirmed.is_set or
                self.persist.is_set or
                self.persist_id.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.confirm_timeout.yfilter != YFilter.not_set or
                self.confirmed.yfilter != YFilter.not_set or
                self.persist.yfilter != YFilter.not_set or
                self.persist_id.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "ietf-netconf:commit/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.confirm_timeout.is_set or self.confirm_timeout.yfilter != YFilter.not_set):
                leaf_name_data.append(self.confirm_timeout.get_name_leafdata())
            if (self.confirmed.is_set or self.confirmed.yfilter != YFilter.not_set):
                leaf_name_data.append(self.confirmed.get_name_leafdata())
            if (self.persist.is_set or self.persist.yfilter != YFilter.not_set):
                leaf_name_data.append(self.persist.get_name_leafdata())
            if (self.persist_id.is_set or self.persist_id.yfilter != YFilter.not_set):
                leaf_name_data.append(self.persist_id.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "confirm-timeout" or name == "confirmed" or name == "persist" or name == "persist-id"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "confirm-timeout"):
                self.confirm_timeout = value
                self.confirm_timeout.value_namespace = name_space
                self.confirm_timeout.value_namespace_prefix = name_space_prefix
            if(value_path == "confirmed"):
                self.confirmed = value
                self.confirmed.value_namespace = name_space
                self.confirmed.value_namespace_prefix = name_space_prefix
            if(value_path == "persist"):
                self.persist = value
                self.persist.value_namespace = name_space
                self.persist.value_namespace_prefix = name_space_prefix
            if(value_path == "persist-id"):
                self.persist_id = value
                self.persist_id.value_namespace = name_space
                self.persist_id.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.input is not None and self.input.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "ietf-netconf:commit" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "input"):
            if (self.input is None):
                self.input = Commit.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "input"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Commit()
        return self._top_entity

class DiscardChanges(Entity):
    """
    Revert the candidate configuration to the current
    running configuration.
    
    

    """

    _prefix = 'nc'
    _revision = '2011-06-01'

    def __init__(self):
        super(DiscardChanges, self).__init__()
        self._top_entity = None

        self.yang_name = "discard-changes"
        self.yang_parent_name = "ietf-netconf"

    def has_data(self):
        return False

    def has_operation(self):
        return self.yfilter != YFilter.not_set

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "ietf-netconf:discard-changes" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        return None

    def has_leaf_or_child_of_name(self, name):
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = DiscardChanges()
        return self._top_entity

class CancelCommit(Entity):
    """
    This operation is used to cancel an ongoing confirmed commit.
    If the confirmed commit is persistent, the parameter
    'persist\-id' must be given, and it must match the value of the
    'persist' parameter.
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.ietf.ietf_netconf.CancelCommit.Input>`
    
    

    """

    _prefix = 'nc'
    _revision = '2011-06-01'

    def __init__(self):
        super(CancelCommit, self).__init__()
        self._top_entity = None

        self.yang_name = "cancel-commit"
        self.yang_parent_name = "ietf-netconf"

        self.input = CancelCommit.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")


    class Input(Entity):
        """
        
        
        .. attribute:: persist_id
        
        	This parameter is given in order to cancel a persistent confirmed commit.  The value must be equal to the value given in the 'persist' parameter to the <commit> operation. If it does not match, the operation fails with an 'invalid\-value' error
        	**type**\:  str
        
        

        """

        _prefix = 'nc'
        _revision = '2011-06-01'

        def __init__(self):
            super(CancelCommit.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "cancel-commit"

            self.persist_id = YLeaf(YType.str, "persist-id")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("persist_id") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CancelCommit.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CancelCommit.Input, self).__setattr__(name, value)

        def has_data(self):
            return self.persist_id.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.persist_id.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "ietf-netconf:cancel-commit/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.persist_id.is_set or self.persist_id.yfilter != YFilter.not_set):
                leaf_name_data.append(self.persist_id.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "persist-id"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "persist-id"):
                self.persist_id = value
                self.persist_id.value_namespace = name_space
                self.persist_id.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.input is not None and self.input.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "ietf-netconf:cancel-commit" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "input"):
            if (self.input is None):
                self.input = CancelCommit.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "input"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CancelCommit()
        return self._top_entity

class Validate(Entity):
    """
    Validates the contents of the specified configuration.
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.ietf.ietf_netconf.Validate.Input>`
    
    

    """

    _prefix = 'nc'
    _revision = '2011-06-01'

    def __init__(self):
        super(Validate, self).__init__()
        self._top_entity = None

        self.yang_name = "validate"
        self.yang_parent_name = "ietf-netconf"

        self.input = Validate.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")


    class Input(Entity):
        """
        
        
        .. attribute:: source
        
        	Particular configuration to validate
        	**type**\:   :py:class:`Source <ydk.models.ietf.ietf_netconf.Validate.Input.Source>`
        
        

        """

        _prefix = 'nc'
        _revision = '2011-06-01'

        def __init__(self):
            super(Validate.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "validate"

            self.source = Validate.Input.Source()
            self.source.parent = self
            self._children_name_map["source"] = "source"
            self._children_yang_names.add("source")


        class Source(Entity):
            """
            Particular configuration to validate.
            
            .. attribute:: candidate
            
            	The candidate configuration is the config source
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: config
            
            	Inline Config content\: <config> element.  Represents an entire configuration datastore, not a subset of the running datastore
            	**type**\:  anyxml
            
            .. attribute:: running
            
            	The running configuration is the config source
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: startup
            
            	The startup configuration is the config source
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: url
            
            	The URL\-based configuration is the config source
            	**type**\:  str
            
            

            """

            _prefix = 'nc'
            _revision = '2011-06-01'

            def __init__(self):
                super(Validate.Input.Source, self).__init__()

                self.yang_name = "source"
                self.yang_parent_name = "input"

                self.candidate = YLeaf(YType.empty, "candidate")

                self.config = YLeaf(YType.str, "config")

                self.running = YLeaf(YType.empty, "running")

                self.startup = YLeaf(YType.empty, "startup")

                self.url = YLeaf(YType.str, "url")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("candidate",
                                "config",
                                "running",
                                "startup",
                                "url") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Validate.Input.Source, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Validate.Input.Source, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.candidate.is_set or
                    self.config.is_set or
                    self.running.is_set or
                    self.startup.is_set or
                    self.url.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.candidate.yfilter != YFilter.not_set or
                    self.config.yfilter != YFilter.not_set or
                    self.running.yfilter != YFilter.not_set or
                    self.startup.yfilter != YFilter.not_set or
                    self.url.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "source" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "ietf-netconf:validate/input/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.candidate.is_set or self.candidate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.candidate.get_name_leafdata())
                if (self.config.is_set or self.config.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.config.get_name_leafdata())
                if (self.running.is_set or self.running.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.running.get_name_leafdata())
                if (self.startup.is_set or self.startup.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.startup.get_name_leafdata())
                if (self.url.is_set or self.url.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.url.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "candidate" or name == "config" or name == "running" or name == "startup" or name == "url"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "candidate"):
                    self.candidate = value
                    self.candidate.value_namespace = name_space
                    self.candidate.value_namespace_prefix = name_space_prefix
                if(value_path == "config"):
                    self.config = value
                    self.config.value_namespace = name_space
                    self.config.value_namespace_prefix = name_space_prefix
                if(value_path == "running"):
                    self.running = value
                    self.running.value_namespace = name_space
                    self.running.value_namespace_prefix = name_space_prefix
                if(value_path == "startup"):
                    self.startup = value
                    self.startup.value_namespace = name_space
                    self.startup.value_namespace_prefix = name_space_prefix
                if(value_path == "url"):
                    self.url = value
                    self.url.value_namespace = name_space
                    self.url.value_namespace_prefix = name_space_prefix

        def has_data(self):
            return (self.source is not None and self.source.has_data())

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.source is not None and self.source.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "ietf-netconf:validate/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "source"):
                if (self.source is None):
                    self.source = Validate.Input.Source()
                    self.source.parent = self
                    self._children_name_map["source"] = "source"
                return self.source

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "source"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.input is not None and self.input.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "ietf-netconf:validate" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "input"):
            if (self.input is None):
                self.input = Validate.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "input"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Validate()
        return self._top_entity

