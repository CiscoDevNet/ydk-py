""" vplatform 

This module contains definitions
for the Calvados model objects.

Copyright (c) 2012\-2018 by Cisco Systems, Inc.
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




class VirtualPlatform(_Entity_):
    """
    
    
    .. attribute:: vplatform
    
    	
    	**type**\:  :py:class:`Vplatform <ydk.models.cisco_ios_xr.vplatform.VirtualPlatform.Vplatform>`
    
    	**config**\: False
    
    .. attribute:: udi
    
    	
    	**type**\:  :py:class:`Udi <ydk.models.cisco_ios_xr.vplatform.VirtualPlatform.Udi>`
    
    	**config**\: False
    
    .. attribute:: cpu
    
    	
    	**type**\:  :py:class:`Cpu <ydk.models.cisco_ios_xr.vplatform.VirtualPlatform.Cpu>`
    
    	**config**\: False
    
    .. attribute:: processor
    
    	
    	**type**\:  :py:class:`Processor <ydk.models.cisco_ios_xr.vplatform.VirtualPlatform.Processor>`
    
    	**config**\: False
    
    .. attribute:: memory
    
    	
    	**type**\:  :py:class:`Memory <ydk.models.cisco_ios_xr.vplatform.VirtualPlatform.Memory>`
    
    	**config**\: False
    
    .. attribute:: disk
    
    	
    	**type**\:  :py:class:`Disk <ydk.models.cisco_ios_xr.vplatform.VirtualPlatform.Disk>`
    
    	**config**\: False
    
    .. attribute:: action
    
    	
    	**type**\:  :py:class:`Action <ydk.models.cisco_ios_xr.vplatform.VirtualPlatform.Action>`
    
    	**config**\: False
    
    

    """

    _prefix = 'vplatform'
    _revision = '2015-08-30'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(VirtualPlatform, self).__init__()
        self._top_entity = None

        self.yang_name = "virtual-platform"
        self.yang_parent_name = "vplatform"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("vplatform", ("vplatform", VirtualPlatform.Vplatform)), ("udi", ("udi", VirtualPlatform.Udi)), ("cpu", ("cpu", VirtualPlatform.Cpu)), ("processor", ("processor", VirtualPlatform.Processor)), ("memory", ("memory", VirtualPlatform.Memory)), ("disk", ("disk", VirtualPlatform.Disk)), ("Action", ("action", VirtualPlatform.Action))])
        self._leafs = OrderedDict()

        self.vplatform = VirtualPlatform.Vplatform()
        self.vplatform.parent = self
        self._children_name_map["vplatform"] = "vplatform"

        self.udi = VirtualPlatform.Udi()
        self.udi.parent = self
        self._children_name_map["udi"] = "udi"

        self.cpu = VirtualPlatform.Cpu()
        self.cpu.parent = self
        self._children_name_map["cpu"] = "cpu"

        self.processor = VirtualPlatform.Processor()
        self.processor.parent = self
        self._children_name_map["processor"] = "processor"

        self.memory = VirtualPlatform.Memory()
        self.memory.parent = self
        self._children_name_map["memory"] = "memory"

        self.disk = VirtualPlatform.Disk()
        self.disk.parent = self
        self._children_name_map["disk"] = "disk"

        self.action = VirtualPlatform.Action()
        self.action.parent = self
        self._children_name_map["action"] = "Action"
        self._segment_path = lambda: "vplatform:virtual-platform"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(VirtualPlatform, [], name, value)


    class Vplatform(_Entity_):
        """
        
        
        .. attribute:: summary
        
        	
        	**type**\: list of  		 :py:class:`Summary <ydk.models.cisco_ios_xr.vplatform.VirtualPlatform.Vplatform.Summary>`
        
        	**config**\: False
        
        

        """

        _prefix = 'vplatform'
        _revision = '2015-08-30'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(VirtualPlatform.Vplatform, self).__init__()

            self.yang_name = "vplatform"
            self.yang_parent_name = "virtual-platform"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("summary", ("summary", VirtualPlatform.Vplatform.Summary))])
            self._leafs = OrderedDict()

            self.summary = YList(self)
            self._segment_path = lambda: "vplatform"
            self._absolute_path = lambda: "vplatform:virtual-platform/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(VirtualPlatform.Vplatform, [], name, value)


        class Summary(_Entity_):
            """
            
            
            .. attribute:: lines
            
            	
            	**type**\: str
            
            	**config**\: False
            
            

            """

            _prefix = 'vplatform'
            _revision = '2015-08-30'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(VirtualPlatform.Vplatform.Summary, self).__init__()

                self.yang_name = "summary"
                self.yang_parent_name = "vplatform"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('lines', (YLeaf(YType.str, 'lines'), ['str'])),
                ])
                self.lines = None
                self._segment_path = lambda: "summary"
                self._absolute_path = lambda: "vplatform:virtual-platform/vplatform/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(VirtualPlatform.Vplatform.Summary, ['lines'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _vplatform as meta
                return meta._meta_table['VirtualPlatform.Vplatform.Summary']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _vplatform as meta
            return meta._meta_table['VirtualPlatform.Vplatform']['meta_info']


    class Udi(_Entity_):
        """
        
        
        .. attribute:: history
        
        	
        	**type**\:  :py:class:`History <ydk.models.cisco_ios_xr.vplatform.VirtualPlatform.Udi.History>`
        
        	**config**\: False
        
        

        """

        _prefix = 'vplatform'
        _revision = '2015-08-30'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(VirtualPlatform.Udi, self).__init__()

            self.yang_name = "udi"
            self.yang_parent_name = "virtual-platform"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("history", ("history", VirtualPlatform.Udi.History))])
            self._leafs = OrderedDict()

            self.history = VirtualPlatform.Udi.History()
            self.history.parent = self
            self._children_name_map["history"] = "history"
            self._segment_path = lambda: "udi"
            self._absolute_path = lambda: "vplatform:virtual-platform/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(VirtualPlatform.Udi, [], name, value)


        class History(_Entity_):
            """
            
            
            .. attribute:: udi_his
            
            	
            	**type**\: list of  		 :py:class:`UdiHis <ydk.models.cisco_ios_xr.vplatform.VirtualPlatform.Udi.History.UdiHis>`
            
            	**config**\: False
            
            

            """

            _prefix = 'vplatform'
            _revision = '2015-08-30'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(VirtualPlatform.Udi.History, self).__init__()

                self.yang_name = "history"
                self.yang_parent_name = "udi"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("udi_his", ("udi_his", VirtualPlatform.Udi.History.UdiHis))])
                self._leafs = OrderedDict()

                self.udi_his = YList(self)
                self._segment_path = lambda: "history"
                self._absolute_path = lambda: "vplatform:virtual-platform/udi/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(VirtualPlatform.Udi.History, [], name, value)


            class UdiHis(_Entity_):
                """
                
                
                .. attribute:: history_records
                
                	
                	**type**\: str
                
                	**config**\: False
                
                

                """

                _prefix = 'vplatform'
                _revision = '2015-08-30'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(VirtualPlatform.Udi.History.UdiHis, self).__init__()

                    self.yang_name = "udi_his"
                    self.yang_parent_name = "history"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('history_records', (YLeaf(YType.str, 'history_records'), ['str'])),
                    ])
                    self.history_records = None
                    self._segment_path = lambda: "udi_his"
                    self._absolute_path = lambda: "vplatform:virtual-platform/udi/history/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(VirtualPlatform.Udi.History.UdiHis, ['history_records'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _vplatform as meta
                    return meta._meta_table['VirtualPlatform.Udi.History.UdiHis']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _vplatform as meta
                return meta._meta_table['VirtualPlatform.Udi.History']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _vplatform as meta
            return meta._meta_table['VirtualPlatform.Udi']['meta_info']


    class Cpu(_Entity_):
        """
        
        
        .. attribute:: history
        
        	
        	**type**\:  :py:class:`History <ydk.models.cisco_ios_xr.vplatform.VirtualPlatform.Cpu.History>`
        
        	**config**\: False
        
        

        """

        _prefix = 'vplatform'
        _revision = '2015-08-30'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(VirtualPlatform.Cpu, self).__init__()

            self.yang_name = "cpu"
            self.yang_parent_name = "virtual-platform"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("history", ("history", VirtualPlatform.Cpu.History))])
            self._leafs = OrderedDict()

            self.history = VirtualPlatform.Cpu.History()
            self.history.parent = self
            self._children_name_map["history"] = "history"
            self._segment_path = lambda: "cpu"
            self._absolute_path = lambda: "vplatform:virtual-platform/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(VirtualPlatform.Cpu, [], name, value)


        class History(_Entity_):
            """
            
            
            .. attribute:: cpu_utl
            
            	
            	**type**\: list of  		 :py:class:`CpuUtl <ydk.models.cisco_ios_xr.vplatform.VirtualPlatform.Cpu.History.CpuUtl>`
            
            	**config**\: False
            
            

            """

            _prefix = 'vplatform'
            _revision = '2015-08-30'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(VirtualPlatform.Cpu.History, self).__init__()

                self.yang_name = "history"
                self.yang_parent_name = "cpu"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("cpu_utl", ("cpu_utl", VirtualPlatform.Cpu.History.CpuUtl))])
                self._leafs = OrderedDict()

                self.cpu_utl = YList(self)
                self._segment_path = lambda: "history"
                self._absolute_path = lambda: "vplatform:virtual-platform/cpu/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(VirtualPlatform.Cpu.History, [], name, value)


            class CpuUtl(_Entity_):
                """
                
                
                .. attribute:: history_records
                
                	
                	**type**\: str
                
                	**config**\: False
                
                

                """

                _prefix = 'vplatform'
                _revision = '2015-08-30'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(VirtualPlatform.Cpu.History.CpuUtl, self).__init__()

                    self.yang_name = "cpu_utl"
                    self.yang_parent_name = "history"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('history_records', (YLeaf(YType.str, 'history_records'), ['str'])),
                    ])
                    self.history_records = None
                    self._segment_path = lambda: "cpu_utl"
                    self._absolute_path = lambda: "vplatform:virtual-platform/cpu/history/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(VirtualPlatform.Cpu.History.CpuUtl, ['history_records'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _vplatform as meta
                    return meta._meta_table['VirtualPlatform.Cpu.History.CpuUtl']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _vplatform as meta
                return meta._meta_table['VirtualPlatform.Cpu.History']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _vplatform as meta
            return meta._meta_table['VirtualPlatform.Cpu']['meta_info']


    class Processor(_Entity_):
        """
        
        
        .. attribute:: history
        
        	
        	**type**\:  :py:class:`History <ydk.models.cisco_ios_xr.vplatform.VirtualPlatform.Processor.History>`
        
        	**config**\: False
        
        

        """

        _prefix = 'vplatform'
        _revision = '2015-08-30'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(VirtualPlatform.Processor, self).__init__()

            self.yang_name = "processor"
            self.yang_parent_name = "virtual-platform"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("history", ("history", VirtualPlatform.Processor.History))])
            self._leafs = OrderedDict()

            self.history = VirtualPlatform.Processor.History()
            self.history.parent = self
            self._children_name_map["history"] = "history"
            self._segment_path = lambda: "processor"
            self._absolute_path = lambda: "vplatform:virtual-platform/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(VirtualPlatform.Processor, [], name, value)


        class History(_Entity_):
            """
            
            
            .. attribute:: proc_info
            
            	
            	**type**\: list of  		 :py:class:`ProcInfo <ydk.models.cisco_ios_xr.vplatform.VirtualPlatform.Processor.History.ProcInfo>`
            
            	**config**\: False
            
            

            """

            _prefix = 'vplatform'
            _revision = '2015-08-30'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(VirtualPlatform.Processor.History, self).__init__()

                self.yang_name = "history"
                self.yang_parent_name = "processor"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("proc_info", ("proc_info", VirtualPlatform.Processor.History.ProcInfo))])
                self._leafs = OrderedDict()

                self.proc_info = YList(self)
                self._segment_path = lambda: "history"
                self._absolute_path = lambda: "vplatform:virtual-platform/processor/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(VirtualPlatform.Processor.History, [], name, value)


            class ProcInfo(_Entity_):
                """
                
                
                .. attribute:: history_records
                
                	
                	**type**\: str
                
                	**config**\: False
                
                

                """

                _prefix = 'vplatform'
                _revision = '2015-08-30'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(VirtualPlatform.Processor.History.ProcInfo, self).__init__()

                    self.yang_name = "proc_info"
                    self.yang_parent_name = "history"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('history_records', (YLeaf(YType.str, 'history_records'), ['str'])),
                    ])
                    self.history_records = None
                    self._segment_path = lambda: "proc_info"
                    self._absolute_path = lambda: "vplatform:virtual-platform/processor/history/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(VirtualPlatform.Processor.History.ProcInfo, ['history_records'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _vplatform as meta
                    return meta._meta_table['VirtualPlatform.Processor.History.ProcInfo']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _vplatform as meta
                return meta._meta_table['VirtualPlatform.Processor.History']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _vplatform as meta
            return meta._meta_table['VirtualPlatform.Processor']['meta_info']


    class Memory(_Entity_):
        """
        
        
        .. attribute:: history
        
        	
        	**type**\:  :py:class:`History <ydk.models.cisco_ios_xr.vplatform.VirtualPlatform.Memory.History>`
        
        	**config**\: False
        
        

        """

        _prefix = 'vplatform'
        _revision = '2015-08-30'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(VirtualPlatform.Memory, self).__init__()

            self.yang_name = "memory"
            self.yang_parent_name = "virtual-platform"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("history", ("history", VirtualPlatform.Memory.History))])
            self._leafs = OrderedDict()

            self.history = VirtualPlatform.Memory.History()
            self.history.parent = self
            self._children_name_map["history"] = "history"
            self._segment_path = lambda: "memory"
            self._absolute_path = lambda: "vplatform:virtual-platform/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(VirtualPlatform.Memory, [], name, value)


        class History(_Entity_):
            """
            
            
            .. attribute:: mem_usg
            
            	
            	**type**\: list of  		 :py:class:`MemUsg <ydk.models.cisco_ios_xr.vplatform.VirtualPlatform.Memory.History.MemUsg>`
            
            	**config**\: False
            
            

            """

            _prefix = 'vplatform'
            _revision = '2015-08-30'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(VirtualPlatform.Memory.History, self).__init__()

                self.yang_name = "history"
                self.yang_parent_name = "memory"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("mem_usg", ("mem_usg", VirtualPlatform.Memory.History.MemUsg))])
                self._leafs = OrderedDict()

                self.mem_usg = YList(self)
                self._segment_path = lambda: "history"
                self._absolute_path = lambda: "vplatform:virtual-platform/memory/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(VirtualPlatform.Memory.History, [], name, value)


            class MemUsg(_Entity_):
                """
                
                
                .. attribute:: history_records
                
                	
                	**type**\: str
                
                	**config**\: False
                
                

                """

                _prefix = 'vplatform'
                _revision = '2015-08-30'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(VirtualPlatform.Memory.History.MemUsg, self).__init__()

                    self.yang_name = "mem_usg"
                    self.yang_parent_name = "history"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('history_records', (YLeaf(YType.str, 'history_records'), ['str'])),
                    ])
                    self.history_records = None
                    self._segment_path = lambda: "mem_usg"
                    self._absolute_path = lambda: "vplatform:virtual-platform/memory/history/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(VirtualPlatform.Memory.History.MemUsg, ['history_records'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _vplatform as meta
                    return meta._meta_table['VirtualPlatform.Memory.History.MemUsg']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _vplatform as meta
                return meta._meta_table['VirtualPlatform.Memory.History']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _vplatform as meta
            return meta._meta_table['VirtualPlatform.Memory']['meta_info']


    class Disk(_Entity_):
        """
        
        
        .. attribute:: history
        
        	
        	**type**\:  :py:class:`History <ydk.models.cisco_ios_xr.vplatform.VirtualPlatform.Disk.History>`
        
        	**config**\: False
        
        

        """

        _prefix = 'vplatform'
        _revision = '2015-08-30'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(VirtualPlatform.Disk, self).__init__()

            self.yang_name = "disk"
            self.yang_parent_name = "virtual-platform"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("history", ("history", VirtualPlatform.Disk.History))])
            self._leafs = OrderedDict()

            self.history = VirtualPlatform.Disk.History()
            self.history.parent = self
            self._children_name_map["history"] = "history"
            self._segment_path = lambda: "disk"
            self._absolute_path = lambda: "vplatform:virtual-platform/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(VirtualPlatform.Disk, [], name, value)


        class History(_Entity_):
            """
            
            
            .. attribute:: disk_utl
            
            	
            	**type**\: list of  		 :py:class:`DiskUtl <ydk.models.cisco_ios_xr.vplatform.VirtualPlatform.Disk.History.DiskUtl>`
            
            	**config**\: False
            
            

            """

            _prefix = 'vplatform'
            _revision = '2015-08-30'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(VirtualPlatform.Disk.History, self).__init__()

                self.yang_name = "history"
                self.yang_parent_name = "disk"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("disk_utl", ("disk_utl", VirtualPlatform.Disk.History.DiskUtl))])
                self._leafs = OrderedDict()

                self.disk_utl = YList(self)
                self._segment_path = lambda: "history"
                self._absolute_path = lambda: "vplatform:virtual-platform/disk/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(VirtualPlatform.Disk.History, [], name, value)


            class DiskUtl(_Entity_):
                """
                
                
                .. attribute:: history_records
                
                	
                	**type**\: str
                
                	**config**\: False
                
                

                """

                _prefix = 'vplatform'
                _revision = '2015-08-30'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(VirtualPlatform.Disk.History.DiskUtl, self).__init__()

                    self.yang_name = "disk_utl"
                    self.yang_parent_name = "history"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('history_records', (YLeaf(YType.str, 'history_records'), ['str'])),
                    ])
                    self.history_records = None
                    self._segment_path = lambda: "disk_utl"
                    self._absolute_path = lambda: "vplatform:virtual-platform/disk/history/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(VirtualPlatform.Disk.History.DiskUtl, ['history_records'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _vplatform as meta
                    return meta._meta_table['VirtualPlatform.Disk.History.DiskUtl']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _vplatform as meta
                return meta._meta_table['VirtualPlatform.Disk.History']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _vplatform as meta
            return meta._meta_table['VirtualPlatform.Disk']['meta_info']


    class Action(_Entity_):
        """
        
        
        .. attribute:: udi
        
        	UDI Operations
        	**type**\: list of  		 :py:class:`Udi <ydk.models.cisco_ios_xr.vplatform.VirtualPlatform.Action.Udi>`
        
        	**config**\: False
        
        

        """

        _prefix = 'vplatform'
        _revision = '2015-08-30'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(VirtualPlatform.Action, self).__init__()

            self.yang_name = "Action"
            self.yang_parent_name = "virtual-platform"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("udi", ("udi", VirtualPlatform.Action.Udi))])
            self._leafs = OrderedDict()

            self.udi = YList(self)
            self._segment_path = lambda: "Action"
            self._absolute_path = lambda: "vplatform:virtual-platform/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(VirtualPlatform.Action, [], name, value)


        class Udi(_Entity_):
            """
            UDI Operations
            
            

            """

            _prefix = 'vplatform'
            _revision = '2015-08-30'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(VirtualPlatform.Action.Udi, self).__init__()

                self.yang_name = "udi"
                self.yang_parent_name = "Action"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict()
                self._segment_path = lambda: "udi"
                self._absolute_path = lambda: "vplatform:virtual-platform/Action/%s" % self._segment_path()
                self._is_frozen = True

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _vplatform as meta
                return meta._meta_table['VirtualPlatform.Action.Udi']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _vplatform as meta
            return meta._meta_table['VirtualPlatform.Action']['meta_info']

    def clone_ptr(self):
        self._top_entity = VirtualPlatform()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _vplatform as meta
        return meta._meta_table['VirtualPlatform']['meta_info']


