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
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class StartQuery(Entity):
    """
    
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xe.tailf_netconf_query.StartQuery.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xe.tailf_netconf_query.StartQuery.Output>`
    
    

    """

    _prefix = 'tfncq'
    _revision = '2014-11-13'

    def __init__(self):
        super(StartQuery, self).__init__()
        self._top_entity = None

        self.yang_name = "start-query"
        self.yang_parent_name = "tailf-netconf-query"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = StartQuery.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")

        self.output = StartQuery.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._children_yang_names.add("output")
        self._segment_path = lambda: "tailf-netconf-query:start-query"


    class Input(Entity):
        """
        
        
        .. attribute:: foreach
        
        	An XPath 1.0 expression that returns a node set.  For each node in this node set, a 'result' entry is constructed.  For each such node all 'select/expression's are evaluated, and stored in 'result/select'.  The resulting entries are returned from the 'fetch\-query\-result' function.  When this XPath expression is evaluated, the context node is the root node of the requested data store
        	**type**\: str
        
        	**mandatory**\: True
        
        .. attribute:: select
        
        	A list of expressions that define what to return from each node in the node set returned by the 'foreach' expression
        	**type**\: list of  		 :py:class:`Select <ydk.models.cisco_ios_xe.tailf_netconf_query.StartQuery.Input.Select>`
        
        .. attribute:: sort_by
        
        	It is possible to sort the result using an ordered list of XPath expressions.  For each node in the node set returned by 'foreach', all 'sort\-by' expressions are evaluated, in order, with the node from the 'foreach' evaluation as context node, and the result is stored in a tuple.  Thus, this tuple has as many elements as entries in the 'sort\-by' leaf list.  Each expression should return a node set where the first node should be a leaf.  The value of this leaf is used in the tuple.  If the expression returns something else, the value in the tuple is undefined.  When the 'result' list is fetched, is is sorted according to the associated tuple
        	**type**\: list of str
        
        .. attribute:: limit
        
        	The maximum number of 'result' entries to return in each call to 'fetch\-query\-result'.  If this parameter is not given, all entries are returned
        	**type**\: int
        
        	**range:** 1..4294967295
        
        .. attribute:: offset
        
        	
        	**type**\: int
        
        	**range:** 1..4294967295
        
        	**default value**\: 1
        
        .. attribute:: timeout
        
        	The maximum time (in seconds) before a query times out. Resets every new request, i.e. subsequent function calls starts a new timeout timer
        	**type**\: int
        
        	**range:** 1..4294967295
        
        	**default value**\: 600
        
        

        """

        _prefix = 'tfncq'
        _revision = '2014-11-13'

        def __init__(self):
            super(StartQuery.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "start-query"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("select", ("select", StartQuery.Input.Select))])
            self._leafs = OrderedDict([
                ('foreach', YLeaf(YType.str, 'foreach')),
                ('sort_by', YLeafList(YType.str, 'sort-by')),
                ('limit', YLeaf(YType.uint32, 'limit')),
                ('offset', YLeaf(YType.uint32, 'offset')),
                ('timeout', YLeaf(YType.uint32, 'timeout')),
            ])
            self.foreach = None
            self.sort_by = []
            self.limit = None
            self.offset = None
            self.timeout = None

            self.select = YList(self)
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "tailf-netconf-query:start-query/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(StartQuery.Input, ['foreach', 'sort_by', 'limit', 'offset', 'timeout'], name, value)


        class Select(Entity):
            """
            A list of expressions that define what to return from each
            node in the node set returned by the 'foreach' expression.
            
            .. attribute:: label
            
            	Optional label which is copied as is to the 'result' list; can be used for easy labeling of the returned node(s)
            	**type**\: str
            
            .. attribute:: expression
            
            	Declare what node(s) you want to retrieve.  This XPath expression is evaluated once for every node in the node set returned by the 'foreach' expression.  That node is the inital context node when this expression is evaluated
            	**type**\: str
            
            	**mandatory**\: True
            
            .. attribute:: result_type
            
            	Controls how the result of the select expression is returned in 'fetch\-query\-result'
            	**type**\: list of   :py:class:`ResultType <ydk.models.cisco_ios_xe.tailf_netconf_query.StartQuery.Input.Select.ResultType>`
            
            

            """

            _prefix = 'tfncq'
            _revision = '2014-11-13'

            def __init__(self):
                super(StartQuery.Input.Select, self).__init__()

                self.yang_name = "select"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('label', YLeaf(YType.str, 'label')),
                    ('expression', YLeaf(YType.str, 'expression')),
                    ('result_type', YLeafList(YType.enumeration, 'result-type')),
                ])
                self.label = None
                self.expression = None
                self.result_type = []
                self._segment_path = lambda: "select"
                self._absolute_path = lambda: "tailf-netconf-query:start-query/input/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(StartQuery.Input.Select, ['label', 'expression', 'result_type'], name, value)

            class ResultType(Enum):
                """
                ResultType (Enum Class)

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



    class Output(Entity):
        """
        
        
        .. attribute:: query_handle
        
        	
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'tfncq'
        _revision = '2014-11-13'

        def __init__(self):
            super(StartQuery.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "start-query"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('query_handle', YLeaf(YType.uint32, 'query-handle')),
            ])
            self.query_handle = None
            self._segment_path = lambda: "output"
            self._absolute_path = lambda: "tailf-netconf-query:start-query/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(StartQuery.Output, ['query_handle'], name, value)

    def clone_ptr(self):
        self._top_entity = StartQuery()
        return self._top_entity

