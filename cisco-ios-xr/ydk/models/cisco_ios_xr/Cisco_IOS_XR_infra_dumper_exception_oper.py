""" Cisco_IOS_XR_infra_dumper_exception_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-dumper\-exception package operational data.

This module contains definitions
for the following management objects\:
  exception\: Show all exception dump configuration

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Exception(Entity):
    """
    Show all exception dump configuration
    
    .. attribute:: enter
    
    	exception bag
    	**type**\:  :py:class:`Enter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_exception_oper.Exception.Enter>`
    
    	**config**\: False
    
    

    """

    _prefix = 'infra-dumper-exception-oper'
    _revision = '2017-05-05'

    def __init__(self):
        super(Exception, self).__init__()
        self._top_entity = None

        self.yang_name = "exception"
        self.yang_parent_name = "Cisco-IOS-XR-infra-dumper-exception-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("enter", ("enter", Exception.Enter))])
        self._leafs = OrderedDict()

        self.enter = Exception.Enter()
        self.enter.parent = self
        self._children_name_map["enter"] = "enter"
        self._segment_path = lambda: "Cisco-IOS-XR-infra-dumper-exception-oper:exception"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Exception, [], name, value)


    class Enter(Entity):
        """
        exception bag
        
        .. attribute:: display_config1
        
        	Display Configuration
        	**type**\:  :py:class:`DisplayConfig1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_exception_oper.Exception.Enter.DisplayConfig1>`
        
        	**config**\: False
        
        .. attribute:: display_config2
        
        	Display Configuration
        	**type**\:  :py:class:`DisplayConfig2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_exception_oper.Exception.Enter.DisplayConfig2>`
        
        	**config**\: False
        
        .. attribute:: display_config3
        
        	Display Configuration
        	**type**\:  :py:class:`DisplayConfig3 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_exception_oper.Exception.Enter.DisplayConfig3>`
        
        	**config**\: False
        
        .. attribute:: display_fall_back_config1
        
        	Display fallback Configuration
        	**type**\:  :py:class:`DisplayFallBackConfig1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_exception_oper.Exception.Enter.DisplayFallBackConfig1>`
        
        	**config**\: False
        
        .. attribute:: display_fall_back_config2
        
        	Display fallback Configuration
        	**type**\:  :py:class:`DisplayFallBackConfig2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_exception_oper.Exception.Enter.DisplayFallBackConfig2>`
        
        	**config**\: False
        
        .. attribute:: display_fall_back_config3
        
        	Display fallback Configuration
        	**type**\:  :py:class:`DisplayFallBackConfig3 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_exception_oper.Exception.Enter.DisplayFallBackConfig3>`
        
        	**config**\: False
        
        .. attribute:: kernel_config
        
        	Kernel Configuration
        	**type**\:  :py:class:`KernelConfig <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_exception_oper.Exception.Enter.KernelConfig>`
        
        	**config**\: False
        
        .. attribute:: kernel_route_config
        
        	Kernel Route Configuration
        	**type**\:  :py:class:`KernelRouteConfig <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_exception_oper.Exception.Enter.KernelRouteConfig>`
        
        	**config**\: False
        
        .. attribute:: core_size
        
        	Core Size
        	**type**\:  :py:class:`CoreSize <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_exception_oper.Exception.Enter.CoreSize>`
        
        	**config**\: False
        
        .. attribute:: memory_threshold
        
        	Memory Threshold 
        	**type**\:  :py:class:`MemoryThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_exception_oper.Exception.Enter.MemoryThreshold>`
        
        	**config**\: False
        
        .. attribute:: proc_size
        
        	Proc Size
        	**type**\:  :py:class:`ProcSize <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_exception_oper.Exception.Enter.ProcSize>`
        
        	**config**\: False
        
        .. attribute:: qsize
        
        	QSIZE 
        	**type**\:  :py:class:`Qsize <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_exception_oper.Exception.Enter.Qsize>`
        
        	**config**\: False
        
        .. attribute:: pak_mem
        
        	Pak MEM
        	**type**\: str
        
        	**config**\: False
        
        .. attribute:: sparse
        
        	Sparse 
        	**type**\: str
        
        	**config**\: False
        
        .. attribute:: spr_size
        
        	Spr Size
        	**type**\: str
        
        	**config**\: False
        
        .. attribute:: core_verification
        
        	Core Verification 
        	**type**\: str
        
        	**config**\: False
        
        .. attribute:: dump_time_out
        
        	Dump Timeout 
        	**type**\: str
        
        	**config**\: False
        
        

        """

        _prefix = 'infra-dumper-exception-oper'
        _revision = '2017-05-05'

        def __init__(self):
            super(Exception.Enter, self).__init__()

            self.yang_name = "enter"
            self.yang_parent_name = "exception"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("display-config1", ("display_config1", Exception.Enter.DisplayConfig1)), ("display-config2", ("display_config2", Exception.Enter.DisplayConfig2)), ("display-config3", ("display_config3", Exception.Enter.DisplayConfig3)), ("display-fall-back-config1", ("display_fall_back_config1", Exception.Enter.DisplayFallBackConfig1)), ("display-fall-back-config2", ("display_fall_back_config2", Exception.Enter.DisplayFallBackConfig2)), ("display-fall-back-config3", ("display_fall_back_config3", Exception.Enter.DisplayFallBackConfig3)), ("kernel-config", ("kernel_config", Exception.Enter.KernelConfig)), ("kernel-route-config", ("kernel_route_config", Exception.Enter.KernelRouteConfig)), ("core-size", ("core_size", Exception.Enter.CoreSize)), ("memory-threshold", ("memory_threshold", Exception.Enter.MemoryThreshold)), ("proc-size", ("proc_size", Exception.Enter.ProcSize)), ("qsize", ("qsize", Exception.Enter.Qsize))])
            self._leafs = OrderedDict([
                ('pak_mem', (YLeaf(YType.str, 'pak-mem'), ['str'])),
                ('sparse', (YLeaf(YType.str, 'sparse'), ['str'])),
                ('spr_size', (YLeaf(YType.str, 'spr-size'), ['str'])),
                ('core_verification', (YLeaf(YType.str, 'core-verification'), ['str'])),
                ('dump_time_out', (YLeaf(YType.str, 'dump-time-out'), ['str'])),
            ])
            self.pak_mem = None
            self.sparse = None
            self.spr_size = None
            self.core_verification = None
            self.dump_time_out = None

            self.display_config1 = Exception.Enter.DisplayConfig1()
            self.display_config1.parent = self
            self._children_name_map["display_config1"] = "display-config1"

            self.display_config2 = Exception.Enter.DisplayConfig2()
            self.display_config2.parent = self
            self._children_name_map["display_config2"] = "display-config2"

            self.display_config3 = Exception.Enter.DisplayConfig3()
            self.display_config3.parent = self
            self._children_name_map["display_config3"] = "display-config3"

            self.display_fall_back_config1 = Exception.Enter.DisplayFallBackConfig1()
            self.display_fall_back_config1.parent = self
            self._children_name_map["display_fall_back_config1"] = "display-fall-back-config1"

            self.display_fall_back_config2 = Exception.Enter.DisplayFallBackConfig2()
            self.display_fall_back_config2.parent = self
            self._children_name_map["display_fall_back_config2"] = "display-fall-back-config2"

            self.display_fall_back_config3 = Exception.Enter.DisplayFallBackConfig3()
            self.display_fall_back_config3.parent = self
            self._children_name_map["display_fall_back_config3"] = "display-fall-back-config3"

            self.kernel_config = Exception.Enter.KernelConfig()
            self.kernel_config.parent = self
            self._children_name_map["kernel_config"] = "kernel-config"

            self.kernel_route_config = Exception.Enter.KernelRouteConfig()
            self.kernel_route_config.parent = self
            self._children_name_map["kernel_route_config"] = "kernel-route-config"

            self.core_size = Exception.Enter.CoreSize()
            self.core_size.parent = self
            self._children_name_map["core_size"] = "core-size"

            self.memory_threshold = Exception.Enter.MemoryThreshold()
            self.memory_threshold.parent = self
            self._children_name_map["memory_threshold"] = "memory-threshold"

            self.proc_size = Exception.Enter.ProcSize()
            self.proc_size.parent = self
            self._children_name_map["proc_size"] = "proc-size"

            self.qsize = Exception.Enter.Qsize()
            self.qsize.parent = self
            self._children_name_map["qsize"] = "qsize"
            self._segment_path = lambda: "enter"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-dumper-exception-oper:exception/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Exception.Enter, [u'pak_mem', u'sparse', u'spr_size', u'core_verification', u'dump_time_out'], name, value)


        class DisplayConfig1(Entity):
            """
            Display Configuration
            
            .. attribute:: choice
            
            	Choice 
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: path
            
            	Path 
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: compress
            
            	Compress on/off 
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: file_name
            
            	Name of the File 
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: range_low
            
            	Range Low 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: range_high
            
            	Range High 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'infra-dumper-exception-oper'
            _revision = '2017-05-05'

            def __init__(self):
                super(Exception.Enter.DisplayConfig1, self).__init__()

                self.yang_name = "display-config1"
                self.yang_parent_name = "enter"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('choice', (YLeaf(YType.str, 'choice'), ['str'])),
                    ('path', (YLeaf(YType.str, 'path'), ['str'])),
                    ('compress', (YLeaf(YType.str, 'compress'), ['str'])),
                    ('file_name', (YLeaf(YType.str, 'file-name'), ['str'])),
                    ('range_low', (YLeaf(YType.uint32, 'range-low'), ['int'])),
                    ('range_high', (YLeaf(YType.uint32, 'range-high'), ['int'])),
                ])
                self.choice = None
                self.path = None
                self.compress = None
                self.file_name = None
                self.range_low = None
                self.range_high = None
                self._segment_path = lambda: "display-config1"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-dumper-exception-oper:exception/enter/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Exception.Enter.DisplayConfig1, [u'choice', u'path', u'compress', u'file_name', u'range_low', u'range_high'], name, value)



        class DisplayConfig2(Entity):
            """
            Display Configuration
            
            .. attribute:: choice
            
            	Choice 
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: path
            
            	Path 
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: compress
            
            	Compress on/off 
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: file_name
            
            	Name of the File 
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: range_low
            
            	Range Low 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: range_high
            
            	Range High 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'infra-dumper-exception-oper'
            _revision = '2017-05-05'

            def __init__(self):
                super(Exception.Enter.DisplayConfig2, self).__init__()

                self.yang_name = "display-config2"
                self.yang_parent_name = "enter"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('choice', (YLeaf(YType.str, 'choice'), ['str'])),
                    ('path', (YLeaf(YType.str, 'path'), ['str'])),
                    ('compress', (YLeaf(YType.str, 'compress'), ['str'])),
                    ('file_name', (YLeaf(YType.str, 'file-name'), ['str'])),
                    ('range_low', (YLeaf(YType.uint32, 'range-low'), ['int'])),
                    ('range_high', (YLeaf(YType.uint32, 'range-high'), ['int'])),
                ])
                self.choice = None
                self.path = None
                self.compress = None
                self.file_name = None
                self.range_low = None
                self.range_high = None
                self._segment_path = lambda: "display-config2"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-dumper-exception-oper:exception/enter/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Exception.Enter.DisplayConfig2, [u'choice', u'path', u'compress', u'file_name', u'range_low', u'range_high'], name, value)



        class DisplayConfig3(Entity):
            """
            Display Configuration
            
            .. attribute:: choice
            
            	Choice 
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: path
            
            	Path 
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: compress
            
            	Compress on/off 
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: file_name
            
            	Name of the File 
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: range_low
            
            	Range Low 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: range_high
            
            	Range High 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'infra-dumper-exception-oper'
            _revision = '2017-05-05'

            def __init__(self):
                super(Exception.Enter.DisplayConfig3, self).__init__()

                self.yang_name = "display-config3"
                self.yang_parent_name = "enter"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('choice', (YLeaf(YType.str, 'choice'), ['str'])),
                    ('path', (YLeaf(YType.str, 'path'), ['str'])),
                    ('compress', (YLeaf(YType.str, 'compress'), ['str'])),
                    ('file_name', (YLeaf(YType.str, 'file-name'), ['str'])),
                    ('range_low', (YLeaf(YType.uint32, 'range-low'), ['int'])),
                    ('range_high', (YLeaf(YType.uint32, 'range-high'), ['int'])),
                ])
                self.choice = None
                self.path = None
                self.compress = None
                self.file_name = None
                self.range_low = None
                self.range_high = None
                self._segment_path = lambda: "display-config3"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-dumper-exception-oper:exception/enter/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Exception.Enter.DisplayConfig3, [u'choice', u'path', u'compress', u'file_name', u'range_low', u'range_high'], name, value)



        class DisplayFallBackConfig1(Entity):
            """
            Display fallback Configuration
            
            .. attribute:: choice_fall_back
            
            	Choice 
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: path
            
            	Path 
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: compress
            
            	Compress on/off 
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: file_name
            
            	Name of the File 
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: boot_device_str
            
            	Boot Device String 
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: range_low
            
            	Range Low 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: range_high
            
            	Range High 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'infra-dumper-exception-oper'
            _revision = '2017-05-05'

            def __init__(self):
                super(Exception.Enter.DisplayFallBackConfig1, self).__init__()

                self.yang_name = "display-fall-back-config1"
                self.yang_parent_name = "enter"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('choice_fall_back', (YLeaf(YType.str, 'choice-fall-back'), ['str'])),
                    ('path', (YLeaf(YType.str, 'path'), ['str'])),
                    ('compress', (YLeaf(YType.str, 'compress'), ['str'])),
                    ('file_name', (YLeaf(YType.str, 'file-name'), ['str'])),
                    ('boot_device_str', (YLeaf(YType.str, 'boot-device-str'), ['str'])),
                    ('range_low', (YLeaf(YType.uint32, 'range-low'), ['int'])),
                    ('range_high', (YLeaf(YType.uint32, 'range-high'), ['int'])),
                ])
                self.choice_fall_back = None
                self.path = None
                self.compress = None
                self.file_name = None
                self.boot_device_str = None
                self.range_low = None
                self.range_high = None
                self._segment_path = lambda: "display-fall-back-config1"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-dumper-exception-oper:exception/enter/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Exception.Enter.DisplayFallBackConfig1, [u'choice_fall_back', u'path', u'compress', u'file_name', u'boot_device_str', u'range_low', u'range_high'], name, value)



        class DisplayFallBackConfig2(Entity):
            """
            Display fallback Configuration
            
            .. attribute:: choice_fall_back
            
            	Choice 
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: path
            
            	Path 
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: compress
            
            	Compress on/off 
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: file_name
            
            	Name of the File 
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: boot_device_str
            
            	Boot Device String 
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: range_low
            
            	Range Low 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: range_high
            
            	Range High 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'infra-dumper-exception-oper'
            _revision = '2017-05-05'

            def __init__(self):
                super(Exception.Enter.DisplayFallBackConfig2, self).__init__()

                self.yang_name = "display-fall-back-config2"
                self.yang_parent_name = "enter"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('choice_fall_back', (YLeaf(YType.str, 'choice-fall-back'), ['str'])),
                    ('path', (YLeaf(YType.str, 'path'), ['str'])),
                    ('compress', (YLeaf(YType.str, 'compress'), ['str'])),
                    ('file_name', (YLeaf(YType.str, 'file-name'), ['str'])),
                    ('boot_device_str', (YLeaf(YType.str, 'boot-device-str'), ['str'])),
                    ('range_low', (YLeaf(YType.uint32, 'range-low'), ['int'])),
                    ('range_high', (YLeaf(YType.uint32, 'range-high'), ['int'])),
                ])
                self.choice_fall_back = None
                self.path = None
                self.compress = None
                self.file_name = None
                self.boot_device_str = None
                self.range_low = None
                self.range_high = None
                self._segment_path = lambda: "display-fall-back-config2"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-dumper-exception-oper:exception/enter/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Exception.Enter.DisplayFallBackConfig2, [u'choice_fall_back', u'path', u'compress', u'file_name', u'boot_device_str', u'range_low', u'range_high'], name, value)



        class DisplayFallBackConfig3(Entity):
            """
            Display fallback Configuration
            
            .. attribute:: choice_fall_back
            
            	Choice 
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: path
            
            	Path 
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: compress
            
            	Compress on/off 
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: file_name
            
            	Name of the File 
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: boot_device_str
            
            	Boot Device String 
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: range_low
            
            	Range Low 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: range_high
            
            	Range High 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'infra-dumper-exception-oper'
            _revision = '2017-05-05'

            def __init__(self):
                super(Exception.Enter.DisplayFallBackConfig3, self).__init__()

                self.yang_name = "display-fall-back-config3"
                self.yang_parent_name = "enter"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('choice_fall_back', (YLeaf(YType.str, 'choice-fall-back'), ['str'])),
                    ('path', (YLeaf(YType.str, 'path'), ['str'])),
                    ('compress', (YLeaf(YType.str, 'compress'), ['str'])),
                    ('file_name', (YLeaf(YType.str, 'file-name'), ['str'])),
                    ('boot_device_str', (YLeaf(YType.str, 'boot-device-str'), ['str'])),
                    ('range_low', (YLeaf(YType.uint32, 'range-low'), ['int'])),
                    ('range_high', (YLeaf(YType.uint32, 'range-high'), ['int'])),
                ])
                self.choice_fall_back = None
                self.path = None
                self.compress = None
                self.file_name = None
                self.boot_device_str = None
                self.range_low = None
                self.range_high = None
                self._segment_path = lambda: "display-fall-back-config3"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-dumper-exception-oper:exception/enter/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Exception.Enter.DisplayFallBackConfig3, [u'choice_fall_back', u'path', u'compress', u'file_name', u'boot_device_str', u'range_low', u'range_high'], name, value)



        class KernelConfig(Entity):
            """
            Kernel Configuration
            
            .. attribute:: choice_fall_back
            
            	Choice 
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: path
            
            	Path 
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: file_name
            
            	Name of the File 
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: memory
            
            	Memory 
            	**type**\: str
            
            	**config**\: False
            
            

            """

            _prefix = 'infra-dumper-exception-oper'
            _revision = '2017-05-05'

            def __init__(self):
                super(Exception.Enter.KernelConfig, self).__init__()

                self.yang_name = "kernel-config"
                self.yang_parent_name = "enter"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('choice_fall_back', (YLeaf(YType.str, 'choice-fall-back'), ['str'])),
                    ('path', (YLeaf(YType.str, 'path'), ['str'])),
                    ('file_name', (YLeaf(YType.str, 'file-name'), ['str'])),
                    ('memory', (YLeaf(YType.str, 'memory'), ['str'])),
                ])
                self.choice_fall_back = None
                self.path = None
                self.file_name = None
                self.memory = None
                self._segment_path = lambda: "kernel-config"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-dumper-exception-oper:exception/enter/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Exception.Enter.KernelConfig, [u'choice_fall_back', u'path', u'file_name', u'memory'], name, value)



        class KernelRouteConfig(Entity):
            """
            Kernel Route Configuration
            
            .. attribute:: slot
            
            	Slot 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: port
            
            	Port 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: ip_addr
            
            	IP Address
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: mask
            
            	Mask
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: destination
            
            	Destination 
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: next_hop
            
            	NextHop 
            	**type**\: str
            
            	**config**\: False
            
            

            """

            _prefix = 'infra-dumper-exception-oper'
            _revision = '2017-05-05'

            def __init__(self):
                super(Exception.Enter.KernelRouteConfig, self).__init__()

                self.yang_name = "kernel-route-config"
                self.yang_parent_name = "enter"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('slot', (YLeaf(YType.uint32, 'slot'), ['int'])),
                    ('port', (YLeaf(YType.uint32, 'port'), ['int'])),
                    ('ip_addr', (YLeaf(YType.str, 'ip-addr'), ['str'])),
                    ('mask', (YLeaf(YType.str, 'mask'), ['str'])),
                    ('destination', (YLeaf(YType.str, 'destination'), ['str'])),
                    ('next_hop', (YLeaf(YType.str, 'next-hop'), ['str'])),
                ])
                self.slot = None
                self.port = None
                self.ip_addr = None
                self.mask = None
                self.destination = None
                self.next_hop = None
                self._segment_path = lambda: "kernel-route-config"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-dumper-exception-oper:exception/enter/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Exception.Enter.KernelRouteConfig, [u'slot', u'port', u'ip_addr', u'mask', u'destination', u'next_hop'], name, value)



        class CoreSize(Entity):
            """
            Core Size
            
            .. attribute:: string
            
            	String  
            	**type**\: str
            
            	**config**\: False
            
            

            """

            _prefix = 'infra-dumper-exception-oper'
            _revision = '2017-05-05'

            def __init__(self):
                super(Exception.Enter.CoreSize, self).__init__()

                self.yang_name = "core-size"
                self.yang_parent_name = "enter"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('string', (YLeaf(YType.str, 'string'), ['str'])),
                ])
                self.string = None
                self._segment_path = lambda: "core-size"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-dumper-exception-oper:exception/enter/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Exception.Enter.CoreSize, [u'string'], name, value)



        class MemoryThreshold(Entity):
            """
            Memory Threshold 
            
            .. attribute:: string
            
            	String  
            	**type**\: str
            
            	**config**\: False
            
            

            """

            _prefix = 'infra-dumper-exception-oper'
            _revision = '2017-05-05'

            def __init__(self):
                super(Exception.Enter.MemoryThreshold, self).__init__()

                self.yang_name = "memory-threshold"
                self.yang_parent_name = "enter"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('string', (YLeaf(YType.str, 'string'), ['str'])),
                ])
                self.string = None
                self._segment_path = lambda: "memory-threshold"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-dumper-exception-oper:exception/enter/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Exception.Enter.MemoryThreshold, [u'string'], name, value)



        class ProcSize(Entity):
            """
            Proc Size
            
            .. attribute:: string
            
            	String  
            	**type**\: str
            
            	**config**\: False
            
            

            """

            _prefix = 'infra-dumper-exception-oper'
            _revision = '2017-05-05'

            def __init__(self):
                super(Exception.Enter.ProcSize, self).__init__()

                self.yang_name = "proc-size"
                self.yang_parent_name = "enter"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('string', (YLeaf(YType.str, 'string'), ['str'])),
                ])
                self.string = None
                self._segment_path = lambda: "proc-size"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-dumper-exception-oper:exception/enter/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Exception.Enter.ProcSize, [u'string'], name, value)



        class Qsize(Entity):
            """
            QSIZE 
            
            .. attribute:: string
            
            	String  
            	**type**\: str
            
            	**config**\: False
            
            

            """

            _prefix = 'infra-dumper-exception-oper'
            _revision = '2017-05-05'

            def __init__(self):
                super(Exception.Enter.Qsize, self).__init__()

                self.yang_name = "qsize"
                self.yang_parent_name = "enter"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('string', (YLeaf(YType.str, 'string'), ['str'])),
                ])
                self.string = None
                self._segment_path = lambda: "qsize"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-dumper-exception-oper:exception/enter/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Exception.Enter.Qsize, [u'string'], name, value)



    def clone_ptr(self):
        self._top_entity = Exception()
        return self._top_entity



