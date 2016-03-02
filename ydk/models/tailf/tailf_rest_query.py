""" tailf_rest_query 

This module defines the structure of the query interface for REST.

It is an internal module, not exported over any other northbound
interface.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class ResultType_Enum(Enum):
    """
    ResultType_Enum

    """

    """

    Return the result of evaluating the expression as if it
    was surrounded by a call to the xpath function string().

    """
    STRING = 0

    """

    If the result is a node set, return the path to the
    first node in the node set as an instance\-identifier.
    
    If the result is not a node set, nothing is returned
    for this expression.

    """
    PATH = 1

    """

    If the result is a node set, return the value of the
    first node in the node set, if the first node is a leaf.
    Otherwise, nothing is returned for this expression.

    """
    LEAF_VALUE = 2


    @staticmethod
    def _meta_info():
        from ydk.models.tailf._meta import _tailf_rest_query as meta
        return meta._meta_table['ResultType_Enum']



class FetchQueryResult(object):
    """
    Request return data from an XPath Query by POSTing to /api/query,
    where the body contains the 'fetch\-query\-result' container.  On
    success, a 'query\-result' will be returned.
    
    .. attribute:: query_handle
    
    	Query handle, as returned from 'start\-query'
    	**type**\: int
    
    	**range:** 0..4294967295
    
    

    This class is a :ref:`presence class<presence-class>`

    """

    _prefix = 'tfrestq'
    _revision = '2014-06-30'

    def __init__(self):
        self.query_handle = None

    @property
    def _common_path(self):

        return '/tailf-rest-query:fetch-query-result'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.query_handle is not None:
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return True

    @staticmethod
    def _meta_info():
        from ydk.models.tailf._meta import _tailf_rest_query as meta
        return meta._meta_table['FetchQueryResult']['meta_info']


class QueryResult(object):
    """
    REPLY\: to fetch\-query\-result
    
    Fetch (more) data, resulting from the query.
    
    .. attribute:: result
    
    	There will be one result for each node in the node set produced by evaluating the 'foreach' expression
    	**type**\: list of :py:class:`Result <ydk.models.tailf.tailf_rest_query.QueryResult.Result>`
    
    

    This class is a :ref:`presence class<presence-class>`

    """

    _prefix = 'tfrestq'
    _revision = '2014-06-30'

    def __init__(self):
        self.result = YList()
        self.result.parent = self
        self.result.name = 'result'


    class Result(object):
        """
        There will be one result for each node in the node set
        produced by evaluating the 'foreach' expression.
        
        .. attribute:: no_more_data
        
        	Present if no more data is available
        	**type**\: :py:class:`Empty <ydk.types.Empty>`
        
        .. attribute:: select
        
        	A list of data according to what was specified in the corresponding select of the start\-query request
        	**type**\: list of :py:class:`Select <ydk.models.tailf.tailf_rest_query.QueryResult.Result.Select>`
        
        

        """

        _prefix = 'tfrestq'
        _revision = '2014-06-30'

        def __init__(self):
            self.parent = None
            self.no_more_data = None
            self.select = YList()
            self.select.parent = self
            self.select.name = 'select'


        class Select(object):
            """
            A list of data according to what was specified in the
            corresponding select of the start\-query request.
            
            .. attribute:: label
            
            	Present if the label was given in the start\-query select entry
            	**type**\: str
            
            .. attribute:: path
            
            	
            	**type**\: str
            
            .. attribute:: value
            
            	
            	**type**\: str
            
            

            """

            _prefix = 'tfrestq'
            _revision = '2014-06-30'

            def __init__(self):
                self.parent = None
                self.label = None
                self.path = None
                self.value = None

            @property
            def _common_path(self):

                return '/tailf-rest-query:query-result/tailf-rest-query:result/tailf-rest-query:select'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.label is not None:
                    return True

                if self.path is not None:
                    return True

                if self.value is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.tailf._meta import _tailf_rest_query as meta
                return meta._meta_table['QueryResult.Result.Select']['meta_info']

        @property
        def _common_path(self):

            return '/tailf-rest-query:query-result/tailf-rest-query:result'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.no_more_data is not None:
                return True

            if self.select is not None:
                for child_ref in self.select:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.tailf._meta import _tailf_rest_query as meta
            return meta._meta_table['QueryResult.Result']['meta_info']

    @property
    def _common_path(self):

        return '/tailf-rest-query:query-result'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.result is not None:
            for child_ref in self.result:
                if child_ref._has_data():
                    return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return True

    @staticmethod
    def _meta_info():
        from ydk.models.tailf._meta import _tailf_rest_query as meta
        return meta._meta_table['QueryResult']['meta_info']


class ResetQuery(object):
    """
    Reset an existing query by POSTing to /api/query, where the body
    contains a 'reset\-query' container.
    
    The next fetch\-query\-result will retrieve the given chunk of
    data again.
    
    .. attribute:: offset
    
    	Define which 'result' entry to be returned
    	**type**\: int
    
    	**range:** 1..4294967295
    
    .. attribute:: query_handle
    
    	Query handle, as returned from 'start\-query'
    	**type**\: int
    
    	**range:** 0..4294967295
    
    

    This class is a :ref:`presence class<presence-class>`

    """

    _prefix = 'tfrestq'
    _revision = '2014-06-30'

    def __init__(self):
        self.offset = None
        self.query_handle = None

    @property
    def _common_path(self):

        return '/tailf-rest-query:reset-query'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.offset is not None:
            return True

        if self.query_handle is not None:
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return True

    @staticmethod
    def _meta_info():
        from ydk.models.tailf._meta import _tailf_rest_query as meta
        return meta._meta_table['ResetQuery']['meta_info']


class StartQuery(object):
    """
    Start an XPath Query by POSTing to /api/query, where the
    body contains the 'start\-query' container.  On success,
    a 'start\-query\-result' will be returned with a handle to
    the query.
    
    .. attribute:: foreach
    
    	An XPath 1.0 expression that returns a node set.  For each node in this node set, a 'result' entry is constructed.  For each such node all 'select/expression's are evaluated, and stored in 'result/select'.  The resulting entries are returned from the 'fetch\-query\-result' operation.  When evaluating this expression, the context node is the root node of the requested data store
    	**type**\: str
    
    .. attribute:: limit
    
    	The maximum number of 'result' entries to return in each call to 'fetch\-query\-result'.  If this parameter is not given, all entries are returned
    	**type**\: int
    
    	**range:** 1..4294967295
    
    .. attribute:: offset
    
    	Define which 'result' entry to be returned
    	**type**\: int
    
    	**range:** 1..4294967295
    
    .. attribute:: select
    
    	Declare what parts of the result you want to get back and in what form it should be represented
    	**type**\: list of :py:class:`Select <ydk.models.tailf.tailf_rest_query.StartQuery.Select>`
    
    .. attribute:: sort_by
    
    	It is possible to sort the result using an ordered list of XPath expressions.  For each node in the node set returned by 'foreach', all 'sort\-by' expressions are evaluated, in order, with the node from the 'foreach' evaluation as context node, and the result is stored in a tuple.  Thus, this tuple has as many elements as entries in the 'sort\-by' leaf list.  Each expression should return a node set where the first node should be a leaf.  The value of this leaf is used in the tuple.  If the expression returns something else, the value in the tuple is undefined.  When the 'result' list is fetched, is is sorted according to the associated tuple
    	**type**\: list of str
    
    

    This class is a :ref:`presence class<presence-class>`

    """

    _prefix = 'tfrestq'
    _revision = '2014-06-30'

    def __init__(self):
        self.foreach = None
        self.limit = None
        self.offset = None
        self.select = YList()
        self.select.parent = self
        self.select.name = 'select'
        self.sort_by = []


    class Select(object):
        """
        Declare what parts of the result you want to get back
        and in what form it should be represented.
        
        .. attribute:: expression
        
        	Declare what element(s) you want to retrieve
        	**type**\: str
        
        .. attribute:: label
        
        	Optional label which is copied as is to the 'result' list; can be used for easy labeling of the returned element
        	**type**\: str
        
        .. attribute:: result_type
        
        	Declare in what form(s) the returned elements should be represented as
        	**type**\: list of :py:class:`ResultType_Enum <ydk.models.tailf.tailf_rest_query.ResultType_Enum>`
        
        

        """

        _prefix = 'tfrestq'
        _revision = '2014-06-30'

        def __init__(self):
            self.parent = None
            self.expression = None
            self.label = None
            self.result_type = []

        @property
        def _common_path(self):

            return '/tailf-rest-query:start-query/tailf-rest-query:select'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.expression is not None:
                return True

            if self.label is not None:
                return True

            if self.result_type is not None:
                for child in self.result_type:
                    if child is not None:
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.tailf._meta import _tailf_rest_query as meta
            return meta._meta_table['StartQuery.Select']['meta_info']

    @property
    def _common_path(self):

        return '/tailf-rest-query:start-query'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.foreach is not None:
            return True

        if self.limit is not None:
            return True

        if self.offset is not None:
            return True

        if self.select is not None:
            for child_ref in self.select:
                if child_ref._has_data():
                    return True

        if self.sort_by is not None:
            for child in self.sort_by:
                if child is not None:
                    return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return True

    @staticmethod
    def _meta_info():
        from ydk.models.tailf._meta import _tailf_rest_query as meta
        return meta._meta_table['StartQuery']['meta_info']


class StartQueryResult(object):
    """
    REPLY\: to start\-query
    
    Format of the returned answer from a start\-query request.
    The returned query\-handle is used in any succeeding
    use of the fetch\-query\-result request.
    
    .. attribute:: query_handle
    
    	Query handle to be used in succeeding requests
    	**type**\: int
    
    	**range:** 0..4294967295
    
    

    This class is a :ref:`presence class<presence-class>`

    """

    _prefix = 'tfrestq'
    _revision = '2014-06-30'

    def __init__(self):
        self.query_handle = None

    @property
    def _common_path(self):

        return '/tailf-rest-query:start-query-result'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.query_handle is not None:
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return True

    @staticmethod
    def _meta_info():
        from ydk.models.tailf._meta import _tailf_rest_query as meta
        return meta._meta_table['StartQueryResult']['meta_info']


class StopQuery(object):
    """
    Stop the query.
    
    .. attribute:: query_handle
    
    	Query handle, as returned from 'start\-query'
    	**type**\: int
    
    	**range:** 0..4294967295
    
    

    This class is a :ref:`presence class<presence-class>`

    """

    _prefix = 'tfrestq'
    _revision = '2014-06-30'

    def __init__(self):
        self.query_handle = None

    @property
    def _common_path(self):

        return '/tailf-rest-query:stop-query'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.query_handle is not None:
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return True

    @staticmethod
    def _meta_info():
        from ydk.models.tailf._meta import _tailf_rest_query as meta
        return meta._meta_table['StopQuery']['meta_info']


