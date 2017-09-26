""" Cisco_IOS_XR_infra_dumper_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-dumper package operational data.

This module contains definitions
for the following management objects\:
  context\: Core dump configuration commands

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Context(Entity):
    """
    Core dump configuration commands
    
    .. attribute:: all
    
    	context bag
    	**type**\:   :py:class:`All <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.All>`
    
    .. attribute:: context_locations
    
    	Core Context location table
    	**type**\:   :py:class:`ContextLocations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.ContextLocations>`
    
    .. attribute:: context_numbers
    
    	Context number table
    	**type**\:   :py:class:`ContextNumbers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.ContextNumbers>`
    
    

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
        self._child_container_classes = {"all" : ("all", Context.All), "context-locations" : ("context_locations", Context.ContextLocations), "context-numbers" : ("context_numbers", Context.ContextNumbers)}
        self._child_list_classes = {}

        self.all = Context.All()
        self.all.parent = self
        self._children_name_map["all"] = "all"
        self._children_yang_names.add("all")

        self.context_locations = Context.ContextLocations()
        self.context_locations.parent = self
        self._children_name_map["context_locations"] = "context-locations"
        self._children_yang_names.add("context-locations")

        self.context_numbers = Context.ContextNumbers()
        self.context_numbers.parent = self
        self._children_name_map["context_numbers"] = "context-numbers"
        self._children_yang_names.add("context-numbers")
        self._segment_path = lambda: "Cisco-IOS-XR-infra-dumper-oper:context"


    class All(Entity):
        """
        context bag
        
        .. attribute:: crash_info
        
        	All crash info
        	**type**\: list of    :py:class:`CrashInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.All.CrashInfo>`
        
        

        """

        _prefix = 'infra-dumper-oper'
        _revision = '2017-05-05'

        def __init__(self):
            super(Context.All, self).__init__()

            self.yang_name = "all"
            self.yang_parent_name = "context"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"crash-info" : ("crash_info", Context.All.CrashInfo)}

            self.crash_info = YList(self)
            self._segment_path = lambda: "all"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-dumper-oper:context/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Context.All, [], name, value)


        class CrashInfo(Entity):
            """
            All crash info
            
            .. attribute:: context_info
            
            	Context Information
            	**type**\: list of    :py:class:`ContextInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.All.CrashInfo.ContextInfo>`
            
            .. attribute:: crash_package_information
            
            	Crash Package Information
            	**type**\: list of    :py:class:`CrashPackageInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.All.CrashInfo.CrashPackageInformation>`
            
            .. attribute:: node
            
            	Node name
            	**type**\:  str
            
            

            """

            _prefix = 'infra-dumper-oper'
            _revision = '2017-05-05'

            def __init__(self):
                super(Context.All.CrashInfo, self).__init__()

                self.yang_name = "crash-info"
                self.yang_parent_name = "all"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"context-info" : ("context_info", Context.All.CrashInfo.ContextInfo), "crash-package-information" : ("crash_package_information", Context.All.CrashInfo.CrashPackageInformation)}

                self.node = YLeaf(YType.str, "node")

                self.context_info = YList(self)
                self.crash_package_information = YList(self)
                self._segment_path = lambda: "crash-info"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-dumper-oper:context/all/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Context.All.CrashInfo, ['node'], name, value)


            class ContextInfo(Entity):
                """
                Context Information
                
                .. attribute:: core_dump_time
                
                	Core dump time/Crash time
                	**type**\:  str
                
                .. attribute:: core_for_process
                
                	Core for process at 
                	**type**\:  str
                
                .. attribute:: dll_info
                
                	DLL Information
                	**type**\: list of    :py:class:`DllInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.All.CrashInfo.ContextInfo.DllInfo>`
                
                .. attribute:: pid
                
                	Process ID
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: process_name
                
                	Process name
                	**type**\:  str
                
                .. attribute:: registers_info
                
                	Registers Info
                	**type**\:  str
                
                .. attribute:: sig_code
                
                	Signal code
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: sig_num
                
                	Signal number
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: sig_send_pid
                
                	Sender pid
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: sin_err_str
                
                	Signal error string
                	**type**\:  str
                
                .. attribute:: sin_info
                
                	Signal info
                	**type**\:  str
                
                .. attribute:: stack_trace
                
                	Stack Trace
                	**type**\: list of    :py:class:`StackTrace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.All.CrashInfo.ContextInfo.StackTrace>`
                
                .. attribute:: tid
                
                	Thread ID
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'infra-dumper-oper'
                _revision = '2017-05-05'

                def __init__(self):
                    super(Context.All.CrashInfo.ContextInfo, self).__init__()

                    self.yang_name = "context-info"
                    self.yang_parent_name = "crash-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"dll-info" : ("dll_info", Context.All.CrashInfo.ContextInfo.DllInfo), "stack-trace" : ("stack_trace", Context.All.CrashInfo.ContextInfo.StackTrace)}

                    self.core_dump_time = YLeaf(YType.str, "core-dump-time")

                    self.core_for_process = YLeaf(YType.str, "core-for-process")

                    self.pid = YLeaf(YType.uint32, "pid")

                    self.process_name = YLeaf(YType.str, "process-name")

                    self.registers_info = YLeaf(YType.str, "registers-info")

                    self.sig_code = YLeaf(YType.uint32, "sig-code")

                    self.sig_num = YLeaf(YType.uint32, "sig-num")

                    self.sig_send_pid = YLeaf(YType.uint32, "sig-send-pid")

                    self.sin_err_str = YLeaf(YType.str, "sin-err-str")

                    self.sin_info = YLeaf(YType.str, "sin-info")

                    self.tid = YLeaf(YType.uint32, "tid")

                    self.dll_info = YList(self)
                    self.stack_trace = YList(self)
                    self._segment_path = lambda: "context-info"
                    self._absolute_path = lambda: "Cisco-IOS-XR-infra-dumper-oper:context/all/crash-info/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Context.All.CrashInfo.ContextInfo, ['core_dump_time', 'core_for_process', 'pid', 'process_name', 'registers_info', 'sig_code', 'sig_num', 'sig_send_pid', 'sin_err_str', 'sin_info', 'tid'], name, value)


                class DllInfo(Entity):
                    """
                    DLL Information
                    
                    .. attribute:: data_addr
                    
                    	data addr
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: data_size
                    
                    	data size
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: path
                    
                    	DLL Path
                    	**type**\:  str
                    
                    .. attribute:: text_addr
                    
                    	text addr
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: text_size
                    
                    	text size
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: version
                    
                    	version
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-dumper-oper'
                    _revision = '2017-05-05'

                    def __init__(self):
                        super(Context.All.CrashInfo.ContextInfo.DllInfo, self).__init__()

                        self.yang_name = "dll-info"
                        self.yang_parent_name = "context-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.data_addr = YLeaf(YType.uint32, "data-addr")

                        self.data_size = YLeaf(YType.uint32, "data-size")

                        self.path = YLeaf(YType.str, "path")

                        self.text_addr = YLeaf(YType.uint32, "text-addr")

                        self.text_size = YLeaf(YType.uint32, "text-size")

                        self.version = YLeaf(YType.uint32, "version")
                        self._segment_path = lambda: "dll-info"
                        self._absolute_path = lambda: "Cisco-IOS-XR-infra-dumper-oper:context/all/crash-info/context-info/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Context.All.CrashInfo.ContextInfo.DllInfo, ['data_addr', 'data_size', 'path', 'text_addr', 'text_size', 'version'], name, value)


                class StackTrace(Entity):
                    """
                    Stack Trace
                    
                    .. attribute:: stack_trace
                    
                    	stack trace
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-dumper-oper'
                    _revision = '2017-05-05'

                    def __init__(self):
                        super(Context.All.CrashInfo.ContextInfo.StackTrace, self).__init__()

                        self.yang_name = "stack-trace"
                        self.yang_parent_name = "context-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.stack_trace = YLeaf(YType.uint32, "stack-trace")
                        self._segment_path = lambda: "stack-trace"
                        self._absolute_path = lambda: "Cisco-IOS-XR-infra-dumper-oper:context/all/crash-info/context-info/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Context.All.CrashInfo.ContextInfo.StackTrace, ['stack_trace'], name, value)


            class CrashPackageInformation(Entity):
                """
                Crash Package Information
                
                .. attribute:: name
                
                	Package name
                	**type**\:  str
                
                .. attribute:: source
                
                	Package Source
                	**type**\:  str
                
                

                """

                _prefix = 'infra-dumper-oper'
                _revision = '2017-05-05'

                def __init__(self):
                    super(Context.All.CrashInfo.CrashPackageInformation, self).__init__()

                    self.yang_name = "crash-package-information"
                    self.yang_parent_name = "crash-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.name = YLeaf(YType.str, "name")

                    self.source = YLeaf(YType.str, "source")
                    self._segment_path = lambda: "crash-package-information"
                    self._absolute_path = lambda: "Cisco-IOS-XR-infra-dumper-oper:context/all/crash-info/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Context.All.CrashInfo.CrashPackageInformation, ['name', 'source'], name, value)


    class ContextLocations(Entity):
        """
        Core Context location table
        
        .. attribute:: context_location
        
        	Operational Context for a particular location
        	**type**\: list of    :py:class:`ContextLocation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.ContextLocations.ContextLocation>`
        
        

        """

        _prefix = 'infra-dumper-oper'
        _revision = '2017-05-05'

        def __init__(self):
            super(Context.ContextLocations, self).__init__()

            self.yang_name = "context-locations"
            self.yang_parent_name = "context"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"context-location" : ("context_location", Context.ContextLocations.ContextLocation)}

            self.context_location = YList(self)
            self._segment_path = lambda: "context-locations"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-dumper-oper:context/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Context.ContextLocations, [], name, value)


        class ContextLocation(Entity):
            """
            Operational Context for a particular location
            
            .. attribute:: node_name  <key>
            
            	The node
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: all
            
            	context bag
            	**type**\:   :py:class:`All <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.ContextLocations.ContextLocation.All>`
            
            .. attribute:: numbers
            
            	Context number Table
            	**type**\:   :py:class:`Numbers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.ContextLocations.ContextLocation.Numbers>`
            
            

            """

            _prefix = 'infra-dumper-oper'
            _revision = '2017-05-05'

            def __init__(self):
                super(Context.ContextLocations.ContextLocation, self).__init__()

                self.yang_name = "context-location"
                self.yang_parent_name = "context-locations"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"all" : ("all", Context.ContextLocations.ContextLocation.All), "numbers" : ("numbers", Context.ContextLocations.ContextLocation.Numbers)}
                self._child_list_classes = {}

                self.node_name = YLeaf(YType.str, "node-name")

                self.all = Context.ContextLocations.ContextLocation.All()
                self.all.parent = self
                self._children_name_map["all"] = "all"
                self._children_yang_names.add("all")

                self.numbers = Context.ContextLocations.ContextLocation.Numbers()
                self.numbers.parent = self
                self._children_name_map["numbers"] = "numbers"
                self._children_yang_names.add("numbers")
                self._segment_path = lambda: "context-location" + "[node-name='" + self.node_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-dumper-oper:context/context-locations/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Context.ContextLocations.ContextLocation, ['node_name'], name, value)


            class All(Entity):
                """
                context bag
                
                .. attribute:: crash_info
                
                	All crash info
                	**type**\: list of    :py:class:`CrashInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.ContextLocations.ContextLocation.All.CrashInfo>`
                
                

                """

                _prefix = 'infra-dumper-oper'
                _revision = '2017-05-05'

                def __init__(self):
                    super(Context.ContextLocations.ContextLocation.All, self).__init__()

                    self.yang_name = "all"
                    self.yang_parent_name = "context-location"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"crash-info" : ("crash_info", Context.ContextLocations.ContextLocation.All.CrashInfo)}

                    self.crash_info = YList(self)
                    self._segment_path = lambda: "all"

                def __setattr__(self, name, value):
                    self._perform_setattr(Context.ContextLocations.ContextLocation.All, [], name, value)


                class CrashInfo(Entity):
                    """
                    All crash info
                    
                    .. attribute:: context_info
                    
                    	Context Information
                    	**type**\: list of    :py:class:`ContextInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.ContextLocations.ContextLocation.All.CrashInfo.ContextInfo>`
                    
                    .. attribute:: crash_package_information
                    
                    	Crash Package Information
                    	**type**\: list of    :py:class:`CrashPackageInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.ContextLocations.ContextLocation.All.CrashInfo.CrashPackageInformation>`
                    
                    .. attribute:: node
                    
                    	Node name
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'infra-dumper-oper'
                    _revision = '2017-05-05'

                    def __init__(self):
                        super(Context.ContextLocations.ContextLocation.All.CrashInfo, self).__init__()

                        self.yang_name = "crash-info"
                        self.yang_parent_name = "all"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"context-info" : ("context_info", Context.ContextLocations.ContextLocation.All.CrashInfo.ContextInfo), "crash-package-information" : ("crash_package_information", Context.ContextLocations.ContextLocation.All.CrashInfo.CrashPackageInformation)}

                        self.node = YLeaf(YType.str, "node")

                        self.context_info = YList(self)
                        self.crash_package_information = YList(self)
                        self._segment_path = lambda: "crash-info"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Context.ContextLocations.ContextLocation.All.CrashInfo, ['node'], name, value)


                    class ContextInfo(Entity):
                        """
                        Context Information
                        
                        .. attribute:: core_dump_time
                        
                        	Core dump time/Crash time
                        	**type**\:  str
                        
                        .. attribute:: core_for_process
                        
                        	Core for process at 
                        	**type**\:  str
                        
                        .. attribute:: dll_info
                        
                        	DLL Information
                        	**type**\: list of    :py:class:`DllInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.ContextLocations.ContextLocation.All.CrashInfo.ContextInfo.DllInfo>`
                        
                        .. attribute:: pid
                        
                        	Process ID
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: process_name
                        
                        	Process name
                        	**type**\:  str
                        
                        .. attribute:: registers_info
                        
                        	Registers Info
                        	**type**\:  str
                        
                        .. attribute:: sig_code
                        
                        	Signal code
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sig_num
                        
                        	Signal number
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sig_send_pid
                        
                        	Sender pid
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sin_err_str
                        
                        	Signal error string
                        	**type**\:  str
                        
                        .. attribute:: sin_info
                        
                        	Signal info
                        	**type**\:  str
                        
                        .. attribute:: stack_trace
                        
                        	Stack Trace
                        	**type**\: list of    :py:class:`StackTrace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.ContextLocations.ContextLocation.All.CrashInfo.ContextInfo.StackTrace>`
                        
                        .. attribute:: tid
                        
                        	Thread ID
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'infra-dumper-oper'
                        _revision = '2017-05-05'

                        def __init__(self):
                            super(Context.ContextLocations.ContextLocation.All.CrashInfo.ContextInfo, self).__init__()

                            self.yang_name = "context-info"
                            self.yang_parent_name = "crash-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"dll-info" : ("dll_info", Context.ContextLocations.ContextLocation.All.CrashInfo.ContextInfo.DllInfo), "stack-trace" : ("stack_trace", Context.ContextLocations.ContextLocation.All.CrashInfo.ContextInfo.StackTrace)}

                            self.core_dump_time = YLeaf(YType.str, "core-dump-time")

                            self.core_for_process = YLeaf(YType.str, "core-for-process")

                            self.pid = YLeaf(YType.uint32, "pid")

                            self.process_name = YLeaf(YType.str, "process-name")

                            self.registers_info = YLeaf(YType.str, "registers-info")

                            self.sig_code = YLeaf(YType.uint32, "sig-code")

                            self.sig_num = YLeaf(YType.uint32, "sig-num")

                            self.sig_send_pid = YLeaf(YType.uint32, "sig-send-pid")

                            self.sin_err_str = YLeaf(YType.str, "sin-err-str")

                            self.sin_info = YLeaf(YType.str, "sin-info")

                            self.tid = YLeaf(YType.uint32, "tid")

                            self.dll_info = YList(self)
                            self.stack_trace = YList(self)
                            self._segment_path = lambda: "context-info"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Context.ContextLocations.ContextLocation.All.CrashInfo.ContextInfo, ['core_dump_time', 'core_for_process', 'pid', 'process_name', 'registers_info', 'sig_code', 'sig_num', 'sig_send_pid', 'sin_err_str', 'sin_info', 'tid'], name, value)


                        class DllInfo(Entity):
                            """
                            DLL Information
                            
                            .. attribute:: data_addr
                            
                            	data addr
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: data_size
                            
                            	data size
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: path
                            
                            	DLL Path
                            	**type**\:  str
                            
                            .. attribute:: text_addr
                            
                            	text addr
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: text_size
                            
                            	text size
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: version
                            
                            	version
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'infra-dumper-oper'
                            _revision = '2017-05-05'

                            def __init__(self):
                                super(Context.ContextLocations.ContextLocation.All.CrashInfo.ContextInfo.DllInfo, self).__init__()

                                self.yang_name = "dll-info"
                                self.yang_parent_name = "context-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.data_addr = YLeaf(YType.uint32, "data-addr")

                                self.data_size = YLeaf(YType.uint32, "data-size")

                                self.path = YLeaf(YType.str, "path")

                                self.text_addr = YLeaf(YType.uint32, "text-addr")

                                self.text_size = YLeaf(YType.uint32, "text-size")

                                self.version = YLeaf(YType.uint32, "version")
                                self._segment_path = lambda: "dll-info"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Context.ContextLocations.ContextLocation.All.CrashInfo.ContextInfo.DllInfo, ['data_addr', 'data_size', 'path', 'text_addr', 'text_size', 'version'], name, value)


                        class StackTrace(Entity):
                            """
                            Stack Trace
                            
                            .. attribute:: stack_trace
                            
                            	stack trace
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'infra-dumper-oper'
                            _revision = '2017-05-05'

                            def __init__(self):
                                super(Context.ContextLocations.ContextLocation.All.CrashInfo.ContextInfo.StackTrace, self).__init__()

                                self.yang_name = "stack-trace"
                                self.yang_parent_name = "context-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.stack_trace = YLeaf(YType.uint32, "stack-trace")
                                self._segment_path = lambda: "stack-trace"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Context.ContextLocations.ContextLocation.All.CrashInfo.ContextInfo.StackTrace, ['stack_trace'], name, value)


                    class CrashPackageInformation(Entity):
                        """
                        Crash Package Information
                        
                        .. attribute:: name
                        
                        	Package name
                        	**type**\:  str
                        
                        .. attribute:: source
                        
                        	Package Source
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'infra-dumper-oper'
                        _revision = '2017-05-05'

                        def __init__(self):
                            super(Context.ContextLocations.ContextLocation.All.CrashInfo.CrashPackageInformation, self).__init__()

                            self.yang_name = "crash-package-information"
                            self.yang_parent_name = "crash-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.name = YLeaf(YType.str, "name")

                            self.source = YLeaf(YType.str, "source")
                            self._segment_path = lambda: "crash-package-information"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Context.ContextLocations.ContextLocation.All.CrashInfo.CrashPackageInformation, ['name', 'source'], name, value)


            class Numbers(Entity):
                """
                Context number Table
                
                .. attribute:: number
                
                	Context number
                	**type**\: list of    :py:class:`Number <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.ContextLocations.ContextLocation.Numbers.Number>`
                
                

                """

                _prefix = 'infra-dumper-oper'
                _revision = '2017-05-05'

                def __init__(self):
                    super(Context.ContextLocations.ContextLocation.Numbers, self).__init__()

                    self.yang_name = "numbers"
                    self.yang_parent_name = "context-location"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"number" : ("number", Context.ContextLocations.ContextLocation.Numbers.Number)}

                    self.number = YList(self)
                    self._segment_path = lambda: "numbers"

                def __setattr__(self, name, value):
                    self._perform_setattr(Context.ContextLocations.ContextLocation.Numbers, [], name, value)


                class Number(Entity):
                    """
                    Context number
                    
                    .. attribute:: context_num  <key>
                    
                    	Context for which crash dump info required
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: enter
                    
                    	Context info bag
                    	**type**\:   :py:class:`Enter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.ContextLocations.ContextLocation.Numbers.Number.Enter>`
                    
                    

                    """

                    _prefix = 'infra-dumper-oper'
                    _revision = '2017-05-05'

                    def __init__(self):
                        super(Context.ContextLocations.ContextLocation.Numbers.Number, self).__init__()

                        self.yang_name = "number"
                        self.yang_parent_name = "numbers"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"enter" : ("enter", Context.ContextLocations.ContextLocation.Numbers.Number.Enter)}
                        self._child_list_classes = {}

                        self.context_num = YLeaf(YType.int32, "context-num")

                        self.enter = Context.ContextLocations.ContextLocation.Numbers.Number.Enter()
                        self.enter.parent = self
                        self._children_name_map["enter"] = "enter"
                        self._children_yang_names.add("enter")
                        self._segment_path = lambda: "number" + "[context-num='" + self.context_num.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Context.ContextLocations.ContextLocation.Numbers.Number, ['context_num'], name, value)


                    class Enter(Entity):
                        """
                        Context info bag
                        
                        .. attribute:: crash_info
                        
                        	All crash info
                        	**type**\: list of    :py:class:`CrashInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.ContextLocations.ContextLocation.Numbers.Number.Enter.CrashInfo>`
                        
                        

                        """

                        _prefix = 'infra-dumper-oper'
                        _revision = '2017-05-05'

                        def __init__(self):
                            super(Context.ContextLocations.ContextLocation.Numbers.Number.Enter, self).__init__()

                            self.yang_name = "enter"
                            self.yang_parent_name = "number"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"crash-info" : ("crash_info", Context.ContextLocations.ContextLocation.Numbers.Number.Enter.CrashInfo)}

                            self.crash_info = YList(self)
                            self._segment_path = lambda: "enter"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Context.ContextLocations.ContextLocation.Numbers.Number.Enter, [], name, value)


                        class CrashInfo(Entity):
                            """
                            All crash info
                            
                            .. attribute:: context_info
                            
                            	Context Information
                            	**type**\: list of    :py:class:`ContextInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.ContextLocations.ContextLocation.Numbers.Number.Enter.CrashInfo.ContextInfo>`
                            
                            .. attribute:: crash_package_information
                            
                            	Crash Package Information
                            	**type**\: list of    :py:class:`CrashPackageInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.ContextLocations.ContextLocation.Numbers.Number.Enter.CrashInfo.CrashPackageInformation>`
                            
                            .. attribute:: node
                            
                            	Node name
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'infra-dumper-oper'
                            _revision = '2017-05-05'

                            def __init__(self):
                                super(Context.ContextLocations.ContextLocation.Numbers.Number.Enter.CrashInfo, self).__init__()

                                self.yang_name = "crash-info"
                                self.yang_parent_name = "enter"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"context-info" : ("context_info", Context.ContextLocations.ContextLocation.Numbers.Number.Enter.CrashInfo.ContextInfo), "crash-package-information" : ("crash_package_information", Context.ContextLocations.ContextLocation.Numbers.Number.Enter.CrashInfo.CrashPackageInformation)}

                                self.node = YLeaf(YType.str, "node")

                                self.context_info = YList(self)
                                self.crash_package_information = YList(self)
                                self._segment_path = lambda: "crash-info"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Context.ContextLocations.ContextLocation.Numbers.Number.Enter.CrashInfo, ['node'], name, value)


                            class ContextInfo(Entity):
                                """
                                Context Information
                                
                                .. attribute:: core_dump_time
                                
                                	Core dump time/Crash time
                                	**type**\:  str
                                
                                .. attribute:: core_for_process
                                
                                	Core for process at 
                                	**type**\:  str
                                
                                .. attribute:: dll_info
                                
                                	DLL Information
                                	**type**\: list of    :py:class:`DllInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.ContextLocations.ContextLocation.Numbers.Number.Enter.CrashInfo.ContextInfo.DllInfo>`
                                
                                .. attribute:: pid
                                
                                	Process ID
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: process_name
                                
                                	Process name
                                	**type**\:  str
                                
                                .. attribute:: registers_info
                                
                                	Registers Info
                                	**type**\:  str
                                
                                .. attribute:: sig_code
                                
                                	Signal code
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: sig_num
                                
                                	Signal number
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: sig_send_pid
                                
                                	Sender pid
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: sin_err_str
                                
                                	Signal error string
                                	**type**\:  str
                                
                                .. attribute:: sin_info
                                
                                	Signal info
                                	**type**\:  str
                                
                                .. attribute:: stack_trace
                                
                                	Stack Trace
                                	**type**\: list of    :py:class:`StackTrace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.ContextLocations.ContextLocation.Numbers.Number.Enter.CrashInfo.ContextInfo.StackTrace>`
                                
                                .. attribute:: tid
                                
                                	Thread ID
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'infra-dumper-oper'
                                _revision = '2017-05-05'

                                def __init__(self):
                                    super(Context.ContextLocations.ContextLocation.Numbers.Number.Enter.CrashInfo.ContextInfo, self).__init__()

                                    self.yang_name = "context-info"
                                    self.yang_parent_name = "crash-info"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"dll-info" : ("dll_info", Context.ContextLocations.ContextLocation.Numbers.Number.Enter.CrashInfo.ContextInfo.DllInfo), "stack-trace" : ("stack_trace", Context.ContextLocations.ContextLocation.Numbers.Number.Enter.CrashInfo.ContextInfo.StackTrace)}

                                    self.core_dump_time = YLeaf(YType.str, "core-dump-time")

                                    self.core_for_process = YLeaf(YType.str, "core-for-process")

                                    self.pid = YLeaf(YType.uint32, "pid")

                                    self.process_name = YLeaf(YType.str, "process-name")

                                    self.registers_info = YLeaf(YType.str, "registers-info")

                                    self.sig_code = YLeaf(YType.uint32, "sig-code")

                                    self.sig_num = YLeaf(YType.uint32, "sig-num")

                                    self.sig_send_pid = YLeaf(YType.uint32, "sig-send-pid")

                                    self.sin_err_str = YLeaf(YType.str, "sin-err-str")

                                    self.sin_info = YLeaf(YType.str, "sin-info")

                                    self.tid = YLeaf(YType.uint32, "tid")

                                    self.dll_info = YList(self)
                                    self.stack_trace = YList(self)
                                    self._segment_path = lambda: "context-info"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Context.ContextLocations.ContextLocation.Numbers.Number.Enter.CrashInfo.ContextInfo, ['core_dump_time', 'core_for_process', 'pid', 'process_name', 'registers_info', 'sig_code', 'sig_num', 'sig_send_pid', 'sin_err_str', 'sin_info', 'tid'], name, value)


                                class DllInfo(Entity):
                                    """
                                    DLL Information
                                    
                                    .. attribute:: data_addr
                                    
                                    	data addr
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: data_size
                                    
                                    	data size
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: path
                                    
                                    	DLL Path
                                    	**type**\:  str
                                    
                                    .. attribute:: text_addr
                                    
                                    	text addr
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: text_size
                                    
                                    	text size
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: version
                                    
                                    	version
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'infra-dumper-oper'
                                    _revision = '2017-05-05'

                                    def __init__(self):
                                        super(Context.ContextLocations.ContextLocation.Numbers.Number.Enter.CrashInfo.ContextInfo.DllInfo, self).__init__()

                                        self.yang_name = "dll-info"
                                        self.yang_parent_name = "context-info"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.data_addr = YLeaf(YType.uint32, "data-addr")

                                        self.data_size = YLeaf(YType.uint32, "data-size")

                                        self.path = YLeaf(YType.str, "path")

                                        self.text_addr = YLeaf(YType.uint32, "text-addr")

                                        self.text_size = YLeaf(YType.uint32, "text-size")

                                        self.version = YLeaf(YType.uint32, "version")
                                        self._segment_path = lambda: "dll-info"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Context.ContextLocations.ContextLocation.Numbers.Number.Enter.CrashInfo.ContextInfo.DllInfo, ['data_addr', 'data_size', 'path', 'text_addr', 'text_size', 'version'], name, value)


                                class StackTrace(Entity):
                                    """
                                    Stack Trace
                                    
                                    .. attribute:: stack_trace
                                    
                                    	stack trace
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'infra-dumper-oper'
                                    _revision = '2017-05-05'

                                    def __init__(self):
                                        super(Context.ContextLocations.ContextLocation.Numbers.Number.Enter.CrashInfo.ContextInfo.StackTrace, self).__init__()

                                        self.yang_name = "stack-trace"
                                        self.yang_parent_name = "context-info"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.stack_trace = YLeaf(YType.uint32, "stack-trace")
                                        self._segment_path = lambda: "stack-trace"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Context.ContextLocations.ContextLocation.Numbers.Number.Enter.CrashInfo.ContextInfo.StackTrace, ['stack_trace'], name, value)


                            class CrashPackageInformation(Entity):
                                """
                                Crash Package Information
                                
                                .. attribute:: name
                                
                                	Package name
                                	**type**\:  str
                                
                                .. attribute:: source
                                
                                	Package Source
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'infra-dumper-oper'
                                _revision = '2017-05-05'

                                def __init__(self):
                                    super(Context.ContextLocations.ContextLocation.Numbers.Number.Enter.CrashInfo.CrashPackageInformation, self).__init__()

                                    self.yang_name = "crash-package-information"
                                    self.yang_parent_name = "crash-info"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.name = YLeaf(YType.str, "name")

                                    self.source = YLeaf(YType.str, "source")
                                    self._segment_path = lambda: "crash-package-information"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Context.ContextLocations.ContextLocation.Numbers.Number.Enter.CrashInfo.CrashPackageInformation, ['name', 'source'], name, value)


    class ContextNumbers(Entity):
        """
        Context number table
        
        .. attribute:: context_number
        
        	Context number 
        	**type**\: list of    :py:class:`ContextNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.ContextNumbers.ContextNumber>`
        
        

        """

        _prefix = 'infra-dumper-oper'
        _revision = '2017-05-05'

        def __init__(self):
            super(Context.ContextNumbers, self).__init__()

            self.yang_name = "context-numbers"
            self.yang_parent_name = "context"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"context-number" : ("context_number", Context.ContextNumbers.ContextNumber)}

            self.context_number = YList(self)
            self._segment_path = lambda: "context-numbers"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-dumper-oper:context/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Context.ContextNumbers, [], name, value)


        class ContextNumber(Entity):
            """
            Context number 
            
            .. attribute:: context_num  <key>
            
            	Context for which crash dump info required
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: all
            
            	context bag
            	**type**\:   :py:class:`All <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.ContextNumbers.ContextNumber.All>`
            
            .. attribute:: locations
            
            	Core Context location table
            	**type**\:   :py:class:`Locations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.ContextNumbers.ContextNumber.Locations>`
            
            

            """

            _prefix = 'infra-dumper-oper'
            _revision = '2017-05-05'

            def __init__(self):
                super(Context.ContextNumbers.ContextNumber, self).__init__()

                self.yang_name = "context-number"
                self.yang_parent_name = "context-numbers"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"all" : ("all", Context.ContextNumbers.ContextNumber.All), "locations" : ("locations", Context.ContextNumbers.ContextNumber.Locations)}
                self._child_list_classes = {}

                self.context_num = YLeaf(YType.int32, "context-num")

                self.all = Context.ContextNumbers.ContextNumber.All()
                self.all.parent = self
                self._children_name_map["all"] = "all"
                self._children_yang_names.add("all")

                self.locations = Context.ContextNumbers.ContextNumber.Locations()
                self.locations.parent = self
                self._children_name_map["locations"] = "locations"
                self._children_yang_names.add("locations")
                self._segment_path = lambda: "context-number" + "[context-num='" + self.context_num.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-dumper-oper:context/context-numbers/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Context.ContextNumbers.ContextNumber, ['context_num'], name, value)


            class All(Entity):
                """
                context bag
                
                .. attribute:: crash_info
                
                	All crash info
                	**type**\: list of    :py:class:`CrashInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.ContextNumbers.ContextNumber.All.CrashInfo>`
                
                

                """

                _prefix = 'infra-dumper-oper'
                _revision = '2017-05-05'

                def __init__(self):
                    super(Context.ContextNumbers.ContextNumber.All, self).__init__()

                    self.yang_name = "all"
                    self.yang_parent_name = "context-number"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"crash-info" : ("crash_info", Context.ContextNumbers.ContextNumber.All.CrashInfo)}

                    self.crash_info = YList(self)
                    self._segment_path = lambda: "all"

                def __setattr__(self, name, value):
                    self._perform_setattr(Context.ContextNumbers.ContextNumber.All, [], name, value)


                class CrashInfo(Entity):
                    """
                    All crash info
                    
                    .. attribute:: context_info
                    
                    	Context Information
                    	**type**\: list of    :py:class:`ContextInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.ContextNumbers.ContextNumber.All.CrashInfo.ContextInfo>`
                    
                    .. attribute:: crash_package_information
                    
                    	Crash Package Information
                    	**type**\: list of    :py:class:`CrashPackageInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.ContextNumbers.ContextNumber.All.CrashInfo.CrashPackageInformation>`
                    
                    .. attribute:: node
                    
                    	Node name
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'infra-dumper-oper'
                    _revision = '2017-05-05'

                    def __init__(self):
                        super(Context.ContextNumbers.ContextNumber.All.CrashInfo, self).__init__()

                        self.yang_name = "crash-info"
                        self.yang_parent_name = "all"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"context-info" : ("context_info", Context.ContextNumbers.ContextNumber.All.CrashInfo.ContextInfo), "crash-package-information" : ("crash_package_information", Context.ContextNumbers.ContextNumber.All.CrashInfo.CrashPackageInformation)}

                        self.node = YLeaf(YType.str, "node")

                        self.context_info = YList(self)
                        self.crash_package_information = YList(self)
                        self._segment_path = lambda: "crash-info"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Context.ContextNumbers.ContextNumber.All.CrashInfo, ['node'], name, value)


                    class ContextInfo(Entity):
                        """
                        Context Information
                        
                        .. attribute:: core_dump_time
                        
                        	Core dump time/Crash time
                        	**type**\:  str
                        
                        .. attribute:: core_for_process
                        
                        	Core for process at 
                        	**type**\:  str
                        
                        .. attribute:: dll_info
                        
                        	DLL Information
                        	**type**\: list of    :py:class:`DllInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.ContextNumbers.ContextNumber.All.CrashInfo.ContextInfo.DllInfo>`
                        
                        .. attribute:: pid
                        
                        	Process ID
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: process_name
                        
                        	Process name
                        	**type**\:  str
                        
                        .. attribute:: registers_info
                        
                        	Registers Info
                        	**type**\:  str
                        
                        .. attribute:: sig_code
                        
                        	Signal code
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sig_num
                        
                        	Signal number
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sig_send_pid
                        
                        	Sender pid
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sin_err_str
                        
                        	Signal error string
                        	**type**\:  str
                        
                        .. attribute:: sin_info
                        
                        	Signal info
                        	**type**\:  str
                        
                        .. attribute:: stack_trace
                        
                        	Stack Trace
                        	**type**\: list of    :py:class:`StackTrace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.ContextNumbers.ContextNumber.All.CrashInfo.ContextInfo.StackTrace>`
                        
                        .. attribute:: tid
                        
                        	Thread ID
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'infra-dumper-oper'
                        _revision = '2017-05-05'

                        def __init__(self):
                            super(Context.ContextNumbers.ContextNumber.All.CrashInfo.ContextInfo, self).__init__()

                            self.yang_name = "context-info"
                            self.yang_parent_name = "crash-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"dll-info" : ("dll_info", Context.ContextNumbers.ContextNumber.All.CrashInfo.ContextInfo.DllInfo), "stack-trace" : ("stack_trace", Context.ContextNumbers.ContextNumber.All.CrashInfo.ContextInfo.StackTrace)}

                            self.core_dump_time = YLeaf(YType.str, "core-dump-time")

                            self.core_for_process = YLeaf(YType.str, "core-for-process")

                            self.pid = YLeaf(YType.uint32, "pid")

                            self.process_name = YLeaf(YType.str, "process-name")

                            self.registers_info = YLeaf(YType.str, "registers-info")

                            self.sig_code = YLeaf(YType.uint32, "sig-code")

                            self.sig_num = YLeaf(YType.uint32, "sig-num")

                            self.sig_send_pid = YLeaf(YType.uint32, "sig-send-pid")

                            self.sin_err_str = YLeaf(YType.str, "sin-err-str")

                            self.sin_info = YLeaf(YType.str, "sin-info")

                            self.tid = YLeaf(YType.uint32, "tid")

                            self.dll_info = YList(self)
                            self.stack_trace = YList(self)
                            self._segment_path = lambda: "context-info"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Context.ContextNumbers.ContextNumber.All.CrashInfo.ContextInfo, ['core_dump_time', 'core_for_process', 'pid', 'process_name', 'registers_info', 'sig_code', 'sig_num', 'sig_send_pid', 'sin_err_str', 'sin_info', 'tid'], name, value)


                        class DllInfo(Entity):
                            """
                            DLL Information
                            
                            .. attribute:: data_addr
                            
                            	data addr
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: data_size
                            
                            	data size
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: path
                            
                            	DLL Path
                            	**type**\:  str
                            
                            .. attribute:: text_addr
                            
                            	text addr
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: text_size
                            
                            	text size
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: version
                            
                            	version
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'infra-dumper-oper'
                            _revision = '2017-05-05'

                            def __init__(self):
                                super(Context.ContextNumbers.ContextNumber.All.CrashInfo.ContextInfo.DllInfo, self).__init__()

                                self.yang_name = "dll-info"
                                self.yang_parent_name = "context-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.data_addr = YLeaf(YType.uint32, "data-addr")

                                self.data_size = YLeaf(YType.uint32, "data-size")

                                self.path = YLeaf(YType.str, "path")

                                self.text_addr = YLeaf(YType.uint32, "text-addr")

                                self.text_size = YLeaf(YType.uint32, "text-size")

                                self.version = YLeaf(YType.uint32, "version")
                                self._segment_path = lambda: "dll-info"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Context.ContextNumbers.ContextNumber.All.CrashInfo.ContextInfo.DllInfo, ['data_addr', 'data_size', 'path', 'text_addr', 'text_size', 'version'], name, value)


                        class StackTrace(Entity):
                            """
                            Stack Trace
                            
                            .. attribute:: stack_trace
                            
                            	stack trace
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'infra-dumper-oper'
                            _revision = '2017-05-05'

                            def __init__(self):
                                super(Context.ContextNumbers.ContextNumber.All.CrashInfo.ContextInfo.StackTrace, self).__init__()

                                self.yang_name = "stack-trace"
                                self.yang_parent_name = "context-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.stack_trace = YLeaf(YType.uint32, "stack-trace")
                                self._segment_path = lambda: "stack-trace"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Context.ContextNumbers.ContextNumber.All.CrashInfo.ContextInfo.StackTrace, ['stack_trace'], name, value)


                    class CrashPackageInformation(Entity):
                        """
                        Crash Package Information
                        
                        .. attribute:: name
                        
                        	Package name
                        	**type**\:  str
                        
                        .. attribute:: source
                        
                        	Package Source
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'infra-dumper-oper'
                        _revision = '2017-05-05'

                        def __init__(self):
                            super(Context.ContextNumbers.ContextNumber.All.CrashInfo.CrashPackageInformation, self).__init__()

                            self.yang_name = "crash-package-information"
                            self.yang_parent_name = "crash-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.name = YLeaf(YType.str, "name")

                            self.source = YLeaf(YType.str, "source")
                            self._segment_path = lambda: "crash-package-information"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Context.ContextNumbers.ContextNumber.All.CrashInfo.CrashPackageInformation, ['name', 'source'], name, value)


            class Locations(Entity):
                """
                Core Context location table
                
                .. attribute:: location
                
                	Operational Context for a particular location
                	**type**\: list of    :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.ContextNumbers.ContextNumber.Locations.Location>`
                
                

                """

                _prefix = 'infra-dumper-oper'
                _revision = '2017-05-05'

                def __init__(self):
                    super(Context.ContextNumbers.ContextNumber.Locations, self).__init__()

                    self.yang_name = "locations"
                    self.yang_parent_name = "context-number"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"location" : ("location", Context.ContextNumbers.ContextNumber.Locations.Location)}

                    self.location = YList(self)
                    self._segment_path = lambda: "locations"

                def __setattr__(self, name, value):
                    self._perform_setattr(Context.ContextNumbers.ContextNumber.Locations, [], name, value)


                class Location(Entity):
                    """
                    Operational Context for a particular location
                    
                    .. attribute:: node_name  <key>
                    
                    	The node
                    	**type**\:  str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    .. attribute:: enter
                    
                    	Context info bag
                    	**type**\:   :py:class:`Enter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.ContextNumbers.ContextNumber.Locations.Location.Enter>`
                    
                    

                    """

                    _prefix = 'infra-dumper-oper'
                    _revision = '2017-05-05'

                    def __init__(self):
                        super(Context.ContextNumbers.ContextNumber.Locations.Location, self).__init__()

                        self.yang_name = "location"
                        self.yang_parent_name = "locations"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"enter" : ("enter", Context.ContextNumbers.ContextNumber.Locations.Location.Enter)}
                        self._child_list_classes = {}

                        self.node_name = YLeaf(YType.str, "node-name")

                        self.enter = Context.ContextNumbers.ContextNumber.Locations.Location.Enter()
                        self.enter.parent = self
                        self._children_name_map["enter"] = "enter"
                        self._children_yang_names.add("enter")
                        self._segment_path = lambda: "location" + "[node-name='" + self.node_name.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Context.ContextNumbers.ContextNumber.Locations.Location, ['node_name'], name, value)


                    class Enter(Entity):
                        """
                        Context info bag
                        
                        .. attribute:: crash_info
                        
                        	All crash info
                        	**type**\: list of    :py:class:`CrashInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.ContextNumbers.ContextNumber.Locations.Location.Enter.CrashInfo>`
                        
                        

                        """

                        _prefix = 'infra-dumper-oper'
                        _revision = '2017-05-05'

                        def __init__(self):
                            super(Context.ContextNumbers.ContextNumber.Locations.Location.Enter, self).__init__()

                            self.yang_name = "enter"
                            self.yang_parent_name = "location"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"crash-info" : ("crash_info", Context.ContextNumbers.ContextNumber.Locations.Location.Enter.CrashInfo)}

                            self.crash_info = YList(self)
                            self._segment_path = lambda: "enter"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Context.ContextNumbers.ContextNumber.Locations.Location.Enter, [], name, value)


                        class CrashInfo(Entity):
                            """
                            All crash info
                            
                            .. attribute:: context_info
                            
                            	Context Information
                            	**type**\: list of    :py:class:`ContextInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.ContextNumbers.ContextNumber.Locations.Location.Enter.CrashInfo.ContextInfo>`
                            
                            .. attribute:: crash_package_information
                            
                            	Crash Package Information
                            	**type**\: list of    :py:class:`CrashPackageInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.ContextNumbers.ContextNumber.Locations.Location.Enter.CrashInfo.CrashPackageInformation>`
                            
                            .. attribute:: node
                            
                            	Node name
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'infra-dumper-oper'
                            _revision = '2017-05-05'

                            def __init__(self):
                                super(Context.ContextNumbers.ContextNumber.Locations.Location.Enter.CrashInfo, self).__init__()

                                self.yang_name = "crash-info"
                                self.yang_parent_name = "enter"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"context-info" : ("context_info", Context.ContextNumbers.ContextNumber.Locations.Location.Enter.CrashInfo.ContextInfo), "crash-package-information" : ("crash_package_information", Context.ContextNumbers.ContextNumber.Locations.Location.Enter.CrashInfo.CrashPackageInformation)}

                                self.node = YLeaf(YType.str, "node")

                                self.context_info = YList(self)
                                self.crash_package_information = YList(self)
                                self._segment_path = lambda: "crash-info"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Context.ContextNumbers.ContextNumber.Locations.Location.Enter.CrashInfo, ['node'], name, value)


                            class ContextInfo(Entity):
                                """
                                Context Information
                                
                                .. attribute:: core_dump_time
                                
                                	Core dump time/Crash time
                                	**type**\:  str
                                
                                .. attribute:: core_for_process
                                
                                	Core for process at 
                                	**type**\:  str
                                
                                .. attribute:: dll_info
                                
                                	DLL Information
                                	**type**\: list of    :py:class:`DllInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.ContextNumbers.ContextNumber.Locations.Location.Enter.CrashInfo.ContextInfo.DllInfo>`
                                
                                .. attribute:: pid
                                
                                	Process ID
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: process_name
                                
                                	Process name
                                	**type**\:  str
                                
                                .. attribute:: registers_info
                                
                                	Registers Info
                                	**type**\:  str
                                
                                .. attribute:: sig_code
                                
                                	Signal code
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: sig_num
                                
                                	Signal number
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: sig_send_pid
                                
                                	Sender pid
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: sin_err_str
                                
                                	Signal error string
                                	**type**\:  str
                                
                                .. attribute:: sin_info
                                
                                	Signal info
                                	**type**\:  str
                                
                                .. attribute:: stack_trace
                                
                                	Stack Trace
                                	**type**\: list of    :py:class:`StackTrace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_oper.Context.ContextNumbers.ContextNumber.Locations.Location.Enter.CrashInfo.ContextInfo.StackTrace>`
                                
                                .. attribute:: tid
                                
                                	Thread ID
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'infra-dumper-oper'
                                _revision = '2017-05-05'

                                def __init__(self):
                                    super(Context.ContextNumbers.ContextNumber.Locations.Location.Enter.CrashInfo.ContextInfo, self).__init__()

                                    self.yang_name = "context-info"
                                    self.yang_parent_name = "crash-info"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"dll-info" : ("dll_info", Context.ContextNumbers.ContextNumber.Locations.Location.Enter.CrashInfo.ContextInfo.DllInfo), "stack-trace" : ("stack_trace", Context.ContextNumbers.ContextNumber.Locations.Location.Enter.CrashInfo.ContextInfo.StackTrace)}

                                    self.core_dump_time = YLeaf(YType.str, "core-dump-time")

                                    self.core_for_process = YLeaf(YType.str, "core-for-process")

                                    self.pid = YLeaf(YType.uint32, "pid")

                                    self.process_name = YLeaf(YType.str, "process-name")

                                    self.registers_info = YLeaf(YType.str, "registers-info")

                                    self.sig_code = YLeaf(YType.uint32, "sig-code")

                                    self.sig_num = YLeaf(YType.uint32, "sig-num")

                                    self.sig_send_pid = YLeaf(YType.uint32, "sig-send-pid")

                                    self.sin_err_str = YLeaf(YType.str, "sin-err-str")

                                    self.sin_info = YLeaf(YType.str, "sin-info")

                                    self.tid = YLeaf(YType.uint32, "tid")

                                    self.dll_info = YList(self)
                                    self.stack_trace = YList(self)
                                    self._segment_path = lambda: "context-info"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Context.ContextNumbers.ContextNumber.Locations.Location.Enter.CrashInfo.ContextInfo, ['core_dump_time', 'core_for_process', 'pid', 'process_name', 'registers_info', 'sig_code', 'sig_num', 'sig_send_pid', 'sin_err_str', 'sin_info', 'tid'], name, value)


                                class DllInfo(Entity):
                                    """
                                    DLL Information
                                    
                                    .. attribute:: data_addr
                                    
                                    	data addr
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: data_size
                                    
                                    	data size
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: path
                                    
                                    	DLL Path
                                    	**type**\:  str
                                    
                                    .. attribute:: text_addr
                                    
                                    	text addr
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: text_size
                                    
                                    	text size
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: version
                                    
                                    	version
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'infra-dumper-oper'
                                    _revision = '2017-05-05'

                                    def __init__(self):
                                        super(Context.ContextNumbers.ContextNumber.Locations.Location.Enter.CrashInfo.ContextInfo.DllInfo, self).__init__()

                                        self.yang_name = "dll-info"
                                        self.yang_parent_name = "context-info"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.data_addr = YLeaf(YType.uint32, "data-addr")

                                        self.data_size = YLeaf(YType.uint32, "data-size")

                                        self.path = YLeaf(YType.str, "path")

                                        self.text_addr = YLeaf(YType.uint32, "text-addr")

                                        self.text_size = YLeaf(YType.uint32, "text-size")

                                        self.version = YLeaf(YType.uint32, "version")
                                        self._segment_path = lambda: "dll-info"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Context.ContextNumbers.ContextNumber.Locations.Location.Enter.CrashInfo.ContextInfo.DllInfo, ['data_addr', 'data_size', 'path', 'text_addr', 'text_size', 'version'], name, value)


                                class StackTrace(Entity):
                                    """
                                    Stack Trace
                                    
                                    .. attribute:: stack_trace
                                    
                                    	stack trace
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'infra-dumper-oper'
                                    _revision = '2017-05-05'

                                    def __init__(self):
                                        super(Context.ContextNumbers.ContextNumber.Locations.Location.Enter.CrashInfo.ContextInfo.StackTrace, self).__init__()

                                        self.yang_name = "stack-trace"
                                        self.yang_parent_name = "context-info"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.stack_trace = YLeaf(YType.uint32, "stack-trace")
                                        self._segment_path = lambda: "stack-trace"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Context.ContextNumbers.ContextNumber.Locations.Location.Enter.CrashInfo.ContextInfo.StackTrace, ['stack_trace'], name, value)


                            class CrashPackageInformation(Entity):
                                """
                                Crash Package Information
                                
                                .. attribute:: name
                                
                                	Package name
                                	**type**\:  str
                                
                                .. attribute:: source
                                
                                	Package Source
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'infra-dumper-oper'
                                _revision = '2017-05-05'

                                def __init__(self):
                                    super(Context.ContextNumbers.ContextNumber.Locations.Location.Enter.CrashInfo.CrashPackageInformation, self).__init__()

                                    self.yang_name = "crash-package-information"
                                    self.yang_parent_name = "crash-info"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.name = YLeaf(YType.str, "name")

                                    self.source = YLeaf(YType.str, "source")
                                    self._segment_path = lambda: "crash-package-information"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Context.ContextNumbers.ContextNumber.Locations.Location.Enter.CrashInfo.CrashPackageInformation, ['name', 'source'], name, value)

    def clone_ptr(self):
        self._top_entity = Context()
        return self._top_entity

