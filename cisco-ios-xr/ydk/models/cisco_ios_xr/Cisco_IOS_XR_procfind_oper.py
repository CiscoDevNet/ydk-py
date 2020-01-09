""" Cisco_IOS_XR_procfind_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR procfind package operational data.

This module contains definitions
for the following management objects\:
  proc\-distribution\: Process distribution information

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




class ProcDistribution(_Entity_):
    """
    Process distribution information
    
    .. attribute:: nodes
    
    	List of nodes
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_procfind_oper.ProcDistribution.Nodes>`
    
    	**config**\: False
    
    

    """

    _prefix = 'procfind-oper'
    _revision = '2015-11-09'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(ProcDistribution, self).__init__()
        self._top_entity = None

        self.yang_name = "proc-distribution"
        self.yang_parent_name = "Cisco-IOS-XR-procfind-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("nodes", ("nodes", ProcDistribution.Nodes))])
        self._leafs = OrderedDict()

        self.nodes = ProcDistribution.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._segment_path = lambda: "Cisco-IOS-XR-procfind-oper:proc-distribution"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(ProcDistribution, [], name, value)


    class Nodes(_Entity_):
        """
        List of nodes
        
        .. attribute:: node
        
        	Process distribution information per node
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_procfind_oper.ProcDistribution.Nodes.Node>`
        
        	**config**\: False
        
        

        """

        _prefix = 'procfind-oper'
        _revision = '2015-11-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(ProcDistribution.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "proc-distribution"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node", ("node", ProcDistribution.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-procfind-oper:proc-distribution/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ProcDistribution.Nodes, [], name, value)


        class Node(_Entity_):
            """
            Process distribution information per node
            
            .. attribute:: node_name  (key)
            
            	The node name
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            	**config**\: False
            
            .. attribute:: process
            
            	Process distribution information
            	**type**\: list of  		 :py:class:`Process <ydk.models.cisco_ios_xr.Cisco_IOS_XR_procfind_oper.ProcDistribution.Nodes.Node.Process>`
            
            	**config**\: False
            
            

            """

            _prefix = 'procfind-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(ProcDistribution.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_classes = OrderedDict([("process", ("process", ProcDistribution.Nodes.Node.Process))])
                self._leafs = OrderedDict([
                    ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                ])
                self.node_name = None

                self.process = YList(self)
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-procfind-oper:proc-distribution/nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ProcDistribution.Nodes.Node, ['node_name'], name, value)


            class Process(_Entity_):
                """
                Process distribution information
                
                .. attribute:: proc_name  (key)
                
                	Process Name
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: filter_type
                
                	Process distribution information
                	**type**\: list of  		 :py:class:`FilterType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_procfind_oper.ProcDistribution.Nodes.Node.Process.FilterType>`
                
                	**config**\: False
                
                

                """

                _prefix = 'procfind-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(ProcDistribution.Nodes.Node.Process, self).__init__()

                    self.yang_name = "process"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['proc_name']
                    self._child_classes = OrderedDict([("filter-type", ("filter_type", ProcDistribution.Nodes.Node.Process.FilterType))])
                    self._leafs = OrderedDict([
                        ('proc_name', (YLeaf(YType.str, 'proc-name'), ['str'])),
                    ])
                    self.proc_name = None

                    self.filter_type = YList(self)
                    self._segment_path = lambda: "process" + "[proc-name='" + str(self.proc_name) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(ProcDistribution.Nodes.Node.Process, ['proc_name'], name, value)


                class FilterType(_Entity_):
                    """
                    Process distribution information
                    
                    .. attribute:: filter_type  (key)
                    
                    	Filter Type
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: nodeid
                    
                    	Node ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: nodetype
                    
                    	Node type
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: pid
                    
                    	Process ID
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**config**\: False
                    
                    .. attribute:: jid
                    
                    	Job ID
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**config**\: False
                    
                    .. attribute:: num_threads
                    
                    	Number of threads
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**config**\: False
                    
                    .. attribute:: name
                    
                    	Process name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'procfind-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(ProcDistribution.Nodes.Node.Process.FilterType, self).__init__()

                        self.yang_name = "filter-type"
                        self.yang_parent_name = "process"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['filter_type']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('filter_type', (YLeaf(YType.str, 'filter-type'), ['str'])),
                            ('nodeid', (YLeaf(YType.uint32, 'nodeid'), ['int'])),
                            ('nodetype', (YLeaf(YType.uint32, 'nodetype'), ['int'])),
                            ('pid', (YLeaf(YType.int32, 'pid'), ['int'])),
                            ('jid', (YLeaf(YType.int32, 'jid'), ['int'])),
                            ('num_threads', (YLeaf(YType.int32, 'num-threads'), ['int'])),
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                        ])
                        self.filter_type = None
                        self.nodeid = None
                        self.nodetype = None
                        self.pid = None
                        self.jid = None
                        self.num_threads = None
                        self.name = None
                        self._segment_path = lambda: "filter-type" + "[filter-type='" + str(self.filter_type) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ProcDistribution.Nodes.Node.Process.FilterType, ['filter_type', 'nodeid', 'nodetype', 'pid', 'jid', 'num_threads', 'name'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_procfind_oper as meta
                        return meta._meta_table['ProcDistribution.Nodes.Node.Process.FilterType']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_procfind_oper as meta
                    return meta._meta_table['ProcDistribution.Nodes.Node.Process']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_procfind_oper as meta
                return meta._meta_table['ProcDistribution.Nodes.Node']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_procfind_oper as meta
            return meta._meta_table['ProcDistribution.Nodes']['meta_info']

    def clone_ptr(self):
        self._top_entity = ProcDistribution()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_procfind_oper as meta
        return meta._meta_table['ProcDistribution']['meta_info']


