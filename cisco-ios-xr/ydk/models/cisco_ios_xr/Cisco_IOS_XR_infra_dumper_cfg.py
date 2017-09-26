""" Cisco_IOS_XR_infra_dumper_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-dumper package configuration.

This module contains definitions
for the following management objects\:
  exception\: Core dump configuration commands

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Context(Enum):
    """
    Context

    Context

    .. data:: default = 0

    	context not configured

    .. data:: context = 65536

    	Dump context info only: Overrides other options

    	except for 'no-core'

    """

    default = Enum.YLeaf(0, "default")

    context = Enum.YLeaf(65536, "context")


class Copy(Enum):
    """
    Copy

    Copy

    .. data:: default = 0

    	copy not configured

    .. data:: copy = 512

    	Dump to local memory: for time critical

    	processes

    """

    default = Enum.YLeaf(0, "default")

    copy = Enum.YLeaf(512, "copy")


class Mainmemory(Enum):
    """
    Mainmemory

    Mainmemory

    .. data:: default = 0

    	main memory not configured

    .. data:: main_memory = 1

    	Dump main memory of the target process

    """

    default = Enum.YLeaf(0, "default")

    main_memory = Enum.YLeaf(1, "main-memory")


class Nocore(Enum):
    """
    Nocore

    Nocore

    .. data:: default = 0

    	no core not configured

    .. data:: no_core = 131072

    	Disable core dump for the target process:

    	Overrides other options

    """

    default = Enum.YLeaf(0, "default")

    no_core = Enum.YLeaf(131072, "no-core")


class Packetmemory(Enum):
    """
    Packetmemory

    Packetmemory

    .. data:: default = 0

    	packet memory not configured

    .. data:: packet_memory = 8

    	Dump packet memory of the target process

    """

    default = Enum.YLeaf(0, "default")

    packet_memory = Enum.YLeaf(8, "packet-memory")


class Sharedmemory(Enum):
    """
    Sharedmemory

    Sharedmemory

    .. data:: default = 0

    	shared memory not configured

    .. data:: shared_memory = 2

    	Dump shared memory of the target process

    """

    default = Enum.YLeaf(0, "default")

    shared_memory = Enum.YLeaf(2, "shared-memory")


class Skipcpuinfo(Enum):
    """
    Skipcpuinfo

    Skipcpuinfo

    .. data:: default = 0

    	skip-cpu-info not configured

    .. data:: skip_cpu_info = 4096

    	Skip CPU usage snapshot: for time critical

    	processes

    """

    default = Enum.YLeaf(0, "default")

    skip_cpu_info = Enum.YLeaf(4096, "skip-cpu-info")


class Sparse(Enum):
    """
    Sparse

    Sparse

    .. data:: default = 0

    	sparse not configured

    .. data:: sparse = 1024

    	Dump memory relevant to stack trace only: for

    	time critical processes

    """

    default = Enum.YLeaf(0, "default")

    sparse = Enum.YLeaf(1024, "sparse")



class Exception(Entity):
    """
    Core dump configuration commands
    
    .. attribute:: choice1
    
    	Preference of the dump location
    	**type**\:   :py:class:`Choice1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_cfg.Exception.Choice1>`
    
    .. attribute:: choice2
    
    	Preference of the dump location
    	**type**\:   :py:class:`Choice2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_cfg.Exception.Choice2>`
    
    .. attribute:: choice3
    
    	Preference of the dump location
    	**type**\:   :py:class:`Choice3 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_cfg.Exception.Choice3>`
    
    .. attribute:: core_size
    
    	Only print out stack trace and create no core file beyond this size
    	**type**\:  int
    
    	**range:** 1..4095
    
    .. attribute:: core_verification
    
    	Disable core file verification
    	**type**\:  bool
    
    .. attribute:: kernel_debugger
    
    	Enable kernel debugger
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: memory_threshold
    
    	Give up core dump if specified free memory can not be secured
    	**type**\:  int
    
    	**range:** 3..40
    
    	**units**\: percentage
    
    .. attribute:: packet_memory
    
    	Specify 'true' to dump packet memory for all process, 'false' to disable dump of packet memory
    	**type**\:  bool
    
    .. attribute:: process_names
    
    	Specify per process configuration
    	**type**\:   :py:class:`ProcessNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_cfg.Exception.ProcessNames>`
    
    .. attribute:: sparse
    
    	Specify 'true' to enable sparse core dump, 'false' to disable sparse core dump
    	**type**\:  bool
    
    .. attribute:: sparse_size
    
    	Switch to sparse core dump at this size
    	**type**\:  int
    
    	**range:** 1..4095
    
    

    """

    _prefix = 'infra-dumper-cfg'
    _revision = '2017-04-28'

    def __init__(self):
        super(Exception, self).__init__()
        self._top_entity = None

        self.yang_name = "exception"
        self.yang_parent_name = "Cisco-IOS-XR-infra-dumper-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"choice1" : ("choice1", Exception.Choice1), "choice2" : ("choice2", Exception.Choice2), "choice3" : ("choice3", Exception.Choice3), "process-names" : ("process_names", Exception.ProcessNames)}
        self._child_list_classes = {}

        self.core_size = YLeaf(YType.uint32, "core-size")

        self.core_verification = YLeaf(YType.boolean, "core-verification")

        self.kernel_debugger = YLeaf(YType.empty, "kernel-debugger")

        self.memory_threshold = YLeaf(YType.uint32, "memory-threshold")

        self.packet_memory = YLeaf(YType.boolean, "packet-memory")

        self.sparse = YLeaf(YType.boolean, "sparse")

        self.sparse_size = YLeaf(YType.uint32, "sparse-size")

        self.choice1 = Exception.Choice1()
        self.choice1.parent = self
        self._children_name_map["choice1"] = "choice1"
        self._children_yang_names.add("choice1")

        self.choice2 = Exception.Choice2()
        self.choice2.parent = self
        self._children_name_map["choice2"] = "choice2"
        self._children_yang_names.add("choice2")

        self.choice3 = Exception.Choice3()
        self.choice3.parent = self
        self._children_name_map["choice3"] = "choice3"
        self._children_yang_names.add("choice3")

        self.process_names = Exception.ProcessNames()
        self.process_names.parent = self
        self._children_name_map["process_names"] = "process-names"
        self._children_yang_names.add("process-names")
        self._segment_path = lambda: "Cisco-IOS-XR-infra-dumper-cfg:exception"

    def __setattr__(self, name, value):
        self._perform_setattr(Exception, ['core_size', 'core_verification', 'kernel_debugger', 'memory_threshold', 'packet_memory', 'sparse', 'sparse_size'], name, value)


    class Choice1(Entity):
        """
        Preference of the dump location
        
        .. attribute:: compress
        
        	Specify 'true' to compress core files dumped on this path, 'false' to not compress
        	**type**\:  bool
        
        .. attribute:: file_path
        
        	Protocol and directory
        	**type**\:  str
        
        .. attribute:: filename
        
        	Dump filename
        	**type**\:  str
        
        .. attribute:: higher_limit
        
        	Higher limit.  This is required if Filename is specified
        	**type**\:  int
        
        	**range:** 5..64
        
        .. attribute:: lower_limit
        
        	Lower limit.  This is required if Filename is specified
        	**type**\:  int
        
        	**range:** 0..4
        
        

        """

        _prefix = 'infra-dumper-cfg'
        _revision = '2017-04-28'

        def __init__(self):
            super(Exception.Choice1, self).__init__()

            self.yang_name = "choice1"
            self.yang_parent_name = "exception"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.compress = YLeaf(YType.boolean, "compress")

            self.file_path = YLeaf(YType.str, "file-path")

            self.filename = YLeaf(YType.str, "filename")

            self.higher_limit = YLeaf(YType.uint32, "higher-limit")

            self.lower_limit = YLeaf(YType.uint32, "lower-limit")
            self._segment_path = lambda: "choice1"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-dumper-cfg:exception/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Exception.Choice1, ['compress', 'file_path', 'filename', 'higher_limit', 'lower_limit'], name, value)


    class Choice2(Entity):
        """
        Preference of the dump location
        
        .. attribute:: compress
        
        	Specify 'true' to compress core files dumped on this path, 'false' to not compress
        	**type**\:  bool
        
        .. attribute:: file_path
        
        	Protocol and directory
        	**type**\:  str
        
        .. attribute:: filename
        
        	Dump filename
        	**type**\:  str
        
        .. attribute:: higher_limit
        
        	Higher limit.  This is required if Filename is specified
        	**type**\:  int
        
        	**range:** 5..64
        
        .. attribute:: lower_limit
        
        	Lower limit.  This is required if Filename is specified
        	**type**\:  int
        
        	**range:** 0..4
        
        

        """

        _prefix = 'infra-dumper-cfg'
        _revision = '2017-04-28'

        def __init__(self):
            super(Exception.Choice2, self).__init__()

            self.yang_name = "choice2"
            self.yang_parent_name = "exception"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.compress = YLeaf(YType.boolean, "compress")

            self.file_path = YLeaf(YType.str, "file-path")

            self.filename = YLeaf(YType.str, "filename")

            self.higher_limit = YLeaf(YType.uint32, "higher-limit")

            self.lower_limit = YLeaf(YType.uint32, "lower-limit")
            self._segment_path = lambda: "choice2"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-dumper-cfg:exception/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Exception.Choice2, ['compress', 'file_path', 'filename', 'higher_limit', 'lower_limit'], name, value)


    class Choice3(Entity):
        """
        Preference of the dump location
        
        .. attribute:: compress
        
        	Specify 'true' to compress core files dumped on this path, 'false' to not compress
        	**type**\:  bool
        
        .. attribute:: file_path
        
        	Protocol and directory
        	**type**\:  str
        
        .. attribute:: filename
        
        	Dump filename
        	**type**\:  str
        
        .. attribute:: higher_limit
        
        	Higher limit.  This is required if Filename is specified
        	**type**\:  int
        
        	**range:** 5..64
        
        .. attribute:: lower_limit
        
        	Lower limit.  This is required if Filename is specified
        	**type**\:  int
        
        	**range:** 0..4
        
        

        """

        _prefix = 'infra-dumper-cfg'
        _revision = '2017-04-28'

        def __init__(self):
            super(Exception.Choice3, self).__init__()

            self.yang_name = "choice3"
            self.yang_parent_name = "exception"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.compress = YLeaf(YType.boolean, "compress")

            self.file_path = YLeaf(YType.str, "file-path")

            self.filename = YLeaf(YType.str, "filename")

            self.higher_limit = YLeaf(YType.uint32, "higher-limit")

            self.lower_limit = YLeaf(YType.uint32, "lower-limit")
            self._segment_path = lambda: "choice3"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-dumper-cfg:exception/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Exception.Choice3, ['compress', 'file_path', 'filename', 'higher_limit', 'lower_limit'], name, value)


    class ProcessNames(Entity):
        """
        Specify per process configuration
        
        .. attribute:: process_name
        
        	Specify per process configuration
        	**type**\: list of    :py:class:`ProcessName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_cfg.Exception.ProcessNames.ProcessName>`
        
        

        """

        _prefix = 'infra-dumper-cfg'
        _revision = '2017-04-28'

        def __init__(self):
            super(Exception.ProcessNames, self).__init__()

            self.yang_name = "process-names"
            self.yang_parent_name = "exception"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"process-name" : ("process_name", Exception.ProcessNames.ProcessName)}

            self.process_name = YList(self)
            self._segment_path = lambda: "process-names"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-dumper-cfg:exception/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Exception.ProcessNames, [], name, value)


        class ProcessName(Entity):
            """
            Specify per process configuration
            
            .. attribute:: processname  <key>
            
            	Specify per process configuration
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: core_option
            
            	Specify per process core option
            	**type**\:   :py:class:`CoreOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_cfg.Exception.ProcessNames.ProcessName.CoreOption>`
            
            

            """

            _prefix = 'infra-dumper-cfg'
            _revision = '2017-04-28'

            def __init__(self):
                super(Exception.ProcessNames.ProcessName, self).__init__()

                self.yang_name = "process-name"
                self.yang_parent_name = "process-names"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"core-option" : ("core_option", Exception.ProcessNames.ProcessName.CoreOption)}
                self._child_list_classes = {}

                self.processname = YLeaf(YType.str, "processname")

                self.core_option = Exception.ProcessNames.ProcessName.CoreOption()
                self.core_option.parent = self
                self._children_name_map["core_option"] = "core-option"
                self._children_yang_names.add("core-option")
                self._segment_path = lambda: "process-name" + "[processname='" + self.processname.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-dumper-cfg:exception/process-names/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Exception.ProcessNames.ProcessName, ['processname'], name, value)


            class CoreOption(Entity):
                """
                Specify per process core option
                
                .. attribute:: contextval
                
                	Dump context info only\: Overrides other options except for 'no\-core'
                	**type**\:   :py:class:`Context <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_cfg.Context>`
                
                	**default value**\: default
                
                .. attribute:: copyval
                
                	Dump to local memory\: for time critical processes
                	**type**\:   :py:class:`Copy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_cfg.Copy>`
                
                	**default value**\: default
                
                .. attribute:: main_memoryval
                
                	Dump main memory of the target process
                	**type**\:   :py:class:`Mainmemory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_cfg.Mainmemory>`
                
                	**default value**\: default
                
                .. attribute:: nocoreval
                
                	Disable core dump for the target process\: Overrides other options
                	**type**\:   :py:class:`Nocore <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_cfg.Nocore>`
                
                	**default value**\: default
                
                .. attribute:: packet_memoryval
                
                	Dump packet memory of the target process
                	**type**\:   :py:class:`Packetmemory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_cfg.Packetmemory>`
                
                	**default value**\: default
                
                .. attribute:: shared_memoryval
                
                	Dump shared memory of the target process
                	**type**\:   :py:class:`Sharedmemory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_cfg.Sharedmemory>`
                
                	**default value**\: default
                
                .. attribute:: skipcpuinfoval
                
                	Skip CPU usage snapshot\: for time critical processes
                	**type**\:   :py:class:`Skipcpuinfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_cfg.Skipcpuinfo>`
                
                	**default value**\: default
                
                .. attribute:: sparseval
                
                	Dump memory relevant to stack trace only\: for time critical processes
                	**type**\:   :py:class:`Sparse <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_cfg.Sparse>`
                
                	**default value**\: default
                
                

                """

                _prefix = 'infra-dumper-cfg'
                _revision = '2017-04-28'

                def __init__(self):
                    super(Exception.ProcessNames.ProcessName.CoreOption, self).__init__()

                    self.yang_name = "core-option"
                    self.yang_parent_name = "process-name"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.contextval = YLeaf(YType.enumeration, "contextval")

                    self.copyval = YLeaf(YType.enumeration, "copyval")

                    self.main_memoryval = YLeaf(YType.enumeration, "main-memoryval")

                    self.nocoreval = YLeaf(YType.enumeration, "nocoreval")

                    self.packet_memoryval = YLeaf(YType.enumeration, "packet-memoryval")

                    self.shared_memoryval = YLeaf(YType.enumeration, "shared-memoryval")

                    self.skipcpuinfoval = YLeaf(YType.enumeration, "skipcpuinfoval")

                    self.sparseval = YLeaf(YType.enumeration, "sparseval")
                    self._segment_path = lambda: "core-option"

                def __setattr__(self, name, value):
                    self._perform_setattr(Exception.ProcessNames.ProcessName.CoreOption, ['contextval', 'copyval', 'main_memoryval', 'nocoreval', 'packet_memoryval', 'shared_memoryval', 'skipcpuinfoval', 'sparseval'], name, value)

    def clone_ptr(self):
        self._top_entity = Exception()
        return self._top_entity

