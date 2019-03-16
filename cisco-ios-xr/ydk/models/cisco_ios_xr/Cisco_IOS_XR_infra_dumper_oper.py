""" Cisco_IOS_XR_infra_dumper_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-dumper package operational data.

This module contains definitions
for the following management objects\:
  context\: Core dump configuration commands

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Context(Entity):
    """
    Core dump configuration commands
    
    .. attribute:: context_numbers
    
    	Context number table
    	**type**\:  :py:class:`ContextNumbers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.ContextNumbers>`
    
    	**config**\: False
    
    .. attribute:: context_locations
    
    	Core Context location table
    	**type**\:  :py:class:`ContextLocations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.ContextLocations>`
    
    	**config**\: False
    
    .. attribute:: all
    
    	context bag
    	**type**\:  :py:class:`All <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.All>`
    
    	**config**\: False
    
    

    """

    _prefix = 'infra-dumper-oper'
    _revision = '2017-05-05'

    def __init__(self):
        super(Context, self).__init__()
        self._top_entity = None

        self.yang_name = "context"
        self.yang_parent_name = "Cisco-IOS-XR-infra-dumper-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("context-numbers", ("context_numbers", Context.ContextNumbers)), ("context-locations", ("context_locations", Context.ContextLocations)), ("all", ("all", Context.All))])
        self._leafs = OrderedDict()

        self.context_numbers = Context.ContextNumbers()
        self.context_numbers.parent = self
        self._children_name_map["context_numbers"] = "context-numbers"

        self.context_locations = Context.ContextLocations()
        self.context_locations.parent = self
        self._children_name_map["context_locations"] = "context-locations"

        self.all = Context.All()
        self.all.parent = self
        self._children_name_map["all"] = "all"
        self._segment_path = lambda: "Cisco-IOS-XR-infra-dumper-oper:context"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Context, [], name, value)


    class ContextNumbers(Entity):
        """
        Context number table
        
        .. attribute:: context_number
        
        	Context number 
        	**type**\: list of  		 :py:class:`ContextNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.ContextNumbers.ContextNumber>`
        
        	**config**\: False
        
        

        """

        _prefix = 'infra-dumper-oper'
        _revision = '2017-05-05'

        def __init__(self):
            super(Context.ContextNumbers, self).__init__()

            self.yang_name = "context-numbers"
            self.yang_parent_name = "context"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("context-number", ("context_number", Context.ContextNumbers.ContextNumber))])
            self._leafs = OrderedDict()

            self.context_number = YList(self)
            self._segment_path = lambda: "context-numbers"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-dumper-oper:context/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Context.ContextNumbers, [], name, value)


        class ContextNumber(Entity):
            """
            Context number 
            
            .. attribute:: context_num  (key)
            
            	Context for which crash dump info required
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: locations
            
            	Core Context location table
            	**type**\:  :py:class:`Locations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.ContextNumbers.ContextNumber.Locations>`
            
            	**config**\: False
            
            .. attribute:: all
            
            	context bag
            	**type**\:  :py:class:`All <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.ContextNumbers.ContextNumber.All>`
            
            	**config**\: False
            
            

            """

            _prefix = 'infra-dumper-oper'
            _revision = '2017-05-05'

            def __init__(self):
                super(Context.ContextNumbers.ContextNumber, self).__init__()

                self.yang_name = "context-number"
                self.yang_parent_name = "context-numbers"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['context_num']
                self._child_classes = OrderedDict([("locations", ("locations", Context.ContextNumbers.ContextNumber.Locations)), ("all", ("all", Context.ContextNumbers.ContextNumber.All))])
                self._leafs = OrderedDict([
                    ('context_num', (YLeaf(YType.uint32, 'context-num'), ['int'])),
                ])
                self.context_num = None

                self.locations = Context.ContextNumbers.ContextNumber.Locations()
                self.locations.parent = self
                self._children_name_map["locations"] = "locations"

                self.all = Context.ContextNumbers.ContextNumber.All()
                self.all.parent = self
                self._children_name_map["all"] = "all"
                self._segment_path = lambda: "context-number" + "[context-num='" + str(self.context_num) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-dumper-oper:context/context-numbers/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Context.ContextNumbers.ContextNumber, ['context_num'], name, value)


            class Locations(Entity):
                """
                Core Context location table
                
                .. attribute:: location
                
                	Operational Context for a particular location
                	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.ContextNumbers.ContextNumber.Locations.Location>`
                
                	**config**\: False
                
                

                """

                _prefix = 'infra-dumper-oper'
                _revision = '2017-05-05'

                def __init__(self):
                    super(Context.ContextNumbers.ContextNumber.Locations, self).__init__()

                    self.yang_name = "locations"
                    self.yang_parent_name = "context-number"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("location", ("location", Context.ContextNumbers.ContextNumber.Locations.Location))])
                    self._leafs = OrderedDict()

                    self.location = YList(self)
                    self._segment_path = lambda: "locations"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Context.ContextNumbers.ContextNumber.Locations, [], name, value)


                class Location(Entity):
                    """
                    Operational Context for a particular location
                    
                    .. attribute:: node_name  (key)
                    
                    	The node
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    	**config**\: False
                    
                    .. attribute:: enter
                    
                    	Context info bag
                    	**type**\:  :py:class:`Enter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.ContextNumbers.ContextNumber.Locations.Location.Enter>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'infra-dumper-oper'
                    _revision = '2017-05-05'

                    def __init__(self):
                        super(Context.ContextNumbers.ContextNumber.Locations.Location, self).__init__()

                        self.yang_name = "location"
                        self.yang_parent_name = "locations"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['node_name']
                        self._child_classes = OrderedDict([("enter", ("enter", Context.ContextNumbers.ContextNumber.Locations.Location.Enter))])
                        self._leafs = OrderedDict([
                            ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                        ])
                        self.node_name = None

                        self.enter = Context.ContextNumbers.ContextNumber.Locations.Location.Enter()
                        self.enter.parent = self
                        self._children_name_map["enter"] = "enter"
                        self._segment_path = lambda: "location" + "[node-name='" + str(self.node_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Context.ContextNumbers.ContextNumber.Locations.Location, ['node_name'], name, value)


                    class Enter(Entity):
                        """
                        Context info bag
                        
                        .. attribute:: crash_info
                        
                        	All crash info
                        	**type**\: list of  		 :py:class:`CrashInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.ContextNumbers.ContextNumber.Locations.Location.Enter.CrashInfo>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'infra-dumper-oper'
                        _revision = '2017-05-05'

                        def __init__(self):
                            super(Context.ContextNumbers.ContextNumber.Locations.Location.Enter, self).__init__()

                            self.yang_name = "enter"
                            self.yang_parent_name = "location"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("crash-info", ("crash_info", Context.ContextNumbers.ContextNumber.Locations.Location.Enter.CrashInfo))])
                            self._leafs = OrderedDict()

                            self.crash_info = YList(self)
                            self._segment_path = lambda: "enter"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Context.ContextNumbers.ContextNumber.Locations.Location.Enter, [], name, value)


                        class CrashInfo(Entity):
                            """
                            All crash info
                            
                            .. attribute:: node
                            
                            	Node name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: context_info
                            
                            	Context Information
                            	**type**\: list of  		 :py:class:`ContextInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.ContextNumbers.ContextNumber.Locations.Location.Enter.CrashInfo.ContextInfo>`
                            
                            	**config**\: False
                            
                            .. attribute:: crash_package_information
                            
                            	Crash Package Information
                            	**type**\: list of  		 :py:class:`CrashPackageInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.ContextNumbers.ContextNumber.Locations.Location.Enter.CrashInfo.CrashPackageInformation>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'infra-dumper-oper'
                            _revision = '2017-05-05'

                            def __init__(self):
                                super(Context.ContextNumbers.ContextNumber.Locations.Location.Enter.CrashInfo, self).__init__()

                                self.yang_name = "crash-info"
                                self.yang_parent_name = "enter"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("context-info", ("context_info", Context.ContextNumbers.ContextNumber.Locations.Location.Enter.CrashInfo.ContextInfo)), ("crash-package-information", ("crash_package_information", Context.ContextNumbers.ContextNumber.Locations.Location.Enter.CrashInfo.CrashPackageInformation))])
                                self._leafs = OrderedDict([
                                    ('node', (YLeaf(YType.str, 'node'), ['str'])),
                                ])
                                self.node = None

                                self.context_info = YList(self)
                                self.crash_package_information = YList(self)
                                self._segment_path = lambda: "crash-info"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Context.ContextNumbers.ContextNumber.Locations.Location.Enter.CrashInfo, ['node'], name, value)


                            class ContextInfo(Entity):
                                """
                                Context Information
                                
                                .. attribute:: process_name
                                
                                	Process name
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: pid
                                
                                	Process ID
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: tid
                                
                                	Thread ID
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: core_dump_time
                                
                                	Core dump time/Crash time
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: sig_num
                                
                                	Signal number
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: sin_err_str
                                
                                	Signal error string
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: sig_send_pid
                                
                                	Sender pid
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: sig_code
                                
                                	Signal code
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: sin_info
                                
                                	Signal info
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: core_for_process
                                
                                	Core for process at 
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: registers_info
                                
                                	Registers Info
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: stack_trace
                                
                                	Stack Trace
                                	**type**\: list of  		 :py:class:`StackTrace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.ContextNumbers.ContextNumber.Locations.Location.Enter.CrashInfo.ContextInfo.StackTrace>`
                                
                                	**config**\: False
                                
                                .. attribute:: dll_info
                                
                                	DLL Information
                                	**type**\: list of  		 :py:class:`DllInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.ContextNumbers.ContextNumber.Locations.Location.Enter.CrashInfo.ContextInfo.DllInfo>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'infra-dumper-oper'
                                _revision = '2017-05-05'

                                def __init__(self):
                                    super(Context.ContextNumbers.ContextNumber.Locations.Location.Enter.CrashInfo.ContextInfo, self).__init__()

                                    self.yang_name = "context-info"
                                    self.yang_parent_name = "crash-info"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("stack-trace", ("stack_trace", Context.ContextNumbers.ContextNumber.Locations.Location.Enter.CrashInfo.ContextInfo.StackTrace)), ("dll-info", ("dll_info", Context.ContextNumbers.ContextNumber.Locations.Location.Enter.CrashInfo.ContextInfo.DllInfo))])
                                    self._leafs = OrderedDict([
                                        ('process_name', (YLeaf(YType.str, 'process-name'), ['str'])),
                                        ('pid', (YLeaf(YType.uint32, 'pid'), ['int'])),
                                        ('tid', (YLeaf(YType.uint32, 'tid'), ['int'])),
                                        ('core_dump_time', (YLeaf(YType.str, 'core-dump-time'), ['str'])),
                                        ('sig_num', (YLeaf(YType.uint32, 'sig-num'), ['int'])),
                                        ('sin_err_str', (YLeaf(YType.str, 'sin-err-str'), ['str'])),
                                        ('sig_send_pid', (YLeaf(YType.uint32, 'sig-send-pid'), ['int'])),
                                        ('sig_code', (YLeaf(YType.uint32, 'sig-code'), ['int'])),
                                        ('sin_info', (YLeaf(YType.str, 'sin-info'), ['str'])),
                                        ('core_for_process', (YLeaf(YType.str, 'core-for-process'), ['str'])),
                                        ('registers_info', (YLeaf(YType.str, 'registers-info'), ['str'])),
                                    ])
                                    self.process_name = None
                                    self.pid = None
                                    self.tid = None
                                    self.core_dump_time = None
                                    self.sig_num = None
                                    self.sin_err_str = None
                                    self.sig_send_pid = None
                                    self.sig_code = None
                                    self.sin_info = None
                                    self.core_for_process = None
                                    self.registers_info = None

                                    self.stack_trace = YList(self)
                                    self.dll_info = YList(self)
                                    self._segment_path = lambda: "context-info"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Context.ContextNumbers.ContextNumber.Locations.Location.Enter.CrashInfo.ContextInfo, ['process_name', 'pid', 'tid', 'core_dump_time', 'sig_num', 'sin_err_str', 'sig_send_pid', 'sig_code', 'sin_info', 'core_for_process', 'registers_info'], name, value)


                                class StackTrace(Entity):
                                    """
                                    Stack Trace
                                    
                                    .. attribute:: stack_trace
                                    
                                    	stack trace
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'infra-dumper-oper'
                                    _revision = '2017-05-05'

                                    def __init__(self):
                                        super(Context.ContextNumbers.ContextNumber.Locations.Location.Enter.CrashInfo.ContextInfo.StackTrace, self).__init__()

                                        self.yang_name = "stack-trace"
                                        self.yang_parent_name = "context-info"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('stack_trace', (YLeaf(YType.uint32, 'stack-trace'), ['int'])),
                                        ])
                                        self.stack_trace = None
                                        self._segment_path = lambda: "stack-trace"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Context.ContextNumbers.ContextNumber.Locations.Location.Enter.CrashInfo.ContextInfo.StackTrace, ['stack_trace'], name, value)



                                class DllInfo(Entity):
                                    """
                                    DLL Information
                                    
                                    .. attribute:: path
                                    
                                    	DLL Path
                                    	**type**\: str
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: text_addr
                                    
                                    	text addr
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: text_size
                                    
                                    	text size
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: data_addr
                                    
                                    	data addr
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: data_size
                                    
                                    	data size
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: version
                                    
                                    	version
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'infra-dumper-oper'
                                    _revision = '2017-05-05'

                                    def __init__(self):
                                        super(Context.ContextNumbers.ContextNumber.Locations.Location.Enter.CrashInfo.ContextInfo.DllInfo, self).__init__()

                                        self.yang_name = "dll-info"
                                        self.yang_parent_name = "context-info"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('path', (YLeaf(YType.str, 'path'), ['str'])),
                                            ('text_addr', (YLeaf(YType.uint32, 'text-addr'), ['int'])),
                                            ('text_size', (YLeaf(YType.uint32, 'text-size'), ['int'])),
                                            ('data_addr', (YLeaf(YType.uint32, 'data-addr'), ['int'])),
                                            ('data_size', (YLeaf(YType.uint32, 'data-size'), ['int'])),
                                            ('version', (YLeaf(YType.uint32, 'version'), ['int'])),
                                        ])
                                        self.path = None
                                        self.text_addr = None
                                        self.text_size = None
                                        self.data_addr = None
                                        self.data_size = None
                                        self.version = None
                                        self._segment_path = lambda: "dll-info"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Context.ContextNumbers.ContextNumber.Locations.Location.Enter.CrashInfo.ContextInfo.DllInfo, ['path', 'text_addr', 'text_size', 'data_addr', 'data_size', 'version'], name, value)




                            class CrashPackageInformation(Entity):
                                """
                                Crash Package Information
                                
                                .. attribute:: name
                                
                                	Package name
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: source
                                
                                	Package Source
                                	**type**\: str
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'infra-dumper-oper'
                                _revision = '2017-05-05'

                                def __init__(self):
                                    super(Context.ContextNumbers.ContextNumber.Locations.Location.Enter.CrashInfo.CrashPackageInformation, self).__init__()

                                    self.yang_name = "crash-package-information"
                                    self.yang_parent_name = "crash-info"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                        ('source', (YLeaf(YType.str, 'source'), ['str'])),
                                    ])
                                    self.name = None
                                    self.source = None
                                    self._segment_path = lambda: "crash-package-information"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Context.ContextNumbers.ContextNumber.Locations.Location.Enter.CrashInfo.CrashPackageInformation, ['name', 'source'], name, value)







            class All(Entity):
                """
                context bag
                
                .. attribute:: crash_info
                
                	All crash info
                	**type**\: list of  		 :py:class:`CrashInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.ContextNumbers.ContextNumber.All.CrashInfo>`
                
                	**config**\: False
                
                

                """

                _prefix = 'infra-dumper-oper'
                _revision = '2017-05-05'

                def __init__(self):
                    super(Context.ContextNumbers.ContextNumber.All, self).__init__()

                    self.yang_name = "all"
                    self.yang_parent_name = "context-number"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("crash-info", ("crash_info", Context.ContextNumbers.ContextNumber.All.CrashInfo))])
                    self._leafs = OrderedDict()

                    self.crash_info = YList(self)
                    self._segment_path = lambda: "all"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Context.ContextNumbers.ContextNumber.All, [], name, value)


                class CrashInfo(Entity):
                    """
                    All crash info
                    
                    .. attribute:: node
                    
                    	Node name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: context_info
                    
                    	Context Information
                    	**type**\: list of  		 :py:class:`ContextInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.ContextNumbers.ContextNumber.All.CrashInfo.ContextInfo>`
                    
                    	**config**\: False
                    
                    .. attribute:: crash_package_information
                    
                    	Crash Package Information
                    	**type**\: list of  		 :py:class:`CrashPackageInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.ContextNumbers.ContextNumber.All.CrashInfo.CrashPackageInformation>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'infra-dumper-oper'
                    _revision = '2017-05-05'

                    def __init__(self):
                        super(Context.ContextNumbers.ContextNumber.All.CrashInfo, self).__init__()

                        self.yang_name = "crash-info"
                        self.yang_parent_name = "all"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("context-info", ("context_info", Context.ContextNumbers.ContextNumber.All.CrashInfo.ContextInfo)), ("crash-package-information", ("crash_package_information", Context.ContextNumbers.ContextNumber.All.CrashInfo.CrashPackageInformation))])
                        self._leafs = OrderedDict([
                            ('node', (YLeaf(YType.str, 'node'), ['str'])),
                        ])
                        self.node = None

                        self.context_info = YList(self)
                        self.crash_package_information = YList(self)
                        self._segment_path = lambda: "crash-info"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Context.ContextNumbers.ContextNumber.All.CrashInfo, ['node'], name, value)


                    class ContextInfo(Entity):
                        """
                        Context Information
                        
                        .. attribute:: process_name
                        
                        	Process name
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: pid
                        
                        	Process ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: tid
                        
                        	Thread ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: core_dump_time
                        
                        	Core dump time/Crash time
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: sig_num
                        
                        	Signal number
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: sin_err_str
                        
                        	Signal error string
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: sig_send_pid
                        
                        	Sender pid
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: sig_code
                        
                        	Signal code
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: sin_info
                        
                        	Signal info
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: core_for_process
                        
                        	Core for process at 
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: registers_info
                        
                        	Registers Info
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: stack_trace
                        
                        	Stack Trace
                        	**type**\: list of  		 :py:class:`StackTrace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.ContextNumbers.ContextNumber.All.CrashInfo.ContextInfo.StackTrace>`
                        
                        	**config**\: False
                        
                        .. attribute:: dll_info
                        
                        	DLL Information
                        	**type**\: list of  		 :py:class:`DllInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.ContextNumbers.ContextNumber.All.CrashInfo.ContextInfo.DllInfo>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'infra-dumper-oper'
                        _revision = '2017-05-05'

                        def __init__(self):
                            super(Context.ContextNumbers.ContextNumber.All.CrashInfo.ContextInfo, self).__init__()

                            self.yang_name = "context-info"
                            self.yang_parent_name = "crash-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("stack-trace", ("stack_trace", Context.ContextNumbers.ContextNumber.All.CrashInfo.ContextInfo.StackTrace)), ("dll-info", ("dll_info", Context.ContextNumbers.ContextNumber.All.CrashInfo.ContextInfo.DllInfo))])
                            self._leafs = OrderedDict([
                                ('process_name', (YLeaf(YType.str, 'process-name'), ['str'])),
                                ('pid', (YLeaf(YType.uint32, 'pid'), ['int'])),
                                ('tid', (YLeaf(YType.uint32, 'tid'), ['int'])),
                                ('core_dump_time', (YLeaf(YType.str, 'core-dump-time'), ['str'])),
                                ('sig_num', (YLeaf(YType.uint32, 'sig-num'), ['int'])),
                                ('sin_err_str', (YLeaf(YType.str, 'sin-err-str'), ['str'])),
                                ('sig_send_pid', (YLeaf(YType.uint32, 'sig-send-pid'), ['int'])),
                                ('sig_code', (YLeaf(YType.uint32, 'sig-code'), ['int'])),
                                ('sin_info', (YLeaf(YType.str, 'sin-info'), ['str'])),
                                ('core_for_process', (YLeaf(YType.str, 'core-for-process'), ['str'])),
                                ('registers_info', (YLeaf(YType.str, 'registers-info'), ['str'])),
                            ])
                            self.process_name = None
                            self.pid = None
                            self.tid = None
                            self.core_dump_time = None
                            self.sig_num = None
                            self.sin_err_str = None
                            self.sig_send_pid = None
                            self.sig_code = None
                            self.sin_info = None
                            self.core_for_process = None
                            self.registers_info = None

                            self.stack_trace = YList(self)
                            self.dll_info = YList(self)
                            self._segment_path = lambda: "context-info"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Context.ContextNumbers.ContextNumber.All.CrashInfo.ContextInfo, ['process_name', 'pid', 'tid', 'core_dump_time', 'sig_num', 'sin_err_str', 'sig_send_pid', 'sig_code', 'sin_info', 'core_for_process', 'registers_info'], name, value)


                        class StackTrace(Entity):
                            """
                            Stack Trace
                            
                            .. attribute:: stack_trace
                            
                            	stack trace
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'infra-dumper-oper'
                            _revision = '2017-05-05'

                            def __init__(self):
                                super(Context.ContextNumbers.ContextNumber.All.CrashInfo.ContextInfo.StackTrace, self).__init__()

                                self.yang_name = "stack-trace"
                                self.yang_parent_name = "context-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('stack_trace', (YLeaf(YType.uint32, 'stack-trace'), ['int'])),
                                ])
                                self.stack_trace = None
                                self._segment_path = lambda: "stack-trace"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Context.ContextNumbers.ContextNumber.All.CrashInfo.ContextInfo.StackTrace, ['stack_trace'], name, value)



                        class DllInfo(Entity):
                            """
                            DLL Information
                            
                            .. attribute:: path
                            
                            	DLL Path
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: text_addr
                            
                            	text addr
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: text_size
                            
                            	text size
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: data_addr
                            
                            	data addr
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: data_size
                            
                            	data size
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: version
                            
                            	version
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'infra-dumper-oper'
                            _revision = '2017-05-05'

                            def __init__(self):
                                super(Context.ContextNumbers.ContextNumber.All.CrashInfo.ContextInfo.DllInfo, self).__init__()

                                self.yang_name = "dll-info"
                                self.yang_parent_name = "context-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('path', (YLeaf(YType.str, 'path'), ['str'])),
                                    ('text_addr', (YLeaf(YType.uint32, 'text-addr'), ['int'])),
                                    ('text_size', (YLeaf(YType.uint32, 'text-size'), ['int'])),
                                    ('data_addr', (YLeaf(YType.uint32, 'data-addr'), ['int'])),
                                    ('data_size', (YLeaf(YType.uint32, 'data-size'), ['int'])),
                                    ('version', (YLeaf(YType.uint32, 'version'), ['int'])),
                                ])
                                self.path = None
                                self.text_addr = None
                                self.text_size = None
                                self.data_addr = None
                                self.data_size = None
                                self.version = None
                                self._segment_path = lambda: "dll-info"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Context.ContextNumbers.ContextNumber.All.CrashInfo.ContextInfo.DllInfo, ['path', 'text_addr', 'text_size', 'data_addr', 'data_size', 'version'], name, value)




                    class CrashPackageInformation(Entity):
                        """
                        Crash Package Information
                        
                        .. attribute:: name
                        
                        	Package name
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: source
                        
                        	Package Source
                        	**type**\: str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'infra-dumper-oper'
                        _revision = '2017-05-05'

                        def __init__(self):
                            super(Context.ContextNumbers.ContextNumber.All.CrashInfo.CrashPackageInformation, self).__init__()

                            self.yang_name = "crash-package-information"
                            self.yang_parent_name = "crash-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                ('source', (YLeaf(YType.str, 'source'), ['str'])),
                            ])
                            self.name = None
                            self.source = None
                            self._segment_path = lambda: "crash-package-information"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Context.ContextNumbers.ContextNumber.All.CrashInfo.CrashPackageInformation, ['name', 'source'], name, value)







    class ContextLocations(Entity):
        """
        Core Context location table
        
        .. attribute:: context_location
        
        	Operational Context for a particular location
        	**type**\: list of  		 :py:class:`ContextLocation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.ContextLocations.ContextLocation>`
        
        	**config**\: False
        
        

        """

        _prefix = 'infra-dumper-oper'
        _revision = '2017-05-05'

        def __init__(self):
            super(Context.ContextLocations, self).__init__()

            self.yang_name = "context-locations"
            self.yang_parent_name = "context"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("context-location", ("context_location", Context.ContextLocations.ContextLocation))])
            self._leafs = OrderedDict()

            self.context_location = YList(self)
            self._segment_path = lambda: "context-locations"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-dumper-oper:context/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Context.ContextLocations, [], name, value)


        class ContextLocation(Entity):
            """
            Operational Context for a particular location
            
            .. attribute:: node_name  (key)
            
            	The node
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            	**config**\: False
            
            .. attribute:: numbers
            
            	Context number Table
            	**type**\:  :py:class:`Numbers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.ContextLocations.ContextLocation.Numbers>`
            
            	**config**\: False
            
            .. attribute:: all
            
            	context bag
            	**type**\:  :py:class:`All <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.ContextLocations.ContextLocation.All>`
            
            	**config**\: False
            
            

            """

            _prefix = 'infra-dumper-oper'
            _revision = '2017-05-05'

            def __init__(self):
                super(Context.ContextLocations.ContextLocation, self).__init__()

                self.yang_name = "context-location"
                self.yang_parent_name = "context-locations"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_classes = OrderedDict([("numbers", ("numbers", Context.ContextLocations.ContextLocation.Numbers)), ("all", ("all", Context.ContextLocations.ContextLocation.All))])
                self._leafs = OrderedDict([
                    ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                ])
                self.node_name = None

                self.numbers = Context.ContextLocations.ContextLocation.Numbers()
                self.numbers.parent = self
                self._children_name_map["numbers"] = "numbers"

                self.all = Context.ContextLocations.ContextLocation.All()
                self.all.parent = self
                self._children_name_map["all"] = "all"
                self._segment_path = lambda: "context-location" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-dumper-oper:context/context-locations/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Context.ContextLocations.ContextLocation, ['node_name'], name, value)


            class Numbers(Entity):
                """
                Context number Table
                
                .. attribute:: number
                
                	Context number
                	**type**\: list of  		 :py:class:`Number <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.ContextLocations.ContextLocation.Numbers.Number>`
                
                	**config**\: False
                
                

                """

                _prefix = 'infra-dumper-oper'
                _revision = '2017-05-05'

                def __init__(self):
                    super(Context.ContextLocations.ContextLocation.Numbers, self).__init__()

                    self.yang_name = "numbers"
                    self.yang_parent_name = "context-location"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("number", ("number", Context.ContextLocations.ContextLocation.Numbers.Number))])
                    self._leafs = OrderedDict()

                    self.number = YList(self)
                    self._segment_path = lambda: "numbers"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Context.ContextLocations.ContextLocation.Numbers, [], name, value)


                class Number(Entity):
                    """
                    Context number
                    
                    .. attribute:: context_num  (key)
                    
                    	Context for which crash dump info required
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: enter
                    
                    	Context info bag
                    	**type**\:  :py:class:`Enter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.ContextLocations.ContextLocation.Numbers.Number.Enter>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'infra-dumper-oper'
                    _revision = '2017-05-05'

                    def __init__(self):
                        super(Context.ContextLocations.ContextLocation.Numbers.Number, self).__init__()

                        self.yang_name = "number"
                        self.yang_parent_name = "numbers"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['context_num']
                        self._child_classes = OrderedDict([("enter", ("enter", Context.ContextLocations.ContextLocation.Numbers.Number.Enter))])
                        self._leafs = OrderedDict([
                            ('context_num', (YLeaf(YType.uint32, 'context-num'), ['int'])),
                        ])
                        self.context_num = None

                        self.enter = Context.ContextLocations.ContextLocation.Numbers.Number.Enter()
                        self.enter.parent = self
                        self._children_name_map["enter"] = "enter"
                        self._segment_path = lambda: "number" + "[context-num='" + str(self.context_num) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Context.ContextLocations.ContextLocation.Numbers.Number, ['context_num'], name, value)


                    class Enter(Entity):
                        """
                        Context info bag
                        
                        .. attribute:: crash_info
                        
                        	All crash info
                        	**type**\: list of  		 :py:class:`CrashInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.ContextLocations.ContextLocation.Numbers.Number.Enter.CrashInfo>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'infra-dumper-oper'
                        _revision = '2017-05-05'

                        def __init__(self):
                            super(Context.ContextLocations.ContextLocation.Numbers.Number.Enter, self).__init__()

                            self.yang_name = "enter"
                            self.yang_parent_name = "number"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("crash-info", ("crash_info", Context.ContextLocations.ContextLocation.Numbers.Number.Enter.CrashInfo))])
                            self._leafs = OrderedDict()

                            self.crash_info = YList(self)
                            self._segment_path = lambda: "enter"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Context.ContextLocations.ContextLocation.Numbers.Number.Enter, [], name, value)


                        class CrashInfo(Entity):
                            """
                            All crash info
                            
                            .. attribute:: node
                            
                            	Node name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: context_info
                            
                            	Context Information
                            	**type**\: list of  		 :py:class:`ContextInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.ContextLocations.ContextLocation.Numbers.Number.Enter.CrashInfo.ContextInfo>`
                            
                            	**config**\: False
                            
                            .. attribute:: crash_package_information
                            
                            	Crash Package Information
                            	**type**\: list of  		 :py:class:`CrashPackageInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.ContextLocations.ContextLocation.Numbers.Number.Enter.CrashInfo.CrashPackageInformation>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'infra-dumper-oper'
                            _revision = '2017-05-05'

                            def __init__(self):
                                super(Context.ContextLocations.ContextLocation.Numbers.Number.Enter.CrashInfo, self).__init__()

                                self.yang_name = "crash-info"
                                self.yang_parent_name = "enter"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("context-info", ("context_info", Context.ContextLocations.ContextLocation.Numbers.Number.Enter.CrashInfo.ContextInfo)), ("crash-package-information", ("crash_package_information", Context.ContextLocations.ContextLocation.Numbers.Number.Enter.CrashInfo.CrashPackageInformation))])
                                self._leafs = OrderedDict([
                                    ('node', (YLeaf(YType.str, 'node'), ['str'])),
                                ])
                                self.node = None

                                self.context_info = YList(self)
                                self.crash_package_information = YList(self)
                                self._segment_path = lambda: "crash-info"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Context.ContextLocations.ContextLocation.Numbers.Number.Enter.CrashInfo, ['node'], name, value)


                            class ContextInfo(Entity):
                                """
                                Context Information
                                
                                .. attribute:: process_name
                                
                                	Process name
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: pid
                                
                                	Process ID
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: tid
                                
                                	Thread ID
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: core_dump_time
                                
                                	Core dump time/Crash time
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: sig_num
                                
                                	Signal number
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: sin_err_str
                                
                                	Signal error string
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: sig_send_pid
                                
                                	Sender pid
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: sig_code
                                
                                	Signal code
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: sin_info
                                
                                	Signal info
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: core_for_process
                                
                                	Core for process at 
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: registers_info
                                
                                	Registers Info
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: stack_trace
                                
                                	Stack Trace
                                	**type**\: list of  		 :py:class:`StackTrace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.ContextLocations.ContextLocation.Numbers.Number.Enter.CrashInfo.ContextInfo.StackTrace>`
                                
                                	**config**\: False
                                
                                .. attribute:: dll_info
                                
                                	DLL Information
                                	**type**\: list of  		 :py:class:`DllInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.ContextLocations.ContextLocation.Numbers.Number.Enter.CrashInfo.ContextInfo.DllInfo>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'infra-dumper-oper'
                                _revision = '2017-05-05'

                                def __init__(self):
                                    super(Context.ContextLocations.ContextLocation.Numbers.Number.Enter.CrashInfo.ContextInfo, self).__init__()

                                    self.yang_name = "context-info"
                                    self.yang_parent_name = "crash-info"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("stack-trace", ("stack_trace", Context.ContextLocations.ContextLocation.Numbers.Number.Enter.CrashInfo.ContextInfo.StackTrace)), ("dll-info", ("dll_info", Context.ContextLocations.ContextLocation.Numbers.Number.Enter.CrashInfo.ContextInfo.DllInfo))])
                                    self._leafs = OrderedDict([
                                        ('process_name', (YLeaf(YType.str, 'process-name'), ['str'])),
                                        ('pid', (YLeaf(YType.uint32, 'pid'), ['int'])),
                                        ('tid', (YLeaf(YType.uint32, 'tid'), ['int'])),
                                        ('core_dump_time', (YLeaf(YType.str, 'core-dump-time'), ['str'])),
                                        ('sig_num', (YLeaf(YType.uint32, 'sig-num'), ['int'])),
                                        ('sin_err_str', (YLeaf(YType.str, 'sin-err-str'), ['str'])),
                                        ('sig_send_pid', (YLeaf(YType.uint32, 'sig-send-pid'), ['int'])),
                                        ('sig_code', (YLeaf(YType.uint32, 'sig-code'), ['int'])),
                                        ('sin_info', (YLeaf(YType.str, 'sin-info'), ['str'])),
                                        ('core_for_process', (YLeaf(YType.str, 'core-for-process'), ['str'])),
                                        ('registers_info', (YLeaf(YType.str, 'registers-info'), ['str'])),
                                    ])
                                    self.process_name = None
                                    self.pid = None
                                    self.tid = None
                                    self.core_dump_time = None
                                    self.sig_num = None
                                    self.sin_err_str = None
                                    self.sig_send_pid = None
                                    self.sig_code = None
                                    self.sin_info = None
                                    self.core_for_process = None
                                    self.registers_info = None

                                    self.stack_trace = YList(self)
                                    self.dll_info = YList(self)
                                    self._segment_path = lambda: "context-info"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Context.ContextLocations.ContextLocation.Numbers.Number.Enter.CrashInfo.ContextInfo, ['process_name', 'pid', 'tid', 'core_dump_time', 'sig_num', 'sin_err_str', 'sig_send_pid', 'sig_code', 'sin_info', 'core_for_process', 'registers_info'], name, value)


                                class StackTrace(Entity):
                                    """
                                    Stack Trace
                                    
                                    .. attribute:: stack_trace
                                    
                                    	stack trace
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'infra-dumper-oper'
                                    _revision = '2017-05-05'

                                    def __init__(self):
                                        super(Context.ContextLocations.ContextLocation.Numbers.Number.Enter.CrashInfo.ContextInfo.StackTrace, self).__init__()

                                        self.yang_name = "stack-trace"
                                        self.yang_parent_name = "context-info"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('stack_trace', (YLeaf(YType.uint32, 'stack-trace'), ['int'])),
                                        ])
                                        self.stack_trace = None
                                        self._segment_path = lambda: "stack-trace"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Context.ContextLocations.ContextLocation.Numbers.Number.Enter.CrashInfo.ContextInfo.StackTrace, ['stack_trace'], name, value)



                                class DllInfo(Entity):
                                    """
                                    DLL Information
                                    
                                    .. attribute:: path
                                    
                                    	DLL Path
                                    	**type**\: str
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: text_addr
                                    
                                    	text addr
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: text_size
                                    
                                    	text size
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: data_addr
                                    
                                    	data addr
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: data_size
                                    
                                    	data size
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: version
                                    
                                    	version
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'infra-dumper-oper'
                                    _revision = '2017-05-05'

                                    def __init__(self):
                                        super(Context.ContextLocations.ContextLocation.Numbers.Number.Enter.CrashInfo.ContextInfo.DllInfo, self).__init__()

                                        self.yang_name = "dll-info"
                                        self.yang_parent_name = "context-info"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('path', (YLeaf(YType.str, 'path'), ['str'])),
                                            ('text_addr', (YLeaf(YType.uint32, 'text-addr'), ['int'])),
                                            ('text_size', (YLeaf(YType.uint32, 'text-size'), ['int'])),
                                            ('data_addr', (YLeaf(YType.uint32, 'data-addr'), ['int'])),
                                            ('data_size', (YLeaf(YType.uint32, 'data-size'), ['int'])),
                                            ('version', (YLeaf(YType.uint32, 'version'), ['int'])),
                                        ])
                                        self.path = None
                                        self.text_addr = None
                                        self.text_size = None
                                        self.data_addr = None
                                        self.data_size = None
                                        self.version = None
                                        self._segment_path = lambda: "dll-info"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Context.ContextLocations.ContextLocation.Numbers.Number.Enter.CrashInfo.ContextInfo.DllInfo, ['path', 'text_addr', 'text_size', 'data_addr', 'data_size', 'version'], name, value)




                            class CrashPackageInformation(Entity):
                                """
                                Crash Package Information
                                
                                .. attribute:: name
                                
                                	Package name
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: source
                                
                                	Package Source
                                	**type**\: str
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'infra-dumper-oper'
                                _revision = '2017-05-05'

                                def __init__(self):
                                    super(Context.ContextLocations.ContextLocation.Numbers.Number.Enter.CrashInfo.CrashPackageInformation, self).__init__()

                                    self.yang_name = "crash-package-information"
                                    self.yang_parent_name = "crash-info"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                        ('source', (YLeaf(YType.str, 'source'), ['str'])),
                                    ])
                                    self.name = None
                                    self.source = None
                                    self._segment_path = lambda: "crash-package-information"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Context.ContextLocations.ContextLocation.Numbers.Number.Enter.CrashInfo.CrashPackageInformation, ['name', 'source'], name, value)







            class All(Entity):
                """
                context bag
                
                .. attribute:: crash_info
                
                	All crash info
                	**type**\: list of  		 :py:class:`CrashInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.ContextLocations.ContextLocation.All.CrashInfo>`
                
                	**config**\: False
                
                

                """

                _prefix = 'infra-dumper-oper'
                _revision = '2017-05-05'

                def __init__(self):
                    super(Context.ContextLocations.ContextLocation.All, self).__init__()

                    self.yang_name = "all"
                    self.yang_parent_name = "context-location"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("crash-info", ("crash_info", Context.ContextLocations.ContextLocation.All.CrashInfo))])
                    self._leafs = OrderedDict()

                    self.crash_info = YList(self)
                    self._segment_path = lambda: "all"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Context.ContextLocations.ContextLocation.All, [], name, value)


                class CrashInfo(Entity):
                    """
                    All crash info
                    
                    .. attribute:: node
                    
                    	Node name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: context_info
                    
                    	Context Information
                    	**type**\: list of  		 :py:class:`ContextInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.ContextLocations.ContextLocation.All.CrashInfo.ContextInfo>`
                    
                    	**config**\: False
                    
                    .. attribute:: crash_package_information
                    
                    	Crash Package Information
                    	**type**\: list of  		 :py:class:`CrashPackageInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.ContextLocations.ContextLocation.All.CrashInfo.CrashPackageInformation>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'infra-dumper-oper'
                    _revision = '2017-05-05'

                    def __init__(self):
                        super(Context.ContextLocations.ContextLocation.All.CrashInfo, self).__init__()

                        self.yang_name = "crash-info"
                        self.yang_parent_name = "all"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("context-info", ("context_info", Context.ContextLocations.ContextLocation.All.CrashInfo.ContextInfo)), ("crash-package-information", ("crash_package_information", Context.ContextLocations.ContextLocation.All.CrashInfo.CrashPackageInformation))])
                        self._leafs = OrderedDict([
                            ('node', (YLeaf(YType.str, 'node'), ['str'])),
                        ])
                        self.node = None

                        self.context_info = YList(self)
                        self.crash_package_information = YList(self)
                        self._segment_path = lambda: "crash-info"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Context.ContextLocations.ContextLocation.All.CrashInfo, ['node'], name, value)


                    class ContextInfo(Entity):
                        """
                        Context Information
                        
                        .. attribute:: process_name
                        
                        	Process name
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: pid
                        
                        	Process ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: tid
                        
                        	Thread ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: core_dump_time
                        
                        	Core dump time/Crash time
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: sig_num
                        
                        	Signal number
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: sin_err_str
                        
                        	Signal error string
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: sig_send_pid
                        
                        	Sender pid
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: sig_code
                        
                        	Signal code
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: sin_info
                        
                        	Signal info
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: core_for_process
                        
                        	Core for process at 
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: registers_info
                        
                        	Registers Info
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: stack_trace
                        
                        	Stack Trace
                        	**type**\: list of  		 :py:class:`StackTrace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.ContextLocations.ContextLocation.All.CrashInfo.ContextInfo.StackTrace>`
                        
                        	**config**\: False
                        
                        .. attribute:: dll_info
                        
                        	DLL Information
                        	**type**\: list of  		 :py:class:`DllInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.ContextLocations.ContextLocation.All.CrashInfo.ContextInfo.DllInfo>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'infra-dumper-oper'
                        _revision = '2017-05-05'

                        def __init__(self):
                            super(Context.ContextLocations.ContextLocation.All.CrashInfo.ContextInfo, self).__init__()

                            self.yang_name = "context-info"
                            self.yang_parent_name = "crash-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("stack-trace", ("stack_trace", Context.ContextLocations.ContextLocation.All.CrashInfo.ContextInfo.StackTrace)), ("dll-info", ("dll_info", Context.ContextLocations.ContextLocation.All.CrashInfo.ContextInfo.DllInfo))])
                            self._leafs = OrderedDict([
                                ('process_name', (YLeaf(YType.str, 'process-name'), ['str'])),
                                ('pid', (YLeaf(YType.uint32, 'pid'), ['int'])),
                                ('tid', (YLeaf(YType.uint32, 'tid'), ['int'])),
                                ('core_dump_time', (YLeaf(YType.str, 'core-dump-time'), ['str'])),
                                ('sig_num', (YLeaf(YType.uint32, 'sig-num'), ['int'])),
                                ('sin_err_str', (YLeaf(YType.str, 'sin-err-str'), ['str'])),
                                ('sig_send_pid', (YLeaf(YType.uint32, 'sig-send-pid'), ['int'])),
                                ('sig_code', (YLeaf(YType.uint32, 'sig-code'), ['int'])),
                                ('sin_info', (YLeaf(YType.str, 'sin-info'), ['str'])),
                                ('core_for_process', (YLeaf(YType.str, 'core-for-process'), ['str'])),
                                ('registers_info', (YLeaf(YType.str, 'registers-info'), ['str'])),
                            ])
                            self.process_name = None
                            self.pid = None
                            self.tid = None
                            self.core_dump_time = None
                            self.sig_num = None
                            self.sin_err_str = None
                            self.sig_send_pid = None
                            self.sig_code = None
                            self.sin_info = None
                            self.core_for_process = None
                            self.registers_info = None

                            self.stack_trace = YList(self)
                            self.dll_info = YList(self)
                            self._segment_path = lambda: "context-info"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Context.ContextLocations.ContextLocation.All.CrashInfo.ContextInfo, ['process_name', 'pid', 'tid', 'core_dump_time', 'sig_num', 'sin_err_str', 'sig_send_pid', 'sig_code', 'sin_info', 'core_for_process', 'registers_info'], name, value)


                        class StackTrace(Entity):
                            """
                            Stack Trace
                            
                            .. attribute:: stack_trace
                            
                            	stack trace
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'infra-dumper-oper'
                            _revision = '2017-05-05'

                            def __init__(self):
                                super(Context.ContextLocations.ContextLocation.All.CrashInfo.ContextInfo.StackTrace, self).__init__()

                                self.yang_name = "stack-trace"
                                self.yang_parent_name = "context-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('stack_trace', (YLeaf(YType.uint32, 'stack-trace'), ['int'])),
                                ])
                                self.stack_trace = None
                                self._segment_path = lambda: "stack-trace"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Context.ContextLocations.ContextLocation.All.CrashInfo.ContextInfo.StackTrace, ['stack_trace'], name, value)



                        class DllInfo(Entity):
                            """
                            DLL Information
                            
                            .. attribute:: path
                            
                            	DLL Path
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: text_addr
                            
                            	text addr
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: text_size
                            
                            	text size
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: data_addr
                            
                            	data addr
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: data_size
                            
                            	data size
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: version
                            
                            	version
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'infra-dumper-oper'
                            _revision = '2017-05-05'

                            def __init__(self):
                                super(Context.ContextLocations.ContextLocation.All.CrashInfo.ContextInfo.DllInfo, self).__init__()

                                self.yang_name = "dll-info"
                                self.yang_parent_name = "context-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('path', (YLeaf(YType.str, 'path'), ['str'])),
                                    ('text_addr', (YLeaf(YType.uint32, 'text-addr'), ['int'])),
                                    ('text_size', (YLeaf(YType.uint32, 'text-size'), ['int'])),
                                    ('data_addr', (YLeaf(YType.uint32, 'data-addr'), ['int'])),
                                    ('data_size', (YLeaf(YType.uint32, 'data-size'), ['int'])),
                                    ('version', (YLeaf(YType.uint32, 'version'), ['int'])),
                                ])
                                self.path = None
                                self.text_addr = None
                                self.text_size = None
                                self.data_addr = None
                                self.data_size = None
                                self.version = None
                                self._segment_path = lambda: "dll-info"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Context.ContextLocations.ContextLocation.All.CrashInfo.ContextInfo.DllInfo, ['path', 'text_addr', 'text_size', 'data_addr', 'data_size', 'version'], name, value)




                    class CrashPackageInformation(Entity):
                        """
                        Crash Package Information
                        
                        .. attribute:: name
                        
                        	Package name
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: source
                        
                        	Package Source
                        	**type**\: str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'infra-dumper-oper'
                        _revision = '2017-05-05'

                        def __init__(self):
                            super(Context.ContextLocations.ContextLocation.All.CrashInfo.CrashPackageInformation, self).__init__()

                            self.yang_name = "crash-package-information"
                            self.yang_parent_name = "crash-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                ('source', (YLeaf(YType.str, 'source'), ['str'])),
                            ])
                            self.name = None
                            self.source = None
                            self._segment_path = lambda: "crash-package-information"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Context.ContextLocations.ContextLocation.All.CrashInfo.CrashPackageInformation, ['name', 'source'], name, value)







    class All(Entity):
        """
        context bag
        
        .. attribute:: crash_info
        
        	All crash info
        	**type**\: list of  		 :py:class:`CrashInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.All.CrashInfo>`
        
        	**config**\: False
        
        

        """

        _prefix = 'infra-dumper-oper'
        _revision = '2017-05-05'

        def __init__(self):
            super(Context.All, self).__init__()

            self.yang_name = "all"
            self.yang_parent_name = "context"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("crash-info", ("crash_info", Context.All.CrashInfo))])
            self._leafs = OrderedDict()

            self.crash_info = YList(self)
            self._segment_path = lambda: "all"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-dumper-oper:context/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Context.All, [], name, value)


        class CrashInfo(Entity):
            """
            All crash info
            
            .. attribute:: node
            
            	Node name
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: context_info
            
            	Context Information
            	**type**\: list of  		 :py:class:`ContextInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.All.CrashInfo.ContextInfo>`
            
            	**config**\: False
            
            .. attribute:: crash_package_information
            
            	Crash Package Information
            	**type**\: list of  		 :py:class:`CrashPackageInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.All.CrashInfo.CrashPackageInformation>`
            
            	**config**\: False
            
            

            """

            _prefix = 'infra-dumper-oper'
            _revision = '2017-05-05'

            def __init__(self):
                super(Context.All.CrashInfo, self).__init__()

                self.yang_name = "crash-info"
                self.yang_parent_name = "all"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("context-info", ("context_info", Context.All.CrashInfo.ContextInfo)), ("crash-package-information", ("crash_package_information", Context.All.CrashInfo.CrashPackageInformation))])
                self._leafs = OrderedDict([
                    ('node', (YLeaf(YType.str, 'node'), ['str'])),
                ])
                self.node = None

                self.context_info = YList(self)
                self.crash_package_information = YList(self)
                self._segment_path = lambda: "crash-info"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-dumper-oper:context/all/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Context.All.CrashInfo, ['node'], name, value)


            class ContextInfo(Entity):
                """
                Context Information
                
                .. attribute:: process_name
                
                	Process name
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: pid
                
                	Process ID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: tid
                
                	Thread ID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: core_dump_time
                
                	Core dump time/Crash time
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: sig_num
                
                	Signal number
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: sin_err_str
                
                	Signal error string
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: sig_send_pid
                
                	Sender pid
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: sig_code
                
                	Signal code
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: sin_info
                
                	Signal info
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: core_for_process
                
                	Core for process at 
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: registers_info
                
                	Registers Info
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: stack_trace
                
                	Stack Trace
                	**type**\: list of  		 :py:class:`StackTrace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.All.CrashInfo.ContextInfo.StackTrace>`
                
                	**config**\: False
                
                .. attribute:: dll_info
                
                	DLL Information
                	**type**\: list of  		 :py:class:`DllInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.All.CrashInfo.ContextInfo.DllInfo>`
                
                	**config**\: False
                
                

                """

                _prefix = 'infra-dumper-oper'
                _revision = '2017-05-05'

                def __init__(self):
                    super(Context.All.CrashInfo.ContextInfo, self).__init__()

                    self.yang_name = "context-info"
                    self.yang_parent_name = "crash-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("stack-trace", ("stack_trace", Context.All.CrashInfo.ContextInfo.StackTrace)), ("dll-info", ("dll_info", Context.All.CrashInfo.ContextInfo.DllInfo))])
                    self._leafs = OrderedDict([
                        ('process_name', (YLeaf(YType.str, 'process-name'), ['str'])),
                        ('pid', (YLeaf(YType.uint32, 'pid'), ['int'])),
                        ('tid', (YLeaf(YType.uint32, 'tid'), ['int'])),
                        ('core_dump_time', (YLeaf(YType.str, 'core-dump-time'), ['str'])),
                        ('sig_num', (YLeaf(YType.uint32, 'sig-num'), ['int'])),
                        ('sin_err_str', (YLeaf(YType.str, 'sin-err-str'), ['str'])),
                        ('sig_send_pid', (YLeaf(YType.uint32, 'sig-send-pid'), ['int'])),
                        ('sig_code', (YLeaf(YType.uint32, 'sig-code'), ['int'])),
                        ('sin_info', (YLeaf(YType.str, 'sin-info'), ['str'])),
                        ('core_for_process', (YLeaf(YType.str, 'core-for-process'), ['str'])),
                        ('registers_info', (YLeaf(YType.str, 'registers-info'), ['str'])),
                    ])
                    self.process_name = None
                    self.pid = None
                    self.tid = None
                    self.core_dump_time = None
                    self.sig_num = None
                    self.sin_err_str = None
                    self.sig_send_pid = None
                    self.sig_code = None
                    self.sin_info = None
                    self.core_for_process = None
                    self.registers_info = None

                    self.stack_trace = YList(self)
                    self.dll_info = YList(self)
                    self._segment_path = lambda: "context-info"
                    self._absolute_path = lambda: "Cisco-IOS-XR-infra-dumper-oper:context/all/crash-info/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Context.All.CrashInfo.ContextInfo, ['process_name', 'pid', 'tid', 'core_dump_time', 'sig_num', 'sin_err_str', 'sig_send_pid', 'sig_code', 'sin_info', 'core_for_process', 'registers_info'], name, value)


                class StackTrace(Entity):
                    """
                    Stack Trace
                    
                    .. attribute:: stack_trace
                    
                    	stack trace
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'infra-dumper-oper'
                    _revision = '2017-05-05'

                    def __init__(self):
                        super(Context.All.CrashInfo.ContextInfo.StackTrace, self).__init__()

                        self.yang_name = "stack-trace"
                        self.yang_parent_name = "context-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('stack_trace', (YLeaf(YType.uint32, 'stack-trace'), ['int'])),
                        ])
                        self.stack_trace = None
                        self._segment_path = lambda: "stack-trace"
                        self._absolute_path = lambda: "Cisco-IOS-XR-infra-dumper-oper:context/all/crash-info/context-info/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Context.All.CrashInfo.ContextInfo.StackTrace, ['stack_trace'], name, value)



                class DllInfo(Entity):
                    """
                    DLL Information
                    
                    .. attribute:: path
                    
                    	DLL Path
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: text_addr
                    
                    	text addr
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: text_size
                    
                    	text size
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: data_addr
                    
                    	data addr
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: data_size
                    
                    	data size
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: version
                    
                    	version
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'infra-dumper-oper'
                    _revision = '2017-05-05'

                    def __init__(self):
                        super(Context.All.CrashInfo.ContextInfo.DllInfo, self).__init__()

                        self.yang_name = "dll-info"
                        self.yang_parent_name = "context-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('path', (YLeaf(YType.str, 'path'), ['str'])),
                            ('text_addr', (YLeaf(YType.uint32, 'text-addr'), ['int'])),
                            ('text_size', (YLeaf(YType.uint32, 'text-size'), ['int'])),
                            ('data_addr', (YLeaf(YType.uint32, 'data-addr'), ['int'])),
                            ('data_size', (YLeaf(YType.uint32, 'data-size'), ['int'])),
                            ('version', (YLeaf(YType.uint32, 'version'), ['int'])),
                        ])
                        self.path = None
                        self.text_addr = None
                        self.text_size = None
                        self.data_addr = None
                        self.data_size = None
                        self.version = None
                        self._segment_path = lambda: "dll-info"
                        self._absolute_path = lambda: "Cisco-IOS-XR-infra-dumper-oper:context/all/crash-info/context-info/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Context.All.CrashInfo.ContextInfo.DllInfo, ['path', 'text_addr', 'text_size', 'data_addr', 'data_size', 'version'], name, value)




            class CrashPackageInformation(Entity):
                """
                Crash Package Information
                
                .. attribute:: name
                
                	Package name
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: source
                
                	Package Source
                	**type**\: str
                
                	**config**\: False
                
                

                """

                _prefix = 'infra-dumper-oper'
                _revision = '2017-05-05'

                def __init__(self):
                    super(Context.All.CrashInfo.CrashPackageInformation, self).__init__()

                    self.yang_name = "crash-package-information"
                    self.yang_parent_name = "crash-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                        ('source', (YLeaf(YType.str, 'source'), ['str'])),
                    ])
                    self.name = None
                    self.source = None
                    self._segment_path = lambda: "crash-package-information"
                    self._absolute_path = lambda: "Cisco-IOS-XR-infra-dumper-oper:context/all/crash-info/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Context.All.CrashInfo.CrashPackageInformation, ['name', 'source'], name, value)




    def clone_ptr(self):
        self._top_entity = Context()
        return self._top_entity



