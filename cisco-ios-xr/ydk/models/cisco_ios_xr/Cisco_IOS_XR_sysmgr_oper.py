""" Cisco_IOS_XR_sysmgr_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR sysmgr package operational data.

This module contains definitions
for the following management objects\:
  system\-process\: Process information

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



class PlacementState(Enum):
    """
    PlacementState (Enum Class)

    Process placement state

    .. data:: place_null = 0

    	Process runs everywhere (ubiquitous)

    .. data:: place_placeable = 1

    	Process runs on node chosen by PlaceD

    .. data:: place_dlrsc_tracker = 2

    	Process runs on dSDRSC only

    .. data:: place_rack_centric = 3

    	Process runs on RP of each rack

    .. data:: place_dsc_tracker = 4

    	Process runs on DSC only

    """

    place_null = Enum.YLeaf(0, "place-null")

    place_placeable = Enum.YLeaf(1, "place-placeable")

    place_dlrsc_tracker = Enum.YLeaf(2, "place-dlrsc-tracker")

    place_rack_centric = Enum.YLeaf(3, "place-rack-centric")

    place_dsc_tracker = Enum.YLeaf(4, "place-dsc-tracker")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
        return meta._meta_table['PlacementState']


class ProcessState(Enum):
    """
    ProcessState (Enum Class)

    Process state

    .. data:: none = 0

    	NONE

    .. data:: run = 1

    	RUN

    .. data:: exited = 2

    	EXITED

    .. data:: hold = 3

    	HOLD

    .. data:: wait = 4

    	WAIT

    .. data:: restart = 5

    	RESTART

    .. data:: initializing = 6

    	INITIALIZING

    .. data:: killed = 7

    	KILLED

    .. data:: queued = 8

    	QUEUED

    .. data:: error = 9

    	ERROR

    .. data:: tuple_set = 10

    	TUPLESET

    .. data:: unknown = 11

    	UNKNOWN

    """

    none = Enum.YLeaf(0, "none")

    run = Enum.YLeaf(1, "run")

    exited = Enum.YLeaf(2, "exited")

    hold = Enum.YLeaf(3, "hold")

    wait = Enum.YLeaf(4, "wait")

    restart = Enum.YLeaf(5, "restart")

    initializing = Enum.YLeaf(6, "initializing")

    killed = Enum.YLeaf(7, "killed")

    queued = Enum.YLeaf(8, "queued")

    error = Enum.YLeaf(9, "error")

    tuple_set = Enum.YLeaf(10, "tuple-set")

    unknown = Enum.YLeaf(11, "unknown")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
        return meta._meta_table['ProcessState']



class SystemProcess(_Entity_):
    """
    Process information
    
    .. attribute:: node_table
    
    	List of nodes
    	**type**\:  :py:class:`NodeTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.SystemProcess.NodeTable>`
    
    	**config**\: False
    
    

    """

    _prefix = 'sysmgr-oper'
    _revision = '2015-11-09'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(SystemProcess, self).__init__()
        self._top_entity = None

        self.yang_name = "system-process"
        self.yang_parent_name = "Cisco-IOS-XR-sysmgr-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("node-table", ("node_table", SystemProcess.NodeTable))])
        self._leafs = OrderedDict()

        self.node_table = SystemProcess.NodeTable()
        self.node_table.parent = self
        self._children_name_map["node_table"] = "node-table"
        self._segment_path = lambda: "Cisco-IOS-XR-sysmgr-oper:system-process"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(SystemProcess, [], name, value)


    class NodeTable(_Entity_):
        """
        List of nodes
        
        .. attribute:: node
        
        	Process information per node
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.SystemProcess.NodeTable.Node>`
        
        	**config**\: False
        
        

        """

        _prefix = 'sysmgr-oper'
        _revision = '2015-11-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(SystemProcess.NodeTable, self).__init__()

            self.yang_name = "node-table"
            self.yang_parent_name = "system-process"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node", ("node", SystemProcess.NodeTable.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "node-table"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysmgr-oper:system-process/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(SystemProcess.NodeTable, [], name, value)


        class Node(_Entity_):
            """
            Process information per node
            
            .. attribute:: node_name  (key)
            
            	The node name
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            	**config**\: False
            
            .. attribute:: name
            
            	Process <WORD> information
            	**type**\:  :py:class:`Name <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.SystemProcess.NodeTable.Node.Name>`
            
            	**config**\: False
            
            .. attribute:: jids
            
            	Process job id information
            	**type**\:  :py:class:`Jids <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.SystemProcess.NodeTable.Node.Jids>`
            
            	**config**\: False
            
            .. attribute:: dynamic
            
            	Process Dynamic information
            	**type**\:  :py:class:`Dynamic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.SystemProcess.NodeTable.Node.Dynamic>`
            
            	**config**\: False
            
            .. attribute:: boot_stalled
            
            	Process Boot Stalled information
            	**type**\:  :py:class:`BootStalled <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.SystemProcess.NodeTable.Node.BootStalled>`
            
            	**config**\: False
            
            .. attribute:: processes
            
            	Process all information
            	**type**\:  :py:class:`Processes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.SystemProcess.NodeTable.Node.Processes>`
            
            	**config**\: False
            
            .. attribute:: startup
            
            	Process Startup information
            	**type**\:  :py:class:`Startup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.SystemProcess.NodeTable.Node.Startup>`
            
            	**config**\: False
            
            .. attribute:: mandatory
            
            	Mandatory Process information
            	**type**\:  :py:class:`Mandatory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.SystemProcess.NodeTable.Node.Mandatory>`
            
            	**config**\: False
            
            .. attribute:: abort
            
            	Process Abort information
            	**type**\:  :py:class:`Abort <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.SystemProcess.NodeTable.Node.Abort>`
            
            	**config**\: False
            
            .. attribute:: failover
            
            	Process Failover information
            	**type**\:  :py:class:`Failover <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.SystemProcess.NodeTable.Node.Failover>`
            
            	**config**\: False
            
            .. attribute:: boot
            
            	Process Boot information
            	**type**\:  :py:class:`Boot <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.SystemProcess.NodeTable.Node.Boot>`
            
            	**config**\: False
            
            .. attribute:: logs
            
            	Process Log information
            	**type**\:  :py:class:`Logs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.SystemProcess.NodeTable.Node.Logs>`
            
            	**config**\: False
            
            .. attribute:: searchpath
            
            	Process Searchpath information
            	**type**\:  :py:class:`Searchpath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.SystemProcess.NodeTable.Node.Searchpath>`
            
            	**config**\: False
            
            

            """

            _prefix = 'sysmgr-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(SystemProcess.NodeTable.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "node-table"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_classes = OrderedDict([("name", ("name", SystemProcess.NodeTable.Node.Name)), ("jids", ("jids", SystemProcess.NodeTable.Node.Jids)), ("dynamic", ("dynamic", SystemProcess.NodeTable.Node.Dynamic)), ("boot-stalled", ("boot_stalled", SystemProcess.NodeTable.Node.BootStalled)), ("processes", ("processes", SystemProcess.NodeTable.Node.Processes)), ("startup", ("startup", SystemProcess.NodeTable.Node.Startup)), ("mandatory", ("mandatory", SystemProcess.NodeTable.Node.Mandatory)), ("abort", ("abort", SystemProcess.NodeTable.Node.Abort)), ("failover", ("failover", SystemProcess.NodeTable.Node.Failover)), ("boot", ("boot", SystemProcess.NodeTable.Node.Boot)), ("logs", ("logs", SystemProcess.NodeTable.Node.Logs)), ("searchpath", ("searchpath", SystemProcess.NodeTable.Node.Searchpath))])
                self._leafs = OrderedDict([
                    ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                ])
                self.node_name = None

                self.name = SystemProcess.NodeTable.Node.Name()
                self.name.parent = self
                self._children_name_map["name"] = "name"

                self.jids = SystemProcess.NodeTable.Node.Jids()
                self.jids.parent = self
                self._children_name_map["jids"] = "jids"

                self.dynamic = SystemProcess.NodeTable.Node.Dynamic()
                self.dynamic.parent = self
                self._children_name_map["dynamic"] = "dynamic"

                self.boot_stalled = SystemProcess.NodeTable.Node.BootStalled()
                self.boot_stalled.parent = self
                self._children_name_map["boot_stalled"] = "boot-stalled"

                self.processes = SystemProcess.NodeTable.Node.Processes()
                self.processes.parent = self
                self._children_name_map["processes"] = "processes"

                self.startup = SystemProcess.NodeTable.Node.Startup()
                self.startup.parent = self
                self._children_name_map["startup"] = "startup"

                self.mandatory = SystemProcess.NodeTable.Node.Mandatory()
                self.mandatory.parent = self
                self._children_name_map["mandatory"] = "mandatory"

                self.abort = SystemProcess.NodeTable.Node.Abort()
                self.abort.parent = self
                self._children_name_map["abort"] = "abort"

                self.failover = SystemProcess.NodeTable.Node.Failover()
                self.failover.parent = self
                self._children_name_map["failover"] = "failover"

                self.boot = SystemProcess.NodeTable.Node.Boot()
                self.boot.parent = self
                self._children_name_map["boot"] = "boot"

                self.logs = SystemProcess.NodeTable.Node.Logs()
                self.logs.parent = self
                self._children_name_map["logs"] = "logs"

                self.searchpath = SystemProcess.NodeTable.Node.Searchpath()
                self.searchpath.parent = self
                self._children_name_map["searchpath"] = "searchpath"
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysmgr-oper:system-process/node-table/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(SystemProcess.NodeTable.Node, ['node_name'], name, value)


            class Name(_Entity_):
                """
                Process <WORD> information
                
                .. attribute:: process_name_run_infos
                
                	Process <WORD> information
                	**type**\:  :py:class:`ProcessNameRunInfos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.SystemProcess.NodeTable.Node.Name.ProcessNameRunInfos>`
                
                	**config**\: False
                
                .. attribute:: process_name_infos
                
                	Process <WORD> information
                	**type**\:  :py:class:`ProcessNameInfos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.SystemProcess.NodeTable.Node.Name.ProcessNameInfos>`
                
                	**config**\: False
                
                .. attribute:: process_name_run_details
                
                	Process <WORD> information
                	**type**\:  :py:class:`ProcessNameRunDetails <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.SystemProcess.NodeTable.Node.Name.ProcessNameRunDetails>`
                
                	**config**\: False
                
                .. attribute:: process_name_runverboses
                
                	Process <WORD> information
                	**type**\:  :py:class:`ProcessNameRunverboses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.SystemProcess.NodeTable.Node.Name.ProcessNameRunverboses>`
                
                	**config**\: False
                
                .. attribute:: process_name_details
                
                	Process <WORD> information
                	**type**\:  :py:class:`ProcessNameDetails <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.SystemProcess.NodeTable.Node.Name.ProcessNameDetails>`
                
                	**config**\: False
                
                .. attribute:: process_name_verboses
                
                	Process <WORD> information
                	**type**\:  :py:class:`ProcessNameVerboses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.SystemProcess.NodeTable.Node.Name.ProcessNameVerboses>`
                
                	**config**\: False
                
                

                """

                _prefix = 'sysmgr-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(SystemProcess.NodeTable.Node.Name, self).__init__()

                    self.yang_name = "name"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("process-name-run-infos", ("process_name_run_infos", SystemProcess.NodeTable.Node.Name.ProcessNameRunInfos)), ("process-name-infos", ("process_name_infos", SystemProcess.NodeTable.Node.Name.ProcessNameInfos)), ("process-name-run-details", ("process_name_run_details", SystemProcess.NodeTable.Node.Name.ProcessNameRunDetails)), ("process-name-runverboses", ("process_name_runverboses", SystemProcess.NodeTable.Node.Name.ProcessNameRunverboses)), ("process-name-details", ("process_name_details", SystemProcess.NodeTable.Node.Name.ProcessNameDetails)), ("process-name-verboses", ("process_name_verboses", SystemProcess.NodeTable.Node.Name.ProcessNameVerboses))])
                    self._leafs = OrderedDict()

                    self.process_name_run_infos = SystemProcess.NodeTable.Node.Name.ProcessNameRunInfos()
                    self.process_name_run_infos.parent = self
                    self._children_name_map["process_name_run_infos"] = "process-name-run-infos"

                    self.process_name_infos = SystemProcess.NodeTable.Node.Name.ProcessNameInfos()
                    self.process_name_infos.parent = self
                    self._children_name_map["process_name_infos"] = "process-name-infos"

                    self.process_name_run_details = SystemProcess.NodeTable.Node.Name.ProcessNameRunDetails()
                    self.process_name_run_details.parent = self
                    self._children_name_map["process_name_run_details"] = "process-name-run-details"

                    self.process_name_runverboses = SystemProcess.NodeTable.Node.Name.ProcessNameRunverboses()
                    self.process_name_runverboses.parent = self
                    self._children_name_map["process_name_runverboses"] = "process-name-runverboses"

                    self.process_name_details = SystemProcess.NodeTable.Node.Name.ProcessNameDetails()
                    self.process_name_details.parent = self
                    self._children_name_map["process_name_details"] = "process-name-details"

                    self.process_name_verboses = SystemProcess.NodeTable.Node.Name.ProcessNameVerboses()
                    self.process_name_verboses.parent = self
                    self._children_name_map["process_name_verboses"] = "process-name-verboses"
                    self._segment_path = lambda: "name"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(SystemProcess.NodeTable.Node.Name, [], name, value)


                class ProcessNameRunInfos(_Entity_):
                    """
                    Process <WORD> information
                    
                    .. attribute:: process_name_run_info
                    
                    	Process <WORD> run information
                    	**type**\: list of  		 :py:class:`ProcessNameRunInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.SystemProcess.NodeTable.Node.Name.ProcessNameRunInfos.ProcessNameRunInfo>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'sysmgr-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(SystemProcess.NodeTable.Node.Name.ProcessNameRunInfos, self).__init__()

                        self.yang_name = "process-name-run-infos"
                        self.yang_parent_name = "name"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("process-name-run-info", ("process_name_run_info", SystemProcess.NodeTable.Node.Name.ProcessNameRunInfos.ProcessNameRunInfo))])
                        self._leafs = OrderedDict()

                        self.process_name_run_info = YList(self)
                        self._segment_path = lambda: "process-name-run-infos"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(SystemProcess.NodeTable.Node.Name.ProcessNameRunInfos, [], name, value)


                    class ProcessNameRunInfo(_Entity_):
                        """
                        Process <WORD> run information
                        
                        .. attribute:: proc_name  (key)
                        
                        	Process Name
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        	**config**\: False
                        
                        .. attribute:: proc_cpu_time
                        
                        	Proces cpu time
                        	**type**\:  :py:class:`ProcCpuTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.SystemProcess.NodeTable.Node.Name.ProcessNameRunInfos.ProcessNameRunInfo.ProcCpuTime>`
                        
                        	**config**\: False
                        
                        .. attribute:: job_id_xr
                        
                        	Job ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: process_id
                        
                        	PID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: process_name
                        
                        	Process name
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: executable
                        
                        	Executable name or path
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: active_path
                        
                        	Active Path
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: instance_id
                        
                        	Instance ID
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        .. attribute:: args
                        
                        	Args
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: version_id
                        
                        	Version ID
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: respawn
                        
                        	Respawn on/off
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: respawn_count
                        
                        	Respawn Count
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        .. attribute:: last_started
                        
                        	Last Started
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: process_state
                        
                        	Process State
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: last_exit_status
                        
                        	Last Exit status
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        .. attribute:: last_exit_reason
                        
                        	Last Exit due to
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: package_state
                        
                        	Package State
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: started_on_config
                        
                        	Started on Config
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: feature_name
                        
                        	Feature Name
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: tag
                        
                        	Tag
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: group
                        
                        	Process Group
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: core
                        
                        	Core
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: max_core
                        
                        	Max core
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        .. attribute:: level
                        
                        	Level
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: mandatory
                        
                        	Is mandatory?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: maint_mode_proc
                        
                        	Is admin mode process?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: placement_state
                        
                        	Placement State
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: start_up_path
                        
                        	Startup Path
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: memory_limit
                        
                        	Memory Limit
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: ready
                        
                        	Elapsed Ready
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: available
                        
                        	Elapsed Available
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: registered_item
                        
                        	Registered Items
                        	**type**\: list of  		 :py:class:`RegisteredItem <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.SystemProcess.NodeTable.Node.Name.ProcessNameRunInfos.ProcessNameRunInfo.RegisteredItem>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'sysmgr-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(SystemProcess.NodeTable.Node.Name.ProcessNameRunInfos.ProcessNameRunInfo, self).__init__()

                            self.yang_name = "process-name-run-info"
                            self.yang_parent_name = "process-name-run-infos"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['proc_name']
                            self._child_classes = OrderedDict([("proc-cpu-time", ("proc_cpu_time", SystemProcess.NodeTable.Node.Name.ProcessNameRunInfos.ProcessNameRunInfo.ProcCpuTime)), ("registered-item", ("registered_item", SystemProcess.NodeTable.Node.Name.ProcessNameRunInfos.ProcessNameRunInfo.RegisteredItem))])
                            self._leafs = OrderedDict([
                                ('proc_name', (YLeaf(YType.str, 'proc-name'), ['str'])),
                                ('job_id_xr', (YLeaf(YType.uint32, 'job-id-xr'), ['int'])),
                                ('process_id', (YLeaf(YType.uint32, 'process-id'), ['int'])),
                                ('process_name', (YLeaf(YType.str, 'process-name'), ['str'])),
                                ('executable', (YLeaf(YType.str, 'executable'), ['str'])),
                                ('active_path', (YLeaf(YType.str, 'active-path'), ['str'])),
                                ('instance_id', (YLeaf(YType.int32, 'instance-id'), ['int'])),
                                ('args', (YLeaf(YType.str, 'args'), ['str'])),
                                ('version_id', (YLeaf(YType.str, 'version-id'), ['str'])),
                                ('respawn', (YLeaf(YType.str, 'respawn'), ['str'])),
                                ('respawn_count', (YLeaf(YType.int32, 'respawn-count'), ['int'])),
                                ('last_started', (YLeaf(YType.str, 'last-started'), ['str'])),
                                ('process_state', (YLeaf(YType.str, 'process-state'), ['str'])),
                                ('last_exit_status', (YLeaf(YType.int32, 'last-exit-status'), ['int'])),
                                ('last_exit_reason', (YLeaf(YType.str, 'last-exit-reason'), ['str'])),
                                ('package_state', (YLeaf(YType.str, 'package-state'), ['str'])),
                                ('started_on_config', (YLeaf(YType.str, 'started-on-config'), ['str'])),
                                ('feature_name', (YLeaf(YType.str, 'feature-name'), ['str'])),
                                ('tag', (YLeaf(YType.str, 'tag'), ['str'])),
                                ('group', (YLeaf(YType.str, 'group'), ['str'])),
                                ('core', (YLeaf(YType.str, 'core'), ['str'])),
                                ('max_core', (YLeaf(YType.int32, 'max-core'), ['int'])),
                                ('level', (YLeaf(YType.str, 'level'), ['str'])),
                                ('mandatory', (YLeaf(YType.boolean, 'mandatory'), ['bool'])),
                                ('maint_mode_proc', (YLeaf(YType.boolean, 'maint-mode-proc'), ['bool'])),
                                ('placement_state', (YLeaf(YType.str, 'placement-state'), ['str'])),
                                ('start_up_path', (YLeaf(YType.str, 'start-up-path'), ['str'])),
                                ('memory_limit', (YLeaf(YType.uint32, 'memory-limit'), ['int'])),
                                ('ready', (YLeaf(YType.str, 'ready'), ['str'])),
                                ('available', (YLeaf(YType.str, 'available'), ['str'])),
                            ])
                            self.proc_name = None
                            self.job_id_xr = None
                            self.process_id = None
                            self.process_name = None
                            self.executable = None
                            self.active_path = None
                            self.instance_id = None
                            self.args = None
                            self.version_id = None
                            self.respawn = None
                            self.respawn_count = None
                            self.last_started = None
                            self.process_state = None
                            self.last_exit_status = None
                            self.last_exit_reason = None
                            self.package_state = None
                            self.started_on_config = None
                            self.feature_name = None
                            self.tag = None
                            self.group = None
                            self.core = None
                            self.max_core = None
                            self.level = None
                            self.mandatory = None
                            self.maint_mode_proc = None
                            self.placement_state = None
                            self.start_up_path = None
                            self.memory_limit = None
                            self.ready = None
                            self.available = None

                            self.proc_cpu_time = SystemProcess.NodeTable.Node.Name.ProcessNameRunInfos.ProcessNameRunInfo.ProcCpuTime()
                            self.proc_cpu_time.parent = self
                            self._children_name_map["proc_cpu_time"] = "proc-cpu-time"

                            self.registered_item = YList(self)
                            self._segment_path = lambda: "process-name-run-info" + "[proc-name='" + str(self.proc_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(SystemProcess.NodeTable.Node.Name.ProcessNameRunInfos.ProcessNameRunInfo, ['proc_name', 'job_id_xr', 'process_id', 'process_name', 'executable', 'active_path', 'instance_id', 'args', 'version_id', 'respawn', 'respawn_count', 'last_started', 'process_state', 'last_exit_status', 'last_exit_reason', 'package_state', 'started_on_config', 'feature_name', 'tag', 'group', 'core', 'max_core', 'level', 'mandatory', 'maint_mode_proc', 'placement_state', 'start_up_path', 'memory_limit', 'ready', 'available'], name, value)


                        class ProcCpuTime(_Entity_):
                            """
                            Proces cpu time
                            
                            .. attribute:: user
                            
                            	User time
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: system
                            
                            	Kernel time
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: total
                            
                            	Total time
                            	**type**\: str
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'sysmgr-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(SystemProcess.NodeTable.Node.Name.ProcessNameRunInfos.ProcessNameRunInfo.ProcCpuTime, self).__init__()

                                self.yang_name = "proc-cpu-time"
                                self.yang_parent_name = "process-name-run-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('user', (YLeaf(YType.str, 'user'), ['str'])),
                                    ('system', (YLeaf(YType.str, 'system'), ['str'])),
                                    ('total', (YLeaf(YType.str, 'total'), ['str'])),
                                ])
                                self.user = None
                                self.system = None
                                self.total = None
                                self._segment_path = lambda: "proc-cpu-time"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(SystemProcess.NodeTable.Node.Name.ProcessNameRunInfos.ProcessNameRunInfo.ProcCpuTime, ['user', 'system', 'total'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
                                return meta._meta_table['SystemProcess.NodeTable.Node.Name.ProcessNameRunInfos.ProcessNameRunInfo.ProcCpuTime']['meta_info']


                        class RegisteredItem(_Entity_):
                            """
                            Registered Items
                            
                            .. attribute:: tuple
                            
                            	Tuple
                            	**type**\: str
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'sysmgr-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(SystemProcess.NodeTable.Node.Name.ProcessNameRunInfos.ProcessNameRunInfo.RegisteredItem, self).__init__()

                                self.yang_name = "registered-item"
                                self.yang_parent_name = "process-name-run-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('tuple', (YLeaf(YType.str, 'tuple'), ['str'])),
                                ])
                                self.tuple = None
                                self._segment_path = lambda: "registered-item"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(SystemProcess.NodeTable.Node.Name.ProcessNameRunInfos.ProcessNameRunInfo.RegisteredItem, ['tuple'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
                                return meta._meta_table['SystemProcess.NodeTable.Node.Name.ProcessNameRunInfos.ProcessNameRunInfo.RegisteredItem']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
                            return meta._meta_table['SystemProcess.NodeTable.Node.Name.ProcessNameRunInfos.ProcessNameRunInfo']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
                        return meta._meta_table['SystemProcess.NodeTable.Node.Name.ProcessNameRunInfos']['meta_info']


                class ProcessNameInfos(_Entity_):
                    """
                    Process <WORD> information
                    
                    .. attribute:: process_name_info
                    
                    	Process <WORD> information
                    	**type**\: list of  		 :py:class:`ProcessNameInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.SystemProcess.NodeTable.Node.Name.ProcessNameInfos.ProcessNameInfo>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'sysmgr-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(SystemProcess.NodeTable.Node.Name.ProcessNameInfos, self).__init__()

                        self.yang_name = "process-name-infos"
                        self.yang_parent_name = "name"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("process-name-info", ("process_name_info", SystemProcess.NodeTable.Node.Name.ProcessNameInfos.ProcessNameInfo))])
                        self._leafs = OrderedDict()

                        self.process_name_info = YList(self)
                        self._segment_path = lambda: "process-name-infos"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(SystemProcess.NodeTable.Node.Name.ProcessNameInfos, [], name, value)


                    class ProcessNameInfo(_Entity_):
                        """
                        Process <WORD> information
                        
                        .. attribute:: proc_name  (key)
                        
                        	Process Name
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        	**config**\: False
                        
                        .. attribute:: proc_cpu_time
                        
                        	Proces cpu time
                        	**type**\:  :py:class:`ProcCpuTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.SystemProcess.NodeTable.Node.Name.ProcessNameInfos.ProcessNameInfo.ProcCpuTime>`
                        
                        	**config**\: False
                        
                        .. attribute:: job_id_xr
                        
                        	Job ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: process_id
                        
                        	PID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: process_name
                        
                        	Process name
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: executable
                        
                        	Executable name or path
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: active_path
                        
                        	Active Path
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: instance_id
                        
                        	Instance ID
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        .. attribute:: args
                        
                        	Args
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: version_id
                        
                        	Version ID
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: respawn
                        
                        	Respawn on/off
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: respawn_count
                        
                        	Respawn Count
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        .. attribute:: last_started
                        
                        	Last Started
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: process_state
                        
                        	Process State
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: last_exit_status
                        
                        	Last Exit status
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        .. attribute:: last_exit_reason
                        
                        	Last Exit due to
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: package_state
                        
                        	Package State
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: started_on_config
                        
                        	Started on Config
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: feature_name
                        
                        	Feature Name
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: tag
                        
                        	Tag
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: group
                        
                        	Process Group
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: core
                        
                        	Core
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: max_core
                        
                        	Max core
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        .. attribute:: level
                        
                        	Level
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: mandatory
                        
                        	Is mandatory?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: maint_mode_proc
                        
                        	Is admin mode process?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: placement_state
                        
                        	Placement State
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: start_up_path
                        
                        	Startup Path
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: memory_limit
                        
                        	Memory Limit
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: ready
                        
                        	Elapsed Ready
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: available
                        
                        	Elapsed Available
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: registered_item
                        
                        	Registered Items
                        	**type**\: list of  		 :py:class:`RegisteredItem <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.SystemProcess.NodeTable.Node.Name.ProcessNameInfos.ProcessNameInfo.RegisteredItem>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'sysmgr-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(SystemProcess.NodeTable.Node.Name.ProcessNameInfos.ProcessNameInfo, self).__init__()

                            self.yang_name = "process-name-info"
                            self.yang_parent_name = "process-name-infos"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['proc_name']
                            self._child_classes = OrderedDict([("proc-cpu-time", ("proc_cpu_time", SystemProcess.NodeTable.Node.Name.ProcessNameInfos.ProcessNameInfo.ProcCpuTime)), ("registered-item", ("registered_item", SystemProcess.NodeTable.Node.Name.ProcessNameInfos.ProcessNameInfo.RegisteredItem))])
                            self._leafs = OrderedDict([
                                ('proc_name', (YLeaf(YType.str, 'proc-name'), ['str'])),
                                ('job_id_xr', (YLeaf(YType.uint32, 'job-id-xr'), ['int'])),
                                ('process_id', (YLeaf(YType.uint32, 'process-id'), ['int'])),
                                ('process_name', (YLeaf(YType.str, 'process-name'), ['str'])),
                                ('executable', (YLeaf(YType.str, 'executable'), ['str'])),
                                ('active_path', (YLeaf(YType.str, 'active-path'), ['str'])),
                                ('instance_id', (YLeaf(YType.int32, 'instance-id'), ['int'])),
                                ('args', (YLeaf(YType.str, 'args'), ['str'])),
                                ('version_id', (YLeaf(YType.str, 'version-id'), ['str'])),
                                ('respawn', (YLeaf(YType.str, 'respawn'), ['str'])),
                                ('respawn_count', (YLeaf(YType.int32, 'respawn-count'), ['int'])),
                                ('last_started', (YLeaf(YType.str, 'last-started'), ['str'])),
                                ('process_state', (YLeaf(YType.str, 'process-state'), ['str'])),
                                ('last_exit_status', (YLeaf(YType.int32, 'last-exit-status'), ['int'])),
                                ('last_exit_reason', (YLeaf(YType.str, 'last-exit-reason'), ['str'])),
                                ('package_state', (YLeaf(YType.str, 'package-state'), ['str'])),
                                ('started_on_config', (YLeaf(YType.str, 'started-on-config'), ['str'])),
                                ('feature_name', (YLeaf(YType.str, 'feature-name'), ['str'])),
                                ('tag', (YLeaf(YType.str, 'tag'), ['str'])),
                                ('group', (YLeaf(YType.str, 'group'), ['str'])),
                                ('core', (YLeaf(YType.str, 'core'), ['str'])),
                                ('max_core', (YLeaf(YType.int32, 'max-core'), ['int'])),
                                ('level', (YLeaf(YType.str, 'level'), ['str'])),
                                ('mandatory', (YLeaf(YType.boolean, 'mandatory'), ['bool'])),
                                ('maint_mode_proc', (YLeaf(YType.boolean, 'maint-mode-proc'), ['bool'])),
                                ('placement_state', (YLeaf(YType.str, 'placement-state'), ['str'])),
                                ('start_up_path', (YLeaf(YType.str, 'start-up-path'), ['str'])),
                                ('memory_limit', (YLeaf(YType.uint32, 'memory-limit'), ['int'])),
                                ('ready', (YLeaf(YType.str, 'ready'), ['str'])),
                                ('available', (YLeaf(YType.str, 'available'), ['str'])),
                            ])
                            self.proc_name = None
                            self.job_id_xr = None
                            self.process_id = None
                            self.process_name = None
                            self.executable = None
                            self.active_path = None
                            self.instance_id = None
                            self.args = None
                            self.version_id = None
                            self.respawn = None
                            self.respawn_count = None
                            self.last_started = None
                            self.process_state = None
                            self.last_exit_status = None
                            self.last_exit_reason = None
                            self.package_state = None
                            self.started_on_config = None
                            self.feature_name = None
                            self.tag = None
                            self.group = None
                            self.core = None
                            self.max_core = None
                            self.level = None
                            self.mandatory = None
                            self.maint_mode_proc = None
                            self.placement_state = None
                            self.start_up_path = None
                            self.memory_limit = None
                            self.ready = None
                            self.available = None

                            self.proc_cpu_time = SystemProcess.NodeTable.Node.Name.ProcessNameInfos.ProcessNameInfo.ProcCpuTime()
                            self.proc_cpu_time.parent = self
                            self._children_name_map["proc_cpu_time"] = "proc-cpu-time"

                            self.registered_item = YList(self)
                            self._segment_path = lambda: "process-name-info" + "[proc-name='" + str(self.proc_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(SystemProcess.NodeTable.Node.Name.ProcessNameInfos.ProcessNameInfo, ['proc_name', 'job_id_xr', 'process_id', 'process_name', 'executable', 'active_path', 'instance_id', 'args', 'version_id', 'respawn', 'respawn_count', 'last_started', 'process_state', 'last_exit_status', 'last_exit_reason', 'package_state', 'started_on_config', 'feature_name', 'tag', 'group', 'core', 'max_core', 'level', 'mandatory', 'maint_mode_proc', 'placement_state', 'start_up_path', 'memory_limit', 'ready', 'available'], name, value)


                        class ProcCpuTime(_Entity_):
                            """
                            Proces cpu time
                            
                            .. attribute:: user
                            
                            	User time
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: system
                            
                            	Kernel time
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: total
                            
                            	Total time
                            	**type**\: str
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'sysmgr-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(SystemProcess.NodeTable.Node.Name.ProcessNameInfos.ProcessNameInfo.ProcCpuTime, self).__init__()

                                self.yang_name = "proc-cpu-time"
                                self.yang_parent_name = "process-name-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('user', (YLeaf(YType.str, 'user'), ['str'])),
                                    ('system', (YLeaf(YType.str, 'system'), ['str'])),
                                    ('total', (YLeaf(YType.str, 'total'), ['str'])),
                                ])
                                self.user = None
                                self.system = None
                                self.total = None
                                self._segment_path = lambda: "proc-cpu-time"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(SystemProcess.NodeTable.Node.Name.ProcessNameInfos.ProcessNameInfo.ProcCpuTime, ['user', 'system', 'total'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
                                return meta._meta_table['SystemProcess.NodeTable.Node.Name.ProcessNameInfos.ProcessNameInfo.ProcCpuTime']['meta_info']


                        class RegisteredItem(_Entity_):
                            """
                            Registered Items
                            
                            .. attribute:: tuple
                            
                            	Tuple
                            	**type**\: str
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'sysmgr-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(SystemProcess.NodeTable.Node.Name.ProcessNameInfos.ProcessNameInfo.RegisteredItem, self).__init__()

                                self.yang_name = "registered-item"
                                self.yang_parent_name = "process-name-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('tuple', (YLeaf(YType.str, 'tuple'), ['str'])),
                                ])
                                self.tuple = None
                                self._segment_path = lambda: "registered-item"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(SystemProcess.NodeTable.Node.Name.ProcessNameInfos.ProcessNameInfo.RegisteredItem, ['tuple'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
                                return meta._meta_table['SystemProcess.NodeTable.Node.Name.ProcessNameInfos.ProcessNameInfo.RegisteredItem']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
                            return meta._meta_table['SystemProcess.NodeTable.Node.Name.ProcessNameInfos.ProcessNameInfo']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
                        return meta._meta_table['SystemProcess.NodeTable.Node.Name.ProcessNameInfos']['meta_info']


                class ProcessNameRunDetails(_Entity_):
                    """
                    Process <WORD> information
                    
                    .. attribute:: process_name_run_detail
                    
                    	Process <WORD> run detail information
                    	**type**\: list of  		 :py:class:`ProcessNameRunDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.SystemProcess.NodeTable.Node.Name.ProcessNameRunDetails.ProcessNameRunDetail>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'sysmgr-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(SystemProcess.NodeTable.Node.Name.ProcessNameRunDetails, self).__init__()

                        self.yang_name = "process-name-run-details"
                        self.yang_parent_name = "name"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("process-name-run-detail", ("process_name_run_detail", SystemProcess.NodeTable.Node.Name.ProcessNameRunDetails.ProcessNameRunDetail))])
                        self._leafs = OrderedDict()

                        self.process_name_run_detail = YList(self)
                        self._segment_path = lambda: "process-name-run-details"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(SystemProcess.NodeTable.Node.Name.ProcessNameRunDetails, [], name, value)


                    class ProcessNameRunDetail(_Entity_):
                        """
                        Process <WORD> run detail information
                        
                        .. attribute:: proc_name  (key)
                        
                        	Process Name
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        	**config**\: False
                        
                        .. attribute:: basic_info
                        
                        	Process Basic Info
                        	**type**\:  :py:class:`BasicInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.SystemProcess.NodeTable.Node.Name.ProcessNameRunDetails.ProcessNameRunDetail.BasicInfo>`
                        
                        	**config**\: False
                        
                        .. attribute:: detail_info
                        
                        	Process Detail Info
                        	**type**\:  :py:class:`DetailInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.SystemProcess.NodeTable.Node.Name.ProcessNameRunDetails.ProcessNameRunDetail.DetailInfo>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'sysmgr-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(SystemProcess.NodeTable.Node.Name.ProcessNameRunDetails.ProcessNameRunDetail, self).__init__()

                            self.yang_name = "process-name-run-detail"
                            self.yang_parent_name = "process-name-run-details"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['proc_name']
                            self._child_classes = OrderedDict([("basic-info", ("basic_info", SystemProcess.NodeTable.Node.Name.ProcessNameRunDetails.ProcessNameRunDetail.BasicInfo)), ("detail-info", ("detail_info", SystemProcess.NodeTable.Node.Name.ProcessNameRunDetails.ProcessNameRunDetail.DetailInfo))])
                            self._leafs = OrderedDict([
                                ('proc_name', (YLeaf(YType.str, 'proc-name'), ['str'])),
                            ])
                            self.proc_name = None

                            self.basic_info = SystemProcess.NodeTable.Node.Name.ProcessNameRunDetails.ProcessNameRunDetail.BasicInfo()
                            self.basic_info.parent = self
                            self._children_name_map["basic_info"] = "basic-info"

                            self.detail_info = SystemProcess.NodeTable.Node.Name.ProcessNameRunDetails.ProcessNameRunDetail.DetailInfo()
                            self.detail_info.parent = self
                            self._children_name_map["detail_info"] = "detail-info"
                            self._segment_path = lambda: "process-name-run-detail" + "[proc-name='" + str(self.proc_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(SystemProcess.NodeTable.Node.Name.ProcessNameRunDetails.ProcessNameRunDetail, ['proc_name'], name, value)


                        class BasicInfo(_Entity_):
                            """
                            Process Basic Info
                            
                            .. attribute:: proc_cpu_time
                            
                            	Proces cpu time
                            	**type**\:  :py:class:`ProcCpuTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.SystemProcess.NodeTable.Node.Name.ProcessNameRunDetails.ProcessNameRunDetail.BasicInfo.ProcCpuTime>`
                            
                            	**config**\: False
                            
                            .. attribute:: job_id_xr
                            
                            	Job ID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: process_id
                            
                            	PID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: process_name
                            
                            	Process name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: executable
                            
                            	Executable name or path
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: active_path
                            
                            	Active Path
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: instance_id
                            
                            	Instance ID
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: args
                            
                            	Args
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: version_id
                            
                            	Version ID
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: respawn
                            
                            	Respawn on/off
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: respawn_count
                            
                            	Respawn Count
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: last_started
                            
                            	Last Started
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: process_state
                            
                            	Process State
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: last_exit_status
                            
                            	Last Exit status
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: last_exit_reason
                            
                            	Last Exit due to
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: package_state
                            
                            	Package State
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: started_on_config
                            
                            	Started on Config
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: feature_name
                            
                            	Feature Name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: tag
                            
                            	Tag
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: group
                            
                            	Process Group
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: core
                            
                            	Core
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: max_core
                            
                            	Max core
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: level
                            
                            	Level
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: mandatory
                            
                            	Is mandatory?
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: maint_mode_proc
                            
                            	Is admin mode process?
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: placement_state
                            
                            	Placement State
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: start_up_path
                            
                            	Startup Path
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: memory_limit
                            
                            	Memory Limit
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: ready
                            
                            	Elapsed Ready
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: available
                            
                            	Elapsed Available
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: registered_item
                            
                            	Registered Items
                            	**type**\: list of  		 :py:class:`RegisteredItem <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.SystemProcess.NodeTable.Node.Name.ProcessNameRunDetails.ProcessNameRunDetail.BasicInfo.RegisteredItem>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'sysmgr-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(SystemProcess.NodeTable.Node.Name.ProcessNameRunDetails.ProcessNameRunDetail.BasicInfo, self).__init__()

                                self.yang_name = "basic-info"
                                self.yang_parent_name = "process-name-run-detail"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("proc-cpu-time", ("proc_cpu_time", SystemProcess.NodeTable.Node.Name.ProcessNameRunDetails.ProcessNameRunDetail.BasicInfo.ProcCpuTime)), ("registered-item", ("registered_item", SystemProcess.NodeTable.Node.Name.ProcessNameRunDetails.ProcessNameRunDetail.BasicInfo.RegisteredItem))])
                                self._leafs = OrderedDict([
                                    ('job_id_xr', (YLeaf(YType.uint32, 'job-id-xr'), ['int'])),
                                    ('process_id', (YLeaf(YType.uint32, 'process-id'), ['int'])),
                                    ('process_name', (YLeaf(YType.str, 'process-name'), ['str'])),
                                    ('executable', (YLeaf(YType.str, 'executable'), ['str'])),
                                    ('active_path', (YLeaf(YType.str, 'active-path'), ['str'])),
                                    ('instance_id', (YLeaf(YType.int32, 'instance-id'), ['int'])),
                                    ('args', (YLeaf(YType.str, 'args'), ['str'])),
                                    ('version_id', (YLeaf(YType.str, 'version-id'), ['str'])),
                                    ('respawn', (YLeaf(YType.str, 'respawn'), ['str'])),
                                    ('respawn_count', (YLeaf(YType.int32, 'respawn-count'), ['int'])),
                                    ('last_started', (YLeaf(YType.str, 'last-started'), ['str'])),
                                    ('process_state', (YLeaf(YType.str, 'process-state'), ['str'])),
                                    ('last_exit_status', (YLeaf(YType.int32, 'last-exit-status'), ['int'])),
                                    ('last_exit_reason', (YLeaf(YType.str, 'last-exit-reason'), ['str'])),
                                    ('package_state', (YLeaf(YType.str, 'package-state'), ['str'])),
                                    ('started_on_config', (YLeaf(YType.str, 'started-on-config'), ['str'])),
                                    ('feature_name', (YLeaf(YType.str, 'feature-name'), ['str'])),
                                    ('tag', (YLeaf(YType.str, 'tag'), ['str'])),
                                    ('group', (YLeaf(YType.str, 'group'), ['str'])),
                                    ('core', (YLeaf(YType.str, 'core'), ['str'])),
                                    ('max_core', (YLeaf(YType.int32, 'max-core'), ['int'])),
                                    ('level', (YLeaf(YType.str, 'level'), ['str'])),
                                    ('mandatory', (YLeaf(YType.boolean, 'mandatory'), ['bool'])),
                                    ('maint_mode_proc', (YLeaf(YType.boolean, 'maint-mode-proc'), ['bool'])),
                                    ('placement_state', (YLeaf(YType.str, 'placement-state'), ['str'])),
                                    ('start_up_path', (YLeaf(YType.str, 'start-up-path'), ['str'])),
                                    ('memory_limit', (YLeaf(YType.uint32, 'memory-limit'), ['int'])),
                                    ('ready', (YLeaf(YType.str, 'ready'), ['str'])),
                                    ('available', (YLeaf(YType.str, 'available'), ['str'])),
                                ])
                                self.job_id_xr = None
                                self.process_id = None
                                self.process_name = None
                                self.executable = None
                                self.active_path = None
                                self.instance_id = None
                                self.args = None
                                self.version_id = None
                                self.respawn = None
                                self.respawn_count = None
                                self.last_started = None
                                self.process_state = None
                                self.last_exit_status = None
                                self.last_exit_reason = None
                                self.package_state = None
                                self.started_on_config = None
                                self.feature_name = None
                                self.tag = None
                                self.group = None
                                self.core = None
                                self.max_core = None
                                self.level = None
                                self.mandatory = None
                                self.maint_mode_proc = None
                                self.placement_state = None
                                self.start_up_path = None
                                self.memory_limit = None
                                self.ready = None
                                self.available = None

                                self.proc_cpu_time = SystemProcess.NodeTable.Node.Name.ProcessNameRunDetails.ProcessNameRunDetail.BasicInfo.ProcCpuTime()
                                self.proc_cpu_time.parent = self
                                self._children_name_map["proc_cpu_time"] = "proc-cpu-time"

                                self.registered_item = YList(self)
                                self._segment_path = lambda: "basic-info"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(SystemProcess.NodeTable.Node.Name.ProcessNameRunDetails.ProcessNameRunDetail.BasicInfo, ['job_id_xr', 'process_id', 'process_name', 'executable', 'active_path', 'instance_id', 'args', 'version_id', 'respawn', 'respawn_count', 'last_started', 'process_state', 'last_exit_status', 'last_exit_reason', 'package_state', 'started_on_config', 'feature_name', 'tag', 'group', 'core', 'max_core', 'level', 'mandatory', 'maint_mode_proc', 'placement_state', 'start_up_path', 'memory_limit', 'ready', 'available'], name, value)


                            class ProcCpuTime(_Entity_):
                                """
                                Proces cpu time
                                
                                .. attribute:: user
                                
                                	User time
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: system
                                
                                	Kernel time
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: total
                                
                                	Total time
                                	**type**\: str
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'sysmgr-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(SystemProcess.NodeTable.Node.Name.ProcessNameRunDetails.ProcessNameRunDetail.BasicInfo.ProcCpuTime, self).__init__()

                                    self.yang_name = "proc-cpu-time"
                                    self.yang_parent_name = "basic-info"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('user', (YLeaf(YType.str, 'user'), ['str'])),
                                        ('system', (YLeaf(YType.str, 'system'), ['str'])),
                                        ('total', (YLeaf(YType.str, 'total'), ['str'])),
                                    ])
                                    self.user = None
                                    self.system = None
                                    self.total = None
                                    self._segment_path = lambda: "proc-cpu-time"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(SystemProcess.NodeTable.Node.Name.ProcessNameRunDetails.ProcessNameRunDetail.BasicInfo.ProcCpuTime, ['user', 'system', 'total'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
                                    return meta._meta_table['SystemProcess.NodeTable.Node.Name.ProcessNameRunDetails.ProcessNameRunDetail.BasicInfo.ProcCpuTime']['meta_info']


                            class RegisteredItem(_Entity_):
                                """
                                Registered Items
                                
                                .. attribute:: tuple
                                
                                	Tuple
                                	**type**\: str
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'sysmgr-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(SystemProcess.NodeTable.Node.Name.ProcessNameRunDetails.ProcessNameRunDetail.BasicInfo.RegisteredItem, self).__init__()

                                    self.yang_name = "registered-item"
                                    self.yang_parent_name = "basic-info"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('tuple', (YLeaf(YType.str, 'tuple'), ['str'])),
                                    ])
                                    self.tuple = None
                                    self._segment_path = lambda: "registered-item"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(SystemProcess.NodeTable.Node.Name.ProcessNameRunDetails.ProcessNameRunDetail.BasicInfo.RegisteredItem, ['tuple'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
                                    return meta._meta_table['SystemProcess.NodeTable.Node.Name.ProcessNameRunDetails.ProcessNameRunDetail.BasicInfo.RegisteredItem']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
                                return meta._meta_table['SystemProcess.NodeTable.Node.Name.ProcessNameRunDetails.ProcessNameRunDetail.BasicInfo']['meta_info']


                        class DetailInfo(_Entity_):
                            """
                            Process Detail Info
                            
                            .. attribute:: running_path
                            
                            	Running path
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: package_path
                            
                            	Package path
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: job_id_link
                            
                            	Job Id Link
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: group_jid
                            
                            	Group Jid
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: fail_count
                            
                            	Fail count
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: restart_needed
                            
                            	Restart needed
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: init_process
                            
                            	Init process
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: last_online
                            
                            	Last Online
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: this_pcb
                            
                            	This PCB
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: next_pcb
                            
                            	Next PCB
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: envs
                            
                            	Env variables
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: wait_for
                            
                            	Wait For /dev/xxx
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: job_id_on_rp
                            
                            	Job ID on RP
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: is_standby_capable
                            
                            	Is standby capable?
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: disable_kill
                            
                            	Disable kill?
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: send_avail
                            
                            	Check avail
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: node_event_cli_info
                            
                            	Node Event CLI info
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: node_redundancy_state
                            
                            	Node redundancy state
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: role_event_cli_info
                            
                            	Role event cli info
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: proc_role_state
                            
                            	Proc Role State
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: standby_event_cli_info
                            
                            	Standby Event CLI info
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: cleanup_event_cli_info
                            
                            	Cleanup event CLI info
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: band_ready_event_cli_info
                            
                            	Band Ready Event CLI Info
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: lr_event_cli_info
                            
                            	LR Event CLI Info
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: plane_ready_event_cli_info
                            
                            	Plane Ready Event CLI info
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: mdr_is_done_cli_info
                            
                            	MDR is done CLI Info
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'sysmgr-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(SystemProcess.NodeTable.Node.Name.ProcessNameRunDetails.ProcessNameRunDetail.DetailInfo, self).__init__()

                                self.yang_name = "detail-info"
                                self.yang_parent_name = "process-name-run-detail"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('running_path', (YLeaf(YType.str, 'running-path'), ['str'])),
                                    ('package_path', (YLeaf(YType.str, 'package-path'), ['str'])),
                                    ('job_id_link', (YLeaf(YType.int32, 'job-id-link'), ['int'])),
                                    ('group_jid', (YLeaf(YType.str, 'group-jid'), ['str'])),
                                    ('fail_count', (YLeaf(YType.uint32, 'fail-count'), ['int'])),
                                    ('restart_needed', (YLeaf(YType.boolean, 'restart-needed'), ['bool'])),
                                    ('init_process', (YLeaf(YType.boolean, 'init-process'), ['bool'])),
                                    ('last_online', (YLeaf(YType.str, 'last-online'), ['str'])),
                                    ('this_pcb', (YLeaf(YType.str, 'this-pcb'), ['str'])),
                                    ('next_pcb', (YLeaf(YType.str, 'next-pcb'), ['str'])),
                                    ('envs', (YLeaf(YType.str, 'envs'), ['str'])),
                                    ('wait_for', (YLeaf(YType.str, 'wait-for'), ['str'])),
                                    ('job_id_on_rp', (YLeaf(YType.int32, 'job-id-on-rp'), ['int'])),
                                    ('is_standby_capable', (YLeaf(YType.boolean, 'is-standby-capable'), ['bool'])),
                                    ('disable_kill', (YLeaf(YType.boolean, 'disable-kill'), ['bool'])),
                                    ('send_avail', (YLeaf(YType.boolean, 'send-avail'), ['bool'])),
                                    ('node_event_cli_info', (YLeaf(YType.int32, 'node-event-cli-info'), ['int'])),
                                    ('node_redundancy_state', (YLeaf(YType.str, 'node-redundancy-state'), ['str'])),
                                    ('role_event_cli_info', (YLeaf(YType.int32, 'role-event-cli-info'), ['int'])),
                                    ('proc_role_state', (YLeaf(YType.str, 'proc-role-state'), ['str'])),
                                    ('standby_event_cli_info', (YLeaf(YType.int32, 'standby-event-cli-info'), ['int'])),
                                    ('cleanup_event_cli_info', (YLeaf(YType.int32, 'cleanup-event-cli-info'), ['int'])),
                                    ('band_ready_event_cli_info', (YLeaf(YType.int32, 'band-ready-event-cli-info'), ['int'])),
                                    ('lr_event_cli_info', (YLeaf(YType.int32, 'lr-event-cli-info'), ['int'])),
                                    ('plane_ready_event_cli_info', (YLeaf(YType.int32, 'plane-ready-event-cli-info'), ['int'])),
                                    ('mdr_is_done_cli_info', (YLeaf(YType.int32, 'mdr-is-done-cli-info'), ['int'])),
                                ])
                                self.running_path = None
                                self.package_path = None
                                self.job_id_link = None
                                self.group_jid = None
                                self.fail_count = None
                                self.restart_needed = None
                                self.init_process = None
                                self.last_online = None
                                self.this_pcb = None
                                self.next_pcb = None
                                self.envs = None
                                self.wait_for = None
                                self.job_id_on_rp = None
                                self.is_standby_capable = None
                                self.disable_kill = None
                                self.send_avail = None
                                self.node_event_cli_info = None
                                self.node_redundancy_state = None
                                self.role_event_cli_info = None
                                self.proc_role_state = None
                                self.standby_event_cli_info = None
                                self.cleanup_event_cli_info = None
                                self.band_ready_event_cli_info = None
                                self.lr_event_cli_info = None
                                self.plane_ready_event_cli_info = None
                                self.mdr_is_done_cli_info = None
                                self._segment_path = lambda: "detail-info"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(SystemProcess.NodeTable.Node.Name.ProcessNameRunDetails.ProcessNameRunDetail.DetailInfo, ['running_path', 'package_path', 'job_id_link', 'group_jid', 'fail_count', 'restart_needed', 'init_process', 'last_online', 'this_pcb', 'next_pcb', 'envs', 'wait_for', 'job_id_on_rp', 'is_standby_capable', 'disable_kill', 'send_avail', 'node_event_cli_info', 'node_redundancy_state', 'role_event_cli_info', 'proc_role_state', 'standby_event_cli_info', 'cleanup_event_cli_info', 'band_ready_event_cli_info', 'lr_event_cli_info', 'plane_ready_event_cli_info', 'mdr_is_done_cli_info'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
                                return meta._meta_table['SystemProcess.NodeTable.Node.Name.ProcessNameRunDetails.ProcessNameRunDetail.DetailInfo']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
                            return meta._meta_table['SystemProcess.NodeTable.Node.Name.ProcessNameRunDetails.ProcessNameRunDetail']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
                        return meta._meta_table['SystemProcess.NodeTable.Node.Name.ProcessNameRunDetails']['meta_info']


                class ProcessNameRunverboses(_Entity_):
                    """
                    Process <WORD> information
                    
                    .. attribute:: process_name_runverbose
                    
                    	Process <WORD> run verbose information
                    	**type**\: list of  		 :py:class:`ProcessNameRunverbose <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.SystemProcess.NodeTable.Node.Name.ProcessNameRunverboses.ProcessNameRunverbose>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'sysmgr-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(SystemProcess.NodeTable.Node.Name.ProcessNameRunverboses, self).__init__()

                        self.yang_name = "process-name-runverboses"
                        self.yang_parent_name = "name"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("process-name-runverbose", ("process_name_runverbose", SystemProcess.NodeTable.Node.Name.ProcessNameRunverboses.ProcessNameRunverbose))])
                        self._leafs = OrderedDict()

                        self.process_name_runverbose = YList(self)
                        self._segment_path = lambda: "process-name-runverboses"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(SystemProcess.NodeTable.Node.Name.ProcessNameRunverboses, [], name, value)


                    class ProcessNameRunverbose(_Entity_):
                        """
                        Process <WORD> run verbose information
                        
                        .. attribute:: proc_name  (key)
                        
                        	Process Name
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        	**config**\: False
                        
                        .. attribute:: basic_info
                        
                        	Process Basic Info
                        	**type**\:  :py:class:`BasicInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.SystemProcess.NodeTable.Node.Name.ProcessNameRunverboses.ProcessNameRunverbose.BasicInfo>`
                        
                        	**config**\: False
                        
                        .. attribute:: detail_info
                        
                        	Process Detail Info
                        	**type**\:  :py:class:`DetailInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.SystemProcess.NodeTable.Node.Name.ProcessNameRunverboses.ProcessNameRunverbose.DetailInfo>`
                        
                        	**config**\: False
                        
                        .. attribute:: verbose_info
                        
                        	Process Verbose Info
                        	**type**\:  :py:class:`VerboseInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.SystemProcess.NodeTable.Node.Name.ProcessNameRunverboses.ProcessNameRunverbose.VerboseInfo>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'sysmgr-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(SystemProcess.NodeTable.Node.Name.ProcessNameRunverboses.ProcessNameRunverbose, self).__init__()

                            self.yang_name = "process-name-runverbose"
                            self.yang_parent_name = "process-name-runverboses"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['proc_name']
                            self._child_classes = OrderedDict([("basic-info", ("basic_info", SystemProcess.NodeTable.Node.Name.ProcessNameRunverboses.ProcessNameRunverbose.BasicInfo)), ("detail-info", ("detail_info", SystemProcess.NodeTable.Node.Name.ProcessNameRunverboses.ProcessNameRunverbose.DetailInfo)), ("verbose-info", ("verbose_info", SystemProcess.NodeTable.Node.Name.ProcessNameRunverboses.ProcessNameRunverbose.VerboseInfo))])
                            self._leafs = OrderedDict([
                                ('proc_name', (YLeaf(YType.str, 'proc-name'), ['str'])),
                            ])
                            self.proc_name = None

                            self.basic_info = SystemProcess.NodeTable.Node.Name.ProcessNameRunverboses.ProcessNameRunverbose.BasicInfo()
                            self.basic_info.parent = self
                            self._children_name_map["basic_info"] = "basic-info"

                            self.detail_info = SystemProcess.NodeTable.Node.Name.ProcessNameRunverboses.ProcessNameRunverbose.DetailInfo()
                            self.detail_info.parent = self
                            self._children_name_map["detail_info"] = "detail-info"

                            self.verbose_info = SystemProcess.NodeTable.Node.Name.ProcessNameRunverboses.ProcessNameRunverbose.VerboseInfo()
                            self.verbose_info.parent = self
                            self._children_name_map["verbose_info"] = "verbose-info"
                            self._segment_path = lambda: "process-name-runverbose" + "[proc-name='" + str(self.proc_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(SystemProcess.NodeTable.Node.Name.ProcessNameRunverboses.ProcessNameRunverbose, ['proc_name'], name, value)


                        class BasicInfo(_Entity_):
                            """
                            Process Basic Info
                            
                            .. attribute:: proc_cpu_time
                            
                            	Proces cpu time
                            	**type**\:  :py:class:`ProcCpuTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.SystemProcess.NodeTable.Node.Name.ProcessNameRunverboses.ProcessNameRunverbose.BasicInfo.ProcCpuTime>`
                            
                            	**config**\: False
                            
                            .. attribute:: job_id_xr
                            
                            	Job ID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: process_id
                            
                            	PID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: process_name
                            
                            	Process name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: executable
                            
                            	Executable name or path
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: active_path
                            
                            	Active Path
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: instance_id
                            
                            	Instance ID
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: args
                            
                            	Args
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: version_id
                            
                            	Version ID
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: respawn
                            
                            	Respawn on/off
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: respawn_count
                            
                            	Respawn Count
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: last_started
                            
                            	Last Started
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: process_state
                            
                            	Process State
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: last_exit_status
                            
                            	Last Exit status
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: last_exit_reason
                            
                            	Last Exit due to
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: package_state
                            
                            	Package State
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: started_on_config
                            
                            	Started on Config
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: feature_name
                            
                            	Feature Name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: tag
                            
                            	Tag
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: group
                            
                            	Process Group
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: core
                            
                            	Core
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: max_core
                            
                            	Max core
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: level
                            
                            	Level
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: mandatory
                            
                            	Is mandatory?
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: maint_mode_proc
                            
                            	Is admin mode process?
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: placement_state
                            
                            	Placement State
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: start_up_path
                            
                            	Startup Path
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: memory_limit
                            
                            	Memory Limit
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: ready
                            
                            	Elapsed Ready
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: available
                            
                            	Elapsed Available
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: registered_item
                            
                            	Registered Items
                            	**type**\: list of  		 :py:class:`RegisteredItem <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.SystemProcess.NodeTable.Node.Name.ProcessNameRunverboses.ProcessNameRunverbose.BasicInfo.RegisteredItem>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'sysmgr-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(SystemProcess.NodeTable.Node.Name.ProcessNameRunverboses.ProcessNameRunverbose.BasicInfo, self).__init__()

                                self.yang_name = "basic-info"
                                self.yang_parent_name = "process-name-runverbose"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("proc-cpu-time", ("proc_cpu_time", SystemProcess.NodeTable.Node.Name.ProcessNameRunverboses.ProcessNameRunverbose.BasicInfo.ProcCpuTime)), ("registered-item", ("registered_item", SystemProcess.NodeTable.Node.Name.ProcessNameRunverboses.ProcessNameRunverbose.BasicInfo.RegisteredItem))])
                                self._leafs = OrderedDict([
                                    ('job_id_xr', (YLeaf(YType.uint32, 'job-id-xr'), ['int'])),
                                    ('process_id', (YLeaf(YType.uint32, 'process-id'), ['int'])),
                                    ('process_name', (YLeaf(YType.str, 'process-name'), ['str'])),
                                    ('executable', (YLeaf(YType.str, 'executable'), ['str'])),
                                    ('active_path', (YLeaf(YType.str, 'active-path'), ['str'])),
                                    ('instance_id', (YLeaf(YType.int32, 'instance-id'), ['int'])),
                                    ('args', (YLeaf(YType.str, 'args'), ['str'])),
                                    ('version_id', (YLeaf(YType.str, 'version-id'), ['str'])),
                                    ('respawn', (YLeaf(YType.str, 'respawn'), ['str'])),
                                    ('respawn_count', (YLeaf(YType.int32, 'respawn-count'), ['int'])),
                                    ('last_started', (YLeaf(YType.str, 'last-started'), ['str'])),
                                    ('process_state', (YLeaf(YType.str, 'process-state'), ['str'])),
                                    ('last_exit_status', (YLeaf(YType.int32, 'last-exit-status'), ['int'])),
                                    ('last_exit_reason', (YLeaf(YType.str, 'last-exit-reason'), ['str'])),
                                    ('package_state', (YLeaf(YType.str, 'package-state'), ['str'])),
                                    ('started_on_config', (YLeaf(YType.str, 'started-on-config'), ['str'])),
                                    ('feature_name', (YLeaf(YType.str, 'feature-name'), ['str'])),
                                    ('tag', (YLeaf(YType.str, 'tag'), ['str'])),
                                    ('group', (YLeaf(YType.str, 'group'), ['str'])),
                                    ('core', (YLeaf(YType.str, 'core'), ['str'])),
                                    ('max_core', (YLeaf(YType.int32, 'max-core'), ['int'])),
                                    ('level', (YLeaf(YType.str, 'level'), ['str'])),
                                    ('mandatory', (YLeaf(YType.boolean, 'mandatory'), ['bool'])),
                                    ('maint_mode_proc', (YLeaf(YType.boolean, 'maint-mode-proc'), ['bool'])),
                                    ('placement_state', (YLeaf(YType.str, 'placement-state'), ['str'])),
                                    ('start_up_path', (YLeaf(YType.str, 'start-up-path'), ['str'])),
                                    ('memory_limit', (YLeaf(YType.uint32, 'memory-limit'), ['int'])),
                                    ('ready', (YLeaf(YType.str, 'ready'), ['str'])),
                                    ('available', (YLeaf(YType.str, 'available'), ['str'])),
                                ])
                                self.job_id_xr = None
                                self.process_id = None
                                self.process_name = None
                                self.executable = None
                                self.active_path = None
                                self.instance_id = None
                                self.args = None
                                self.version_id = None
                                self.respawn = None
                                self.respawn_count = None
                                self.last_started = None
                                self.process_state = None
                                self.last_exit_status = None
                                self.last_exit_reason = None
                                self.package_state = None
                                self.started_on_config = None
                                self.feature_name = None
                                self.tag = None
                                self.group = None
                                self.core = None
                                self.max_core = None
                                self.level = None
                                self.mandatory = None
                                self.maint_mode_proc = None
                                self.placement_state = None
                                self.start_up_path = None
                                self.memory_limit = None
                                self.ready = None
                                self.available = None

                                self.proc_cpu_time = SystemProcess.NodeTable.Node.Name.ProcessNameRunverboses.ProcessNameRunverbose.BasicInfo.ProcCpuTime()
                                self.proc_cpu_time.parent = self
                                self._children_name_map["proc_cpu_time"] = "proc-cpu-time"

                                self.registered_item = YList(self)
                                self._segment_path = lambda: "basic-info"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(SystemProcess.NodeTable.Node.Name.ProcessNameRunverboses.ProcessNameRunverbose.BasicInfo, ['job_id_xr', 'process_id', 'process_name', 'executable', 'active_path', 'instance_id', 'args', 'version_id', 'respawn', 'respawn_count', 'last_started', 'process_state', 'last_exit_status', 'last_exit_reason', 'package_state', 'started_on_config', 'feature_name', 'tag', 'group', 'core', 'max_core', 'level', 'mandatory', 'maint_mode_proc', 'placement_state', 'start_up_path', 'memory_limit', 'ready', 'available'], name, value)


                            class ProcCpuTime(_Entity_):
                                """
                                Proces cpu time
                                
                                .. attribute:: user
                                
                                	User time
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: system
                                
                                	Kernel time
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: total
                                
                                	Total time
                                	**type**\: str
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'sysmgr-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(SystemProcess.NodeTable.Node.Name.ProcessNameRunverboses.ProcessNameRunverbose.BasicInfo.ProcCpuTime, self).__init__()

                                    self.yang_name = "proc-cpu-time"
                                    self.yang_parent_name = "basic-info"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('user', (YLeaf(YType.str, 'user'), ['str'])),
                                        ('system', (YLeaf(YType.str, 'system'), ['str'])),
                                        ('total', (YLeaf(YType.str, 'total'), ['str'])),
                                    ])
                                    self.user = None
                                    self.system = None
                                    self.total = None
                                    self._segment_path = lambda: "proc-cpu-time"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(SystemProcess.NodeTable.Node.Name.ProcessNameRunverboses.ProcessNameRunverbose.BasicInfo.ProcCpuTime, ['user', 'system', 'total'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
                                    return meta._meta_table['SystemProcess.NodeTable.Node.Name.ProcessNameRunverboses.ProcessNameRunverbose.BasicInfo.ProcCpuTime']['meta_info']


                            class RegisteredItem(_Entity_):
                                """
                                Registered Items
                                
                                .. attribute:: tuple
                                
                                	Tuple
                                	**type**\: str
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'sysmgr-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(SystemProcess.NodeTable.Node.Name.ProcessNameRunverboses.ProcessNameRunverbose.BasicInfo.RegisteredItem, self).__init__()

                                    self.yang_name = "registered-item"
                                    self.yang_parent_name = "basic-info"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('tuple', (YLeaf(YType.str, 'tuple'), ['str'])),
                                    ])
                                    self.tuple = None
                                    self._segment_path = lambda: "registered-item"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(SystemProcess.NodeTable.Node.Name.ProcessNameRunverboses.ProcessNameRunverbose.BasicInfo.RegisteredItem, ['tuple'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
                                    return meta._meta_table['SystemProcess.NodeTable.Node.Name.ProcessNameRunverboses.ProcessNameRunverbose.BasicInfo.RegisteredItem']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
                                return meta._meta_table['SystemProcess.NodeTable.Node.Name.ProcessNameRunverboses.ProcessNameRunverbose.BasicInfo']['meta_info']


                        class DetailInfo(_Entity_):
                            """
                            Process Detail Info
                            
                            .. attribute:: running_path
                            
                            	Running path
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: package_path
                            
                            	Package path
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: job_id_link
                            
                            	Job Id Link
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: group_jid
                            
                            	Group Jid
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: fail_count
                            
                            	Fail count
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: restart_needed
                            
                            	Restart needed
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: init_process
                            
                            	Init process
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: last_online
                            
                            	Last Online
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: this_pcb
                            
                            	This PCB
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: next_pcb
                            
                            	Next PCB
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: envs
                            
                            	Env variables
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: wait_for
                            
                            	Wait For /dev/xxx
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: job_id_on_rp
                            
                            	Job ID on RP
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: is_standby_capable
                            
                            	Is standby capable?
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: disable_kill
                            
                            	Disable kill?
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: send_avail
                            
                            	Check avail
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: node_event_cli_info
                            
                            	Node Event CLI info
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: node_redundancy_state
                            
                            	Node redundancy state
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: role_event_cli_info
                            
                            	Role event cli info
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: proc_role_state
                            
                            	Proc Role State
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: standby_event_cli_info
                            
                            	Standby Event CLI info
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: cleanup_event_cli_info
                            
                            	Cleanup event CLI info
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: band_ready_event_cli_info
                            
                            	Band Ready Event CLI Info
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: lr_event_cli_info
                            
                            	LR Event CLI Info
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: plane_ready_event_cli_info
                            
                            	Plane Ready Event CLI info
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: mdr_is_done_cli_info
                            
                            	MDR is done CLI Info
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'sysmgr-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(SystemProcess.NodeTable.Node.Name.ProcessNameRunverboses.ProcessNameRunverbose.DetailInfo, self).__init__()

                                self.yang_name = "detail-info"
                                self.yang_parent_name = "process-name-runverbose"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('running_path', (YLeaf(YType.str, 'running-path'), ['str'])),
                                    ('package_path', (YLeaf(YType.str, 'package-path'), ['str'])),
                                    ('job_id_link', (YLeaf(YType.int32, 'job-id-link'), ['int'])),
                                    ('group_jid', (YLeaf(YType.str, 'group-jid'), ['str'])),
                                    ('fail_count', (YLeaf(YType.uint32, 'fail-count'), ['int'])),
                                    ('restart_needed', (YLeaf(YType.boolean, 'restart-needed'), ['bool'])),
                                    ('init_process', (YLeaf(YType.boolean, 'init-process'), ['bool'])),
                                    ('last_online', (YLeaf(YType.str, 'last-online'), ['str'])),
                                    ('this_pcb', (YLeaf(YType.str, 'this-pcb'), ['str'])),
                                    ('next_pcb', (YLeaf(YType.str, 'next-pcb'), ['str'])),
                                    ('envs', (YLeaf(YType.str, 'envs'), ['str'])),
                                    ('wait_for', (YLeaf(YType.str, 'wait-for'), ['str'])),
                                    ('job_id_on_rp', (YLeaf(YType.int32, 'job-id-on-rp'), ['int'])),
                                    ('is_standby_capable', (YLeaf(YType.boolean, 'is-standby-capable'), ['bool'])),
                                    ('disable_kill', (YLeaf(YType.boolean, 'disable-kill'), ['bool'])),
                                    ('send_avail', (YLeaf(YType.boolean, 'send-avail'), ['bool'])),
                                    ('node_event_cli_info', (YLeaf(YType.int32, 'node-event-cli-info'), ['int'])),
                                    ('node_redundancy_state', (YLeaf(YType.str, 'node-redundancy-state'), ['str'])),
                                    ('role_event_cli_info', (YLeaf(YType.int32, 'role-event-cli-info'), ['int'])),
                                    ('proc_role_state', (YLeaf(YType.str, 'proc-role-state'), ['str'])),
                                    ('standby_event_cli_info', (YLeaf(YType.int32, 'standby-event-cli-info'), ['int'])),
                                    ('cleanup_event_cli_info', (YLeaf(YType.int32, 'cleanup-event-cli-info'), ['int'])),
                                    ('band_ready_event_cli_info', (YLeaf(YType.int32, 'band-ready-event-cli-info'), ['int'])),
                                    ('lr_event_cli_info', (YLeaf(YType.int32, 'lr-event-cli-info'), ['int'])),
                                    ('plane_ready_event_cli_info', (YLeaf(YType.int32, 'plane-ready-event-cli-info'), ['int'])),
                                    ('mdr_is_done_cli_info', (YLeaf(YType.int32, 'mdr-is-done-cli-info'), ['int'])),
                                ])
                                self.running_path = None
                                self.package_path = None
                                self.job_id_link = None
                                self.group_jid = None
                                self.fail_count = None
                                self.restart_needed = None
                                self.init_process = None
                                self.last_online = None
                                self.this_pcb = None
                                self.next_pcb = None
                                self.envs = None
                                self.wait_for = None
                                self.job_id_on_rp = None
                                self.is_standby_capable = None
                                self.disable_kill = None
                                self.send_avail = None
                                self.node_event_cli_info = None
                                self.node_redundancy_state = None
                                self.role_event_cli_info = None
                                self.proc_role_state = None
                                self.standby_event_cli_info = None
                                self.cleanup_event_cli_info = None
                                self.band_ready_event_cli_info = None
                                self.lr_event_cli_info = None
                                self.plane_ready_event_cli_info = None
                                self.mdr_is_done_cli_info = None
                                self._segment_path = lambda: "detail-info"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(SystemProcess.NodeTable.Node.Name.ProcessNameRunverboses.ProcessNameRunverbose.DetailInfo, ['running_path', 'package_path', 'job_id_link', 'group_jid', 'fail_count', 'restart_needed', 'init_process', 'last_online', 'this_pcb', 'next_pcb', 'envs', 'wait_for', 'job_id_on_rp', 'is_standby_capable', 'disable_kill', 'send_avail', 'node_event_cli_info', 'node_redundancy_state', 'role_event_cli_info', 'proc_role_state', 'standby_event_cli_info', 'cleanup_event_cli_info', 'band_ready_event_cli_info', 'lr_event_cli_info', 'plane_ready_event_cli_info', 'mdr_is_done_cli_info'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
                                return meta._meta_table['SystemProcess.NodeTable.Node.Name.ProcessNameRunverboses.ProcessNameRunverbose.DetailInfo']['meta_info']


                        class VerboseInfo(_Entity_):
                            """
                            Process Verbose Info
                            
                            .. attribute:: process_group
                            
                            	Process Group
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: respawn_allowed
                            
                            	Is respawn allowed?
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: wait_for_exit
                            
                            	Wait for exit
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: dynamic_tag
                            
                            	Dynamic Tag
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: forced_stop
                            
                            	Forced stop
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: critical_process
                            
                            	Critical Process
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: hold
                            
                            	Hold
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: transient
                            
                            	Transient
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: tuple_cfgmgr
                            
                            	Tuple Cfgmgr
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: standby_capable
                            
                            	Standby capable
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: edm_startup
                            
                            	EDM startup
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: placement
                            
                            	Placement
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: skip_kill_notif
                            
                            	Skip Kill Notif
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: init_proc
                            
                            	Init process
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: sysdb_event
                            
                            	Sysdb Event
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: level_started
                            
                            	Level Started
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: proc_avail
                            
                            	Process available
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: tuples_scanned
                            
                            	Tuples Scanned
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: no_chkpt_start
                            
                            	No checkpoint start
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: in_shut_down
                            
                            	In Shut Down
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: sm_started
                            
                            	SM started
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: ignore_on_sc
                            
                            	Ignore on SC
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: ignore_on_easy_bake
                            
                            	Ignore on EasyBake
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: pre_init
                            
                            	Pre init
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: eoi_received
                            
                            	EOI received
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: eoi_timeout
                            
                            	EOI Timeout
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: avail_timeout
                            
                            	Avail Timeout
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: reserved_memory
                            
                            	Reserved Memory
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: allow_warned
                            
                            	Allow Warned
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: arg_change
                            
                            	Arg Change
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: restart_on_tuple
                            
                            	Restart on tuple
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: boot_hold
                            
                            	Boot Hold
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: reg_id
                            
                            	Reg Id
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: memory_limit
                            
                            	Memory Limit
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: parent_job_id
                            
                            	Parent Job ID
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: tuple_index
                            
                            	Tuple Index
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: dump_count
                            
                            	Dump Count
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: respawn_interval_user
                            
                            	Respawn Interval User
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: silent_restart_count
                            
                            	Silent Restart Count
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: critical_tier
                            
                            	Critical Tier
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: exit_type
                            
                            	Exit Type
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: init_timeout
                            
                            	Init Timeout
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: restart_by_cmd
                            
                            	Restart by Command
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: boot_pref
                            
                            	Boot Pref
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: mdr_mbi_proc
                            
                            	Mdr Mbi proc
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: mdr_non_mbi_kld
                            
                            	Mdr Non Mbi Kld
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: mdr_mbi_kld
                            
                            	Mdr Mbi Kld
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: mdr_shut_delay
                            
                            	Mdr Shut Delay
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: mdr_keep_thru
                            
                            	Mdr Keep Thru
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: mdr_spoofer
                            
                            	Mdr spoofer
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: mdr_spoofed
                            
                            	Mdr spoofed
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: mdr_spoofed_last
                            
                            	Mdr spoofed last
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: mdr_spoofed_ready
                            
                            	Mdr Spoofed Ready
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: mdr_pcb_check
                            
                            	Mdr PCB Check
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: mdr_kill_tier
                            
                            	Mdr Kill Tier
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: mdr_kld
                            
                            	Mdr kld
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: mdr_level
                            
                            	Mdr Level
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: fm_restart_cnt
                            
                            	FM restart count
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: self_managed
                            
                            	Self Managed
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: tuple
                            
                            	Tuple
                            	**type**\: list of  		 :py:class:`Tuple <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.SystemProcess.NodeTable.Node.Name.ProcessNameRunverboses.ProcessNameRunverbose.VerboseInfo.Tuple>`
                            
                            	**config**\: False
                            
                            .. attribute:: orig_tuple
                            
                            	Orig Tuple
                            	**type**\: list of  		 :py:class:`OrigTuple <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.SystemProcess.NodeTable.Node.Name.ProcessNameRunverboses.ProcessNameRunverbose.VerboseInfo.OrigTuple>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'sysmgr-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(SystemProcess.NodeTable.Node.Name.ProcessNameRunverboses.ProcessNameRunverbose.VerboseInfo, self).__init__()

                                self.yang_name = "verbose-info"
                                self.yang_parent_name = "process-name-runverbose"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("tuple", ("tuple", SystemProcess.NodeTable.Node.Name.ProcessNameRunverboses.ProcessNameRunverbose.VerboseInfo.Tuple)), ("orig-tuple", ("orig_tuple", SystemProcess.NodeTable.Node.Name.ProcessNameRunverboses.ProcessNameRunverbose.VerboseInfo.OrigTuple))])
                                self._leafs = OrderedDict([
                                    ('process_group', (YLeaf(YType.str, 'process-group'), ['str'])),
                                    ('respawn_allowed', (YLeaf(YType.int32, 'respawn-allowed'), ['int'])),
                                    ('wait_for_exit', (YLeaf(YType.int32, 'wait-for-exit'), ['int'])),
                                    ('dynamic_tag', (YLeaf(YType.int32, 'dynamic-tag'), ['int'])),
                                    ('forced_stop', (YLeaf(YType.int32, 'forced-stop'), ['int'])),
                                    ('critical_process', (YLeaf(YType.int32, 'critical-process'), ['int'])),
                                    ('hold', (YLeaf(YType.int32, 'hold'), ['int'])),
                                    ('transient', (YLeaf(YType.int32, 'transient'), ['int'])),
                                    ('tuple_cfgmgr', (YLeaf(YType.int32, 'tuple-cfgmgr'), ['int'])),
                                    ('standby_capable', (YLeaf(YType.int32, 'standby-capable'), ['int'])),
                                    ('edm_startup', (YLeaf(YType.int32, 'edm-startup'), ['int'])),
                                    ('placement', (YLeaf(YType.int32, 'placement'), ['int'])),
                                    ('skip_kill_notif', (YLeaf(YType.int32, 'skip-kill-notif'), ['int'])),
                                    ('init_proc', (YLeaf(YType.int32, 'init-proc'), ['int'])),
                                    ('sysdb_event', (YLeaf(YType.int32, 'sysdb-event'), ['int'])),
                                    ('level_started', (YLeaf(YType.int32, 'level-started'), ['int'])),
                                    ('proc_avail', (YLeaf(YType.int32, 'proc-avail'), ['int'])),
                                    ('tuples_scanned', (YLeaf(YType.int32, 'tuples-scanned'), ['int'])),
                                    ('no_chkpt_start', (YLeaf(YType.int32, 'no-chkpt-start'), ['int'])),
                                    ('in_shut_down', (YLeaf(YType.int32, 'in-shut-down'), ['int'])),
                                    ('sm_started', (YLeaf(YType.int32, 'sm-started'), ['int'])),
                                    ('ignore_on_sc', (YLeaf(YType.int32, 'ignore-on-sc'), ['int'])),
                                    ('ignore_on_easy_bake', (YLeaf(YType.int32, 'ignore-on-easy-bake'), ['int'])),
                                    ('pre_init', (YLeaf(YType.int32, 'pre-init'), ['int'])),
                                    ('eoi_received', (YLeaf(YType.int32, 'eoi-received'), ['int'])),
                                    ('eoi_timeout', (YLeaf(YType.int32, 'eoi-timeout'), ['int'])),
                                    ('avail_timeout', (YLeaf(YType.int32, 'avail-timeout'), ['int'])),
                                    ('reserved_memory', (YLeaf(YType.int32, 'reserved-memory'), ['int'])),
                                    ('allow_warned', (YLeaf(YType.int32, 'allow-warned'), ['int'])),
                                    ('arg_change', (YLeaf(YType.int32, 'arg-change'), ['int'])),
                                    ('restart_on_tuple', (YLeaf(YType.int32, 'restart-on-tuple'), ['int'])),
                                    ('boot_hold', (YLeaf(YType.int32, 'boot-hold'), ['int'])),
                                    ('reg_id', (YLeaf(YType.int32, 'reg-id'), ['int'])),
                                    ('memory_limit', (YLeaf(YType.int32, 'memory-limit'), ['int'])),
                                    ('parent_job_id', (YLeaf(YType.int32, 'parent-job-id'), ['int'])),
                                    ('tuple_index', (YLeaf(YType.int32, 'tuple-index'), ['int'])),
                                    ('dump_count', (YLeaf(YType.int32, 'dump-count'), ['int'])),
                                    ('respawn_interval_user', (YLeaf(YType.int32, 'respawn-interval-user'), ['int'])),
                                    ('silent_restart_count', (YLeaf(YType.int32, 'silent-restart-count'), ['int'])),
                                    ('critical_tier', (YLeaf(YType.int32, 'critical-tier'), ['int'])),
                                    ('exit_type', (YLeaf(YType.int32, 'exit-type'), ['int'])),
                                    ('init_timeout', (YLeaf(YType.int32, 'init-timeout'), ['int'])),
                                    ('restart_by_cmd', (YLeaf(YType.int32, 'restart-by-cmd'), ['int'])),
                                    ('boot_pref', (YLeaf(YType.int32, 'boot-pref'), ['int'])),
                                    ('mdr_mbi_proc', (YLeaf(YType.int32, 'mdr-mbi-proc'), ['int'])),
                                    ('mdr_non_mbi_kld', (YLeaf(YType.int32, 'mdr-non-mbi-kld'), ['int'])),
                                    ('mdr_mbi_kld', (YLeaf(YType.int32, 'mdr-mbi-kld'), ['int'])),
                                    ('mdr_shut_delay', (YLeaf(YType.int32, 'mdr-shut-delay'), ['int'])),
                                    ('mdr_keep_thru', (YLeaf(YType.int32, 'mdr-keep-thru'), ['int'])),
                                    ('mdr_spoofer', (YLeaf(YType.int32, 'mdr-spoofer'), ['int'])),
                                    ('mdr_spoofed', (YLeaf(YType.int32, 'mdr-spoofed'), ['int'])),
                                    ('mdr_spoofed_last', (YLeaf(YType.int32, 'mdr-spoofed-last'), ['int'])),
                                    ('mdr_spoofed_ready', (YLeaf(YType.int32, 'mdr-spoofed-ready'), ['int'])),
                                    ('mdr_pcb_check', (YLeaf(YType.int32, 'mdr-pcb-check'), ['int'])),
                                    ('mdr_kill_tier', (YLeaf(YType.int32, 'mdr-kill-tier'), ['int'])),
                                    ('mdr_kld', (YLeaf(YType.int32, 'mdr-kld'), ['int'])),
                                    ('mdr_level', (YLeaf(YType.int32, 'mdr-level'), ['int'])),
                                    ('fm_restart_cnt', (YLeaf(YType.int32, 'fm-restart-cnt'), ['int'])),
                                    ('self_managed', (YLeaf(YType.int32, 'self-managed'), ['int'])),
                                ])
                                self.process_group = None
                                self.respawn_allowed = None
                                self.wait_for_exit = None
                                self.dynamic_tag = None
                                self.forced_stop = None
                                self.critical_process = None
                                self.hold = None
                                self.transient = None
                                self.tuple_cfgmgr = None
                                self.standby_capable = None
                                self.edm_startup = None
                                self.placement = None
                                self.skip_kill_notif = None
                                self.init_proc = None
                                self.sysdb_event = None
                                self.level_started = None
                                self.proc_avail = None
                                self.tuples_scanned = None
                                self.no_chkpt_start = None
                                self.in_shut_down = None
                                self.sm_started = None
                                self.ignore_on_sc = None
                                self.ignore_on_easy_bake = None
                                self.pre_init = None
                                self.eoi_received = None
                                self.eoi_timeout = None
                                self.avail_timeout = None
                                self.reserved_memory = None
                                self.allow_warned = None
                                self.arg_change = None
                                self.restart_on_tuple = None
                                self.boot_hold = None
                                self.reg_id = None
                                self.memory_limit = None
                                self.parent_job_id = None
                                self.tuple_index = None
                                self.dump_count = None
                                self.respawn_interval_user = None
                                self.silent_restart_count = None
                                self.critical_tier = None
                                self.exit_type = None
                                self.init_timeout = None
                                self.restart_by_cmd = None
                                self.boot_pref = None
                                self.mdr_mbi_proc = None
                                self.mdr_non_mbi_kld = None
                                self.mdr_mbi_kld = None
                                self.mdr_shut_delay = None
                                self.mdr_keep_thru = None
                                self.mdr_spoofer = None
                                self.mdr_spoofed = None
                                self.mdr_spoofed_last = None
                                self.mdr_spoofed_ready = None
                                self.mdr_pcb_check = None
                                self.mdr_kill_tier = None
                                self.mdr_kld = None
                                self.mdr_level = None
                                self.fm_restart_cnt = None
                                self.self_managed = None

                                self.tuple = YList(self)
                                self.orig_tuple = YList(self)
                                self._segment_path = lambda: "verbose-info"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(SystemProcess.NodeTable.Node.Name.ProcessNameRunverboses.ProcessNameRunverbose.VerboseInfo, ['process_group', 'respawn_allowed', 'wait_for_exit', 'dynamic_tag', 'forced_stop', 'critical_process', 'hold', 'transient', 'tuple_cfgmgr', 'standby_capable', 'edm_startup', 'placement', 'skip_kill_notif', 'init_proc', 'sysdb_event', 'level_started', 'proc_avail', 'tuples_scanned', 'no_chkpt_start', 'in_shut_down', 'sm_started', 'ignore_on_sc', 'ignore_on_easy_bake', 'pre_init', 'eoi_received', 'eoi_timeout', 'avail_timeout', 'reserved_memory', 'allow_warned', 'arg_change', 'restart_on_tuple', 'boot_hold', 'reg_id', 'memory_limit', 'parent_job_id', 'tuple_index', 'dump_count', 'respawn_interval_user', 'silent_restart_count', 'critical_tier', 'exit_type', 'init_timeout', 'restart_by_cmd', 'boot_pref', 'mdr_mbi_proc', 'mdr_non_mbi_kld', 'mdr_mbi_kld', 'mdr_shut_delay', 'mdr_keep_thru', 'mdr_spoofer', 'mdr_spoofed', 'mdr_spoofed_last', 'mdr_spoofed_ready', 'mdr_pcb_check', 'mdr_kill_tier', 'mdr_kld', 'mdr_level', 'fm_restart_cnt', 'self_managed'], name, value)


                            class Tuple(_Entity_):
                                """
                                Tuple
                                
                                .. attribute:: tuple
                                
                                	Tuple
                                	**type**\: str
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'sysmgr-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(SystemProcess.NodeTable.Node.Name.ProcessNameRunverboses.ProcessNameRunverbose.VerboseInfo.Tuple, self).__init__()

                                    self.yang_name = "tuple"
                                    self.yang_parent_name = "verbose-info"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('tuple', (YLeaf(YType.str, 'tuple'), ['str'])),
                                    ])
                                    self.tuple = None
                                    self._segment_path = lambda: "tuple"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(SystemProcess.NodeTable.Node.Name.ProcessNameRunverboses.ProcessNameRunverbose.VerboseInfo.Tuple, ['tuple'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
                                    return meta._meta_table['SystemProcess.NodeTable.Node.Name.ProcessNameRunverboses.ProcessNameRunverbose.VerboseInfo.Tuple']['meta_info']


                            class OrigTuple(_Entity_):
                                """
                                Orig Tuple
                                
                                .. attribute:: tuple
                                
                                	Tuple
                                	**type**\: str
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'sysmgr-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(SystemProcess.NodeTable.Node.Name.ProcessNameRunverboses.ProcessNameRunverbose.VerboseInfo.OrigTuple, self).__init__()

                                    self.yang_name = "orig-tuple"
                                    self.yang_parent_name = "verbose-info"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('tuple', (YLeaf(YType.str, 'tuple'), ['str'])),
                                    ])
                                    self.tuple = None
                                    self._segment_path = lambda: "orig-tuple"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(SystemProcess.NodeTable.Node.Name.ProcessNameRunverboses.ProcessNameRunverbose.VerboseInfo.OrigTuple, ['tuple'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
                                    return meta._meta_table['SystemProcess.NodeTable.Node.Name.ProcessNameRunverboses.ProcessNameRunverbose.VerboseInfo.OrigTuple']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
                                return meta._meta_table['SystemProcess.NodeTable.Node.Name.ProcessNameRunverboses.ProcessNameRunverbose.VerboseInfo']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
                            return meta._meta_table['SystemProcess.NodeTable.Node.Name.ProcessNameRunverboses.ProcessNameRunverbose']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
                        return meta._meta_table['SystemProcess.NodeTable.Node.Name.ProcessNameRunverboses']['meta_info']


                class ProcessNameDetails(_Entity_):
                    """
                    Process <WORD> information
                    
                    .. attribute:: process_name_detail
                    
                    	Process <WORD> detail information
                    	**type**\: list of  		 :py:class:`ProcessNameDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.SystemProcess.NodeTable.Node.Name.ProcessNameDetails.ProcessNameDetail>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'sysmgr-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(SystemProcess.NodeTable.Node.Name.ProcessNameDetails, self).__init__()

                        self.yang_name = "process-name-details"
                        self.yang_parent_name = "name"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("process-name-detail", ("process_name_detail", SystemProcess.NodeTable.Node.Name.ProcessNameDetails.ProcessNameDetail))])
                        self._leafs = OrderedDict()

                        self.process_name_detail = YList(self)
                        self._segment_path = lambda: "process-name-details"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(SystemProcess.NodeTable.Node.Name.ProcessNameDetails, [], name, value)


                    class ProcessNameDetail(_Entity_):
                        """
                        Process <WORD> detail information
                        
                        .. attribute:: proc_name  (key)
                        
                        	Process Name
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        	**config**\: False
                        
                        .. attribute:: basic_info
                        
                        	Process Basic Info
                        	**type**\:  :py:class:`BasicInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.SystemProcess.NodeTable.Node.Name.ProcessNameDetails.ProcessNameDetail.BasicInfo>`
                        
                        	**config**\: False
                        
                        .. attribute:: detail_info
                        
                        	Process Detail Info
                        	**type**\:  :py:class:`DetailInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.SystemProcess.NodeTable.Node.Name.ProcessNameDetails.ProcessNameDetail.DetailInfo>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'sysmgr-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(SystemProcess.NodeTable.Node.Name.ProcessNameDetails.ProcessNameDetail, self).__init__()

                            self.yang_name = "process-name-detail"
                            self.yang_parent_name = "process-name-details"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['proc_name']
                            self._child_classes = OrderedDict([("basic-info", ("basic_info", SystemProcess.NodeTable.Node.Name.ProcessNameDetails.ProcessNameDetail.BasicInfo)), ("detail-info", ("detail_info", SystemProcess.NodeTable.Node.Name.ProcessNameDetails.ProcessNameDetail.DetailInfo))])
                            self._leafs = OrderedDict([
                                ('proc_name', (YLeaf(YType.str, 'proc-name'), ['str'])),
                            ])
                            self.proc_name = None

                            self.basic_info = SystemProcess.NodeTable.Node.Name.ProcessNameDetails.ProcessNameDetail.BasicInfo()
                            self.basic_info.parent = self
                            self._children_name_map["basic_info"] = "basic-info"

                            self.detail_info = SystemProcess.NodeTable.Node.Name.ProcessNameDetails.ProcessNameDetail.DetailInfo()
                            self.detail_info.parent = self
                            self._children_name_map["detail_info"] = "detail-info"
                            self._segment_path = lambda: "process-name-detail" + "[proc-name='" + str(self.proc_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(SystemProcess.NodeTable.Node.Name.ProcessNameDetails.ProcessNameDetail, ['proc_name'], name, value)


                        class BasicInfo(_Entity_):
                            """
                            Process Basic Info
                            
                            .. attribute:: proc_cpu_time
                            
                            	Proces cpu time
                            	**type**\:  :py:class:`ProcCpuTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.SystemProcess.NodeTable.Node.Name.ProcessNameDetails.ProcessNameDetail.BasicInfo.ProcCpuTime>`
                            
                            	**config**\: False
                            
                            .. attribute:: job_id_xr
                            
                            	Job ID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: process_id
                            
                            	PID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: process_name
                            
                            	Process name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: executable
                            
                            	Executable name or path
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: active_path
                            
                            	Active Path
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: instance_id
                            
                            	Instance ID
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: args
                            
                            	Args
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: version_id
                            
                            	Version ID
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: respawn
                            
                            	Respawn on/off
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: respawn_count
                            
                            	Respawn Count
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: last_started
                            
                            	Last Started
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: process_state
                            
                            	Process State
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: last_exit_status
                            
                            	Last Exit status
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: last_exit_reason
                            
                            	Last Exit due to
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: package_state
                            
                            	Package State
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: started_on_config
                            
                            	Started on Config
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: feature_name
                            
                            	Feature Name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: tag
                            
                            	Tag
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: group
                            
                            	Process Group
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: core
                            
                            	Core
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: max_core
                            
                            	Max core
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: level
                            
                            	Level
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: mandatory
                            
                            	Is mandatory?
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: maint_mode_proc
                            
                            	Is admin mode process?
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: placement_state
                            
                            	Placement State
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: start_up_path
                            
                            	Startup Path
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: memory_limit
                            
                            	Memory Limit
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: ready
                            
                            	Elapsed Ready
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: available
                            
                            	Elapsed Available
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: registered_item
                            
                            	Registered Items
                            	**type**\: list of  		 :py:class:`RegisteredItem <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.SystemProcess.NodeTable.Node.Name.ProcessNameDetails.ProcessNameDetail.BasicInfo.RegisteredItem>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'sysmgr-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(SystemProcess.NodeTable.Node.Name.ProcessNameDetails.ProcessNameDetail.BasicInfo, self).__init__()

                                self.yang_name = "basic-info"
                                self.yang_parent_name = "process-name-detail"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("proc-cpu-time", ("proc_cpu_time", SystemProcess.NodeTable.Node.Name.ProcessNameDetails.ProcessNameDetail.BasicInfo.ProcCpuTime)), ("registered-item", ("registered_item", SystemProcess.NodeTable.Node.Name.ProcessNameDetails.ProcessNameDetail.BasicInfo.RegisteredItem))])
                                self._leafs = OrderedDict([
                                    ('job_id_xr', (YLeaf(YType.uint32, 'job-id-xr'), ['int'])),
                                    ('process_id', (YLeaf(YType.uint32, 'process-id'), ['int'])),
                                    ('process_name', (YLeaf(YType.str, 'process-name'), ['str'])),
                                    ('executable', (YLeaf(YType.str, 'executable'), ['str'])),
                                    ('active_path', (YLeaf(YType.str, 'active-path'), ['str'])),
                                    ('instance_id', (YLeaf(YType.int32, 'instance-id'), ['int'])),
                                    ('args', (YLeaf(YType.str, 'args'), ['str'])),
                                    ('version_id', (YLeaf(YType.str, 'version-id'), ['str'])),
                                    ('respawn', (YLeaf(YType.str, 'respawn'), ['str'])),
                                    ('respawn_count', (YLeaf(YType.int32, 'respawn-count'), ['int'])),
                                    ('last_started', (YLeaf(YType.str, 'last-started'), ['str'])),
                                    ('process_state', (YLeaf(YType.str, 'process-state'), ['str'])),
                                    ('last_exit_status', (YLeaf(YType.int32, 'last-exit-status'), ['int'])),
                                    ('last_exit_reason', (YLeaf(YType.str, 'last-exit-reason'), ['str'])),
                                    ('package_state', (YLeaf(YType.str, 'package-state'), ['str'])),
                                    ('started_on_config', (YLeaf(YType.str, 'started-on-config'), ['str'])),
                                    ('feature_name', (YLeaf(YType.str, 'feature-name'), ['str'])),
                                    ('tag', (YLeaf(YType.str, 'tag'), ['str'])),
                                    ('group', (YLeaf(YType.str, 'group'), ['str'])),
                                    ('core', (YLeaf(YType.str, 'core'), ['str'])),
                                    ('max_core', (YLeaf(YType.int32, 'max-core'), ['int'])),
                                    ('level', (YLeaf(YType.str, 'level'), ['str'])),
                                    ('mandatory', (YLeaf(YType.boolean, 'mandatory'), ['bool'])),
                                    ('maint_mode_proc', (YLeaf(YType.boolean, 'maint-mode-proc'), ['bool'])),
                                    ('placement_state', (YLeaf(YType.str, 'placement-state'), ['str'])),
                                    ('start_up_path', (YLeaf(YType.str, 'start-up-path'), ['str'])),
                                    ('memory_limit', (YLeaf(YType.uint32, 'memory-limit'), ['int'])),
                                    ('ready', (YLeaf(YType.str, 'ready'), ['str'])),
                                    ('available', (YLeaf(YType.str, 'available'), ['str'])),
                                ])
                                self.job_id_xr = None
                                self.process_id = None
                                self.process_name = None
                                self.executable = None
                                self.active_path = None
                                self.instance_id = None
                                self.args = None
                                self.version_id = None
                                self.respawn = None
                                self.respawn_count = None
                                self.last_started = None
                                self.process_state = None
                                self.last_exit_status = None
                                self.last_exit_reason = None
                                self.package_state = None
                                self.started_on_config = None
                                self.feature_name = None
                                self.tag = None
                                self.group = None
                                self.core = None
                                self.max_core = None
                                self.level = None
                                self.mandatory = None
                                self.maint_mode_proc = None
                                self.placement_state = None
                                self.start_up_path = None
                                self.memory_limit = None
                                self.ready = None
                                self.available = None

                                self.proc_cpu_time = SystemProcess.NodeTable.Node.Name.ProcessNameDetails.ProcessNameDetail.BasicInfo.ProcCpuTime()
                                self.proc_cpu_time.parent = self
                                self._children_name_map["proc_cpu_time"] = "proc-cpu-time"

                                self.registered_item = YList(self)
                                self._segment_path = lambda: "basic-info"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(SystemProcess.NodeTable.Node.Name.ProcessNameDetails.ProcessNameDetail.BasicInfo, ['job_id_xr', 'process_id', 'process_name', 'executable', 'active_path', 'instance_id', 'args', 'version_id', 'respawn', 'respawn_count', 'last_started', 'process_state', 'last_exit_status', 'last_exit_reason', 'package_state', 'started_on_config', 'feature_name', 'tag', 'group', 'core', 'max_core', 'level', 'mandatory', 'maint_mode_proc', 'placement_state', 'start_up_path', 'memory_limit', 'ready', 'available'], name, value)


                            class ProcCpuTime(_Entity_):
                                """
                                Proces cpu time
                                
                                .. attribute:: user
                                
                                	User time
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: system
                                
                                	Kernel time
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: total
                                
                                	Total time
                                	**type**\: str
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'sysmgr-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(SystemProcess.NodeTable.Node.Name.ProcessNameDetails.ProcessNameDetail.BasicInfo.ProcCpuTime, self).__init__()

                                    self.yang_name = "proc-cpu-time"
                                    self.yang_parent_name = "basic-info"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('user', (YLeaf(YType.str, 'user'), ['str'])),
                                        ('system', (YLeaf(YType.str, 'system'), ['str'])),
                                        ('total', (YLeaf(YType.str, 'total'), ['str'])),
                                    ])
                                    self.user = None
                                    self.system = None
                                    self.total = None
                                    self._segment_path = lambda: "proc-cpu-time"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(SystemProcess.NodeTable.Node.Name.ProcessNameDetails.ProcessNameDetail.BasicInfo.ProcCpuTime, ['user', 'system', 'total'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
                                    return meta._meta_table['SystemProcess.NodeTable.Node.Name.ProcessNameDetails.ProcessNameDetail.BasicInfo.ProcCpuTime']['meta_info']


                            class RegisteredItem(_Entity_):
                                """
                                Registered Items
                                
                                .. attribute:: tuple
                                
                                	Tuple
                                	**type**\: str
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'sysmgr-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(SystemProcess.NodeTable.Node.Name.ProcessNameDetails.ProcessNameDetail.BasicInfo.RegisteredItem, self).__init__()

                                    self.yang_name = "registered-item"
                                    self.yang_parent_name = "basic-info"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('tuple', (YLeaf(YType.str, 'tuple'), ['str'])),
                                    ])
                                    self.tuple = None
                                    self._segment_path = lambda: "registered-item"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(SystemProcess.NodeTable.Node.Name.ProcessNameDetails.ProcessNameDetail.BasicInfo.RegisteredItem, ['tuple'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
                                    return meta._meta_table['SystemProcess.NodeTable.Node.Name.ProcessNameDetails.ProcessNameDetail.BasicInfo.RegisteredItem']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
                                return meta._meta_table['SystemProcess.NodeTable.Node.Name.ProcessNameDetails.ProcessNameDetail.BasicInfo']['meta_info']


                        class DetailInfo(_Entity_):
                            """
                            Process Detail Info
                            
                            .. attribute:: running_path
                            
                            	Running path
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: package_path
                            
                            	Package path
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: job_id_link
                            
                            	Job Id Link
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: group_jid
                            
                            	Group Jid
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: fail_count
                            
                            	Fail count
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: restart_needed
                            
                            	Restart needed
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: init_process
                            
                            	Init process
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: last_online
                            
                            	Last Online
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: this_pcb
                            
                            	This PCB
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: next_pcb
                            
                            	Next PCB
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: envs
                            
                            	Env variables
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: wait_for
                            
                            	Wait For /dev/xxx
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: job_id_on_rp
                            
                            	Job ID on RP
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: is_standby_capable
                            
                            	Is standby capable?
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: disable_kill
                            
                            	Disable kill?
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: send_avail
                            
                            	Check avail
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: node_event_cli_info
                            
                            	Node Event CLI info
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: node_redundancy_state
                            
                            	Node redundancy state
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: role_event_cli_info
                            
                            	Role event cli info
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: proc_role_state
                            
                            	Proc Role State
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: standby_event_cli_info
                            
                            	Standby Event CLI info
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: cleanup_event_cli_info
                            
                            	Cleanup event CLI info
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: band_ready_event_cli_info
                            
                            	Band Ready Event CLI Info
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: lr_event_cli_info
                            
                            	LR Event CLI Info
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: plane_ready_event_cli_info
                            
                            	Plane Ready Event CLI info
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: mdr_is_done_cli_info
                            
                            	MDR is done CLI Info
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'sysmgr-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(SystemProcess.NodeTable.Node.Name.ProcessNameDetails.ProcessNameDetail.DetailInfo, self).__init__()

                                self.yang_name = "detail-info"
                                self.yang_parent_name = "process-name-detail"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('running_path', (YLeaf(YType.str, 'running-path'), ['str'])),
                                    ('package_path', (YLeaf(YType.str, 'package-path'), ['str'])),
                                    ('job_id_link', (YLeaf(YType.int32, 'job-id-link'), ['int'])),
                                    ('group_jid', (YLeaf(YType.str, 'group-jid'), ['str'])),
                                    ('fail_count', (YLeaf(YType.uint32, 'fail-count'), ['int'])),
                                    ('restart_needed', (YLeaf(YType.boolean, 'restart-needed'), ['bool'])),
                                    ('init_process', (YLeaf(YType.boolean, 'init-process'), ['bool'])),
                                    ('last_online', (YLeaf(YType.str, 'last-online'), ['str'])),
                                    ('this_pcb', (YLeaf(YType.str, 'this-pcb'), ['str'])),
                                    ('next_pcb', (YLeaf(YType.str, 'next-pcb'), ['str'])),
                                    ('envs', (YLeaf(YType.str, 'envs'), ['str'])),
                                    ('wait_for', (YLeaf(YType.str, 'wait-for'), ['str'])),
                                    ('job_id_on_rp', (YLeaf(YType.int32, 'job-id-on-rp'), ['int'])),
                                    ('is_standby_capable', (YLeaf(YType.boolean, 'is-standby-capable'), ['bool'])),
                                    ('disable_kill', (YLeaf(YType.boolean, 'disable-kill'), ['bool'])),
                                    ('send_avail', (YLeaf(YType.boolean, 'send-avail'), ['bool'])),
                                    ('node_event_cli_info', (YLeaf(YType.int32, 'node-event-cli-info'), ['int'])),
                                    ('node_redundancy_state', (YLeaf(YType.str, 'node-redundancy-state'), ['str'])),
                                    ('role_event_cli_info', (YLeaf(YType.int32, 'role-event-cli-info'), ['int'])),
                                    ('proc_role_state', (YLeaf(YType.str, 'proc-role-state'), ['str'])),
                                    ('standby_event_cli_info', (YLeaf(YType.int32, 'standby-event-cli-info'), ['int'])),
                                    ('cleanup_event_cli_info', (YLeaf(YType.int32, 'cleanup-event-cli-info'), ['int'])),
                                    ('band_ready_event_cli_info', (YLeaf(YType.int32, 'band-ready-event-cli-info'), ['int'])),
                                    ('lr_event_cli_info', (YLeaf(YType.int32, 'lr-event-cli-info'), ['int'])),
                                    ('plane_ready_event_cli_info', (YLeaf(YType.int32, 'plane-ready-event-cli-info'), ['int'])),
                                    ('mdr_is_done_cli_info', (YLeaf(YType.int32, 'mdr-is-done-cli-info'), ['int'])),
                                ])
                                self.running_path = None
                                self.package_path = None
                                self.job_id_link = None
                                self.group_jid = None
                                self.fail_count = None
                                self.restart_needed = None
                                self.init_process = None
                                self.last_online = None
                                self.this_pcb = None
                                self.next_pcb = None
                                self.envs = None
                                self.wait_for = None
                                self.job_id_on_rp = None
                                self.is_standby_capable = None
                                self.disable_kill = None
                                self.send_avail = None
                                self.node_event_cli_info = None
                                self.node_redundancy_state = None
                                self.role_event_cli_info = None
                                self.proc_role_state = None
                                self.standby_event_cli_info = None
                                self.cleanup_event_cli_info = None
                                self.band_ready_event_cli_info = None
                                self.lr_event_cli_info = None
                                self.plane_ready_event_cli_info = None
                                self.mdr_is_done_cli_info = None
                                self._segment_path = lambda: "detail-info"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(SystemProcess.NodeTable.Node.Name.ProcessNameDetails.ProcessNameDetail.DetailInfo, ['running_path', 'package_path', 'job_id_link', 'group_jid', 'fail_count', 'restart_needed', 'init_process', 'last_online', 'this_pcb', 'next_pcb', 'envs', 'wait_for', 'job_id_on_rp', 'is_standby_capable', 'disable_kill', 'send_avail', 'node_event_cli_info', 'node_redundancy_state', 'role_event_cli_info', 'proc_role_state', 'standby_event_cli_info', 'cleanup_event_cli_info', 'band_ready_event_cli_info', 'lr_event_cli_info', 'plane_ready_event_cli_info', 'mdr_is_done_cli_info'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
                                return meta._meta_table['SystemProcess.NodeTable.Node.Name.ProcessNameDetails.ProcessNameDetail.DetailInfo']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
                            return meta._meta_table['SystemProcess.NodeTable.Node.Name.ProcessNameDetails.ProcessNameDetail']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
                        return meta._meta_table['SystemProcess.NodeTable.Node.Name.ProcessNameDetails']['meta_info']


                class ProcessNameVerboses(_Entity_):
                    """
                    Process <WORD> information
                    
                    .. attribute:: process_name_verbose
                    
                    	Process <WORD> verbose information
                    	**type**\: list of  		 :py:class:`ProcessNameVerbose <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.SystemProcess.NodeTable.Node.Name.ProcessNameVerboses.ProcessNameVerbose>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'sysmgr-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(SystemProcess.NodeTable.Node.Name.ProcessNameVerboses, self).__init__()

                        self.yang_name = "process-name-verboses"
                        self.yang_parent_name = "name"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("process-name-verbose", ("process_name_verbose", SystemProcess.NodeTable.Node.Name.ProcessNameVerboses.ProcessNameVerbose))])
                        self._leafs = OrderedDict()

                        self.process_name_verbose = YList(self)
                        self._segment_path = lambda: "process-name-verboses"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(SystemProcess.NodeTable.Node.Name.ProcessNameVerboses, [], name, value)


                    class ProcessNameVerbose(_Entity_):
                        """
                        Process <WORD> verbose information
                        
                        .. attribute:: proc_name  (key)
                        
                        	Process Name
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        	**config**\: False
                        
                        .. attribute:: basic_info
                        
                        	Process Basic Info
                        	**type**\:  :py:class:`BasicInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.SystemProcess.NodeTable.Node.Name.ProcessNameVerboses.ProcessNameVerbose.BasicInfo>`
                        
                        	**config**\: False
                        
                        .. attribute:: detail_info
                        
                        	Process Detail Info
                        	**type**\:  :py:class:`DetailInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.SystemProcess.NodeTable.Node.Name.ProcessNameVerboses.ProcessNameVerbose.DetailInfo>`
                        
                        	**config**\: False
                        
                        .. attribute:: verbose_info
                        
                        	Process Verbose Info
                        	**type**\:  :py:class:`VerboseInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.SystemProcess.NodeTable.Node.Name.ProcessNameVerboses.ProcessNameVerbose.VerboseInfo>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'sysmgr-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(SystemProcess.NodeTable.Node.Name.ProcessNameVerboses.ProcessNameVerbose, self).__init__()

                            self.yang_name = "process-name-verbose"
                            self.yang_parent_name = "process-name-verboses"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['proc_name']
                            self._child_classes = OrderedDict([("basic-info", ("basic_info", SystemProcess.NodeTable.Node.Name.ProcessNameVerboses.ProcessNameVerbose.BasicInfo)), ("detail-info", ("detail_info", SystemProcess.NodeTable.Node.Name.ProcessNameVerboses.ProcessNameVerbose.DetailInfo)), ("verbose-info", ("verbose_info", SystemProcess.NodeTable.Node.Name.ProcessNameVerboses.ProcessNameVerbose.VerboseInfo))])
                            self._leafs = OrderedDict([
                                ('proc_name', (YLeaf(YType.str, 'proc-name'), ['str'])),
                            ])
                            self.proc_name = None

                            self.basic_info = SystemProcess.NodeTable.Node.Name.ProcessNameVerboses.ProcessNameVerbose.BasicInfo()
                            self.basic_info.parent = self
                            self._children_name_map["basic_info"] = "basic-info"

                            self.detail_info = SystemProcess.NodeTable.Node.Name.ProcessNameVerboses.ProcessNameVerbose.DetailInfo()
                            self.detail_info.parent = self
                            self._children_name_map["detail_info"] = "detail-info"

                            self.verbose_info = SystemProcess.NodeTable.Node.Name.ProcessNameVerboses.ProcessNameVerbose.VerboseInfo()
                            self.verbose_info.parent = self
                            self._children_name_map["verbose_info"] = "verbose-info"
                            self._segment_path = lambda: "process-name-verbose" + "[proc-name='" + str(self.proc_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(SystemProcess.NodeTable.Node.Name.ProcessNameVerboses.ProcessNameVerbose, ['proc_name'], name, value)


                        class BasicInfo(_Entity_):
                            """
                            Process Basic Info
                            
                            .. attribute:: proc_cpu_time
                            
                            	Proces cpu time
                            	**type**\:  :py:class:`ProcCpuTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.SystemProcess.NodeTable.Node.Name.ProcessNameVerboses.ProcessNameVerbose.BasicInfo.ProcCpuTime>`
                            
                            	**config**\: False
                            
                            .. attribute:: job_id_xr
                            
                            	Job ID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: process_id
                            
                            	PID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: process_name
                            
                            	Process name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: executable
                            
                            	Executable name or path
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: active_path
                            
                            	Active Path
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: instance_id
                            
                            	Instance ID
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: args
                            
                            	Args
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: version_id
                            
                            	Version ID
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: respawn
                            
                            	Respawn on/off
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: respawn_count
                            
                            	Respawn Count
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: last_started
                            
                            	Last Started
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: process_state
                            
                            	Process State
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: last_exit_status
                            
                            	Last Exit status
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: last_exit_reason
                            
                            	Last Exit due to
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: package_state
                            
                            	Package State
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: started_on_config
                            
                            	Started on Config
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: feature_name
                            
                            	Feature Name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: tag
                            
                            	Tag
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: group
                            
                            	Process Group
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: core
                            
                            	Core
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: max_core
                            
                            	Max core
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: level
                            
                            	Level
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: mandatory
                            
                            	Is mandatory?
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: maint_mode_proc
                            
                            	Is admin mode process?
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: placement_state
                            
                            	Placement State
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: start_up_path
                            
                            	Startup Path
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: memory_limit
                            
                            	Memory Limit
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: ready
                            
                            	Elapsed Ready
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: available
                            
                            	Elapsed Available
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: registered_item
                            
                            	Registered Items
                            	**type**\: list of  		 :py:class:`RegisteredItem <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.SystemProcess.NodeTable.Node.Name.ProcessNameVerboses.ProcessNameVerbose.BasicInfo.RegisteredItem>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'sysmgr-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(SystemProcess.NodeTable.Node.Name.ProcessNameVerboses.ProcessNameVerbose.BasicInfo, self).__init__()

                                self.yang_name = "basic-info"
                                self.yang_parent_name = "process-name-verbose"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("proc-cpu-time", ("proc_cpu_time", SystemProcess.NodeTable.Node.Name.ProcessNameVerboses.ProcessNameVerbose.BasicInfo.ProcCpuTime)), ("registered-item", ("registered_item", SystemProcess.NodeTable.Node.Name.ProcessNameVerboses.ProcessNameVerbose.BasicInfo.RegisteredItem))])
                                self._leafs = OrderedDict([
                                    ('job_id_xr', (YLeaf(YType.uint32, 'job-id-xr'), ['int'])),
                                    ('process_id', (YLeaf(YType.uint32, 'process-id'), ['int'])),
                                    ('process_name', (YLeaf(YType.str, 'process-name'), ['str'])),
                                    ('executable', (YLeaf(YType.str, 'executable'), ['str'])),
                                    ('active_path', (YLeaf(YType.str, 'active-path'), ['str'])),
                                    ('instance_id', (YLeaf(YType.int32, 'instance-id'), ['int'])),
                                    ('args', (YLeaf(YType.str, 'args'), ['str'])),
                                    ('version_id', (YLeaf(YType.str, 'version-id'), ['str'])),
                                    ('respawn', (YLeaf(YType.str, 'respawn'), ['str'])),
                                    ('respawn_count', (YLeaf(YType.int32, 'respawn-count'), ['int'])),
                                    ('last_started', (YLeaf(YType.str, 'last-started'), ['str'])),
                                    ('process_state', (YLeaf(YType.str, 'process-state'), ['str'])),
                                    ('last_exit_status', (YLeaf(YType.int32, 'last-exit-status'), ['int'])),
                                    ('last_exit_reason', (YLeaf(YType.str, 'last-exit-reason'), ['str'])),
                                    ('package_state', (YLeaf(YType.str, 'package-state'), ['str'])),
                                    ('started_on_config', (YLeaf(YType.str, 'started-on-config'), ['str'])),
                                    ('feature_name', (YLeaf(YType.str, 'feature-name'), ['str'])),
                                    ('tag', (YLeaf(YType.str, 'tag'), ['str'])),
                                    ('group', (YLeaf(YType.str, 'group'), ['str'])),
                                    ('core', (YLeaf(YType.str, 'core'), ['str'])),
                                    ('max_core', (YLeaf(YType.int32, 'max-core'), ['int'])),
                                    ('level', (YLeaf(YType.str, 'level'), ['str'])),
                                    ('mandatory', (YLeaf(YType.boolean, 'mandatory'), ['bool'])),
                                    ('maint_mode_proc', (YLeaf(YType.boolean, 'maint-mode-proc'), ['bool'])),
                                    ('placement_state', (YLeaf(YType.str, 'placement-state'), ['str'])),
                                    ('start_up_path', (YLeaf(YType.str, 'start-up-path'), ['str'])),
                                    ('memory_limit', (YLeaf(YType.uint32, 'memory-limit'), ['int'])),
                                    ('ready', (YLeaf(YType.str, 'ready'), ['str'])),
                                    ('available', (YLeaf(YType.str, 'available'), ['str'])),
                                ])
                                self.job_id_xr = None
                                self.process_id = None
                                self.process_name = None
                                self.executable = None
                                self.active_path = None
                                self.instance_id = None
                                self.args = None
                                self.version_id = None
                                self.respawn = None
                                self.respawn_count = None
                                self.last_started = None
                                self.process_state = None
                                self.last_exit_status = None
                                self.last_exit_reason = None
                                self.package_state = None
                                self.started_on_config = None
                                self.feature_name = None
                                self.tag = None
                                self.group = None
                                self.core = None
                                self.max_core = None
                                self.level = None
                                self.mandatory = None
                                self.maint_mode_proc = None
                                self.placement_state = None
                                self.start_up_path = None
                                self.memory_limit = None
                                self.ready = None
                                self.available = None

                                self.proc_cpu_time = SystemProcess.NodeTable.Node.Name.ProcessNameVerboses.ProcessNameVerbose.BasicInfo.ProcCpuTime()
                                self.proc_cpu_time.parent = self
                                self._children_name_map["proc_cpu_time"] = "proc-cpu-time"

                                self.registered_item = YList(self)
                                self._segment_path = lambda: "basic-info"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(SystemProcess.NodeTable.Node.Name.ProcessNameVerboses.ProcessNameVerbose.BasicInfo, ['job_id_xr', 'process_id', 'process_name', 'executable', 'active_path', 'instance_id', 'args', 'version_id', 'respawn', 'respawn_count', 'last_started', 'process_state', 'last_exit_status', 'last_exit_reason', 'package_state', 'started_on_config', 'feature_name', 'tag', 'group', 'core', 'max_core', 'level', 'mandatory', 'maint_mode_proc', 'placement_state', 'start_up_path', 'memory_limit', 'ready', 'available'], name, value)


                            class ProcCpuTime(_Entity_):
                                """
                                Proces cpu time
                                
                                .. attribute:: user
                                
                                	User time
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: system
                                
                                	Kernel time
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: total
                                
                                	Total time
                                	**type**\: str
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'sysmgr-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(SystemProcess.NodeTable.Node.Name.ProcessNameVerboses.ProcessNameVerbose.BasicInfo.ProcCpuTime, self).__init__()

                                    self.yang_name = "proc-cpu-time"
                                    self.yang_parent_name = "basic-info"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('user', (YLeaf(YType.str, 'user'), ['str'])),
                                        ('system', (YLeaf(YType.str, 'system'), ['str'])),
                                        ('total', (YLeaf(YType.str, 'total'), ['str'])),
                                    ])
                                    self.user = None
                                    self.system = None
                                    self.total = None
                                    self._segment_path = lambda: "proc-cpu-time"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(SystemProcess.NodeTable.Node.Name.ProcessNameVerboses.ProcessNameVerbose.BasicInfo.ProcCpuTime, ['user', 'system', 'total'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
                                    return meta._meta_table['SystemProcess.NodeTable.Node.Name.ProcessNameVerboses.ProcessNameVerbose.BasicInfo.ProcCpuTime']['meta_info']


                            class RegisteredItem(_Entity_):
                                """
                                Registered Items
                                
                                .. attribute:: tuple
                                
                                	Tuple
                                	**type**\: str
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'sysmgr-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(SystemProcess.NodeTable.Node.Name.ProcessNameVerboses.ProcessNameVerbose.BasicInfo.RegisteredItem, self).__init__()

                                    self.yang_name = "registered-item"
                                    self.yang_parent_name = "basic-info"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('tuple', (YLeaf(YType.str, 'tuple'), ['str'])),
                                    ])
                                    self.tuple = None
                                    self._segment_path = lambda: "registered-item"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(SystemProcess.NodeTable.Node.Name.ProcessNameVerboses.ProcessNameVerbose.BasicInfo.RegisteredItem, ['tuple'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
                                    return meta._meta_table['SystemProcess.NodeTable.Node.Name.ProcessNameVerboses.ProcessNameVerbose.BasicInfo.RegisteredItem']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
                                return meta._meta_table['SystemProcess.NodeTable.Node.Name.ProcessNameVerboses.ProcessNameVerbose.BasicInfo']['meta_info']


                        class DetailInfo(_Entity_):
                            """
                            Process Detail Info
                            
                            .. attribute:: running_path
                            
                            	Running path
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: package_path
                            
                            	Package path
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: job_id_link
                            
                            	Job Id Link
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: group_jid
                            
                            	Group Jid
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: fail_count
                            
                            	Fail count
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: restart_needed
                            
                            	Restart needed
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: init_process
                            
                            	Init process
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: last_online
                            
                            	Last Online
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: this_pcb
                            
                            	This PCB
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: next_pcb
                            
                            	Next PCB
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: envs
                            
                            	Env variables
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: wait_for
                            
                            	Wait For /dev/xxx
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: job_id_on_rp
                            
                            	Job ID on RP
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: is_standby_capable
                            
                            	Is standby capable?
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: disable_kill
                            
                            	Disable kill?
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: send_avail
                            
                            	Check avail
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: node_event_cli_info
                            
                            	Node Event CLI info
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: node_redundancy_state
                            
                            	Node redundancy state
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: role_event_cli_info
                            
                            	Role event cli info
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: proc_role_state
                            
                            	Proc Role State
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: standby_event_cli_info
                            
                            	Standby Event CLI info
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: cleanup_event_cli_info
                            
                            	Cleanup event CLI info
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: band_ready_event_cli_info
                            
                            	Band Ready Event CLI Info
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: lr_event_cli_info
                            
                            	LR Event CLI Info
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: plane_ready_event_cli_info
                            
                            	Plane Ready Event CLI info
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: mdr_is_done_cli_info
                            
                            	MDR is done CLI Info
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'sysmgr-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(SystemProcess.NodeTable.Node.Name.ProcessNameVerboses.ProcessNameVerbose.DetailInfo, self).__init__()

                                self.yang_name = "detail-info"
                                self.yang_parent_name = "process-name-verbose"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('running_path', (YLeaf(YType.str, 'running-path'), ['str'])),
                                    ('package_path', (YLeaf(YType.str, 'package-path'), ['str'])),
                                    ('job_id_link', (YLeaf(YType.int32, 'job-id-link'), ['int'])),
                                    ('group_jid', (YLeaf(YType.str, 'group-jid'), ['str'])),
                                    ('fail_count', (YLeaf(YType.uint32, 'fail-count'), ['int'])),
                                    ('restart_needed', (YLeaf(YType.boolean, 'restart-needed'), ['bool'])),
                                    ('init_process', (YLeaf(YType.boolean, 'init-process'), ['bool'])),
                                    ('last_online', (YLeaf(YType.str, 'last-online'), ['str'])),
                                    ('this_pcb', (YLeaf(YType.str, 'this-pcb'), ['str'])),
                                    ('next_pcb', (YLeaf(YType.str, 'next-pcb'), ['str'])),
                                    ('envs', (YLeaf(YType.str, 'envs'), ['str'])),
                                    ('wait_for', (YLeaf(YType.str, 'wait-for'), ['str'])),
                                    ('job_id_on_rp', (YLeaf(YType.int32, 'job-id-on-rp'), ['int'])),
                                    ('is_standby_capable', (YLeaf(YType.boolean, 'is-standby-capable'), ['bool'])),
                                    ('disable_kill', (YLeaf(YType.boolean, 'disable-kill'), ['bool'])),
                                    ('send_avail', (YLeaf(YType.boolean, 'send-avail'), ['bool'])),
                                    ('node_event_cli_info', (YLeaf(YType.int32, 'node-event-cli-info'), ['int'])),
                                    ('node_redundancy_state', (YLeaf(YType.str, 'node-redundancy-state'), ['str'])),
                                    ('role_event_cli_info', (YLeaf(YType.int32, 'role-event-cli-info'), ['int'])),
                                    ('proc_role_state', (YLeaf(YType.str, 'proc-role-state'), ['str'])),
                                    ('standby_event_cli_info', (YLeaf(YType.int32, 'standby-event-cli-info'), ['int'])),
                                    ('cleanup_event_cli_info', (YLeaf(YType.int32, 'cleanup-event-cli-info'), ['int'])),
                                    ('band_ready_event_cli_info', (YLeaf(YType.int32, 'band-ready-event-cli-info'), ['int'])),
                                    ('lr_event_cli_info', (YLeaf(YType.int32, 'lr-event-cli-info'), ['int'])),
                                    ('plane_ready_event_cli_info', (YLeaf(YType.int32, 'plane-ready-event-cli-info'), ['int'])),
                                    ('mdr_is_done_cli_info', (YLeaf(YType.int32, 'mdr-is-done-cli-info'), ['int'])),
                                ])
                                self.running_path = None
                                self.package_path = None
                                self.job_id_link = None
                                self.group_jid = None
                                self.fail_count = None
                                self.restart_needed = None
                                self.init_process = None
                                self.last_online = None
                                self.this_pcb = None
                                self.next_pcb = None
                                self.envs = None
                                self.wait_for = None
                                self.job_id_on_rp = None
                                self.is_standby_capable = None
                                self.disable_kill = None
                                self.send_avail = None
                                self.node_event_cli_info = None
                                self.node_redundancy_state = None
                                self.role_event_cli_info = None
                                self.proc_role_state = None
                                self.standby_event_cli_info = None
                                self.cleanup_event_cli_info = None
                                self.band_ready_event_cli_info = None
                                self.lr_event_cli_info = None
                                self.plane_ready_event_cli_info = None
                                self.mdr_is_done_cli_info = None
                                self._segment_path = lambda: "detail-info"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(SystemProcess.NodeTable.Node.Name.ProcessNameVerboses.ProcessNameVerbose.DetailInfo, ['running_path', 'package_path', 'job_id_link', 'group_jid', 'fail_count', 'restart_needed', 'init_process', 'last_online', 'this_pcb', 'next_pcb', 'envs', 'wait_for', 'job_id_on_rp', 'is_standby_capable', 'disable_kill', 'send_avail', 'node_event_cli_info', 'node_redundancy_state', 'role_event_cli_info', 'proc_role_state', 'standby_event_cli_info', 'cleanup_event_cli_info', 'band_ready_event_cli_info', 'lr_event_cli_info', 'plane_ready_event_cli_info', 'mdr_is_done_cli_info'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
                                return meta._meta_table['SystemProcess.NodeTable.Node.Name.ProcessNameVerboses.ProcessNameVerbose.DetailInfo']['meta_info']


                        class VerboseInfo(_Entity_):
                            """
                            Process Verbose Info
                            
                            .. attribute:: process_group
                            
                            	Process Group
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: respawn_allowed
                            
                            	Is respawn allowed?
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: wait_for_exit
                            
                            	Wait for exit
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: dynamic_tag
                            
                            	Dynamic Tag
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: forced_stop
                            
                            	Forced stop
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: critical_process
                            
                            	Critical Process
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: hold
                            
                            	Hold
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: transient
                            
                            	Transient
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: tuple_cfgmgr
                            
                            	Tuple Cfgmgr
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: standby_capable
                            
                            	Standby capable
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: edm_startup
                            
                            	EDM startup
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: placement
                            
                            	Placement
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: skip_kill_notif
                            
                            	Skip Kill Notif
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: init_proc
                            
                            	Init process
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: sysdb_event
                            
                            	Sysdb Event
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: level_started
                            
                            	Level Started
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: proc_avail
                            
                            	Process available
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: tuples_scanned
                            
                            	Tuples Scanned
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: no_chkpt_start
                            
                            	No checkpoint start
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: in_shut_down
                            
                            	In Shut Down
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: sm_started
                            
                            	SM started
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: ignore_on_sc
                            
                            	Ignore on SC
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: ignore_on_easy_bake
                            
                            	Ignore on EasyBake
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: pre_init
                            
                            	Pre init
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: eoi_received
                            
                            	EOI received
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: eoi_timeout
                            
                            	EOI Timeout
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: avail_timeout
                            
                            	Avail Timeout
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: reserved_memory
                            
                            	Reserved Memory
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: allow_warned
                            
                            	Allow Warned
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: arg_change
                            
                            	Arg Change
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: restart_on_tuple
                            
                            	Restart on tuple
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: boot_hold
                            
                            	Boot Hold
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: reg_id
                            
                            	Reg Id
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: memory_limit
                            
                            	Memory Limit
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: parent_job_id
                            
                            	Parent Job ID
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: tuple_index
                            
                            	Tuple Index
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: dump_count
                            
                            	Dump Count
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: respawn_interval_user
                            
                            	Respawn Interval User
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: silent_restart_count
                            
                            	Silent Restart Count
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: critical_tier
                            
                            	Critical Tier
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: exit_type
                            
                            	Exit Type
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: init_timeout
                            
                            	Init Timeout
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: restart_by_cmd
                            
                            	Restart by Command
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: boot_pref
                            
                            	Boot Pref
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: mdr_mbi_proc
                            
                            	Mdr Mbi proc
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: mdr_non_mbi_kld
                            
                            	Mdr Non Mbi Kld
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: mdr_mbi_kld
                            
                            	Mdr Mbi Kld
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: mdr_shut_delay
                            
                            	Mdr Shut Delay
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: mdr_keep_thru
                            
                            	Mdr Keep Thru
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: mdr_spoofer
                            
                            	Mdr spoofer
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: mdr_spoofed
                            
                            	Mdr spoofed
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: mdr_spoofed_last
                            
                            	Mdr spoofed last
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: mdr_spoofed_ready
                            
                            	Mdr Spoofed Ready
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: mdr_pcb_check
                            
                            	Mdr PCB Check
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: mdr_kill_tier
                            
                            	Mdr Kill Tier
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: mdr_kld
                            
                            	Mdr kld
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: mdr_level
                            
                            	Mdr Level
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: fm_restart_cnt
                            
                            	FM restart count
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: self_managed
                            
                            	Self Managed
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: tuple
                            
                            	Tuple
                            	**type**\: list of  		 :py:class:`Tuple <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.SystemProcess.NodeTable.Node.Name.ProcessNameVerboses.ProcessNameVerbose.VerboseInfo.Tuple>`
                            
                            	**config**\: False
                            
                            .. attribute:: orig_tuple
                            
                            	Orig Tuple
                            	**type**\: list of  		 :py:class:`OrigTuple <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.SystemProcess.NodeTable.Node.Name.ProcessNameVerboses.ProcessNameVerbose.VerboseInfo.OrigTuple>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'sysmgr-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(SystemProcess.NodeTable.Node.Name.ProcessNameVerboses.ProcessNameVerbose.VerboseInfo, self).__init__()

                                self.yang_name = "verbose-info"
                                self.yang_parent_name = "process-name-verbose"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("tuple", ("tuple", SystemProcess.NodeTable.Node.Name.ProcessNameVerboses.ProcessNameVerbose.VerboseInfo.Tuple)), ("orig-tuple", ("orig_tuple", SystemProcess.NodeTable.Node.Name.ProcessNameVerboses.ProcessNameVerbose.VerboseInfo.OrigTuple))])
                                self._leafs = OrderedDict([
                                    ('process_group', (YLeaf(YType.str, 'process-group'), ['str'])),
                                    ('respawn_allowed', (YLeaf(YType.int32, 'respawn-allowed'), ['int'])),
                                    ('wait_for_exit', (YLeaf(YType.int32, 'wait-for-exit'), ['int'])),
                                    ('dynamic_tag', (YLeaf(YType.int32, 'dynamic-tag'), ['int'])),
                                    ('forced_stop', (YLeaf(YType.int32, 'forced-stop'), ['int'])),
                                    ('critical_process', (YLeaf(YType.int32, 'critical-process'), ['int'])),
                                    ('hold', (YLeaf(YType.int32, 'hold'), ['int'])),
                                    ('transient', (YLeaf(YType.int32, 'transient'), ['int'])),
                                    ('tuple_cfgmgr', (YLeaf(YType.int32, 'tuple-cfgmgr'), ['int'])),
                                    ('standby_capable', (YLeaf(YType.int32, 'standby-capable'), ['int'])),
                                    ('edm_startup', (YLeaf(YType.int32, 'edm-startup'), ['int'])),
                                    ('placement', (YLeaf(YType.int32, 'placement'), ['int'])),
                                    ('skip_kill_notif', (YLeaf(YType.int32, 'skip-kill-notif'), ['int'])),
                                    ('init_proc', (YLeaf(YType.int32, 'init-proc'), ['int'])),
                                    ('sysdb_event', (YLeaf(YType.int32, 'sysdb-event'), ['int'])),
                                    ('level_started', (YLeaf(YType.int32, 'level-started'), ['int'])),
                                    ('proc_avail', (YLeaf(YType.int32, 'proc-avail'), ['int'])),
                                    ('tuples_scanned', (YLeaf(YType.int32, 'tuples-scanned'), ['int'])),
                                    ('no_chkpt_start', (YLeaf(YType.int32, 'no-chkpt-start'), ['int'])),
                                    ('in_shut_down', (YLeaf(YType.int32, 'in-shut-down'), ['int'])),
                                    ('sm_started', (YLeaf(YType.int32, 'sm-started'), ['int'])),
                                    ('ignore_on_sc', (YLeaf(YType.int32, 'ignore-on-sc'), ['int'])),
                                    ('ignore_on_easy_bake', (YLeaf(YType.int32, 'ignore-on-easy-bake'), ['int'])),
                                    ('pre_init', (YLeaf(YType.int32, 'pre-init'), ['int'])),
                                    ('eoi_received', (YLeaf(YType.int32, 'eoi-received'), ['int'])),
                                    ('eoi_timeout', (YLeaf(YType.int32, 'eoi-timeout'), ['int'])),
                                    ('avail_timeout', (YLeaf(YType.int32, 'avail-timeout'), ['int'])),
                                    ('reserved_memory', (YLeaf(YType.int32, 'reserved-memory'), ['int'])),
                                    ('allow_warned', (YLeaf(YType.int32, 'allow-warned'), ['int'])),
                                    ('arg_change', (YLeaf(YType.int32, 'arg-change'), ['int'])),
                                    ('restart_on_tuple', (YLeaf(YType.int32, 'restart-on-tuple'), ['int'])),
                                    ('boot_hold', (YLeaf(YType.int32, 'boot-hold'), ['int'])),
                                    ('reg_id', (YLeaf(YType.int32, 'reg-id'), ['int'])),
                                    ('memory_limit', (YLeaf(YType.int32, 'memory-limit'), ['int'])),
                                    ('parent_job_id', (YLeaf(YType.int32, 'parent-job-id'), ['int'])),
                                    ('tuple_index', (YLeaf(YType.int32, 'tuple-index'), ['int'])),
                                    ('dump_count', (YLeaf(YType.int32, 'dump-count'), ['int'])),
                                    ('respawn_interval_user', (YLeaf(YType.int32, 'respawn-interval-user'), ['int'])),
                                    ('silent_restart_count', (YLeaf(YType.int32, 'silent-restart-count'), ['int'])),
                                    ('critical_tier', (YLeaf(YType.int32, 'critical-tier'), ['int'])),
                                    ('exit_type', (YLeaf(YType.int32, 'exit-type'), ['int'])),
                                    ('init_timeout', (YLeaf(YType.int32, 'init-timeout'), ['int'])),
                                    ('restart_by_cmd', (YLeaf(YType.int32, 'restart-by-cmd'), ['int'])),
                                    ('boot_pref', (YLeaf(YType.int32, 'boot-pref'), ['int'])),
                                    ('mdr_mbi_proc', (YLeaf(YType.int32, 'mdr-mbi-proc'), ['int'])),
                                    ('mdr_non_mbi_kld', (YLeaf(YType.int32, 'mdr-non-mbi-kld'), ['int'])),
                                    ('mdr_mbi_kld', (YLeaf(YType.int32, 'mdr-mbi-kld'), ['int'])),
                                    ('mdr_shut_delay', (YLeaf(YType.int32, 'mdr-shut-delay'), ['int'])),
                                    ('mdr_keep_thru', (YLeaf(YType.int32, 'mdr-keep-thru'), ['int'])),
                                    ('mdr_spoofer', (YLeaf(YType.int32, 'mdr-spoofer'), ['int'])),
                                    ('mdr_spoofed', (YLeaf(YType.int32, 'mdr-spoofed'), ['int'])),
                                    ('mdr_spoofed_last', (YLeaf(YType.int32, 'mdr-spoofed-last'), ['int'])),
                                    ('mdr_spoofed_ready', (YLeaf(YType.int32, 'mdr-spoofed-ready'), ['int'])),
                                    ('mdr_pcb_check', (YLeaf(YType.int32, 'mdr-pcb-check'), ['int'])),
                                    ('mdr_kill_tier', (YLeaf(YType.int32, 'mdr-kill-tier'), ['int'])),
                                    ('mdr_kld', (YLeaf(YType.int32, 'mdr-kld'), ['int'])),
                                    ('mdr_level', (YLeaf(YType.int32, 'mdr-level'), ['int'])),
                                    ('fm_restart_cnt', (YLeaf(YType.int32, 'fm-restart-cnt'), ['int'])),
                                    ('self_managed', (YLeaf(YType.int32, 'self-managed'), ['int'])),
                                ])
                                self.process_group = None
                                self.respawn_allowed = None
                                self.wait_for_exit = None
                                self.dynamic_tag = None
                                self.forced_stop = None
                                self.critical_process = None
                                self.hold = None
                                self.transient = None
                                self.tuple_cfgmgr = None
                                self.standby_capable = None
                                self.edm_startup = None
                                self.placement = None
                                self.skip_kill_notif = None
                                self.init_proc = None
                                self.sysdb_event = None
                                self.level_started = None
                                self.proc_avail = None
                                self.tuples_scanned = None
                                self.no_chkpt_start = None
                                self.in_shut_down = None
                                self.sm_started = None
                                self.ignore_on_sc = None
                                self.ignore_on_easy_bake = None
                                self.pre_init = None
                                self.eoi_received = None
                                self.eoi_timeout = None
                                self.avail_timeout = None
                                self.reserved_memory = None
                                self.allow_warned = None
                                self.arg_change = None
                                self.restart_on_tuple = None
                                self.boot_hold = None
                                self.reg_id = None
                                self.memory_limit = None
                                self.parent_job_id = None
                                self.tuple_index = None
                                self.dump_count = None
                                self.respawn_interval_user = None
                                self.silent_restart_count = None
                                self.critical_tier = None
                                self.exit_type = None
                                self.init_timeout = None
                                self.restart_by_cmd = None
                                self.boot_pref = None
                                self.mdr_mbi_proc = None
                                self.mdr_non_mbi_kld = None
                                self.mdr_mbi_kld = None
                                self.mdr_shut_delay = None
                                self.mdr_keep_thru = None
                                self.mdr_spoofer = None
                                self.mdr_spoofed = None
                                self.mdr_spoofed_last = None
                                self.mdr_spoofed_ready = None
                                self.mdr_pcb_check = None
                                self.mdr_kill_tier = None
                                self.mdr_kld = None
                                self.mdr_level = None
                                self.fm_restart_cnt = None
                                self.self_managed = None

                                self.tuple = YList(self)
                                self.orig_tuple = YList(self)
                                self._segment_path = lambda: "verbose-info"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(SystemProcess.NodeTable.Node.Name.ProcessNameVerboses.ProcessNameVerbose.VerboseInfo, ['process_group', 'respawn_allowed', 'wait_for_exit', 'dynamic_tag', 'forced_stop', 'critical_process', 'hold', 'transient', 'tuple_cfgmgr', 'standby_capable', 'edm_startup', 'placement', 'skip_kill_notif', 'init_proc', 'sysdb_event', 'level_started', 'proc_avail', 'tuples_scanned', 'no_chkpt_start', 'in_shut_down', 'sm_started', 'ignore_on_sc', 'ignore_on_easy_bake', 'pre_init', 'eoi_received', 'eoi_timeout', 'avail_timeout', 'reserved_memory', 'allow_warned', 'arg_change', 'restart_on_tuple', 'boot_hold', 'reg_id', 'memory_limit', 'parent_job_id', 'tuple_index', 'dump_count', 'respawn_interval_user', 'silent_restart_count', 'critical_tier', 'exit_type', 'init_timeout', 'restart_by_cmd', 'boot_pref', 'mdr_mbi_proc', 'mdr_non_mbi_kld', 'mdr_mbi_kld', 'mdr_shut_delay', 'mdr_keep_thru', 'mdr_spoofer', 'mdr_spoofed', 'mdr_spoofed_last', 'mdr_spoofed_ready', 'mdr_pcb_check', 'mdr_kill_tier', 'mdr_kld', 'mdr_level', 'fm_restart_cnt', 'self_managed'], name, value)


                            class Tuple(_Entity_):
                                """
                                Tuple
                                
                                .. attribute:: tuple
                                
                                	Tuple
                                	**type**\: str
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'sysmgr-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(SystemProcess.NodeTable.Node.Name.ProcessNameVerboses.ProcessNameVerbose.VerboseInfo.Tuple, self).__init__()

                                    self.yang_name = "tuple"
                                    self.yang_parent_name = "verbose-info"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('tuple', (YLeaf(YType.str, 'tuple'), ['str'])),
                                    ])
                                    self.tuple = None
                                    self._segment_path = lambda: "tuple"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(SystemProcess.NodeTable.Node.Name.ProcessNameVerboses.ProcessNameVerbose.VerboseInfo.Tuple, ['tuple'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
                                    return meta._meta_table['SystemProcess.NodeTable.Node.Name.ProcessNameVerboses.ProcessNameVerbose.VerboseInfo.Tuple']['meta_info']


                            class OrigTuple(_Entity_):
                                """
                                Orig Tuple
                                
                                .. attribute:: tuple
                                
                                	Tuple
                                	**type**\: str
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'sysmgr-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(SystemProcess.NodeTable.Node.Name.ProcessNameVerboses.ProcessNameVerbose.VerboseInfo.OrigTuple, self).__init__()

                                    self.yang_name = "orig-tuple"
                                    self.yang_parent_name = "verbose-info"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('tuple', (YLeaf(YType.str, 'tuple'), ['str'])),
                                    ])
                                    self.tuple = None
                                    self._segment_path = lambda: "orig-tuple"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(SystemProcess.NodeTable.Node.Name.ProcessNameVerboses.ProcessNameVerbose.VerboseInfo.OrigTuple, ['tuple'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
                                    return meta._meta_table['SystemProcess.NodeTable.Node.Name.ProcessNameVerboses.ProcessNameVerbose.VerboseInfo.OrigTuple']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
                                return meta._meta_table['SystemProcess.NodeTable.Node.Name.ProcessNameVerboses.ProcessNameVerbose.VerboseInfo']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
                            return meta._meta_table['SystemProcess.NodeTable.Node.Name.ProcessNameVerboses.ProcessNameVerbose']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
                        return meta._meta_table['SystemProcess.NodeTable.Node.Name.ProcessNameVerboses']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
                    return meta._meta_table['SystemProcess.NodeTable.Node.Name']['meta_info']


            class Jids(_Entity_):
                """
                Process job id information
                
                .. attribute:: jid
                
                	Process <jid> information
                	**type**\: list of  		 :py:class:`Jid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.SystemProcess.NodeTable.Node.Jids.Jid>`
                
                	**config**\: False
                
                

                """

                _prefix = 'sysmgr-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(SystemProcess.NodeTable.Node.Jids, self).__init__()

                    self.yang_name = "jids"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("jid", ("jid", SystemProcess.NodeTable.Node.Jids.Jid))])
                    self._leafs = OrderedDict()

                    self.jid = YList(self)
                    self._segment_path = lambda: "jids"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(SystemProcess.NodeTable.Node.Jids, [], name, value)


                class Jid(_Entity_):
                    """
                    Process <jid> information
                    
                    .. attribute:: job_id  (key)
                    
                    	Job ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: proc_cpu_time
                    
                    	Proces cpu time
                    	**type**\:  :py:class:`ProcCpuTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.SystemProcess.NodeTable.Node.Jids.Jid.ProcCpuTime>`
                    
                    	**config**\: False
                    
                    .. attribute:: job_id_xr
                    
                    	Job ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: process_id
                    
                    	PID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: process_name
                    
                    	Process name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: executable
                    
                    	Executable name or path
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: active_path
                    
                    	Active Path
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: instance_id
                    
                    	Instance ID
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**config**\: False
                    
                    .. attribute:: args
                    
                    	Args
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: version_id
                    
                    	Version ID
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: respawn
                    
                    	Respawn on/off
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: respawn_count
                    
                    	Respawn Count
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**config**\: False
                    
                    .. attribute:: last_started
                    
                    	Last Started
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: process_state
                    
                    	Process State
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: last_exit_status
                    
                    	Last Exit status
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**config**\: False
                    
                    .. attribute:: last_exit_reason
                    
                    	Last Exit due to
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: package_state
                    
                    	Package State
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: started_on_config
                    
                    	Started on Config
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: feature_name
                    
                    	Feature Name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: tag
                    
                    	Tag
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: group
                    
                    	Process Group
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: core
                    
                    	Core
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: max_core
                    
                    	Max core
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**config**\: False
                    
                    .. attribute:: level
                    
                    	Level
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: mandatory
                    
                    	Is mandatory?
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: maint_mode_proc
                    
                    	Is admin mode process?
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: placement_state
                    
                    	Placement State
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: start_up_path
                    
                    	Startup Path
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: memory_limit
                    
                    	Memory Limit
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: ready
                    
                    	Elapsed Ready
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: available
                    
                    	Elapsed Available
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: registered_item
                    
                    	Registered Items
                    	**type**\: list of  		 :py:class:`RegisteredItem <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.SystemProcess.NodeTable.Node.Jids.Jid.RegisteredItem>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'sysmgr-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(SystemProcess.NodeTable.Node.Jids.Jid, self).__init__()

                        self.yang_name = "jid"
                        self.yang_parent_name = "jids"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['job_id']
                        self._child_classes = OrderedDict([("proc-cpu-time", ("proc_cpu_time", SystemProcess.NodeTable.Node.Jids.Jid.ProcCpuTime)), ("registered-item", ("registered_item", SystemProcess.NodeTable.Node.Jids.Jid.RegisteredItem))])
                        self._leafs = OrderedDict([
                            ('job_id', (YLeaf(YType.uint32, 'job-id'), ['int'])),
                            ('job_id_xr', (YLeaf(YType.uint32, 'job-id-xr'), ['int'])),
                            ('process_id', (YLeaf(YType.uint32, 'process-id'), ['int'])),
                            ('process_name', (YLeaf(YType.str, 'process-name'), ['str'])),
                            ('executable', (YLeaf(YType.str, 'executable'), ['str'])),
                            ('active_path', (YLeaf(YType.str, 'active-path'), ['str'])),
                            ('instance_id', (YLeaf(YType.int32, 'instance-id'), ['int'])),
                            ('args', (YLeaf(YType.str, 'args'), ['str'])),
                            ('version_id', (YLeaf(YType.str, 'version-id'), ['str'])),
                            ('respawn', (YLeaf(YType.str, 'respawn'), ['str'])),
                            ('respawn_count', (YLeaf(YType.int32, 'respawn-count'), ['int'])),
                            ('last_started', (YLeaf(YType.str, 'last-started'), ['str'])),
                            ('process_state', (YLeaf(YType.str, 'process-state'), ['str'])),
                            ('last_exit_status', (YLeaf(YType.int32, 'last-exit-status'), ['int'])),
                            ('last_exit_reason', (YLeaf(YType.str, 'last-exit-reason'), ['str'])),
                            ('package_state', (YLeaf(YType.str, 'package-state'), ['str'])),
                            ('started_on_config', (YLeaf(YType.str, 'started-on-config'), ['str'])),
                            ('feature_name', (YLeaf(YType.str, 'feature-name'), ['str'])),
                            ('tag', (YLeaf(YType.str, 'tag'), ['str'])),
                            ('group', (YLeaf(YType.str, 'group'), ['str'])),
                            ('core', (YLeaf(YType.str, 'core'), ['str'])),
                            ('max_core', (YLeaf(YType.int32, 'max-core'), ['int'])),
                            ('level', (YLeaf(YType.str, 'level'), ['str'])),
                            ('mandatory', (YLeaf(YType.boolean, 'mandatory'), ['bool'])),
                            ('maint_mode_proc', (YLeaf(YType.boolean, 'maint-mode-proc'), ['bool'])),
                            ('placement_state', (YLeaf(YType.str, 'placement-state'), ['str'])),
                            ('start_up_path', (YLeaf(YType.str, 'start-up-path'), ['str'])),
                            ('memory_limit', (YLeaf(YType.uint32, 'memory-limit'), ['int'])),
                            ('ready', (YLeaf(YType.str, 'ready'), ['str'])),
                            ('available', (YLeaf(YType.str, 'available'), ['str'])),
                        ])
                        self.job_id = None
                        self.job_id_xr = None
                        self.process_id = None
                        self.process_name = None
                        self.executable = None
                        self.active_path = None
                        self.instance_id = None
                        self.args = None
                        self.version_id = None
                        self.respawn = None
                        self.respawn_count = None
                        self.last_started = None
                        self.process_state = None
                        self.last_exit_status = None
                        self.last_exit_reason = None
                        self.package_state = None
                        self.started_on_config = None
                        self.feature_name = None
                        self.tag = None
                        self.group = None
                        self.core = None
                        self.max_core = None
                        self.level = None
                        self.mandatory = None
                        self.maint_mode_proc = None
                        self.placement_state = None
                        self.start_up_path = None
                        self.memory_limit = None
                        self.ready = None
                        self.available = None

                        self.proc_cpu_time = SystemProcess.NodeTable.Node.Jids.Jid.ProcCpuTime()
                        self.proc_cpu_time.parent = self
                        self._children_name_map["proc_cpu_time"] = "proc-cpu-time"

                        self.registered_item = YList(self)
                        self._segment_path = lambda: "jid" + "[job-id='" + str(self.job_id) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(SystemProcess.NodeTable.Node.Jids.Jid, ['job_id', 'job_id_xr', 'process_id', 'process_name', 'executable', 'active_path', 'instance_id', 'args', 'version_id', 'respawn', 'respawn_count', 'last_started', 'process_state', 'last_exit_status', 'last_exit_reason', 'package_state', 'started_on_config', 'feature_name', 'tag', 'group', 'core', 'max_core', 'level', 'mandatory', 'maint_mode_proc', 'placement_state', 'start_up_path', 'memory_limit', 'ready', 'available'], name, value)


                    class ProcCpuTime(_Entity_):
                        """
                        Proces cpu time
                        
                        .. attribute:: user
                        
                        	User time
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: system
                        
                        	Kernel time
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: total
                        
                        	Total time
                        	**type**\: str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'sysmgr-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(SystemProcess.NodeTable.Node.Jids.Jid.ProcCpuTime, self).__init__()

                            self.yang_name = "proc-cpu-time"
                            self.yang_parent_name = "jid"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('user', (YLeaf(YType.str, 'user'), ['str'])),
                                ('system', (YLeaf(YType.str, 'system'), ['str'])),
                                ('total', (YLeaf(YType.str, 'total'), ['str'])),
                            ])
                            self.user = None
                            self.system = None
                            self.total = None
                            self._segment_path = lambda: "proc-cpu-time"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(SystemProcess.NodeTable.Node.Jids.Jid.ProcCpuTime, ['user', 'system', 'total'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
                            return meta._meta_table['SystemProcess.NodeTable.Node.Jids.Jid.ProcCpuTime']['meta_info']


                    class RegisteredItem(_Entity_):
                        """
                        Registered Items
                        
                        .. attribute:: tuple
                        
                        	Tuple
                        	**type**\: str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'sysmgr-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(SystemProcess.NodeTable.Node.Jids.Jid.RegisteredItem, self).__init__()

                            self.yang_name = "registered-item"
                            self.yang_parent_name = "jid"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('tuple', (YLeaf(YType.str, 'tuple'), ['str'])),
                            ])
                            self.tuple = None
                            self._segment_path = lambda: "registered-item"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(SystemProcess.NodeTable.Node.Jids.Jid.RegisteredItem, ['tuple'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
                            return meta._meta_table['SystemProcess.NodeTable.Node.Jids.Jid.RegisteredItem']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
                        return meta._meta_table['SystemProcess.NodeTable.Node.Jids.Jid']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
                    return meta._meta_table['SystemProcess.NodeTable.Node.Jids']['meta_info']


            class Dynamic(_Entity_):
                """
                Process Dynamic information
                
                .. attribute:: process_count
                
                	Number of processes
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: process
                
                	Array of processes
                	**type**\: list of  		 :py:class:`Process <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.SystemProcess.NodeTable.Node.Dynamic.Process>`
                
                	**config**\: False
                
                

                """

                _prefix = 'sysmgr-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(SystemProcess.NodeTable.Node.Dynamic, self).__init__()

                    self.yang_name = "dynamic"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("process", ("process", SystemProcess.NodeTable.Node.Dynamic.Process))])
                    self._leafs = OrderedDict([
                        ('process_count', (YLeaf(YType.uint32, 'process-count'), ['int'])),
                    ])
                    self.process_count = None

                    self.process = YList(self)
                    self._segment_path = lambda: "dynamic"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(SystemProcess.NodeTable.Node.Dynamic, ['process_count'], name, value)


                class Process(_Entity_):
                    """
                    Array of processes
                    
                    .. attribute:: name
                    
                    	Process name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: instance_id
                    
                    	Instance ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: args
                    
                    	Arguments
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: jid
                    
                    	Job ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: state
                    
                    	Process state
                    	**type**\:  :py:class:`ProcessState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.ProcessState>`
                    
                    	**config**\: False
                    
                    .. attribute:: last_started
                    
                    	Date and time of process last started
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: respawn_count
                    
                    	Respawn count
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: placement_state
                    
                    	Placement state
                    	**type**\:  :py:class:`PlacementState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.PlacementState>`
                    
                    	**config**\: False
                    
                    .. attribute:: is_mandatory
                    
                    	Is process mandatory?
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: is_maintenance
                    
                    	Is maintenance mode?
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'sysmgr-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(SystemProcess.NodeTable.Node.Dynamic.Process, self).__init__()

                        self.yang_name = "process"
                        self.yang_parent_name = "dynamic"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                            ('instance_id', (YLeaf(YType.uint32, 'instance-id'), ['int'])),
                            ('args', (YLeaf(YType.str, 'args'), ['str'])),
                            ('jid', (YLeaf(YType.uint32, 'jid'), ['int'])),
                            ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper', 'ProcessState', '')])),
                            ('last_started', (YLeaf(YType.str, 'last-started'), ['str'])),
                            ('respawn_count', (YLeaf(YType.uint8, 'respawn-count'), ['int'])),
                            ('placement_state', (YLeaf(YType.enumeration, 'placement-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper', 'PlacementState', '')])),
                            ('is_mandatory', (YLeaf(YType.boolean, 'is-mandatory'), ['bool'])),
                            ('is_maintenance', (YLeaf(YType.boolean, 'is-maintenance'), ['bool'])),
                        ])
                        self.name = None
                        self.instance_id = None
                        self.args = None
                        self.jid = None
                        self.state = None
                        self.last_started = None
                        self.respawn_count = None
                        self.placement_state = None
                        self.is_mandatory = None
                        self.is_maintenance = None
                        self._segment_path = lambda: "process"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(SystemProcess.NodeTable.Node.Dynamic.Process, ['name', 'instance_id', 'args', 'jid', 'state', 'last_started', 'respawn_count', 'placement_state', 'is_mandatory', 'is_maintenance'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
                        return meta._meta_table['SystemProcess.NodeTable.Node.Dynamic.Process']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
                    return meta._meta_table['SystemProcess.NodeTable.Node.Dynamic']['meta_info']


            class BootStalled(_Entity_):
                """
                Process Boot Stalled information
                
                .. attribute:: spawn_status
                
                	Spawn status of the processes
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: boot_hold
                
                	Boot hold information of the processes
                	**type**\: list of  		 :py:class:`BootHold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.SystemProcess.NodeTable.Node.BootStalled.BootHold>`
                
                	**config**\: False
                
                

                """

                _prefix = 'sysmgr-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(SystemProcess.NodeTable.Node.BootStalled, self).__init__()

                    self.yang_name = "boot-stalled"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("boot-hold", ("boot_hold", SystemProcess.NodeTable.Node.BootStalled.BootHold))])
                    self._leafs = OrderedDict([
                        ('spawn_status', (YLeaf(YType.str, 'spawn-status'), ['str'])),
                    ])
                    self.spawn_status = None

                    self.boot_hold = YList(self)
                    self._segment_path = lambda: "boot-stalled"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(SystemProcess.NodeTable.Node.BootStalled, ['spawn_status'], name, value)


                class BootHold(_Entity_):
                    """
                    Boot hold information of the processes
                    
                    .. attribute:: boot_held_by_name
                    
                    	Processs name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: instance_id
                    
                    	Instance Id
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: jid
                    
                    	Job ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'sysmgr-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(SystemProcess.NodeTable.Node.BootStalled.BootHold, self).__init__()

                        self.yang_name = "boot-hold"
                        self.yang_parent_name = "boot-stalled"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('boot_held_by_name', (YLeaf(YType.str, 'boot-held-by-name'), ['str'])),
                            ('instance_id', (YLeaf(YType.uint32, 'instance-id'), ['int'])),
                            ('jid', (YLeaf(YType.uint32, 'jid'), ['int'])),
                        ])
                        self.boot_held_by_name = None
                        self.instance_id = None
                        self.jid = None
                        self._segment_path = lambda: "boot-hold"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(SystemProcess.NodeTable.Node.BootStalled.BootHold, ['boot_held_by_name', 'instance_id', 'jid'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
                        return meta._meta_table['SystemProcess.NodeTable.Node.BootStalled.BootHold']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
                    return meta._meta_table['SystemProcess.NodeTable.Node.BootStalled']['meta_info']


            class Processes(_Entity_):
                """
                Process all information
                
                .. attribute:: process_count
                
                	Number of processes
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: process
                
                	Array of processes
                	**type**\: list of  		 :py:class:`Process <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.SystemProcess.NodeTable.Node.Processes.Process>`
                
                	**config**\: False
                
                

                """

                _prefix = 'sysmgr-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(SystemProcess.NodeTable.Node.Processes, self).__init__()

                    self.yang_name = "processes"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("process", ("process", SystemProcess.NodeTable.Node.Processes.Process))])
                    self._leafs = OrderedDict([
                        ('process_count', (YLeaf(YType.uint32, 'process-count'), ['int'])),
                    ])
                    self.process_count = None

                    self.process = YList(self)
                    self._segment_path = lambda: "processes"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(SystemProcess.NodeTable.Node.Processes, ['process_count'], name, value)


                class Process(_Entity_):
                    """
                    Array of processes
                    
                    .. attribute:: name
                    
                    	Process name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: instance_id
                    
                    	Instance ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: args
                    
                    	Arguments
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: jid
                    
                    	Job ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: state
                    
                    	Process state
                    	**type**\:  :py:class:`ProcessState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.ProcessState>`
                    
                    	**config**\: False
                    
                    .. attribute:: last_started
                    
                    	Date and time of process last started
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: respawn_count
                    
                    	Respawn count
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: placement_state
                    
                    	Placement state
                    	**type**\:  :py:class:`PlacementState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.PlacementState>`
                    
                    	**config**\: False
                    
                    .. attribute:: is_mandatory
                    
                    	Is process mandatory?
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: is_maintenance
                    
                    	Is maintenance mode?
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'sysmgr-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(SystemProcess.NodeTable.Node.Processes.Process, self).__init__()

                        self.yang_name = "process"
                        self.yang_parent_name = "processes"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                            ('instance_id', (YLeaf(YType.uint32, 'instance-id'), ['int'])),
                            ('args', (YLeaf(YType.str, 'args'), ['str'])),
                            ('jid', (YLeaf(YType.uint32, 'jid'), ['int'])),
                            ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper', 'ProcessState', '')])),
                            ('last_started', (YLeaf(YType.str, 'last-started'), ['str'])),
                            ('respawn_count', (YLeaf(YType.uint8, 'respawn-count'), ['int'])),
                            ('placement_state', (YLeaf(YType.enumeration, 'placement-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper', 'PlacementState', '')])),
                            ('is_mandatory', (YLeaf(YType.boolean, 'is-mandatory'), ['bool'])),
                            ('is_maintenance', (YLeaf(YType.boolean, 'is-maintenance'), ['bool'])),
                        ])
                        self.name = None
                        self.instance_id = None
                        self.args = None
                        self.jid = None
                        self.state = None
                        self.last_started = None
                        self.respawn_count = None
                        self.placement_state = None
                        self.is_mandatory = None
                        self.is_maintenance = None
                        self._segment_path = lambda: "process"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(SystemProcess.NodeTable.Node.Processes.Process, ['name', 'instance_id', 'args', 'jid', 'state', 'last_started', 'respawn_count', 'placement_state', 'is_mandatory', 'is_maintenance'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
                        return meta._meta_table['SystemProcess.NodeTable.Node.Processes.Process']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
                    return meta._meta_table['SystemProcess.NodeTable.Node.Processes']['meta_info']


            class Startup(_Entity_):
                """
                Process Startup information
                
                .. attribute:: process_count
                
                	Number of processes
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: process
                
                	Array of processes
                	**type**\: list of  		 :py:class:`Process <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.SystemProcess.NodeTable.Node.Startup.Process>`
                
                	**config**\: False
                
                

                """

                _prefix = 'sysmgr-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(SystemProcess.NodeTable.Node.Startup, self).__init__()

                    self.yang_name = "startup"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("process", ("process", SystemProcess.NodeTable.Node.Startup.Process))])
                    self._leafs = OrderedDict([
                        ('process_count', (YLeaf(YType.uint32, 'process-count'), ['int'])),
                    ])
                    self.process_count = None

                    self.process = YList(self)
                    self._segment_path = lambda: "startup"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(SystemProcess.NodeTable.Node.Startup, ['process_count'], name, value)


                class Process(_Entity_):
                    """
                    Array of processes
                    
                    .. attribute:: name
                    
                    	Process name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: instance_id
                    
                    	Instance ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: args
                    
                    	Arguments
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: jid
                    
                    	Job ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: state
                    
                    	Process state
                    	**type**\:  :py:class:`ProcessState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.ProcessState>`
                    
                    	**config**\: False
                    
                    .. attribute:: last_started
                    
                    	Date and time of process last started
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: respawn_count
                    
                    	Respawn count
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: placement_state
                    
                    	Placement state
                    	**type**\:  :py:class:`PlacementState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.PlacementState>`
                    
                    	**config**\: False
                    
                    .. attribute:: is_mandatory
                    
                    	Is process mandatory?
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: is_maintenance
                    
                    	Is maintenance mode?
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'sysmgr-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(SystemProcess.NodeTable.Node.Startup.Process, self).__init__()

                        self.yang_name = "process"
                        self.yang_parent_name = "startup"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                            ('instance_id', (YLeaf(YType.uint32, 'instance-id'), ['int'])),
                            ('args', (YLeaf(YType.str, 'args'), ['str'])),
                            ('jid', (YLeaf(YType.uint32, 'jid'), ['int'])),
                            ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper', 'ProcessState', '')])),
                            ('last_started', (YLeaf(YType.str, 'last-started'), ['str'])),
                            ('respawn_count', (YLeaf(YType.uint8, 'respawn-count'), ['int'])),
                            ('placement_state', (YLeaf(YType.enumeration, 'placement-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper', 'PlacementState', '')])),
                            ('is_mandatory', (YLeaf(YType.boolean, 'is-mandatory'), ['bool'])),
                            ('is_maintenance', (YLeaf(YType.boolean, 'is-maintenance'), ['bool'])),
                        ])
                        self.name = None
                        self.instance_id = None
                        self.args = None
                        self.jid = None
                        self.state = None
                        self.last_started = None
                        self.respawn_count = None
                        self.placement_state = None
                        self.is_mandatory = None
                        self.is_maintenance = None
                        self._segment_path = lambda: "process"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(SystemProcess.NodeTable.Node.Startup.Process, ['name', 'instance_id', 'args', 'jid', 'state', 'last_started', 'respawn_count', 'placement_state', 'is_mandatory', 'is_maintenance'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
                        return meta._meta_table['SystemProcess.NodeTable.Node.Startup.Process']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
                    return meta._meta_table['SystemProcess.NodeTable.Node.Startup']['meta_info']


            class Mandatory(_Entity_):
                """
                Mandatory Process information
                
                .. attribute:: process_count
                
                	Number of processes
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: process
                
                	Array of processes
                	**type**\: list of  		 :py:class:`Process <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.SystemProcess.NodeTable.Node.Mandatory.Process>`
                
                	**config**\: False
                
                

                """

                _prefix = 'sysmgr-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(SystemProcess.NodeTable.Node.Mandatory, self).__init__()

                    self.yang_name = "mandatory"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("process", ("process", SystemProcess.NodeTable.Node.Mandatory.Process))])
                    self._leafs = OrderedDict([
                        ('process_count', (YLeaf(YType.uint32, 'process-count'), ['int'])),
                    ])
                    self.process_count = None

                    self.process = YList(self)
                    self._segment_path = lambda: "mandatory"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(SystemProcess.NodeTable.Node.Mandatory, ['process_count'], name, value)


                class Process(_Entity_):
                    """
                    Array of processes
                    
                    .. attribute:: name
                    
                    	Process name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: instance_id
                    
                    	Instance ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: args
                    
                    	Arguments
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: jid
                    
                    	Job ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: state
                    
                    	Process state
                    	**type**\:  :py:class:`ProcessState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.ProcessState>`
                    
                    	**config**\: False
                    
                    .. attribute:: last_started
                    
                    	Date and time of process last started
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: respawn_count
                    
                    	Respawn count
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: placement_state
                    
                    	Placement state
                    	**type**\:  :py:class:`PlacementState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.PlacementState>`
                    
                    	**config**\: False
                    
                    .. attribute:: is_mandatory
                    
                    	Is process mandatory?
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: is_maintenance
                    
                    	Is maintenance mode?
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'sysmgr-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(SystemProcess.NodeTable.Node.Mandatory.Process, self).__init__()

                        self.yang_name = "process"
                        self.yang_parent_name = "mandatory"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                            ('instance_id', (YLeaf(YType.uint32, 'instance-id'), ['int'])),
                            ('args', (YLeaf(YType.str, 'args'), ['str'])),
                            ('jid', (YLeaf(YType.uint32, 'jid'), ['int'])),
                            ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper', 'ProcessState', '')])),
                            ('last_started', (YLeaf(YType.str, 'last-started'), ['str'])),
                            ('respawn_count', (YLeaf(YType.uint8, 'respawn-count'), ['int'])),
                            ('placement_state', (YLeaf(YType.enumeration, 'placement-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper', 'PlacementState', '')])),
                            ('is_mandatory', (YLeaf(YType.boolean, 'is-mandatory'), ['bool'])),
                            ('is_maintenance', (YLeaf(YType.boolean, 'is-maintenance'), ['bool'])),
                        ])
                        self.name = None
                        self.instance_id = None
                        self.args = None
                        self.jid = None
                        self.state = None
                        self.last_started = None
                        self.respawn_count = None
                        self.placement_state = None
                        self.is_mandatory = None
                        self.is_maintenance = None
                        self._segment_path = lambda: "process"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(SystemProcess.NodeTable.Node.Mandatory.Process, ['name', 'instance_id', 'args', 'jid', 'state', 'last_started', 'respawn_count', 'placement_state', 'is_mandatory', 'is_maintenance'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
                        return meta._meta_table['SystemProcess.NodeTable.Node.Mandatory.Process']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
                    return meta._meta_table['SystemProcess.NodeTable.Node.Mandatory']['meta_info']


            class Abort(_Entity_):
                """
                Process Abort information
                
                .. attribute:: process_abort_count
                
                	Number of Aborted Processes
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: process
                
                	Array of aborted processes
                	**type**\: list of  		 :py:class:`Process <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.SystemProcess.NodeTable.Node.Abort.Process>`
                
                	**config**\: False
                
                

                """

                _prefix = 'sysmgr-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(SystemProcess.NodeTable.Node.Abort, self).__init__()

                    self.yang_name = "abort"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("process", ("process", SystemProcess.NodeTable.Node.Abort.Process))])
                    self._leafs = OrderedDict([
                        ('process_abort_count', (YLeaf(YType.uint32, 'process-abort-count'), ['int'])),
                    ])
                    self.process_abort_count = None

                    self.process = YList(self)
                    self._segment_path = lambda: "abort"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(SystemProcess.NodeTable.Node.Abort, ['process_abort_count'], name, value)


                class Process(_Entity_):
                    """
                    Array of aborted processes
                    
                    .. attribute:: name
                    
                    	Process name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: timebuf
                    
                    	Date and time of process abort
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: job_id
                    
                    	Job ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: is_respawned
                    
                    	Respawn information
                    	**type**\: str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'sysmgr-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(SystemProcess.NodeTable.Node.Abort.Process, self).__init__()

                        self.yang_name = "process"
                        self.yang_parent_name = "abort"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                            ('timebuf', (YLeaf(YType.str, 'timebuf'), ['str'])),
                            ('job_id', (YLeaf(YType.uint32, 'job-id'), ['int'])),
                            ('is_respawned', (YLeaf(YType.str, 'is-respawned'), ['str'])),
                        ])
                        self.name = None
                        self.timebuf = None
                        self.job_id = None
                        self.is_respawned = None
                        self._segment_path = lambda: "process"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(SystemProcess.NodeTable.Node.Abort.Process, ['name', 'timebuf', 'job_id', 'is_respawned'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
                        return meta._meta_table['SystemProcess.NodeTable.Node.Abort.Process']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
                    return meta._meta_table['SystemProcess.NodeTable.Node.Abort']['meta_info']


            class Failover(_Entity_):
                """
                Process Failover information
                
                .. attribute:: failover_log
                
                	Failover log message
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: critical_failover_elapsed_time
                
                	Critical Failover Elapsed Time
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: last_process_started
                
                	Last process started
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: primary_failover_elapsed_time
                
                	Primary failover elapsed time
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: last_primary_proc_started
                
                	Last primary process started
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: standby_band_statistic
                
                	Standby Band statistics
                	**type**\: list of  		 :py:class:`StandbyBandStatistic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.SystemProcess.NodeTable.Node.Failover.StandbyBandStatistic>`
                
                	**config**\: False
                
                .. attribute:: active_band_statistic
                
                	Active Band statistics
                	**type**\: list of  		 :py:class:`ActiveBandStatistic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.SystemProcess.NodeTable.Node.Failover.ActiveBandStatistic>`
                
                	**config**\: False
                
                .. attribute:: active_ts_boot_proc
                
                	List of booted process as per avail time
                	**type**\: list of  		 :py:class:`ActiveTsBootProc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.SystemProcess.NodeTable.Node.Failover.ActiveTsBootProc>`
                
                	**config**\: False
                
                .. attribute:: start_ts_boot_proc
                
                	List of booted processes per start time
                	**type**\: list of  		 :py:class:`StartTsBootProc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.SystemProcess.NodeTable.Node.Failover.StartTsBootProc>`
                
                	**config**\: False
                
                .. attribute:: primary_band_statistic
                
                	Primary Band statistics
                	**type**\: list of  		 :py:class:`PrimaryBandStatistic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.SystemProcess.NodeTable.Node.Failover.PrimaryBandStatistic>`
                
                	**config**\: False
                
                .. attribute:: primary_ts_boot_proc
                
                	List of booted processes per primary time
                	**type**\: list of  		 :py:class:`PrimaryTsBootProc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.SystemProcess.NodeTable.Node.Failover.PrimaryTsBootProc>`
                
                	**config**\: False
                
                .. attribute:: primary_start_ts_boot_proc
                
                	List of booted process per primary start time
                	**type**\: list of  		 :py:class:`PrimaryStartTsBootProc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.SystemProcess.NodeTable.Node.Failover.PrimaryStartTsBootProc>`
                
                	**config**\: False
                
                

                """

                _prefix = 'sysmgr-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(SystemProcess.NodeTable.Node.Failover, self).__init__()

                    self.yang_name = "failover"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("standby-band-statistic", ("standby_band_statistic", SystemProcess.NodeTable.Node.Failover.StandbyBandStatistic)), ("active-band-statistic", ("active_band_statistic", SystemProcess.NodeTable.Node.Failover.ActiveBandStatistic)), ("active-ts-boot-proc", ("active_ts_boot_proc", SystemProcess.NodeTable.Node.Failover.ActiveTsBootProc)), ("start-ts-boot-proc", ("start_ts_boot_proc", SystemProcess.NodeTable.Node.Failover.StartTsBootProc)), ("primary-band-statistic", ("primary_band_statistic", SystemProcess.NodeTable.Node.Failover.PrimaryBandStatistic)), ("primary-ts-boot-proc", ("primary_ts_boot_proc", SystemProcess.NodeTable.Node.Failover.PrimaryTsBootProc)), ("primary-start-ts-boot-proc", ("primary_start_ts_boot_proc", SystemProcess.NodeTable.Node.Failover.PrimaryStartTsBootProc))])
                    self._leafs = OrderedDict([
                        ('failover_log', (YLeaf(YType.str, 'failover-log'), ['str'])),
                        ('critical_failover_elapsed_time', (YLeaf(YType.str, 'critical-failover-elapsed-time'), ['str'])),
                        ('last_process_started', (YLeaf(YType.str, 'last-process-started'), ['str'])),
                        ('primary_failover_elapsed_time', (YLeaf(YType.str, 'primary-failover-elapsed-time'), ['str'])),
                        ('last_primary_proc_started', (YLeaf(YType.str, 'last-primary-proc-started'), ['str'])),
                    ])
                    self.failover_log = None
                    self.critical_failover_elapsed_time = None
                    self.last_process_started = None
                    self.primary_failover_elapsed_time = None
                    self.last_primary_proc_started = None

                    self.standby_band_statistic = YList(self)
                    self.active_band_statistic = YList(self)
                    self.active_ts_boot_proc = YList(self)
                    self.start_ts_boot_proc = YList(self)
                    self.primary_band_statistic = YList(self)
                    self.primary_ts_boot_proc = YList(self)
                    self.primary_start_ts_boot_proc = YList(self)
                    self._segment_path = lambda: "failover"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(SystemProcess.NodeTable.Node.Failover, ['failover_log', 'critical_failover_elapsed_time', 'last_process_started', 'primary_failover_elapsed_time', 'last_primary_proc_started'], name, value)


                class StandbyBandStatistic(_Entity_):
                    """
                    Standby Band statistics
                    
                    .. attribute:: level
                    
                    	Level
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: band_name
                    
                    	Band Name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: band_finish_time
                    
                    	Band finish time
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: band_time
                    
                    	Band time
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: finish_time
                    
                    	Finish Time
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: idle_percentage
                    
                    	Idle Percentage
                    	**type**\: str
                    
                    	**config**\: False
                    
                    	**units**\: percentage
                    
                    .. attribute:: jid
                    
                    	Jid
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: ready_time
                    
                    	Ready Time
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: last_process
                    
                    	Last Process Name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'sysmgr-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(SystemProcess.NodeTable.Node.Failover.StandbyBandStatistic, self).__init__()

                        self.yang_name = "standby-band-statistic"
                        self.yang_parent_name = "failover"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('level', (YLeaf(YType.str, 'level'), ['str'])),
                            ('band_name', (YLeaf(YType.str, 'band-name'), ['str'])),
                            ('band_finish_time', (YLeaf(YType.str, 'band-finish-time'), ['str'])),
                            ('band_time', (YLeaf(YType.str, 'band-time'), ['str'])),
                            ('finish_time', (YLeaf(YType.str, 'finish-time'), ['str'])),
                            ('idle_percentage', (YLeaf(YType.str, 'idle-percentage'), ['str'])),
                            ('jid', (YLeaf(YType.uint32, 'jid'), ['int'])),
                            ('ready_time', (YLeaf(YType.str, 'ready-time'), ['str'])),
                            ('last_process', (YLeaf(YType.str, 'last-process'), ['str'])),
                        ])
                        self.level = None
                        self.band_name = None
                        self.band_finish_time = None
                        self.band_time = None
                        self.finish_time = None
                        self.idle_percentage = None
                        self.jid = None
                        self.ready_time = None
                        self.last_process = None
                        self._segment_path = lambda: "standby-band-statistic"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(SystemProcess.NodeTable.Node.Failover.StandbyBandStatistic, ['level', 'band_name', 'band_finish_time', 'band_time', 'finish_time', 'idle_percentage', 'jid', 'ready_time', 'last_process'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
                        return meta._meta_table['SystemProcess.NodeTable.Node.Failover.StandbyBandStatistic']['meta_info']


                class ActiveBandStatistic(_Entity_):
                    """
                    Active Band statistics
                    
                    .. attribute:: level
                    
                    	Level
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: band_name
                    
                    	Band Name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: band_finish_time
                    
                    	Band finish time
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: band_time
                    
                    	Band time
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: finish_time
                    
                    	Finish Time
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: idle_percentage
                    
                    	Idle Percentage
                    	**type**\: str
                    
                    	**config**\: False
                    
                    	**units**\: percentage
                    
                    .. attribute:: jid
                    
                    	Jid
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: ready_time
                    
                    	Ready Time
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: last_process
                    
                    	Last Process Name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'sysmgr-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(SystemProcess.NodeTable.Node.Failover.ActiveBandStatistic, self).__init__()

                        self.yang_name = "active-band-statistic"
                        self.yang_parent_name = "failover"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('level', (YLeaf(YType.str, 'level'), ['str'])),
                            ('band_name', (YLeaf(YType.str, 'band-name'), ['str'])),
                            ('band_finish_time', (YLeaf(YType.str, 'band-finish-time'), ['str'])),
                            ('band_time', (YLeaf(YType.str, 'band-time'), ['str'])),
                            ('finish_time', (YLeaf(YType.str, 'finish-time'), ['str'])),
                            ('idle_percentage', (YLeaf(YType.str, 'idle-percentage'), ['str'])),
                            ('jid', (YLeaf(YType.uint32, 'jid'), ['int'])),
                            ('ready_time', (YLeaf(YType.str, 'ready-time'), ['str'])),
                            ('last_process', (YLeaf(YType.str, 'last-process'), ['str'])),
                        ])
                        self.level = None
                        self.band_name = None
                        self.band_finish_time = None
                        self.band_time = None
                        self.finish_time = None
                        self.idle_percentage = None
                        self.jid = None
                        self.ready_time = None
                        self.last_process = None
                        self._segment_path = lambda: "active-band-statistic"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(SystemProcess.NodeTable.Node.Failover.ActiveBandStatistic, ['level', 'band_name', 'band_finish_time', 'band_time', 'finish_time', 'idle_percentage', 'jid', 'ready_time', 'last_process'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
                        return meta._meta_table['SystemProcess.NodeTable.Node.Failover.ActiveBandStatistic']['meta_info']


                class ActiveTsBootProc(_Entity_):
                    """
                    List of booted process as per avail time
                    
                    .. attribute:: active_time_stamp
                    
                    	Active Time Stamp
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: go_active
                    
                    	Go Active time stamp
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: level
                    
                    	Level
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: band_name
                    
                    	Band Name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: job_id
                    
                    	Job Id
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**config**\: False
                    
                    .. attribute:: instance_id
                    
                    	Instance Id
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**config**\: False
                    
                    .. attribute:: avail_time_stamp
                    
                    	Avail Time Stamp
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: avail
                    
                    	Time since Avail
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: is_avail_timeout
                    
                    	Is Avail timeout
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: process_name
                    
                    	Process Name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'sysmgr-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(SystemProcess.NodeTable.Node.Failover.ActiveTsBootProc, self).__init__()

                        self.yang_name = "active-ts-boot-proc"
                        self.yang_parent_name = "failover"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('active_time_stamp', (YLeaf(YType.str, 'active-time-stamp'), ['str'])),
                            ('go_active', (YLeaf(YType.str, 'go-active'), ['str'])),
                            ('level', (YLeaf(YType.str, 'level'), ['str'])),
                            ('band_name', (YLeaf(YType.str, 'band-name'), ['str'])),
                            ('job_id', (YLeaf(YType.int32, 'job-id'), ['int'])),
                            ('instance_id', (YLeaf(YType.int32, 'instance-id'), ['int'])),
                            ('avail_time_stamp', (YLeaf(YType.str, 'avail-time-stamp'), ['str'])),
                            ('avail', (YLeaf(YType.str, 'avail'), ['str'])),
                            ('is_avail_timeout', (YLeaf(YType.boolean, 'is-avail-timeout'), ['bool'])),
                            ('process_name', (YLeaf(YType.str, 'process-name'), ['str'])),
                        ])
                        self.active_time_stamp = None
                        self.go_active = None
                        self.level = None
                        self.band_name = None
                        self.job_id = None
                        self.instance_id = None
                        self.avail_time_stamp = None
                        self.avail = None
                        self.is_avail_timeout = None
                        self.process_name = None
                        self._segment_path = lambda: "active-ts-boot-proc"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(SystemProcess.NodeTable.Node.Failover.ActiveTsBootProc, ['active_time_stamp', 'go_active', 'level', 'band_name', 'job_id', 'instance_id', 'avail_time_stamp', 'avail', 'is_avail_timeout', 'process_name'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
                        return meta._meta_table['SystemProcess.NodeTable.Node.Failover.ActiveTsBootProc']['meta_info']


                class StartTsBootProc(_Entity_):
                    """
                    List of booted processes per start time
                    
                    .. attribute:: start_time_stamp
                    
                    	Start Time Stamp
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: started
                    
                    	Time since started
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: level
                    
                    	Level
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: jid
                    
                    	Job Id
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**config**\: False
                    
                    .. attribute:: instance_id
                    
                    	Instance Id
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**config**\: False
                    
                    .. attribute:: ready_time_stamp
                    
                    	Ready Time Stamp
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: ready
                    
                    	Time since Ready
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: is_eoi_timeout
                    
                    	Is EOI timeout
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: process_name
                    
                    	Process Name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'sysmgr-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(SystemProcess.NodeTable.Node.Failover.StartTsBootProc, self).__init__()

                        self.yang_name = "start-ts-boot-proc"
                        self.yang_parent_name = "failover"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('start_time_stamp', (YLeaf(YType.str, 'start-time-stamp'), ['str'])),
                            ('started', (YLeaf(YType.str, 'started'), ['str'])),
                            ('level', (YLeaf(YType.str, 'level'), ['str'])),
                            ('jid', (YLeaf(YType.int32, 'jid'), ['int'])),
                            ('instance_id', (YLeaf(YType.int32, 'instance-id'), ['int'])),
                            ('ready_time_stamp', (YLeaf(YType.str, 'ready-time-stamp'), ['str'])),
                            ('ready', (YLeaf(YType.str, 'ready'), ['str'])),
                            ('is_eoi_timeout', (YLeaf(YType.boolean, 'is-eoi-timeout'), ['bool'])),
                            ('process_name', (YLeaf(YType.str, 'process-name'), ['str'])),
                        ])
                        self.start_time_stamp = None
                        self.started = None
                        self.level = None
                        self.jid = None
                        self.instance_id = None
                        self.ready_time_stamp = None
                        self.ready = None
                        self.is_eoi_timeout = None
                        self.process_name = None
                        self._segment_path = lambda: "start-ts-boot-proc"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(SystemProcess.NodeTable.Node.Failover.StartTsBootProc, ['start_time_stamp', 'started', 'level', 'jid', 'instance_id', 'ready_time_stamp', 'ready', 'is_eoi_timeout', 'process_name'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
                        return meta._meta_table['SystemProcess.NodeTable.Node.Failover.StartTsBootProc']['meta_info']


                class PrimaryBandStatistic(_Entity_):
                    """
                    Primary Band statistics
                    
                    .. attribute:: level
                    
                    	Level
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: band_name
                    
                    	Band Name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: band_finish_time
                    
                    	Band finish time
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: band_time
                    
                    	Band time
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: finish_time
                    
                    	Finish Time
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: idle_percentage
                    
                    	Idle Percentage
                    	**type**\: str
                    
                    	**config**\: False
                    
                    	**units**\: percentage
                    
                    .. attribute:: jid
                    
                    	Jid
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: ready_time
                    
                    	Ready Time
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: last_process
                    
                    	Last Process Name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'sysmgr-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(SystemProcess.NodeTable.Node.Failover.PrimaryBandStatistic, self).__init__()

                        self.yang_name = "primary-band-statistic"
                        self.yang_parent_name = "failover"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('level', (YLeaf(YType.str, 'level'), ['str'])),
                            ('band_name', (YLeaf(YType.str, 'band-name'), ['str'])),
                            ('band_finish_time', (YLeaf(YType.str, 'band-finish-time'), ['str'])),
                            ('band_time', (YLeaf(YType.str, 'band-time'), ['str'])),
                            ('finish_time', (YLeaf(YType.str, 'finish-time'), ['str'])),
                            ('idle_percentage', (YLeaf(YType.str, 'idle-percentage'), ['str'])),
                            ('jid', (YLeaf(YType.uint32, 'jid'), ['int'])),
                            ('ready_time', (YLeaf(YType.str, 'ready-time'), ['str'])),
                            ('last_process', (YLeaf(YType.str, 'last-process'), ['str'])),
                        ])
                        self.level = None
                        self.band_name = None
                        self.band_finish_time = None
                        self.band_time = None
                        self.finish_time = None
                        self.idle_percentage = None
                        self.jid = None
                        self.ready_time = None
                        self.last_process = None
                        self._segment_path = lambda: "primary-band-statistic"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(SystemProcess.NodeTable.Node.Failover.PrimaryBandStatistic, ['level', 'band_name', 'band_finish_time', 'band_time', 'finish_time', 'idle_percentage', 'jid', 'ready_time', 'last_process'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
                        return meta._meta_table['SystemProcess.NodeTable.Node.Failover.PrimaryBandStatistic']['meta_info']


                class PrimaryTsBootProc(_Entity_):
                    """
                    List of booted processes per primary time
                    
                    .. attribute:: prim_time_stamp
                    
                    	Primary Time Stamp
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: go_primary
                    
                    	Go primary time stamp
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: level
                    
                    	Level
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: band_name
                    
                    	Band Name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: jid
                    
                    	Job Id
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**config**\: False
                    
                    .. attribute:: instance_id
                    
                    	Instance Id
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**config**\: False
                    
                    .. attribute:: avail_time_stamp
                    
                    	Avail Time Stamp
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: avail
                    
                    	Time since Avail
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: is_avail_timeout
                    
                    	Is EOI timeout
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: process_name
                    
                    	Process Name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'sysmgr-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(SystemProcess.NodeTable.Node.Failover.PrimaryTsBootProc, self).__init__()

                        self.yang_name = "primary-ts-boot-proc"
                        self.yang_parent_name = "failover"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('prim_time_stamp', (YLeaf(YType.str, 'prim-time-stamp'), ['str'])),
                            ('go_primary', (YLeaf(YType.str, 'go-primary'), ['str'])),
                            ('level', (YLeaf(YType.str, 'level'), ['str'])),
                            ('band_name', (YLeaf(YType.str, 'band-name'), ['str'])),
                            ('jid', (YLeaf(YType.int32, 'jid'), ['int'])),
                            ('instance_id', (YLeaf(YType.int32, 'instance-id'), ['int'])),
                            ('avail_time_stamp', (YLeaf(YType.str, 'avail-time-stamp'), ['str'])),
                            ('avail', (YLeaf(YType.str, 'avail'), ['str'])),
                            ('is_avail_timeout', (YLeaf(YType.boolean, 'is-avail-timeout'), ['bool'])),
                            ('process_name', (YLeaf(YType.str, 'process-name'), ['str'])),
                        ])
                        self.prim_time_stamp = None
                        self.go_primary = None
                        self.level = None
                        self.band_name = None
                        self.jid = None
                        self.instance_id = None
                        self.avail_time_stamp = None
                        self.avail = None
                        self.is_avail_timeout = None
                        self.process_name = None
                        self._segment_path = lambda: "primary-ts-boot-proc"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(SystemProcess.NodeTable.Node.Failover.PrimaryTsBootProc, ['prim_time_stamp', 'go_primary', 'level', 'band_name', 'jid', 'instance_id', 'avail_time_stamp', 'avail', 'is_avail_timeout', 'process_name'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
                        return meta._meta_table['SystemProcess.NodeTable.Node.Failover.PrimaryTsBootProc']['meta_info']


                class PrimaryStartTsBootProc(_Entity_):
                    """
                    List of booted process per primary start time
                    
                    .. attribute:: start_time_stamp
                    
                    	Start Time Stamp
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: started
                    
                    	Time since started
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: level
                    
                    	Level
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: jid
                    
                    	Job Id
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**config**\: False
                    
                    .. attribute:: instance_id
                    
                    	Instance Id
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**config**\: False
                    
                    .. attribute:: ready_time_stamp
                    
                    	Ready Time Stamp
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: ready
                    
                    	Time since Ready
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: is_eoi_timeout
                    
                    	Is EOI timeout
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: process_name
                    
                    	Process Name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'sysmgr-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(SystemProcess.NodeTable.Node.Failover.PrimaryStartTsBootProc, self).__init__()

                        self.yang_name = "primary-start-ts-boot-proc"
                        self.yang_parent_name = "failover"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('start_time_stamp', (YLeaf(YType.str, 'start-time-stamp'), ['str'])),
                            ('started', (YLeaf(YType.str, 'started'), ['str'])),
                            ('level', (YLeaf(YType.str, 'level'), ['str'])),
                            ('jid', (YLeaf(YType.int32, 'jid'), ['int'])),
                            ('instance_id', (YLeaf(YType.int32, 'instance-id'), ['int'])),
                            ('ready_time_stamp', (YLeaf(YType.str, 'ready-time-stamp'), ['str'])),
                            ('ready', (YLeaf(YType.str, 'ready'), ['str'])),
                            ('is_eoi_timeout', (YLeaf(YType.boolean, 'is-eoi-timeout'), ['bool'])),
                            ('process_name', (YLeaf(YType.str, 'process-name'), ['str'])),
                        ])
                        self.start_time_stamp = None
                        self.started = None
                        self.level = None
                        self.jid = None
                        self.instance_id = None
                        self.ready_time_stamp = None
                        self.ready = None
                        self.is_eoi_timeout = None
                        self.process_name = None
                        self._segment_path = lambda: "primary-start-ts-boot-proc"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(SystemProcess.NodeTable.Node.Failover.PrimaryStartTsBootProc, ['start_time_stamp', 'started', 'level', 'jid', 'instance_id', 'ready_time_stamp', 'ready', 'is_eoi_timeout', 'process_name'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
                        return meta._meta_table['SystemProcess.NodeTable.Node.Failover.PrimaryStartTsBootProc']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
                    return meta._meta_table['SystemProcess.NodeTable.Node.Failover']['meta_info']


            class Boot(_Entity_):
                """
                Process Boot information
                
                .. attribute:: last_process_started
                
                	Last process started
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: standby_band_statistic
                
                	Standby Band statistics
                	**type**\: list of  		 :py:class:`StandbyBandStatistic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.SystemProcess.NodeTable.Node.Boot.StandbyBandStatistic>`
                
                	**config**\: False
                
                .. attribute:: active_band_statistic
                
                	Active Band statistics
                	**type**\: list of  		 :py:class:`ActiveBandStatistic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.SystemProcess.NodeTable.Node.Boot.ActiveBandStatistic>`
                
                	**config**\: False
                
                .. attribute:: booted_process
                
                	List of booted processes
                	**type**\: list of  		 :py:class:`BootedProcess <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_oper.SystemProcess.NodeTable.Node.Boot.BootedProcess>`
                
                	**config**\: False
                
                

                """

                _prefix = 'sysmgr-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(SystemProcess.NodeTable.Node.Boot, self).__init__()

                    self.yang_name = "boot"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("standby-band-statistic", ("standby_band_statistic", SystemProcess.NodeTable.Node.Boot.StandbyBandStatistic)), ("active-band-statistic", ("active_band_statistic", SystemProcess.NodeTable.Node.Boot.ActiveBandStatistic)), ("booted-process", ("booted_process", SystemProcess.NodeTable.Node.Boot.BootedProcess))])
                    self._leafs = OrderedDict([
                        ('last_process_started', (YLeaf(YType.str, 'last-process-started'), ['str'])),
                    ])
                    self.last_process_started = None

                    self.standby_band_statistic = YList(self)
                    self.active_band_statistic = YList(self)
                    self.booted_process = YList(self)
                    self._segment_path = lambda: "boot"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(SystemProcess.NodeTable.Node.Boot, ['last_process_started'], name, value)


                class StandbyBandStatistic(_Entity_):
                    """
                    Standby Band statistics
                    
                    .. attribute:: level
                    
                    	Level
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: band_name
                    
                    	Band Name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: band_finish_time
                    
                    	Band finish time
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: band_time
                    
                    	Band time
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: finish_time
                    
                    	Finish Time
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: idle_percentage
                    
                    	Idle Percentage
                    	**type**\: str
                    
                    	**config**\: False
                    
                    	**units**\: percentage
                    
                    .. attribute:: jid
                    
                    	Jid
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: ready_time
                    
                    	Ready Time
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: last_process
                    
                    	Last Process Name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'sysmgr-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(SystemProcess.NodeTable.Node.Boot.StandbyBandStatistic, self).__init__()

                        self.yang_name = "standby-band-statistic"
                        self.yang_parent_name = "boot"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('level', (YLeaf(YType.str, 'level'), ['str'])),
                            ('band_name', (YLeaf(YType.str, 'band-name'), ['str'])),
                            ('band_finish_time', (YLeaf(YType.str, 'band-finish-time'), ['str'])),
                            ('band_time', (YLeaf(YType.str, 'band-time'), ['str'])),
                            ('finish_time', (YLeaf(YType.str, 'finish-time'), ['str'])),
                            ('idle_percentage', (YLeaf(YType.str, 'idle-percentage'), ['str'])),
                            ('jid', (YLeaf(YType.uint32, 'jid'), ['int'])),
                            ('ready_time', (YLeaf(YType.str, 'ready-time'), ['str'])),
                            ('last_process', (YLeaf(YType.str, 'last-process'), ['str'])),
                        ])
                        self.level = None
                        self.band_name = None
                        self.band_finish_time = None
                        self.band_time = None
                        self.finish_time = None
                        self.idle_percentage = None
                        self.jid = None
                        self.ready_time = None
                        self.last_process = None
                        self._segment_path = lambda: "standby-band-statistic"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(SystemProcess.NodeTable.Node.Boot.StandbyBandStatistic, ['level', 'band_name', 'band_finish_time', 'band_time', 'finish_time', 'idle_percentage', 'jid', 'ready_time', 'last_process'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
                        return meta._meta_table['SystemProcess.NodeTable.Node.Boot.StandbyBandStatistic']['meta_info']


                class ActiveBandStatistic(_Entity_):
                    """
                    Active Band statistics
                    
                    .. attribute:: level
                    
                    	Level
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: band_name
                    
                    	Band Name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: band_finish_time
                    
                    	Band finish time
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: band_time
                    
                    	Band time
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: finish_time
                    
                    	Finish Time
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: idle_percentage
                    
                    	Idle Percentage
                    	**type**\: str
                    
                    	**config**\: False
                    
                    	**units**\: percentage
                    
                    .. attribute:: jid
                    
                    	Jid
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: ready_time
                    
                    	Ready Time
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: last_process
                    
                    	Last Process Name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'sysmgr-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(SystemProcess.NodeTable.Node.Boot.ActiveBandStatistic, self).__init__()

                        self.yang_name = "active-band-statistic"
                        self.yang_parent_name = "boot"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('level', (YLeaf(YType.str, 'level'), ['str'])),
                            ('band_name', (YLeaf(YType.str, 'band-name'), ['str'])),
                            ('band_finish_time', (YLeaf(YType.str, 'band-finish-time'), ['str'])),
                            ('band_time', (YLeaf(YType.str, 'band-time'), ['str'])),
                            ('finish_time', (YLeaf(YType.str, 'finish-time'), ['str'])),
                            ('idle_percentage', (YLeaf(YType.str, 'idle-percentage'), ['str'])),
                            ('jid', (YLeaf(YType.uint32, 'jid'), ['int'])),
                            ('ready_time', (YLeaf(YType.str, 'ready-time'), ['str'])),
                            ('last_process', (YLeaf(YType.str, 'last-process'), ['str'])),
                        ])
                        self.level = None
                        self.band_name = None
                        self.band_finish_time = None
                        self.band_time = None
                        self.finish_time = None
                        self.idle_percentage = None
                        self.jid = None
                        self.ready_time = None
                        self.last_process = None
                        self._segment_path = lambda: "active-band-statistic"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(SystemProcess.NodeTable.Node.Boot.ActiveBandStatistic, ['level', 'band_name', 'band_finish_time', 'band_time', 'finish_time', 'idle_percentage', 'jid', 'ready_time', 'last_process'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
                        return meta._meta_table['SystemProcess.NodeTable.Node.Boot.ActiveBandStatistic']['meta_info']


                class BootedProcess(_Entity_):
                    """
                    List of booted processes
                    
                    .. attribute:: start_time_stamp
                    
                    	Start Time Stamp
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: started
                    
                    	Time since started
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: level
                    
                    	Level
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: jid
                    
                    	Job Id
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**config**\: False
                    
                    .. attribute:: instance_id
                    
                    	Instance Id
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**config**\: False
                    
                    .. attribute:: ready_time_stamp
                    
                    	Ready Time Stamp
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: ready
                    
                    	Time since Ready
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: is_eoi_timeout
                    
                    	Is EOI timeout
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: process_name
                    
                    	Process Name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'sysmgr-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(SystemProcess.NodeTable.Node.Boot.BootedProcess, self).__init__()

                        self.yang_name = "booted-process"
                        self.yang_parent_name = "boot"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('start_time_stamp', (YLeaf(YType.str, 'start-time-stamp'), ['str'])),
                            ('started', (YLeaf(YType.str, 'started'), ['str'])),
                            ('level', (YLeaf(YType.str, 'level'), ['str'])),
                            ('jid', (YLeaf(YType.int32, 'jid'), ['int'])),
                            ('instance_id', (YLeaf(YType.int32, 'instance-id'), ['int'])),
                            ('ready_time_stamp', (YLeaf(YType.str, 'ready-time-stamp'), ['str'])),
                            ('ready', (YLeaf(YType.str, 'ready'), ['str'])),
                            ('is_eoi_timeout', (YLeaf(YType.boolean, 'is-eoi-timeout'), ['bool'])),
                            ('process_name', (YLeaf(YType.str, 'process-name'), ['str'])),
                        ])
                        self.start_time_stamp = None
                        self.started = None
                        self.level = None
                        self.jid = None
                        self.instance_id = None
                        self.ready_time_stamp = None
                        self.ready = None
                        self.is_eoi_timeout = None
                        self.process_name = None
                        self._segment_path = lambda: "booted-process"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(SystemProcess.NodeTable.Node.Boot.BootedProcess, ['start_time_stamp', 'started', 'level', 'jid', 'instance_id', 'ready_time_stamp', 'ready', 'is_eoi_timeout', 'process_name'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
                        return meta._meta_table['SystemProcess.NodeTable.Node.Boot.BootedProcess']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
                    return meta._meta_table['SystemProcess.NodeTable.Node.Boot']['meta_info']


            class Logs(_Entity_):
                """
                Process Log information
                
                .. attribute:: log
                
                	Process log
                	**type**\: str
                
                	**config**\: False
                
                

                """

                _prefix = 'sysmgr-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(SystemProcess.NodeTable.Node.Logs, self).__init__()

                    self.yang_name = "logs"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('log', (YLeaf(YType.str, 'log'), ['str'])),
                    ])
                    self.log = None
                    self._segment_path = lambda: "logs"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(SystemProcess.NodeTable.Node.Logs, ['log'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
                    return meta._meta_table['SystemProcess.NodeTable.Node.Logs']['meta_info']


            class Searchpath(_Entity_):
                """
                Process Searchpath information
                
                .. attribute:: path
                
                	process searchpath
                	**type**\: str
                
                	**config**\: False
                
                

                """

                _prefix = 'sysmgr-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(SystemProcess.NodeTable.Node.Searchpath, self).__init__()

                    self.yang_name = "searchpath"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('path', (YLeaf(YType.str, 'path'), ['str'])),
                    ])
                    self.path = None
                    self._segment_path = lambda: "searchpath"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(SystemProcess.NodeTable.Node.Searchpath, ['path'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
                    return meta._meta_table['SystemProcess.NodeTable.Node.Searchpath']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
                return meta._meta_table['SystemProcess.NodeTable.Node']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
            return meta._meta_table['SystemProcess.NodeTable']['meta_info']

    def clone_ptr(self):
        self._top_entity = SystemProcess()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysmgr_oper as meta
        return meta._meta_table['SystemProcess']['meta_info']


