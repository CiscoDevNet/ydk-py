""" Cisco_IOS_XR_sysadmin_show_trace_cm 

This module contains definitions
for the Calvados model objects.

This module contains a collection of YANG
definitions for Cisco IOS\-XR SysAdmin configuration.

Copyright(c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

Copyright (c) 2012\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Cm(Entity):
    """
    
    
    .. attribute:: trace
    
    	show traceable processes
    	**type**\: list of  		 :py:class:`Trace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_show_trace_cm.Cm.Trace>`
    
    .. attribute:: lsp
    
    	System Admin Manager lspdb of a location
    	**type**\:  :py:class:`Lsp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_show_trace_cm.Cm.Lsp>`
    
    

    """

    _prefix = 'cm'
    _revision = '2017-04-12'

    def __init__(self):
        super(Cm, self).__init__()
        self._top_entity = None

        self.yang_name = "cm"
        self.yang_parent_name = "Cisco-IOS-XR-sysadmin-show-trace-cm"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("trace", ("trace", Cm.Trace)), ("Cisco-IOS-XR-sysadmin-cm:lsp", ("lsp", Cm.Lsp))])
        self._leafs = OrderedDict()

        self.lsp = Cm.Lsp()
        self.lsp.parent = self
        self._children_name_map["lsp"] = "Cisco-IOS-XR-sysadmin-cm:lsp"

        self.trace = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-show-trace-cm:cm"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Cm, [], name, value)


    class Trace(Entity):
        """
        show traceable processes
        
        .. attribute:: buffer  (key)
        
        	
        	**type**\: str
        
        .. attribute:: location
        
        	
        	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_show_trace_cm.Cm.Trace.Location>`
        
        

        """

        _prefix = 'cm'
        _revision = '2017-04-12'

        def __init__(self):
            super(Cm.Trace, self).__init__()

            self.yang_name = "trace"
            self.yang_parent_name = "cm"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['buffer']
            self._child_classes = OrderedDict([("location", ("location", Cm.Trace.Location))])
            self._leafs = OrderedDict([
                ('buffer', (YLeaf(YType.str, 'buffer'), ['str'])),
            ])
            self.buffer = None

            self.location = YList(self)
            self._segment_path = lambda: "trace" + "[buffer='" + str(self.buffer) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-show-trace-cm:cm/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Cm.Trace, [u'buffer'], name, value)


        class Location(Entity):
            """
            
            
            .. attribute:: location_name  (key)
            
            	
            	**type**\: str
            
            .. attribute:: all_options
            
            	
            	**type**\: list of  		 :py:class:`AllOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_show_trace_cm.Cm.Trace.Location.AllOptions>`
            
            

            """

            _prefix = 'cm'
            _revision = '2017-04-12'

            def __init__(self):
                super(Cm.Trace.Location, self).__init__()

                self.yang_name = "location"
                self.yang_parent_name = "trace"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = ['location_name']
                self._child_classes = OrderedDict([("all-options", ("all_options", Cm.Trace.Location.AllOptions))])
                self._leafs = OrderedDict([
                    ('location_name', (YLeaf(YType.str, 'location_name'), ['str'])),
                ])
                self.location_name = None

                self.all_options = YList(self)
                self._segment_path = lambda: "location" + "[location_name='" + str(self.location_name) + "']"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Cm.Trace.Location, [u'location_name'], name, value)


            class AllOptions(Entity):
                """
                
                
                .. attribute:: option  (key)
                
                	
                	**type**\: str
                
                .. attribute:: trace_blocks
                
                	
                	**type**\: list of  		 :py:class:`TraceBlocks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_show_trace_cm.Cm.Trace.Location.AllOptions.TraceBlocks>`
                
                

                """

                _prefix = 'cm'
                _revision = '2017-04-12'

                def __init__(self):
                    super(Cm.Trace.Location.AllOptions, self).__init__()

                    self.yang_name = "all-options"
                    self.yang_parent_name = "location"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['option']
                    self._child_classes = OrderedDict([("trace-blocks", ("trace_blocks", Cm.Trace.Location.AllOptions.TraceBlocks))])
                    self._leafs = OrderedDict([
                        ('option', (YLeaf(YType.str, 'option'), ['str'])),
                    ])
                    self.option = None

                    self.trace_blocks = YList(self)
                    self._segment_path = lambda: "all-options" + "[option='" + str(self.option) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Cm.Trace.Location.AllOptions, [u'option'], name, value)


                class TraceBlocks(Entity):
                    """
                    
                    
                    .. attribute:: data
                    
                    	Trace output block
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'cm'
                    _revision = '2017-04-12'

                    def __init__(self):
                        super(Cm.Trace.Location.AllOptions.TraceBlocks, self).__init__()

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
                        self._perform_setattr(Cm.Trace.Location.AllOptions.TraceBlocks, [u'data'], name, value)


    class Lsp(Entity):
        """
        System Admin Manager lspdb of a location
        
        .. attribute:: lspdb_locations
        
        	
        	**type**\: list of  		 :py:class:`LspdbLocations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_show_trace_cm.Cm.Lsp.LspdbLocations>`
        
        

        """

        _prefix = 'cmh'
        _revision = '2017-04-12'

        def __init__(self):
            super(Cm.Lsp, self).__init__()

            self.yang_name = "lsp"
            self.yang_parent_name = "cm"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("lspdb_locations", ("lspdb_locations", Cm.Lsp.LspdbLocations))])
            self._leafs = OrderedDict()

            self.lspdb_locations = YList(self)
            self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-cm:lsp"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-show-trace-cm:cm/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Cm.Lsp, [], name, value)


        class LspdbLocations(Entity):
            """
            
            
            .. attribute:: lspdb_location  (key)
            
            	
            	**type**\: str
            
            	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
            
            .. attribute:: lspdbi
            
            	
            	**type**\: list of  		 :py:class:`Lspdbi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_show_trace_cm.Cm.Lsp.LspdbLocations.Lspdbi>`
            
            

            """

            _prefix = 'cmh'
            _revision = '2017-04-12'

            def __init__(self):
                super(Cm.Lsp.LspdbLocations, self).__init__()

                self.yang_name = "lspdb_locations"
                self.yang_parent_name = "lsp"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['lspdb_location']
                self._child_classes = OrderedDict([("lspdbi", ("lspdbi", Cm.Lsp.LspdbLocations.Lspdbi))])
                self._leafs = OrderedDict([
                    ('lspdb_location', (YLeaf(YType.str, 'lspdb_location'), ['str'])),
                ])
                self.lspdb_location = None

                self.lspdbi = YList(self)
                self._segment_path = lambda: "lspdb_locations" + "[lspdb_location='" + str(self.lspdb_location) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-show-trace-cm:cm/Cisco-IOS-XR-sysadmin-cm:lsp/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Cm.Lsp.LspdbLocations, ['lspdb_location'], name, value)


            class Lspdbi(Entity):
                """
                
                
                .. attribute:: lsp_id  (key)
                
                	LSP System ID
                	**type**\: str
                
                .. attribute:: lsp_area_type  (key)
                
                	LSP Area Type
                	**type**\:  :py:class:`AreaType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_cm.AreaType>`
                
                .. attribute:: lsp_sequence
                
                	LSP sequence number
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: lsp_core
                
                	LSP core data bits
                	**type**\: str
                
                .. attribute:: lsp_tlvs
                
                	LSP TLV data
                	**type**\: list of str
                
                

                """

                _prefix = 'cmh'
                _revision = '2017-04-12'

                def __init__(self):
                    super(Cm.Lsp.LspdbLocations.Lspdbi, self).__init__()

                    self.yang_name = "lspdbi"
                    self.yang_parent_name = "lspdb_locations"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['lsp_id','lsp_area_type']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('lsp_id', (YLeaf(YType.str, 'lsp_id'), ['str'])),
                        ('lsp_area_type', (YLeaf(YType.enumeration, 'lsp_area_type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_cm', 'AreaType', '')])),
                        ('lsp_sequence', (YLeaf(YType.uint32, 'lsp_sequence'), ['int'])),
                        ('lsp_core', (YLeaf(YType.str, 'lsp_core'), ['str'])),
                        ('lsp_tlvs', (YLeafList(YType.str, 'lsp_tlvs'), ['str'])),
                    ])
                    self.lsp_id = None
                    self.lsp_area_type = None
                    self.lsp_sequence = None
                    self.lsp_core = None
                    self.lsp_tlvs = []
                    self._segment_path = lambda: "lspdbi" + "[lsp_id='" + str(self.lsp_id) + "']" + "[lsp_area_type='" + str(self.lsp_area_type) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Cm.Lsp.LspdbLocations.Lspdbi, ['lsp_id', 'lsp_area_type', 'lsp_sequence', 'lsp_core', 'lsp_tlvs'], name, value)

    def clone_ptr(self):
        self._top_entity = Cm()
        return self._top_entity

