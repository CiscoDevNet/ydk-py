


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'ResultType_Enum' : _MetaInfoEnum('ResultType_Enum', 'ydk.models.tailf.tailf_rest_query',
        {
            'string':'STRING',
            'path':'PATH',
            'leaf-value':'LEAF_VALUE',
        }, 'tailf-rest-query', _yang_ns._namespaces['tailf-rest-query']),
    'FetchQueryResult' : {
        'meta_info' : _MetaInfoClass('FetchQueryResult',
            False, 
            [
            _MetaInfoClassMember('query-handle', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Query handle, as returned from 'start-query'
                ''',
                'query_handle',
                'tailf-rest-query', False),
            ],
            'tailf-rest-query',
            'fetch-query-result',
            _yang_ns._namespaces['tailf-rest-query'],
        'ydk.models.tailf.tailf_rest_query'
        ),
    },
    'QueryResult.Result.Select' : {
        'meta_info' : _MetaInfoClass('QueryResult.Result.Select',
            False, 
            [
            _MetaInfoClassMember('label', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Present if the label was given in the start-query select
                entry.
                ''',
                'label',
                'tailf-rest-query', False),
            _MetaInfoClassMember('path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ''',
                'path',
                'tailf-rest-query', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ''',
                'value',
                'tailf-rest-query', False),
            ],
            'tailf-rest-query',
            'select',
            _yang_ns._namespaces['tailf-rest-query'],
        'ydk.models.tailf.tailf_rest_query'
        ),
    },
    'QueryResult.Result' : {
        'meta_info' : _MetaInfoClass('QueryResult.Result',
            False, 
            [
            _MetaInfoClassMember('no-more-data', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Present if no more data is available.
                ''',
                'no_more_data',
                'tailf-rest-query', False),
            _MetaInfoClassMember('select', REFERENCE_LIST, 'Select' , 'ydk.models.tailf.tailf_rest_query', 'QueryResult.Result.Select', 
                [], [], 
                '''                A list of data according to what was specified in the
                corresponding select of the start-query request.
                ''',
                'select',
                'tailf-rest-query', False),
            ],
            'tailf-rest-query',
            'result',
            _yang_ns._namespaces['tailf-rest-query'],
        'ydk.models.tailf.tailf_rest_query'
        ),
    },
    'QueryResult' : {
        'meta_info' : _MetaInfoClass('QueryResult',
            False, 
            [
            _MetaInfoClassMember('result', REFERENCE_LIST, 'Result' , 'ydk.models.tailf.tailf_rest_query', 'QueryResult.Result', 
                [], [], 
                '''                There will be one result for each node in the node set
                produced by evaluating the 'foreach' expression.
                ''',
                'result',
                'tailf-rest-query', False),
            ],
            'tailf-rest-query',
            'query-result',
            _yang_ns._namespaces['tailf-rest-query'],
        'ydk.models.tailf.tailf_rest_query'
        ),
    },
    'ResetQuery' : {
        'meta_info' : _MetaInfoClass('ResetQuery',
            False, 
            [
            _MetaInfoClassMember('offset', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                Define which 'result' entry to be returned.
                ''',
                'offset',
                'tailf-rest-query', False),
            _MetaInfoClassMember('query-handle', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Query handle, as returned from 'start-query'
                ''',
                'query_handle',
                'tailf-rest-query', False),
            ],
            'tailf-rest-query',
            'reset-query',
            _yang_ns._namespaces['tailf-rest-query'],
        'ydk.models.tailf.tailf_rest_query'
        ),
    },
    'StartQuery.Select' : {
        'meta_info' : _MetaInfoClass('StartQuery.Select',
            False, 
            [
            _MetaInfoClassMember('expression', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Declare what element(s) you want to retrieve.
                ''',
                'expression',
                'tailf-rest-query', False),
            _MetaInfoClassMember('label', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Optional label which is copied as is to the 'result' list;
                can be used for easy labeling of the returned element.
                ''',
                'label',
                'tailf-rest-query', False),
            _MetaInfoClassMember('result-type', REFERENCE_LEAFLIST, 'ResultType_Enum' , 'ydk.models.tailf.tailf_rest_query', 'ResultType_Enum', 
                [], [], 
                '''                Declare in what form(s) the returned elements should be
                represented as.
                ''',
                'result_type',
                'tailf-rest-query', False),
            ],
            'tailf-rest-query',
            'select',
            _yang_ns._namespaces['tailf-rest-query'],
        'ydk.models.tailf.tailf_rest_query'
        ),
    },
    'StartQuery' : {
        'meta_info' : _MetaInfoClass('StartQuery',
            False, 
            [
            _MetaInfoClassMember('foreach', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                An XPath 1.0 expression that returns a node set.  For each
                node in this node set, a 'result' entry is constructed.  For
                each such node all 'select/expression's are evaluated, and
                stored in 'result/select'.  The resulting entries are
                returned from the 'fetch-query-result' operation.
                
                When evaluating this expression, the context node is the root
                node of the requested data store.
                ''',
                'foreach',
                'tailf-rest-query', False),
            _MetaInfoClassMember('limit', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                The maximum number of 'result' entries to return in each
                call to 'fetch-query-result'.
                
                If this parameter is not given, all entries are returned.
                ''',
                'limit',
                'tailf-rest-query', False),
            _MetaInfoClassMember('offset', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                Define which 'result' entry to be returned.
                ''',
                'offset',
                'tailf-rest-query', False),
            _MetaInfoClassMember('select', REFERENCE_LIST, 'Select' , 'ydk.models.tailf.tailf_rest_query', 'StartQuery.Select', 
                [], [], 
                '''                Declare what parts of the result you want to get back
                and in what form it should be represented.
                ''',
                'select',
                'tailf-rest-query', False),
            _MetaInfoClassMember('sort-by', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                It is possible to sort the result using an ordered list of
                XPath expressions.
                
                For each node in the node set returned by 'foreach', all
                'sort-by' expressions are evaluated, in order, with the node
                from the 'foreach' evaluation as context node, and the result
                is stored in a tuple.  Thus, this tuple has as many elements
                as entries in the 'sort-by' leaf list.
                
                Each expression should return a node set where the first
                node should be a leaf.  The value of this leaf is used in
                the tuple.  If the expression returns something else, the
                value in the tuple is undefined.
                
                When the 'result' list is fetched, is is sorted according to
                the associated tuple.
                ''',
                'sort_by',
                'tailf-rest-query', False),
            ],
            'tailf-rest-query',
            'start-query',
            _yang_ns._namespaces['tailf-rest-query'],
        'ydk.models.tailf.tailf_rest_query'
        ),
    },
    'StartQueryResult' : {
        'meta_info' : _MetaInfoClass('StartQueryResult',
            False, 
            [
            _MetaInfoClassMember('query-handle', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Query handle to be used in succeeding requests.
                ''',
                'query_handle',
                'tailf-rest-query', False),
            ],
            'tailf-rest-query',
            'start-query-result',
            _yang_ns._namespaces['tailf-rest-query'],
        'ydk.models.tailf.tailf_rest_query'
        ),
    },
    'StopQuery' : {
        'meta_info' : _MetaInfoClass('StopQuery',
            False, 
            [
            _MetaInfoClassMember('query-handle', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Query handle, as returned from 'start-query'
                ''',
                'query_handle',
                'tailf-rest-query', False),
            ],
            'tailf-rest-query',
            'stop-query',
            _yang_ns._namespaces['tailf-rest-query'],
        'ydk.models.tailf.tailf_rest_query'
        ),
    },
}
_meta_table['QueryResult.Result.Select']['meta_info'].parent =_meta_table['QueryResult.Result']['meta_info']
_meta_table['QueryResult.Result']['meta_info'].parent =_meta_table['QueryResult']['meta_info']
_meta_table['StartQuery.Select']['meta_info'].parent =_meta_table['StartQuery']['meta_info']
