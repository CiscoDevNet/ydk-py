""" Cisco_IOS_XR_ascii_ltrace_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ascii\-ltrace package operational data.

This module contains definitions
for the following management objects\:
  ltrace\: ASCII ltrace data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Ltrace(_Entity_):
    """
    ASCII ltrace data
    
    .. attribute:: features
    
    	feature
    	**type**\:  :py:class:`Features <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ascii_ltrace_oper.Ltrace.Features>`
    
    	**config**\: False
    
    

    """

    _prefix = 'ascii-ltrace-oper'
    _revision = '2018-01-21'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(Ltrace, self).__init__()
        self._top_entity = None

        self.yang_name = "ltrace"
        self.yang_parent_name = "Cisco-IOS-XR-ascii-ltrace-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("features", ("features", Ltrace.Features))])
        self._leafs = OrderedDict()

        self.features = Ltrace.Features()
        self.features.parent = self
        self._children_name_map["features"] = "features"
        self._segment_path = lambda: "Cisco-IOS-XR-ascii-ltrace-oper:ltrace"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Ltrace, [], name, value)


    class Features(_Entity_):
        """
        feature
        
        .. attribute:: feature
        
        	feature
        	**type**\: list of  		 :py:class:`Feature <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ascii_ltrace_oper.Ltrace.Features.Feature>`
        
        	**config**\: False
        
        

        """

        _prefix = 'ascii-ltrace-oper'
        _revision = '2018-01-21'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Ltrace.Features, self).__init__()

            self.yang_name = "features"
            self.yang_parent_name = "ltrace"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("feature", ("feature", Ltrace.Features.Feature))])
            self._leafs = OrderedDict()

            self.feature = YList(self)
            self._segment_path = lambda: "features"
            self._absolute_path = lambda: "Cisco-IOS-XR-ascii-ltrace-oper:ltrace/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ltrace.Features, [], name, value)


        class Feature(_Entity_):
            """
            feature
            
            .. attribute:: traces
            
            	trace
            	**type**\:  :py:class:`Traces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ascii_ltrace_oper.Ltrace.Features.Feature.Traces>`
            
            	**config**\: False
            
            .. attribute:: feature_name
            
            	feature name
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            	**config**\: False
            
            .. attribute:: trace_buf
            
            	trace buffer name
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            	**config**\: False
            
            

            """

            _prefix = 'ascii-ltrace-oper'
            _revision = '2018-01-21'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Ltrace.Features.Feature, self).__init__()

                self.yang_name = "feature"
                self.yang_parent_name = "features"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("traces", ("traces", Ltrace.Features.Feature.Traces))])
                self._leafs = OrderedDict([
                    ('feature_name', (YLeaf(YType.str, 'feature-name'), ['str'])),
                    ('trace_buf', (YLeaf(YType.str, 'trace-buf'), ['str'])),
                ])
                self.feature_name = None
                self.trace_buf = None

                self.traces = Ltrace.Features.Feature.Traces()
                self.traces.parent = self
                self._children_name_map["traces"] = "traces"
                self._segment_path = lambda: "feature"
                self._absolute_path = lambda: "Cisco-IOS-XR-ascii-ltrace-oper:ltrace/features/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ltrace.Features.Feature, ['feature_name', 'trace_buf'], name, value)


            class Traces(_Entity_):
                """
                trace
                
                .. attribute:: trace
                
                	trace
                	**type**\: list of  		 :py:class:`Trace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ascii_ltrace_oper.Ltrace.Features.Feature.Traces.Trace>`
                
                	**config**\: False
                
                

                """

                _prefix = 'ascii-ltrace-oper'
                _revision = '2018-01-21'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ltrace.Features.Feature.Traces, self).__init__()

                    self.yang_name = "traces"
                    self.yang_parent_name = "feature"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("trace", ("trace", Ltrace.Features.Feature.Traces.Trace))])
                    self._leafs = OrderedDict()

                    self.trace = YList(self)
                    self._segment_path = lambda: "traces"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ascii-ltrace-oper:ltrace/features/feature/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ltrace.Features.Feature.Traces, [], name, value)


                class Trace(_Entity_):
                    """
                    trace
                    
                    .. attribute:: ltrace_id  (key)
                    
                    	Ltrace ID of ltrace
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: timestamp
                    
                    	timestamp
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: line
                    
                    	a single line of a trace point
                    	**type**\: str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ascii-ltrace-oper'
                    _revision = '2018-01-21'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Ltrace.Features.Feature.Traces.Trace, self).__init__()

                        self.yang_name = "trace"
                        self.yang_parent_name = "traces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['ltrace_id']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('ltrace_id', (YLeaf(YType.uint32, 'ltrace-id'), ['int'])),
                            ('timestamp', (YLeaf(YType.str, 'timestamp'), ['str'])),
                            ('line', (YLeaf(YType.str, 'line'), ['str'])),
                        ])
                        self.ltrace_id = None
                        self.timestamp = None
                        self.line = None
                        self._segment_path = lambda: "trace" + "[ltrace-id='" + str(self.ltrace_id) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ascii-ltrace-oper:ltrace/features/feature/traces/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ltrace.Features.Feature.Traces.Trace, ['ltrace_id', 'timestamp', 'line'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ascii_ltrace_oper as meta
                        return meta._meta_table['Ltrace.Features.Feature.Traces.Trace']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ascii_ltrace_oper as meta
                    return meta._meta_table['Ltrace.Features.Feature.Traces']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ascii_ltrace_oper as meta
                return meta._meta_table['Ltrace.Features.Feature']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ascii_ltrace_oper as meta
            return meta._meta_table['Ltrace.Features']['meta_info']

    def clone_ptr(self):
        self._top_entity = Ltrace()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ascii_ltrace_oper as meta
        return meta._meta_table['Ltrace']['meta_info']


