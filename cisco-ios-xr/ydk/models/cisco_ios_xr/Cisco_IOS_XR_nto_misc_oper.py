""" Cisco_IOS_XR_nto_misc_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR nto\-misc package operational data.

This module contains definitions
for the following management objects\:
  memory\-summary\: Memory summary information

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class MemorySummary(object):
    """
    Memory summary information
    
    .. attribute:: nodes
    
    	List of nodes
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_nto_misc_oper.MemorySummary.Nodes>`
    
    

    """

    _prefix = 'nto-misc-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.nodes = MemorySummary.Nodes()
        self.nodes.parent = self


    class Nodes(object):
        """
        List of nodes
        
        .. attribute:: node
        
        	Name of nodes
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_nto_misc_oper.MemorySummary.Nodes.Node>`
        
        

        """

        _prefix = 'nto-misc-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.node = YList()
            self.node.parent = self
            self.node.name = 'node'


        class Node(object):
            """
            Name of nodes
            
            .. attribute:: node_name  <key>
            
            	Node name
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: detail
            
            	Detail Memory summary information for a specific node
            	**type**\:   :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_nto_misc_oper.MemorySummary.Nodes.Node.Detail>`
            
            .. attribute:: summary
            
            	Memory summary information for a specific node
            	**type**\:   :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_nto_misc_oper.MemorySummary.Nodes.Node.Summary>`
            
            

            """

            _prefix = 'nto-misc-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.node_name = None
                self.detail = MemorySummary.Nodes.Node.Detail()
                self.detail.parent = self
                self.summary = MemorySummary.Nodes.Node.Summary()
                self.summary.parent = self


            class Summary(object):
                """
                Memory summary information for a specific node
                
                .. attribute:: boot_ram_size
                
                	Boot RAM size in bytes
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: flash_system
                
                	Flash System size in bytes
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: free_application_memory
                
                	Application memory available in bytes
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: free_physical_memory
                
                	Physical memory available in bytes
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: image_memory
                
                	Image memory size in bytes
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: io_memory
                
                	IO memory size in bytes
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: page_size
                
                	Page size in bytes
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: byte
                
                .. attribute:: ram_memory
                
                	Physical memory size in bytes
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: reserved_memory
                
                	Reserved memory size in bytes
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: system_ram_memory
                
                	Application memory size in bytes
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                

                """

                _prefix = 'nto-misc-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.boot_ram_size = None
                    self.flash_system = None
                    self.free_application_memory = None
                    self.free_physical_memory = None
                    self.image_memory = None
                    self.io_memory = None
                    self.page_size = None
                    self.ram_memory = None
                    self.reserved_memory = None
                    self.system_ram_memory = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-nto-misc-oper:summary'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.boot_ram_size is not None:
                        return True

                    if self.flash_system is not None:
                        return True

                    if self.free_application_memory is not None:
                        return True

                    if self.free_physical_memory is not None:
                        return True

                    if self.image_memory is not None:
                        return True

                    if self.io_memory is not None:
                        return True

                    if self.page_size is not None:
                        return True

                    if self.ram_memory is not None:
                        return True

                    if self.reserved_memory is not None:
                        return True

                    if self.system_ram_memory is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_nto_misc_oper as meta
                    return meta._meta_table['MemorySummary.Nodes.Node.Summary']['meta_info']


            class Detail(object):
                """
                Detail Memory summary information for a
                specific node
                
                .. attribute:: allocated_memory
                
                	Allocated Memory Size
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: boot_ram_size
                
                	Boot RAM size in bytes
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: flash_system
                
                	Flash System size in bytes
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: free_application_memory
                
                	Application memory available in bytes
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: free_physical_memory
                
                	Physical memory available in bytes
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: image_memory
                
                	Image memory size in bytes
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: io_memory
                
                	IO memory size in bytes
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: page_size
                
                	Page size in bytes
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: byte
                
                .. attribute:: private_physical_memory
                
                	Private Physical memory in bytes
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: program_data
                
                	Program Data Size
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: program_stack
                
                	Program Stack Size
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: program_text
                
                	Program Text Size
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: ram_memory
                
                	Physical memory size in bytes
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: reserved_memory
                
                	Reserved memory size in bytes
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: shared_window
                
                	Available Shared windows
                	**type**\: list of    :py:class:`SharedWindow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_nto_misc_oper.MemorySummary.Nodes.Node.Detail.SharedWindow>`
                
                .. attribute:: system_ram_memory
                
                	Application memory size in bytes
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: total_shared_window
                
                	Total Shared window
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'nto-misc-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.allocated_memory = None
                    self.boot_ram_size = None
                    self.flash_system = None
                    self.free_application_memory = None
                    self.free_physical_memory = None
                    self.image_memory = None
                    self.io_memory = None
                    self.page_size = None
                    self.private_physical_memory = None
                    self.program_data = None
                    self.program_stack = None
                    self.program_text = None
                    self.ram_memory = None
                    self.reserved_memory = None
                    self.shared_window = YList()
                    self.shared_window.parent = self
                    self.shared_window.name = 'shared_window'
                    self.system_ram_memory = None
                    self.total_shared_window = None


                class SharedWindow(object):
                    """
                    Available Shared windows
                    
                    .. attribute:: shared_window
                    
                    	Name of shared window
                    	**type**\:  str
                    
                    .. attribute:: window_size
                    
                    	Size of shared window
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'nto-misc-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.shared_window = None
                        self.window_size = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-nto-misc-oper:shared-window'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.shared_window is not None:
                            return True

                        if self.window_size is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_nto_misc_oper as meta
                        return meta._meta_table['MemorySummary.Nodes.Node.Detail.SharedWindow']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-nto-misc-oper:detail'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.allocated_memory is not None:
                        return True

                    if self.boot_ram_size is not None:
                        return True

                    if self.flash_system is not None:
                        return True

                    if self.free_application_memory is not None:
                        return True

                    if self.free_physical_memory is not None:
                        return True

                    if self.image_memory is not None:
                        return True

                    if self.io_memory is not None:
                        return True

                    if self.page_size is not None:
                        return True

                    if self.private_physical_memory is not None:
                        return True

                    if self.program_data is not None:
                        return True

                    if self.program_stack is not None:
                        return True

                    if self.program_text is not None:
                        return True

                    if self.ram_memory is not None:
                        return True

                    if self.reserved_memory is not None:
                        return True

                    if self.shared_window is not None:
                        for child_ref in self.shared_window:
                            if child_ref._has_data():
                                return True

                    if self.system_ram_memory is not None:
                        return True

                    if self.total_shared_window is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_nto_misc_oper as meta
                    return meta._meta_table['MemorySummary.Nodes.Node.Detail']['meta_info']

            @property
            def _common_path(self):
                if self.node_name is None:
                    raise YPYModelError('Key property node_name is None')

                return '/Cisco-IOS-XR-nto-misc-oper:memory-summary/Cisco-IOS-XR-nto-misc-oper:nodes/Cisco-IOS-XR-nto-misc-oper:node[Cisco-IOS-XR-nto-misc-oper:node-name = ' + str(self.node_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.node_name is not None:
                    return True

                if self.detail is not None and self.detail._has_data():
                    return True

                if self.summary is not None and self.summary._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_nto_misc_oper as meta
                return meta._meta_table['MemorySummary.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-nto-misc-oper:memory-summary/Cisco-IOS-XR-nto-misc-oper:nodes'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_nto_misc_oper as meta
            return meta._meta_table['MemorySummary.Nodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-nto-misc-oper:memory-summary'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.nodes is not None and self.nodes._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_nto_misc_oper as meta
        return meta._meta_table['MemorySummary']['meta_info']


