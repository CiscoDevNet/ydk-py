""" Cisco_IOS_XR_sysadmin_show_trace_debug_agent 

This module contains a collection of YANG
definitions for Cisco IOS\-XR SysAdmin configuration.

Copyright(c) 2012\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class DebugAgent(Entity):
    """
    
    
    .. attribute:: trace
    
    	show traceable processes
    	**type**\: list of  		 :py:class:`Trace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_show_trace_debug_agent.DebugAgent.Trace>`
    
    

    """

    _prefix = 'debug_agent'
    _revision = '2017-04-12'

    def __init__(self):
        super(DebugAgent, self).__init__()
        self._top_entity = None

        self.yang_name = "debug_agent"
        self.yang_parent_name = "Cisco-IOS-XR-sysadmin-show-trace-debug-agent"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([("trace", ("trace", DebugAgent.Trace))])
        self._leafs = OrderedDict()

        self.trace = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-show-trace-debug-agent:debug_agent"

    def __setattr__(self, name, value):
        self._perform_setattr(DebugAgent, [], name, value)


    class Trace(Entity):
        """
        show traceable processes
        
        .. attribute:: buffer  (key)
        
        	
        	**type**\: str
        
        .. attribute:: location
        
        	
        	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_show_trace_debug_agent.DebugAgent.Trace.Location>`
        
        

        """

        _prefix = 'debug_agent'
        _revision = '2017-04-12'

        def __init__(self):
            super(DebugAgent.Trace, self).__init__()

            self.yang_name = "trace"
            self.yang_parent_name = "debug_agent"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['buffer']
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("location", ("location", DebugAgent.Trace.Location))])
            self._leafs = OrderedDict([
                ('buffer', YLeaf(YType.str, 'buffer')),
            ])
            self.buffer = None

            self.location = YList(self)
            self._segment_path = lambda: "trace" + "[buffer='" + str(self.buffer) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-show-trace-debug-agent:debug_agent/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(DebugAgent.Trace, ['buffer'], name, value)


        class Location(Entity):
            """
            
            
            .. attribute:: location_name  (key)
            
            	
            	**type**\: str
            
            .. attribute:: all_options
            
            	
            	**type**\: list of  		 :py:class:`AllOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_show_trace_debug_agent.DebugAgent.Trace.Location.AllOptions>`
            
            

            """

            _prefix = 'debug_agent'
            _revision = '2017-04-12'

            def __init__(self):
                super(DebugAgent.Trace.Location, self).__init__()

                self.yang_name = "location"
                self.yang_parent_name = "trace"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = ['location_name']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("all-options", ("all_options", DebugAgent.Trace.Location.AllOptions))])
                self._leafs = OrderedDict([
                    ('location_name', YLeaf(YType.str, 'location_name')),
                ])
                self.location_name = None

                self.all_options = YList(self)
                self._segment_path = lambda: "location" + "[location_name='" + str(self.location_name) + "']"

            def __setattr__(self, name, value):
                self._perform_setattr(DebugAgent.Trace.Location, ['location_name'], name, value)


            class AllOptions(Entity):
                """
                
                
                .. attribute:: option  (key)
                
                	
                	**type**\: str
                
                .. attribute:: trace_blocks
                
                	
                	**type**\: list of  		 :py:class:`TraceBlocks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_show_trace_debug_agent.DebugAgent.Trace.Location.AllOptions.TraceBlocks>`
                
                

                """

                _prefix = 'debug_agent'
                _revision = '2017-04-12'

                def __init__(self):
                    super(DebugAgent.Trace.Location.AllOptions, self).__init__()

                    self.yang_name = "all-options"
                    self.yang_parent_name = "location"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['option']
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("trace-blocks", ("trace_blocks", DebugAgent.Trace.Location.AllOptions.TraceBlocks))])
                    self._leafs = OrderedDict([
                        ('option', YLeaf(YType.str, 'option')),
                    ])
                    self.option = None

                    self.trace_blocks = YList(self)
                    self._segment_path = lambda: "all-options" + "[option='" + str(self.option) + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(DebugAgent.Trace.Location.AllOptions, ['option'], name, value)


                class TraceBlocks(Entity):
                    """
                    
                    
                    .. attribute:: data
                    
                    	Trace output block
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'debug_agent'
                    _revision = '2017-04-12'

                    def __init__(self):
                        super(DebugAgent.Trace.Location.AllOptions.TraceBlocks, self).__init__()

                        self.yang_name = "trace-blocks"
                        self.yang_parent_name = "all-options"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('data', YLeaf(YType.str, 'data')),
                        ])
                        self.data = None
                        self._segment_path = lambda: "trace-blocks"

                    def __setattr__(self, name, value):
                        self._perform_setattr(DebugAgent.Trace.Location.AllOptions.TraceBlocks, ['data'], name, value)

    def clone_ptr(self):
        self._top_entity = DebugAgent()
        return self._top_entity

