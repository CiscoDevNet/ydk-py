""" Cisco_IOS_XR_sysadmin_obfl 

This module holds OBFL data.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Obfl(Entity):
    """
    
    
    .. attribute:: obfl_mgr
    
    	
    	**type**\:  :py:class:`ObflMgr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_obfl.Obfl.ObflMgr>`
    
    .. attribute:: obfl_show
    
    	
    	**type**\:  :py:class:`ObflShow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_obfl.Obfl.ObflShow>`
    
    

    """

    _prefix = 'obfl'
    _revision = '2017-07-31'

    def __init__(self):
        super(Obfl, self).__init__()
        self._top_entity = None

        self.yang_name = "obfl"
        self.yang_parent_name = "Cisco-IOS-XR-sysadmin-obfl"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("obfl_mgr", ("obfl_mgr", Obfl.ObflMgr)), ("obfl_show", ("obfl_show", Obfl.ObflShow))])
        self._leafs = OrderedDict()

        self.obfl_mgr = Obfl.ObflMgr()
        self.obfl_mgr.parent = self
        self._children_name_map["obfl_mgr"] = "obfl_mgr"

        self.obfl_show = Obfl.ObflShow()
        self.obfl_show.parent = self
        self._children_name_map["obfl_show"] = "obfl_show"
        self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-obfl:obfl"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Obfl, [], name, value)


    class ObflMgr(Entity):
        """
        
        
        .. attribute:: trace
        
        	show traceable processes
        	**type**\: list of  		 :py:class:`Trace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_obfl.Obfl.ObflMgr.Trace>`
        
        

        """

        _prefix = 'obfl'
        _revision = '2017-07-31'

        def __init__(self):
            super(Obfl.ObflMgr, self).__init__()

            self.yang_name = "obfl_mgr"
            self.yang_parent_name = "obfl"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("trace", ("trace", Obfl.ObflMgr.Trace))])
            self._leafs = OrderedDict()

            self.trace = YList(self)
            self._segment_path = lambda: "obfl_mgr"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-obfl:obfl/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Obfl.ObflMgr, [], name, value)


        class Trace(Entity):
            """
            show traceable processes
            
            .. attribute:: buffer  (key)
            
            	
            	**type**\: str
            
            .. attribute:: location
            
            	
            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_obfl.Obfl.ObflMgr.Trace.Location>`
            
            

            """

            _prefix = 'obfl'
            _revision = '2017-07-31'

            def __init__(self):
                super(Obfl.ObflMgr.Trace, self).__init__()

                self.yang_name = "trace"
                self.yang_parent_name = "obfl_mgr"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['buffer']
                self._child_classes = OrderedDict([("location", ("location", Obfl.ObflMgr.Trace.Location))])
                self._leafs = OrderedDict([
                    ('buffer', (YLeaf(YType.str, 'buffer'), ['str'])),
                ])
                self.buffer = None

                self.location = YList(self)
                self._segment_path = lambda: "trace" + "[buffer='" + str(self.buffer) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-obfl:obfl/obfl_mgr/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Obfl.ObflMgr.Trace, [u'buffer'], name, value)


            class Location(Entity):
                """
                
                
                .. attribute:: location_name  (key)
                
                	
                	**type**\: str
                
                .. attribute:: all_options
                
                	
                	**type**\: list of  		 :py:class:`AllOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_obfl.Obfl.ObflMgr.Trace.Location.AllOptions>`
                
                

                """

                _prefix = 'obfl'
                _revision = '2017-07-31'

                def __init__(self):
                    super(Obfl.ObflMgr.Trace.Location, self).__init__()

                    self.yang_name = "location"
                    self.yang_parent_name = "trace"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['location_name']
                    self._child_classes = OrderedDict([("all-options", ("all_options", Obfl.ObflMgr.Trace.Location.AllOptions))])
                    self._leafs = OrderedDict([
                        ('location_name', (YLeaf(YType.str, 'location_name'), ['str'])),
                    ])
                    self.location_name = None

                    self.all_options = YList(self)
                    self._segment_path = lambda: "location" + "[location_name='" + str(self.location_name) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Obfl.ObflMgr.Trace.Location, [u'location_name'], name, value)


                class AllOptions(Entity):
                    """
                    
                    
                    .. attribute:: option  (key)
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: trace_blocks
                    
                    	
                    	**type**\: list of  		 :py:class:`TraceBlocks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_obfl.Obfl.ObflMgr.Trace.Location.AllOptions.TraceBlocks>`
                    
                    

                    """

                    _prefix = 'obfl'
                    _revision = '2017-07-31'

                    def __init__(self):
                        super(Obfl.ObflMgr.Trace.Location.AllOptions, self).__init__()

                        self.yang_name = "all-options"
                        self.yang_parent_name = "location"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['option']
                        self._child_classes = OrderedDict([("trace-blocks", ("trace_blocks", Obfl.ObflMgr.Trace.Location.AllOptions.TraceBlocks))])
                        self._leafs = OrderedDict([
                            ('option', (YLeaf(YType.str, 'option'), ['str'])),
                        ])
                        self.option = None

                        self.trace_blocks = YList(self)
                        self._segment_path = lambda: "all-options" + "[option='" + str(self.option) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Obfl.ObflMgr.Trace.Location.AllOptions, [u'option'], name, value)


                    class TraceBlocks(Entity):
                        """
                        
                        
                        .. attribute:: data
                        
                        	Trace output block
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'obfl'
                        _revision = '2017-07-31'

                        def __init__(self):
                            super(Obfl.ObflMgr.Trace.Location.AllOptions.TraceBlocks, self).__init__()

                            self.yang_name = "trace-blocks"
                            self.yang_parent_name = "all-options"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('data', (YLeaf(YType.str, 'data'), ['str'])),
                            ])
                            self.data = None
                            self._segment_path = lambda: "trace-blocks"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Obfl.ObflMgr.Trace.Location.AllOptions.TraceBlocks, [u'data'], name, value)


    class ObflShow(Entity):
        """
        
        
        .. attribute:: trace
        
        	show traceable processes
        	**type**\: list of  		 :py:class:`Trace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_obfl.Obfl.ObflShow.Trace>`
        
        

        """

        _prefix = 'obfl'
        _revision = '2017-07-31'

        def __init__(self):
            super(Obfl.ObflShow, self).__init__()

            self.yang_name = "obfl_show"
            self.yang_parent_name = "obfl"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("trace", ("trace", Obfl.ObflShow.Trace))])
            self._leafs = OrderedDict()

            self.trace = YList(self)
            self._segment_path = lambda: "obfl_show"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-obfl:obfl/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Obfl.ObflShow, [], name, value)


        class Trace(Entity):
            """
            show traceable processes
            
            .. attribute:: buffer  (key)
            
            	
            	**type**\: str
            
            .. attribute:: location
            
            	
            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_obfl.Obfl.ObflShow.Trace.Location>`
            
            

            """

            _prefix = 'obfl'
            _revision = '2017-07-31'

            def __init__(self):
                super(Obfl.ObflShow.Trace, self).__init__()

                self.yang_name = "trace"
                self.yang_parent_name = "obfl_show"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['buffer']
                self._child_classes = OrderedDict([("location", ("location", Obfl.ObflShow.Trace.Location))])
                self._leafs = OrderedDict([
                    ('buffer', (YLeaf(YType.str, 'buffer'), ['str'])),
                ])
                self.buffer = None

                self.location = YList(self)
                self._segment_path = lambda: "trace" + "[buffer='" + str(self.buffer) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-obfl:obfl/obfl_show/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Obfl.ObflShow.Trace, [u'buffer'], name, value)


            class Location(Entity):
                """
                
                
                .. attribute:: location_name  (key)
                
                	
                	**type**\: str
                
                .. attribute:: all_options
                
                	
                	**type**\: list of  		 :py:class:`AllOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_obfl.Obfl.ObflShow.Trace.Location.AllOptions>`
                
                

                """

                _prefix = 'obfl'
                _revision = '2017-07-31'

                def __init__(self):
                    super(Obfl.ObflShow.Trace.Location, self).__init__()

                    self.yang_name = "location"
                    self.yang_parent_name = "trace"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['location_name']
                    self._child_classes = OrderedDict([("all-options", ("all_options", Obfl.ObflShow.Trace.Location.AllOptions))])
                    self._leafs = OrderedDict([
                        ('location_name', (YLeaf(YType.str, 'location_name'), ['str'])),
                    ])
                    self.location_name = None

                    self.all_options = YList(self)
                    self._segment_path = lambda: "location" + "[location_name='" + str(self.location_name) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Obfl.ObflShow.Trace.Location, [u'location_name'], name, value)


                class AllOptions(Entity):
                    """
                    
                    
                    .. attribute:: option  (key)
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: trace_blocks
                    
                    	
                    	**type**\: list of  		 :py:class:`TraceBlocks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_obfl.Obfl.ObflShow.Trace.Location.AllOptions.TraceBlocks>`
                    
                    

                    """

                    _prefix = 'obfl'
                    _revision = '2017-07-31'

                    def __init__(self):
                        super(Obfl.ObflShow.Trace.Location.AllOptions, self).__init__()

                        self.yang_name = "all-options"
                        self.yang_parent_name = "location"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['option']
                        self._child_classes = OrderedDict([("trace-blocks", ("trace_blocks", Obfl.ObflShow.Trace.Location.AllOptions.TraceBlocks))])
                        self._leafs = OrderedDict([
                            ('option', (YLeaf(YType.str, 'option'), ['str'])),
                        ])
                        self.option = None

                        self.trace_blocks = YList(self)
                        self._segment_path = lambda: "all-options" + "[option='" + str(self.option) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Obfl.ObflShow.Trace.Location.AllOptions, [u'option'], name, value)


                    class TraceBlocks(Entity):
                        """
                        
                        
                        .. attribute:: data
                        
                        	Trace output block
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'obfl'
                        _revision = '2017-07-31'

                        def __init__(self):
                            super(Obfl.ObflShow.Trace.Location.AllOptions.TraceBlocks, self).__init__()

                            self.yang_name = "trace-blocks"
                            self.yang_parent_name = "all-options"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('data', (YLeaf(YType.str, 'data'), ['str'])),
                            ])
                            self.data = None
                            self._segment_path = lambda: "trace-blocks"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Obfl.ObflShow.Trace.Location.AllOptions.TraceBlocks, [u'data'], name, value)

    def clone_ptr(self):
        self._top_entity = Obfl()
        return self._top_entity

