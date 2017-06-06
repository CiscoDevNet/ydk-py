""" Cisco_IOS_XR_wd_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR wd package operational data.

This module contains definitions
for the following management objects\:
  watchdog\: Watchdog information

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class MemoryStateEnum(Enum):
    """
    MemoryStateEnum

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

    unknown = 0

    normal = 1

    minor = 2

    severe = 3

    critical = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_wd_oper as meta
        return meta._meta_table['MemoryStateEnum']


class OverloadCtrlNotifEnum(Enum):
    """
    OverloadCtrlNotifEnum

    Overload control notification

    .. data:: disabled = 0

    	Diabled

    .. data:: enabled = 1

    	Enabled

    """

    disabled = 0

    enabled = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_wd_oper as meta
        return meta._meta_table['OverloadCtrlNotifEnum']



class Watchdog(object):
    """
    Watchdog information
    
    .. attribute:: nodes
    
    	List of nodes
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_oper.Watchdog.Nodes>`
    
    

    """

    _prefix = 'wd-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.nodes = Watchdog.Nodes()
        self.nodes.parent = self


    class Nodes(object):
        """
        List of nodes
        
        .. attribute:: node
        
        	Node ID
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_oper.Watchdog.Nodes.Node>`
        
        

        """

        _prefix = 'wd-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.node = YList()
            self.node.parent = self
            self.node.name = 'node'


        class Node(object):
            """
            Node ID
            
            .. attribute:: node_name  <key>
            
            	Node name
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: memory_state
            
            	Memory state
            	**type**\:   :py:class:`MemoryState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_oper.Watchdog.Nodes.Node.MemoryState>`
            
            .. attribute:: overload_state
            
            	Display overload control state
            	**type**\:   :py:class:`OverloadState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_oper.Watchdog.Nodes.Node.OverloadState>`
            
            .. attribute:: threshold_memory
            
            	Threshold memory
            	**type**\:   :py:class:`ThresholdMemory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_oper.Watchdog.Nodes.Node.ThresholdMemory>`
            
            

            """

            _prefix = 'wd-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.node_name = None
                self.memory_state = Watchdog.Nodes.Node.MemoryState()
                self.memory_state.parent = self
                self.overload_state = Watchdog.Nodes.Node.OverloadState()
                self.overload_state.parent = self
                self.threshold_memory = Watchdog.Nodes.Node.ThresholdMemory()
                self.threshold_memory.parent = self


            class ThresholdMemory(object):
                """
                Threshold memory
                
                .. attribute:: configured
                
                	Memory configured by user
                	**type**\:   :py:class:`Configured <ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_oper.Watchdog.Nodes.Node.ThresholdMemory.Configured>`
                
                .. attribute:: default
                
                	System default memory
                	**type**\:   :py:class:`Default <ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_oper.Watchdog.Nodes.Node.ThresholdMemory.Default>`
                
                

                """

                _prefix = 'wd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.configured = Watchdog.Nodes.Node.ThresholdMemory.Configured()
                    self.configured.parent = self
                    self.default = Watchdog.Nodes.Node.ThresholdMemory.Default()
                    self.default.parent = self


                class Default(object):
                    """
                    System default memory
                    
                    .. attribute:: configured_memory
                    
                    	Configured memory
                    	**type**\:   :py:class:`ConfiguredMemory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_oper.Watchdog.Nodes.Node.ThresholdMemory.Default.ConfiguredMemory>`
                    
                    .. attribute:: memory
                    
                    	Memory Information
                    	**type**\:   :py:class:`Memory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_oper.Watchdog.Nodes.Node.ThresholdMemory.Default.Memory>`
                    
                    

                    """

                    _prefix = 'wd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.configured_memory = Watchdog.Nodes.Node.ThresholdMemory.Default.ConfiguredMemory()
                        self.configured_memory.parent = self
                        self.memory = Watchdog.Nodes.Node.ThresholdMemory.Default.Memory()
                        self.memory.parent = self


                    class ConfiguredMemory(object):
                        """
                        Configured memory
                        
                        .. attribute:: critical
                        
                        	Critical memory in bytes
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: byte
                        
                        .. attribute:: minor
                        
                        	Minor memory threshold in bytes
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: byte
                        
                        .. attribute:: severe
                        
                        	Severe memory threshold in bytes
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: byte
                        
                        

                        """

                        _prefix = 'wd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.critical = None
                            self.minor = None
                            self.severe = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-wd-oper:configured-memory'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.critical is not None:
                                return True

                            if self.minor is not None:
                                return True

                            if self.severe is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_wd_oper as meta
                            return meta._meta_table['Watchdog.Nodes.Node.ThresholdMemory.Default.ConfiguredMemory']['meta_info']


                    class Memory(object):
                        """
                        Memory Information
                        
                        .. attribute:: free_memory
                        
                        	Free memory in bytes
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: byte
                        
                        .. attribute:: memory_state
                        
                        	State of memory
                        	**type**\:   :py:class:`MemoryStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_oper.MemoryStateEnum>`
                        
                        .. attribute:: physical_memory
                        
                        	Physical memory in bytes
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: byte
                        
                        

                        """

                        _prefix = 'wd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.free_memory = None
                            self.memory_state = None
                            self.physical_memory = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-wd-oper:memory'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.free_memory is not None:
                                return True

                            if self.memory_state is not None:
                                return True

                            if self.physical_memory is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_wd_oper as meta
                            return meta._meta_table['Watchdog.Nodes.Node.ThresholdMemory.Default.Memory']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-wd-oper:default'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.configured_memory is not None and self.configured_memory._has_data():
                            return True

                        if self.memory is not None and self.memory._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_wd_oper as meta
                        return meta._meta_table['Watchdog.Nodes.Node.ThresholdMemory.Default']['meta_info']


                class Configured(object):
                    """
                    Memory configured by user
                    
                    .. attribute:: critical
                    
                    	Critical memory in bytes
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: byte
                    
                    .. attribute:: minor
                    
                    	Minor memory threshold in bytes
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: byte
                    
                    .. attribute:: severe
                    
                    	Severe memory threshold in bytes
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: byte
                    
                    

                    """

                    _prefix = 'wd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.critical = None
                        self.minor = None
                        self.severe = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-wd-oper:configured'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.critical is not None:
                            return True

                        if self.minor is not None:
                            return True

                        if self.severe is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_wd_oper as meta
                        return meta._meta_table['Watchdog.Nodes.Node.ThresholdMemory.Configured']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-wd-oper:threshold-memory'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.configured is not None and self.configured._has_data():
                        return True

                    if self.default is not None and self.default._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_wd_oper as meta
                    return meta._meta_table['Watchdog.Nodes.Node.ThresholdMemory']['meta_info']


            class MemoryState(object):
                """
                Memory state
                
                .. attribute:: free_memory
                
                	Free memory in bytes
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: memory_state
                
                	State of memory
                	**type**\:   :py:class:`MemoryStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_oper.MemoryStateEnum>`
                
                .. attribute:: physical_memory
                
                	Physical memory in bytes
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: byte
                
                

                """

                _prefix = 'wd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.free_memory = None
                    self.memory_state = None
                    self.physical_memory = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-wd-oper:memory-state'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.free_memory is not None:
                        return True

                    if self.memory_state is not None:
                        return True

                    if self.physical_memory is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_wd_oper as meta
                    return meta._meta_table['Watchdog.Nodes.Node.MemoryState']['meta_info']


            class OverloadState(object):
                """
                Display overload control state
                
                .. attribute:: configured_wdsysmon_throttle
                
                	Configured resmon throttle
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: current_throttle
                
                	Current throttle information
                	**type**\:   :py:class:`CurrentThrottle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_oper.Watchdog.Nodes.Node.OverloadState.CurrentThrottle>`
                
                .. attribute:: default_wdsysmon_throttle
                
                	Default resmon throttle
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: last_throttle
                
                	Last throttle information
                	**type**\: list of    :py:class:`LastThrottle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_oper.Watchdog.Nodes.Node.OverloadState.LastThrottle>`
                
                .. attribute:: overload_control_notification
                
                	State of overload control notification
                	**type**\:   :py:class:`OverloadCtrlNotifEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_oper.OverloadCtrlNotifEnum>`
                
                

                """

                _prefix = 'wd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.configured_wdsysmon_throttle = None
                    self.current_throttle = Watchdog.Nodes.Node.OverloadState.CurrentThrottle()
                    self.current_throttle.parent = self
                    self.default_wdsysmon_throttle = None
                    self.last_throttle = YList()
                    self.last_throttle.parent = self
                    self.last_throttle.name = 'last_throttle'
                    self.overload_control_notification = None


                class CurrentThrottle(object):
                    """
                    Current throttle information
                    
                    .. attribute:: start_time
                    
                    	Current throttle start time in format  \:day\-of\-week month date\-of\-month HH\:MM\:SS year eg\: Thu Feb 1 18\:32\:14 2011
                    	**type**\:  str
                    
                    	**length:** 0..25
                    
                    .. attribute:: throttle_duration
                    
                    	Current throttle duration in seconds
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    

                    """

                    _prefix = 'wd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.start_time = None
                        self.throttle_duration = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-wd-oper:current-throttle'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.start_time is not None:
                            return True

                        if self.throttle_duration is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_wd_oper as meta
                        return meta._meta_table['Watchdog.Nodes.Node.OverloadState.CurrentThrottle']['meta_info']


                class LastThrottle(object):
                    """
                    Last throttle information
                    
                    .. attribute:: start_time
                    
                    	Last throttle start time in format \:day\-of\-week month date\-of\-month HH\:MM\:SS year eg\: Thu Feb 1 18\:32\:14 2011
                    	**type**\:  str
                    
                    	**length:** 0..25
                    
                    .. attribute:: stop_time
                    
                    	Last throttle stop time in format \:day\-of\-week month date\-of\-month HH\:MM\:SS year eg\: Thu Feb 1 18\:32\:14 2011
                    	**type**\:  str
                    
                    	**length:** 0..25
                    
                    .. attribute:: throttle_duration
                    
                    	Last throttle duration in seconds
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    

                    """

                    _prefix = 'wd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.start_time = None
                        self.stop_time = None
                        self.throttle_duration = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-wd-oper:last-throttle'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.start_time is not None:
                            return True

                        if self.stop_time is not None:
                            return True

                        if self.throttle_duration is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_wd_oper as meta
                        return meta._meta_table['Watchdog.Nodes.Node.OverloadState.LastThrottle']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-wd-oper:overload-state'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.configured_wdsysmon_throttle is not None:
                        return True

                    if self.current_throttle is not None and self.current_throttle._has_data():
                        return True

                    if self.default_wdsysmon_throttle is not None:
                        return True

                    if self.last_throttle is not None:
                        for child_ref in self.last_throttle:
                            if child_ref._has_data():
                                return True

                    if self.overload_control_notification is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_wd_oper as meta
                    return meta._meta_table['Watchdog.Nodes.Node.OverloadState']['meta_info']

            @property
            def _common_path(self):
                if self.node_name is None:
                    raise YPYModelError('Key property node_name is None')

                return '/Cisco-IOS-XR-wd-oper:watchdog/Cisco-IOS-XR-wd-oper:nodes/Cisco-IOS-XR-wd-oper:node[Cisco-IOS-XR-wd-oper:node-name = ' + str(self.node_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.node_name is not None:
                    return True

                if self.memory_state is not None and self.memory_state._has_data():
                    return True

                if self.overload_state is not None and self.overload_state._has_data():
                    return True

                if self.threshold_memory is not None and self.threshold_memory._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_wd_oper as meta
                return meta._meta_table['Watchdog.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-wd-oper:watchdog/Cisco-IOS-XR-wd-oper:nodes'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.node is not None:
                for child_ref in self.node:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_wd_oper as meta
            return meta._meta_table['Watchdog.Nodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-wd-oper:watchdog'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.nodes is not None and self.nodes._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_wd_oper as meta
        return meta._meta_table['Watchdog']['meta_info']


