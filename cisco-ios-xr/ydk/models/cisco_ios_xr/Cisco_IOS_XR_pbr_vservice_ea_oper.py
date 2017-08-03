""" Cisco_IOS_XR_pbr_vservice_ea_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR pbr\-vservice\-ea package operational data.

This module contains definitions
for the following management objects\:
  service\-function\-chaining\: NSH Service Function Chaining
    operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class VsNshStats(Enum):
    """
    VsNshStats

    Vs nsh stats

    .. data:: vs_nsh_stats_spi_si = 0

    	vs nsh stats spi si

    .. data:: vs_nsh_stats_ter_min_ate = 1

    	vs nsh stats ter min ate

    .. data:: vs_nsh_stats_sf = 2

    	vs nsh stats sf

    .. data:: vs_nsh_stats_sff = 3

    	vs nsh stats sff

    .. data:: vs_nsh_stats_sff_local = 4

    	vs nsh stats sff local

    .. data:: vs_nsh_stats_sfp = 5

    	vs nsh stats sfp

    .. data:: vs_nsh_stats_sfp_detail = 6

    	vs nsh stats sfp detail

    .. data:: vs_nsh_stats_max = 7

    	vs nsh stats max

    """

    vs_nsh_stats_spi_si = Enum.YLeaf(0, "vs-nsh-stats-spi-si")

    vs_nsh_stats_ter_min_ate = Enum.YLeaf(1, "vs-nsh-stats-ter-min-ate")

    vs_nsh_stats_sf = Enum.YLeaf(2, "vs-nsh-stats-sf")

    vs_nsh_stats_sff = Enum.YLeaf(3, "vs-nsh-stats-sff")

    vs_nsh_stats_sff_local = Enum.YLeaf(4, "vs-nsh-stats-sff-local")

    vs_nsh_stats_sfp = Enum.YLeaf(5, "vs-nsh-stats-sfp")

    vs_nsh_stats_sfp_detail = Enum.YLeaf(6, "vs-nsh-stats-sfp-detail")

    vs_nsh_stats_max = Enum.YLeaf(7, "vs-nsh-stats-max")



class ServiceFunctionChaining(Entity):
    """
    NSH Service Function Chaining operational data
    
    .. attribute:: nodes
    
    	Node\-specific NSH Service Function Chaining operational data
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes>`
    
    

    """

    _prefix = 'pbr-vservice-ea-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(ServiceFunctionChaining, self).__init__()
        self._top_entity = None

        self.yang_name = "service-function-chaining"
        self.yang_parent_name = "Cisco-IOS-XR-pbr-vservice-ea-oper"

        self.nodes = ServiceFunctionChaining.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")


    class Nodes(Entity):
        """
        Node\-specific NSH Service Function Chaining
        operational data
        
        .. attribute:: node
        
        	NSH operational data for a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node>`
        
        

        """

        _prefix = 'pbr-vservice-ea-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(ServiceFunctionChaining.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "service-function-chaining"

            self.node = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(ServiceFunctionChaining.Nodes, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(ServiceFunctionChaining.Nodes, self).__setattr__(name, value)


        class Node(Entity):
            """
            NSH operational data for a particular node
            
            .. attribute:: node_name  <key>
            
            	Node to collect statistics from
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: process
            
            	Client Process
            	**type**\:   :py:class:`Process <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process>`
            
            

            """

            _prefix = 'pbr-vservice-ea-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(ServiceFunctionChaining.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"

                self.node_name = YLeaf(YType.str, "node-name")

                self.process = ServiceFunctionChaining.Nodes.Node.Process()
                self.process.parent = self
                self._children_name_map["process"] = "process"
                self._children_yang_names.add("process")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("node_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(ServiceFunctionChaining.Nodes.Node, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(ServiceFunctionChaining.Nodes.Node, self).__setattr__(name, value)


            class Process(Entity):
                """
                Client Process
                
                .. attribute:: service_function
                
                	Service Function operational data
                	**type**\:   :py:class:`ServiceFunction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction>`
                
                .. attribute:: service_function_forwarder
                
                	Service Function Forwarder operational data
                	**type**\:   :py:class:`ServiceFunctionForwarder <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder>`
                
                .. attribute:: service_function_path
                
                	Service Function Path operational data
                	**type**\:   :py:class:`ServiceFunctionPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath>`
                
                

                """

                _prefix = 'pbr-vservice-ea-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ServiceFunctionChaining.Nodes.Node.Process, self).__init__()

                    self.yang_name = "process"
                    self.yang_parent_name = "node"

                    self.service_function = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction()
                    self.service_function.parent = self
                    self._children_name_map["service_function"] = "service-function"
                    self._children_yang_names.add("service-function")

                    self.service_function_forwarder = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder()
                    self.service_function_forwarder.parent = self
                    self._children_name_map["service_function_forwarder"] = "service-function-forwarder"
                    self._children_yang_names.add("service-function-forwarder")

                    self.service_function_path = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath()
                    self.service_function_path.parent = self
                    self._children_name_map["service_function_path"] = "service-function-path"
                    self._children_yang_names.add("service-function-path")


                class ServiceFunctionPath(Entity):
                    """
                    Service Function Path operational data
                    
                    .. attribute:: path_ids
                    
                    	Service Function Path Id 
                    	**type**\:   :py:class:`PathIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds>`
                    
                    

                    """

                    _prefix = 'pbr-vservice-ea-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath, self).__init__()

                        self.yang_name = "service-function-path"
                        self.yang_parent_name = "process"

                        self.path_ids = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds()
                        self.path_ids.parent = self
                        self._children_name_map["path_ids"] = "path-ids"
                        self._children_yang_names.add("path-ids")


                    class PathIds(Entity):
                        """
                        Service Function Path Id 
                        
                        .. attribute:: path_id
                        
                        	Specific Service\-Function\-Path identifier 
                        	**type**\: list of    :py:class:`PathId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId>`
                        
                        

                        """

                        _prefix = 'pbr-vservice-ea-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds, self).__init__()

                            self.yang_name = "path-ids"
                            self.yang_parent_name = "service-function-path"

                            self.path_id = YList(self)

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in () and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds, self).__setattr__(name, value)


                        class PathId(Entity):
                            """
                            Specific Service\-Function\-Path identifier 
                            
                            .. attribute:: id  <key>
                            
                            	Specific Service\-Function\-Path identifier
                            	**type**\:  int
                            
                            	**range:** 1..16777215
                            
                            .. attribute:: service_indexes
                            
                            	Service Index Belonging to Path
                            	**type**\:   :py:class:`ServiceIndexes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes>`
                            
                            .. attribute:: stats
                            
                            	SFP Statistics
                            	**type**\:   :py:class:`Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats>`
                            
                            

                            """

                            _prefix = 'pbr-vservice-ea-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId, self).__init__()

                                self.yang_name = "path-id"
                                self.yang_parent_name = "path-ids"

                                self.id = YLeaf(YType.uint32, "id")

                                self.service_indexes = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes()
                                self.service_indexes.parent = self
                                self._children_name_map["service_indexes"] = "service-indexes"
                                self._children_yang_names.add("service-indexes")

                                self.stats = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats()
                                self.stats.parent = self
                                self._children_name_map["stats"] = "stats"
                                self._children_yang_names.add("stats")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("id") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId, self).__setattr__(name, value)


                            class ServiceIndexes(Entity):
                                """
                                Service Index Belonging to Path
                                
                                .. attribute:: service_index
                                
                                	Service index operational data belonging to this path
                                	**type**\: list of    :py:class:`ServiceIndex <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex>`
                                
                                

                                """

                                _prefix = 'pbr-vservice-ea-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes, self).__init__()

                                    self.yang_name = "service-indexes"
                                    self.yang_parent_name = "path-id"

                                    self.service_index = YList(self)

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in () and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes, self).__setattr__(name, value)


                                class ServiceIndex(Entity):
                                    """
                                    Service index operational data belonging
                                    to this path
                                    
                                    .. attribute:: index  <key>
                                    
                                    	Service Index
                                    	**type**\:  int
                                    
                                    	**range:** 1..255
                                    
                                    .. attribute:: data
                                    
                                    	Statistics data
                                    	**type**\:   :py:class:`Data <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data>`
                                    
                                    .. attribute:: si_arr
                                    
                                    	SI array in case of detail stats
                                    	**type**\: list of    :py:class:`SiArr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr>`
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-ea-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex, self).__init__()

                                        self.yang_name = "service-index"
                                        self.yang_parent_name = "service-indexes"

                                        self.index = YLeaf(YType.uint32, "index")

                                        self.data = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data()
                                        self.data.parent = self
                                        self._children_name_map["data"] = "data"
                                        self._children_yang_names.add("data")

                                        self.si_arr = YList(self)

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("index") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex, self).__setattr__(name, value)


                                    class Data(Entity):
                                        """
                                        Statistics data
                                        
                                        .. attribute:: sf
                                        
                                        	Service function stats
                                        	**type**\:   :py:class:`Sf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sf>`
                                        
                                        .. attribute:: sff
                                        
                                        	Service function forwarder stats
                                        	**type**\:   :py:class:`Sff <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sff>`
                                        
                                        .. attribute:: sff_local
                                        
                                        	Local service function forwarder stats
                                        	**type**\:   :py:class:`SffLocal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.SffLocal>`
                                        
                                        .. attribute:: sfp
                                        
                                        	SFP stats
                                        	**type**\:   :py:class:`Sfp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sfp>`
                                        
                                        .. attribute:: spi_si
                                        
                                        	SPI SI stats
                                        	**type**\:   :py:class:`SpiSi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.SpiSi>`
                                        
                                        .. attribute:: term
                                        
                                        	Terminate stats
                                        	**type**\:   :py:class:`Term <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Term>`
                                        
                                        .. attribute:: type
                                        
                                        	type
                                        	**type**\:   :py:class:`VsNshStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.VsNshStats>`
                                        
                                        

                                        """

                                        _prefix = 'pbr-vservice-ea-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data, self).__init__()

                                            self.yang_name = "data"
                                            self.yang_parent_name = "service-index"

                                            self.type = YLeaf(YType.enumeration, "type")

                                            self.sf = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sf()
                                            self.sf.parent = self
                                            self._children_name_map["sf"] = "sf"
                                            self._children_yang_names.add("sf")

                                            self.sff = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sff()
                                            self.sff.parent = self
                                            self._children_name_map["sff"] = "sff"
                                            self._children_yang_names.add("sff")

                                            self.sff_local = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.SffLocal()
                                            self.sff_local.parent = self
                                            self._children_name_map["sff_local"] = "sff-local"
                                            self._children_yang_names.add("sff-local")

                                            self.sfp = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sfp()
                                            self.sfp.parent = self
                                            self._children_name_map["sfp"] = "sfp"
                                            self._children_yang_names.add("sfp")

                                            self.spi_si = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.SpiSi()
                                            self.spi_si.parent = self
                                            self._children_name_map["spi_si"] = "spi-si"
                                            self._children_yang_names.add("spi-si")

                                            self.term = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Term()
                                            self.term.parent = self
                                            self._children_name_map["term"] = "term"
                                            self._children_yang_names.add("term")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("type") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data, self).__setattr__(name, value)


                                        class Sfp(Entity):
                                            """
                                            SFP stats
                                            
                                            .. attribute:: spi_si
                                            
                                            	Service index counters
                                            	**type**\:   :py:class:`SpiSi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sfp.SpiSi>`
                                            
                                            .. attribute:: term
                                            
                                            	Terminate counters
                                            	**type**\:   :py:class:`Term <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sfp.Term>`
                                            
                                            

                                            """

                                            _prefix = 'pbr-vservice-ea-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sfp, self).__init__()

                                                self.yang_name = "sfp"
                                                self.yang_parent_name = "data"

                                                self.spi_si = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sfp.SpiSi()
                                                self.spi_si.parent = self
                                                self._children_name_map["spi_si"] = "spi-si"
                                                self._children_yang_names.add("spi-si")

                                                self.term = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sfp.Term()
                                                self.term.parent = self
                                                self._children_name_map["term"] = "term"
                                                self._children_yang_names.add("term")


                                            class SpiSi(Entity):
                                                """
                                                Service index counters
                                                
                                                .. attribute:: processed_bytes
                                                
                                                	Total bytes processed
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**units**\: byte
                                                
                                                .. attribute:: processed_pkts
                                                
                                                	Number of packets processed
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                

                                                """

                                                _prefix = 'pbr-vservice-ea-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sfp.SpiSi, self).__init__()

                                                    self.yang_name = "spi-si"
                                                    self.yang_parent_name = "sfp"

                                                    self.processed_bytes = YLeaf(YType.uint64, "processed-bytes")

                                                    self.processed_pkts = YLeaf(YType.uint64, "processed-pkts")

                                                def __setattr__(self, name, value):
                                                    self._check_monkey_patching_error(name, value)
                                                    with _handle_type_error():
                                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                                "Please use list append or extend method."
                                                                                .format(value))
                                                        if isinstance(value, Enum.YLeaf):
                                                            value = value.name
                                                        if name in ("processed_bytes",
                                                                    "processed_pkts") and name in self.__dict__:
                                                            if isinstance(value, YLeaf):
                                                                self.__dict__[name].set(value.get())
                                                            elif isinstance(value, YLeafList):
                                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sfp.SpiSi, self).__setattr__(name, value)
                                                            else:
                                                                self.__dict__[name].set(value)
                                                        else:
                                                            if hasattr(value, "parent") and name != "parent":
                                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                    value.parent = self
                                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                    value.parent = self
                                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sfp.SpiSi, self).__setattr__(name, value)

                                                def has_data(self):
                                                    return (
                                                        self.processed_bytes.is_set or
                                                        self.processed_pkts.is_set)

                                                def has_operation(self):
                                                    return (
                                                        self.yfilter != YFilter.not_set or
                                                        self.processed_bytes.yfilter != YFilter.not_set or
                                                        self.processed_pkts.yfilter != YFilter.not_set)

                                                def get_segment_path(self):
                                                    path_buffer = ""
                                                    path_buffer = "spi-si" + path_buffer

                                                    return path_buffer

                                                def get_entity_path(self, ancestor):
                                                    path_buffer = ""
                                                    if (ancestor is None):
                                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                    else:
                                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                    leaf_name_data = LeafDataList()
                                                    if (self.processed_bytes.is_set or self.processed_bytes.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.processed_bytes.get_name_leafdata())
                                                    if (self.processed_pkts.is_set or self.processed_pkts.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.processed_pkts.get_name_leafdata())

                                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                                    return entity_path

                                                def get_child_by_name(self, child_yang_name, segment_path):
                                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                    if child is not None:
                                                        return child

                                                    return None

                                                def has_leaf_or_child_of_name(self, name):
                                                    if(name == "processed-bytes" or name == "processed-pkts"):
                                                        return True
                                                    return False

                                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                                    if(value_path == "processed-bytes"):
                                                        self.processed_bytes = value
                                                        self.processed_bytes.value_namespace = name_space
                                                        self.processed_bytes.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "processed-pkts"):
                                                        self.processed_pkts = value
                                                        self.processed_pkts.value_namespace = name_space
                                                        self.processed_pkts.value_namespace_prefix = name_space_prefix


                                            class Term(Entity):
                                                """
                                                Terminate counters
                                                
                                                .. attribute:: terminated_bytes
                                                
                                                	Total bytes terminated
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**units**\: byte
                                                
                                                .. attribute:: terminated_pkts
                                                
                                                	Number of terminated packets
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                

                                                """

                                                _prefix = 'pbr-vservice-ea-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sfp.Term, self).__init__()

                                                    self.yang_name = "term"
                                                    self.yang_parent_name = "sfp"

                                                    self.terminated_bytes = YLeaf(YType.uint64, "terminated-bytes")

                                                    self.terminated_pkts = YLeaf(YType.uint64, "terminated-pkts")

                                                def __setattr__(self, name, value):
                                                    self._check_monkey_patching_error(name, value)
                                                    with _handle_type_error():
                                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                                "Please use list append or extend method."
                                                                                .format(value))
                                                        if isinstance(value, Enum.YLeaf):
                                                            value = value.name
                                                        if name in ("terminated_bytes",
                                                                    "terminated_pkts") and name in self.__dict__:
                                                            if isinstance(value, YLeaf):
                                                                self.__dict__[name].set(value.get())
                                                            elif isinstance(value, YLeafList):
                                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sfp.Term, self).__setattr__(name, value)
                                                            else:
                                                                self.__dict__[name].set(value)
                                                        else:
                                                            if hasattr(value, "parent") and name != "parent":
                                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                    value.parent = self
                                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                    value.parent = self
                                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sfp.Term, self).__setattr__(name, value)

                                                def has_data(self):
                                                    return (
                                                        self.terminated_bytes.is_set or
                                                        self.terminated_pkts.is_set)

                                                def has_operation(self):
                                                    return (
                                                        self.yfilter != YFilter.not_set or
                                                        self.terminated_bytes.yfilter != YFilter.not_set or
                                                        self.terminated_pkts.yfilter != YFilter.not_set)

                                                def get_segment_path(self):
                                                    path_buffer = ""
                                                    path_buffer = "term" + path_buffer

                                                    return path_buffer

                                                def get_entity_path(self, ancestor):
                                                    path_buffer = ""
                                                    if (ancestor is None):
                                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                    else:
                                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                    leaf_name_data = LeafDataList()
                                                    if (self.terminated_bytes.is_set or self.terminated_bytes.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.terminated_bytes.get_name_leafdata())
                                                    if (self.terminated_pkts.is_set or self.terminated_pkts.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.terminated_pkts.get_name_leafdata())

                                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                                    return entity_path

                                                def get_child_by_name(self, child_yang_name, segment_path):
                                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                    if child is not None:
                                                        return child

                                                    return None

                                                def has_leaf_or_child_of_name(self, name):
                                                    if(name == "terminated-bytes" or name == "terminated-pkts"):
                                                        return True
                                                    return False

                                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                                    if(value_path == "terminated-bytes"):
                                                        self.terminated_bytes = value
                                                        self.terminated_bytes.value_namespace = name_space
                                                        self.terminated_bytes.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "terminated-pkts"):
                                                        self.terminated_pkts = value
                                                        self.terminated_pkts.value_namespace = name_space
                                                        self.terminated_pkts.value_namespace_prefix = name_space_prefix

                                            def has_data(self):
                                                return (
                                                    (self.spi_si is not None and self.spi_si.has_data()) or
                                                    (self.term is not None and self.term.has_data()))

                                            def has_operation(self):
                                                return (
                                                    self.yfilter != YFilter.not_set or
                                                    (self.spi_si is not None and self.spi_si.has_operation()) or
                                                    (self.term is not None and self.term.has_operation()))

                                            def get_segment_path(self):
                                                path_buffer = ""
                                                path_buffer = "sfp" + path_buffer

                                                return path_buffer

                                            def get_entity_path(self, ancestor):
                                                path_buffer = ""
                                                if (ancestor is None):
                                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                else:
                                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                leaf_name_data = LeafDataList()

                                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                                return entity_path

                                            def get_child_by_name(self, child_yang_name, segment_path):
                                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                if child is not None:
                                                    return child

                                                if (child_yang_name == "spi-si"):
                                                    if (self.spi_si is None):
                                                        self.spi_si = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sfp.SpiSi()
                                                        self.spi_si.parent = self
                                                        self._children_name_map["spi_si"] = "spi-si"
                                                    return self.spi_si

                                                if (child_yang_name == "term"):
                                                    if (self.term is None):
                                                        self.term = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sfp.Term()
                                                        self.term.parent = self
                                                        self._children_name_map["term"] = "term"
                                                    return self.term

                                                return None

                                            def has_leaf_or_child_of_name(self, name):
                                                if(name == "spi-si" or name == "term"):
                                                    return True
                                                return False

                                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                                pass


                                        class SpiSi(Entity):
                                            """
                                            SPI SI stats
                                            
                                            .. attribute:: processed_bytes
                                            
                                            	Total bytes processed
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            	**units**\: byte
                                            
                                            .. attribute:: processed_pkts
                                            
                                            	Number of packets processed
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            

                                            """

                                            _prefix = 'pbr-vservice-ea-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.SpiSi, self).__init__()

                                                self.yang_name = "spi-si"
                                                self.yang_parent_name = "data"

                                                self.processed_bytes = YLeaf(YType.uint64, "processed-bytes")

                                                self.processed_pkts = YLeaf(YType.uint64, "processed-pkts")

                                            def __setattr__(self, name, value):
                                                self._check_monkey_patching_error(name, value)
                                                with _handle_type_error():
                                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                            "Please use list append or extend method."
                                                                            .format(value))
                                                    if isinstance(value, Enum.YLeaf):
                                                        value = value.name
                                                    if name in ("processed_bytes",
                                                                "processed_pkts") and name in self.__dict__:
                                                        if isinstance(value, YLeaf):
                                                            self.__dict__[name].set(value.get())
                                                        elif isinstance(value, YLeafList):
                                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.SpiSi, self).__setattr__(name, value)
                                                        else:
                                                            self.__dict__[name].set(value)
                                                    else:
                                                        if hasattr(value, "parent") and name != "parent":
                                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                value.parent = self
                                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                value.parent = self
                                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.SpiSi, self).__setattr__(name, value)

                                            def has_data(self):
                                                return (
                                                    self.processed_bytes.is_set or
                                                    self.processed_pkts.is_set)

                                            def has_operation(self):
                                                return (
                                                    self.yfilter != YFilter.not_set or
                                                    self.processed_bytes.yfilter != YFilter.not_set or
                                                    self.processed_pkts.yfilter != YFilter.not_set)

                                            def get_segment_path(self):
                                                path_buffer = ""
                                                path_buffer = "spi-si" + path_buffer

                                                return path_buffer

                                            def get_entity_path(self, ancestor):
                                                path_buffer = ""
                                                if (ancestor is None):
                                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                else:
                                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                leaf_name_data = LeafDataList()
                                                if (self.processed_bytes.is_set or self.processed_bytes.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.processed_bytes.get_name_leafdata())
                                                if (self.processed_pkts.is_set or self.processed_pkts.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.processed_pkts.get_name_leafdata())

                                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                                return entity_path

                                            def get_child_by_name(self, child_yang_name, segment_path):
                                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                if child is not None:
                                                    return child

                                                return None

                                            def has_leaf_or_child_of_name(self, name):
                                                if(name == "processed-bytes" or name == "processed-pkts"):
                                                    return True
                                                return False

                                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                                if(value_path == "processed-bytes"):
                                                    self.processed_bytes = value
                                                    self.processed_bytes.value_namespace = name_space
                                                    self.processed_bytes.value_namespace_prefix = name_space_prefix
                                                if(value_path == "processed-pkts"):
                                                    self.processed_pkts = value
                                                    self.processed_pkts.value_namespace = name_space
                                                    self.processed_pkts.value_namespace_prefix = name_space_prefix


                                        class Term(Entity):
                                            """
                                            Terminate stats
                                            
                                            .. attribute:: terminated_bytes
                                            
                                            	Total bytes terminated
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            	**units**\: byte
                                            
                                            .. attribute:: terminated_pkts
                                            
                                            	Number of terminated packets
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            

                                            """

                                            _prefix = 'pbr-vservice-ea-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Term, self).__init__()

                                                self.yang_name = "term"
                                                self.yang_parent_name = "data"

                                                self.terminated_bytes = YLeaf(YType.uint64, "terminated-bytes")

                                                self.terminated_pkts = YLeaf(YType.uint64, "terminated-pkts")

                                            def __setattr__(self, name, value):
                                                self._check_monkey_patching_error(name, value)
                                                with _handle_type_error():
                                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                            "Please use list append or extend method."
                                                                            .format(value))
                                                    if isinstance(value, Enum.YLeaf):
                                                        value = value.name
                                                    if name in ("terminated_bytes",
                                                                "terminated_pkts") and name in self.__dict__:
                                                        if isinstance(value, YLeaf):
                                                            self.__dict__[name].set(value.get())
                                                        elif isinstance(value, YLeafList):
                                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Term, self).__setattr__(name, value)
                                                        else:
                                                            self.__dict__[name].set(value)
                                                    else:
                                                        if hasattr(value, "parent") and name != "parent":
                                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                value.parent = self
                                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                value.parent = self
                                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Term, self).__setattr__(name, value)

                                            def has_data(self):
                                                return (
                                                    self.terminated_bytes.is_set or
                                                    self.terminated_pkts.is_set)

                                            def has_operation(self):
                                                return (
                                                    self.yfilter != YFilter.not_set or
                                                    self.terminated_bytes.yfilter != YFilter.not_set or
                                                    self.terminated_pkts.yfilter != YFilter.not_set)

                                            def get_segment_path(self):
                                                path_buffer = ""
                                                path_buffer = "term" + path_buffer

                                                return path_buffer

                                            def get_entity_path(self, ancestor):
                                                path_buffer = ""
                                                if (ancestor is None):
                                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                else:
                                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                leaf_name_data = LeafDataList()
                                                if (self.terminated_bytes.is_set or self.terminated_bytes.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.terminated_bytes.get_name_leafdata())
                                                if (self.terminated_pkts.is_set or self.terminated_pkts.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.terminated_pkts.get_name_leafdata())

                                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                                return entity_path

                                            def get_child_by_name(self, child_yang_name, segment_path):
                                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                if child is not None:
                                                    return child

                                                return None

                                            def has_leaf_or_child_of_name(self, name):
                                                if(name == "terminated-bytes" or name == "terminated-pkts"):
                                                    return True
                                                return False

                                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                                if(value_path == "terminated-bytes"):
                                                    self.terminated_bytes = value
                                                    self.terminated_bytes.value_namespace = name_space
                                                    self.terminated_bytes.value_namespace_prefix = name_space_prefix
                                                if(value_path == "terminated-pkts"):
                                                    self.terminated_pkts = value
                                                    self.terminated_pkts.value_namespace = name_space
                                                    self.terminated_pkts.value_namespace_prefix = name_space_prefix


                                        class Sf(Entity):
                                            """
                                            Service function stats
                                            
                                            .. attribute:: processed_bytes
                                            
                                            	Total bytes processed
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            	**units**\: byte
                                            
                                            .. attribute:: processed_pkts
                                            
                                            	Number of packets processed
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            

                                            """

                                            _prefix = 'pbr-vservice-ea-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sf, self).__init__()

                                                self.yang_name = "sf"
                                                self.yang_parent_name = "data"

                                                self.processed_bytes = YLeaf(YType.uint64, "processed-bytes")

                                                self.processed_pkts = YLeaf(YType.uint64, "processed-pkts")

                                            def __setattr__(self, name, value):
                                                self._check_monkey_patching_error(name, value)
                                                with _handle_type_error():
                                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                            "Please use list append or extend method."
                                                                            .format(value))
                                                    if isinstance(value, Enum.YLeaf):
                                                        value = value.name
                                                    if name in ("processed_bytes",
                                                                "processed_pkts") and name in self.__dict__:
                                                        if isinstance(value, YLeaf):
                                                            self.__dict__[name].set(value.get())
                                                        elif isinstance(value, YLeafList):
                                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sf, self).__setattr__(name, value)
                                                        else:
                                                            self.__dict__[name].set(value)
                                                    else:
                                                        if hasattr(value, "parent") and name != "parent":
                                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                value.parent = self
                                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                value.parent = self
                                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sf, self).__setattr__(name, value)

                                            def has_data(self):
                                                return (
                                                    self.processed_bytes.is_set or
                                                    self.processed_pkts.is_set)

                                            def has_operation(self):
                                                return (
                                                    self.yfilter != YFilter.not_set or
                                                    self.processed_bytes.yfilter != YFilter.not_set or
                                                    self.processed_pkts.yfilter != YFilter.not_set)

                                            def get_segment_path(self):
                                                path_buffer = ""
                                                path_buffer = "sf" + path_buffer

                                                return path_buffer

                                            def get_entity_path(self, ancestor):
                                                path_buffer = ""
                                                if (ancestor is None):
                                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                else:
                                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                leaf_name_data = LeafDataList()
                                                if (self.processed_bytes.is_set or self.processed_bytes.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.processed_bytes.get_name_leafdata())
                                                if (self.processed_pkts.is_set or self.processed_pkts.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.processed_pkts.get_name_leafdata())

                                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                                return entity_path

                                            def get_child_by_name(self, child_yang_name, segment_path):
                                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                if child is not None:
                                                    return child

                                                return None

                                            def has_leaf_or_child_of_name(self, name):
                                                if(name == "processed-bytes" or name == "processed-pkts"):
                                                    return True
                                                return False

                                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                                if(value_path == "processed-bytes"):
                                                    self.processed_bytes = value
                                                    self.processed_bytes.value_namespace = name_space
                                                    self.processed_bytes.value_namespace_prefix = name_space_prefix
                                                if(value_path == "processed-pkts"):
                                                    self.processed_pkts = value
                                                    self.processed_pkts.value_namespace = name_space
                                                    self.processed_pkts.value_namespace_prefix = name_space_prefix


                                        class Sff(Entity):
                                            """
                                            Service function forwarder stats
                                            
                                            .. attribute:: processed_bytes
                                            
                                            	Total bytes processed
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            	**units**\: byte
                                            
                                            .. attribute:: processed_pkts
                                            
                                            	Number of packets processed
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            

                                            """

                                            _prefix = 'pbr-vservice-ea-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sff, self).__init__()

                                                self.yang_name = "sff"
                                                self.yang_parent_name = "data"

                                                self.processed_bytes = YLeaf(YType.uint64, "processed-bytes")

                                                self.processed_pkts = YLeaf(YType.uint64, "processed-pkts")

                                            def __setattr__(self, name, value):
                                                self._check_monkey_patching_error(name, value)
                                                with _handle_type_error():
                                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                            "Please use list append or extend method."
                                                                            .format(value))
                                                    if isinstance(value, Enum.YLeaf):
                                                        value = value.name
                                                    if name in ("processed_bytes",
                                                                "processed_pkts") and name in self.__dict__:
                                                        if isinstance(value, YLeaf):
                                                            self.__dict__[name].set(value.get())
                                                        elif isinstance(value, YLeafList):
                                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sff, self).__setattr__(name, value)
                                                        else:
                                                            self.__dict__[name].set(value)
                                                    else:
                                                        if hasattr(value, "parent") and name != "parent":
                                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                value.parent = self
                                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                value.parent = self
                                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sff, self).__setattr__(name, value)

                                            def has_data(self):
                                                return (
                                                    self.processed_bytes.is_set or
                                                    self.processed_pkts.is_set)

                                            def has_operation(self):
                                                return (
                                                    self.yfilter != YFilter.not_set or
                                                    self.processed_bytes.yfilter != YFilter.not_set or
                                                    self.processed_pkts.yfilter != YFilter.not_set)

                                            def get_segment_path(self):
                                                path_buffer = ""
                                                path_buffer = "sff" + path_buffer

                                                return path_buffer

                                            def get_entity_path(self, ancestor):
                                                path_buffer = ""
                                                if (ancestor is None):
                                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                else:
                                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                leaf_name_data = LeafDataList()
                                                if (self.processed_bytes.is_set or self.processed_bytes.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.processed_bytes.get_name_leafdata())
                                                if (self.processed_pkts.is_set or self.processed_pkts.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.processed_pkts.get_name_leafdata())

                                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                                return entity_path

                                            def get_child_by_name(self, child_yang_name, segment_path):
                                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                if child is not None:
                                                    return child

                                                return None

                                            def has_leaf_or_child_of_name(self, name):
                                                if(name == "processed-bytes" or name == "processed-pkts"):
                                                    return True
                                                return False

                                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                                if(value_path == "processed-bytes"):
                                                    self.processed_bytes = value
                                                    self.processed_bytes.value_namespace = name_space
                                                    self.processed_bytes.value_namespace_prefix = name_space_prefix
                                                if(value_path == "processed-pkts"):
                                                    self.processed_pkts = value
                                                    self.processed_pkts.value_namespace = name_space
                                                    self.processed_pkts.value_namespace_prefix = name_space_prefix


                                        class SffLocal(Entity):
                                            """
                                            Local service function forwarder stats
                                            
                                            .. attribute:: lookup_err_bytes
                                            
                                            	Total bytes with unknown spi\-si
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            	**units**\: byte
                                            
                                            .. attribute:: lookup_err_pkts
                                            
                                            	Number of packets with unknown spi\-si
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            .. attribute:: malformed_err_bytes
                                            
                                            	Total bytes with invalid NSH header
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            	**units**\: byte
                                            
                                            .. attribute:: malformed_err_pkts
                                            
                                            	Number of packets with invalid NSH header
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            

                                            """

                                            _prefix = 'pbr-vservice-ea-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.SffLocal, self).__init__()

                                                self.yang_name = "sff-local"
                                                self.yang_parent_name = "data"

                                                self.lookup_err_bytes = YLeaf(YType.uint64, "lookup-err-bytes")

                                                self.lookup_err_pkts = YLeaf(YType.uint64, "lookup-err-pkts")

                                                self.malformed_err_bytes = YLeaf(YType.uint64, "malformed-err-bytes")

                                                self.malformed_err_pkts = YLeaf(YType.uint64, "malformed-err-pkts")

                                            def __setattr__(self, name, value):
                                                self._check_monkey_patching_error(name, value)
                                                with _handle_type_error():
                                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                            "Please use list append or extend method."
                                                                            .format(value))
                                                    if isinstance(value, Enum.YLeaf):
                                                        value = value.name
                                                    if name in ("lookup_err_bytes",
                                                                "lookup_err_pkts",
                                                                "malformed_err_bytes",
                                                                "malformed_err_pkts") and name in self.__dict__:
                                                        if isinstance(value, YLeaf):
                                                            self.__dict__[name].set(value.get())
                                                        elif isinstance(value, YLeafList):
                                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.SffLocal, self).__setattr__(name, value)
                                                        else:
                                                            self.__dict__[name].set(value)
                                                    else:
                                                        if hasattr(value, "parent") and name != "parent":
                                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                value.parent = self
                                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                value.parent = self
                                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.SffLocal, self).__setattr__(name, value)

                                            def has_data(self):
                                                return (
                                                    self.lookup_err_bytes.is_set or
                                                    self.lookup_err_pkts.is_set or
                                                    self.malformed_err_bytes.is_set or
                                                    self.malformed_err_pkts.is_set)

                                            def has_operation(self):
                                                return (
                                                    self.yfilter != YFilter.not_set or
                                                    self.lookup_err_bytes.yfilter != YFilter.not_set or
                                                    self.lookup_err_pkts.yfilter != YFilter.not_set or
                                                    self.malformed_err_bytes.yfilter != YFilter.not_set or
                                                    self.malformed_err_pkts.yfilter != YFilter.not_set)

                                            def get_segment_path(self):
                                                path_buffer = ""
                                                path_buffer = "sff-local" + path_buffer

                                                return path_buffer

                                            def get_entity_path(self, ancestor):
                                                path_buffer = ""
                                                if (ancestor is None):
                                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                else:
                                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                leaf_name_data = LeafDataList()
                                                if (self.lookup_err_bytes.is_set or self.lookup_err_bytes.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.lookup_err_bytes.get_name_leafdata())
                                                if (self.lookup_err_pkts.is_set or self.lookup_err_pkts.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.lookup_err_pkts.get_name_leafdata())
                                                if (self.malformed_err_bytes.is_set or self.malformed_err_bytes.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.malformed_err_bytes.get_name_leafdata())
                                                if (self.malformed_err_pkts.is_set or self.malformed_err_pkts.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.malformed_err_pkts.get_name_leafdata())

                                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                                return entity_path

                                            def get_child_by_name(self, child_yang_name, segment_path):
                                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                if child is not None:
                                                    return child

                                                return None

                                            def has_leaf_or_child_of_name(self, name):
                                                if(name == "lookup-err-bytes" or name == "lookup-err-pkts" or name == "malformed-err-bytes" or name == "malformed-err-pkts"):
                                                    return True
                                                return False

                                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                                if(value_path == "lookup-err-bytes"):
                                                    self.lookup_err_bytes = value
                                                    self.lookup_err_bytes.value_namespace = name_space
                                                    self.lookup_err_bytes.value_namespace_prefix = name_space_prefix
                                                if(value_path == "lookup-err-pkts"):
                                                    self.lookup_err_pkts = value
                                                    self.lookup_err_pkts.value_namespace = name_space
                                                    self.lookup_err_pkts.value_namespace_prefix = name_space_prefix
                                                if(value_path == "malformed-err-bytes"):
                                                    self.malformed_err_bytes = value
                                                    self.malformed_err_bytes.value_namespace = name_space
                                                    self.malformed_err_bytes.value_namespace_prefix = name_space_prefix
                                                if(value_path == "malformed-err-pkts"):
                                                    self.malformed_err_pkts = value
                                                    self.malformed_err_pkts.value_namespace = name_space
                                                    self.malformed_err_pkts.value_namespace_prefix = name_space_prefix

                                        def has_data(self):
                                            return (
                                                self.type.is_set or
                                                (self.sf is not None and self.sf.has_data()) or
                                                (self.sff is not None and self.sff.has_data()) or
                                                (self.sff_local is not None and self.sff_local.has_data()) or
                                                (self.sfp is not None and self.sfp.has_data()) or
                                                (self.spi_si is not None and self.spi_si.has_data()) or
                                                (self.term is not None and self.term.has_data()))

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.type.yfilter != YFilter.not_set or
                                                (self.sf is not None and self.sf.has_operation()) or
                                                (self.sff is not None and self.sff.has_operation()) or
                                                (self.sff_local is not None and self.sff_local.has_operation()) or
                                                (self.sfp is not None and self.sfp.has_operation()) or
                                                (self.spi_si is not None and self.spi_si.has_operation()) or
                                                (self.term is not None and self.term.has_operation()))

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "data" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.type.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            if (child_yang_name == "sf"):
                                                if (self.sf is None):
                                                    self.sf = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sf()
                                                    self.sf.parent = self
                                                    self._children_name_map["sf"] = "sf"
                                                return self.sf

                                            if (child_yang_name == "sff"):
                                                if (self.sff is None):
                                                    self.sff = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sff()
                                                    self.sff.parent = self
                                                    self._children_name_map["sff"] = "sff"
                                                return self.sff

                                            if (child_yang_name == "sff-local"):
                                                if (self.sff_local is None):
                                                    self.sff_local = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.SffLocal()
                                                    self.sff_local.parent = self
                                                    self._children_name_map["sff_local"] = "sff-local"
                                                return self.sff_local

                                            if (child_yang_name == "sfp"):
                                                if (self.sfp is None):
                                                    self.sfp = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sfp()
                                                    self.sfp.parent = self
                                                    self._children_name_map["sfp"] = "sfp"
                                                return self.sfp

                                            if (child_yang_name == "spi-si"):
                                                if (self.spi_si is None):
                                                    self.spi_si = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.SpiSi()
                                                    self.spi_si.parent = self
                                                    self._children_name_map["spi_si"] = "spi-si"
                                                return self.spi_si

                                            if (child_yang_name == "term"):
                                                if (self.term is None):
                                                    self.term = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Term()
                                                    self.term.parent = self
                                                    self._children_name_map["term"] = "term"
                                                return self.term

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "sf" or name == "sff" or name == "sff-local" or name == "sfp" or name == "spi-si" or name == "term" or name == "type"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "type"):
                                                self.type = value
                                                self.type.value_namespace = name_space
                                                self.type.value_namespace_prefix = name_space_prefix


                                    class SiArr(Entity):
                                        """
                                        SI array in case of detail stats
                                        
                                        .. attribute:: data
                                        
                                        	Stats counter for this index
                                        	**type**\:   :py:class:`Data <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data>`
                                        
                                        .. attribute:: si
                                        
                                        	Service index
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'pbr-vservice-ea-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr, self).__init__()

                                            self.yang_name = "si-arr"
                                            self.yang_parent_name = "service-index"

                                            self.si = YLeaf(YType.uint8, "si")

                                            self.data = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data()
                                            self.data.parent = self
                                            self._children_name_map["data"] = "data"
                                            self._children_yang_names.add("data")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("si") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr, self).__setattr__(name, value)


                                        class Data(Entity):
                                            """
                                            Stats counter for this index
                                            
                                            .. attribute:: spi_si
                                            
                                            	SF/SFF stats
                                            	**type**\:   :py:class:`SpiSi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data.SpiSi>`
                                            
                                            .. attribute:: term
                                            
                                            	Terminate stats
                                            	**type**\:   :py:class:`Term <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data.Term>`
                                            
                                            .. attribute:: type
                                            
                                            	type
                                            	**type**\:   :py:class:`VsNshStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.VsNshStats>`
                                            
                                            

                                            """

                                            _prefix = 'pbr-vservice-ea-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data, self).__init__()

                                                self.yang_name = "data"
                                                self.yang_parent_name = "si-arr"

                                                self.type = YLeaf(YType.enumeration, "type")

                                                self.spi_si = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data.SpiSi()
                                                self.spi_si.parent = self
                                                self._children_name_map["spi_si"] = "spi-si"
                                                self._children_yang_names.add("spi-si")

                                                self.term = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data.Term()
                                                self.term.parent = self
                                                self._children_name_map["term"] = "term"
                                                self._children_yang_names.add("term")

                                            def __setattr__(self, name, value):
                                                self._check_monkey_patching_error(name, value)
                                                with _handle_type_error():
                                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                            "Please use list append or extend method."
                                                                            .format(value))
                                                    if isinstance(value, Enum.YLeaf):
                                                        value = value.name
                                                    if name in ("type") and name in self.__dict__:
                                                        if isinstance(value, YLeaf):
                                                            self.__dict__[name].set(value.get())
                                                        elif isinstance(value, YLeafList):
                                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data, self).__setattr__(name, value)
                                                        else:
                                                            self.__dict__[name].set(value)
                                                    else:
                                                        if hasattr(value, "parent") and name != "parent":
                                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                value.parent = self
                                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                value.parent = self
                                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data, self).__setattr__(name, value)


                                            class SpiSi(Entity):
                                                """
                                                SF/SFF stats
                                                
                                                .. attribute:: processed_bytes
                                                
                                                	Total bytes processed
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**units**\: byte
                                                
                                                .. attribute:: processed_pkts
                                                
                                                	Number of packets processed
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                

                                                """

                                                _prefix = 'pbr-vservice-ea-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data.SpiSi, self).__init__()

                                                    self.yang_name = "spi-si"
                                                    self.yang_parent_name = "data"

                                                    self.processed_bytes = YLeaf(YType.uint64, "processed-bytes")

                                                    self.processed_pkts = YLeaf(YType.uint64, "processed-pkts")

                                                def __setattr__(self, name, value):
                                                    self._check_monkey_patching_error(name, value)
                                                    with _handle_type_error():
                                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                                "Please use list append or extend method."
                                                                                .format(value))
                                                        if isinstance(value, Enum.YLeaf):
                                                            value = value.name
                                                        if name in ("processed_bytes",
                                                                    "processed_pkts") and name in self.__dict__:
                                                            if isinstance(value, YLeaf):
                                                                self.__dict__[name].set(value.get())
                                                            elif isinstance(value, YLeafList):
                                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data.SpiSi, self).__setattr__(name, value)
                                                            else:
                                                                self.__dict__[name].set(value)
                                                        else:
                                                            if hasattr(value, "parent") and name != "parent":
                                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                    value.parent = self
                                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                    value.parent = self
                                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data.SpiSi, self).__setattr__(name, value)

                                                def has_data(self):
                                                    return (
                                                        self.processed_bytes.is_set or
                                                        self.processed_pkts.is_set)

                                                def has_operation(self):
                                                    return (
                                                        self.yfilter != YFilter.not_set or
                                                        self.processed_bytes.yfilter != YFilter.not_set or
                                                        self.processed_pkts.yfilter != YFilter.not_set)

                                                def get_segment_path(self):
                                                    path_buffer = ""
                                                    path_buffer = "spi-si" + path_buffer

                                                    return path_buffer

                                                def get_entity_path(self, ancestor):
                                                    path_buffer = ""
                                                    if (ancestor is None):
                                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                    else:
                                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                    leaf_name_data = LeafDataList()
                                                    if (self.processed_bytes.is_set or self.processed_bytes.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.processed_bytes.get_name_leafdata())
                                                    if (self.processed_pkts.is_set or self.processed_pkts.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.processed_pkts.get_name_leafdata())

                                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                                    return entity_path

                                                def get_child_by_name(self, child_yang_name, segment_path):
                                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                    if child is not None:
                                                        return child

                                                    return None

                                                def has_leaf_or_child_of_name(self, name):
                                                    if(name == "processed-bytes" or name == "processed-pkts"):
                                                        return True
                                                    return False

                                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                                    if(value_path == "processed-bytes"):
                                                        self.processed_bytes = value
                                                        self.processed_bytes.value_namespace = name_space
                                                        self.processed_bytes.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "processed-pkts"):
                                                        self.processed_pkts = value
                                                        self.processed_pkts.value_namespace = name_space
                                                        self.processed_pkts.value_namespace_prefix = name_space_prefix


                                            class Term(Entity):
                                                """
                                                Terminate stats
                                                
                                                .. attribute:: terminated_bytes
                                                
                                                	Total bytes terminated
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**units**\: byte
                                                
                                                .. attribute:: terminated_pkts
                                                
                                                	Number of terminated packets
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                

                                                """

                                                _prefix = 'pbr-vservice-ea-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data.Term, self).__init__()

                                                    self.yang_name = "term"
                                                    self.yang_parent_name = "data"

                                                    self.terminated_bytes = YLeaf(YType.uint64, "terminated-bytes")

                                                    self.terminated_pkts = YLeaf(YType.uint64, "terminated-pkts")

                                                def __setattr__(self, name, value):
                                                    self._check_monkey_patching_error(name, value)
                                                    with _handle_type_error():
                                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                                "Please use list append or extend method."
                                                                                .format(value))
                                                        if isinstance(value, Enum.YLeaf):
                                                            value = value.name
                                                        if name in ("terminated_bytes",
                                                                    "terminated_pkts") and name in self.__dict__:
                                                            if isinstance(value, YLeaf):
                                                                self.__dict__[name].set(value.get())
                                                            elif isinstance(value, YLeafList):
                                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data.Term, self).__setattr__(name, value)
                                                            else:
                                                                self.__dict__[name].set(value)
                                                        else:
                                                            if hasattr(value, "parent") and name != "parent":
                                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                    value.parent = self
                                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                    value.parent = self
                                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data.Term, self).__setattr__(name, value)

                                                def has_data(self):
                                                    return (
                                                        self.terminated_bytes.is_set or
                                                        self.terminated_pkts.is_set)

                                                def has_operation(self):
                                                    return (
                                                        self.yfilter != YFilter.not_set or
                                                        self.terminated_bytes.yfilter != YFilter.not_set or
                                                        self.terminated_pkts.yfilter != YFilter.not_set)

                                                def get_segment_path(self):
                                                    path_buffer = ""
                                                    path_buffer = "term" + path_buffer

                                                    return path_buffer

                                                def get_entity_path(self, ancestor):
                                                    path_buffer = ""
                                                    if (ancestor is None):
                                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                    else:
                                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                    leaf_name_data = LeafDataList()
                                                    if (self.terminated_bytes.is_set or self.terminated_bytes.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.terminated_bytes.get_name_leafdata())
                                                    if (self.terminated_pkts.is_set or self.terminated_pkts.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.terminated_pkts.get_name_leafdata())

                                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                                    return entity_path

                                                def get_child_by_name(self, child_yang_name, segment_path):
                                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                    if child is not None:
                                                        return child

                                                    return None

                                                def has_leaf_or_child_of_name(self, name):
                                                    if(name == "terminated-bytes" or name == "terminated-pkts"):
                                                        return True
                                                    return False

                                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                                    if(value_path == "terminated-bytes"):
                                                        self.terminated_bytes = value
                                                        self.terminated_bytes.value_namespace = name_space
                                                        self.terminated_bytes.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "terminated-pkts"):
                                                        self.terminated_pkts = value
                                                        self.terminated_pkts.value_namespace = name_space
                                                        self.terminated_pkts.value_namespace_prefix = name_space_prefix

                                            def has_data(self):
                                                return (
                                                    self.type.is_set or
                                                    (self.spi_si is not None and self.spi_si.has_data()) or
                                                    (self.term is not None and self.term.has_data()))

                                            def has_operation(self):
                                                return (
                                                    self.yfilter != YFilter.not_set or
                                                    self.type.yfilter != YFilter.not_set or
                                                    (self.spi_si is not None and self.spi_si.has_operation()) or
                                                    (self.term is not None and self.term.has_operation()))

                                            def get_segment_path(self):
                                                path_buffer = ""
                                                path_buffer = "data" + path_buffer

                                                return path_buffer

                                            def get_entity_path(self, ancestor):
                                                path_buffer = ""
                                                if (ancestor is None):
                                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                else:
                                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                leaf_name_data = LeafDataList()
                                                if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.type.get_name_leafdata())

                                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                                return entity_path

                                            def get_child_by_name(self, child_yang_name, segment_path):
                                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                if child is not None:
                                                    return child

                                                if (child_yang_name == "spi-si"):
                                                    if (self.spi_si is None):
                                                        self.spi_si = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data.SpiSi()
                                                        self.spi_si.parent = self
                                                        self._children_name_map["spi_si"] = "spi-si"
                                                    return self.spi_si

                                                if (child_yang_name == "term"):
                                                    if (self.term is None):
                                                        self.term = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data.Term()
                                                        self.term.parent = self
                                                        self._children_name_map["term"] = "term"
                                                    return self.term

                                                return None

                                            def has_leaf_or_child_of_name(self, name):
                                                if(name == "spi-si" or name == "term" or name == "type"):
                                                    return True
                                                return False

                                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                                if(value_path == "type"):
                                                    self.type = value
                                                    self.type.value_namespace = name_space
                                                    self.type.value_namespace_prefix = name_space_prefix

                                        def has_data(self):
                                            return (
                                                self.si.is_set or
                                                (self.data is not None and self.data.has_data()))

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.si.yfilter != YFilter.not_set or
                                                (self.data is not None and self.data.has_operation()))

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "si-arr" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.si.is_set or self.si.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.si.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            if (child_yang_name == "data"):
                                                if (self.data is None):
                                                    self.data = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data()
                                                    self.data.parent = self
                                                    self._children_name_map["data"] = "data"
                                                return self.data

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "data" or name == "si"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "si"):
                                                self.si = value
                                                self.si.value_namespace = name_space
                                                self.si.value_namespace_prefix = name_space_prefix

                                    def has_data(self):
                                        for c in self.si_arr:
                                            if (c.has_data()):
                                                return True
                                        return (
                                            self.index.is_set or
                                            (self.data is not None and self.data.has_data()))

                                    def has_operation(self):
                                        for c in self.si_arr:
                                            if (c.has_operation()):
                                                return True
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.index.yfilter != YFilter.not_set or
                                            (self.data is not None and self.data.has_operation()))

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "service-index" + "[index='" + self.index.get() + "']" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.index.is_set or self.index.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.index.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        if (child_yang_name == "data"):
                                            if (self.data is None):
                                                self.data = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data()
                                                self.data.parent = self
                                                self._children_name_map["data"] = "data"
                                            return self.data

                                        if (child_yang_name == "si-arr"):
                                            for c in self.si_arr:
                                                segment = c.get_segment_path()
                                                if (segment_path == segment):
                                                    return c
                                            c = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr()
                                            c.parent = self
                                            local_reference_key = "ydk::seg::%s" % segment_path
                                            self._local_refs[local_reference_key] = c
                                            self.si_arr.append(c)
                                            return c

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "data" or name == "si-arr" or name == "index"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "index"):
                                            self.index = value
                                            self.index.value_namespace = name_space
                                            self.index.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    for c in self.service_index:
                                        if (c.has_data()):
                                            return True
                                    return False

                                def has_operation(self):
                                    for c in self.service_index:
                                        if (c.has_operation()):
                                            return True
                                    return self.yfilter != YFilter.not_set

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "service-indexes" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "service-index"):
                                        for c in self.service_index:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.service_index.append(c)
                                        return c

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "service-index"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    pass


                            class Stats(Entity):
                                """
                                SFP Statistics
                                
                                .. attribute:: detail
                                
                                	Detail statistics per service index 
                                	**type**\:   :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail>`
                                
                                .. attribute:: summarized
                                
                                	Combined statistics of all service index in service functionpath
                                	**type**\:   :py:class:`Summarized <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized>`
                                
                                

                                """

                                _prefix = 'pbr-vservice-ea-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats, self).__init__()

                                    self.yang_name = "stats"
                                    self.yang_parent_name = "path-id"

                                    self.detail = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail()
                                    self.detail.parent = self
                                    self._children_name_map["detail"] = "detail"
                                    self._children_yang_names.add("detail")

                                    self.summarized = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized()
                                    self.summarized.parent = self
                                    self._children_name_map["summarized"] = "summarized"
                                    self._children_yang_names.add("summarized")


                                class Detail(Entity):
                                    """
                                    Detail statistics per service index 
                                    
                                    .. attribute:: data
                                    
                                    	Statistics data
                                    	**type**\:   :py:class:`Data <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data>`
                                    
                                    .. attribute:: si_arr
                                    
                                    	SI array in case of detail stats
                                    	**type**\: list of    :py:class:`SiArr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr>`
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-ea-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail, self).__init__()

                                        self.yang_name = "detail"
                                        self.yang_parent_name = "stats"

                                        self.data = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data()
                                        self.data.parent = self
                                        self._children_name_map["data"] = "data"
                                        self._children_yang_names.add("data")

                                        self.si_arr = YList(self)

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in () and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail, self).__setattr__(name, value)


                                    class Data(Entity):
                                        """
                                        Statistics data
                                        
                                        .. attribute:: sf
                                        
                                        	Service function stats
                                        	**type**\:   :py:class:`Sf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sf>`
                                        
                                        .. attribute:: sff
                                        
                                        	Service function forwarder stats
                                        	**type**\:   :py:class:`Sff <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sff>`
                                        
                                        .. attribute:: sff_local
                                        
                                        	Local service function forwarder stats
                                        	**type**\:   :py:class:`SffLocal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.SffLocal>`
                                        
                                        .. attribute:: sfp
                                        
                                        	SFP stats
                                        	**type**\:   :py:class:`Sfp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sfp>`
                                        
                                        .. attribute:: spi_si
                                        
                                        	SPI SI stats
                                        	**type**\:   :py:class:`SpiSi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.SpiSi>`
                                        
                                        .. attribute:: term
                                        
                                        	Terminate stats
                                        	**type**\:   :py:class:`Term <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Term>`
                                        
                                        .. attribute:: type
                                        
                                        	type
                                        	**type**\:   :py:class:`VsNshStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.VsNshStats>`
                                        
                                        

                                        """

                                        _prefix = 'pbr-vservice-ea-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data, self).__init__()

                                            self.yang_name = "data"
                                            self.yang_parent_name = "detail"

                                            self.type = YLeaf(YType.enumeration, "type")

                                            self.sf = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sf()
                                            self.sf.parent = self
                                            self._children_name_map["sf"] = "sf"
                                            self._children_yang_names.add("sf")

                                            self.sff = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sff()
                                            self.sff.parent = self
                                            self._children_name_map["sff"] = "sff"
                                            self._children_yang_names.add("sff")

                                            self.sff_local = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.SffLocal()
                                            self.sff_local.parent = self
                                            self._children_name_map["sff_local"] = "sff-local"
                                            self._children_yang_names.add("sff-local")

                                            self.sfp = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sfp()
                                            self.sfp.parent = self
                                            self._children_name_map["sfp"] = "sfp"
                                            self._children_yang_names.add("sfp")

                                            self.spi_si = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.SpiSi()
                                            self.spi_si.parent = self
                                            self._children_name_map["spi_si"] = "spi-si"
                                            self._children_yang_names.add("spi-si")

                                            self.term = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Term()
                                            self.term.parent = self
                                            self._children_name_map["term"] = "term"
                                            self._children_yang_names.add("term")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("type") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data, self).__setattr__(name, value)


                                        class Sfp(Entity):
                                            """
                                            SFP stats
                                            
                                            .. attribute:: spi_si
                                            
                                            	Service index counters
                                            	**type**\:   :py:class:`SpiSi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sfp.SpiSi>`
                                            
                                            .. attribute:: term
                                            
                                            	Terminate counters
                                            	**type**\:   :py:class:`Term <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sfp.Term>`
                                            
                                            

                                            """

                                            _prefix = 'pbr-vservice-ea-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sfp, self).__init__()

                                                self.yang_name = "sfp"
                                                self.yang_parent_name = "data"

                                                self.spi_si = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sfp.SpiSi()
                                                self.spi_si.parent = self
                                                self._children_name_map["spi_si"] = "spi-si"
                                                self._children_yang_names.add("spi-si")

                                                self.term = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sfp.Term()
                                                self.term.parent = self
                                                self._children_name_map["term"] = "term"
                                                self._children_yang_names.add("term")


                                            class SpiSi(Entity):
                                                """
                                                Service index counters
                                                
                                                .. attribute:: processed_bytes
                                                
                                                	Total bytes processed
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**units**\: byte
                                                
                                                .. attribute:: processed_pkts
                                                
                                                	Number of packets processed
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                

                                                """

                                                _prefix = 'pbr-vservice-ea-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sfp.SpiSi, self).__init__()

                                                    self.yang_name = "spi-si"
                                                    self.yang_parent_name = "sfp"

                                                    self.processed_bytes = YLeaf(YType.uint64, "processed-bytes")

                                                    self.processed_pkts = YLeaf(YType.uint64, "processed-pkts")

                                                def __setattr__(self, name, value):
                                                    self._check_monkey_patching_error(name, value)
                                                    with _handle_type_error():
                                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                                "Please use list append or extend method."
                                                                                .format(value))
                                                        if isinstance(value, Enum.YLeaf):
                                                            value = value.name
                                                        if name in ("processed_bytes",
                                                                    "processed_pkts") and name in self.__dict__:
                                                            if isinstance(value, YLeaf):
                                                                self.__dict__[name].set(value.get())
                                                            elif isinstance(value, YLeafList):
                                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sfp.SpiSi, self).__setattr__(name, value)
                                                            else:
                                                                self.__dict__[name].set(value)
                                                        else:
                                                            if hasattr(value, "parent") and name != "parent":
                                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                    value.parent = self
                                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                    value.parent = self
                                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sfp.SpiSi, self).__setattr__(name, value)

                                                def has_data(self):
                                                    return (
                                                        self.processed_bytes.is_set or
                                                        self.processed_pkts.is_set)

                                                def has_operation(self):
                                                    return (
                                                        self.yfilter != YFilter.not_set or
                                                        self.processed_bytes.yfilter != YFilter.not_set or
                                                        self.processed_pkts.yfilter != YFilter.not_set)

                                                def get_segment_path(self):
                                                    path_buffer = ""
                                                    path_buffer = "spi-si" + path_buffer

                                                    return path_buffer

                                                def get_entity_path(self, ancestor):
                                                    path_buffer = ""
                                                    if (ancestor is None):
                                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                    else:
                                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                    leaf_name_data = LeafDataList()
                                                    if (self.processed_bytes.is_set or self.processed_bytes.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.processed_bytes.get_name_leafdata())
                                                    if (self.processed_pkts.is_set or self.processed_pkts.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.processed_pkts.get_name_leafdata())

                                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                                    return entity_path

                                                def get_child_by_name(self, child_yang_name, segment_path):
                                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                    if child is not None:
                                                        return child

                                                    return None

                                                def has_leaf_or_child_of_name(self, name):
                                                    if(name == "processed-bytes" or name == "processed-pkts"):
                                                        return True
                                                    return False

                                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                                    if(value_path == "processed-bytes"):
                                                        self.processed_bytes = value
                                                        self.processed_bytes.value_namespace = name_space
                                                        self.processed_bytes.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "processed-pkts"):
                                                        self.processed_pkts = value
                                                        self.processed_pkts.value_namespace = name_space
                                                        self.processed_pkts.value_namespace_prefix = name_space_prefix


                                            class Term(Entity):
                                                """
                                                Terminate counters
                                                
                                                .. attribute:: terminated_bytes
                                                
                                                	Total bytes terminated
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**units**\: byte
                                                
                                                .. attribute:: terminated_pkts
                                                
                                                	Number of terminated packets
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                

                                                """

                                                _prefix = 'pbr-vservice-ea-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sfp.Term, self).__init__()

                                                    self.yang_name = "term"
                                                    self.yang_parent_name = "sfp"

                                                    self.terminated_bytes = YLeaf(YType.uint64, "terminated-bytes")

                                                    self.terminated_pkts = YLeaf(YType.uint64, "terminated-pkts")

                                                def __setattr__(self, name, value):
                                                    self._check_monkey_patching_error(name, value)
                                                    with _handle_type_error():
                                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                                "Please use list append or extend method."
                                                                                .format(value))
                                                        if isinstance(value, Enum.YLeaf):
                                                            value = value.name
                                                        if name in ("terminated_bytes",
                                                                    "terminated_pkts") and name in self.__dict__:
                                                            if isinstance(value, YLeaf):
                                                                self.__dict__[name].set(value.get())
                                                            elif isinstance(value, YLeafList):
                                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sfp.Term, self).__setattr__(name, value)
                                                            else:
                                                                self.__dict__[name].set(value)
                                                        else:
                                                            if hasattr(value, "parent") and name != "parent":
                                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                    value.parent = self
                                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                    value.parent = self
                                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sfp.Term, self).__setattr__(name, value)

                                                def has_data(self):
                                                    return (
                                                        self.terminated_bytes.is_set or
                                                        self.terminated_pkts.is_set)

                                                def has_operation(self):
                                                    return (
                                                        self.yfilter != YFilter.not_set or
                                                        self.terminated_bytes.yfilter != YFilter.not_set or
                                                        self.terminated_pkts.yfilter != YFilter.not_set)

                                                def get_segment_path(self):
                                                    path_buffer = ""
                                                    path_buffer = "term" + path_buffer

                                                    return path_buffer

                                                def get_entity_path(self, ancestor):
                                                    path_buffer = ""
                                                    if (ancestor is None):
                                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                    else:
                                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                    leaf_name_data = LeafDataList()
                                                    if (self.terminated_bytes.is_set or self.terminated_bytes.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.terminated_bytes.get_name_leafdata())
                                                    if (self.terminated_pkts.is_set or self.terminated_pkts.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.terminated_pkts.get_name_leafdata())

                                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                                    return entity_path

                                                def get_child_by_name(self, child_yang_name, segment_path):
                                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                    if child is not None:
                                                        return child

                                                    return None

                                                def has_leaf_or_child_of_name(self, name):
                                                    if(name == "terminated-bytes" or name == "terminated-pkts"):
                                                        return True
                                                    return False

                                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                                    if(value_path == "terminated-bytes"):
                                                        self.terminated_bytes = value
                                                        self.terminated_bytes.value_namespace = name_space
                                                        self.terminated_bytes.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "terminated-pkts"):
                                                        self.terminated_pkts = value
                                                        self.terminated_pkts.value_namespace = name_space
                                                        self.terminated_pkts.value_namespace_prefix = name_space_prefix

                                            def has_data(self):
                                                return (
                                                    (self.spi_si is not None and self.spi_si.has_data()) or
                                                    (self.term is not None and self.term.has_data()))

                                            def has_operation(self):
                                                return (
                                                    self.yfilter != YFilter.not_set or
                                                    (self.spi_si is not None and self.spi_si.has_operation()) or
                                                    (self.term is not None and self.term.has_operation()))

                                            def get_segment_path(self):
                                                path_buffer = ""
                                                path_buffer = "sfp" + path_buffer

                                                return path_buffer

                                            def get_entity_path(self, ancestor):
                                                path_buffer = ""
                                                if (ancestor is None):
                                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                else:
                                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                leaf_name_data = LeafDataList()

                                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                                return entity_path

                                            def get_child_by_name(self, child_yang_name, segment_path):
                                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                if child is not None:
                                                    return child

                                                if (child_yang_name == "spi-si"):
                                                    if (self.spi_si is None):
                                                        self.spi_si = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sfp.SpiSi()
                                                        self.spi_si.parent = self
                                                        self._children_name_map["spi_si"] = "spi-si"
                                                    return self.spi_si

                                                if (child_yang_name == "term"):
                                                    if (self.term is None):
                                                        self.term = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sfp.Term()
                                                        self.term.parent = self
                                                        self._children_name_map["term"] = "term"
                                                    return self.term

                                                return None

                                            def has_leaf_or_child_of_name(self, name):
                                                if(name == "spi-si" or name == "term"):
                                                    return True
                                                return False

                                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                                pass


                                        class SpiSi(Entity):
                                            """
                                            SPI SI stats
                                            
                                            .. attribute:: processed_bytes
                                            
                                            	Total bytes processed
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            	**units**\: byte
                                            
                                            .. attribute:: processed_pkts
                                            
                                            	Number of packets processed
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            

                                            """

                                            _prefix = 'pbr-vservice-ea-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.SpiSi, self).__init__()

                                                self.yang_name = "spi-si"
                                                self.yang_parent_name = "data"

                                                self.processed_bytes = YLeaf(YType.uint64, "processed-bytes")

                                                self.processed_pkts = YLeaf(YType.uint64, "processed-pkts")

                                            def __setattr__(self, name, value):
                                                self._check_monkey_patching_error(name, value)
                                                with _handle_type_error():
                                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                            "Please use list append or extend method."
                                                                            .format(value))
                                                    if isinstance(value, Enum.YLeaf):
                                                        value = value.name
                                                    if name in ("processed_bytes",
                                                                "processed_pkts") and name in self.__dict__:
                                                        if isinstance(value, YLeaf):
                                                            self.__dict__[name].set(value.get())
                                                        elif isinstance(value, YLeafList):
                                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.SpiSi, self).__setattr__(name, value)
                                                        else:
                                                            self.__dict__[name].set(value)
                                                    else:
                                                        if hasattr(value, "parent") and name != "parent":
                                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                value.parent = self
                                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                value.parent = self
                                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.SpiSi, self).__setattr__(name, value)

                                            def has_data(self):
                                                return (
                                                    self.processed_bytes.is_set or
                                                    self.processed_pkts.is_set)

                                            def has_operation(self):
                                                return (
                                                    self.yfilter != YFilter.not_set or
                                                    self.processed_bytes.yfilter != YFilter.not_set or
                                                    self.processed_pkts.yfilter != YFilter.not_set)

                                            def get_segment_path(self):
                                                path_buffer = ""
                                                path_buffer = "spi-si" + path_buffer

                                                return path_buffer

                                            def get_entity_path(self, ancestor):
                                                path_buffer = ""
                                                if (ancestor is None):
                                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                else:
                                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                leaf_name_data = LeafDataList()
                                                if (self.processed_bytes.is_set or self.processed_bytes.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.processed_bytes.get_name_leafdata())
                                                if (self.processed_pkts.is_set or self.processed_pkts.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.processed_pkts.get_name_leafdata())

                                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                                return entity_path

                                            def get_child_by_name(self, child_yang_name, segment_path):
                                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                if child is not None:
                                                    return child

                                                return None

                                            def has_leaf_or_child_of_name(self, name):
                                                if(name == "processed-bytes" or name == "processed-pkts"):
                                                    return True
                                                return False

                                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                                if(value_path == "processed-bytes"):
                                                    self.processed_bytes = value
                                                    self.processed_bytes.value_namespace = name_space
                                                    self.processed_bytes.value_namespace_prefix = name_space_prefix
                                                if(value_path == "processed-pkts"):
                                                    self.processed_pkts = value
                                                    self.processed_pkts.value_namespace = name_space
                                                    self.processed_pkts.value_namespace_prefix = name_space_prefix


                                        class Term(Entity):
                                            """
                                            Terminate stats
                                            
                                            .. attribute:: terminated_bytes
                                            
                                            	Total bytes terminated
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            	**units**\: byte
                                            
                                            .. attribute:: terminated_pkts
                                            
                                            	Number of terminated packets
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            

                                            """

                                            _prefix = 'pbr-vservice-ea-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Term, self).__init__()

                                                self.yang_name = "term"
                                                self.yang_parent_name = "data"

                                                self.terminated_bytes = YLeaf(YType.uint64, "terminated-bytes")

                                                self.terminated_pkts = YLeaf(YType.uint64, "terminated-pkts")

                                            def __setattr__(self, name, value):
                                                self._check_monkey_patching_error(name, value)
                                                with _handle_type_error():
                                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                            "Please use list append or extend method."
                                                                            .format(value))
                                                    if isinstance(value, Enum.YLeaf):
                                                        value = value.name
                                                    if name in ("terminated_bytes",
                                                                "terminated_pkts") and name in self.__dict__:
                                                        if isinstance(value, YLeaf):
                                                            self.__dict__[name].set(value.get())
                                                        elif isinstance(value, YLeafList):
                                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Term, self).__setattr__(name, value)
                                                        else:
                                                            self.__dict__[name].set(value)
                                                    else:
                                                        if hasattr(value, "parent") and name != "parent":
                                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                value.parent = self
                                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                value.parent = self
                                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Term, self).__setattr__(name, value)

                                            def has_data(self):
                                                return (
                                                    self.terminated_bytes.is_set or
                                                    self.terminated_pkts.is_set)

                                            def has_operation(self):
                                                return (
                                                    self.yfilter != YFilter.not_set or
                                                    self.terminated_bytes.yfilter != YFilter.not_set or
                                                    self.terminated_pkts.yfilter != YFilter.not_set)

                                            def get_segment_path(self):
                                                path_buffer = ""
                                                path_buffer = "term" + path_buffer

                                                return path_buffer

                                            def get_entity_path(self, ancestor):
                                                path_buffer = ""
                                                if (ancestor is None):
                                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                else:
                                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                leaf_name_data = LeafDataList()
                                                if (self.terminated_bytes.is_set or self.terminated_bytes.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.terminated_bytes.get_name_leafdata())
                                                if (self.terminated_pkts.is_set or self.terminated_pkts.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.terminated_pkts.get_name_leafdata())

                                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                                return entity_path

                                            def get_child_by_name(self, child_yang_name, segment_path):
                                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                if child is not None:
                                                    return child

                                                return None

                                            def has_leaf_or_child_of_name(self, name):
                                                if(name == "terminated-bytes" or name == "terminated-pkts"):
                                                    return True
                                                return False

                                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                                if(value_path == "terminated-bytes"):
                                                    self.terminated_bytes = value
                                                    self.terminated_bytes.value_namespace = name_space
                                                    self.terminated_bytes.value_namespace_prefix = name_space_prefix
                                                if(value_path == "terminated-pkts"):
                                                    self.terminated_pkts = value
                                                    self.terminated_pkts.value_namespace = name_space
                                                    self.terminated_pkts.value_namespace_prefix = name_space_prefix


                                        class Sf(Entity):
                                            """
                                            Service function stats
                                            
                                            .. attribute:: processed_bytes
                                            
                                            	Total bytes processed
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            	**units**\: byte
                                            
                                            .. attribute:: processed_pkts
                                            
                                            	Number of packets processed
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            

                                            """

                                            _prefix = 'pbr-vservice-ea-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sf, self).__init__()

                                                self.yang_name = "sf"
                                                self.yang_parent_name = "data"

                                                self.processed_bytes = YLeaf(YType.uint64, "processed-bytes")

                                                self.processed_pkts = YLeaf(YType.uint64, "processed-pkts")

                                            def __setattr__(self, name, value):
                                                self._check_monkey_patching_error(name, value)
                                                with _handle_type_error():
                                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                            "Please use list append or extend method."
                                                                            .format(value))
                                                    if isinstance(value, Enum.YLeaf):
                                                        value = value.name
                                                    if name in ("processed_bytes",
                                                                "processed_pkts") and name in self.__dict__:
                                                        if isinstance(value, YLeaf):
                                                            self.__dict__[name].set(value.get())
                                                        elif isinstance(value, YLeafList):
                                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sf, self).__setattr__(name, value)
                                                        else:
                                                            self.__dict__[name].set(value)
                                                    else:
                                                        if hasattr(value, "parent") and name != "parent":
                                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                value.parent = self
                                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                value.parent = self
                                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sf, self).__setattr__(name, value)

                                            def has_data(self):
                                                return (
                                                    self.processed_bytes.is_set or
                                                    self.processed_pkts.is_set)

                                            def has_operation(self):
                                                return (
                                                    self.yfilter != YFilter.not_set or
                                                    self.processed_bytes.yfilter != YFilter.not_set or
                                                    self.processed_pkts.yfilter != YFilter.not_set)

                                            def get_segment_path(self):
                                                path_buffer = ""
                                                path_buffer = "sf" + path_buffer

                                                return path_buffer

                                            def get_entity_path(self, ancestor):
                                                path_buffer = ""
                                                if (ancestor is None):
                                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                else:
                                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                leaf_name_data = LeafDataList()
                                                if (self.processed_bytes.is_set or self.processed_bytes.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.processed_bytes.get_name_leafdata())
                                                if (self.processed_pkts.is_set or self.processed_pkts.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.processed_pkts.get_name_leafdata())

                                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                                return entity_path

                                            def get_child_by_name(self, child_yang_name, segment_path):
                                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                if child is not None:
                                                    return child

                                                return None

                                            def has_leaf_or_child_of_name(self, name):
                                                if(name == "processed-bytes" or name == "processed-pkts"):
                                                    return True
                                                return False

                                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                                if(value_path == "processed-bytes"):
                                                    self.processed_bytes = value
                                                    self.processed_bytes.value_namespace = name_space
                                                    self.processed_bytes.value_namespace_prefix = name_space_prefix
                                                if(value_path == "processed-pkts"):
                                                    self.processed_pkts = value
                                                    self.processed_pkts.value_namespace = name_space
                                                    self.processed_pkts.value_namespace_prefix = name_space_prefix


                                        class Sff(Entity):
                                            """
                                            Service function forwarder stats
                                            
                                            .. attribute:: processed_bytes
                                            
                                            	Total bytes processed
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            	**units**\: byte
                                            
                                            .. attribute:: processed_pkts
                                            
                                            	Number of packets processed
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            

                                            """

                                            _prefix = 'pbr-vservice-ea-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sff, self).__init__()

                                                self.yang_name = "sff"
                                                self.yang_parent_name = "data"

                                                self.processed_bytes = YLeaf(YType.uint64, "processed-bytes")

                                                self.processed_pkts = YLeaf(YType.uint64, "processed-pkts")

                                            def __setattr__(self, name, value):
                                                self._check_monkey_patching_error(name, value)
                                                with _handle_type_error():
                                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                            "Please use list append or extend method."
                                                                            .format(value))
                                                    if isinstance(value, Enum.YLeaf):
                                                        value = value.name
                                                    if name in ("processed_bytes",
                                                                "processed_pkts") and name in self.__dict__:
                                                        if isinstance(value, YLeaf):
                                                            self.__dict__[name].set(value.get())
                                                        elif isinstance(value, YLeafList):
                                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sff, self).__setattr__(name, value)
                                                        else:
                                                            self.__dict__[name].set(value)
                                                    else:
                                                        if hasattr(value, "parent") and name != "parent":
                                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                value.parent = self
                                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                value.parent = self
                                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sff, self).__setattr__(name, value)

                                            def has_data(self):
                                                return (
                                                    self.processed_bytes.is_set or
                                                    self.processed_pkts.is_set)

                                            def has_operation(self):
                                                return (
                                                    self.yfilter != YFilter.not_set or
                                                    self.processed_bytes.yfilter != YFilter.not_set or
                                                    self.processed_pkts.yfilter != YFilter.not_set)

                                            def get_segment_path(self):
                                                path_buffer = ""
                                                path_buffer = "sff" + path_buffer

                                                return path_buffer

                                            def get_entity_path(self, ancestor):
                                                path_buffer = ""
                                                if (ancestor is None):
                                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                else:
                                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                leaf_name_data = LeafDataList()
                                                if (self.processed_bytes.is_set or self.processed_bytes.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.processed_bytes.get_name_leafdata())
                                                if (self.processed_pkts.is_set or self.processed_pkts.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.processed_pkts.get_name_leafdata())

                                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                                return entity_path

                                            def get_child_by_name(self, child_yang_name, segment_path):
                                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                if child is not None:
                                                    return child

                                                return None

                                            def has_leaf_or_child_of_name(self, name):
                                                if(name == "processed-bytes" or name == "processed-pkts"):
                                                    return True
                                                return False

                                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                                if(value_path == "processed-bytes"):
                                                    self.processed_bytes = value
                                                    self.processed_bytes.value_namespace = name_space
                                                    self.processed_bytes.value_namespace_prefix = name_space_prefix
                                                if(value_path == "processed-pkts"):
                                                    self.processed_pkts = value
                                                    self.processed_pkts.value_namespace = name_space
                                                    self.processed_pkts.value_namespace_prefix = name_space_prefix


                                        class SffLocal(Entity):
                                            """
                                            Local service function forwarder stats
                                            
                                            .. attribute:: lookup_err_bytes
                                            
                                            	Total bytes with unknown spi\-si
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            	**units**\: byte
                                            
                                            .. attribute:: lookup_err_pkts
                                            
                                            	Number of packets with unknown spi\-si
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            .. attribute:: malformed_err_bytes
                                            
                                            	Total bytes with invalid NSH header
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            	**units**\: byte
                                            
                                            .. attribute:: malformed_err_pkts
                                            
                                            	Number of packets with invalid NSH header
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            

                                            """

                                            _prefix = 'pbr-vservice-ea-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.SffLocal, self).__init__()

                                                self.yang_name = "sff-local"
                                                self.yang_parent_name = "data"

                                                self.lookup_err_bytes = YLeaf(YType.uint64, "lookup-err-bytes")

                                                self.lookup_err_pkts = YLeaf(YType.uint64, "lookup-err-pkts")

                                                self.malformed_err_bytes = YLeaf(YType.uint64, "malformed-err-bytes")

                                                self.malformed_err_pkts = YLeaf(YType.uint64, "malformed-err-pkts")

                                            def __setattr__(self, name, value):
                                                self._check_monkey_patching_error(name, value)
                                                with _handle_type_error():
                                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                            "Please use list append or extend method."
                                                                            .format(value))
                                                    if isinstance(value, Enum.YLeaf):
                                                        value = value.name
                                                    if name in ("lookup_err_bytes",
                                                                "lookup_err_pkts",
                                                                "malformed_err_bytes",
                                                                "malformed_err_pkts") and name in self.__dict__:
                                                        if isinstance(value, YLeaf):
                                                            self.__dict__[name].set(value.get())
                                                        elif isinstance(value, YLeafList):
                                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.SffLocal, self).__setattr__(name, value)
                                                        else:
                                                            self.__dict__[name].set(value)
                                                    else:
                                                        if hasattr(value, "parent") and name != "parent":
                                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                value.parent = self
                                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                value.parent = self
                                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.SffLocal, self).__setattr__(name, value)

                                            def has_data(self):
                                                return (
                                                    self.lookup_err_bytes.is_set or
                                                    self.lookup_err_pkts.is_set or
                                                    self.malformed_err_bytes.is_set or
                                                    self.malformed_err_pkts.is_set)

                                            def has_operation(self):
                                                return (
                                                    self.yfilter != YFilter.not_set or
                                                    self.lookup_err_bytes.yfilter != YFilter.not_set or
                                                    self.lookup_err_pkts.yfilter != YFilter.not_set or
                                                    self.malformed_err_bytes.yfilter != YFilter.not_set or
                                                    self.malformed_err_pkts.yfilter != YFilter.not_set)

                                            def get_segment_path(self):
                                                path_buffer = ""
                                                path_buffer = "sff-local" + path_buffer

                                                return path_buffer

                                            def get_entity_path(self, ancestor):
                                                path_buffer = ""
                                                if (ancestor is None):
                                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                else:
                                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                leaf_name_data = LeafDataList()
                                                if (self.lookup_err_bytes.is_set or self.lookup_err_bytes.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.lookup_err_bytes.get_name_leafdata())
                                                if (self.lookup_err_pkts.is_set or self.lookup_err_pkts.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.lookup_err_pkts.get_name_leafdata())
                                                if (self.malformed_err_bytes.is_set or self.malformed_err_bytes.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.malformed_err_bytes.get_name_leafdata())
                                                if (self.malformed_err_pkts.is_set or self.malformed_err_pkts.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.malformed_err_pkts.get_name_leafdata())

                                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                                return entity_path

                                            def get_child_by_name(self, child_yang_name, segment_path):
                                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                if child is not None:
                                                    return child

                                                return None

                                            def has_leaf_or_child_of_name(self, name):
                                                if(name == "lookup-err-bytes" or name == "lookup-err-pkts" or name == "malformed-err-bytes" or name == "malformed-err-pkts"):
                                                    return True
                                                return False

                                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                                if(value_path == "lookup-err-bytes"):
                                                    self.lookup_err_bytes = value
                                                    self.lookup_err_bytes.value_namespace = name_space
                                                    self.lookup_err_bytes.value_namespace_prefix = name_space_prefix
                                                if(value_path == "lookup-err-pkts"):
                                                    self.lookup_err_pkts = value
                                                    self.lookup_err_pkts.value_namespace = name_space
                                                    self.lookup_err_pkts.value_namespace_prefix = name_space_prefix
                                                if(value_path == "malformed-err-bytes"):
                                                    self.malformed_err_bytes = value
                                                    self.malformed_err_bytes.value_namespace = name_space
                                                    self.malformed_err_bytes.value_namespace_prefix = name_space_prefix
                                                if(value_path == "malformed-err-pkts"):
                                                    self.malformed_err_pkts = value
                                                    self.malformed_err_pkts.value_namespace = name_space
                                                    self.malformed_err_pkts.value_namespace_prefix = name_space_prefix

                                        def has_data(self):
                                            return (
                                                self.type.is_set or
                                                (self.sf is not None and self.sf.has_data()) or
                                                (self.sff is not None and self.sff.has_data()) or
                                                (self.sff_local is not None and self.sff_local.has_data()) or
                                                (self.sfp is not None and self.sfp.has_data()) or
                                                (self.spi_si is not None and self.spi_si.has_data()) or
                                                (self.term is not None and self.term.has_data()))

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.type.yfilter != YFilter.not_set or
                                                (self.sf is not None and self.sf.has_operation()) or
                                                (self.sff is not None and self.sff.has_operation()) or
                                                (self.sff_local is not None and self.sff_local.has_operation()) or
                                                (self.sfp is not None and self.sfp.has_operation()) or
                                                (self.spi_si is not None and self.spi_si.has_operation()) or
                                                (self.term is not None and self.term.has_operation()))

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "data" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.type.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            if (child_yang_name == "sf"):
                                                if (self.sf is None):
                                                    self.sf = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sf()
                                                    self.sf.parent = self
                                                    self._children_name_map["sf"] = "sf"
                                                return self.sf

                                            if (child_yang_name == "sff"):
                                                if (self.sff is None):
                                                    self.sff = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sff()
                                                    self.sff.parent = self
                                                    self._children_name_map["sff"] = "sff"
                                                return self.sff

                                            if (child_yang_name == "sff-local"):
                                                if (self.sff_local is None):
                                                    self.sff_local = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.SffLocal()
                                                    self.sff_local.parent = self
                                                    self._children_name_map["sff_local"] = "sff-local"
                                                return self.sff_local

                                            if (child_yang_name == "sfp"):
                                                if (self.sfp is None):
                                                    self.sfp = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sfp()
                                                    self.sfp.parent = self
                                                    self._children_name_map["sfp"] = "sfp"
                                                return self.sfp

                                            if (child_yang_name == "spi-si"):
                                                if (self.spi_si is None):
                                                    self.spi_si = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.SpiSi()
                                                    self.spi_si.parent = self
                                                    self._children_name_map["spi_si"] = "spi-si"
                                                return self.spi_si

                                            if (child_yang_name == "term"):
                                                if (self.term is None):
                                                    self.term = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Term()
                                                    self.term.parent = self
                                                    self._children_name_map["term"] = "term"
                                                return self.term

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "sf" or name == "sff" or name == "sff-local" or name == "sfp" or name == "spi-si" or name == "term" or name == "type"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "type"):
                                                self.type = value
                                                self.type.value_namespace = name_space
                                                self.type.value_namespace_prefix = name_space_prefix


                                    class SiArr(Entity):
                                        """
                                        SI array in case of detail stats
                                        
                                        .. attribute:: data
                                        
                                        	Stats counter for this index
                                        	**type**\:   :py:class:`Data <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data>`
                                        
                                        .. attribute:: si
                                        
                                        	Service index
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'pbr-vservice-ea-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr, self).__init__()

                                            self.yang_name = "si-arr"
                                            self.yang_parent_name = "detail"

                                            self.si = YLeaf(YType.uint8, "si")

                                            self.data = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data()
                                            self.data.parent = self
                                            self._children_name_map["data"] = "data"
                                            self._children_yang_names.add("data")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("si") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr, self).__setattr__(name, value)


                                        class Data(Entity):
                                            """
                                            Stats counter for this index
                                            
                                            .. attribute:: spi_si
                                            
                                            	SF/SFF stats
                                            	**type**\:   :py:class:`SpiSi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data.SpiSi>`
                                            
                                            .. attribute:: term
                                            
                                            	Terminate stats
                                            	**type**\:   :py:class:`Term <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data.Term>`
                                            
                                            .. attribute:: type
                                            
                                            	type
                                            	**type**\:   :py:class:`VsNshStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.VsNshStats>`
                                            
                                            

                                            """

                                            _prefix = 'pbr-vservice-ea-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data, self).__init__()

                                                self.yang_name = "data"
                                                self.yang_parent_name = "si-arr"

                                                self.type = YLeaf(YType.enumeration, "type")

                                                self.spi_si = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data.SpiSi()
                                                self.spi_si.parent = self
                                                self._children_name_map["spi_si"] = "spi-si"
                                                self._children_yang_names.add("spi-si")

                                                self.term = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data.Term()
                                                self.term.parent = self
                                                self._children_name_map["term"] = "term"
                                                self._children_yang_names.add("term")

                                            def __setattr__(self, name, value):
                                                self._check_monkey_patching_error(name, value)
                                                with _handle_type_error():
                                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                            "Please use list append or extend method."
                                                                            .format(value))
                                                    if isinstance(value, Enum.YLeaf):
                                                        value = value.name
                                                    if name in ("type") and name in self.__dict__:
                                                        if isinstance(value, YLeaf):
                                                            self.__dict__[name].set(value.get())
                                                        elif isinstance(value, YLeafList):
                                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data, self).__setattr__(name, value)
                                                        else:
                                                            self.__dict__[name].set(value)
                                                    else:
                                                        if hasattr(value, "parent") and name != "parent":
                                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                value.parent = self
                                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                value.parent = self
                                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data, self).__setattr__(name, value)


                                            class SpiSi(Entity):
                                                """
                                                SF/SFF stats
                                                
                                                .. attribute:: processed_bytes
                                                
                                                	Total bytes processed
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**units**\: byte
                                                
                                                .. attribute:: processed_pkts
                                                
                                                	Number of packets processed
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                

                                                """

                                                _prefix = 'pbr-vservice-ea-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data.SpiSi, self).__init__()

                                                    self.yang_name = "spi-si"
                                                    self.yang_parent_name = "data"

                                                    self.processed_bytes = YLeaf(YType.uint64, "processed-bytes")

                                                    self.processed_pkts = YLeaf(YType.uint64, "processed-pkts")

                                                def __setattr__(self, name, value):
                                                    self._check_monkey_patching_error(name, value)
                                                    with _handle_type_error():
                                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                                "Please use list append or extend method."
                                                                                .format(value))
                                                        if isinstance(value, Enum.YLeaf):
                                                            value = value.name
                                                        if name in ("processed_bytes",
                                                                    "processed_pkts") and name in self.__dict__:
                                                            if isinstance(value, YLeaf):
                                                                self.__dict__[name].set(value.get())
                                                            elif isinstance(value, YLeafList):
                                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data.SpiSi, self).__setattr__(name, value)
                                                            else:
                                                                self.__dict__[name].set(value)
                                                        else:
                                                            if hasattr(value, "parent") and name != "parent":
                                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                    value.parent = self
                                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                    value.parent = self
                                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data.SpiSi, self).__setattr__(name, value)

                                                def has_data(self):
                                                    return (
                                                        self.processed_bytes.is_set or
                                                        self.processed_pkts.is_set)

                                                def has_operation(self):
                                                    return (
                                                        self.yfilter != YFilter.not_set or
                                                        self.processed_bytes.yfilter != YFilter.not_set or
                                                        self.processed_pkts.yfilter != YFilter.not_set)

                                                def get_segment_path(self):
                                                    path_buffer = ""
                                                    path_buffer = "spi-si" + path_buffer

                                                    return path_buffer

                                                def get_entity_path(self, ancestor):
                                                    path_buffer = ""
                                                    if (ancestor is None):
                                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                    else:
                                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                    leaf_name_data = LeafDataList()
                                                    if (self.processed_bytes.is_set or self.processed_bytes.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.processed_bytes.get_name_leafdata())
                                                    if (self.processed_pkts.is_set or self.processed_pkts.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.processed_pkts.get_name_leafdata())

                                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                                    return entity_path

                                                def get_child_by_name(self, child_yang_name, segment_path):
                                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                    if child is not None:
                                                        return child

                                                    return None

                                                def has_leaf_or_child_of_name(self, name):
                                                    if(name == "processed-bytes" or name == "processed-pkts"):
                                                        return True
                                                    return False

                                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                                    if(value_path == "processed-bytes"):
                                                        self.processed_bytes = value
                                                        self.processed_bytes.value_namespace = name_space
                                                        self.processed_bytes.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "processed-pkts"):
                                                        self.processed_pkts = value
                                                        self.processed_pkts.value_namespace = name_space
                                                        self.processed_pkts.value_namespace_prefix = name_space_prefix


                                            class Term(Entity):
                                                """
                                                Terminate stats
                                                
                                                .. attribute:: terminated_bytes
                                                
                                                	Total bytes terminated
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**units**\: byte
                                                
                                                .. attribute:: terminated_pkts
                                                
                                                	Number of terminated packets
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                

                                                """

                                                _prefix = 'pbr-vservice-ea-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data.Term, self).__init__()

                                                    self.yang_name = "term"
                                                    self.yang_parent_name = "data"

                                                    self.terminated_bytes = YLeaf(YType.uint64, "terminated-bytes")

                                                    self.terminated_pkts = YLeaf(YType.uint64, "terminated-pkts")

                                                def __setattr__(self, name, value):
                                                    self._check_monkey_patching_error(name, value)
                                                    with _handle_type_error():
                                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                                "Please use list append or extend method."
                                                                                .format(value))
                                                        if isinstance(value, Enum.YLeaf):
                                                            value = value.name
                                                        if name in ("terminated_bytes",
                                                                    "terminated_pkts") and name in self.__dict__:
                                                            if isinstance(value, YLeaf):
                                                                self.__dict__[name].set(value.get())
                                                            elif isinstance(value, YLeafList):
                                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data.Term, self).__setattr__(name, value)
                                                            else:
                                                                self.__dict__[name].set(value)
                                                        else:
                                                            if hasattr(value, "parent") and name != "parent":
                                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                    value.parent = self
                                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                    value.parent = self
                                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data.Term, self).__setattr__(name, value)

                                                def has_data(self):
                                                    return (
                                                        self.terminated_bytes.is_set or
                                                        self.terminated_pkts.is_set)

                                                def has_operation(self):
                                                    return (
                                                        self.yfilter != YFilter.not_set or
                                                        self.terminated_bytes.yfilter != YFilter.not_set or
                                                        self.terminated_pkts.yfilter != YFilter.not_set)

                                                def get_segment_path(self):
                                                    path_buffer = ""
                                                    path_buffer = "term" + path_buffer

                                                    return path_buffer

                                                def get_entity_path(self, ancestor):
                                                    path_buffer = ""
                                                    if (ancestor is None):
                                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                    else:
                                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                    leaf_name_data = LeafDataList()
                                                    if (self.terminated_bytes.is_set or self.terminated_bytes.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.terminated_bytes.get_name_leafdata())
                                                    if (self.terminated_pkts.is_set or self.terminated_pkts.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.terminated_pkts.get_name_leafdata())

                                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                                    return entity_path

                                                def get_child_by_name(self, child_yang_name, segment_path):
                                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                    if child is not None:
                                                        return child

                                                    return None

                                                def has_leaf_or_child_of_name(self, name):
                                                    if(name == "terminated-bytes" or name == "terminated-pkts"):
                                                        return True
                                                    return False

                                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                                    if(value_path == "terminated-bytes"):
                                                        self.terminated_bytes = value
                                                        self.terminated_bytes.value_namespace = name_space
                                                        self.terminated_bytes.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "terminated-pkts"):
                                                        self.terminated_pkts = value
                                                        self.terminated_pkts.value_namespace = name_space
                                                        self.terminated_pkts.value_namespace_prefix = name_space_prefix

                                            def has_data(self):
                                                return (
                                                    self.type.is_set or
                                                    (self.spi_si is not None and self.spi_si.has_data()) or
                                                    (self.term is not None and self.term.has_data()))

                                            def has_operation(self):
                                                return (
                                                    self.yfilter != YFilter.not_set or
                                                    self.type.yfilter != YFilter.not_set or
                                                    (self.spi_si is not None and self.spi_si.has_operation()) or
                                                    (self.term is not None and self.term.has_operation()))

                                            def get_segment_path(self):
                                                path_buffer = ""
                                                path_buffer = "data" + path_buffer

                                                return path_buffer

                                            def get_entity_path(self, ancestor):
                                                path_buffer = ""
                                                if (ancestor is None):
                                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                else:
                                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                leaf_name_data = LeafDataList()
                                                if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.type.get_name_leafdata())

                                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                                return entity_path

                                            def get_child_by_name(self, child_yang_name, segment_path):
                                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                if child is not None:
                                                    return child

                                                if (child_yang_name == "spi-si"):
                                                    if (self.spi_si is None):
                                                        self.spi_si = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data.SpiSi()
                                                        self.spi_si.parent = self
                                                        self._children_name_map["spi_si"] = "spi-si"
                                                    return self.spi_si

                                                if (child_yang_name == "term"):
                                                    if (self.term is None):
                                                        self.term = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data.Term()
                                                        self.term.parent = self
                                                        self._children_name_map["term"] = "term"
                                                    return self.term

                                                return None

                                            def has_leaf_or_child_of_name(self, name):
                                                if(name == "spi-si" or name == "term" or name == "type"):
                                                    return True
                                                return False

                                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                                if(value_path == "type"):
                                                    self.type = value
                                                    self.type.value_namespace = name_space
                                                    self.type.value_namespace_prefix = name_space_prefix

                                        def has_data(self):
                                            return (
                                                self.si.is_set or
                                                (self.data is not None and self.data.has_data()))

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.si.yfilter != YFilter.not_set or
                                                (self.data is not None and self.data.has_operation()))

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "si-arr" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.si.is_set or self.si.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.si.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            if (child_yang_name == "data"):
                                                if (self.data is None):
                                                    self.data = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data()
                                                    self.data.parent = self
                                                    self._children_name_map["data"] = "data"
                                                return self.data

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "data" or name == "si"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "si"):
                                                self.si = value
                                                self.si.value_namespace = name_space
                                                self.si.value_namespace_prefix = name_space_prefix

                                    def has_data(self):
                                        for c in self.si_arr:
                                            if (c.has_data()):
                                                return True
                                        return (self.data is not None and self.data.has_data())

                                    def has_operation(self):
                                        for c in self.si_arr:
                                            if (c.has_operation()):
                                                return True
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            (self.data is not None and self.data.has_operation()))

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "detail" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        if (child_yang_name == "data"):
                                            if (self.data is None):
                                                self.data = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data()
                                                self.data.parent = self
                                                self._children_name_map["data"] = "data"
                                            return self.data

                                        if (child_yang_name == "si-arr"):
                                            for c in self.si_arr:
                                                segment = c.get_segment_path()
                                                if (segment_path == segment):
                                                    return c
                                            c = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr()
                                            c.parent = self
                                            local_reference_key = "ydk::seg::%s" % segment_path
                                            self._local_refs[local_reference_key] = c
                                            self.si_arr.append(c)
                                            return c

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "data" or name == "si-arr"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        pass


                                class Summarized(Entity):
                                    """
                                    Combined statistics of all service index
                                    in service functionpath
                                    
                                    .. attribute:: data
                                    
                                    	Statistics data
                                    	**type**\:   :py:class:`Data <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data>`
                                    
                                    .. attribute:: si_arr
                                    
                                    	SI array in case of detail stats
                                    	**type**\: list of    :py:class:`SiArr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr>`
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-ea-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized, self).__init__()

                                        self.yang_name = "summarized"
                                        self.yang_parent_name = "stats"

                                        self.data = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data()
                                        self.data.parent = self
                                        self._children_name_map["data"] = "data"
                                        self._children_yang_names.add("data")

                                        self.si_arr = YList(self)

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in () and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized, self).__setattr__(name, value)


                                    class Data(Entity):
                                        """
                                        Statistics data
                                        
                                        .. attribute:: sf
                                        
                                        	Service function stats
                                        	**type**\:   :py:class:`Sf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sf>`
                                        
                                        .. attribute:: sff
                                        
                                        	Service function forwarder stats
                                        	**type**\:   :py:class:`Sff <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sff>`
                                        
                                        .. attribute:: sff_local
                                        
                                        	Local service function forwarder stats
                                        	**type**\:   :py:class:`SffLocal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.SffLocal>`
                                        
                                        .. attribute:: sfp
                                        
                                        	SFP stats
                                        	**type**\:   :py:class:`Sfp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sfp>`
                                        
                                        .. attribute:: spi_si
                                        
                                        	SPI SI stats
                                        	**type**\:   :py:class:`SpiSi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.SpiSi>`
                                        
                                        .. attribute:: term
                                        
                                        	Terminate stats
                                        	**type**\:   :py:class:`Term <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Term>`
                                        
                                        .. attribute:: type
                                        
                                        	type
                                        	**type**\:   :py:class:`VsNshStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.VsNshStats>`
                                        
                                        

                                        """

                                        _prefix = 'pbr-vservice-ea-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data, self).__init__()

                                            self.yang_name = "data"
                                            self.yang_parent_name = "summarized"

                                            self.type = YLeaf(YType.enumeration, "type")

                                            self.sf = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sf()
                                            self.sf.parent = self
                                            self._children_name_map["sf"] = "sf"
                                            self._children_yang_names.add("sf")

                                            self.sff = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sff()
                                            self.sff.parent = self
                                            self._children_name_map["sff"] = "sff"
                                            self._children_yang_names.add("sff")

                                            self.sff_local = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.SffLocal()
                                            self.sff_local.parent = self
                                            self._children_name_map["sff_local"] = "sff-local"
                                            self._children_yang_names.add("sff-local")

                                            self.sfp = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sfp()
                                            self.sfp.parent = self
                                            self._children_name_map["sfp"] = "sfp"
                                            self._children_yang_names.add("sfp")

                                            self.spi_si = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.SpiSi()
                                            self.spi_si.parent = self
                                            self._children_name_map["spi_si"] = "spi-si"
                                            self._children_yang_names.add("spi-si")

                                            self.term = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Term()
                                            self.term.parent = self
                                            self._children_name_map["term"] = "term"
                                            self._children_yang_names.add("term")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("type") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data, self).__setattr__(name, value)


                                        class Sfp(Entity):
                                            """
                                            SFP stats
                                            
                                            .. attribute:: spi_si
                                            
                                            	Service index counters
                                            	**type**\:   :py:class:`SpiSi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sfp.SpiSi>`
                                            
                                            .. attribute:: term
                                            
                                            	Terminate counters
                                            	**type**\:   :py:class:`Term <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sfp.Term>`
                                            
                                            

                                            """

                                            _prefix = 'pbr-vservice-ea-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sfp, self).__init__()

                                                self.yang_name = "sfp"
                                                self.yang_parent_name = "data"

                                                self.spi_si = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sfp.SpiSi()
                                                self.spi_si.parent = self
                                                self._children_name_map["spi_si"] = "spi-si"
                                                self._children_yang_names.add("spi-si")

                                                self.term = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sfp.Term()
                                                self.term.parent = self
                                                self._children_name_map["term"] = "term"
                                                self._children_yang_names.add("term")


                                            class SpiSi(Entity):
                                                """
                                                Service index counters
                                                
                                                .. attribute:: processed_bytes
                                                
                                                	Total bytes processed
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**units**\: byte
                                                
                                                .. attribute:: processed_pkts
                                                
                                                	Number of packets processed
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                

                                                """

                                                _prefix = 'pbr-vservice-ea-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sfp.SpiSi, self).__init__()

                                                    self.yang_name = "spi-si"
                                                    self.yang_parent_name = "sfp"

                                                    self.processed_bytes = YLeaf(YType.uint64, "processed-bytes")

                                                    self.processed_pkts = YLeaf(YType.uint64, "processed-pkts")

                                                def __setattr__(self, name, value):
                                                    self._check_monkey_patching_error(name, value)
                                                    with _handle_type_error():
                                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                                "Please use list append or extend method."
                                                                                .format(value))
                                                        if isinstance(value, Enum.YLeaf):
                                                            value = value.name
                                                        if name in ("processed_bytes",
                                                                    "processed_pkts") and name in self.__dict__:
                                                            if isinstance(value, YLeaf):
                                                                self.__dict__[name].set(value.get())
                                                            elif isinstance(value, YLeafList):
                                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sfp.SpiSi, self).__setattr__(name, value)
                                                            else:
                                                                self.__dict__[name].set(value)
                                                        else:
                                                            if hasattr(value, "parent") and name != "parent":
                                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                    value.parent = self
                                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                    value.parent = self
                                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sfp.SpiSi, self).__setattr__(name, value)

                                                def has_data(self):
                                                    return (
                                                        self.processed_bytes.is_set or
                                                        self.processed_pkts.is_set)

                                                def has_operation(self):
                                                    return (
                                                        self.yfilter != YFilter.not_set or
                                                        self.processed_bytes.yfilter != YFilter.not_set or
                                                        self.processed_pkts.yfilter != YFilter.not_set)

                                                def get_segment_path(self):
                                                    path_buffer = ""
                                                    path_buffer = "spi-si" + path_buffer

                                                    return path_buffer

                                                def get_entity_path(self, ancestor):
                                                    path_buffer = ""
                                                    if (ancestor is None):
                                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                    else:
                                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                    leaf_name_data = LeafDataList()
                                                    if (self.processed_bytes.is_set or self.processed_bytes.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.processed_bytes.get_name_leafdata())
                                                    if (self.processed_pkts.is_set or self.processed_pkts.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.processed_pkts.get_name_leafdata())

                                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                                    return entity_path

                                                def get_child_by_name(self, child_yang_name, segment_path):
                                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                    if child is not None:
                                                        return child

                                                    return None

                                                def has_leaf_or_child_of_name(self, name):
                                                    if(name == "processed-bytes" or name == "processed-pkts"):
                                                        return True
                                                    return False

                                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                                    if(value_path == "processed-bytes"):
                                                        self.processed_bytes = value
                                                        self.processed_bytes.value_namespace = name_space
                                                        self.processed_bytes.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "processed-pkts"):
                                                        self.processed_pkts = value
                                                        self.processed_pkts.value_namespace = name_space
                                                        self.processed_pkts.value_namespace_prefix = name_space_prefix


                                            class Term(Entity):
                                                """
                                                Terminate counters
                                                
                                                .. attribute:: terminated_bytes
                                                
                                                	Total bytes terminated
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**units**\: byte
                                                
                                                .. attribute:: terminated_pkts
                                                
                                                	Number of terminated packets
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                

                                                """

                                                _prefix = 'pbr-vservice-ea-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sfp.Term, self).__init__()

                                                    self.yang_name = "term"
                                                    self.yang_parent_name = "sfp"

                                                    self.terminated_bytes = YLeaf(YType.uint64, "terminated-bytes")

                                                    self.terminated_pkts = YLeaf(YType.uint64, "terminated-pkts")

                                                def __setattr__(self, name, value):
                                                    self._check_monkey_patching_error(name, value)
                                                    with _handle_type_error():
                                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                                "Please use list append or extend method."
                                                                                .format(value))
                                                        if isinstance(value, Enum.YLeaf):
                                                            value = value.name
                                                        if name in ("terminated_bytes",
                                                                    "terminated_pkts") and name in self.__dict__:
                                                            if isinstance(value, YLeaf):
                                                                self.__dict__[name].set(value.get())
                                                            elif isinstance(value, YLeafList):
                                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sfp.Term, self).__setattr__(name, value)
                                                            else:
                                                                self.__dict__[name].set(value)
                                                        else:
                                                            if hasattr(value, "parent") and name != "parent":
                                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                    value.parent = self
                                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                    value.parent = self
                                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sfp.Term, self).__setattr__(name, value)

                                                def has_data(self):
                                                    return (
                                                        self.terminated_bytes.is_set or
                                                        self.terminated_pkts.is_set)

                                                def has_operation(self):
                                                    return (
                                                        self.yfilter != YFilter.not_set or
                                                        self.terminated_bytes.yfilter != YFilter.not_set or
                                                        self.terminated_pkts.yfilter != YFilter.not_set)

                                                def get_segment_path(self):
                                                    path_buffer = ""
                                                    path_buffer = "term" + path_buffer

                                                    return path_buffer

                                                def get_entity_path(self, ancestor):
                                                    path_buffer = ""
                                                    if (ancestor is None):
                                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                    else:
                                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                    leaf_name_data = LeafDataList()
                                                    if (self.terminated_bytes.is_set or self.terminated_bytes.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.terminated_bytes.get_name_leafdata())
                                                    if (self.terminated_pkts.is_set or self.terminated_pkts.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.terminated_pkts.get_name_leafdata())

                                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                                    return entity_path

                                                def get_child_by_name(self, child_yang_name, segment_path):
                                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                    if child is not None:
                                                        return child

                                                    return None

                                                def has_leaf_or_child_of_name(self, name):
                                                    if(name == "terminated-bytes" or name == "terminated-pkts"):
                                                        return True
                                                    return False

                                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                                    if(value_path == "terminated-bytes"):
                                                        self.terminated_bytes = value
                                                        self.terminated_bytes.value_namespace = name_space
                                                        self.terminated_bytes.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "terminated-pkts"):
                                                        self.terminated_pkts = value
                                                        self.terminated_pkts.value_namespace = name_space
                                                        self.terminated_pkts.value_namespace_prefix = name_space_prefix

                                            def has_data(self):
                                                return (
                                                    (self.spi_si is not None and self.spi_si.has_data()) or
                                                    (self.term is not None and self.term.has_data()))

                                            def has_operation(self):
                                                return (
                                                    self.yfilter != YFilter.not_set or
                                                    (self.spi_si is not None and self.spi_si.has_operation()) or
                                                    (self.term is not None and self.term.has_operation()))

                                            def get_segment_path(self):
                                                path_buffer = ""
                                                path_buffer = "sfp" + path_buffer

                                                return path_buffer

                                            def get_entity_path(self, ancestor):
                                                path_buffer = ""
                                                if (ancestor is None):
                                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                else:
                                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                leaf_name_data = LeafDataList()

                                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                                return entity_path

                                            def get_child_by_name(self, child_yang_name, segment_path):
                                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                if child is not None:
                                                    return child

                                                if (child_yang_name == "spi-si"):
                                                    if (self.spi_si is None):
                                                        self.spi_si = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sfp.SpiSi()
                                                        self.spi_si.parent = self
                                                        self._children_name_map["spi_si"] = "spi-si"
                                                    return self.spi_si

                                                if (child_yang_name == "term"):
                                                    if (self.term is None):
                                                        self.term = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sfp.Term()
                                                        self.term.parent = self
                                                        self._children_name_map["term"] = "term"
                                                    return self.term

                                                return None

                                            def has_leaf_or_child_of_name(self, name):
                                                if(name == "spi-si" or name == "term"):
                                                    return True
                                                return False

                                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                                pass


                                        class SpiSi(Entity):
                                            """
                                            SPI SI stats
                                            
                                            .. attribute:: processed_bytes
                                            
                                            	Total bytes processed
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            	**units**\: byte
                                            
                                            .. attribute:: processed_pkts
                                            
                                            	Number of packets processed
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            

                                            """

                                            _prefix = 'pbr-vservice-ea-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.SpiSi, self).__init__()

                                                self.yang_name = "spi-si"
                                                self.yang_parent_name = "data"

                                                self.processed_bytes = YLeaf(YType.uint64, "processed-bytes")

                                                self.processed_pkts = YLeaf(YType.uint64, "processed-pkts")

                                            def __setattr__(self, name, value):
                                                self._check_monkey_patching_error(name, value)
                                                with _handle_type_error():
                                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                            "Please use list append or extend method."
                                                                            .format(value))
                                                    if isinstance(value, Enum.YLeaf):
                                                        value = value.name
                                                    if name in ("processed_bytes",
                                                                "processed_pkts") and name in self.__dict__:
                                                        if isinstance(value, YLeaf):
                                                            self.__dict__[name].set(value.get())
                                                        elif isinstance(value, YLeafList):
                                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.SpiSi, self).__setattr__(name, value)
                                                        else:
                                                            self.__dict__[name].set(value)
                                                    else:
                                                        if hasattr(value, "parent") and name != "parent":
                                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                value.parent = self
                                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                value.parent = self
                                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.SpiSi, self).__setattr__(name, value)

                                            def has_data(self):
                                                return (
                                                    self.processed_bytes.is_set or
                                                    self.processed_pkts.is_set)

                                            def has_operation(self):
                                                return (
                                                    self.yfilter != YFilter.not_set or
                                                    self.processed_bytes.yfilter != YFilter.not_set or
                                                    self.processed_pkts.yfilter != YFilter.not_set)

                                            def get_segment_path(self):
                                                path_buffer = ""
                                                path_buffer = "spi-si" + path_buffer

                                                return path_buffer

                                            def get_entity_path(self, ancestor):
                                                path_buffer = ""
                                                if (ancestor is None):
                                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                else:
                                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                leaf_name_data = LeafDataList()
                                                if (self.processed_bytes.is_set or self.processed_bytes.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.processed_bytes.get_name_leafdata())
                                                if (self.processed_pkts.is_set or self.processed_pkts.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.processed_pkts.get_name_leafdata())

                                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                                return entity_path

                                            def get_child_by_name(self, child_yang_name, segment_path):
                                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                if child is not None:
                                                    return child

                                                return None

                                            def has_leaf_or_child_of_name(self, name):
                                                if(name == "processed-bytes" or name == "processed-pkts"):
                                                    return True
                                                return False

                                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                                if(value_path == "processed-bytes"):
                                                    self.processed_bytes = value
                                                    self.processed_bytes.value_namespace = name_space
                                                    self.processed_bytes.value_namespace_prefix = name_space_prefix
                                                if(value_path == "processed-pkts"):
                                                    self.processed_pkts = value
                                                    self.processed_pkts.value_namespace = name_space
                                                    self.processed_pkts.value_namespace_prefix = name_space_prefix


                                        class Term(Entity):
                                            """
                                            Terminate stats
                                            
                                            .. attribute:: terminated_bytes
                                            
                                            	Total bytes terminated
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            	**units**\: byte
                                            
                                            .. attribute:: terminated_pkts
                                            
                                            	Number of terminated packets
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            

                                            """

                                            _prefix = 'pbr-vservice-ea-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Term, self).__init__()

                                                self.yang_name = "term"
                                                self.yang_parent_name = "data"

                                                self.terminated_bytes = YLeaf(YType.uint64, "terminated-bytes")

                                                self.terminated_pkts = YLeaf(YType.uint64, "terminated-pkts")

                                            def __setattr__(self, name, value):
                                                self._check_monkey_patching_error(name, value)
                                                with _handle_type_error():
                                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                            "Please use list append or extend method."
                                                                            .format(value))
                                                    if isinstance(value, Enum.YLeaf):
                                                        value = value.name
                                                    if name in ("terminated_bytes",
                                                                "terminated_pkts") and name in self.__dict__:
                                                        if isinstance(value, YLeaf):
                                                            self.__dict__[name].set(value.get())
                                                        elif isinstance(value, YLeafList):
                                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Term, self).__setattr__(name, value)
                                                        else:
                                                            self.__dict__[name].set(value)
                                                    else:
                                                        if hasattr(value, "parent") and name != "parent":
                                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                value.parent = self
                                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                value.parent = self
                                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Term, self).__setattr__(name, value)

                                            def has_data(self):
                                                return (
                                                    self.terminated_bytes.is_set or
                                                    self.terminated_pkts.is_set)

                                            def has_operation(self):
                                                return (
                                                    self.yfilter != YFilter.not_set or
                                                    self.terminated_bytes.yfilter != YFilter.not_set or
                                                    self.terminated_pkts.yfilter != YFilter.not_set)

                                            def get_segment_path(self):
                                                path_buffer = ""
                                                path_buffer = "term" + path_buffer

                                                return path_buffer

                                            def get_entity_path(self, ancestor):
                                                path_buffer = ""
                                                if (ancestor is None):
                                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                else:
                                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                leaf_name_data = LeafDataList()
                                                if (self.terminated_bytes.is_set or self.terminated_bytes.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.terminated_bytes.get_name_leafdata())
                                                if (self.terminated_pkts.is_set or self.terminated_pkts.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.terminated_pkts.get_name_leafdata())

                                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                                return entity_path

                                            def get_child_by_name(self, child_yang_name, segment_path):
                                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                if child is not None:
                                                    return child

                                                return None

                                            def has_leaf_or_child_of_name(self, name):
                                                if(name == "terminated-bytes" or name == "terminated-pkts"):
                                                    return True
                                                return False

                                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                                if(value_path == "terminated-bytes"):
                                                    self.terminated_bytes = value
                                                    self.terminated_bytes.value_namespace = name_space
                                                    self.terminated_bytes.value_namespace_prefix = name_space_prefix
                                                if(value_path == "terminated-pkts"):
                                                    self.terminated_pkts = value
                                                    self.terminated_pkts.value_namespace = name_space
                                                    self.terminated_pkts.value_namespace_prefix = name_space_prefix


                                        class Sf(Entity):
                                            """
                                            Service function stats
                                            
                                            .. attribute:: processed_bytes
                                            
                                            	Total bytes processed
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            	**units**\: byte
                                            
                                            .. attribute:: processed_pkts
                                            
                                            	Number of packets processed
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            

                                            """

                                            _prefix = 'pbr-vservice-ea-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sf, self).__init__()

                                                self.yang_name = "sf"
                                                self.yang_parent_name = "data"

                                                self.processed_bytes = YLeaf(YType.uint64, "processed-bytes")

                                                self.processed_pkts = YLeaf(YType.uint64, "processed-pkts")

                                            def __setattr__(self, name, value):
                                                self._check_monkey_patching_error(name, value)
                                                with _handle_type_error():
                                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                            "Please use list append or extend method."
                                                                            .format(value))
                                                    if isinstance(value, Enum.YLeaf):
                                                        value = value.name
                                                    if name in ("processed_bytes",
                                                                "processed_pkts") and name in self.__dict__:
                                                        if isinstance(value, YLeaf):
                                                            self.__dict__[name].set(value.get())
                                                        elif isinstance(value, YLeafList):
                                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sf, self).__setattr__(name, value)
                                                        else:
                                                            self.__dict__[name].set(value)
                                                    else:
                                                        if hasattr(value, "parent") and name != "parent":
                                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                value.parent = self
                                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                value.parent = self
                                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sf, self).__setattr__(name, value)

                                            def has_data(self):
                                                return (
                                                    self.processed_bytes.is_set or
                                                    self.processed_pkts.is_set)

                                            def has_operation(self):
                                                return (
                                                    self.yfilter != YFilter.not_set or
                                                    self.processed_bytes.yfilter != YFilter.not_set or
                                                    self.processed_pkts.yfilter != YFilter.not_set)

                                            def get_segment_path(self):
                                                path_buffer = ""
                                                path_buffer = "sf" + path_buffer

                                                return path_buffer

                                            def get_entity_path(self, ancestor):
                                                path_buffer = ""
                                                if (ancestor is None):
                                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                else:
                                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                leaf_name_data = LeafDataList()
                                                if (self.processed_bytes.is_set or self.processed_bytes.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.processed_bytes.get_name_leafdata())
                                                if (self.processed_pkts.is_set or self.processed_pkts.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.processed_pkts.get_name_leafdata())

                                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                                return entity_path

                                            def get_child_by_name(self, child_yang_name, segment_path):
                                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                if child is not None:
                                                    return child

                                                return None

                                            def has_leaf_or_child_of_name(self, name):
                                                if(name == "processed-bytes" or name == "processed-pkts"):
                                                    return True
                                                return False

                                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                                if(value_path == "processed-bytes"):
                                                    self.processed_bytes = value
                                                    self.processed_bytes.value_namespace = name_space
                                                    self.processed_bytes.value_namespace_prefix = name_space_prefix
                                                if(value_path == "processed-pkts"):
                                                    self.processed_pkts = value
                                                    self.processed_pkts.value_namespace = name_space
                                                    self.processed_pkts.value_namespace_prefix = name_space_prefix


                                        class Sff(Entity):
                                            """
                                            Service function forwarder stats
                                            
                                            .. attribute:: processed_bytes
                                            
                                            	Total bytes processed
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            	**units**\: byte
                                            
                                            .. attribute:: processed_pkts
                                            
                                            	Number of packets processed
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            

                                            """

                                            _prefix = 'pbr-vservice-ea-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sff, self).__init__()

                                                self.yang_name = "sff"
                                                self.yang_parent_name = "data"

                                                self.processed_bytes = YLeaf(YType.uint64, "processed-bytes")

                                                self.processed_pkts = YLeaf(YType.uint64, "processed-pkts")

                                            def __setattr__(self, name, value):
                                                self._check_monkey_patching_error(name, value)
                                                with _handle_type_error():
                                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                            "Please use list append or extend method."
                                                                            .format(value))
                                                    if isinstance(value, Enum.YLeaf):
                                                        value = value.name
                                                    if name in ("processed_bytes",
                                                                "processed_pkts") and name in self.__dict__:
                                                        if isinstance(value, YLeaf):
                                                            self.__dict__[name].set(value.get())
                                                        elif isinstance(value, YLeafList):
                                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sff, self).__setattr__(name, value)
                                                        else:
                                                            self.__dict__[name].set(value)
                                                    else:
                                                        if hasattr(value, "parent") and name != "parent":
                                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                value.parent = self
                                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                value.parent = self
                                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sff, self).__setattr__(name, value)

                                            def has_data(self):
                                                return (
                                                    self.processed_bytes.is_set or
                                                    self.processed_pkts.is_set)

                                            def has_operation(self):
                                                return (
                                                    self.yfilter != YFilter.not_set or
                                                    self.processed_bytes.yfilter != YFilter.not_set or
                                                    self.processed_pkts.yfilter != YFilter.not_set)

                                            def get_segment_path(self):
                                                path_buffer = ""
                                                path_buffer = "sff" + path_buffer

                                                return path_buffer

                                            def get_entity_path(self, ancestor):
                                                path_buffer = ""
                                                if (ancestor is None):
                                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                else:
                                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                leaf_name_data = LeafDataList()
                                                if (self.processed_bytes.is_set or self.processed_bytes.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.processed_bytes.get_name_leafdata())
                                                if (self.processed_pkts.is_set or self.processed_pkts.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.processed_pkts.get_name_leafdata())

                                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                                return entity_path

                                            def get_child_by_name(self, child_yang_name, segment_path):
                                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                if child is not None:
                                                    return child

                                                return None

                                            def has_leaf_or_child_of_name(self, name):
                                                if(name == "processed-bytes" or name == "processed-pkts"):
                                                    return True
                                                return False

                                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                                if(value_path == "processed-bytes"):
                                                    self.processed_bytes = value
                                                    self.processed_bytes.value_namespace = name_space
                                                    self.processed_bytes.value_namespace_prefix = name_space_prefix
                                                if(value_path == "processed-pkts"):
                                                    self.processed_pkts = value
                                                    self.processed_pkts.value_namespace = name_space
                                                    self.processed_pkts.value_namespace_prefix = name_space_prefix


                                        class SffLocal(Entity):
                                            """
                                            Local service function forwarder stats
                                            
                                            .. attribute:: lookup_err_bytes
                                            
                                            	Total bytes with unknown spi\-si
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            	**units**\: byte
                                            
                                            .. attribute:: lookup_err_pkts
                                            
                                            	Number of packets with unknown spi\-si
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            .. attribute:: malformed_err_bytes
                                            
                                            	Total bytes with invalid NSH header
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            	**units**\: byte
                                            
                                            .. attribute:: malformed_err_pkts
                                            
                                            	Number of packets with invalid NSH header
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            

                                            """

                                            _prefix = 'pbr-vservice-ea-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.SffLocal, self).__init__()

                                                self.yang_name = "sff-local"
                                                self.yang_parent_name = "data"

                                                self.lookup_err_bytes = YLeaf(YType.uint64, "lookup-err-bytes")

                                                self.lookup_err_pkts = YLeaf(YType.uint64, "lookup-err-pkts")

                                                self.malformed_err_bytes = YLeaf(YType.uint64, "malformed-err-bytes")

                                                self.malformed_err_pkts = YLeaf(YType.uint64, "malformed-err-pkts")

                                            def __setattr__(self, name, value):
                                                self._check_monkey_patching_error(name, value)
                                                with _handle_type_error():
                                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                            "Please use list append or extend method."
                                                                            .format(value))
                                                    if isinstance(value, Enum.YLeaf):
                                                        value = value.name
                                                    if name in ("lookup_err_bytes",
                                                                "lookup_err_pkts",
                                                                "malformed_err_bytes",
                                                                "malformed_err_pkts") and name in self.__dict__:
                                                        if isinstance(value, YLeaf):
                                                            self.__dict__[name].set(value.get())
                                                        elif isinstance(value, YLeafList):
                                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.SffLocal, self).__setattr__(name, value)
                                                        else:
                                                            self.__dict__[name].set(value)
                                                    else:
                                                        if hasattr(value, "parent") and name != "parent":
                                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                value.parent = self
                                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                value.parent = self
                                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.SffLocal, self).__setattr__(name, value)

                                            def has_data(self):
                                                return (
                                                    self.lookup_err_bytes.is_set or
                                                    self.lookup_err_pkts.is_set or
                                                    self.malformed_err_bytes.is_set or
                                                    self.malformed_err_pkts.is_set)

                                            def has_operation(self):
                                                return (
                                                    self.yfilter != YFilter.not_set or
                                                    self.lookup_err_bytes.yfilter != YFilter.not_set or
                                                    self.lookup_err_pkts.yfilter != YFilter.not_set or
                                                    self.malformed_err_bytes.yfilter != YFilter.not_set or
                                                    self.malformed_err_pkts.yfilter != YFilter.not_set)

                                            def get_segment_path(self):
                                                path_buffer = ""
                                                path_buffer = "sff-local" + path_buffer

                                                return path_buffer

                                            def get_entity_path(self, ancestor):
                                                path_buffer = ""
                                                if (ancestor is None):
                                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                else:
                                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                leaf_name_data = LeafDataList()
                                                if (self.lookup_err_bytes.is_set or self.lookup_err_bytes.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.lookup_err_bytes.get_name_leafdata())
                                                if (self.lookup_err_pkts.is_set or self.lookup_err_pkts.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.lookup_err_pkts.get_name_leafdata())
                                                if (self.malformed_err_bytes.is_set or self.malformed_err_bytes.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.malformed_err_bytes.get_name_leafdata())
                                                if (self.malformed_err_pkts.is_set or self.malformed_err_pkts.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.malformed_err_pkts.get_name_leafdata())

                                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                                return entity_path

                                            def get_child_by_name(self, child_yang_name, segment_path):
                                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                if child is not None:
                                                    return child

                                                return None

                                            def has_leaf_or_child_of_name(self, name):
                                                if(name == "lookup-err-bytes" or name == "lookup-err-pkts" or name == "malformed-err-bytes" or name == "malformed-err-pkts"):
                                                    return True
                                                return False

                                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                                if(value_path == "lookup-err-bytes"):
                                                    self.lookup_err_bytes = value
                                                    self.lookup_err_bytes.value_namespace = name_space
                                                    self.lookup_err_bytes.value_namespace_prefix = name_space_prefix
                                                if(value_path == "lookup-err-pkts"):
                                                    self.lookup_err_pkts = value
                                                    self.lookup_err_pkts.value_namespace = name_space
                                                    self.lookup_err_pkts.value_namespace_prefix = name_space_prefix
                                                if(value_path == "malformed-err-bytes"):
                                                    self.malformed_err_bytes = value
                                                    self.malformed_err_bytes.value_namespace = name_space
                                                    self.malformed_err_bytes.value_namespace_prefix = name_space_prefix
                                                if(value_path == "malformed-err-pkts"):
                                                    self.malformed_err_pkts = value
                                                    self.malformed_err_pkts.value_namespace = name_space
                                                    self.malformed_err_pkts.value_namespace_prefix = name_space_prefix

                                        def has_data(self):
                                            return (
                                                self.type.is_set or
                                                (self.sf is not None and self.sf.has_data()) or
                                                (self.sff is not None and self.sff.has_data()) or
                                                (self.sff_local is not None and self.sff_local.has_data()) or
                                                (self.sfp is not None and self.sfp.has_data()) or
                                                (self.spi_si is not None and self.spi_si.has_data()) or
                                                (self.term is not None and self.term.has_data()))

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.type.yfilter != YFilter.not_set or
                                                (self.sf is not None and self.sf.has_operation()) or
                                                (self.sff is not None and self.sff.has_operation()) or
                                                (self.sff_local is not None and self.sff_local.has_operation()) or
                                                (self.sfp is not None and self.sfp.has_operation()) or
                                                (self.spi_si is not None and self.spi_si.has_operation()) or
                                                (self.term is not None and self.term.has_operation()))

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "data" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.type.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            if (child_yang_name == "sf"):
                                                if (self.sf is None):
                                                    self.sf = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sf()
                                                    self.sf.parent = self
                                                    self._children_name_map["sf"] = "sf"
                                                return self.sf

                                            if (child_yang_name == "sff"):
                                                if (self.sff is None):
                                                    self.sff = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sff()
                                                    self.sff.parent = self
                                                    self._children_name_map["sff"] = "sff"
                                                return self.sff

                                            if (child_yang_name == "sff-local"):
                                                if (self.sff_local is None):
                                                    self.sff_local = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.SffLocal()
                                                    self.sff_local.parent = self
                                                    self._children_name_map["sff_local"] = "sff-local"
                                                return self.sff_local

                                            if (child_yang_name == "sfp"):
                                                if (self.sfp is None):
                                                    self.sfp = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sfp()
                                                    self.sfp.parent = self
                                                    self._children_name_map["sfp"] = "sfp"
                                                return self.sfp

                                            if (child_yang_name == "spi-si"):
                                                if (self.spi_si is None):
                                                    self.spi_si = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.SpiSi()
                                                    self.spi_si.parent = self
                                                    self._children_name_map["spi_si"] = "spi-si"
                                                return self.spi_si

                                            if (child_yang_name == "term"):
                                                if (self.term is None):
                                                    self.term = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Term()
                                                    self.term.parent = self
                                                    self._children_name_map["term"] = "term"
                                                return self.term

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "sf" or name == "sff" or name == "sff-local" or name == "sfp" or name == "spi-si" or name == "term" or name == "type"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "type"):
                                                self.type = value
                                                self.type.value_namespace = name_space
                                                self.type.value_namespace_prefix = name_space_prefix


                                    class SiArr(Entity):
                                        """
                                        SI array in case of detail stats
                                        
                                        .. attribute:: data
                                        
                                        	Stats counter for this index
                                        	**type**\:   :py:class:`Data <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data>`
                                        
                                        .. attribute:: si
                                        
                                        	Service index
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'pbr-vservice-ea-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr, self).__init__()

                                            self.yang_name = "si-arr"
                                            self.yang_parent_name = "summarized"

                                            self.si = YLeaf(YType.uint8, "si")

                                            self.data = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data()
                                            self.data.parent = self
                                            self._children_name_map["data"] = "data"
                                            self._children_yang_names.add("data")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("si") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr, self).__setattr__(name, value)


                                        class Data(Entity):
                                            """
                                            Stats counter for this index
                                            
                                            .. attribute:: spi_si
                                            
                                            	SF/SFF stats
                                            	**type**\:   :py:class:`SpiSi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data.SpiSi>`
                                            
                                            .. attribute:: term
                                            
                                            	Terminate stats
                                            	**type**\:   :py:class:`Term <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data.Term>`
                                            
                                            .. attribute:: type
                                            
                                            	type
                                            	**type**\:   :py:class:`VsNshStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.VsNshStats>`
                                            
                                            

                                            """

                                            _prefix = 'pbr-vservice-ea-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data, self).__init__()

                                                self.yang_name = "data"
                                                self.yang_parent_name = "si-arr"

                                                self.type = YLeaf(YType.enumeration, "type")

                                                self.spi_si = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data.SpiSi()
                                                self.spi_si.parent = self
                                                self._children_name_map["spi_si"] = "spi-si"
                                                self._children_yang_names.add("spi-si")

                                                self.term = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data.Term()
                                                self.term.parent = self
                                                self._children_name_map["term"] = "term"
                                                self._children_yang_names.add("term")

                                            def __setattr__(self, name, value):
                                                self._check_monkey_patching_error(name, value)
                                                with _handle_type_error():
                                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                            "Please use list append or extend method."
                                                                            .format(value))
                                                    if isinstance(value, Enum.YLeaf):
                                                        value = value.name
                                                    if name in ("type") and name in self.__dict__:
                                                        if isinstance(value, YLeaf):
                                                            self.__dict__[name].set(value.get())
                                                        elif isinstance(value, YLeafList):
                                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data, self).__setattr__(name, value)
                                                        else:
                                                            self.__dict__[name].set(value)
                                                    else:
                                                        if hasattr(value, "parent") and name != "parent":
                                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                value.parent = self
                                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                value.parent = self
                                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data, self).__setattr__(name, value)


                                            class SpiSi(Entity):
                                                """
                                                SF/SFF stats
                                                
                                                .. attribute:: processed_bytes
                                                
                                                	Total bytes processed
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**units**\: byte
                                                
                                                .. attribute:: processed_pkts
                                                
                                                	Number of packets processed
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                

                                                """

                                                _prefix = 'pbr-vservice-ea-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data.SpiSi, self).__init__()

                                                    self.yang_name = "spi-si"
                                                    self.yang_parent_name = "data"

                                                    self.processed_bytes = YLeaf(YType.uint64, "processed-bytes")

                                                    self.processed_pkts = YLeaf(YType.uint64, "processed-pkts")

                                                def __setattr__(self, name, value):
                                                    self._check_monkey_patching_error(name, value)
                                                    with _handle_type_error():
                                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                                "Please use list append or extend method."
                                                                                .format(value))
                                                        if isinstance(value, Enum.YLeaf):
                                                            value = value.name
                                                        if name in ("processed_bytes",
                                                                    "processed_pkts") and name in self.__dict__:
                                                            if isinstance(value, YLeaf):
                                                                self.__dict__[name].set(value.get())
                                                            elif isinstance(value, YLeafList):
                                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data.SpiSi, self).__setattr__(name, value)
                                                            else:
                                                                self.__dict__[name].set(value)
                                                        else:
                                                            if hasattr(value, "parent") and name != "parent":
                                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                    value.parent = self
                                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                    value.parent = self
                                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data.SpiSi, self).__setattr__(name, value)

                                                def has_data(self):
                                                    return (
                                                        self.processed_bytes.is_set or
                                                        self.processed_pkts.is_set)

                                                def has_operation(self):
                                                    return (
                                                        self.yfilter != YFilter.not_set or
                                                        self.processed_bytes.yfilter != YFilter.not_set or
                                                        self.processed_pkts.yfilter != YFilter.not_set)

                                                def get_segment_path(self):
                                                    path_buffer = ""
                                                    path_buffer = "spi-si" + path_buffer

                                                    return path_buffer

                                                def get_entity_path(self, ancestor):
                                                    path_buffer = ""
                                                    if (ancestor is None):
                                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                    else:
                                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                    leaf_name_data = LeafDataList()
                                                    if (self.processed_bytes.is_set or self.processed_bytes.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.processed_bytes.get_name_leafdata())
                                                    if (self.processed_pkts.is_set or self.processed_pkts.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.processed_pkts.get_name_leafdata())

                                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                                    return entity_path

                                                def get_child_by_name(self, child_yang_name, segment_path):
                                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                    if child is not None:
                                                        return child

                                                    return None

                                                def has_leaf_or_child_of_name(self, name):
                                                    if(name == "processed-bytes" or name == "processed-pkts"):
                                                        return True
                                                    return False

                                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                                    if(value_path == "processed-bytes"):
                                                        self.processed_bytes = value
                                                        self.processed_bytes.value_namespace = name_space
                                                        self.processed_bytes.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "processed-pkts"):
                                                        self.processed_pkts = value
                                                        self.processed_pkts.value_namespace = name_space
                                                        self.processed_pkts.value_namespace_prefix = name_space_prefix


                                            class Term(Entity):
                                                """
                                                Terminate stats
                                                
                                                .. attribute:: terminated_bytes
                                                
                                                	Total bytes terminated
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**units**\: byte
                                                
                                                .. attribute:: terminated_pkts
                                                
                                                	Number of terminated packets
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                

                                                """

                                                _prefix = 'pbr-vservice-ea-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data.Term, self).__init__()

                                                    self.yang_name = "term"
                                                    self.yang_parent_name = "data"

                                                    self.terminated_bytes = YLeaf(YType.uint64, "terminated-bytes")

                                                    self.terminated_pkts = YLeaf(YType.uint64, "terminated-pkts")

                                                def __setattr__(self, name, value):
                                                    self._check_monkey_patching_error(name, value)
                                                    with _handle_type_error():
                                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                                "Please use list append or extend method."
                                                                                .format(value))
                                                        if isinstance(value, Enum.YLeaf):
                                                            value = value.name
                                                        if name in ("terminated_bytes",
                                                                    "terminated_pkts") and name in self.__dict__:
                                                            if isinstance(value, YLeaf):
                                                                self.__dict__[name].set(value.get())
                                                            elif isinstance(value, YLeafList):
                                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data.Term, self).__setattr__(name, value)
                                                            else:
                                                                self.__dict__[name].set(value)
                                                        else:
                                                            if hasattr(value, "parent") and name != "parent":
                                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                    value.parent = self
                                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                    value.parent = self
                                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data.Term, self).__setattr__(name, value)

                                                def has_data(self):
                                                    return (
                                                        self.terminated_bytes.is_set or
                                                        self.terminated_pkts.is_set)

                                                def has_operation(self):
                                                    return (
                                                        self.yfilter != YFilter.not_set or
                                                        self.terminated_bytes.yfilter != YFilter.not_set or
                                                        self.terminated_pkts.yfilter != YFilter.not_set)

                                                def get_segment_path(self):
                                                    path_buffer = ""
                                                    path_buffer = "term" + path_buffer

                                                    return path_buffer

                                                def get_entity_path(self, ancestor):
                                                    path_buffer = ""
                                                    if (ancestor is None):
                                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                    else:
                                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                    leaf_name_data = LeafDataList()
                                                    if (self.terminated_bytes.is_set or self.terminated_bytes.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.terminated_bytes.get_name_leafdata())
                                                    if (self.terminated_pkts.is_set or self.terminated_pkts.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.terminated_pkts.get_name_leafdata())

                                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                                    return entity_path

                                                def get_child_by_name(self, child_yang_name, segment_path):
                                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                    if child is not None:
                                                        return child

                                                    return None

                                                def has_leaf_or_child_of_name(self, name):
                                                    if(name == "terminated-bytes" or name == "terminated-pkts"):
                                                        return True
                                                    return False

                                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                                    if(value_path == "terminated-bytes"):
                                                        self.terminated_bytes = value
                                                        self.terminated_bytes.value_namespace = name_space
                                                        self.terminated_bytes.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "terminated-pkts"):
                                                        self.terminated_pkts = value
                                                        self.terminated_pkts.value_namespace = name_space
                                                        self.terminated_pkts.value_namespace_prefix = name_space_prefix

                                            def has_data(self):
                                                return (
                                                    self.type.is_set or
                                                    (self.spi_si is not None and self.spi_si.has_data()) or
                                                    (self.term is not None and self.term.has_data()))

                                            def has_operation(self):
                                                return (
                                                    self.yfilter != YFilter.not_set or
                                                    self.type.yfilter != YFilter.not_set or
                                                    (self.spi_si is not None and self.spi_si.has_operation()) or
                                                    (self.term is not None and self.term.has_operation()))

                                            def get_segment_path(self):
                                                path_buffer = ""
                                                path_buffer = "data" + path_buffer

                                                return path_buffer

                                            def get_entity_path(self, ancestor):
                                                path_buffer = ""
                                                if (ancestor is None):
                                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                else:
                                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                leaf_name_data = LeafDataList()
                                                if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.type.get_name_leafdata())

                                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                                return entity_path

                                            def get_child_by_name(self, child_yang_name, segment_path):
                                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                if child is not None:
                                                    return child

                                                if (child_yang_name == "spi-si"):
                                                    if (self.spi_si is None):
                                                        self.spi_si = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data.SpiSi()
                                                        self.spi_si.parent = self
                                                        self._children_name_map["spi_si"] = "spi-si"
                                                    return self.spi_si

                                                if (child_yang_name == "term"):
                                                    if (self.term is None):
                                                        self.term = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data.Term()
                                                        self.term.parent = self
                                                        self._children_name_map["term"] = "term"
                                                    return self.term

                                                return None

                                            def has_leaf_or_child_of_name(self, name):
                                                if(name == "spi-si" or name == "term" or name == "type"):
                                                    return True
                                                return False

                                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                                if(value_path == "type"):
                                                    self.type = value
                                                    self.type.value_namespace = name_space
                                                    self.type.value_namespace_prefix = name_space_prefix

                                        def has_data(self):
                                            return (
                                                self.si.is_set or
                                                (self.data is not None and self.data.has_data()))

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.si.yfilter != YFilter.not_set or
                                                (self.data is not None and self.data.has_operation()))

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "si-arr" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.si.is_set or self.si.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.si.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            if (child_yang_name == "data"):
                                                if (self.data is None):
                                                    self.data = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data()
                                                    self.data.parent = self
                                                    self._children_name_map["data"] = "data"
                                                return self.data

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "data" or name == "si"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "si"):
                                                self.si = value
                                                self.si.value_namespace = name_space
                                                self.si.value_namespace_prefix = name_space_prefix

                                    def has_data(self):
                                        for c in self.si_arr:
                                            if (c.has_data()):
                                                return True
                                        return (self.data is not None and self.data.has_data())

                                    def has_operation(self):
                                        for c in self.si_arr:
                                            if (c.has_operation()):
                                                return True
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            (self.data is not None and self.data.has_operation()))

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "summarized" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        if (child_yang_name == "data"):
                                            if (self.data is None):
                                                self.data = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data()
                                                self.data.parent = self
                                                self._children_name_map["data"] = "data"
                                            return self.data

                                        if (child_yang_name == "si-arr"):
                                            for c in self.si_arr:
                                                segment = c.get_segment_path()
                                                if (segment_path == segment):
                                                    return c
                                            c = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr()
                                            c.parent = self
                                            local_reference_key = "ydk::seg::%s" % segment_path
                                            self._local_refs[local_reference_key] = c
                                            self.si_arr.append(c)
                                            return c

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "data" or name == "si-arr"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        pass

                                def has_data(self):
                                    return (
                                        (self.detail is not None and self.detail.has_data()) or
                                        (self.summarized is not None and self.summarized.has_data()))

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        (self.detail is not None and self.detail.has_operation()) or
                                        (self.summarized is not None and self.summarized.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "stats" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "detail"):
                                        if (self.detail is None):
                                            self.detail = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail()
                                            self.detail.parent = self
                                            self._children_name_map["detail"] = "detail"
                                        return self.detail

                                    if (child_yang_name == "summarized"):
                                        if (self.summarized is None):
                                            self.summarized = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized()
                                            self.summarized.parent = self
                                            self._children_name_map["summarized"] = "summarized"
                                        return self.summarized

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "detail" or name == "summarized"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    pass

                            def has_data(self):
                                return (
                                    self.id.is_set or
                                    (self.service_indexes is not None and self.service_indexes.has_data()) or
                                    (self.stats is not None and self.stats.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.id.yfilter != YFilter.not_set or
                                    (self.service_indexes is not None and self.service_indexes.has_operation()) or
                                    (self.stats is not None and self.stats.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "path-id" + "[id='" + self.id.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.id.is_set or self.id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.id.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "service-indexes"):
                                    if (self.service_indexes is None):
                                        self.service_indexes = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes()
                                        self.service_indexes.parent = self
                                        self._children_name_map["service_indexes"] = "service-indexes"
                                    return self.service_indexes

                                if (child_yang_name == "stats"):
                                    if (self.stats is None):
                                        self.stats = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats()
                                        self.stats.parent = self
                                        self._children_name_map["stats"] = "stats"
                                    return self.stats

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "service-indexes" or name == "stats" or name == "id"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "id"):
                                    self.id = value
                                    self.id.value_namespace = name_space
                                    self.id.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.path_id:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.path_id:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "path-ids" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "path-id"):
                                for c in self.path_id:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.path_id.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "path-id"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (self.path_ids is not None and self.path_ids.has_data())

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.path_ids is not None and self.path_ids.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "service-function-path" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "path-ids"):
                            if (self.path_ids is None):
                                self.path_ids = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds()
                                self.path_ids.parent = self
                                self._children_name_map["path_ids"] = "path-ids"
                            return self.path_ids

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "path-ids"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class ServiceFunction(Entity):
                    """
                    Service Function operational data
                    
                    .. attribute:: sf_names
                    
                    	List of Service Function Names
                    	**type**\:   :py:class:`SfNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames>`
                    
                    

                    """

                    _prefix = 'pbr-vservice-ea-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction, self).__init__()

                        self.yang_name = "service-function"
                        self.yang_parent_name = "process"

                        self.sf_names = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames()
                        self.sf_names.parent = self
                        self._children_name_map["sf_names"] = "sf-names"
                        self._children_yang_names.add("sf-names")


                    class SfNames(Entity):
                        """
                        List of Service Function Names
                        
                        .. attribute:: sf_name
                        
                        	Name of Service Function
                        	**type**\: list of    :py:class:`SfName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName>`
                        
                        

                        """

                        _prefix = 'pbr-vservice-ea-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames, self).__init__()

                            self.yang_name = "sf-names"
                            self.yang_parent_name = "service-function"

                            self.sf_name = YList(self)

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in () and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames, self).__setattr__(name, value)


                        class SfName(Entity):
                            """
                            Name of Service Function
                            
                            .. attribute:: name  <key>
                            
                            	Name
                            	**type**\:  str
                            
                            	**length:** 1..32
                            
                            .. attribute:: data
                            
                            	Statistics data
                            	**type**\:   :py:class:`Data <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data>`
                            
                            .. attribute:: si_arr
                            
                            	SI array in case of detail stats
                            	**type**\: list of    :py:class:`SiArr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.SiArr>`
                            
                            

                            """

                            _prefix = 'pbr-vservice-ea-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName, self).__init__()

                                self.yang_name = "sf-name"
                                self.yang_parent_name = "sf-names"

                                self.name = YLeaf(YType.str, "name")

                                self.data = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data()
                                self.data.parent = self
                                self._children_name_map["data"] = "data"
                                self._children_yang_names.add("data")

                                self.si_arr = YList(self)

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("name") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName, self).__setattr__(name, value)


                            class Data(Entity):
                                """
                                Statistics data
                                
                                .. attribute:: sf
                                
                                	Service function stats
                                	**type**\:   :py:class:`Sf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Sf>`
                                
                                .. attribute:: sff
                                
                                	Service function forwarder stats
                                	**type**\:   :py:class:`Sff <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Sff>`
                                
                                .. attribute:: sff_local
                                
                                	Local service function forwarder stats
                                	**type**\:   :py:class:`SffLocal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.SffLocal>`
                                
                                .. attribute:: sfp
                                
                                	SFP stats
                                	**type**\:   :py:class:`Sfp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Sfp>`
                                
                                .. attribute:: spi_si
                                
                                	SPI SI stats
                                	**type**\:   :py:class:`SpiSi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.SpiSi>`
                                
                                .. attribute:: term
                                
                                	Terminate stats
                                	**type**\:   :py:class:`Term <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Term>`
                                
                                .. attribute:: type
                                
                                	type
                                	**type**\:   :py:class:`VsNshStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.VsNshStats>`
                                
                                

                                """

                                _prefix = 'pbr-vservice-ea-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data, self).__init__()

                                    self.yang_name = "data"
                                    self.yang_parent_name = "sf-name"

                                    self.type = YLeaf(YType.enumeration, "type")

                                    self.sf = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Sf()
                                    self.sf.parent = self
                                    self._children_name_map["sf"] = "sf"
                                    self._children_yang_names.add("sf")

                                    self.sff = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Sff()
                                    self.sff.parent = self
                                    self._children_name_map["sff"] = "sff"
                                    self._children_yang_names.add("sff")

                                    self.sff_local = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.SffLocal()
                                    self.sff_local.parent = self
                                    self._children_name_map["sff_local"] = "sff-local"
                                    self._children_yang_names.add("sff-local")

                                    self.sfp = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Sfp()
                                    self.sfp.parent = self
                                    self._children_name_map["sfp"] = "sfp"
                                    self._children_yang_names.add("sfp")

                                    self.spi_si = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.SpiSi()
                                    self.spi_si.parent = self
                                    self._children_name_map["spi_si"] = "spi-si"
                                    self._children_yang_names.add("spi-si")

                                    self.term = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Term()
                                    self.term.parent = self
                                    self._children_name_map["term"] = "term"
                                    self._children_yang_names.add("term")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("type") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data, self).__setattr__(name, value)


                                class Sfp(Entity):
                                    """
                                    SFP stats
                                    
                                    .. attribute:: spi_si
                                    
                                    	Service index counters
                                    	**type**\:   :py:class:`SpiSi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Sfp.SpiSi>`
                                    
                                    .. attribute:: term
                                    
                                    	Terminate counters
                                    	**type**\:   :py:class:`Term <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Sfp.Term>`
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-ea-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Sfp, self).__init__()

                                        self.yang_name = "sfp"
                                        self.yang_parent_name = "data"

                                        self.spi_si = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Sfp.SpiSi()
                                        self.spi_si.parent = self
                                        self._children_name_map["spi_si"] = "spi-si"
                                        self._children_yang_names.add("spi-si")

                                        self.term = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Sfp.Term()
                                        self.term.parent = self
                                        self._children_name_map["term"] = "term"
                                        self._children_yang_names.add("term")


                                    class SpiSi(Entity):
                                        """
                                        Service index counters
                                        
                                        .. attribute:: processed_bytes
                                        
                                        	Total bytes processed
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: processed_pkts
                                        
                                        	Number of packets processed
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        

                                        """

                                        _prefix = 'pbr-vservice-ea-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Sfp.SpiSi, self).__init__()

                                            self.yang_name = "spi-si"
                                            self.yang_parent_name = "sfp"

                                            self.processed_bytes = YLeaf(YType.uint64, "processed-bytes")

                                            self.processed_pkts = YLeaf(YType.uint64, "processed-pkts")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("processed_bytes",
                                                            "processed_pkts") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Sfp.SpiSi, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Sfp.SpiSi, self).__setattr__(name, value)

                                        def has_data(self):
                                            return (
                                                self.processed_bytes.is_set or
                                                self.processed_pkts.is_set)

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.processed_bytes.yfilter != YFilter.not_set or
                                                self.processed_pkts.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "spi-si" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.processed_bytes.is_set or self.processed_bytes.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.processed_bytes.get_name_leafdata())
                                            if (self.processed_pkts.is_set or self.processed_pkts.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.processed_pkts.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "processed-bytes" or name == "processed-pkts"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "processed-bytes"):
                                                self.processed_bytes = value
                                                self.processed_bytes.value_namespace = name_space
                                                self.processed_bytes.value_namespace_prefix = name_space_prefix
                                            if(value_path == "processed-pkts"):
                                                self.processed_pkts = value
                                                self.processed_pkts.value_namespace = name_space
                                                self.processed_pkts.value_namespace_prefix = name_space_prefix


                                    class Term(Entity):
                                        """
                                        Terminate counters
                                        
                                        .. attribute:: terminated_bytes
                                        
                                        	Total bytes terminated
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: terminated_pkts
                                        
                                        	Number of terminated packets
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        

                                        """

                                        _prefix = 'pbr-vservice-ea-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Sfp.Term, self).__init__()

                                            self.yang_name = "term"
                                            self.yang_parent_name = "sfp"

                                            self.terminated_bytes = YLeaf(YType.uint64, "terminated-bytes")

                                            self.terminated_pkts = YLeaf(YType.uint64, "terminated-pkts")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("terminated_bytes",
                                                            "terminated_pkts") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Sfp.Term, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Sfp.Term, self).__setattr__(name, value)

                                        def has_data(self):
                                            return (
                                                self.terminated_bytes.is_set or
                                                self.terminated_pkts.is_set)

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.terminated_bytes.yfilter != YFilter.not_set or
                                                self.terminated_pkts.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "term" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.terminated_bytes.is_set or self.terminated_bytes.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.terminated_bytes.get_name_leafdata())
                                            if (self.terminated_pkts.is_set or self.terminated_pkts.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.terminated_pkts.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "terminated-bytes" or name == "terminated-pkts"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "terminated-bytes"):
                                                self.terminated_bytes = value
                                                self.terminated_bytes.value_namespace = name_space
                                                self.terminated_bytes.value_namespace_prefix = name_space_prefix
                                            if(value_path == "terminated-pkts"):
                                                self.terminated_pkts = value
                                                self.terminated_pkts.value_namespace = name_space
                                                self.terminated_pkts.value_namespace_prefix = name_space_prefix

                                    def has_data(self):
                                        return (
                                            (self.spi_si is not None and self.spi_si.has_data()) or
                                            (self.term is not None and self.term.has_data()))

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            (self.spi_si is not None and self.spi_si.has_operation()) or
                                            (self.term is not None and self.term.has_operation()))

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "sfp" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        if (child_yang_name == "spi-si"):
                                            if (self.spi_si is None):
                                                self.spi_si = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Sfp.SpiSi()
                                                self.spi_si.parent = self
                                                self._children_name_map["spi_si"] = "spi-si"
                                            return self.spi_si

                                        if (child_yang_name == "term"):
                                            if (self.term is None):
                                                self.term = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Sfp.Term()
                                                self.term.parent = self
                                                self._children_name_map["term"] = "term"
                                            return self.term

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "spi-si" or name == "term"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        pass


                                class SpiSi(Entity):
                                    """
                                    SPI SI stats
                                    
                                    .. attribute:: processed_bytes
                                    
                                    	Total bytes processed
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: processed_pkts
                                    
                                    	Number of packets processed
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-ea-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.SpiSi, self).__init__()

                                        self.yang_name = "spi-si"
                                        self.yang_parent_name = "data"

                                        self.processed_bytes = YLeaf(YType.uint64, "processed-bytes")

                                        self.processed_pkts = YLeaf(YType.uint64, "processed-pkts")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("processed_bytes",
                                                        "processed_pkts") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.SpiSi, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.SpiSi, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.processed_bytes.is_set or
                                            self.processed_pkts.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.processed_bytes.yfilter != YFilter.not_set or
                                            self.processed_pkts.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "spi-si" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.processed_bytes.is_set or self.processed_bytes.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.processed_bytes.get_name_leafdata())
                                        if (self.processed_pkts.is_set or self.processed_pkts.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.processed_pkts.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "processed-bytes" or name == "processed-pkts"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "processed-bytes"):
                                            self.processed_bytes = value
                                            self.processed_bytes.value_namespace = name_space
                                            self.processed_bytes.value_namespace_prefix = name_space_prefix
                                        if(value_path == "processed-pkts"):
                                            self.processed_pkts = value
                                            self.processed_pkts.value_namespace = name_space
                                            self.processed_pkts.value_namespace_prefix = name_space_prefix


                                class Term(Entity):
                                    """
                                    Terminate stats
                                    
                                    .. attribute:: terminated_bytes
                                    
                                    	Total bytes terminated
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: terminated_pkts
                                    
                                    	Number of terminated packets
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-ea-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Term, self).__init__()

                                        self.yang_name = "term"
                                        self.yang_parent_name = "data"

                                        self.terminated_bytes = YLeaf(YType.uint64, "terminated-bytes")

                                        self.terminated_pkts = YLeaf(YType.uint64, "terminated-pkts")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("terminated_bytes",
                                                        "terminated_pkts") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Term, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Term, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.terminated_bytes.is_set or
                                            self.terminated_pkts.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.terminated_bytes.yfilter != YFilter.not_set or
                                            self.terminated_pkts.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "term" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.terminated_bytes.is_set or self.terminated_bytes.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.terminated_bytes.get_name_leafdata())
                                        if (self.terminated_pkts.is_set or self.terminated_pkts.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.terminated_pkts.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "terminated-bytes" or name == "terminated-pkts"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "terminated-bytes"):
                                            self.terminated_bytes = value
                                            self.terminated_bytes.value_namespace = name_space
                                            self.terminated_bytes.value_namespace_prefix = name_space_prefix
                                        if(value_path == "terminated-pkts"):
                                            self.terminated_pkts = value
                                            self.terminated_pkts.value_namespace = name_space
                                            self.terminated_pkts.value_namespace_prefix = name_space_prefix


                                class Sf(Entity):
                                    """
                                    Service function stats
                                    
                                    .. attribute:: processed_bytes
                                    
                                    	Total bytes processed
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: processed_pkts
                                    
                                    	Number of packets processed
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-ea-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Sf, self).__init__()

                                        self.yang_name = "sf"
                                        self.yang_parent_name = "data"

                                        self.processed_bytes = YLeaf(YType.uint64, "processed-bytes")

                                        self.processed_pkts = YLeaf(YType.uint64, "processed-pkts")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("processed_bytes",
                                                        "processed_pkts") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Sf, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Sf, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.processed_bytes.is_set or
                                            self.processed_pkts.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.processed_bytes.yfilter != YFilter.not_set or
                                            self.processed_pkts.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "sf" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.processed_bytes.is_set or self.processed_bytes.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.processed_bytes.get_name_leafdata())
                                        if (self.processed_pkts.is_set or self.processed_pkts.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.processed_pkts.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "processed-bytes" or name == "processed-pkts"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "processed-bytes"):
                                            self.processed_bytes = value
                                            self.processed_bytes.value_namespace = name_space
                                            self.processed_bytes.value_namespace_prefix = name_space_prefix
                                        if(value_path == "processed-pkts"):
                                            self.processed_pkts = value
                                            self.processed_pkts.value_namespace = name_space
                                            self.processed_pkts.value_namespace_prefix = name_space_prefix


                                class Sff(Entity):
                                    """
                                    Service function forwarder stats
                                    
                                    .. attribute:: processed_bytes
                                    
                                    	Total bytes processed
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: processed_pkts
                                    
                                    	Number of packets processed
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-ea-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Sff, self).__init__()

                                        self.yang_name = "sff"
                                        self.yang_parent_name = "data"

                                        self.processed_bytes = YLeaf(YType.uint64, "processed-bytes")

                                        self.processed_pkts = YLeaf(YType.uint64, "processed-pkts")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("processed_bytes",
                                                        "processed_pkts") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Sff, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Sff, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.processed_bytes.is_set or
                                            self.processed_pkts.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.processed_bytes.yfilter != YFilter.not_set or
                                            self.processed_pkts.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "sff" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.processed_bytes.is_set or self.processed_bytes.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.processed_bytes.get_name_leafdata())
                                        if (self.processed_pkts.is_set or self.processed_pkts.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.processed_pkts.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "processed-bytes" or name == "processed-pkts"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "processed-bytes"):
                                            self.processed_bytes = value
                                            self.processed_bytes.value_namespace = name_space
                                            self.processed_bytes.value_namespace_prefix = name_space_prefix
                                        if(value_path == "processed-pkts"):
                                            self.processed_pkts = value
                                            self.processed_pkts.value_namespace = name_space
                                            self.processed_pkts.value_namespace_prefix = name_space_prefix


                                class SffLocal(Entity):
                                    """
                                    Local service function forwarder stats
                                    
                                    .. attribute:: lookup_err_bytes
                                    
                                    	Total bytes with unknown spi\-si
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: lookup_err_pkts
                                    
                                    	Number of packets with unknown spi\-si
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: malformed_err_bytes
                                    
                                    	Total bytes with invalid NSH header
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: malformed_err_pkts
                                    
                                    	Number of packets with invalid NSH header
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-ea-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.SffLocal, self).__init__()

                                        self.yang_name = "sff-local"
                                        self.yang_parent_name = "data"

                                        self.lookup_err_bytes = YLeaf(YType.uint64, "lookup-err-bytes")

                                        self.lookup_err_pkts = YLeaf(YType.uint64, "lookup-err-pkts")

                                        self.malformed_err_bytes = YLeaf(YType.uint64, "malformed-err-bytes")

                                        self.malformed_err_pkts = YLeaf(YType.uint64, "malformed-err-pkts")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("lookup_err_bytes",
                                                        "lookup_err_pkts",
                                                        "malformed_err_bytes",
                                                        "malformed_err_pkts") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.SffLocal, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.SffLocal, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.lookup_err_bytes.is_set or
                                            self.lookup_err_pkts.is_set or
                                            self.malformed_err_bytes.is_set or
                                            self.malformed_err_pkts.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.lookup_err_bytes.yfilter != YFilter.not_set or
                                            self.lookup_err_pkts.yfilter != YFilter.not_set or
                                            self.malformed_err_bytes.yfilter != YFilter.not_set or
                                            self.malformed_err_pkts.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "sff-local" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.lookup_err_bytes.is_set or self.lookup_err_bytes.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.lookup_err_bytes.get_name_leafdata())
                                        if (self.lookup_err_pkts.is_set or self.lookup_err_pkts.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.lookup_err_pkts.get_name_leafdata())
                                        if (self.malformed_err_bytes.is_set or self.malformed_err_bytes.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.malformed_err_bytes.get_name_leafdata())
                                        if (self.malformed_err_pkts.is_set or self.malformed_err_pkts.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.malformed_err_pkts.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "lookup-err-bytes" or name == "lookup-err-pkts" or name == "malformed-err-bytes" or name == "malformed-err-pkts"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "lookup-err-bytes"):
                                            self.lookup_err_bytes = value
                                            self.lookup_err_bytes.value_namespace = name_space
                                            self.lookup_err_bytes.value_namespace_prefix = name_space_prefix
                                        if(value_path == "lookup-err-pkts"):
                                            self.lookup_err_pkts = value
                                            self.lookup_err_pkts.value_namespace = name_space
                                            self.lookup_err_pkts.value_namespace_prefix = name_space_prefix
                                        if(value_path == "malformed-err-bytes"):
                                            self.malformed_err_bytes = value
                                            self.malformed_err_bytes.value_namespace = name_space
                                            self.malformed_err_bytes.value_namespace_prefix = name_space_prefix
                                        if(value_path == "malformed-err-pkts"):
                                            self.malformed_err_pkts = value
                                            self.malformed_err_pkts.value_namespace = name_space
                                            self.malformed_err_pkts.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    return (
                                        self.type.is_set or
                                        (self.sf is not None and self.sf.has_data()) or
                                        (self.sff is not None and self.sff.has_data()) or
                                        (self.sff_local is not None and self.sff_local.has_data()) or
                                        (self.sfp is not None and self.sfp.has_data()) or
                                        (self.spi_si is not None and self.spi_si.has_data()) or
                                        (self.term is not None and self.term.has_data()))

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.type.yfilter != YFilter.not_set or
                                        (self.sf is not None and self.sf.has_operation()) or
                                        (self.sff is not None and self.sff.has_operation()) or
                                        (self.sff_local is not None and self.sff_local.has_operation()) or
                                        (self.sfp is not None and self.sfp.has_operation()) or
                                        (self.spi_si is not None and self.spi_si.has_operation()) or
                                        (self.term is not None and self.term.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "data" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.type.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "sf"):
                                        if (self.sf is None):
                                            self.sf = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Sf()
                                            self.sf.parent = self
                                            self._children_name_map["sf"] = "sf"
                                        return self.sf

                                    if (child_yang_name == "sff"):
                                        if (self.sff is None):
                                            self.sff = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Sff()
                                            self.sff.parent = self
                                            self._children_name_map["sff"] = "sff"
                                        return self.sff

                                    if (child_yang_name == "sff-local"):
                                        if (self.sff_local is None):
                                            self.sff_local = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.SffLocal()
                                            self.sff_local.parent = self
                                            self._children_name_map["sff_local"] = "sff-local"
                                        return self.sff_local

                                    if (child_yang_name == "sfp"):
                                        if (self.sfp is None):
                                            self.sfp = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Sfp()
                                            self.sfp.parent = self
                                            self._children_name_map["sfp"] = "sfp"
                                        return self.sfp

                                    if (child_yang_name == "spi-si"):
                                        if (self.spi_si is None):
                                            self.spi_si = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.SpiSi()
                                            self.spi_si.parent = self
                                            self._children_name_map["spi_si"] = "spi-si"
                                        return self.spi_si

                                    if (child_yang_name == "term"):
                                        if (self.term is None):
                                            self.term = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Term()
                                            self.term.parent = self
                                            self._children_name_map["term"] = "term"
                                        return self.term

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "sf" or name == "sff" or name == "sff-local" or name == "sfp" or name == "spi-si" or name == "term" or name == "type"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "type"):
                                        self.type = value
                                        self.type.value_namespace = name_space
                                        self.type.value_namespace_prefix = name_space_prefix


                            class SiArr(Entity):
                                """
                                SI array in case of detail stats
                                
                                .. attribute:: data
                                
                                	Stats counter for this index
                                	**type**\:   :py:class:`Data <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.SiArr.Data>`
                                
                                .. attribute:: si
                                
                                	Service index
                                	**type**\:  int
                                
                                	**range:** 0..255
                                
                                

                                """

                                _prefix = 'pbr-vservice-ea-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.SiArr, self).__init__()

                                    self.yang_name = "si-arr"
                                    self.yang_parent_name = "sf-name"

                                    self.si = YLeaf(YType.uint8, "si")

                                    self.data = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.SiArr.Data()
                                    self.data.parent = self
                                    self._children_name_map["data"] = "data"
                                    self._children_yang_names.add("data")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("si") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.SiArr, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.SiArr, self).__setattr__(name, value)


                                class Data(Entity):
                                    """
                                    Stats counter for this index
                                    
                                    .. attribute:: spi_si
                                    
                                    	SF/SFF stats
                                    	**type**\:   :py:class:`SpiSi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.SiArr.Data.SpiSi>`
                                    
                                    .. attribute:: term
                                    
                                    	Terminate stats
                                    	**type**\:   :py:class:`Term <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.SiArr.Data.Term>`
                                    
                                    .. attribute:: type
                                    
                                    	type
                                    	**type**\:   :py:class:`VsNshStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.VsNshStats>`
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-ea-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.SiArr.Data, self).__init__()

                                        self.yang_name = "data"
                                        self.yang_parent_name = "si-arr"

                                        self.type = YLeaf(YType.enumeration, "type")

                                        self.spi_si = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.SiArr.Data.SpiSi()
                                        self.spi_si.parent = self
                                        self._children_name_map["spi_si"] = "spi-si"
                                        self._children_yang_names.add("spi-si")

                                        self.term = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.SiArr.Data.Term()
                                        self.term.parent = self
                                        self._children_name_map["term"] = "term"
                                        self._children_yang_names.add("term")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("type") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.SiArr.Data, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.SiArr.Data, self).__setattr__(name, value)


                                    class SpiSi(Entity):
                                        """
                                        SF/SFF stats
                                        
                                        .. attribute:: processed_bytes
                                        
                                        	Total bytes processed
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: processed_pkts
                                        
                                        	Number of packets processed
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        

                                        """

                                        _prefix = 'pbr-vservice-ea-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.SiArr.Data.SpiSi, self).__init__()

                                            self.yang_name = "spi-si"
                                            self.yang_parent_name = "data"

                                            self.processed_bytes = YLeaf(YType.uint64, "processed-bytes")

                                            self.processed_pkts = YLeaf(YType.uint64, "processed-pkts")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("processed_bytes",
                                                            "processed_pkts") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.SiArr.Data.SpiSi, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.SiArr.Data.SpiSi, self).__setattr__(name, value)

                                        def has_data(self):
                                            return (
                                                self.processed_bytes.is_set or
                                                self.processed_pkts.is_set)

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.processed_bytes.yfilter != YFilter.not_set or
                                                self.processed_pkts.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "spi-si" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.processed_bytes.is_set or self.processed_bytes.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.processed_bytes.get_name_leafdata())
                                            if (self.processed_pkts.is_set or self.processed_pkts.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.processed_pkts.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "processed-bytes" or name == "processed-pkts"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "processed-bytes"):
                                                self.processed_bytes = value
                                                self.processed_bytes.value_namespace = name_space
                                                self.processed_bytes.value_namespace_prefix = name_space_prefix
                                            if(value_path == "processed-pkts"):
                                                self.processed_pkts = value
                                                self.processed_pkts.value_namespace = name_space
                                                self.processed_pkts.value_namespace_prefix = name_space_prefix


                                    class Term(Entity):
                                        """
                                        Terminate stats
                                        
                                        .. attribute:: terminated_bytes
                                        
                                        	Total bytes terminated
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: terminated_pkts
                                        
                                        	Number of terminated packets
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        

                                        """

                                        _prefix = 'pbr-vservice-ea-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.SiArr.Data.Term, self).__init__()

                                            self.yang_name = "term"
                                            self.yang_parent_name = "data"

                                            self.terminated_bytes = YLeaf(YType.uint64, "terminated-bytes")

                                            self.terminated_pkts = YLeaf(YType.uint64, "terminated-pkts")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("terminated_bytes",
                                                            "terminated_pkts") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.SiArr.Data.Term, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.SiArr.Data.Term, self).__setattr__(name, value)

                                        def has_data(self):
                                            return (
                                                self.terminated_bytes.is_set or
                                                self.terminated_pkts.is_set)

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.terminated_bytes.yfilter != YFilter.not_set or
                                                self.terminated_pkts.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "term" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.terminated_bytes.is_set or self.terminated_bytes.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.terminated_bytes.get_name_leafdata())
                                            if (self.terminated_pkts.is_set or self.terminated_pkts.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.terminated_pkts.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "terminated-bytes" or name == "terminated-pkts"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "terminated-bytes"):
                                                self.terminated_bytes = value
                                                self.terminated_bytes.value_namespace = name_space
                                                self.terminated_bytes.value_namespace_prefix = name_space_prefix
                                            if(value_path == "terminated-pkts"):
                                                self.terminated_pkts = value
                                                self.terminated_pkts.value_namespace = name_space
                                                self.terminated_pkts.value_namespace_prefix = name_space_prefix

                                    def has_data(self):
                                        return (
                                            self.type.is_set or
                                            (self.spi_si is not None and self.spi_si.has_data()) or
                                            (self.term is not None and self.term.has_data()))

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.type.yfilter != YFilter.not_set or
                                            (self.spi_si is not None and self.spi_si.has_operation()) or
                                            (self.term is not None and self.term.has_operation()))

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "data" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.type.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        if (child_yang_name == "spi-si"):
                                            if (self.spi_si is None):
                                                self.spi_si = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.SiArr.Data.SpiSi()
                                                self.spi_si.parent = self
                                                self._children_name_map["spi_si"] = "spi-si"
                                            return self.spi_si

                                        if (child_yang_name == "term"):
                                            if (self.term is None):
                                                self.term = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.SiArr.Data.Term()
                                                self.term.parent = self
                                                self._children_name_map["term"] = "term"
                                            return self.term

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "spi-si" or name == "term" or name == "type"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "type"):
                                            self.type = value
                                            self.type.value_namespace = name_space
                                            self.type.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    return (
                                        self.si.is_set or
                                        (self.data is not None and self.data.has_data()))

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.si.yfilter != YFilter.not_set or
                                        (self.data is not None and self.data.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "si-arr" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.si.is_set or self.si.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.si.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "data"):
                                        if (self.data is None):
                                            self.data = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.SiArr.Data()
                                            self.data.parent = self
                                            self._children_name_map["data"] = "data"
                                        return self.data

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "data" or name == "si"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "si"):
                                        self.si = value
                                        self.si.value_namespace = name_space
                                        self.si.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                for c in self.si_arr:
                                    if (c.has_data()):
                                        return True
                                return (
                                    self.name.is_set or
                                    (self.data is not None and self.data.has_data()))

                            def has_operation(self):
                                for c in self.si_arr:
                                    if (c.has_operation()):
                                        return True
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.name.yfilter != YFilter.not_set or
                                    (self.data is not None and self.data.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "sf-name" + "[name='" + self.name.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.name.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "data"):
                                    if (self.data is None):
                                        self.data = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data()
                                        self.data.parent = self
                                        self._children_name_map["data"] = "data"
                                    return self.data

                                if (child_yang_name == "si-arr"):
                                    for c in self.si_arr:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.SiArr()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.si_arr.append(c)
                                    return c

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "data" or name == "si-arr" or name == "name"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "name"):
                                    self.name = value
                                    self.name.value_namespace = name_space
                                    self.name.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.sf_name:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.sf_name:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "sf-names" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "sf-name"):
                                for c in self.sf_name:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.sf_name.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "sf-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (self.sf_names is not None and self.sf_names.has_data())

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.sf_names is not None and self.sf_names.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "service-function" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "sf-names"):
                            if (self.sf_names is None):
                                self.sf_names = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames()
                                self.sf_names.parent = self
                                self._children_name_map["sf_names"] = "sf-names"
                            return self.sf_names

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "sf-names"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class ServiceFunctionForwarder(Entity):
                    """
                    Service Function Forwarder operational data
                    
                    .. attribute:: local
                    
                    	Local Service Function Forwarder operational data
                    	**type**\:   :py:class:`Local <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local>`
                    
                    .. attribute:: sff_names
                    
                    	List of Service Function Forwarder Names
                    	**type**\:   :py:class:`SffNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames>`
                    
                    

                    """

                    _prefix = 'pbr-vservice-ea-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder, self).__init__()

                        self.yang_name = "service-function-forwarder"
                        self.yang_parent_name = "process"

                        self.local = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local()
                        self.local.parent = self
                        self._children_name_map["local"] = "local"
                        self._children_yang_names.add("local")

                        self.sff_names = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames()
                        self.sff_names.parent = self
                        self._children_name_map["sff_names"] = "sff-names"
                        self._children_yang_names.add("sff-names")


                    class Local(Entity):
                        """
                        Local Service Function Forwarder operational
                        data
                        
                        .. attribute:: error
                        
                        	Error Statistics for local service function forwarder
                        	**type**\:   :py:class:`Error <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error>`
                        
                        

                        """

                        _prefix = 'pbr-vservice-ea-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local, self).__init__()

                            self.yang_name = "local"
                            self.yang_parent_name = "service-function-forwarder"

                            self.error = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error()
                            self.error.parent = self
                            self._children_name_map["error"] = "error"
                            self._children_yang_names.add("error")


                        class Error(Entity):
                            """
                            Error Statistics for local service function
                            forwarder
                            
                            .. attribute:: data
                            
                            	Statistics data
                            	**type**\:   :py:class:`Data <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data>`
                            
                            .. attribute:: si_arr
                            
                            	SI array in case of detail stats
                            	**type**\: list of    :py:class:`SiArr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.SiArr>`
                            
                            

                            """

                            _prefix = 'pbr-vservice-ea-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error, self).__init__()

                                self.yang_name = "error"
                                self.yang_parent_name = "local"

                                self.data = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data()
                                self.data.parent = self
                                self._children_name_map["data"] = "data"
                                self._children_yang_names.add("data")

                                self.si_arr = YList(self)

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in () and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error, self).__setattr__(name, value)


                            class Data(Entity):
                                """
                                Statistics data
                                
                                .. attribute:: sf
                                
                                	Service function stats
                                	**type**\:   :py:class:`Sf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Sf>`
                                
                                .. attribute:: sff
                                
                                	Service function forwarder stats
                                	**type**\:   :py:class:`Sff <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Sff>`
                                
                                .. attribute:: sff_local
                                
                                	Local service function forwarder stats
                                	**type**\:   :py:class:`SffLocal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.SffLocal>`
                                
                                .. attribute:: sfp
                                
                                	SFP stats
                                	**type**\:   :py:class:`Sfp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Sfp>`
                                
                                .. attribute:: spi_si
                                
                                	SPI SI stats
                                	**type**\:   :py:class:`SpiSi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.SpiSi>`
                                
                                .. attribute:: term
                                
                                	Terminate stats
                                	**type**\:   :py:class:`Term <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Term>`
                                
                                .. attribute:: type
                                
                                	type
                                	**type**\:   :py:class:`VsNshStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.VsNshStats>`
                                
                                

                                """

                                _prefix = 'pbr-vservice-ea-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data, self).__init__()

                                    self.yang_name = "data"
                                    self.yang_parent_name = "error"

                                    self.type = YLeaf(YType.enumeration, "type")

                                    self.sf = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Sf()
                                    self.sf.parent = self
                                    self._children_name_map["sf"] = "sf"
                                    self._children_yang_names.add("sf")

                                    self.sff = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Sff()
                                    self.sff.parent = self
                                    self._children_name_map["sff"] = "sff"
                                    self._children_yang_names.add("sff")

                                    self.sff_local = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.SffLocal()
                                    self.sff_local.parent = self
                                    self._children_name_map["sff_local"] = "sff-local"
                                    self._children_yang_names.add("sff-local")

                                    self.sfp = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Sfp()
                                    self.sfp.parent = self
                                    self._children_name_map["sfp"] = "sfp"
                                    self._children_yang_names.add("sfp")

                                    self.spi_si = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.SpiSi()
                                    self.spi_si.parent = self
                                    self._children_name_map["spi_si"] = "spi-si"
                                    self._children_yang_names.add("spi-si")

                                    self.term = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Term()
                                    self.term.parent = self
                                    self._children_name_map["term"] = "term"
                                    self._children_yang_names.add("term")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("type") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data, self).__setattr__(name, value)


                                class Sfp(Entity):
                                    """
                                    SFP stats
                                    
                                    .. attribute:: spi_si
                                    
                                    	Service index counters
                                    	**type**\:   :py:class:`SpiSi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Sfp.SpiSi>`
                                    
                                    .. attribute:: term
                                    
                                    	Terminate counters
                                    	**type**\:   :py:class:`Term <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Sfp.Term>`
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-ea-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Sfp, self).__init__()

                                        self.yang_name = "sfp"
                                        self.yang_parent_name = "data"

                                        self.spi_si = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Sfp.SpiSi()
                                        self.spi_si.parent = self
                                        self._children_name_map["spi_si"] = "spi-si"
                                        self._children_yang_names.add("spi-si")

                                        self.term = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Sfp.Term()
                                        self.term.parent = self
                                        self._children_name_map["term"] = "term"
                                        self._children_yang_names.add("term")


                                    class SpiSi(Entity):
                                        """
                                        Service index counters
                                        
                                        .. attribute:: processed_bytes
                                        
                                        	Total bytes processed
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: processed_pkts
                                        
                                        	Number of packets processed
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        

                                        """

                                        _prefix = 'pbr-vservice-ea-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Sfp.SpiSi, self).__init__()

                                            self.yang_name = "spi-si"
                                            self.yang_parent_name = "sfp"

                                            self.processed_bytes = YLeaf(YType.uint64, "processed-bytes")

                                            self.processed_pkts = YLeaf(YType.uint64, "processed-pkts")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("processed_bytes",
                                                            "processed_pkts") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Sfp.SpiSi, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Sfp.SpiSi, self).__setattr__(name, value)

                                        def has_data(self):
                                            return (
                                                self.processed_bytes.is_set or
                                                self.processed_pkts.is_set)

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.processed_bytes.yfilter != YFilter.not_set or
                                                self.processed_pkts.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "spi-si" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.processed_bytes.is_set or self.processed_bytes.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.processed_bytes.get_name_leafdata())
                                            if (self.processed_pkts.is_set or self.processed_pkts.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.processed_pkts.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "processed-bytes" or name == "processed-pkts"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "processed-bytes"):
                                                self.processed_bytes = value
                                                self.processed_bytes.value_namespace = name_space
                                                self.processed_bytes.value_namespace_prefix = name_space_prefix
                                            if(value_path == "processed-pkts"):
                                                self.processed_pkts = value
                                                self.processed_pkts.value_namespace = name_space
                                                self.processed_pkts.value_namespace_prefix = name_space_prefix


                                    class Term(Entity):
                                        """
                                        Terminate counters
                                        
                                        .. attribute:: terminated_bytes
                                        
                                        	Total bytes terminated
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: terminated_pkts
                                        
                                        	Number of terminated packets
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        

                                        """

                                        _prefix = 'pbr-vservice-ea-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Sfp.Term, self).__init__()

                                            self.yang_name = "term"
                                            self.yang_parent_name = "sfp"

                                            self.terminated_bytes = YLeaf(YType.uint64, "terminated-bytes")

                                            self.terminated_pkts = YLeaf(YType.uint64, "terminated-pkts")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("terminated_bytes",
                                                            "terminated_pkts") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Sfp.Term, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Sfp.Term, self).__setattr__(name, value)

                                        def has_data(self):
                                            return (
                                                self.terminated_bytes.is_set or
                                                self.terminated_pkts.is_set)

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.terminated_bytes.yfilter != YFilter.not_set or
                                                self.terminated_pkts.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "term" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.terminated_bytes.is_set or self.terminated_bytes.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.terminated_bytes.get_name_leafdata())
                                            if (self.terminated_pkts.is_set or self.terminated_pkts.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.terminated_pkts.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "terminated-bytes" or name == "terminated-pkts"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "terminated-bytes"):
                                                self.terminated_bytes = value
                                                self.terminated_bytes.value_namespace = name_space
                                                self.terminated_bytes.value_namespace_prefix = name_space_prefix
                                            if(value_path == "terminated-pkts"):
                                                self.terminated_pkts = value
                                                self.terminated_pkts.value_namespace = name_space
                                                self.terminated_pkts.value_namespace_prefix = name_space_prefix

                                    def has_data(self):
                                        return (
                                            (self.spi_si is not None and self.spi_si.has_data()) or
                                            (self.term is not None and self.term.has_data()))

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            (self.spi_si is not None and self.spi_si.has_operation()) or
                                            (self.term is not None and self.term.has_operation()))

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "sfp" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        if (child_yang_name == "spi-si"):
                                            if (self.spi_si is None):
                                                self.spi_si = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Sfp.SpiSi()
                                                self.spi_si.parent = self
                                                self._children_name_map["spi_si"] = "spi-si"
                                            return self.spi_si

                                        if (child_yang_name == "term"):
                                            if (self.term is None):
                                                self.term = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Sfp.Term()
                                                self.term.parent = self
                                                self._children_name_map["term"] = "term"
                                            return self.term

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "spi-si" or name == "term"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        pass


                                class SpiSi(Entity):
                                    """
                                    SPI SI stats
                                    
                                    .. attribute:: processed_bytes
                                    
                                    	Total bytes processed
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: processed_pkts
                                    
                                    	Number of packets processed
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-ea-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.SpiSi, self).__init__()

                                        self.yang_name = "spi-si"
                                        self.yang_parent_name = "data"

                                        self.processed_bytes = YLeaf(YType.uint64, "processed-bytes")

                                        self.processed_pkts = YLeaf(YType.uint64, "processed-pkts")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("processed_bytes",
                                                        "processed_pkts") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.SpiSi, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.SpiSi, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.processed_bytes.is_set or
                                            self.processed_pkts.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.processed_bytes.yfilter != YFilter.not_set or
                                            self.processed_pkts.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "spi-si" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.processed_bytes.is_set or self.processed_bytes.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.processed_bytes.get_name_leafdata())
                                        if (self.processed_pkts.is_set or self.processed_pkts.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.processed_pkts.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "processed-bytes" or name == "processed-pkts"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "processed-bytes"):
                                            self.processed_bytes = value
                                            self.processed_bytes.value_namespace = name_space
                                            self.processed_bytes.value_namespace_prefix = name_space_prefix
                                        if(value_path == "processed-pkts"):
                                            self.processed_pkts = value
                                            self.processed_pkts.value_namespace = name_space
                                            self.processed_pkts.value_namespace_prefix = name_space_prefix


                                class Term(Entity):
                                    """
                                    Terminate stats
                                    
                                    .. attribute:: terminated_bytes
                                    
                                    	Total bytes terminated
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: terminated_pkts
                                    
                                    	Number of terminated packets
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-ea-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Term, self).__init__()

                                        self.yang_name = "term"
                                        self.yang_parent_name = "data"

                                        self.terminated_bytes = YLeaf(YType.uint64, "terminated-bytes")

                                        self.terminated_pkts = YLeaf(YType.uint64, "terminated-pkts")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("terminated_bytes",
                                                        "terminated_pkts") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Term, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Term, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.terminated_bytes.is_set or
                                            self.terminated_pkts.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.terminated_bytes.yfilter != YFilter.not_set or
                                            self.terminated_pkts.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "term" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.terminated_bytes.is_set or self.terminated_bytes.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.terminated_bytes.get_name_leafdata())
                                        if (self.terminated_pkts.is_set or self.terminated_pkts.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.terminated_pkts.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "terminated-bytes" or name == "terminated-pkts"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "terminated-bytes"):
                                            self.terminated_bytes = value
                                            self.terminated_bytes.value_namespace = name_space
                                            self.terminated_bytes.value_namespace_prefix = name_space_prefix
                                        if(value_path == "terminated-pkts"):
                                            self.terminated_pkts = value
                                            self.terminated_pkts.value_namespace = name_space
                                            self.terminated_pkts.value_namespace_prefix = name_space_prefix


                                class Sf(Entity):
                                    """
                                    Service function stats
                                    
                                    .. attribute:: processed_bytes
                                    
                                    	Total bytes processed
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: processed_pkts
                                    
                                    	Number of packets processed
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-ea-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Sf, self).__init__()

                                        self.yang_name = "sf"
                                        self.yang_parent_name = "data"

                                        self.processed_bytes = YLeaf(YType.uint64, "processed-bytes")

                                        self.processed_pkts = YLeaf(YType.uint64, "processed-pkts")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("processed_bytes",
                                                        "processed_pkts") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Sf, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Sf, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.processed_bytes.is_set or
                                            self.processed_pkts.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.processed_bytes.yfilter != YFilter.not_set or
                                            self.processed_pkts.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "sf" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.processed_bytes.is_set or self.processed_bytes.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.processed_bytes.get_name_leafdata())
                                        if (self.processed_pkts.is_set or self.processed_pkts.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.processed_pkts.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "processed-bytes" or name == "processed-pkts"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "processed-bytes"):
                                            self.processed_bytes = value
                                            self.processed_bytes.value_namespace = name_space
                                            self.processed_bytes.value_namespace_prefix = name_space_prefix
                                        if(value_path == "processed-pkts"):
                                            self.processed_pkts = value
                                            self.processed_pkts.value_namespace = name_space
                                            self.processed_pkts.value_namespace_prefix = name_space_prefix


                                class Sff(Entity):
                                    """
                                    Service function forwarder stats
                                    
                                    .. attribute:: processed_bytes
                                    
                                    	Total bytes processed
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: processed_pkts
                                    
                                    	Number of packets processed
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-ea-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Sff, self).__init__()

                                        self.yang_name = "sff"
                                        self.yang_parent_name = "data"

                                        self.processed_bytes = YLeaf(YType.uint64, "processed-bytes")

                                        self.processed_pkts = YLeaf(YType.uint64, "processed-pkts")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("processed_bytes",
                                                        "processed_pkts") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Sff, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Sff, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.processed_bytes.is_set or
                                            self.processed_pkts.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.processed_bytes.yfilter != YFilter.not_set or
                                            self.processed_pkts.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "sff" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.processed_bytes.is_set or self.processed_bytes.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.processed_bytes.get_name_leafdata())
                                        if (self.processed_pkts.is_set or self.processed_pkts.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.processed_pkts.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "processed-bytes" or name == "processed-pkts"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "processed-bytes"):
                                            self.processed_bytes = value
                                            self.processed_bytes.value_namespace = name_space
                                            self.processed_bytes.value_namespace_prefix = name_space_prefix
                                        if(value_path == "processed-pkts"):
                                            self.processed_pkts = value
                                            self.processed_pkts.value_namespace = name_space
                                            self.processed_pkts.value_namespace_prefix = name_space_prefix


                                class SffLocal(Entity):
                                    """
                                    Local service function forwarder stats
                                    
                                    .. attribute:: lookup_err_bytes
                                    
                                    	Total bytes with unknown spi\-si
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: lookup_err_pkts
                                    
                                    	Number of packets with unknown spi\-si
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: malformed_err_bytes
                                    
                                    	Total bytes with invalid NSH header
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: malformed_err_pkts
                                    
                                    	Number of packets with invalid NSH header
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-ea-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.SffLocal, self).__init__()

                                        self.yang_name = "sff-local"
                                        self.yang_parent_name = "data"

                                        self.lookup_err_bytes = YLeaf(YType.uint64, "lookup-err-bytes")

                                        self.lookup_err_pkts = YLeaf(YType.uint64, "lookup-err-pkts")

                                        self.malformed_err_bytes = YLeaf(YType.uint64, "malformed-err-bytes")

                                        self.malformed_err_pkts = YLeaf(YType.uint64, "malformed-err-pkts")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("lookup_err_bytes",
                                                        "lookup_err_pkts",
                                                        "malformed_err_bytes",
                                                        "malformed_err_pkts") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.SffLocal, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.SffLocal, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.lookup_err_bytes.is_set or
                                            self.lookup_err_pkts.is_set or
                                            self.malformed_err_bytes.is_set or
                                            self.malformed_err_pkts.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.lookup_err_bytes.yfilter != YFilter.not_set or
                                            self.lookup_err_pkts.yfilter != YFilter.not_set or
                                            self.malformed_err_bytes.yfilter != YFilter.not_set or
                                            self.malformed_err_pkts.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "sff-local" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.lookup_err_bytes.is_set or self.lookup_err_bytes.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.lookup_err_bytes.get_name_leafdata())
                                        if (self.lookup_err_pkts.is_set or self.lookup_err_pkts.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.lookup_err_pkts.get_name_leafdata())
                                        if (self.malformed_err_bytes.is_set or self.malformed_err_bytes.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.malformed_err_bytes.get_name_leafdata())
                                        if (self.malformed_err_pkts.is_set or self.malformed_err_pkts.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.malformed_err_pkts.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "lookup-err-bytes" or name == "lookup-err-pkts" or name == "malformed-err-bytes" or name == "malformed-err-pkts"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "lookup-err-bytes"):
                                            self.lookup_err_bytes = value
                                            self.lookup_err_bytes.value_namespace = name_space
                                            self.lookup_err_bytes.value_namespace_prefix = name_space_prefix
                                        if(value_path == "lookup-err-pkts"):
                                            self.lookup_err_pkts = value
                                            self.lookup_err_pkts.value_namespace = name_space
                                            self.lookup_err_pkts.value_namespace_prefix = name_space_prefix
                                        if(value_path == "malformed-err-bytes"):
                                            self.malformed_err_bytes = value
                                            self.malformed_err_bytes.value_namespace = name_space
                                            self.malformed_err_bytes.value_namespace_prefix = name_space_prefix
                                        if(value_path == "malformed-err-pkts"):
                                            self.malformed_err_pkts = value
                                            self.malformed_err_pkts.value_namespace = name_space
                                            self.malformed_err_pkts.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    return (
                                        self.type.is_set or
                                        (self.sf is not None and self.sf.has_data()) or
                                        (self.sff is not None and self.sff.has_data()) or
                                        (self.sff_local is not None and self.sff_local.has_data()) or
                                        (self.sfp is not None and self.sfp.has_data()) or
                                        (self.spi_si is not None and self.spi_si.has_data()) or
                                        (self.term is not None and self.term.has_data()))

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.type.yfilter != YFilter.not_set or
                                        (self.sf is not None and self.sf.has_operation()) or
                                        (self.sff is not None and self.sff.has_operation()) or
                                        (self.sff_local is not None and self.sff_local.has_operation()) or
                                        (self.sfp is not None and self.sfp.has_operation()) or
                                        (self.spi_si is not None and self.spi_si.has_operation()) or
                                        (self.term is not None and self.term.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "data" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.type.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "sf"):
                                        if (self.sf is None):
                                            self.sf = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Sf()
                                            self.sf.parent = self
                                            self._children_name_map["sf"] = "sf"
                                        return self.sf

                                    if (child_yang_name == "sff"):
                                        if (self.sff is None):
                                            self.sff = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Sff()
                                            self.sff.parent = self
                                            self._children_name_map["sff"] = "sff"
                                        return self.sff

                                    if (child_yang_name == "sff-local"):
                                        if (self.sff_local is None):
                                            self.sff_local = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.SffLocal()
                                            self.sff_local.parent = self
                                            self._children_name_map["sff_local"] = "sff-local"
                                        return self.sff_local

                                    if (child_yang_name == "sfp"):
                                        if (self.sfp is None):
                                            self.sfp = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Sfp()
                                            self.sfp.parent = self
                                            self._children_name_map["sfp"] = "sfp"
                                        return self.sfp

                                    if (child_yang_name == "spi-si"):
                                        if (self.spi_si is None):
                                            self.spi_si = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.SpiSi()
                                            self.spi_si.parent = self
                                            self._children_name_map["spi_si"] = "spi-si"
                                        return self.spi_si

                                    if (child_yang_name == "term"):
                                        if (self.term is None):
                                            self.term = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Term()
                                            self.term.parent = self
                                            self._children_name_map["term"] = "term"
                                        return self.term

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "sf" or name == "sff" or name == "sff-local" or name == "sfp" or name == "spi-si" or name == "term" or name == "type"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "type"):
                                        self.type = value
                                        self.type.value_namespace = name_space
                                        self.type.value_namespace_prefix = name_space_prefix


                            class SiArr(Entity):
                                """
                                SI array in case of detail stats
                                
                                .. attribute:: data
                                
                                	Stats counter for this index
                                	**type**\:   :py:class:`Data <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.SiArr.Data>`
                                
                                .. attribute:: si
                                
                                	Service index
                                	**type**\:  int
                                
                                	**range:** 0..255
                                
                                

                                """

                                _prefix = 'pbr-vservice-ea-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.SiArr, self).__init__()

                                    self.yang_name = "si-arr"
                                    self.yang_parent_name = "error"

                                    self.si = YLeaf(YType.uint8, "si")

                                    self.data = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.SiArr.Data()
                                    self.data.parent = self
                                    self._children_name_map["data"] = "data"
                                    self._children_yang_names.add("data")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("si") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.SiArr, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.SiArr, self).__setattr__(name, value)


                                class Data(Entity):
                                    """
                                    Stats counter for this index
                                    
                                    .. attribute:: spi_si
                                    
                                    	SF/SFF stats
                                    	**type**\:   :py:class:`SpiSi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.SiArr.Data.SpiSi>`
                                    
                                    .. attribute:: term
                                    
                                    	Terminate stats
                                    	**type**\:   :py:class:`Term <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.SiArr.Data.Term>`
                                    
                                    .. attribute:: type
                                    
                                    	type
                                    	**type**\:   :py:class:`VsNshStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.VsNshStats>`
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-ea-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.SiArr.Data, self).__init__()

                                        self.yang_name = "data"
                                        self.yang_parent_name = "si-arr"

                                        self.type = YLeaf(YType.enumeration, "type")

                                        self.spi_si = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.SiArr.Data.SpiSi()
                                        self.spi_si.parent = self
                                        self._children_name_map["spi_si"] = "spi-si"
                                        self._children_yang_names.add("spi-si")

                                        self.term = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.SiArr.Data.Term()
                                        self.term.parent = self
                                        self._children_name_map["term"] = "term"
                                        self._children_yang_names.add("term")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("type") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.SiArr.Data, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.SiArr.Data, self).__setattr__(name, value)


                                    class SpiSi(Entity):
                                        """
                                        SF/SFF stats
                                        
                                        .. attribute:: processed_bytes
                                        
                                        	Total bytes processed
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: processed_pkts
                                        
                                        	Number of packets processed
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        

                                        """

                                        _prefix = 'pbr-vservice-ea-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.SiArr.Data.SpiSi, self).__init__()

                                            self.yang_name = "spi-si"
                                            self.yang_parent_name = "data"

                                            self.processed_bytes = YLeaf(YType.uint64, "processed-bytes")

                                            self.processed_pkts = YLeaf(YType.uint64, "processed-pkts")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("processed_bytes",
                                                            "processed_pkts") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.SiArr.Data.SpiSi, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.SiArr.Data.SpiSi, self).__setattr__(name, value)

                                        def has_data(self):
                                            return (
                                                self.processed_bytes.is_set or
                                                self.processed_pkts.is_set)

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.processed_bytes.yfilter != YFilter.not_set or
                                                self.processed_pkts.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "spi-si" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.processed_bytes.is_set or self.processed_bytes.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.processed_bytes.get_name_leafdata())
                                            if (self.processed_pkts.is_set or self.processed_pkts.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.processed_pkts.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "processed-bytes" or name == "processed-pkts"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "processed-bytes"):
                                                self.processed_bytes = value
                                                self.processed_bytes.value_namespace = name_space
                                                self.processed_bytes.value_namespace_prefix = name_space_prefix
                                            if(value_path == "processed-pkts"):
                                                self.processed_pkts = value
                                                self.processed_pkts.value_namespace = name_space
                                                self.processed_pkts.value_namespace_prefix = name_space_prefix


                                    class Term(Entity):
                                        """
                                        Terminate stats
                                        
                                        .. attribute:: terminated_bytes
                                        
                                        	Total bytes terminated
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: terminated_pkts
                                        
                                        	Number of terminated packets
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        

                                        """

                                        _prefix = 'pbr-vservice-ea-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.SiArr.Data.Term, self).__init__()

                                            self.yang_name = "term"
                                            self.yang_parent_name = "data"

                                            self.terminated_bytes = YLeaf(YType.uint64, "terminated-bytes")

                                            self.terminated_pkts = YLeaf(YType.uint64, "terminated-pkts")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("terminated_bytes",
                                                            "terminated_pkts") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.SiArr.Data.Term, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.SiArr.Data.Term, self).__setattr__(name, value)

                                        def has_data(self):
                                            return (
                                                self.terminated_bytes.is_set or
                                                self.terminated_pkts.is_set)

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.terminated_bytes.yfilter != YFilter.not_set or
                                                self.terminated_pkts.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "term" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.terminated_bytes.is_set or self.terminated_bytes.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.terminated_bytes.get_name_leafdata())
                                            if (self.terminated_pkts.is_set or self.terminated_pkts.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.terminated_pkts.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "terminated-bytes" or name == "terminated-pkts"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "terminated-bytes"):
                                                self.terminated_bytes = value
                                                self.terminated_bytes.value_namespace = name_space
                                                self.terminated_bytes.value_namespace_prefix = name_space_prefix
                                            if(value_path == "terminated-pkts"):
                                                self.terminated_pkts = value
                                                self.terminated_pkts.value_namespace = name_space
                                                self.terminated_pkts.value_namespace_prefix = name_space_prefix

                                    def has_data(self):
                                        return (
                                            self.type.is_set or
                                            (self.spi_si is not None and self.spi_si.has_data()) or
                                            (self.term is not None and self.term.has_data()))

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.type.yfilter != YFilter.not_set or
                                            (self.spi_si is not None and self.spi_si.has_operation()) or
                                            (self.term is not None and self.term.has_operation()))

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "data" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.type.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        if (child_yang_name == "spi-si"):
                                            if (self.spi_si is None):
                                                self.spi_si = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.SiArr.Data.SpiSi()
                                                self.spi_si.parent = self
                                                self._children_name_map["spi_si"] = "spi-si"
                                            return self.spi_si

                                        if (child_yang_name == "term"):
                                            if (self.term is None):
                                                self.term = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.SiArr.Data.Term()
                                                self.term.parent = self
                                                self._children_name_map["term"] = "term"
                                            return self.term

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "spi-si" or name == "term" or name == "type"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "type"):
                                            self.type = value
                                            self.type.value_namespace = name_space
                                            self.type.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    return (
                                        self.si.is_set or
                                        (self.data is not None and self.data.has_data()))

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.si.yfilter != YFilter.not_set or
                                        (self.data is not None and self.data.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "si-arr" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.si.is_set or self.si.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.si.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "data"):
                                        if (self.data is None):
                                            self.data = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.SiArr.Data()
                                            self.data.parent = self
                                            self._children_name_map["data"] = "data"
                                        return self.data

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "data" or name == "si"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "si"):
                                        self.si = value
                                        self.si.value_namespace = name_space
                                        self.si.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                for c in self.si_arr:
                                    if (c.has_data()):
                                        return True
                                return (self.data is not None and self.data.has_data())

                            def has_operation(self):
                                for c in self.si_arr:
                                    if (c.has_operation()):
                                        return True
                                return (
                                    self.yfilter != YFilter.not_set or
                                    (self.data is not None and self.data.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "error" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "data"):
                                    if (self.data is None):
                                        self.data = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data()
                                        self.data.parent = self
                                        self._children_name_map["data"] = "data"
                                    return self.data

                                if (child_yang_name == "si-arr"):
                                    for c in self.si_arr:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.SiArr()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.si_arr.append(c)
                                    return c

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "data" or name == "si-arr"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass

                        def has_data(self):
                            return (self.error is not None and self.error.has_data())

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                (self.error is not None and self.error.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "local" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "error"):
                                if (self.error is None):
                                    self.error = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error()
                                    self.error.parent = self
                                    self._children_name_map["error"] = "error"
                                return self.error

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "error"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass


                    class SffNames(Entity):
                        """
                        List of Service Function Forwarder Names
                        
                        .. attribute:: sff_name
                        
                        	Name of Service Function Forwarder
                        	**type**\: list of    :py:class:`SffName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName>`
                        
                        

                        """

                        _prefix = 'pbr-vservice-ea-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames, self).__init__()

                            self.yang_name = "sff-names"
                            self.yang_parent_name = "service-function-forwarder"

                            self.sff_name = YList(self)

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in () and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames, self).__setattr__(name, value)


                        class SffName(Entity):
                            """
                            Name of Service Function Forwarder
                            
                            .. attribute:: name  <key>
                            
                            	Name
                            	**type**\:  str
                            
                            	**length:** 1..32
                            
                            .. attribute:: data
                            
                            	Statistics data
                            	**type**\:   :py:class:`Data <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data>`
                            
                            .. attribute:: si_arr
                            
                            	SI array in case of detail stats
                            	**type**\: list of    :py:class:`SiArr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.SiArr>`
                            
                            

                            """

                            _prefix = 'pbr-vservice-ea-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName, self).__init__()

                                self.yang_name = "sff-name"
                                self.yang_parent_name = "sff-names"

                                self.name = YLeaf(YType.str, "name")

                                self.data = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data()
                                self.data.parent = self
                                self._children_name_map["data"] = "data"
                                self._children_yang_names.add("data")

                                self.si_arr = YList(self)

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("name") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName, self).__setattr__(name, value)


                            class Data(Entity):
                                """
                                Statistics data
                                
                                .. attribute:: sf
                                
                                	Service function stats
                                	**type**\:   :py:class:`Sf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Sf>`
                                
                                .. attribute:: sff
                                
                                	Service function forwarder stats
                                	**type**\:   :py:class:`Sff <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Sff>`
                                
                                .. attribute:: sff_local
                                
                                	Local service function forwarder stats
                                	**type**\:   :py:class:`SffLocal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.SffLocal>`
                                
                                .. attribute:: sfp
                                
                                	SFP stats
                                	**type**\:   :py:class:`Sfp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Sfp>`
                                
                                .. attribute:: spi_si
                                
                                	SPI SI stats
                                	**type**\:   :py:class:`SpiSi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.SpiSi>`
                                
                                .. attribute:: term
                                
                                	Terminate stats
                                	**type**\:   :py:class:`Term <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Term>`
                                
                                .. attribute:: type
                                
                                	type
                                	**type**\:   :py:class:`VsNshStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.VsNshStats>`
                                
                                

                                """

                                _prefix = 'pbr-vservice-ea-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data, self).__init__()

                                    self.yang_name = "data"
                                    self.yang_parent_name = "sff-name"

                                    self.type = YLeaf(YType.enumeration, "type")

                                    self.sf = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Sf()
                                    self.sf.parent = self
                                    self._children_name_map["sf"] = "sf"
                                    self._children_yang_names.add("sf")

                                    self.sff = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Sff()
                                    self.sff.parent = self
                                    self._children_name_map["sff"] = "sff"
                                    self._children_yang_names.add("sff")

                                    self.sff_local = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.SffLocal()
                                    self.sff_local.parent = self
                                    self._children_name_map["sff_local"] = "sff-local"
                                    self._children_yang_names.add("sff-local")

                                    self.sfp = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Sfp()
                                    self.sfp.parent = self
                                    self._children_name_map["sfp"] = "sfp"
                                    self._children_yang_names.add("sfp")

                                    self.spi_si = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.SpiSi()
                                    self.spi_si.parent = self
                                    self._children_name_map["spi_si"] = "spi-si"
                                    self._children_yang_names.add("spi-si")

                                    self.term = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Term()
                                    self.term.parent = self
                                    self._children_name_map["term"] = "term"
                                    self._children_yang_names.add("term")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("type") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data, self).__setattr__(name, value)


                                class Sfp(Entity):
                                    """
                                    SFP stats
                                    
                                    .. attribute:: spi_si
                                    
                                    	Service index counters
                                    	**type**\:   :py:class:`SpiSi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Sfp.SpiSi>`
                                    
                                    .. attribute:: term
                                    
                                    	Terminate counters
                                    	**type**\:   :py:class:`Term <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Sfp.Term>`
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-ea-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Sfp, self).__init__()

                                        self.yang_name = "sfp"
                                        self.yang_parent_name = "data"

                                        self.spi_si = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Sfp.SpiSi()
                                        self.spi_si.parent = self
                                        self._children_name_map["spi_si"] = "spi-si"
                                        self._children_yang_names.add("spi-si")

                                        self.term = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Sfp.Term()
                                        self.term.parent = self
                                        self._children_name_map["term"] = "term"
                                        self._children_yang_names.add("term")


                                    class SpiSi(Entity):
                                        """
                                        Service index counters
                                        
                                        .. attribute:: processed_bytes
                                        
                                        	Total bytes processed
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: processed_pkts
                                        
                                        	Number of packets processed
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        

                                        """

                                        _prefix = 'pbr-vservice-ea-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Sfp.SpiSi, self).__init__()

                                            self.yang_name = "spi-si"
                                            self.yang_parent_name = "sfp"

                                            self.processed_bytes = YLeaf(YType.uint64, "processed-bytes")

                                            self.processed_pkts = YLeaf(YType.uint64, "processed-pkts")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("processed_bytes",
                                                            "processed_pkts") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Sfp.SpiSi, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Sfp.SpiSi, self).__setattr__(name, value)

                                        def has_data(self):
                                            return (
                                                self.processed_bytes.is_set or
                                                self.processed_pkts.is_set)

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.processed_bytes.yfilter != YFilter.not_set or
                                                self.processed_pkts.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "spi-si" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.processed_bytes.is_set or self.processed_bytes.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.processed_bytes.get_name_leafdata())
                                            if (self.processed_pkts.is_set or self.processed_pkts.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.processed_pkts.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "processed-bytes" or name == "processed-pkts"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "processed-bytes"):
                                                self.processed_bytes = value
                                                self.processed_bytes.value_namespace = name_space
                                                self.processed_bytes.value_namespace_prefix = name_space_prefix
                                            if(value_path == "processed-pkts"):
                                                self.processed_pkts = value
                                                self.processed_pkts.value_namespace = name_space
                                                self.processed_pkts.value_namespace_prefix = name_space_prefix


                                    class Term(Entity):
                                        """
                                        Terminate counters
                                        
                                        .. attribute:: terminated_bytes
                                        
                                        	Total bytes terminated
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: terminated_pkts
                                        
                                        	Number of terminated packets
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        

                                        """

                                        _prefix = 'pbr-vservice-ea-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Sfp.Term, self).__init__()

                                            self.yang_name = "term"
                                            self.yang_parent_name = "sfp"

                                            self.terminated_bytes = YLeaf(YType.uint64, "terminated-bytes")

                                            self.terminated_pkts = YLeaf(YType.uint64, "terminated-pkts")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("terminated_bytes",
                                                            "terminated_pkts") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Sfp.Term, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Sfp.Term, self).__setattr__(name, value)

                                        def has_data(self):
                                            return (
                                                self.terminated_bytes.is_set or
                                                self.terminated_pkts.is_set)

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.terminated_bytes.yfilter != YFilter.not_set or
                                                self.terminated_pkts.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "term" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.terminated_bytes.is_set or self.terminated_bytes.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.terminated_bytes.get_name_leafdata())
                                            if (self.terminated_pkts.is_set or self.terminated_pkts.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.terminated_pkts.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "terminated-bytes" or name == "terminated-pkts"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "terminated-bytes"):
                                                self.terminated_bytes = value
                                                self.terminated_bytes.value_namespace = name_space
                                                self.terminated_bytes.value_namespace_prefix = name_space_prefix
                                            if(value_path == "terminated-pkts"):
                                                self.terminated_pkts = value
                                                self.terminated_pkts.value_namespace = name_space
                                                self.terminated_pkts.value_namespace_prefix = name_space_prefix

                                    def has_data(self):
                                        return (
                                            (self.spi_si is not None and self.spi_si.has_data()) or
                                            (self.term is not None and self.term.has_data()))

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            (self.spi_si is not None and self.spi_si.has_operation()) or
                                            (self.term is not None and self.term.has_operation()))

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "sfp" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        if (child_yang_name == "spi-si"):
                                            if (self.spi_si is None):
                                                self.spi_si = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Sfp.SpiSi()
                                                self.spi_si.parent = self
                                                self._children_name_map["spi_si"] = "spi-si"
                                            return self.spi_si

                                        if (child_yang_name == "term"):
                                            if (self.term is None):
                                                self.term = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Sfp.Term()
                                                self.term.parent = self
                                                self._children_name_map["term"] = "term"
                                            return self.term

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "spi-si" or name == "term"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        pass


                                class SpiSi(Entity):
                                    """
                                    SPI SI stats
                                    
                                    .. attribute:: processed_bytes
                                    
                                    	Total bytes processed
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: processed_pkts
                                    
                                    	Number of packets processed
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-ea-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.SpiSi, self).__init__()

                                        self.yang_name = "spi-si"
                                        self.yang_parent_name = "data"

                                        self.processed_bytes = YLeaf(YType.uint64, "processed-bytes")

                                        self.processed_pkts = YLeaf(YType.uint64, "processed-pkts")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("processed_bytes",
                                                        "processed_pkts") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.SpiSi, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.SpiSi, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.processed_bytes.is_set or
                                            self.processed_pkts.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.processed_bytes.yfilter != YFilter.not_set or
                                            self.processed_pkts.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "spi-si" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.processed_bytes.is_set or self.processed_bytes.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.processed_bytes.get_name_leafdata())
                                        if (self.processed_pkts.is_set or self.processed_pkts.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.processed_pkts.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "processed-bytes" or name == "processed-pkts"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "processed-bytes"):
                                            self.processed_bytes = value
                                            self.processed_bytes.value_namespace = name_space
                                            self.processed_bytes.value_namespace_prefix = name_space_prefix
                                        if(value_path == "processed-pkts"):
                                            self.processed_pkts = value
                                            self.processed_pkts.value_namespace = name_space
                                            self.processed_pkts.value_namespace_prefix = name_space_prefix


                                class Term(Entity):
                                    """
                                    Terminate stats
                                    
                                    .. attribute:: terminated_bytes
                                    
                                    	Total bytes terminated
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: terminated_pkts
                                    
                                    	Number of terminated packets
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-ea-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Term, self).__init__()

                                        self.yang_name = "term"
                                        self.yang_parent_name = "data"

                                        self.terminated_bytes = YLeaf(YType.uint64, "terminated-bytes")

                                        self.terminated_pkts = YLeaf(YType.uint64, "terminated-pkts")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("terminated_bytes",
                                                        "terminated_pkts") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Term, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Term, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.terminated_bytes.is_set or
                                            self.terminated_pkts.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.terminated_bytes.yfilter != YFilter.not_set or
                                            self.terminated_pkts.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "term" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.terminated_bytes.is_set or self.terminated_bytes.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.terminated_bytes.get_name_leafdata())
                                        if (self.terminated_pkts.is_set or self.terminated_pkts.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.terminated_pkts.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "terminated-bytes" or name == "terminated-pkts"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "terminated-bytes"):
                                            self.terminated_bytes = value
                                            self.terminated_bytes.value_namespace = name_space
                                            self.terminated_bytes.value_namespace_prefix = name_space_prefix
                                        if(value_path == "terminated-pkts"):
                                            self.terminated_pkts = value
                                            self.terminated_pkts.value_namespace = name_space
                                            self.terminated_pkts.value_namespace_prefix = name_space_prefix


                                class Sf(Entity):
                                    """
                                    Service function stats
                                    
                                    .. attribute:: processed_bytes
                                    
                                    	Total bytes processed
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: processed_pkts
                                    
                                    	Number of packets processed
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-ea-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Sf, self).__init__()

                                        self.yang_name = "sf"
                                        self.yang_parent_name = "data"

                                        self.processed_bytes = YLeaf(YType.uint64, "processed-bytes")

                                        self.processed_pkts = YLeaf(YType.uint64, "processed-pkts")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("processed_bytes",
                                                        "processed_pkts") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Sf, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Sf, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.processed_bytes.is_set or
                                            self.processed_pkts.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.processed_bytes.yfilter != YFilter.not_set or
                                            self.processed_pkts.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "sf" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.processed_bytes.is_set or self.processed_bytes.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.processed_bytes.get_name_leafdata())
                                        if (self.processed_pkts.is_set or self.processed_pkts.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.processed_pkts.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "processed-bytes" or name == "processed-pkts"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "processed-bytes"):
                                            self.processed_bytes = value
                                            self.processed_bytes.value_namespace = name_space
                                            self.processed_bytes.value_namespace_prefix = name_space_prefix
                                        if(value_path == "processed-pkts"):
                                            self.processed_pkts = value
                                            self.processed_pkts.value_namespace = name_space
                                            self.processed_pkts.value_namespace_prefix = name_space_prefix


                                class Sff(Entity):
                                    """
                                    Service function forwarder stats
                                    
                                    .. attribute:: processed_bytes
                                    
                                    	Total bytes processed
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: processed_pkts
                                    
                                    	Number of packets processed
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-ea-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Sff, self).__init__()

                                        self.yang_name = "sff"
                                        self.yang_parent_name = "data"

                                        self.processed_bytes = YLeaf(YType.uint64, "processed-bytes")

                                        self.processed_pkts = YLeaf(YType.uint64, "processed-pkts")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("processed_bytes",
                                                        "processed_pkts") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Sff, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Sff, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.processed_bytes.is_set or
                                            self.processed_pkts.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.processed_bytes.yfilter != YFilter.not_set or
                                            self.processed_pkts.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "sff" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.processed_bytes.is_set or self.processed_bytes.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.processed_bytes.get_name_leafdata())
                                        if (self.processed_pkts.is_set or self.processed_pkts.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.processed_pkts.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "processed-bytes" or name == "processed-pkts"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "processed-bytes"):
                                            self.processed_bytes = value
                                            self.processed_bytes.value_namespace = name_space
                                            self.processed_bytes.value_namespace_prefix = name_space_prefix
                                        if(value_path == "processed-pkts"):
                                            self.processed_pkts = value
                                            self.processed_pkts.value_namespace = name_space
                                            self.processed_pkts.value_namespace_prefix = name_space_prefix


                                class SffLocal(Entity):
                                    """
                                    Local service function forwarder stats
                                    
                                    .. attribute:: lookup_err_bytes
                                    
                                    	Total bytes with unknown spi\-si
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: lookup_err_pkts
                                    
                                    	Number of packets with unknown spi\-si
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: malformed_err_bytes
                                    
                                    	Total bytes with invalid NSH header
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: malformed_err_pkts
                                    
                                    	Number of packets with invalid NSH header
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-ea-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.SffLocal, self).__init__()

                                        self.yang_name = "sff-local"
                                        self.yang_parent_name = "data"

                                        self.lookup_err_bytes = YLeaf(YType.uint64, "lookup-err-bytes")

                                        self.lookup_err_pkts = YLeaf(YType.uint64, "lookup-err-pkts")

                                        self.malformed_err_bytes = YLeaf(YType.uint64, "malformed-err-bytes")

                                        self.malformed_err_pkts = YLeaf(YType.uint64, "malformed-err-pkts")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("lookup_err_bytes",
                                                        "lookup_err_pkts",
                                                        "malformed_err_bytes",
                                                        "malformed_err_pkts") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.SffLocal, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.SffLocal, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.lookup_err_bytes.is_set or
                                            self.lookup_err_pkts.is_set or
                                            self.malformed_err_bytes.is_set or
                                            self.malformed_err_pkts.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.lookup_err_bytes.yfilter != YFilter.not_set or
                                            self.lookup_err_pkts.yfilter != YFilter.not_set or
                                            self.malformed_err_bytes.yfilter != YFilter.not_set or
                                            self.malformed_err_pkts.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "sff-local" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.lookup_err_bytes.is_set or self.lookup_err_bytes.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.lookup_err_bytes.get_name_leafdata())
                                        if (self.lookup_err_pkts.is_set or self.lookup_err_pkts.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.lookup_err_pkts.get_name_leafdata())
                                        if (self.malformed_err_bytes.is_set or self.malformed_err_bytes.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.malformed_err_bytes.get_name_leafdata())
                                        if (self.malformed_err_pkts.is_set or self.malformed_err_pkts.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.malformed_err_pkts.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "lookup-err-bytes" or name == "lookup-err-pkts" or name == "malformed-err-bytes" or name == "malformed-err-pkts"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "lookup-err-bytes"):
                                            self.lookup_err_bytes = value
                                            self.lookup_err_bytes.value_namespace = name_space
                                            self.lookup_err_bytes.value_namespace_prefix = name_space_prefix
                                        if(value_path == "lookup-err-pkts"):
                                            self.lookup_err_pkts = value
                                            self.lookup_err_pkts.value_namespace = name_space
                                            self.lookup_err_pkts.value_namespace_prefix = name_space_prefix
                                        if(value_path == "malformed-err-bytes"):
                                            self.malformed_err_bytes = value
                                            self.malformed_err_bytes.value_namespace = name_space
                                            self.malformed_err_bytes.value_namespace_prefix = name_space_prefix
                                        if(value_path == "malformed-err-pkts"):
                                            self.malformed_err_pkts = value
                                            self.malformed_err_pkts.value_namespace = name_space
                                            self.malformed_err_pkts.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    return (
                                        self.type.is_set or
                                        (self.sf is not None and self.sf.has_data()) or
                                        (self.sff is not None and self.sff.has_data()) or
                                        (self.sff_local is not None and self.sff_local.has_data()) or
                                        (self.sfp is not None and self.sfp.has_data()) or
                                        (self.spi_si is not None and self.spi_si.has_data()) or
                                        (self.term is not None and self.term.has_data()))

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.type.yfilter != YFilter.not_set or
                                        (self.sf is not None and self.sf.has_operation()) or
                                        (self.sff is not None and self.sff.has_operation()) or
                                        (self.sff_local is not None and self.sff_local.has_operation()) or
                                        (self.sfp is not None and self.sfp.has_operation()) or
                                        (self.spi_si is not None and self.spi_si.has_operation()) or
                                        (self.term is not None and self.term.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "data" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.type.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "sf"):
                                        if (self.sf is None):
                                            self.sf = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Sf()
                                            self.sf.parent = self
                                            self._children_name_map["sf"] = "sf"
                                        return self.sf

                                    if (child_yang_name == "sff"):
                                        if (self.sff is None):
                                            self.sff = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Sff()
                                            self.sff.parent = self
                                            self._children_name_map["sff"] = "sff"
                                        return self.sff

                                    if (child_yang_name == "sff-local"):
                                        if (self.sff_local is None):
                                            self.sff_local = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.SffLocal()
                                            self.sff_local.parent = self
                                            self._children_name_map["sff_local"] = "sff-local"
                                        return self.sff_local

                                    if (child_yang_name == "sfp"):
                                        if (self.sfp is None):
                                            self.sfp = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Sfp()
                                            self.sfp.parent = self
                                            self._children_name_map["sfp"] = "sfp"
                                        return self.sfp

                                    if (child_yang_name == "spi-si"):
                                        if (self.spi_si is None):
                                            self.spi_si = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.SpiSi()
                                            self.spi_si.parent = self
                                            self._children_name_map["spi_si"] = "spi-si"
                                        return self.spi_si

                                    if (child_yang_name == "term"):
                                        if (self.term is None):
                                            self.term = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Term()
                                            self.term.parent = self
                                            self._children_name_map["term"] = "term"
                                        return self.term

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "sf" or name == "sff" or name == "sff-local" or name == "sfp" or name == "spi-si" or name == "term" or name == "type"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "type"):
                                        self.type = value
                                        self.type.value_namespace = name_space
                                        self.type.value_namespace_prefix = name_space_prefix


                            class SiArr(Entity):
                                """
                                SI array in case of detail stats
                                
                                .. attribute:: data
                                
                                	Stats counter for this index
                                	**type**\:   :py:class:`Data <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data>`
                                
                                .. attribute:: si
                                
                                	Service index
                                	**type**\:  int
                                
                                	**range:** 0..255
                                
                                

                                """

                                _prefix = 'pbr-vservice-ea-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.SiArr, self).__init__()

                                    self.yang_name = "si-arr"
                                    self.yang_parent_name = "sff-name"

                                    self.si = YLeaf(YType.uint8, "si")

                                    self.data = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data()
                                    self.data.parent = self
                                    self._children_name_map["data"] = "data"
                                    self._children_yang_names.add("data")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("si") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.SiArr, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.SiArr, self).__setattr__(name, value)


                                class Data(Entity):
                                    """
                                    Stats counter for this index
                                    
                                    .. attribute:: spi_si
                                    
                                    	SF/SFF stats
                                    	**type**\:   :py:class:`SpiSi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data.SpiSi>`
                                    
                                    .. attribute:: term
                                    
                                    	Terminate stats
                                    	**type**\:   :py:class:`Term <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data.Term>`
                                    
                                    .. attribute:: type
                                    
                                    	type
                                    	**type**\:   :py:class:`VsNshStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.VsNshStats>`
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-ea-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data, self).__init__()

                                        self.yang_name = "data"
                                        self.yang_parent_name = "si-arr"

                                        self.type = YLeaf(YType.enumeration, "type")

                                        self.spi_si = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data.SpiSi()
                                        self.spi_si.parent = self
                                        self._children_name_map["spi_si"] = "spi-si"
                                        self._children_yang_names.add("spi-si")

                                        self.term = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data.Term()
                                        self.term.parent = self
                                        self._children_name_map["term"] = "term"
                                        self._children_yang_names.add("term")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("type") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data, self).__setattr__(name, value)


                                    class SpiSi(Entity):
                                        """
                                        SF/SFF stats
                                        
                                        .. attribute:: processed_bytes
                                        
                                        	Total bytes processed
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: processed_pkts
                                        
                                        	Number of packets processed
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        

                                        """

                                        _prefix = 'pbr-vservice-ea-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data.SpiSi, self).__init__()

                                            self.yang_name = "spi-si"
                                            self.yang_parent_name = "data"

                                            self.processed_bytes = YLeaf(YType.uint64, "processed-bytes")

                                            self.processed_pkts = YLeaf(YType.uint64, "processed-pkts")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("processed_bytes",
                                                            "processed_pkts") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data.SpiSi, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data.SpiSi, self).__setattr__(name, value)

                                        def has_data(self):
                                            return (
                                                self.processed_bytes.is_set or
                                                self.processed_pkts.is_set)

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.processed_bytes.yfilter != YFilter.not_set or
                                                self.processed_pkts.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "spi-si" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.processed_bytes.is_set or self.processed_bytes.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.processed_bytes.get_name_leafdata())
                                            if (self.processed_pkts.is_set or self.processed_pkts.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.processed_pkts.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "processed-bytes" or name == "processed-pkts"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "processed-bytes"):
                                                self.processed_bytes = value
                                                self.processed_bytes.value_namespace = name_space
                                                self.processed_bytes.value_namespace_prefix = name_space_prefix
                                            if(value_path == "processed-pkts"):
                                                self.processed_pkts = value
                                                self.processed_pkts.value_namespace = name_space
                                                self.processed_pkts.value_namespace_prefix = name_space_prefix


                                    class Term(Entity):
                                        """
                                        Terminate stats
                                        
                                        .. attribute:: terminated_bytes
                                        
                                        	Total bytes terminated
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: terminated_pkts
                                        
                                        	Number of terminated packets
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        

                                        """

                                        _prefix = 'pbr-vservice-ea-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data.Term, self).__init__()

                                            self.yang_name = "term"
                                            self.yang_parent_name = "data"

                                            self.terminated_bytes = YLeaf(YType.uint64, "terminated-bytes")

                                            self.terminated_pkts = YLeaf(YType.uint64, "terminated-pkts")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("terminated_bytes",
                                                            "terminated_pkts") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data.Term, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data.Term, self).__setattr__(name, value)

                                        def has_data(self):
                                            return (
                                                self.terminated_bytes.is_set or
                                                self.terminated_pkts.is_set)

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.terminated_bytes.yfilter != YFilter.not_set or
                                                self.terminated_pkts.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "term" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.terminated_bytes.is_set or self.terminated_bytes.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.terminated_bytes.get_name_leafdata())
                                            if (self.terminated_pkts.is_set or self.terminated_pkts.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.terminated_pkts.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "terminated-bytes" or name == "terminated-pkts"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "terminated-bytes"):
                                                self.terminated_bytes = value
                                                self.terminated_bytes.value_namespace = name_space
                                                self.terminated_bytes.value_namespace_prefix = name_space_prefix
                                            if(value_path == "terminated-pkts"):
                                                self.terminated_pkts = value
                                                self.terminated_pkts.value_namespace = name_space
                                                self.terminated_pkts.value_namespace_prefix = name_space_prefix

                                    def has_data(self):
                                        return (
                                            self.type.is_set or
                                            (self.spi_si is not None and self.spi_si.has_data()) or
                                            (self.term is not None and self.term.has_data()))

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.type.yfilter != YFilter.not_set or
                                            (self.spi_si is not None and self.spi_si.has_operation()) or
                                            (self.term is not None and self.term.has_operation()))

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "data" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.type.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        if (child_yang_name == "spi-si"):
                                            if (self.spi_si is None):
                                                self.spi_si = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data.SpiSi()
                                                self.spi_si.parent = self
                                                self._children_name_map["spi_si"] = "spi-si"
                                            return self.spi_si

                                        if (child_yang_name == "term"):
                                            if (self.term is None):
                                                self.term = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data.Term()
                                                self.term.parent = self
                                                self._children_name_map["term"] = "term"
                                            return self.term

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "spi-si" or name == "term" or name == "type"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "type"):
                                            self.type = value
                                            self.type.value_namespace = name_space
                                            self.type.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    return (
                                        self.si.is_set or
                                        (self.data is not None and self.data.has_data()))

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.si.yfilter != YFilter.not_set or
                                        (self.data is not None and self.data.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "si-arr" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.si.is_set or self.si.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.si.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "data"):
                                        if (self.data is None):
                                            self.data = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data()
                                            self.data.parent = self
                                            self._children_name_map["data"] = "data"
                                        return self.data

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "data" or name == "si"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "si"):
                                        self.si = value
                                        self.si.value_namespace = name_space
                                        self.si.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                for c in self.si_arr:
                                    if (c.has_data()):
                                        return True
                                return (
                                    self.name.is_set or
                                    (self.data is not None and self.data.has_data()))

                            def has_operation(self):
                                for c in self.si_arr:
                                    if (c.has_operation()):
                                        return True
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.name.yfilter != YFilter.not_set or
                                    (self.data is not None and self.data.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "sff-name" + "[name='" + self.name.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.name.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "data"):
                                    if (self.data is None):
                                        self.data = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data()
                                        self.data.parent = self
                                        self._children_name_map["data"] = "data"
                                    return self.data

                                if (child_yang_name == "si-arr"):
                                    for c in self.si_arr:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.SiArr()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.si_arr.append(c)
                                    return c

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "data" or name == "si-arr" or name == "name"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "name"):
                                    self.name = value
                                    self.name.value_namespace = name_space
                                    self.name.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.sff_name:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.sff_name:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "sff-names" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "sff-name"):
                                for c in self.sff_name:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.sff_name.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "sff-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (
                            (self.local is not None and self.local.has_data()) or
                            (self.sff_names is not None and self.sff_names.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.local is not None and self.local.has_operation()) or
                            (self.sff_names is not None and self.sff_names.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "service-function-forwarder" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "local"):
                            if (self.local is None):
                                self.local = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local()
                                self.local.parent = self
                                self._children_name_map["local"] = "local"
                            return self.local

                        if (child_yang_name == "sff-names"):
                            if (self.sff_names is None):
                                self.sff_names = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames()
                                self.sff_names.parent = self
                                self._children_name_map["sff_names"] = "sff-names"
                            return self.sff_names

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "local" or name == "sff-names"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        (self.service_function is not None and self.service_function.has_data()) or
                        (self.service_function_forwarder is not None and self.service_function_forwarder.has_data()) or
                        (self.service_function_path is not None and self.service_function_path.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.service_function is not None and self.service_function.has_operation()) or
                        (self.service_function_forwarder is not None and self.service_function_forwarder.has_operation()) or
                        (self.service_function_path is not None and self.service_function_path.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "process" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "service-function"):
                        if (self.service_function is None):
                            self.service_function = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction()
                            self.service_function.parent = self
                            self._children_name_map["service_function"] = "service-function"
                        return self.service_function

                    if (child_yang_name == "service-function-forwarder"):
                        if (self.service_function_forwarder is None):
                            self.service_function_forwarder = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder()
                            self.service_function_forwarder.parent = self
                            self._children_name_map["service_function_forwarder"] = "service-function-forwarder"
                        return self.service_function_forwarder

                    if (child_yang_name == "service-function-path"):
                        if (self.service_function_path is None):
                            self.service_function_path = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath()
                            self.service_function_path.parent = self
                            self._children_name_map["service_function_path"] = "service-function-path"
                        return self.service_function_path

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "service-function" or name == "service-function-forwarder" or name == "service-function-path"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.node_name.is_set or
                    (self.process is not None and self.process.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.node_name.yfilter != YFilter.not_set or
                    (self.process is not None and self.process.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "node" + "[node-name='" + self.node_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-pbr-vservice-ea-oper:service-function-chaining/nodes/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.node_name.is_set or self.node_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.node_name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "process"):
                    if (self.process is None):
                        self.process = ServiceFunctionChaining.Nodes.Node.Process()
                        self.process.parent = self
                        self._children_name_map["process"] = "process"
                    return self.process

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "process" or name == "node-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "node-name"):
                    self.node_name = value
                    self.node_name.value_namespace = name_space
                    self.node_name.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.node:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.node:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "nodes" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-pbr-vservice-ea-oper:service-function-chaining/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "node"):
                for c in self.node:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = ServiceFunctionChaining.Nodes.Node()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.node.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "node"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.nodes is not None and self.nodes.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.nodes is not None and self.nodes.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-pbr-vservice-ea-oper:service-function-chaining" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "nodes"):
            if (self.nodes is None):
                self.nodes = ServiceFunctionChaining.Nodes()
                self.nodes.parent = self
                self._children_name_map["nodes"] = "nodes"
            return self.nodes

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "nodes"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = ServiceFunctionChaining()
        return self._top_entity

