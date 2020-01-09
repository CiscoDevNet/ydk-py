""" Cisco_IOS_XR_wd_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR wd package operational data.

This module contains definitions
for the following management objects\:
  watchdog\: Watchdog information

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



class MemoryState(Enum):
    """
    MemoryState (Enum Class)

    Memory state options

    .. data:: unknown = 0

    	Memory state unknown

    .. data:: normal = 1

    	Memory state normal

    .. data:: minor = 2

    	Memory state minor

    .. data:: severe = 3

    	Memory state severe

    .. data:: critical = 4

    	Memory state critical

    """

    unknown = Enum.YLeaf(0, "unknown")

    normal = Enum.YLeaf(1, "normal")

    minor = Enum.YLeaf(2, "minor")

    severe = Enum.YLeaf(3, "severe")

    critical = Enum.YLeaf(4, "critical")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_wd_oper as meta
        return meta._meta_table['MemoryState']


class OverloadCtrlNotif(Enum):
    """
    OverloadCtrlNotif (Enum Class)

    Overload control notification

    .. data:: disabled = 0

    	Diabled

    .. data:: enabled = 1

    	Enabled

    """

    disabled = Enum.YLeaf(0, "disabled")

    enabled = Enum.YLeaf(1, "enabled")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_wd_oper as meta
        return meta._meta_table['OverloadCtrlNotif']



class Watchdog(_Entity_):
    """
    Watchdog information
    
    .. attribute:: nodes
    
    	List of nodes
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_oper.Watchdog.Nodes>`
    
    	**config**\: False
    
    

    """

    _prefix = 'wd-oper'
    _revision = '2015-11-09'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(Watchdog, self).__init__()
        self._top_entity = None

        self.yang_name = "watchdog"
        self.yang_parent_name = "Cisco-IOS-XR-wd-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("nodes", ("nodes", Watchdog.Nodes))])
        self._leafs = OrderedDict()

        self.nodes = Watchdog.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._segment_path = lambda: "Cisco-IOS-XR-wd-oper:watchdog"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Watchdog, [], name, value)


    class Nodes(_Entity_):
        """
        List of nodes
        
        .. attribute:: node
        
        	Node ID
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_oper.Watchdog.Nodes.Node>`
        
        	**config**\: False
        
        

        """

        _prefix = 'wd-oper'
        _revision = '2015-11-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Watchdog.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "watchdog"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node", ("node", Watchdog.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-wd-oper:watchdog/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Watchdog.Nodes, [], name, value)


        class Node(_Entity_):
            """
            Node ID
            
            .. attribute:: node_name  (key)
            
            	Node name
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            	**config**\: False
            
            .. attribute:: threshold_memory
            
            	Threshold memory
            	**type**\:  :py:class:`ThresholdMemory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_oper.Watchdog.Nodes.Node.ThresholdMemory>`
            
            	**config**\: False
            
            .. attribute:: memory_state
            
            	Memory state
            	**type**\:  :py:class:`MemoryState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_oper.Watchdog.Nodes.Node.MemoryState>`
            
            	**config**\: False
            
            .. attribute:: overload_state
            
            	Display overload control state
            	**type**\:  :py:class:`OverloadState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_oper.Watchdog.Nodes.Node.OverloadState>`
            
            	**config**\: False
            
            

            """

            _prefix = 'wd-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Watchdog.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_classes = OrderedDict([("threshold-memory", ("threshold_memory", Watchdog.Nodes.Node.ThresholdMemory)), ("memory-state", ("memory_state", Watchdog.Nodes.Node.MemoryState)), ("overload-state", ("overload_state", Watchdog.Nodes.Node.OverloadState))])
                self._leafs = OrderedDict([
                    ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                ])
                self.node_name = None

                self.threshold_memory = Watchdog.Nodes.Node.ThresholdMemory()
                self.threshold_memory.parent = self
                self._children_name_map["threshold_memory"] = "threshold-memory"

                self.memory_state = Watchdog.Nodes.Node.MemoryState()
                self.memory_state.parent = self
                self._children_name_map["memory_state"] = "memory-state"

                self.overload_state = Watchdog.Nodes.Node.OverloadState()
                self.overload_state.parent = self
                self._children_name_map["overload_state"] = "overload-state"
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-wd-oper:watchdog/nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Watchdog.Nodes.Node, ['node_name'], name, value)


            class ThresholdMemory(_Entity_):
                """
                Threshold memory
                
                .. attribute:: default
                
                	System default memory
                	**type**\:  :py:class:`Default <ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_oper.Watchdog.Nodes.Node.ThresholdMemory.Default>`
                
                	**config**\: False
                
                .. attribute:: configured
                
                	Memory configured by user
                	**type**\:  :py:class:`Configured <ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_oper.Watchdog.Nodes.Node.ThresholdMemory.Configured>`
                
                	**config**\: False
                
                

                """

                _prefix = 'wd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Watchdog.Nodes.Node.ThresholdMemory, self).__init__()

                    self.yang_name = "threshold-memory"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("default", ("default", Watchdog.Nodes.Node.ThresholdMemory.Default)), ("configured", ("configured", Watchdog.Nodes.Node.ThresholdMemory.Configured))])
                    self._leafs = OrderedDict()

                    self.default = Watchdog.Nodes.Node.ThresholdMemory.Default()
                    self.default.parent = self
                    self._children_name_map["default"] = "default"

                    self.configured = Watchdog.Nodes.Node.ThresholdMemory.Configured()
                    self.configured.parent = self
                    self._children_name_map["configured"] = "configured"
                    self._segment_path = lambda: "threshold-memory"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Watchdog.Nodes.Node.ThresholdMemory, [], name, value)


                class Default(_Entity_):
                    """
                    System default memory
                    
                    .. attribute:: configured_memory
                    
                    	Configured memory
                    	**type**\:  :py:class:`ConfiguredMemory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_oper.Watchdog.Nodes.Node.ThresholdMemory.Default.ConfiguredMemory>`
                    
                    	**config**\: False
                    
                    .. attribute:: memory
                    
                    	Memory Information
                    	**type**\:  :py:class:`Memory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_oper.Watchdog.Nodes.Node.ThresholdMemory.Default.Memory>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'wd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Watchdog.Nodes.Node.ThresholdMemory.Default, self).__init__()

                        self.yang_name = "default"
                        self.yang_parent_name = "threshold-memory"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("configured-memory", ("configured_memory", Watchdog.Nodes.Node.ThresholdMemory.Default.ConfiguredMemory)), ("memory", ("memory", Watchdog.Nodes.Node.ThresholdMemory.Default.Memory))])
                        self._leafs = OrderedDict()

                        self.configured_memory = Watchdog.Nodes.Node.ThresholdMemory.Default.ConfiguredMemory()
                        self.configured_memory.parent = self
                        self._children_name_map["configured_memory"] = "configured-memory"

                        self.memory = Watchdog.Nodes.Node.ThresholdMemory.Default.Memory()
                        self.memory.parent = self
                        self._children_name_map["memory"] = "memory"
                        self._segment_path = lambda: "default"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Watchdog.Nodes.Node.ThresholdMemory.Default, [], name, value)


                    class ConfiguredMemory(_Entity_):
                        """
                        Configured memory
                        
                        .. attribute:: minor
                        
                        	Minor memory threshold in bytes
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        	**units**\: byte
                        
                        .. attribute:: severe
                        
                        	Severe memory threshold in bytes
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        	**units**\: byte
                        
                        .. attribute:: critical
                        
                        	Critical memory in bytes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        	**units**\: byte
                        
                        

                        """

                        _prefix = 'wd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Watchdog.Nodes.Node.ThresholdMemory.Default.ConfiguredMemory, self).__init__()

                            self.yang_name = "configured-memory"
                            self.yang_parent_name = "default"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('minor', (YLeaf(YType.uint32, 'minor'), ['int'])),
                                ('severe', (YLeaf(YType.uint32, 'severe'), ['int'])),
                                ('critical', (YLeaf(YType.uint64, 'critical'), ['int'])),
                            ])
                            self.minor = None
                            self.severe = None
                            self.critical = None
                            self._segment_path = lambda: "configured-memory"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Watchdog.Nodes.Node.ThresholdMemory.Default.ConfiguredMemory, ['minor', 'severe', 'critical'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_wd_oper as meta
                            return meta._meta_table['Watchdog.Nodes.Node.ThresholdMemory.Default.ConfiguredMemory']['meta_info']


                    class Memory(_Entity_):
                        """
                        Memory Information
                        
                        .. attribute:: physical_memory
                        
                        	Physical memory in bytes
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        	**units**\: byte
                        
                        .. attribute:: free_memory
                        
                        	Free memory in bytes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        	**units**\: byte
                        
                        .. attribute:: memory_state
                        
                        	State of memory
                        	**type**\:  :py:class:`MemoryState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_oper.MemoryState>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'wd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Watchdog.Nodes.Node.ThresholdMemory.Default.Memory, self).__init__()

                            self.yang_name = "memory"
                            self.yang_parent_name = "default"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('physical_memory', (YLeaf(YType.uint32, 'physical-memory'), ['int'])),
                                ('free_memory', (YLeaf(YType.uint64, 'free-memory'), ['int'])),
                                ('memory_state', (YLeaf(YType.enumeration, 'memory-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_oper', 'MemoryState', '')])),
                            ])
                            self.physical_memory = None
                            self.free_memory = None
                            self.memory_state = None
                            self._segment_path = lambda: "memory"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Watchdog.Nodes.Node.ThresholdMemory.Default.Memory, ['physical_memory', 'free_memory', 'memory_state'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_wd_oper as meta
                            return meta._meta_table['Watchdog.Nodes.Node.ThresholdMemory.Default.Memory']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_wd_oper as meta
                        return meta._meta_table['Watchdog.Nodes.Node.ThresholdMemory.Default']['meta_info']


                class Configured(_Entity_):
                    """
                    Memory configured by user
                    
                    .. attribute:: minor
                    
                    	Minor memory threshold in bytes
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    	**units**\: byte
                    
                    .. attribute:: severe
                    
                    	Severe memory threshold in bytes
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    	**units**\: byte
                    
                    .. attribute:: critical
                    
                    	Critical memory in bytes
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    	**units**\: byte
                    
                    

                    """

                    _prefix = 'wd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Watchdog.Nodes.Node.ThresholdMemory.Configured, self).__init__()

                        self.yang_name = "configured"
                        self.yang_parent_name = "threshold-memory"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('minor', (YLeaf(YType.uint32, 'minor'), ['int'])),
                            ('severe', (YLeaf(YType.uint32, 'severe'), ['int'])),
                            ('critical', (YLeaf(YType.uint64, 'critical'), ['int'])),
                        ])
                        self.minor = None
                        self.severe = None
                        self.critical = None
                        self._segment_path = lambda: "configured"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Watchdog.Nodes.Node.ThresholdMemory.Configured, ['minor', 'severe', 'critical'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_wd_oper as meta
                        return meta._meta_table['Watchdog.Nodes.Node.ThresholdMemory.Configured']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_wd_oper as meta
                    return meta._meta_table['Watchdog.Nodes.Node.ThresholdMemory']['meta_info']


            class MemoryState(_Entity_):
                """
                Memory state
                
                .. attribute:: physical_memory
                
                	Physical memory in bytes
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                	**units**\: byte
                
                .. attribute:: free_memory
                
                	Free memory in bytes
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                	**units**\: byte
                
                .. attribute:: memory_state
                
                	State of memory
                	**type**\:  :py:class:`MemoryState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_oper.MemoryState>`
                
                	**config**\: False
                
                

                """

                _prefix = 'wd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Watchdog.Nodes.Node.MemoryState, self).__init__()

                    self.yang_name = "memory-state"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('physical_memory', (YLeaf(YType.uint32, 'physical-memory'), ['int'])),
                        ('free_memory', (YLeaf(YType.uint64, 'free-memory'), ['int'])),
                        ('memory_state', (YLeaf(YType.enumeration, 'memory-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_oper', 'MemoryState', '')])),
                    ])
                    self.physical_memory = None
                    self.free_memory = None
                    self.memory_state = None
                    self._segment_path = lambda: "memory-state"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Watchdog.Nodes.Node.MemoryState, ['physical_memory', 'free_memory', 'memory_state'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_wd_oper as meta
                    return meta._meta_table['Watchdog.Nodes.Node.MemoryState']['meta_info']


            class OverloadState(_Entity_):
                """
                Display overload control state
                
                .. attribute:: current_throttle
                
                	Current throttle information
                	**type**\:  :py:class:`CurrentThrottle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_oper.Watchdog.Nodes.Node.OverloadState.CurrentThrottle>`
                
                	**config**\: False
                
                .. attribute:: overload_control_notification
                
                	State of overload control notification
                	**type**\:  :py:class:`OverloadCtrlNotif <ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_oper.OverloadCtrlNotif>`
                
                	**config**\: False
                
                .. attribute:: default_wdsysmon_throttle
                
                	Default resmon throttle
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: configured_wdsysmon_throttle
                
                	Configured resmon throttle
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: last_throttle
                
                	Last throttle information
                	**type**\: list of  		 :py:class:`LastThrottle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_oper.Watchdog.Nodes.Node.OverloadState.LastThrottle>`
                
                	**config**\: False
                
                

                """

                _prefix = 'wd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Watchdog.Nodes.Node.OverloadState, self).__init__()

                    self.yang_name = "overload-state"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("current-throttle", ("current_throttle", Watchdog.Nodes.Node.OverloadState.CurrentThrottle)), ("last-throttle", ("last_throttle", Watchdog.Nodes.Node.OverloadState.LastThrottle))])
                    self._leafs = OrderedDict([
                        ('overload_control_notification', (YLeaf(YType.enumeration, 'overload-control-notification'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_oper', 'OverloadCtrlNotif', '')])),
                        ('default_wdsysmon_throttle', (YLeaf(YType.uint32, 'default-wdsysmon-throttle'), ['int'])),
                        ('configured_wdsysmon_throttle', (YLeaf(YType.uint32, 'configured-wdsysmon-throttle'), ['int'])),
                    ])
                    self.overload_control_notification = None
                    self.default_wdsysmon_throttle = None
                    self.configured_wdsysmon_throttle = None

                    self.current_throttle = Watchdog.Nodes.Node.OverloadState.CurrentThrottle()
                    self.current_throttle.parent = self
                    self._children_name_map["current_throttle"] = "current-throttle"

                    self.last_throttle = YList(self)
                    self._segment_path = lambda: "overload-state"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Watchdog.Nodes.Node.OverloadState, ['overload_control_notification', 'default_wdsysmon_throttle', 'configured_wdsysmon_throttle'], name, value)


                class CurrentThrottle(_Entity_):
                    """
                    Current throttle information
                    
                    .. attribute:: throttle_duration
                    
                    	Current throttle duration in seconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    	**units**\: second
                    
                    .. attribute:: start_time
                    
                    	Current throttle start time in format \:day\-of\-week month date\-of\-month HH\:MM\:SS year eg\: Thu Feb 1 18\:32\:14 2011
                    	**type**\: str
                    
                    	**length:** 0..25
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'wd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Watchdog.Nodes.Node.OverloadState.CurrentThrottle, self).__init__()

                        self.yang_name = "current-throttle"
                        self.yang_parent_name = "overload-state"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('throttle_duration', (YLeaf(YType.uint32, 'throttle-duration'), ['int'])),
                            ('start_time', (YLeaf(YType.str, 'start-time'), ['str'])),
                        ])
                        self.throttle_duration = None
                        self.start_time = None
                        self._segment_path = lambda: "current-throttle"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Watchdog.Nodes.Node.OverloadState.CurrentThrottle, ['throttle_duration', 'start_time'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_wd_oper as meta
                        return meta._meta_table['Watchdog.Nodes.Node.OverloadState.CurrentThrottle']['meta_info']


                class LastThrottle(_Entity_):
                    """
                    Last throttle information
                    
                    .. attribute:: throttle_duration
                    
                    	Last throttle duration in seconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    	**units**\: second
                    
                    .. attribute:: start_time
                    
                    	Last throttle start time in format \:day\-of\-week month date\-of\-month HH\:MM\:SS year eg\: Thu Feb 1 18\:32\:14 2011
                    	**type**\: str
                    
                    	**length:** 0..25
                    
                    	**config**\: False
                    
                    .. attribute:: stop_time
                    
                    	Last throttle stop time in format \:day\-of\-week month date\-of\-month HH\:MM\:SS year eg\: Thu Feb 1 18\:32\:14 2011
                    	**type**\: str
                    
                    	**length:** 0..25
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'wd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Watchdog.Nodes.Node.OverloadState.LastThrottle, self).__init__()

                        self.yang_name = "last-throttle"
                        self.yang_parent_name = "overload-state"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('throttle_duration', (YLeaf(YType.uint32, 'throttle-duration'), ['int'])),
                            ('start_time', (YLeaf(YType.str, 'start-time'), ['str'])),
                            ('stop_time', (YLeaf(YType.str, 'stop-time'), ['str'])),
                        ])
                        self.throttle_duration = None
                        self.start_time = None
                        self.stop_time = None
                        self._segment_path = lambda: "last-throttle"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Watchdog.Nodes.Node.OverloadState.LastThrottle, ['throttle_duration', 'start_time', 'stop_time'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_wd_oper as meta
                        return meta._meta_table['Watchdog.Nodes.Node.OverloadState.LastThrottle']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_wd_oper as meta
                    return meta._meta_table['Watchdog.Nodes.Node.OverloadState']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_wd_oper as meta
                return meta._meta_table['Watchdog.Nodes.Node']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_wd_oper as meta
            return meta._meta_table['Watchdog.Nodes']['meta_info']

    def clone_ptr(self):
        self._top_entity = Watchdog()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_wd_oper as meta
        return meta._meta_table['Watchdog']['meta_info']


