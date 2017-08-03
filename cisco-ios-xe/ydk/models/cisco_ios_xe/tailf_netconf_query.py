""" tailf_netconf_query 

This module introduces four new rpc operations to run
advanced search queries.

The operation 'start\-query' starts a query, with some search
conditions and control parameters for how to return the results.
This operation returns a query handle, to be used in subsequent
operations.

The operation 'fetch\-query\-result' is repeatedly to get result
chunks from the query evaluation.

The operation 'reset\-query' can be used to restart the query.

Finally 'stop\-query' is used to clean up query resources on the
server.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class StartQuery(Entity):
    """
    
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xe.tailf_netconf_query.StartQuery.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:   :py:class:`Output <ydk.models.cisco_ios_xe.tailf_netconf_query.StartQuery.Output>`
    
    

    """

    _prefix = 'tfncq'
    _revision = '2014-11-13'

    def __init__(self):
        super(StartQuery, self).__init__()
        self._top_entity = None

        self.yang_name = "start-query"
        self.yang_parent_name = "tailf-netconf-query"

        self.input = StartQuery.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")

        self.output = StartQuery.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._children_yang_names.add("output")


    class Input(Entity):
        """
        
        
        .. attribute:: foreach
        
        	An XPath 1.0 expression that returns a node set.  For each node in this node set, a 'result' entry is constructed.  For each such node all 'select/expression's are evaluated, and stored in 'result/select'.  The resulting entries are returned from the 'fetch\-query\-result' function.  When this XPath expression is evaluated, the context node is the root node of the requested data store
        	**type**\:  str
        
        	**mandatory**\: True
        
        .. attribute:: limit
        
        	The maximum number of 'result' entries to return in each call to 'fetch\-query\-result'.  If this parameter is not given, all entries are returned
        	**type**\:  int
        
        	**range:** 1..4294967295
        
        .. attribute:: offset
        
        	
        	**type**\:  int
        
        	**range:** 1..4294967295
        
        	**default value**\: 1
        
        .. attribute:: select
        
        	A list of expressions that define what to return from each node in the node set returned by the 'foreach' expression
        	**type**\: list of    :py:class:`Select <ydk.models.cisco_ios_xe.tailf_netconf_query.StartQuery.Input.Select>`
        
        .. attribute:: sort_by
        
        	It is possible to sort the result using an ordered list of XPath expressions.  For each node in the node set returned by 'foreach', all 'sort\-by' expressions are evaluated, in order, with the node from the 'foreach' evaluation as context node, and the result is stored in a tuple.  Thus, this tuple has as many elements as entries in the 'sort\-by' leaf list.  Each expression should return a node set where the first node should be a leaf.  The value of this leaf is used in the tuple.  If the expression returns something else, the value in the tuple is undefined.  When the 'result' list is fetched, is is sorted according to the associated tuple
        	**type**\:  list of str
        
        

        """

        _prefix = 'tfncq'
        _revision = '2014-11-13'

        def __init__(self):
            super(StartQuery.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "start-query"

            self.foreach = YLeaf(YType.str, "foreach")

            self.limit = YLeaf(YType.uint32, "limit")

            self.offset = YLeaf(YType.uint32, "offset")

            self.sort_by = YLeafList(YType.str, "sort-by")

            self.select = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("foreach",
                            "limit",
                            "offset",
                            "sort_by") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(StartQuery.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(StartQuery.Input, self).__setattr__(name, value)


        class Select(Entity):
            """
            A list of expressions that define what to return from each
            node in the node set returned by the 'foreach' expression.
            
            .. attribute:: expression
            
            	Declare what node(s) you want to retrieve.  This XPath expression is evaluated once for every node in the node set returned by the 'foreach' expression.  That node is the inital context node when this expression is evaluated
            	**type**\:  str
            
            	**mandatory**\: True
            
            .. attribute:: label
            
            	Optional label which is copied as is to the 'result' list; can be used for easy labeling of the returned node(s)
            	**type**\:  str
            
            .. attribute:: result_type
            
            	Controls how the result of the select expression is returned in 'fetch\-query\-result'
            	**type**\:  list of   :py:class:`ResultType <ydk.models.cisco_ios_xe.tailf_netconf_query.StartQuery.Input.Select.ResultType>`
            
            

            """

            _prefix = 'tfncq'
            _revision = '2014-11-13'

            def __init__(self):
                super(StartQuery.Input.Select, self).__init__()

                self.yang_name = "select"
                self.yang_parent_name = "input"

                self.expression = YLeaf(YType.str, "expression")

                self.label = YLeaf(YType.str, "label")

                self.result_type = YLeafList(YType.enumeration, "result-type")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("expression",
                                "label",
                                "result_type") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(StartQuery.Input.Select, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(StartQuery.Input.Select, self).__setattr__(name, value)

            class ResultType(Enum):
                """
                ResultType

                Controls how the result of the select expression is returned

                in 'fetch\-query\-result'.

                .. data:: string = 0

                	Return the result of evaluating the expression as if it

                	was surrounded by a call to the xpath function string().

                .. data:: path = 1

                	If the result is a node set, return the path to the

                	first node in the node set as an instance-identifier.

                	If the result is not a node set, nothing is returned

                	for this expression.

                .. data:: leaf_value = 2

                	If the result is a node set, return the value of the

                	first node in the node set, if the first node is a leaf.

                	Otherwise, nothing is returned for this expression.

                .. data:: inline = 3

                	The result is returned inline, i.e., a deep structure

                	of XML (or other API dependent format, e.g., JSON)

                """

                string = Enum.YLeaf(0, "string")

                path = Enum.YLeaf(1, "path")

                leaf_value = Enum.YLeaf(2, "leaf-value")

                inline = Enum.YLeaf(3, "inline")


            def has_data(self):
                for leaf in self.result_type.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                return (
                    self.expression.is_set or
                    self.label.is_set)

            def has_operation(self):
                for leaf in self.result_type.getYLeafs():
                    if (leaf.is_set):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    self.expression.yfilter != YFilter.not_set or
                    self.label.yfilter != YFilter.not_set or
                    self.result_type.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "select" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "tailf-netconf-query:start-query/input/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.expression.is_set or self.expression.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.expression.get_name_leafdata())
                if (self.label.is_set or self.label.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.label.get_name_leafdata())

                leaf_name_data.extend(self.result_type.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "expression" or name == "label" or name == "result-type"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "expression"):
                    self.expression = value
                    self.expression.value_namespace = name_space
                    self.expression.value_namespace_prefix = name_space_prefix
                if(value_path == "label"):
                    self.label = value
                    self.label.value_namespace = name_space
                    self.label.value_namespace_prefix = name_space_prefix
                if(value_path == "result-type"):
                    self.result_type.append(value)

        def has_data(self):
            for c in self.select:
                if (c.has_data()):
                    return True
            for leaf in self.sort_by.getYLeafs():
                if (leaf.yfilter != YFilter.not_set):
                    return True
            return (
                self.foreach.is_set or
                self.limit.is_set or
                self.offset.is_set)

        def has_operation(self):
            for c in self.select:
                if (c.has_operation()):
                    return True
            for leaf in self.sort_by.getYLeafs():
                if (leaf.is_set):
                    return True
            return (
                self.yfilter != YFilter.not_set or
                self.foreach.yfilter != YFilter.not_set or
                self.limit.yfilter != YFilter.not_set or
                self.offset.yfilter != YFilter.not_set or
                self.sort_by.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "tailf-netconf-query:start-query/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.foreach.is_set or self.foreach.yfilter != YFilter.not_set):
                leaf_name_data.append(self.foreach.get_name_leafdata())
            if (self.limit.is_set or self.limit.yfilter != YFilter.not_set):
                leaf_name_data.append(self.limit.get_name_leafdata())
            if (self.offset.is_set or self.offset.yfilter != YFilter.not_set):
                leaf_name_data.append(self.offset.get_name_leafdata())

            leaf_name_data.extend(self.sort_by.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "select"):
                for c in self.select:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = StartQuery.Input.Select()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.select.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "select" or name == "foreach" or name == "limit" or name == "offset" or name == "sort-by"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "foreach"):
                self.foreach = value
                self.foreach.value_namespace = name_space
                self.foreach.value_namespace_prefix = name_space_prefix
            if(value_path == "limit"):
                self.limit = value
                self.limit.value_namespace = name_space
                self.limit.value_namespace_prefix = name_space_prefix
            if(value_path == "offset"):
                self.offset = value
                self.offset.value_namespace = name_space
                self.offset.value_namespace_prefix = name_space_prefix
            if(value_path == "sort-by"):
                self.sort_by.append(value)


    class Output(Entity):
        """
        
        
        .. attribute:: query_handle
        
        	
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'tfncq'
        _revision = '2014-11-13'

        def __init__(self):
            super(StartQuery.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "start-query"

            self.query_handle = YLeaf(YType.uint32, "query-handle")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("query_handle") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(StartQuery.Output, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(StartQuery.Output, self).__setattr__(name, value)

        def has_data(self):
            return self.query_handle.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.query_handle.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "output" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "tailf-netconf-query:start-query/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.query_handle.is_set or self.query_handle.yfilter != YFilter.not_set):
                leaf_name_data.append(self.query_handle.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "query-handle"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "query-handle"):
                self.query_handle = value
                self.query_handle.value_namespace = name_space
                self.query_handle.value_namespace_prefix = name_space_prefix

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
        path_buffer = "tailf-netconf-query:start-query" + path_buffer

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
                self.input = StartQuery.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        if (child_yang_name == "output"):
            if (self.output is None):
                self.output = StartQuery.Output()
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
        self._top_entity = StartQuery()
        return self._top_entity

class FetchQueryResult(Entity):
    """
    
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xe.tailf_netconf_query.FetchQueryResult.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:   :py:class:`Output <ydk.models.cisco_ios_xe.tailf_netconf_query.FetchQueryResult.Output>`
    
    

    """

    _prefix = 'tfncq'
    _revision = '2014-11-13'

    def __init__(self):
        super(FetchQueryResult, self).__init__()
        self._top_entity = None

        self.yang_name = "fetch-query-result"
        self.yang_parent_name = "tailf-netconf-query"

        self.input = FetchQueryResult.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")

        self.output = FetchQueryResult.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._children_yang_names.add("output")


    class Input(Entity):
        """
        
        
        .. attribute:: query_handle
        
        	
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'tfncq'
        _revision = '2014-11-13'

        def __init__(self):
            super(FetchQueryResult.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "fetch-query-result"

            self.query_handle = YLeaf(YType.uint32, "query-handle")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("query_handle") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(FetchQueryResult.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(FetchQueryResult.Input, self).__setattr__(name, value)

        def has_data(self):
            return self.query_handle.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.query_handle.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "tailf-netconf-query:fetch-query-result/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.query_handle.is_set or self.query_handle.yfilter != YFilter.not_set):
                leaf_name_data.append(self.query_handle.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "query-handle"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "query-handle"):
                self.query_handle = value
                self.query_handle.value_namespace = name_space
                self.query_handle.value_namespace_prefix = name_space_prefix


    class Output(Entity):
        """
        
        
        .. attribute:: query_result
        
        	
        	**type**\:   :py:class:`QueryResult <ydk.models.cisco_ios_xe.tailf_netconf_query.FetchQueryResult.Output.QueryResult>`
        
        

        """

        _prefix = 'tfncq'
        _revision = '2014-11-13'

        def __init__(self):
            super(FetchQueryResult.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "fetch-query-result"

            self.query_result = FetchQueryResult.Output.QueryResult()
            self.query_result.parent = self
            self._children_name_map["query_result"] = "query-result"
            self._children_yang_names.add("query-result")


        class QueryResult(Entity):
            """
            
            
            .. attribute:: result
            
            	There will be one result for each node in the node set produced by evaluating the 'foreach' expression
            	**type**\: list of    :py:class:`Result <ydk.models.cisco_ios_xe.tailf_netconf_query.FetchQueryResult.Output.QueryResult.Result>`
            
            

            """

            _prefix = 'tfncq'
            _revision = '2014-11-13'

            def __init__(self):
                super(FetchQueryResult.Output.QueryResult, self).__init__()

                self.yang_name = "query-result"
                self.yang_parent_name = "output"

                self.result = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in () and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(FetchQueryResult.Output.QueryResult, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(FetchQueryResult.Output.QueryResult, self).__setattr__(name, value)


            class Result(Entity):
                """
                There will be one result for each node in the node set
                produced by evaluating the 'foreach' expression.
                
                .. attribute:: select
                
                	
                	**type**\: list of    :py:class:`Select <ydk.models.cisco_ios_xe.tailf_netconf_query.FetchQueryResult.Output.QueryResult.Result.Select>`
                
                

                """

                _prefix = 'tfncq'
                _revision = '2014-11-13'

                def __init__(self):
                    super(FetchQueryResult.Output.QueryResult.Result, self).__init__()

                    self.yang_name = "result"
                    self.yang_parent_name = "query-result"

                    self.select = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in () and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(FetchQueryResult.Output.QueryResult.Result, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(FetchQueryResult.Output.QueryResult.Result, self).__setattr__(name, value)


                class Select(Entity):
                    """
                    
                    
                    .. attribute:: data
                    
                    	A deep structure of XML (or other API dependent format, e.g., JSON)
                    	**type**\:  anyxml
                    
                    .. attribute:: label
                    
                    	Present if the label was given in the input select entry
                    	**type**\:  str
                    
                    .. attribute:: path
                    
                    	
                    	**type**\:  str
                    
                    .. attribute:: value
                    
                    	
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'tfncq'
                    _revision = '2014-11-13'

                    def __init__(self):
                        super(FetchQueryResult.Output.QueryResult.Result.Select, self).__init__()

                        self.yang_name = "select"
                        self.yang_parent_name = "result"

                        self.data = YLeaf(YType.str, "data")

                        self.label = YLeaf(YType.str, "label")

                        self.path = YLeaf(YType.str, "path")

                        self.value = YLeaf(YType.str, "value")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("data",
                                        "label",
                                        "path",
                                        "value") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(FetchQueryResult.Output.QueryResult.Result.Select, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(FetchQueryResult.Output.QueryResult.Result.Select, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.data.is_set or
                            self.label.is_set or
                            self.path.is_set or
                            self.value.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.data.yfilter != YFilter.not_set or
                            self.label.yfilter != YFilter.not_set or
                            self.path.yfilter != YFilter.not_set or
                            self.value.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "select" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "tailf-netconf-query:fetch-query-result/output/query-result/result/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.data.is_set or self.data.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.data.get_name_leafdata())
                        if (self.label.is_set or self.label.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.label.get_name_leafdata())
                        if (self.path.is_set or self.path.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.path.get_name_leafdata())
                        if (self.value.is_set or self.value.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.value.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "data" or name == "label" or name == "path" or name == "value"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "data"):
                            self.data = value
                            self.data.value_namespace = name_space
                            self.data.value_namespace_prefix = name_space_prefix
                        if(value_path == "label"):
                            self.label = value
                            self.label.value_namespace = name_space
                            self.label.value_namespace_prefix = name_space_prefix
                        if(value_path == "path"):
                            self.path = value
                            self.path.value_namespace = name_space
                            self.path.value_namespace_prefix = name_space_prefix
                        if(value_path == "value"):
                            self.value = value
                            self.value.value_namespace = name_space
                            self.value.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.select:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.select:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "result" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "tailf-netconf-query:fetch-query-result/output/query-result/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "select"):
                        for c in self.select:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = FetchQueryResult.Output.QueryResult.Result.Select()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.select.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "select"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                for c in self.result:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.result:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "query-result" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "tailf-netconf-query:fetch-query-result/output/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "result"):
                    for c in self.result:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = FetchQueryResult.Output.QueryResult.Result()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.result.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "result"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (self.query_result is not None and self.query_result.has_data())

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.query_result is not None and self.query_result.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "output" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "tailf-netconf-query:fetch-query-result/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "query-result"):
                if (self.query_result is None):
                    self.query_result = FetchQueryResult.Output.QueryResult()
                    self.query_result.parent = self
                    self._children_name_map["query_result"] = "query-result"
                return self.query_result

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "query-result"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

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
        path_buffer = "tailf-netconf-query:fetch-query-result" + path_buffer

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
                self.input = FetchQueryResult.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        if (child_yang_name == "output"):
            if (self.output is None):
                self.output = FetchQueryResult.Output()
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
        self._top_entity = FetchQueryResult()
        return self._top_entity

class ResetQuery(Entity):
    """
    
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xe.tailf_netconf_query.ResetQuery.Input>`
    
    

    """

    _prefix = 'tfncq'
    _revision = '2014-11-13'

    def __init__(self):
        super(ResetQuery, self).__init__()
        self._top_entity = None

        self.yang_name = "reset-query"
        self.yang_parent_name = "tailf-netconf-query"

        self.input = ResetQuery.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")


    class Input(Entity):
        """
        
        
        .. attribute:: offset
        
        	
        	**type**\:  int
        
        	**range:** 1..4294967295
        
        	**default value**\: 1
        
        .. attribute:: query_handle
        
        	
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'tfncq'
        _revision = '2014-11-13'

        def __init__(self):
            super(ResetQuery.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "reset-query"

            self.offset = YLeaf(YType.uint32, "offset")

            self.query_handle = YLeaf(YType.uint32, "query-handle")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("offset",
                            "query_handle") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(ResetQuery.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(ResetQuery.Input, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.offset.is_set or
                self.query_handle.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.offset.yfilter != YFilter.not_set or
                self.query_handle.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "tailf-netconf-query:reset-query/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.offset.is_set or self.offset.yfilter != YFilter.not_set):
                leaf_name_data.append(self.offset.get_name_leafdata())
            if (self.query_handle.is_set or self.query_handle.yfilter != YFilter.not_set):
                leaf_name_data.append(self.query_handle.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "offset" or name == "query-handle"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "offset"):
                self.offset = value
                self.offset.value_namespace = name_space
                self.offset.value_namespace_prefix = name_space_prefix
            if(value_path == "query-handle"):
                self.query_handle = value
                self.query_handle.value_namespace = name_space
                self.query_handle.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.input is not None and self.input.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "tailf-netconf-query:reset-query" + path_buffer

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
                self.input = ResetQuery.Input()
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
        self._top_entity = ResetQuery()
        return self._top_entity

class StopQuery(Entity):
    """
    
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xe.tailf_netconf_query.StopQuery.Input>`
    
    

    """

    _prefix = 'tfncq'
    _revision = '2014-11-13'

    def __init__(self):
        super(StopQuery, self).__init__()
        self._top_entity = None

        self.yang_name = "stop-query"
        self.yang_parent_name = "tailf-netconf-query"

        self.input = StopQuery.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")


    class Input(Entity):
        """
        
        
        .. attribute:: query_handle
        
        	
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'tfncq'
        _revision = '2014-11-13'

        def __init__(self):
            super(StopQuery.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "stop-query"

            self.query_handle = YLeaf(YType.uint32, "query-handle")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("query_handle") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(StopQuery.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(StopQuery.Input, self).__setattr__(name, value)

        def has_data(self):
            return self.query_handle.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.query_handle.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "tailf-netconf-query:stop-query/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.query_handle.is_set or self.query_handle.yfilter != YFilter.not_set):
                leaf_name_data.append(self.query_handle.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "query-handle"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "query-handle"):
                self.query_handle = value
                self.query_handle.value_namespace = name_space
                self.query_handle.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.input is not None and self.input.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "tailf-netconf-query:stop-query" + path_buffer

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
                self.input = StopQuery.Input()
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
        self._top_entity = StopQuery()
        return self._top_entity