class FetchQueryResult(Entity):
    """
    
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xe.tailf_netconf_query.FetchQueryResult.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xe.tailf_netconf_query.FetchQueryResult.Output>`
    
    

    """

    _prefix = 'tfncq'
    _revision = '2014-11-13'

    def __init__(self):
        super(FetchQueryResult, self).__init__()
        self._top_entity = None

        self.yang_name = "fetch-query-result"
        self.yang_parent_name = "tailf-netconf-query"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = FetchQueryResult.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")

        self.output = FetchQueryResult.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._children_yang_names.add("output")
        self._segment_path = lambda: "tailf-netconf-query:fetch-query-result"


    class Input(Entity):
        """
        
        
        .. attribute:: query_handle
        
        	
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'tfncq'
        _revision = '2014-11-13'

        def __init__(self):
            super(FetchQueryResult.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "fetch-query-result"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('query_handle', YLeaf(YType.uint32, 'query-handle')),
            ])
            self.query_handle = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "tailf-netconf-query:fetch-query-result/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(FetchQueryResult.Input, ['query_handle'], name, value)


    class Output(Entity):
        """
        
        
        .. attribute:: query_result
        
        	
        	**type**\:  :py:class:`QueryResult <ydk.models.cisco_ios_xe.tailf_netconf_query.FetchQueryResult.Output.QueryResult>`
        
        

        """

        _prefix = 'tfncq'
        _revision = '2014-11-13'

        def __init__(self):
            super(FetchQueryResult.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "fetch-query-result"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([("query-result", ("query_result", FetchQueryResult.Output.QueryResult))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict()

            self.query_result = FetchQueryResult.Output.QueryResult()
            self.query_result.parent = self
            self._children_name_map["query_result"] = "query-result"
            self._children_yang_names.add("query-result")
            self._segment_path = lambda: "output"
            self._absolute_path = lambda: "tailf-netconf-query:fetch-query-result/%s" % self._segment_path()


        class QueryResult(Entity):
            """
            
            
            .. attribute:: result
            
            	There will be one result for each node in the node set produced by evaluating the 'foreach' expression
            	**type**\: list of  		 :py:class:`Result <ydk.models.cisco_ios_xe.tailf_netconf_query.FetchQueryResult.Output.QueryResult.Result>`
            
            

            """

            _prefix = 'tfncq'
            _revision = '2014-11-13'

            def __init__(self):
                super(FetchQueryResult.Output.QueryResult, self).__init__()

                self.yang_name = "query-result"
                self.yang_parent_name = "output"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("result", ("result", FetchQueryResult.Output.QueryResult.Result))])
                self._leafs = OrderedDict()

                self.result = YList(self)
                self._segment_path = lambda: "query-result"
                self._absolute_path = lambda: "tailf-netconf-query:fetch-query-result/output/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(FetchQueryResult.Output.QueryResult, [], name, value)


            class Result(Entity):
                """
                There will be one result for each node in the node set
                produced by evaluating the 'foreach' expression.
                
                .. attribute:: select
                
                	
                	**type**\: list of  		 :py:class:`Select <ydk.models.cisco_ios_xe.tailf_netconf_query.FetchQueryResult.Output.QueryResult.Result.Select>`
                
                

                """

                _prefix = 'tfncq'
                _revision = '2014-11-13'

                def __init__(self):
                    super(FetchQueryResult.Output.QueryResult.Result, self).__init__()

                    self.yang_name = "result"
                    self.yang_parent_name = "query-result"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("select", ("select", FetchQueryResult.Output.QueryResult.Result.Select))])
                    self._leafs = OrderedDict()

                    self.select = YList(self)
                    self._segment_path = lambda: "result"
                    self._absolute_path = lambda: "tailf-netconf-query:fetch-query-result/output/query-result/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(FetchQueryResult.Output.QueryResult.Result, [], name, value)


                class Select(Entity):
                    """
                    
                    
                    .. attribute:: label
                    
                    	Present if the label was given in the input select entry
                    	**type**\: str
                    
                    .. attribute:: path
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: value
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: data
                    
                    	A deep structure of XML (or other API dependent format, e.g., JSON)
                    	**type**\: anyxml
                    
                    

                    """

                    _prefix = 'tfncq'
                    _revision = '2014-11-13'

                    def __init__(self):
                        super(FetchQueryResult.Output.QueryResult.Result.Select, self).__init__()

                        self.yang_name = "select"
                        self.yang_parent_name = "result"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('label', YLeaf(YType.str, 'label')),
                            ('path', YLeaf(YType.str, 'path')),
                            ('value', YLeaf(YType.str, 'value')),
                            ('data', YLeaf(YType.str, 'data')),
                        ])
                        self.label = None
                        self.path = None
                        self.value = None
                        self.data = None
                        self._segment_path = lambda: "select"
                        self._absolute_path = lambda: "tailf-netconf-query:fetch-query-result/output/query-result/result/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(FetchQueryResult.Output.QueryResult.Result.Select, ['label', 'path', 'value', 'data'], name, value)

    def clone_ptr(self):
        self._top_entity = FetchQueryResult()
        return self._top_entity

class ResetQuery(Entity):
    """
    
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xe.tailf_netconf_query.ResetQuery.Input>`
    
    

    """

    _prefix = 'tfncq'
    _revision = '2014-11-13'

    def __init__(self):
        super(ResetQuery, self).__init__()
        self._top_entity = None

        self.yang_name = "reset-query"
        self.yang_parent_name = "tailf-netconf-query"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = ResetQuery.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")
        self._segment_path = lambda: "tailf-netconf-query:reset-query"


    class Input(Entity):
        """
        
        
        .. attribute:: query_handle
        
        	
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: offset
        
        	
        	**type**\: int
        
        	**range:** 1..4294967295
        
        	**default value**\: 1
        
        .. attribute:: timeout
        
        	The maximum time (in seconds) before a query times out. Resets every new request, i.e. subsequent function calls starts a new timeout timer
        	**type**\: int
        
        	**range:** 1..4294967295
        
        	**default value**\: 600
        
        

        """

        _prefix = 'tfncq'
        _revision = '2014-11-13'

        def __init__(self):
            super(ResetQuery.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "reset-query"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('query_handle', YLeaf(YType.uint32, 'query-handle')),
                ('offset', YLeaf(YType.uint32, 'offset')),
                ('timeout', YLeaf(YType.uint32, 'timeout')),
            ])
            self.query_handle = None
            self.offset = None
            self.timeout = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "tailf-netconf-query:reset-query/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(ResetQuery.Input, ['query_handle', 'offset', 'timeout'], name, value)

    def clone_ptr(self):
        self._top_entity = ResetQuery()
        return self._top_entity

class StopQuery(Entity):
    """
    
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xe.tailf_netconf_query.StopQuery.Input>`
    
    

    """

    _prefix = 'tfncq'
    _revision = '2014-11-13'

    def __init__(self):
        super(StopQuery, self).__init__()
        self._top_entity = None

        self.yang_name = "stop-query"
        self.yang_parent_name = "tailf-netconf-query"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = StopQuery.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")
        self._segment_path = lambda: "tailf-netconf-query:stop-query"


    class Input(Entity):
        """
        
        
        .. attribute:: query_handle
        
        	
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'tfncq'
        _revision = '2014-11-13'

        def __init__(self):
            super(StopQuery.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "stop-query"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('query_handle', YLeaf(YType.uint32, 'query-handle')),
            ])
            self.query_handle = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "tailf-netconf-query:stop-query/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(StopQuery.Input, ['query_handle'], name, value)

    def clone_ptr(self):
        self._top_entity = StopQuery()
        return self._top_entity

