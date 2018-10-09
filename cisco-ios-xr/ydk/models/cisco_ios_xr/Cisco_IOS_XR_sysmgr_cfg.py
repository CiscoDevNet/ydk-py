""" Cisco_IOS_XR_sysmgr_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR sysmgr package configuration.

This module contains definitions
for the following management objects\:
  process\-mandatory\: Process mandatory configuration
  process\-single\-crash\: process single crash

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class ProcessMandatory(Entity):
    """
    Process mandatory configuration
    
    .. attribute:: nodes
    
    	Table of mandatory nodes
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_cfg.ProcessMandatory.Nodes>`
    
    .. attribute:: all
    
    	Mandatory for all nodes
    	**type**\:  :py:class:`All <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_cfg.ProcessMandatory.All>`
    
    

    """

    _prefix = 'sysmgr-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(ProcessMandatory, self).__init__()
        self._top_entity = None

        self.yang_name = "process-mandatory"
        self.yang_parent_name = "Cisco-IOS-XR-sysmgr-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("nodes", ("nodes", ProcessMandatory.Nodes)), ("all", ("all", ProcessMandatory.All))])
        self._leafs = OrderedDict()

        self.nodes = ProcessMandatory.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"

        self.all = ProcessMandatory.All()
        self.all.parent = self
        self._children_name_map["all"] = "all"
        self._segment_path = lambda: "Cisco-IOS-XR-sysmgr-cfg:process-mandatory"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(ProcessMandatory, [], name, value)


    class Nodes(Entity):
        """
        Table of mandatory nodes
        
        .. attribute:: node
        
        	Mandatory node
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_cfg.ProcessMandatory.Nodes.Node>`
        
        

        """

        _prefix = 'sysmgr-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(ProcessMandatory.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "process-mandatory"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node", ("node", ProcessMandatory.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysmgr-cfg:process-mandatory/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ProcessMandatory.Nodes, [], name, value)


        class Node(Entity):
            """
            Mandatory node
            
            .. attribute:: node_name  (key)
            
            	Node name
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: processes
            
            	Table of processes
            	**type**\:  :py:class:`Processes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_cfg.ProcessMandatory.Nodes.Node.Processes>`
            
            

            """

            _prefix = 'sysmgr-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(ProcessMandatory.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_classes = OrderedDict([("processes", ("processes", ProcessMandatory.Nodes.Node.Processes))])
                self._leafs = OrderedDict([
                    ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                ])
                self.node_name = None

                self.processes = ProcessMandatory.Nodes.Node.Processes()
                self.processes.parent = self
                self._children_name_map["processes"] = "processes"
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysmgr-cfg:process-mandatory/nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ProcessMandatory.Nodes.Node, ['node_name'], name, value)


            class Processes(Entity):
                """
                Table of processes
                
                .. attribute:: process
                
                	Name of the executable process
                	**type**\: list of  		 :py:class:`Process <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_cfg.ProcessMandatory.Nodes.Node.Processes.Process>`
                
                

                """

                _prefix = 'sysmgr-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ProcessMandatory.Nodes.Node.Processes, self).__init__()

                    self.yang_name = "processes"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("process", ("process", ProcessMandatory.Nodes.Node.Processes.Process))])
                    self._leafs = OrderedDict()

                    self.process = YList(self)
                    self._segment_path = lambda: "processes"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(ProcessMandatory.Nodes.Node.Processes, [], name, value)


                class Process(Entity):
                    """
                    Name of the executable process
                    
                    .. attribute:: process_name  (key)
                    
                    	Process name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    

                    """

                    _prefix = 'sysmgr-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ProcessMandatory.Nodes.Node.Processes.Process, self).__init__()

                        self.yang_name = "process"
                        self.yang_parent_name = "processes"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['process_name']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('process_name', (YLeaf(YType.str, 'process-name'), ['str'])),
                        ])
                        self.process_name = None
                        self._segment_path = lambda: "process" + "[process-name='" + str(self.process_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ProcessMandatory.Nodes.Node.Processes.Process, ['process_name'], name, value)


    class All(Entity):
        """
        Mandatory for all nodes
        
        .. attribute:: processes
        
        	Table of processes
        	**type**\:  :py:class:`Processes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_cfg.ProcessMandatory.All.Processes>`
        
        

        """

        _prefix = 'sysmgr-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(ProcessMandatory.All, self).__init__()

            self.yang_name = "all"
            self.yang_parent_name = "process-mandatory"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("processes", ("processes", ProcessMandatory.All.Processes))])
            self._leafs = OrderedDict()

            self.processes = ProcessMandatory.All.Processes()
            self.processes.parent = self
            self._children_name_map["processes"] = "processes"
            self._segment_path = lambda: "all"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysmgr-cfg:process-mandatory/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ProcessMandatory.All, [], name, value)


        class Processes(Entity):
            """
            Table of processes
            
            .. attribute:: process
            
            	Name of the executable process
            	**type**\: list of  		 :py:class:`Process <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_cfg.ProcessMandatory.All.Processes.Process>`
            
            

            """

            _prefix = 'sysmgr-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(ProcessMandatory.All.Processes, self).__init__()

                self.yang_name = "processes"
                self.yang_parent_name = "all"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("process", ("process", ProcessMandatory.All.Processes.Process))])
                self._leafs = OrderedDict()

                self.process = YList(self)
                self._segment_path = lambda: "processes"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysmgr-cfg:process-mandatory/all/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ProcessMandatory.All.Processes, [], name, value)


            class Process(Entity):
                """
                Name of the executable process
                
                .. attribute:: process_name  (key)
                
                	Process name
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                

                """

                _prefix = 'sysmgr-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ProcessMandatory.All.Processes.Process, self).__init__()

                    self.yang_name = "process"
                    self.yang_parent_name = "processes"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['process_name']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('process_name', (YLeaf(YType.str, 'process-name'), ['str'])),
                    ])
                    self.process_name = None
                    self._segment_path = lambda: "process" + "[process-name='" + str(self.process_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysmgr-cfg:process-mandatory/all/processes/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(ProcessMandatory.All.Processes.Process, ['process_name'], name, value)

    def clone_ptr(self):
        self._top_entity = ProcessMandatory()
        return self._top_entity

class ProcessSingleCrash(Entity):
    """
    process single crash
    
    .. attribute:: crashes
    
    	Number of crashes for a process to trigger reboot
    	**type**\: int
    
    	**range:** 1..500
    
    	**mandatory**\: True
    
    .. attribute:: minimum_up_time
    
    	Minimum process up time (in seconds) to reset crash count
    	**type**\: int
    
    	**range:** 0..4294967295
    
    	**units**\: second
    
    	**default value**\: 0
    
    

    This class is a :ref:`presence class<presence-class>`

    """

    _prefix = 'sysmgr-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(ProcessSingleCrash, self).__init__()
        self._top_entity = None

        self.yang_name = "process-single-crash"
        self.yang_parent_name = "Cisco-IOS-XR-sysmgr-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self.is_presence_container = True
        self._leafs = OrderedDict([
            ('crashes', (YLeaf(YType.uint32, 'crashes'), ['int'])),
            ('minimum_up_time', (YLeaf(YType.uint32, 'minimum-up-time'), ['int'])),
        ])
        self.crashes = None
        self.minimum_up_time = None
        self._segment_path = lambda: "Cisco-IOS-XR-sysmgr-cfg:process-single-crash"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(ProcessSingleCrash, ['crashes', 'minimum_up_time'], name, value)

    def clone_ptr(self):
        self._top_entity = ProcessSingleCrash()
        return self._top_entity

