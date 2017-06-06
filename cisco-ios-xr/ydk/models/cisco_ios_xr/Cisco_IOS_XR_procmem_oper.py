""" Cisco_IOS_XR_procmem_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR procmem package operational data.

This module contains definitions
for the following management objects\:
  processes\-memory\: Process statistics

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class ProcessesMemory(object):
    """
    Process statistics
    
    .. attribute:: nodes
    
    	List of nodes
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_procmem_oper.ProcessesMemory.Nodes>`
    
    

    """

    _prefix = 'procmem-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.nodes = ProcessesMemory.Nodes()
        self.nodes.parent = self


    class Nodes(object):
        """
        List of nodes
        
        .. attribute:: node
        
        	Node ID
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_procmem_oper.ProcessesMemory.Nodes.Node>`
        
        

        """

        _prefix = 'procmem-oper'
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
            
            .. attribute:: process_ids
            
            	List of jobs
            	**type**\:   :py:class:`ProcessIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_procmem_oper.ProcessesMemory.Nodes.Node.ProcessIds>`
            
            

            """

            _prefix = 'procmem-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.node_name = None
                self.process_ids = ProcessesMemory.Nodes.Node.ProcessIds()
                self.process_ids.parent = self


            class ProcessIds(object):
                """
                List of jobs
                
                .. attribute:: process_id
                
                	Process Id
                	**type**\: list of    :py:class:`ProcessId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_procmem_oper.ProcessesMemory.Nodes.Node.ProcessIds.ProcessId>`
                
                

                """

                _prefix = 'procmem-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.process_id = YList()
                    self.process_id.parent = self
                    self.process_id.name = 'process_id'


                class ProcessId(object):
                    """
                    Process Id
                    
                    .. attribute:: process_id  <key>
                    
                    	Process Id
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: data_seg_size
                    
                    	Data Segment Size
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: dyn_limit
                    
                    	Dynamic memory limit
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: jid
                    
                    	Job ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: malloc_size
                    
                    	Malloced Memory Size
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: name
                    
                    	Process name
                    	**type**\:  str
                    
                    .. attribute:: physical_mem
                    
                    	Physical memory size
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: pid
                    
                    	Process ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: shared_mem
                    
                    	Shared memory size
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: stack_seg_size
                    
                    	Stack Segment Size
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: text_seg_size
                    
                    	Text Segment Size
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'procmem-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.process_id = None
                        self.data_seg_size = None
                        self.dyn_limit = None
                        self.jid = None
                        self.malloc_size = None
                        self.name = None
                        self.physical_mem = None
                        self.pid = None
                        self.shared_mem = None
                        self.stack_seg_size = None
                        self.text_seg_size = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.process_id is None:
                            raise YPYModelError('Key property process_id is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-procmem-oper:process-id[Cisco-IOS-XR-procmem-oper:process-id = ' + str(self.process_id) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.process_id is not None:
                            return True

                        if self.data_seg_size is not None:
                            return True

                        if self.dyn_limit is not None:
                            return True

                        if self.jid is not None:
                            return True

                        if self.malloc_size is not None:
                            return True

                        if self.name is not None:
                            return True

                        if self.physical_mem is not None:
                            return True

                        if self.pid is not None:
                            return True

                        if self.shared_mem is not None:
                            return True

                        if self.stack_seg_size is not None:
                            return True

                        if self.text_seg_size is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_procmem_oper as meta
                        return meta._meta_table['ProcessesMemory.Nodes.Node.ProcessIds.ProcessId']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-procmem-oper:process-ids'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.process_id is not None:
                        for child_ref in self.process_id:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_procmem_oper as meta
                    return meta._meta_table['ProcessesMemory.Nodes.Node.ProcessIds']['meta_info']

            @property
            def _common_path(self):
                if self.node_name is None:
                    raise YPYModelError('Key property node_name is None')

                return '/Cisco-IOS-XR-procmem-oper:processes-memory/Cisco-IOS-XR-procmem-oper:nodes/Cisco-IOS-XR-procmem-oper:node[Cisco-IOS-XR-procmem-oper:node-name = ' + str(self.node_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.node_name is not None:
                    return True

                if self.process_ids is not None and self.process_ids._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_procmem_oper as meta
                return meta._meta_table['ProcessesMemory.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-procmem-oper:processes-memory/Cisco-IOS-XR-procmem-oper:nodes'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_procmem_oper as meta
            return meta._meta_table['ProcessesMemory.Nodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-procmem-oper:processes-memory'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.nodes is not None and self.nodes._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_procmem_oper as meta
        return meta._meta_table['ProcessesMemory']['meta_info']


