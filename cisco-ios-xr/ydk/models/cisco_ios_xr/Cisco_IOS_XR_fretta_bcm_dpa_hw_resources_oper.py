""" Cisco_IOS_XR_fretta_bcm_dpa_hw_resources_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR fretta\-bcm\-dpa\-hw\-resources package operational data.

This module contains definitions
for the following management objects\:
  dpa\: Stats Data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Resource(Enum):
    """
    Resource

    Resource

    .. data:: lem = 0

    	lem

    .. data:: lpm = 1

    	lpm

    .. data:: encap = 2

    	encap

    .. data:: ext_tcam_ipv4 = 3

    	ext tcam ipv4

    .. data:: ext_tcam_ipv6 = 4

    	ext tcam ipv6

    .. data:: fec = 5

    	fec

    .. data:: ecmpfec = 6

    	ecmp fec

    """

    lem = Enum.YLeaf(0, "lem")

    lpm = Enum.YLeaf(1, "lpm")

    encap = Enum.YLeaf(2, "encap")

    ext_tcam_ipv4 = Enum.YLeaf(3, "ext-tcam-ipv4")

    ext_tcam_ipv6 = Enum.YLeaf(4, "ext-tcam-ipv6")

    fec = Enum.YLeaf(5, "fec")

    ecmpfec = Enum.YLeaf(6, "ecmpfec")



class Dpa(Entity):
    """
    Stats Data
    
    .. attribute:: stats
    
    	Voq or Trap Data
    	**type**\:   :py:class:`Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_hw_resources_oper.Dpa.Stats>`
    
    

    """

    _prefix = 'fretta-bcm-dpa-hw-resources-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Dpa, self).__init__()
        self._top_entity = None

        self.yang_name = "dpa"
        self.yang_parent_name = "Cisco-IOS-XR-fretta-bcm-dpa-hw-resources-oper"

        self.stats = Dpa.Stats()
        self.stats.parent = self
        self._children_name_map["stats"] = "stats"
        self._children_yang_names.add("stats")


    class Stats(Entity):
        """
        Voq or Trap Data
        
        .. attribute:: nodes
        
        	DPA data for available nodes
        	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_hw_resources_oper.Dpa.Stats.Nodes>`
        
        

        """

        _prefix = 'fretta-bcm-dpa-hw-resources-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Dpa.Stats, self).__init__()

            self.yang_name = "stats"
            self.yang_parent_name = "dpa"

            self.nodes = Dpa.Stats.Nodes()
            self.nodes.parent = self
            self._children_name_map["nodes"] = "nodes"
            self._children_yang_names.add("nodes")


        class Nodes(Entity):
            """
            DPA data for available nodes
            
            .. attribute:: node
            
            	DPA operational data for a particular node
            	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_hw_resources_oper.Dpa.Stats.Nodes.Node>`
            
            

            """

            _prefix = 'fretta-bcm-dpa-hw-resources-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Dpa.Stats.Nodes, self).__init__()

                self.yang_name = "nodes"
                self.yang_parent_name = "stats"

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
                            super(Dpa.Stats.Nodes, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Dpa.Stats.Nodes, self).__setattr__(name, value)


            class Node(Entity):
                """
                DPA operational data for a particular node
                
                .. attribute:: node_name  <key>
                
                	Node ID
                	**type**\:  str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                .. attribute:: asic_statistics
                
                	ASIC statistics table
                	**type**\:   :py:class:`AsicStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_hw_resources_oper.Dpa.Stats.Nodes.Node.AsicStatistics>`
                
                .. attribute:: hw_resources_datas
                
                	DPA hw resources stats 
                	**type**\:   :py:class:`HwResourcesDatas <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_hw_resources_oper.Dpa.Stats.Nodes.Node.HwResourcesDatas>`
                
                .. attribute:: npu_ids
                
                	DPA stats hw resources info 
                	**type**\:   :py:class:`NpuIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_hw_resources_oper.Dpa.Stats.Nodes.Node.NpuIds>`
                
                .. attribute:: npu_numbers
                
                	Ingress Stats
                	**type**\:   :py:class:`NpuNumbers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_hw_resources_oper.Dpa.Stats.Nodes.Node.NpuNumbers>`
                
                

                """

                _prefix = 'fretta-bcm-dpa-hw-resources-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Dpa.Stats.Nodes.Node, self).__init__()

                    self.yang_name = "node"
                    self.yang_parent_name = "nodes"

                    self.node_name = YLeaf(YType.str, "node-name")

                    self.asic_statistics = Dpa.Stats.Nodes.Node.AsicStatistics()
                    self.asic_statistics.parent = self
                    self._children_name_map["asic_statistics"] = "asic-statistics"
                    self._children_yang_names.add("asic-statistics")

                    self.hw_resources_datas = Dpa.Stats.Nodes.Node.HwResourcesDatas()
                    self.hw_resources_datas.parent = self
                    self._children_name_map["hw_resources_datas"] = "hw-resources-datas"
                    self._children_yang_names.add("hw-resources-datas")

                    self.npu_ids = Dpa.Stats.Nodes.Node.NpuIds()
                    self.npu_ids.parent = self
                    self._children_name_map["npu_ids"] = "npu-ids"
                    self._children_yang_names.add("npu-ids")

                    self.npu_numbers = Dpa.Stats.Nodes.Node.NpuNumbers()
                    self.npu_numbers.parent = self
                    self._children_name_map["npu_numbers"] = "npu-numbers"
                    self._children_yang_names.add("npu-numbers")

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
                                super(Dpa.Stats.Nodes.Node, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Dpa.Stats.Nodes.Node, self).__setattr__(name, value)


                class HwResourcesDatas(Entity):
                    """
                    DPA hw resources stats 
                    
                    .. attribute:: hw_resources_data
                    
                    	Hardware resources table
                    	**type**\: list of    :py:class:`HwResourcesData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_hw_resources_oper.Dpa.Stats.Nodes.Node.HwResourcesDatas.HwResourcesData>`
                    
                    

                    """

                    _prefix = 'fretta-bcm-dpa-hw-resources-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Dpa.Stats.Nodes.Node.HwResourcesDatas, self).__init__()

                        self.yang_name = "hw-resources-datas"
                        self.yang_parent_name = "node"

                        self.hw_resources_data = YList(self)

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
                                    super(Dpa.Stats.Nodes.Node.HwResourcesDatas, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Dpa.Stats.Nodes.Node.HwResourcesDatas, self).__setattr__(name, value)


                    class HwResourcesData(Entity):
                        """
                        Hardware resources table
                        
                        .. attribute:: resource  <key>
                        
                        	Resource type
                        	**type**\:   :py:class:`Resource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_hw_resources_oper.Resource>`
                        
                        .. attribute:: name
                        
                        	name
                        	**type**\:  str
                        
                        .. attribute:: npu_hwr
                        
                        	npu hwr
                        	**type**\: list of    :py:class:`NpuHwr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_hw_resources_oper.Dpa.Stats.Nodes.Node.HwResourcesDatas.HwResourcesData.NpuHwr>`
                        
                        .. attribute:: num_npus
                        
                        	num npus
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: resource_id
                        
                        	resource id
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'fretta-bcm-dpa-hw-resources-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Dpa.Stats.Nodes.Node.HwResourcesDatas.HwResourcesData, self).__init__()

                            self.yang_name = "hw-resources-data"
                            self.yang_parent_name = "hw-resources-datas"

                            self.resource = YLeaf(YType.enumeration, "resource")

                            self.name = YLeaf(YType.str, "name")

                            self.num_npus = YLeaf(YType.uint32, "num-npus")

                            self.resource_id = YLeaf(YType.uint32, "resource-id")

                            self.npu_hwr = YList(self)

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("resource",
                                            "name",
                                            "num_npus",
                                            "resource_id") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Dpa.Stats.Nodes.Node.HwResourcesDatas.HwResourcesData, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Dpa.Stats.Nodes.Node.HwResourcesDatas.HwResourcesData, self).__setattr__(name, value)


                        class NpuHwr(Entity):
                            """
                            npu hwr
                            
                            .. attribute:: inuse_objects
                            
                            	inuse objects
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: lt_hwr
                            
                            	lt hwr
                            	**type**\: list of    :py:class:`LtHwr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_hw_resources_oper.Dpa.Stats.Nodes.Node.HwResourcesDatas.HwResourcesData.NpuHwr.LtHwr>`
                            
                            .. attribute:: max_allowed
                            
                            	max allowed
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: max_entries
                            
                            	max entries
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: npu_id
                            
                            	npu id
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: num_lt
                            
                            	num lt
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: oor_change_count
                            
                            	oor change count
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: oor_state
                            
                            	oor state
                            	**type**\:  str
                            
                            .. attribute:: oor_state_change_time1
                            
                            	oor state change time1
                            	**type**\:  str
                            
                            .. attribute:: oor_state_change_time2
                            
                            	oor state change time2
                            	**type**\:  str
                            
                            .. attribute:: red_oor_threshold
                            
                            	red oor threshold
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: red_oor_threshold_percent
                            
                            	red oor threshold percent
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: yellow_oor_threshold
                            
                            	yellow oor threshold
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: yellow_oor_threshold_percent
                            
                            	yellow oor threshold percent
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'fretta-bcm-dpa-hw-resources-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dpa.Stats.Nodes.Node.HwResourcesDatas.HwResourcesData.NpuHwr, self).__init__()

                                self.yang_name = "npu-hwr"
                                self.yang_parent_name = "hw-resources-data"

                                self.inuse_objects = YLeaf(YType.uint32, "inuse-objects")

                                self.max_allowed = YLeaf(YType.uint32, "max-allowed")

                                self.max_entries = YLeaf(YType.uint32, "max-entries")

                                self.npu_id = YLeaf(YType.uint32, "npu-id")

                                self.num_lt = YLeaf(YType.uint32, "num-lt")

                                self.oor_change_count = YLeaf(YType.uint32, "oor-change-count")

                                self.oor_state = YLeaf(YType.str, "oor-state")

                                self.oor_state_change_time1 = YLeaf(YType.str, "oor-state-change-time1")

                                self.oor_state_change_time2 = YLeaf(YType.str, "oor-state-change-time2")

                                self.red_oor_threshold = YLeaf(YType.uint32, "red-oor-threshold")

                                self.red_oor_threshold_percent = YLeaf(YType.uint32, "red-oor-threshold-percent")

                                self.yellow_oor_threshold = YLeaf(YType.uint32, "yellow-oor-threshold")

                                self.yellow_oor_threshold_percent = YLeaf(YType.uint32, "yellow-oor-threshold-percent")

                                self.lt_hwr = YList(self)

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("inuse_objects",
                                                "max_allowed",
                                                "max_entries",
                                                "npu_id",
                                                "num_lt",
                                                "oor_change_count",
                                                "oor_state",
                                                "oor_state_change_time1",
                                                "oor_state_change_time2",
                                                "red_oor_threshold",
                                                "red_oor_threshold_percent",
                                                "yellow_oor_threshold",
                                                "yellow_oor_threshold_percent") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Dpa.Stats.Nodes.Node.HwResourcesDatas.HwResourcesData.NpuHwr, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Dpa.Stats.Nodes.Node.HwResourcesDatas.HwResourcesData.NpuHwr, self).__setattr__(name, value)


                            class LtHwr(Entity):
                                """
                                lt hwr
                                
                                .. attribute:: hw_entries
                                
                                	hw entries
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lt_id
                                
                                	lt id
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: name
                                
                                	name
                                	**type**\:  str
                                
                                .. attribute:: sw_entries
                                
                                	sw entries
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'fretta-bcm-dpa-hw-resources-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dpa.Stats.Nodes.Node.HwResourcesDatas.HwResourcesData.NpuHwr.LtHwr, self).__init__()

                                    self.yang_name = "lt-hwr"
                                    self.yang_parent_name = "npu-hwr"

                                    self.hw_entries = YLeaf(YType.uint32, "hw-entries")

                                    self.lt_id = YLeaf(YType.uint32, "lt-id")

                                    self.name = YLeaf(YType.str, "name")

                                    self.sw_entries = YLeaf(YType.uint32, "sw-entries")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("hw_entries",
                                                    "lt_id",
                                                    "name",
                                                    "sw_entries") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Dpa.Stats.Nodes.Node.HwResourcesDatas.HwResourcesData.NpuHwr.LtHwr, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Dpa.Stats.Nodes.Node.HwResourcesDatas.HwResourcesData.NpuHwr.LtHwr, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.hw_entries.is_set or
                                        self.lt_id.is_set or
                                        self.name.is_set or
                                        self.sw_entries.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.hw_entries.yfilter != YFilter.not_set or
                                        self.lt_id.yfilter != YFilter.not_set or
                                        self.name.yfilter != YFilter.not_set or
                                        self.sw_entries.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "lt-hwr" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.hw_entries.is_set or self.hw_entries.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.hw_entries.get_name_leafdata())
                                    if (self.lt_id.is_set or self.lt_id.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.lt_id.get_name_leafdata())
                                    if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.name.get_name_leafdata())
                                    if (self.sw_entries.is_set or self.sw_entries.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.sw_entries.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "hw-entries" or name == "lt-id" or name == "name" or name == "sw-entries"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "hw-entries"):
                                        self.hw_entries = value
                                        self.hw_entries.value_namespace = name_space
                                        self.hw_entries.value_namespace_prefix = name_space_prefix
                                    if(value_path == "lt-id"):
                                        self.lt_id = value
                                        self.lt_id.value_namespace = name_space
                                        self.lt_id.value_namespace_prefix = name_space_prefix
                                    if(value_path == "name"):
                                        self.name = value
                                        self.name.value_namespace = name_space
                                        self.name.value_namespace_prefix = name_space_prefix
                                    if(value_path == "sw-entries"):
                                        self.sw_entries = value
                                        self.sw_entries.value_namespace = name_space
                                        self.sw_entries.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                for c in self.lt_hwr:
                                    if (c.has_data()):
                                        return True
                                return (
                                    self.inuse_objects.is_set or
                                    self.max_allowed.is_set or
                                    self.max_entries.is_set or
                                    self.npu_id.is_set or
                                    self.num_lt.is_set or
                                    self.oor_change_count.is_set or
                                    self.oor_state.is_set or
                                    self.oor_state_change_time1.is_set or
                                    self.oor_state_change_time2.is_set or
                                    self.red_oor_threshold.is_set or
                                    self.red_oor_threshold_percent.is_set or
                                    self.yellow_oor_threshold.is_set or
                                    self.yellow_oor_threshold_percent.is_set)

                            def has_operation(self):
                                for c in self.lt_hwr:
                                    if (c.has_operation()):
                                        return True
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.inuse_objects.yfilter != YFilter.not_set or
                                    self.max_allowed.yfilter != YFilter.not_set or
                                    self.max_entries.yfilter != YFilter.not_set or
                                    self.npu_id.yfilter != YFilter.not_set or
                                    self.num_lt.yfilter != YFilter.not_set or
                                    self.oor_change_count.yfilter != YFilter.not_set or
                                    self.oor_state.yfilter != YFilter.not_set or
                                    self.oor_state_change_time1.yfilter != YFilter.not_set or
                                    self.oor_state_change_time2.yfilter != YFilter.not_set or
                                    self.red_oor_threshold.yfilter != YFilter.not_set or
                                    self.red_oor_threshold_percent.yfilter != YFilter.not_set or
                                    self.yellow_oor_threshold.yfilter != YFilter.not_set or
                                    self.yellow_oor_threshold_percent.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "npu-hwr" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.inuse_objects.is_set or self.inuse_objects.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.inuse_objects.get_name_leafdata())
                                if (self.max_allowed.is_set or self.max_allowed.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.max_allowed.get_name_leafdata())
                                if (self.max_entries.is_set or self.max_entries.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.max_entries.get_name_leafdata())
                                if (self.npu_id.is_set or self.npu_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.npu_id.get_name_leafdata())
                                if (self.num_lt.is_set or self.num_lt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.num_lt.get_name_leafdata())
                                if (self.oor_change_count.is_set or self.oor_change_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.oor_change_count.get_name_leafdata())
                                if (self.oor_state.is_set or self.oor_state.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.oor_state.get_name_leafdata())
                                if (self.oor_state_change_time1.is_set or self.oor_state_change_time1.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.oor_state_change_time1.get_name_leafdata())
                                if (self.oor_state_change_time2.is_set or self.oor_state_change_time2.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.oor_state_change_time2.get_name_leafdata())
                                if (self.red_oor_threshold.is_set or self.red_oor_threshold.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.red_oor_threshold.get_name_leafdata())
                                if (self.red_oor_threshold_percent.is_set or self.red_oor_threshold_percent.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.red_oor_threshold_percent.get_name_leafdata())
                                if (self.yellow_oor_threshold.is_set or self.yellow_oor_threshold.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.yellow_oor_threshold.get_name_leafdata())
                                if (self.yellow_oor_threshold_percent.is_set or self.yellow_oor_threshold_percent.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.yellow_oor_threshold_percent.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "lt-hwr"):
                                    for c in self.lt_hwr:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = Dpa.Stats.Nodes.Node.HwResourcesDatas.HwResourcesData.NpuHwr.LtHwr()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.lt_hwr.append(c)
                                    return c

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "lt-hwr" or name == "inuse-objects" or name == "max-allowed" or name == "max-entries" or name == "npu-id" or name == "num-lt" or name == "oor-change-count" or name == "oor-state" or name == "oor-state-change-time1" or name == "oor-state-change-time2" or name == "red-oor-threshold" or name == "red-oor-threshold-percent" or name == "yellow-oor-threshold" or name == "yellow-oor-threshold-percent"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "inuse-objects"):
                                    self.inuse_objects = value
                                    self.inuse_objects.value_namespace = name_space
                                    self.inuse_objects.value_namespace_prefix = name_space_prefix
                                if(value_path == "max-allowed"):
                                    self.max_allowed = value
                                    self.max_allowed.value_namespace = name_space
                                    self.max_allowed.value_namespace_prefix = name_space_prefix
                                if(value_path == "max-entries"):
                                    self.max_entries = value
                                    self.max_entries.value_namespace = name_space
                                    self.max_entries.value_namespace_prefix = name_space_prefix
                                if(value_path == "npu-id"):
                                    self.npu_id = value
                                    self.npu_id.value_namespace = name_space
                                    self.npu_id.value_namespace_prefix = name_space_prefix
                                if(value_path == "num-lt"):
                                    self.num_lt = value
                                    self.num_lt.value_namespace = name_space
                                    self.num_lt.value_namespace_prefix = name_space_prefix
                                if(value_path == "oor-change-count"):
                                    self.oor_change_count = value
                                    self.oor_change_count.value_namespace = name_space
                                    self.oor_change_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "oor-state"):
                                    self.oor_state = value
                                    self.oor_state.value_namespace = name_space
                                    self.oor_state.value_namespace_prefix = name_space_prefix
                                if(value_path == "oor-state-change-time1"):
                                    self.oor_state_change_time1 = value
                                    self.oor_state_change_time1.value_namespace = name_space
                                    self.oor_state_change_time1.value_namespace_prefix = name_space_prefix
                                if(value_path == "oor-state-change-time2"):
                                    self.oor_state_change_time2 = value
                                    self.oor_state_change_time2.value_namespace = name_space
                                    self.oor_state_change_time2.value_namespace_prefix = name_space_prefix
                                if(value_path == "red-oor-threshold"):
                                    self.red_oor_threshold = value
                                    self.red_oor_threshold.value_namespace = name_space
                                    self.red_oor_threshold.value_namespace_prefix = name_space_prefix
                                if(value_path == "red-oor-threshold-percent"):
                                    self.red_oor_threshold_percent = value
                                    self.red_oor_threshold_percent.value_namespace = name_space
                                    self.red_oor_threshold_percent.value_namespace_prefix = name_space_prefix
                                if(value_path == "yellow-oor-threshold"):
                                    self.yellow_oor_threshold = value
                                    self.yellow_oor_threshold.value_namespace = name_space
                                    self.yellow_oor_threshold.value_namespace_prefix = name_space_prefix
                                if(value_path == "yellow-oor-threshold-percent"):
                                    self.yellow_oor_threshold_percent = value
                                    self.yellow_oor_threshold_percent.value_namespace = name_space
                                    self.yellow_oor_threshold_percent.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.npu_hwr:
                                if (c.has_data()):
                                    return True
                            return (
                                self.resource.is_set or
                                self.name.is_set or
                                self.num_npus.is_set or
                                self.resource_id.is_set)

                        def has_operation(self):
                            for c in self.npu_hwr:
                                if (c.has_operation()):
                                    return True
                            return (
                                self.yfilter != YFilter.not_set or
                                self.resource.yfilter != YFilter.not_set or
                                self.name.yfilter != YFilter.not_set or
                                self.num_npus.yfilter != YFilter.not_set or
                                self.resource_id.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "hw-resources-data" + "[resource='" + self.resource.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.resource.is_set or self.resource.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.resource.get_name_leafdata())
                            if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.name.get_name_leafdata())
                            if (self.num_npus.is_set or self.num_npus.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.num_npus.get_name_leafdata())
                            if (self.resource_id.is_set or self.resource_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.resource_id.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "npu-hwr"):
                                for c in self.npu_hwr:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Dpa.Stats.Nodes.Node.HwResourcesDatas.HwResourcesData.NpuHwr()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.npu_hwr.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "npu-hwr" or name == "resource" or name == "name" or name == "num-npus" or name == "resource-id"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "resource"):
                                self.resource = value
                                self.resource.value_namespace = name_space
                                self.resource.value_namespace_prefix = name_space_prefix
                            if(value_path == "name"):
                                self.name = value
                                self.name.value_namespace = name_space
                                self.name.value_namespace_prefix = name_space_prefix
                            if(value_path == "num-npus"):
                                self.num_npus = value
                                self.num_npus.value_namespace = name_space
                                self.num_npus.value_namespace_prefix = name_space_prefix
                            if(value_path == "resource-id"):
                                self.resource_id = value
                                self.resource_id.value_namespace = name_space
                                self.resource_id.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.hw_resources_data:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.hw_resources_data:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "hw-resources-datas" + path_buffer

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

                        if (child_yang_name == "hw-resources-data"):
                            for c in self.hw_resources_data:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Dpa.Stats.Nodes.Node.HwResourcesDatas.HwResourcesData()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.hw_resources_data.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "hw-resources-data"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class AsicStatistics(Entity):
                    """
                    ASIC statistics table
                    
                    .. attribute:: asic_statistics_detail_for_npu_ids
                    
                    	Detailed ASIC statistics
                    	**type**\:   :py:class:`AsicStatisticsDetailForNpuIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_hw_resources_oper.Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds>`
                    
                    .. attribute:: asic_statistics_for_npu_ids
                    
                    	ASIC statistics
                    	**type**\:   :py:class:`AsicStatisticsForNpuIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_hw_resources_oper.Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsForNpuIds>`
                    
                    

                    """

                    _prefix = 'fretta-bcm-dpa-hw-resources-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Dpa.Stats.Nodes.Node.AsicStatistics, self).__init__()

                        self.yang_name = "asic-statistics"
                        self.yang_parent_name = "node"

                        self.asic_statistics_detail_for_npu_ids = Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds()
                        self.asic_statistics_detail_for_npu_ids.parent = self
                        self._children_name_map["asic_statistics_detail_for_npu_ids"] = "asic-statistics-detail-for-npu-ids"
                        self._children_yang_names.add("asic-statistics-detail-for-npu-ids")

                        self.asic_statistics_for_npu_ids = Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsForNpuIds()
                        self.asic_statistics_for_npu_ids.parent = self
                        self._children_name_map["asic_statistics_for_npu_ids"] = "asic-statistics-for-npu-ids"
                        self._children_yang_names.add("asic-statistics-for-npu-ids")


                    class AsicStatisticsForNpuIds(Entity):
                        """
                        ASIC statistics
                        
                        .. attribute:: asic_statistics_for_npu_id
                        
                        	ASIC statistics for a particular NPU
                        	**type**\: list of    :py:class:`AsicStatisticsForNpuId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_hw_resources_oper.Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsForNpuIds.AsicStatisticsForNpuId>`
                        
                        

                        """

                        _prefix = 'fretta-bcm-dpa-hw-resources-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsForNpuIds, self).__init__()

                            self.yang_name = "asic-statistics-for-npu-ids"
                            self.yang_parent_name = "asic-statistics"

                            self.asic_statistics_for_npu_id = YList(self)

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
                                        super(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsForNpuIds, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsForNpuIds, self).__setattr__(name, value)


                        class AsicStatisticsForNpuId(Entity):
                            """
                            ASIC statistics for a particular NPU
                            
                            .. attribute:: npu_id  <key>
                            
                            	NPU number
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: asic_instance
                            
                            	ASIC instance
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: chip_version
                            
                            	Chip version
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: rack_number
                            
                            	Rack number
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: slot_number
                            
                            	Slot number
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: statistics
                            
                            	Statistics
                            	**type**\:   :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_hw_resources_oper.Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsForNpuIds.AsicStatisticsForNpuId.Statistics>`
                            
                            .. attribute:: valid
                            
                            	Flag to indicate if data is valid
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'fretta-bcm-dpa-hw-resources-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsForNpuIds.AsicStatisticsForNpuId, self).__init__()

                                self.yang_name = "asic-statistics-for-npu-id"
                                self.yang_parent_name = "asic-statistics-for-npu-ids"

                                self.npu_id = YLeaf(YType.int32, "npu-id")

                                self.asic_instance = YLeaf(YType.uint32, "asic-instance")

                                self.chip_version = YLeaf(YType.uint16, "chip-version")

                                self.rack_number = YLeaf(YType.uint32, "rack-number")

                                self.slot_number = YLeaf(YType.uint32, "slot-number")

                                self.valid = YLeaf(YType.boolean, "valid")

                                self.statistics = Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsForNpuIds.AsicStatisticsForNpuId.Statistics()
                                self.statistics.parent = self
                                self._children_name_map["statistics"] = "statistics"
                                self._children_yang_names.add("statistics")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("npu_id",
                                                "asic_instance",
                                                "chip_version",
                                                "rack_number",
                                                "slot_number",
                                                "valid") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsForNpuIds.AsicStatisticsForNpuId, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsForNpuIds.AsicStatisticsForNpuId, self).__setattr__(name, value)


                            class Statistics(Entity):
                                """
                                Statistics
                                
                                .. attribute:: egq_deleted_pkt_cnt
                                
                                	EHP2PQP discarded packet counter
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: egq_ehp_mc_high_discard_cnt
                                
                                	Number of multicast high packets discarded because multicast FIFO is full
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: egq_ehp_mc_high_pkt_cnt
                                
                                	EHP2PQP multicast high packet counter
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: egq_ehp_mc_low_discard_cnt
                                
                                	Number of multicast low packets discarded because multicast FIFO is full
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: egq_ehp_mc_low_pkt_cnt
                                
                                	EHP2PQP multicast low packet counter
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: egq_ehp_uc_pkt_cnt
                                
                                	EHP2PQP unicast packet counter
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: egq_erpp_lag_pruning_discard_cnt
                                
                                	Number of packet descriptors discarded due to LAG multicast pruning
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: egq_erpp_pmf_discard_cnt
                                
                                	Number of packet descriptors discarded due to ERPP PMF
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: egq_erpp_vlan_mbr_discard_cnt
                                
                                	Number of packet descriptors discarded because of egress VLAN membership
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: egq_fqp_pkt_cnt
                                
                                	FQP2EPE packet counter
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: egq_pqp_discard_mc_pkt_cnt
                                
                                	PQP discarded multicast packet counter
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: egq_pqp_discard_uc_pkt_cnt
                                
                                	PQP discarded unicast packet counter
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: egq_pqp_mc_bytes_cnt
                                
                                	PQP2FQP multicast bytes counter
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**units**\: byte
                                
                                .. attribute:: egq_pqp_mc_pkt_cnt
                                
                                	PQP2FQP multicast packet counter
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: egq_pqp_uc_bytes_cnt
                                
                                	PQP2FQP unicast bytes counter
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**units**\: byte
                                
                                .. attribute:: egq_pqp_uc_pkt_cnt
                                
                                	PQP2FQP unicast packet counter
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: epni_epe_byte_cnt
                                
                                	EPE2PNI bytes counter
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**units**\: byte
                                
                                .. attribute:: epni_epe_discard_cnt
                                
                                	EPE discarded packet counter
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: epni_epe_pkt_cnt
                                
                                	EPE2PNI packet counter
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: fda_cells_in_cnt_p1
                                
                                	FDA input cell counter P1
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: fda_cells_in_cnt_p2
                                
                                	FDA input cell counter P2
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: fda_cells_in_cnt_p3
                                
                                	FDA input cell counter P3
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: fda_cells_in_ipt_cnt
                                
                                	FDA input cell counter IPT
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: fda_cells_in_meshmc_cnt
                                
                                	FDA input cell counter MESHMC
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: fda_cells_in_tdm_cnt
                                
                                	FDA input cell counter TDM
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: fda_cells_out_cnt_p1
                                
                                	FDA output cell counter P1
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: fda_cells_out_cnt_p2
                                
                                	FDA output cell counter P2
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: fda_cells_out_cnt_p3
                                
                                	FDA output cell counter P3
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: fda_cells_out_ipt_cnt
                                
                                	FDA output cell counter IPT
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: fda_cells_out_meshmc_cnt
                                
                                	FDA output cell counter MESHMC
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: fda_cells_out_tdm_cnt
                                
                                	FDA output cell counter TDM
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: fda_egq_drop_cnt
                                
                                	FDA EGQ drop counter
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: fda_egq_meshmc_drop_cnt
                                
                                	FDA EGQ MESHMC drop counter
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: fdr_cell_in_cnt_total
                                
                                	FDR total incoming cell counter
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: fdr_p1_cell_in_cnt
                                
                                	FDR total incoming cell counter at pipe 1
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: fdr_p2_cell_in_cnt
                                
                                	FDR total incoming cell counter at pipe 2
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: fdr_p3_cell_in_cnt
                                
                                	FDR total incoming cell counter at pipe 3
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: fdt_ipt_desc_cell_cnt
                                
                                	Descriptor cell counter
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: fdt_ire_desc_cell_cnt
                                
                                	IRE internal descriptor cell counter
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: fdt_transmitted_data_cells_cnt
                                
                                	Counts all transmitted data cells
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: idr_mmu_if_cnt
                                
                                	Performance counter of the MMU interface
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: idr_ocb_if_cnt
                                
                                	Performance counter of the OCB interface
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: ipt_cfg_byte_cnt
                                
                                	Configurable bytes counter
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**units**\: byte
                                
                                .. attribute:: ipt_cfg_event_cnt
                                
                                	Configurable event counter
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: ipt_egq_pkt_cnt
                                
                                	EGQ packet counter
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: ipt_enq_pkt_cnt
                                
                                	ENQ packet counter
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: ipt_fdt_pkt_cnt
                                
                                	FDT packet counter
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: iqm_deleted_pkt_cnt
                                
                                	Counts matched packets discarded in the DEQ process
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: iqm_dequeue_pkt_cnt
                                
                                	Counts dequeued packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: iqm_enq_discarded_pkt_cnt
                                
                                	Counts all packets discarded at the ENQ pipe
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: iqm_enqueue_pkt_cnt
                                
                                	Counts enqueued packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: ire_cpu_pkt_cnt
                                
                                	CPU ingress received packet counter
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: ire_fdt_if_cnt
                                
                                	Performance counter of the FDT interface
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: ire_nif_pkt_cnt
                                
                                	NIF received packet counter
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: ire_oamp_pkt_cnt
                                
                                	OAMP ingress received packet counter
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: ire_olp_pkt_cnt
                                
                                	OLP ingress received packet counter
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: ire_rcy_pkt_cnt
                                
                                	Recycling ingress received packet counter
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: nbi_rx_total_byte_cnt
                                
                                	Total bytes sent from NIF to IRE
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**units**\: byte
                                
                                .. attribute:: nbi_rx_total_pkt_cnt
                                
                                	Total packets sent from NIF to IRE
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: nbi_tx_total_byte_cnt
                                
                                	Total bytes sent from EGQ to NIF
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**units**\: byte
                                
                                .. attribute:: nbi_tx_total_pkt_cnt
                                
                                	Total packets sent from EGQ to NIF
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'fretta-bcm-dpa-hw-resources-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsForNpuIds.AsicStatisticsForNpuId.Statistics, self).__init__()

                                    self.yang_name = "statistics"
                                    self.yang_parent_name = "asic-statistics-for-npu-id"

                                    self.egq_deleted_pkt_cnt = YLeaf(YType.uint64, "egq-deleted-pkt-cnt")

                                    self.egq_ehp_mc_high_discard_cnt = YLeaf(YType.uint64, "egq-ehp-mc-high-discard-cnt")

                                    self.egq_ehp_mc_high_pkt_cnt = YLeaf(YType.uint64, "egq-ehp-mc-high-pkt-cnt")

                                    self.egq_ehp_mc_low_discard_cnt = YLeaf(YType.uint64, "egq-ehp-mc-low-discard-cnt")

                                    self.egq_ehp_mc_low_pkt_cnt = YLeaf(YType.uint64, "egq-ehp-mc-low-pkt-cnt")

                                    self.egq_ehp_uc_pkt_cnt = YLeaf(YType.uint64, "egq-ehp-uc-pkt-cnt")

                                    self.egq_erpp_lag_pruning_discard_cnt = YLeaf(YType.uint64, "egq-erpp-lag-pruning-discard-cnt")

                                    self.egq_erpp_pmf_discard_cnt = YLeaf(YType.uint64, "egq-erpp-pmf-discard-cnt")

                                    self.egq_erpp_vlan_mbr_discard_cnt = YLeaf(YType.uint64, "egq-erpp-vlan-mbr-discard-cnt")

                                    self.egq_fqp_pkt_cnt = YLeaf(YType.uint64, "egq-fqp-pkt-cnt")

                                    self.egq_pqp_discard_mc_pkt_cnt = YLeaf(YType.uint64, "egq-pqp-discard-mc-pkt-cnt")

                                    self.egq_pqp_discard_uc_pkt_cnt = YLeaf(YType.uint64, "egq-pqp-discard-uc-pkt-cnt")

                                    self.egq_pqp_mc_bytes_cnt = YLeaf(YType.uint64, "egq-pqp-mc-bytes-cnt")

                                    self.egq_pqp_mc_pkt_cnt = YLeaf(YType.uint64, "egq-pqp-mc-pkt-cnt")

                                    self.egq_pqp_uc_bytes_cnt = YLeaf(YType.uint64, "egq-pqp-uc-bytes-cnt")

                                    self.egq_pqp_uc_pkt_cnt = YLeaf(YType.uint64, "egq-pqp-uc-pkt-cnt")

                                    self.epni_epe_byte_cnt = YLeaf(YType.uint64, "epni-epe-byte-cnt")

                                    self.epni_epe_discard_cnt = YLeaf(YType.uint64, "epni-epe-discard-cnt")

                                    self.epni_epe_pkt_cnt = YLeaf(YType.uint64, "epni-epe-pkt-cnt")

                                    self.fda_cells_in_cnt_p1 = YLeaf(YType.uint64, "fda-cells-in-cnt-p1")

                                    self.fda_cells_in_cnt_p2 = YLeaf(YType.uint64, "fda-cells-in-cnt-p2")

                                    self.fda_cells_in_cnt_p3 = YLeaf(YType.uint64, "fda-cells-in-cnt-p3")

                                    self.fda_cells_in_ipt_cnt = YLeaf(YType.uint64, "fda-cells-in-ipt-cnt")

                                    self.fda_cells_in_meshmc_cnt = YLeaf(YType.uint64, "fda-cells-in-meshmc-cnt")

                                    self.fda_cells_in_tdm_cnt = YLeaf(YType.uint64, "fda-cells-in-tdm-cnt")

                                    self.fda_cells_out_cnt_p1 = YLeaf(YType.uint64, "fda-cells-out-cnt-p1")

                                    self.fda_cells_out_cnt_p2 = YLeaf(YType.uint64, "fda-cells-out-cnt-p2")

                                    self.fda_cells_out_cnt_p3 = YLeaf(YType.uint64, "fda-cells-out-cnt-p3")

                                    self.fda_cells_out_ipt_cnt = YLeaf(YType.uint64, "fda-cells-out-ipt-cnt")

                                    self.fda_cells_out_meshmc_cnt = YLeaf(YType.uint64, "fda-cells-out-meshmc-cnt")

                                    self.fda_cells_out_tdm_cnt = YLeaf(YType.uint64, "fda-cells-out-tdm-cnt")

                                    self.fda_egq_drop_cnt = YLeaf(YType.uint64, "fda-egq-drop-cnt")

                                    self.fda_egq_meshmc_drop_cnt = YLeaf(YType.uint64, "fda-egq-meshmc-drop-cnt")

                                    self.fdr_cell_in_cnt_total = YLeaf(YType.uint64, "fdr-cell-in-cnt-total")

                                    self.fdr_p1_cell_in_cnt = YLeaf(YType.uint64, "fdr-p1-cell-in-cnt")

                                    self.fdr_p2_cell_in_cnt = YLeaf(YType.uint64, "fdr-p2-cell-in-cnt")

                                    self.fdr_p3_cell_in_cnt = YLeaf(YType.uint64, "fdr-p3-cell-in-cnt")

                                    self.fdt_ipt_desc_cell_cnt = YLeaf(YType.uint64, "fdt-ipt-desc-cell-cnt")

                                    self.fdt_ire_desc_cell_cnt = YLeaf(YType.uint64, "fdt-ire-desc-cell-cnt")

                                    self.fdt_transmitted_data_cells_cnt = YLeaf(YType.uint64, "fdt-transmitted-data-cells-cnt")

                                    self.idr_mmu_if_cnt = YLeaf(YType.uint64, "idr-mmu-if-cnt")

                                    self.idr_ocb_if_cnt = YLeaf(YType.uint64, "idr-ocb-if-cnt")

                                    self.ipt_cfg_byte_cnt = YLeaf(YType.uint64, "ipt-cfg-byte-cnt")

                                    self.ipt_cfg_event_cnt = YLeaf(YType.uint64, "ipt-cfg-event-cnt")

                                    self.ipt_egq_pkt_cnt = YLeaf(YType.uint64, "ipt-egq-pkt-cnt")

                                    self.ipt_enq_pkt_cnt = YLeaf(YType.uint64, "ipt-enq-pkt-cnt")

                                    self.ipt_fdt_pkt_cnt = YLeaf(YType.uint64, "ipt-fdt-pkt-cnt")

                                    self.iqm_deleted_pkt_cnt = YLeaf(YType.uint64, "iqm-deleted-pkt-cnt")

                                    self.iqm_dequeue_pkt_cnt = YLeaf(YType.uint64, "iqm-dequeue-pkt-cnt")

                                    self.iqm_enq_discarded_pkt_cnt = YLeaf(YType.uint64, "iqm-enq-discarded-pkt-cnt")

                                    self.iqm_enqueue_pkt_cnt = YLeaf(YType.uint64, "iqm-enqueue-pkt-cnt")

                                    self.ire_cpu_pkt_cnt = YLeaf(YType.uint64, "ire-cpu-pkt-cnt")

                                    self.ire_fdt_if_cnt = YLeaf(YType.uint64, "ire-fdt-if-cnt")

                                    self.ire_nif_pkt_cnt = YLeaf(YType.uint64, "ire-nif-pkt-cnt")

                                    self.ire_oamp_pkt_cnt = YLeaf(YType.uint64, "ire-oamp-pkt-cnt")

                                    self.ire_olp_pkt_cnt = YLeaf(YType.uint64, "ire-olp-pkt-cnt")

                                    self.ire_rcy_pkt_cnt = YLeaf(YType.uint64, "ire-rcy-pkt-cnt")

                                    self.nbi_rx_total_byte_cnt = YLeaf(YType.uint64, "nbi-rx-total-byte-cnt")

                                    self.nbi_rx_total_pkt_cnt = YLeaf(YType.uint64, "nbi-rx-total-pkt-cnt")

                                    self.nbi_tx_total_byte_cnt = YLeaf(YType.uint64, "nbi-tx-total-byte-cnt")

                                    self.nbi_tx_total_pkt_cnt = YLeaf(YType.uint64, "nbi-tx-total-pkt-cnt")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("egq_deleted_pkt_cnt",
                                                    "egq_ehp_mc_high_discard_cnt",
                                                    "egq_ehp_mc_high_pkt_cnt",
                                                    "egq_ehp_mc_low_discard_cnt",
                                                    "egq_ehp_mc_low_pkt_cnt",
                                                    "egq_ehp_uc_pkt_cnt",
                                                    "egq_erpp_lag_pruning_discard_cnt",
                                                    "egq_erpp_pmf_discard_cnt",
                                                    "egq_erpp_vlan_mbr_discard_cnt",
                                                    "egq_fqp_pkt_cnt",
                                                    "egq_pqp_discard_mc_pkt_cnt",
                                                    "egq_pqp_discard_uc_pkt_cnt",
                                                    "egq_pqp_mc_bytes_cnt",
                                                    "egq_pqp_mc_pkt_cnt",
                                                    "egq_pqp_uc_bytes_cnt",
                                                    "egq_pqp_uc_pkt_cnt",
                                                    "epni_epe_byte_cnt",
                                                    "epni_epe_discard_cnt",
                                                    "epni_epe_pkt_cnt",
                                                    "fda_cells_in_cnt_p1",
                                                    "fda_cells_in_cnt_p2",
                                                    "fda_cells_in_cnt_p3",
                                                    "fda_cells_in_ipt_cnt",
                                                    "fda_cells_in_meshmc_cnt",
                                                    "fda_cells_in_tdm_cnt",
                                                    "fda_cells_out_cnt_p1",
                                                    "fda_cells_out_cnt_p2",
                                                    "fda_cells_out_cnt_p3",
                                                    "fda_cells_out_ipt_cnt",
                                                    "fda_cells_out_meshmc_cnt",
                                                    "fda_cells_out_tdm_cnt",
                                                    "fda_egq_drop_cnt",
                                                    "fda_egq_meshmc_drop_cnt",
                                                    "fdr_cell_in_cnt_total",
                                                    "fdr_p1_cell_in_cnt",
                                                    "fdr_p2_cell_in_cnt",
                                                    "fdr_p3_cell_in_cnt",
                                                    "fdt_ipt_desc_cell_cnt",
                                                    "fdt_ire_desc_cell_cnt",
                                                    "fdt_transmitted_data_cells_cnt",
                                                    "idr_mmu_if_cnt",
                                                    "idr_ocb_if_cnt",
                                                    "ipt_cfg_byte_cnt",
                                                    "ipt_cfg_event_cnt",
                                                    "ipt_egq_pkt_cnt",
                                                    "ipt_enq_pkt_cnt",
                                                    "ipt_fdt_pkt_cnt",
                                                    "iqm_deleted_pkt_cnt",
                                                    "iqm_dequeue_pkt_cnt",
                                                    "iqm_enq_discarded_pkt_cnt",
                                                    "iqm_enqueue_pkt_cnt",
                                                    "ire_cpu_pkt_cnt",
                                                    "ire_fdt_if_cnt",
                                                    "ire_nif_pkt_cnt",
                                                    "ire_oamp_pkt_cnt",
                                                    "ire_olp_pkt_cnt",
                                                    "ire_rcy_pkt_cnt",
                                                    "nbi_rx_total_byte_cnt",
                                                    "nbi_rx_total_pkt_cnt",
                                                    "nbi_tx_total_byte_cnt",
                                                    "nbi_tx_total_pkt_cnt") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsForNpuIds.AsicStatisticsForNpuId.Statistics, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsForNpuIds.AsicStatisticsForNpuId.Statistics, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.egq_deleted_pkt_cnt.is_set or
                                        self.egq_ehp_mc_high_discard_cnt.is_set or
                                        self.egq_ehp_mc_high_pkt_cnt.is_set or
                                        self.egq_ehp_mc_low_discard_cnt.is_set or
                                        self.egq_ehp_mc_low_pkt_cnt.is_set or
                                        self.egq_ehp_uc_pkt_cnt.is_set or
                                        self.egq_erpp_lag_pruning_discard_cnt.is_set or
                                        self.egq_erpp_pmf_discard_cnt.is_set or
                                        self.egq_erpp_vlan_mbr_discard_cnt.is_set or
                                        self.egq_fqp_pkt_cnt.is_set or
                                        self.egq_pqp_discard_mc_pkt_cnt.is_set or
                                        self.egq_pqp_discard_uc_pkt_cnt.is_set or
                                        self.egq_pqp_mc_bytes_cnt.is_set or
                                        self.egq_pqp_mc_pkt_cnt.is_set or
                                        self.egq_pqp_uc_bytes_cnt.is_set or
                                        self.egq_pqp_uc_pkt_cnt.is_set or
                                        self.epni_epe_byte_cnt.is_set or
                                        self.epni_epe_discard_cnt.is_set or
                                        self.epni_epe_pkt_cnt.is_set or
                                        self.fda_cells_in_cnt_p1.is_set or
                                        self.fda_cells_in_cnt_p2.is_set or
                                        self.fda_cells_in_cnt_p3.is_set or
                                        self.fda_cells_in_ipt_cnt.is_set or
                                        self.fda_cells_in_meshmc_cnt.is_set or
                                        self.fda_cells_in_tdm_cnt.is_set or
                                        self.fda_cells_out_cnt_p1.is_set or
                                        self.fda_cells_out_cnt_p2.is_set or
                                        self.fda_cells_out_cnt_p3.is_set or
                                        self.fda_cells_out_ipt_cnt.is_set or
                                        self.fda_cells_out_meshmc_cnt.is_set or
                                        self.fda_cells_out_tdm_cnt.is_set or
                                        self.fda_egq_drop_cnt.is_set or
                                        self.fda_egq_meshmc_drop_cnt.is_set or
                                        self.fdr_cell_in_cnt_total.is_set or
                                        self.fdr_p1_cell_in_cnt.is_set or
                                        self.fdr_p2_cell_in_cnt.is_set or
                                        self.fdr_p3_cell_in_cnt.is_set or
                                        self.fdt_ipt_desc_cell_cnt.is_set or
                                        self.fdt_ire_desc_cell_cnt.is_set or
                                        self.fdt_transmitted_data_cells_cnt.is_set or
                                        self.idr_mmu_if_cnt.is_set or
                                        self.idr_ocb_if_cnt.is_set or
                                        self.ipt_cfg_byte_cnt.is_set or
                                        self.ipt_cfg_event_cnt.is_set or
                                        self.ipt_egq_pkt_cnt.is_set or
                                        self.ipt_enq_pkt_cnt.is_set or
                                        self.ipt_fdt_pkt_cnt.is_set or
                                        self.iqm_deleted_pkt_cnt.is_set or
                                        self.iqm_dequeue_pkt_cnt.is_set or
                                        self.iqm_enq_discarded_pkt_cnt.is_set or
                                        self.iqm_enqueue_pkt_cnt.is_set or
                                        self.ire_cpu_pkt_cnt.is_set or
                                        self.ire_fdt_if_cnt.is_set or
                                        self.ire_nif_pkt_cnt.is_set or
                                        self.ire_oamp_pkt_cnt.is_set or
                                        self.ire_olp_pkt_cnt.is_set or
                                        self.ire_rcy_pkt_cnt.is_set or
                                        self.nbi_rx_total_byte_cnt.is_set or
                                        self.nbi_rx_total_pkt_cnt.is_set or
                                        self.nbi_tx_total_byte_cnt.is_set or
                                        self.nbi_tx_total_pkt_cnt.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.egq_deleted_pkt_cnt.yfilter != YFilter.not_set or
                                        self.egq_ehp_mc_high_discard_cnt.yfilter != YFilter.not_set or
                                        self.egq_ehp_mc_high_pkt_cnt.yfilter != YFilter.not_set or
                                        self.egq_ehp_mc_low_discard_cnt.yfilter != YFilter.not_set or
                                        self.egq_ehp_mc_low_pkt_cnt.yfilter != YFilter.not_set or
                                        self.egq_ehp_uc_pkt_cnt.yfilter != YFilter.not_set or
                                        self.egq_erpp_lag_pruning_discard_cnt.yfilter != YFilter.not_set or
                                        self.egq_erpp_pmf_discard_cnt.yfilter != YFilter.not_set or
                                        self.egq_erpp_vlan_mbr_discard_cnt.yfilter != YFilter.not_set or
                                        self.egq_fqp_pkt_cnt.yfilter != YFilter.not_set or
                                        self.egq_pqp_discard_mc_pkt_cnt.yfilter != YFilter.not_set or
                                        self.egq_pqp_discard_uc_pkt_cnt.yfilter != YFilter.not_set or
                                        self.egq_pqp_mc_bytes_cnt.yfilter != YFilter.not_set or
                                        self.egq_pqp_mc_pkt_cnt.yfilter != YFilter.not_set or
                                        self.egq_pqp_uc_bytes_cnt.yfilter != YFilter.not_set or
                                        self.egq_pqp_uc_pkt_cnt.yfilter != YFilter.not_set or
                                        self.epni_epe_byte_cnt.yfilter != YFilter.not_set or
                                        self.epni_epe_discard_cnt.yfilter != YFilter.not_set or
                                        self.epni_epe_pkt_cnt.yfilter != YFilter.not_set or
                                        self.fda_cells_in_cnt_p1.yfilter != YFilter.not_set or
                                        self.fda_cells_in_cnt_p2.yfilter != YFilter.not_set or
                                        self.fda_cells_in_cnt_p3.yfilter != YFilter.not_set or
                                        self.fda_cells_in_ipt_cnt.yfilter != YFilter.not_set or
                                        self.fda_cells_in_meshmc_cnt.yfilter != YFilter.not_set or
                                        self.fda_cells_in_tdm_cnt.yfilter != YFilter.not_set or
                                        self.fda_cells_out_cnt_p1.yfilter != YFilter.not_set or
                                        self.fda_cells_out_cnt_p2.yfilter != YFilter.not_set or
                                        self.fda_cells_out_cnt_p3.yfilter != YFilter.not_set or
                                        self.fda_cells_out_ipt_cnt.yfilter != YFilter.not_set or
                                        self.fda_cells_out_meshmc_cnt.yfilter != YFilter.not_set or
                                        self.fda_cells_out_tdm_cnt.yfilter != YFilter.not_set or
                                        self.fda_egq_drop_cnt.yfilter != YFilter.not_set or
                                        self.fda_egq_meshmc_drop_cnt.yfilter != YFilter.not_set or
                                        self.fdr_cell_in_cnt_total.yfilter != YFilter.not_set or
                                        self.fdr_p1_cell_in_cnt.yfilter != YFilter.not_set or
                                        self.fdr_p2_cell_in_cnt.yfilter != YFilter.not_set or
                                        self.fdr_p3_cell_in_cnt.yfilter != YFilter.not_set or
                                        self.fdt_ipt_desc_cell_cnt.yfilter != YFilter.not_set or
                                        self.fdt_ire_desc_cell_cnt.yfilter != YFilter.not_set or
                                        self.fdt_transmitted_data_cells_cnt.yfilter != YFilter.not_set or
                                        self.idr_mmu_if_cnt.yfilter != YFilter.not_set or
                                        self.idr_ocb_if_cnt.yfilter != YFilter.not_set or
                                        self.ipt_cfg_byte_cnt.yfilter != YFilter.not_set or
                                        self.ipt_cfg_event_cnt.yfilter != YFilter.not_set or
                                        self.ipt_egq_pkt_cnt.yfilter != YFilter.not_set or
                                        self.ipt_enq_pkt_cnt.yfilter != YFilter.not_set or
                                        self.ipt_fdt_pkt_cnt.yfilter != YFilter.not_set or
                                        self.iqm_deleted_pkt_cnt.yfilter != YFilter.not_set or
                                        self.iqm_dequeue_pkt_cnt.yfilter != YFilter.not_set or
                                        self.iqm_enq_discarded_pkt_cnt.yfilter != YFilter.not_set or
                                        self.iqm_enqueue_pkt_cnt.yfilter != YFilter.not_set or
                                        self.ire_cpu_pkt_cnt.yfilter != YFilter.not_set or
                                        self.ire_fdt_if_cnt.yfilter != YFilter.not_set or
                                        self.ire_nif_pkt_cnt.yfilter != YFilter.not_set or
                                        self.ire_oamp_pkt_cnt.yfilter != YFilter.not_set or
                                        self.ire_olp_pkt_cnt.yfilter != YFilter.not_set or
                                        self.ire_rcy_pkt_cnt.yfilter != YFilter.not_set or
                                        self.nbi_rx_total_byte_cnt.yfilter != YFilter.not_set or
                                        self.nbi_rx_total_pkt_cnt.yfilter != YFilter.not_set or
                                        self.nbi_tx_total_byte_cnt.yfilter != YFilter.not_set or
                                        self.nbi_tx_total_pkt_cnt.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "statistics" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.egq_deleted_pkt_cnt.is_set or self.egq_deleted_pkt_cnt.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.egq_deleted_pkt_cnt.get_name_leafdata())
                                    if (self.egq_ehp_mc_high_discard_cnt.is_set or self.egq_ehp_mc_high_discard_cnt.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.egq_ehp_mc_high_discard_cnt.get_name_leafdata())
                                    if (self.egq_ehp_mc_high_pkt_cnt.is_set or self.egq_ehp_mc_high_pkt_cnt.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.egq_ehp_mc_high_pkt_cnt.get_name_leafdata())
                                    if (self.egq_ehp_mc_low_discard_cnt.is_set or self.egq_ehp_mc_low_discard_cnt.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.egq_ehp_mc_low_discard_cnt.get_name_leafdata())
                                    if (self.egq_ehp_mc_low_pkt_cnt.is_set or self.egq_ehp_mc_low_pkt_cnt.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.egq_ehp_mc_low_pkt_cnt.get_name_leafdata())
                                    if (self.egq_ehp_uc_pkt_cnt.is_set or self.egq_ehp_uc_pkt_cnt.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.egq_ehp_uc_pkt_cnt.get_name_leafdata())
                                    if (self.egq_erpp_lag_pruning_discard_cnt.is_set or self.egq_erpp_lag_pruning_discard_cnt.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.egq_erpp_lag_pruning_discard_cnt.get_name_leafdata())
                                    if (self.egq_erpp_pmf_discard_cnt.is_set or self.egq_erpp_pmf_discard_cnt.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.egq_erpp_pmf_discard_cnt.get_name_leafdata())
                                    if (self.egq_erpp_vlan_mbr_discard_cnt.is_set or self.egq_erpp_vlan_mbr_discard_cnt.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.egq_erpp_vlan_mbr_discard_cnt.get_name_leafdata())
                                    if (self.egq_fqp_pkt_cnt.is_set or self.egq_fqp_pkt_cnt.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.egq_fqp_pkt_cnt.get_name_leafdata())
                                    if (self.egq_pqp_discard_mc_pkt_cnt.is_set or self.egq_pqp_discard_mc_pkt_cnt.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.egq_pqp_discard_mc_pkt_cnt.get_name_leafdata())
                                    if (self.egq_pqp_discard_uc_pkt_cnt.is_set or self.egq_pqp_discard_uc_pkt_cnt.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.egq_pqp_discard_uc_pkt_cnt.get_name_leafdata())
                                    if (self.egq_pqp_mc_bytes_cnt.is_set or self.egq_pqp_mc_bytes_cnt.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.egq_pqp_mc_bytes_cnt.get_name_leafdata())
                                    if (self.egq_pqp_mc_pkt_cnt.is_set or self.egq_pqp_mc_pkt_cnt.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.egq_pqp_mc_pkt_cnt.get_name_leafdata())
                                    if (self.egq_pqp_uc_bytes_cnt.is_set or self.egq_pqp_uc_bytes_cnt.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.egq_pqp_uc_bytes_cnt.get_name_leafdata())
                                    if (self.egq_pqp_uc_pkt_cnt.is_set or self.egq_pqp_uc_pkt_cnt.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.egq_pqp_uc_pkt_cnt.get_name_leafdata())
                                    if (self.epni_epe_byte_cnt.is_set or self.epni_epe_byte_cnt.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.epni_epe_byte_cnt.get_name_leafdata())
                                    if (self.epni_epe_discard_cnt.is_set or self.epni_epe_discard_cnt.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.epni_epe_discard_cnt.get_name_leafdata())
                                    if (self.epni_epe_pkt_cnt.is_set or self.epni_epe_pkt_cnt.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.epni_epe_pkt_cnt.get_name_leafdata())
                                    if (self.fda_cells_in_cnt_p1.is_set or self.fda_cells_in_cnt_p1.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.fda_cells_in_cnt_p1.get_name_leafdata())
                                    if (self.fda_cells_in_cnt_p2.is_set or self.fda_cells_in_cnt_p2.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.fda_cells_in_cnt_p2.get_name_leafdata())
                                    if (self.fda_cells_in_cnt_p3.is_set or self.fda_cells_in_cnt_p3.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.fda_cells_in_cnt_p3.get_name_leafdata())
                                    if (self.fda_cells_in_ipt_cnt.is_set or self.fda_cells_in_ipt_cnt.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.fda_cells_in_ipt_cnt.get_name_leafdata())
                                    if (self.fda_cells_in_meshmc_cnt.is_set or self.fda_cells_in_meshmc_cnt.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.fda_cells_in_meshmc_cnt.get_name_leafdata())
                                    if (self.fda_cells_in_tdm_cnt.is_set or self.fda_cells_in_tdm_cnt.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.fda_cells_in_tdm_cnt.get_name_leafdata())
                                    if (self.fda_cells_out_cnt_p1.is_set or self.fda_cells_out_cnt_p1.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.fda_cells_out_cnt_p1.get_name_leafdata())
                                    if (self.fda_cells_out_cnt_p2.is_set or self.fda_cells_out_cnt_p2.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.fda_cells_out_cnt_p2.get_name_leafdata())
                                    if (self.fda_cells_out_cnt_p3.is_set or self.fda_cells_out_cnt_p3.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.fda_cells_out_cnt_p3.get_name_leafdata())
                                    if (self.fda_cells_out_ipt_cnt.is_set or self.fda_cells_out_ipt_cnt.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.fda_cells_out_ipt_cnt.get_name_leafdata())
                                    if (self.fda_cells_out_meshmc_cnt.is_set or self.fda_cells_out_meshmc_cnt.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.fda_cells_out_meshmc_cnt.get_name_leafdata())
                                    if (self.fda_cells_out_tdm_cnt.is_set or self.fda_cells_out_tdm_cnt.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.fda_cells_out_tdm_cnt.get_name_leafdata())
                                    if (self.fda_egq_drop_cnt.is_set or self.fda_egq_drop_cnt.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.fda_egq_drop_cnt.get_name_leafdata())
                                    if (self.fda_egq_meshmc_drop_cnt.is_set or self.fda_egq_meshmc_drop_cnt.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.fda_egq_meshmc_drop_cnt.get_name_leafdata())
                                    if (self.fdr_cell_in_cnt_total.is_set or self.fdr_cell_in_cnt_total.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.fdr_cell_in_cnt_total.get_name_leafdata())
                                    if (self.fdr_p1_cell_in_cnt.is_set or self.fdr_p1_cell_in_cnt.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.fdr_p1_cell_in_cnt.get_name_leafdata())
                                    if (self.fdr_p2_cell_in_cnt.is_set or self.fdr_p2_cell_in_cnt.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.fdr_p2_cell_in_cnt.get_name_leafdata())
                                    if (self.fdr_p3_cell_in_cnt.is_set or self.fdr_p3_cell_in_cnt.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.fdr_p3_cell_in_cnt.get_name_leafdata())
                                    if (self.fdt_ipt_desc_cell_cnt.is_set or self.fdt_ipt_desc_cell_cnt.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.fdt_ipt_desc_cell_cnt.get_name_leafdata())
                                    if (self.fdt_ire_desc_cell_cnt.is_set or self.fdt_ire_desc_cell_cnt.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.fdt_ire_desc_cell_cnt.get_name_leafdata())
                                    if (self.fdt_transmitted_data_cells_cnt.is_set or self.fdt_transmitted_data_cells_cnt.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.fdt_transmitted_data_cells_cnt.get_name_leafdata())
                                    if (self.idr_mmu_if_cnt.is_set or self.idr_mmu_if_cnt.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.idr_mmu_if_cnt.get_name_leafdata())
                                    if (self.idr_ocb_if_cnt.is_set or self.idr_ocb_if_cnt.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.idr_ocb_if_cnt.get_name_leafdata())
                                    if (self.ipt_cfg_byte_cnt.is_set or self.ipt_cfg_byte_cnt.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.ipt_cfg_byte_cnt.get_name_leafdata())
                                    if (self.ipt_cfg_event_cnt.is_set or self.ipt_cfg_event_cnt.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.ipt_cfg_event_cnt.get_name_leafdata())
                                    if (self.ipt_egq_pkt_cnt.is_set or self.ipt_egq_pkt_cnt.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.ipt_egq_pkt_cnt.get_name_leafdata())
                                    if (self.ipt_enq_pkt_cnt.is_set or self.ipt_enq_pkt_cnt.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.ipt_enq_pkt_cnt.get_name_leafdata())
                                    if (self.ipt_fdt_pkt_cnt.is_set or self.ipt_fdt_pkt_cnt.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.ipt_fdt_pkt_cnt.get_name_leafdata())
                                    if (self.iqm_deleted_pkt_cnt.is_set or self.iqm_deleted_pkt_cnt.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.iqm_deleted_pkt_cnt.get_name_leafdata())
                                    if (self.iqm_dequeue_pkt_cnt.is_set or self.iqm_dequeue_pkt_cnt.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.iqm_dequeue_pkt_cnt.get_name_leafdata())
                                    if (self.iqm_enq_discarded_pkt_cnt.is_set or self.iqm_enq_discarded_pkt_cnt.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.iqm_enq_discarded_pkt_cnt.get_name_leafdata())
                                    if (self.iqm_enqueue_pkt_cnt.is_set or self.iqm_enqueue_pkt_cnt.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.iqm_enqueue_pkt_cnt.get_name_leafdata())
                                    if (self.ire_cpu_pkt_cnt.is_set or self.ire_cpu_pkt_cnt.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.ire_cpu_pkt_cnt.get_name_leafdata())
                                    if (self.ire_fdt_if_cnt.is_set or self.ire_fdt_if_cnt.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.ire_fdt_if_cnt.get_name_leafdata())
                                    if (self.ire_nif_pkt_cnt.is_set or self.ire_nif_pkt_cnt.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.ire_nif_pkt_cnt.get_name_leafdata())
                                    if (self.ire_oamp_pkt_cnt.is_set or self.ire_oamp_pkt_cnt.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.ire_oamp_pkt_cnt.get_name_leafdata())
                                    if (self.ire_olp_pkt_cnt.is_set or self.ire_olp_pkt_cnt.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.ire_olp_pkt_cnt.get_name_leafdata())
                                    if (self.ire_rcy_pkt_cnt.is_set or self.ire_rcy_pkt_cnt.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.ire_rcy_pkt_cnt.get_name_leafdata())
                                    if (self.nbi_rx_total_byte_cnt.is_set or self.nbi_rx_total_byte_cnt.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.nbi_rx_total_byte_cnt.get_name_leafdata())
                                    if (self.nbi_rx_total_pkt_cnt.is_set or self.nbi_rx_total_pkt_cnt.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.nbi_rx_total_pkt_cnt.get_name_leafdata())
                                    if (self.nbi_tx_total_byte_cnt.is_set or self.nbi_tx_total_byte_cnt.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.nbi_tx_total_byte_cnt.get_name_leafdata())
                                    if (self.nbi_tx_total_pkt_cnt.is_set or self.nbi_tx_total_pkt_cnt.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.nbi_tx_total_pkt_cnt.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "egq-deleted-pkt-cnt" or name == "egq-ehp-mc-high-discard-cnt" or name == "egq-ehp-mc-high-pkt-cnt" or name == "egq-ehp-mc-low-discard-cnt" or name == "egq-ehp-mc-low-pkt-cnt" or name == "egq-ehp-uc-pkt-cnt" or name == "egq-erpp-lag-pruning-discard-cnt" or name == "egq-erpp-pmf-discard-cnt" or name == "egq-erpp-vlan-mbr-discard-cnt" or name == "egq-fqp-pkt-cnt" or name == "egq-pqp-discard-mc-pkt-cnt" or name == "egq-pqp-discard-uc-pkt-cnt" or name == "egq-pqp-mc-bytes-cnt" or name == "egq-pqp-mc-pkt-cnt" or name == "egq-pqp-uc-bytes-cnt" or name == "egq-pqp-uc-pkt-cnt" or name == "epni-epe-byte-cnt" or name == "epni-epe-discard-cnt" or name == "epni-epe-pkt-cnt" or name == "fda-cells-in-cnt-p1" or name == "fda-cells-in-cnt-p2" or name == "fda-cells-in-cnt-p3" or name == "fda-cells-in-ipt-cnt" or name == "fda-cells-in-meshmc-cnt" or name == "fda-cells-in-tdm-cnt" or name == "fda-cells-out-cnt-p1" or name == "fda-cells-out-cnt-p2" or name == "fda-cells-out-cnt-p3" or name == "fda-cells-out-ipt-cnt" or name == "fda-cells-out-meshmc-cnt" or name == "fda-cells-out-tdm-cnt" or name == "fda-egq-drop-cnt" or name == "fda-egq-meshmc-drop-cnt" or name == "fdr-cell-in-cnt-total" or name == "fdr-p1-cell-in-cnt" or name == "fdr-p2-cell-in-cnt" or name == "fdr-p3-cell-in-cnt" or name == "fdt-ipt-desc-cell-cnt" or name == "fdt-ire-desc-cell-cnt" or name == "fdt-transmitted-data-cells-cnt" or name == "idr-mmu-if-cnt" or name == "idr-ocb-if-cnt" or name == "ipt-cfg-byte-cnt" or name == "ipt-cfg-event-cnt" or name == "ipt-egq-pkt-cnt" or name == "ipt-enq-pkt-cnt" or name == "ipt-fdt-pkt-cnt" or name == "iqm-deleted-pkt-cnt" or name == "iqm-dequeue-pkt-cnt" or name == "iqm-enq-discarded-pkt-cnt" or name == "iqm-enqueue-pkt-cnt" or name == "ire-cpu-pkt-cnt" or name == "ire-fdt-if-cnt" or name == "ire-nif-pkt-cnt" or name == "ire-oamp-pkt-cnt" or name == "ire-olp-pkt-cnt" or name == "ire-rcy-pkt-cnt" or name == "nbi-rx-total-byte-cnt" or name == "nbi-rx-total-pkt-cnt" or name == "nbi-tx-total-byte-cnt" or name == "nbi-tx-total-pkt-cnt"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "egq-deleted-pkt-cnt"):
                                        self.egq_deleted_pkt_cnt = value
                                        self.egq_deleted_pkt_cnt.value_namespace = name_space
                                        self.egq_deleted_pkt_cnt.value_namespace_prefix = name_space_prefix
                                    if(value_path == "egq-ehp-mc-high-discard-cnt"):
                                        self.egq_ehp_mc_high_discard_cnt = value
                                        self.egq_ehp_mc_high_discard_cnt.value_namespace = name_space
                                        self.egq_ehp_mc_high_discard_cnt.value_namespace_prefix = name_space_prefix
                                    if(value_path == "egq-ehp-mc-high-pkt-cnt"):
                                        self.egq_ehp_mc_high_pkt_cnt = value
                                        self.egq_ehp_mc_high_pkt_cnt.value_namespace = name_space
                                        self.egq_ehp_mc_high_pkt_cnt.value_namespace_prefix = name_space_prefix
                                    if(value_path == "egq-ehp-mc-low-discard-cnt"):
                                        self.egq_ehp_mc_low_discard_cnt = value
                                        self.egq_ehp_mc_low_discard_cnt.value_namespace = name_space
                                        self.egq_ehp_mc_low_discard_cnt.value_namespace_prefix = name_space_prefix
                                    if(value_path == "egq-ehp-mc-low-pkt-cnt"):
                                        self.egq_ehp_mc_low_pkt_cnt = value
                                        self.egq_ehp_mc_low_pkt_cnt.value_namespace = name_space
                                        self.egq_ehp_mc_low_pkt_cnt.value_namespace_prefix = name_space_prefix
                                    if(value_path == "egq-ehp-uc-pkt-cnt"):
                                        self.egq_ehp_uc_pkt_cnt = value
                                        self.egq_ehp_uc_pkt_cnt.value_namespace = name_space
                                        self.egq_ehp_uc_pkt_cnt.value_namespace_prefix = name_space_prefix
                                    if(value_path == "egq-erpp-lag-pruning-discard-cnt"):
                                        self.egq_erpp_lag_pruning_discard_cnt = value
                                        self.egq_erpp_lag_pruning_discard_cnt.value_namespace = name_space
                                        self.egq_erpp_lag_pruning_discard_cnt.value_namespace_prefix = name_space_prefix
                                    if(value_path == "egq-erpp-pmf-discard-cnt"):
                                        self.egq_erpp_pmf_discard_cnt = value
                                        self.egq_erpp_pmf_discard_cnt.value_namespace = name_space
                                        self.egq_erpp_pmf_discard_cnt.value_namespace_prefix = name_space_prefix
                                    if(value_path == "egq-erpp-vlan-mbr-discard-cnt"):
                                        self.egq_erpp_vlan_mbr_discard_cnt = value
                                        self.egq_erpp_vlan_mbr_discard_cnt.value_namespace = name_space
                                        self.egq_erpp_vlan_mbr_discard_cnt.value_namespace_prefix = name_space_prefix
                                    if(value_path == "egq-fqp-pkt-cnt"):
                                        self.egq_fqp_pkt_cnt = value
                                        self.egq_fqp_pkt_cnt.value_namespace = name_space
                                        self.egq_fqp_pkt_cnt.value_namespace_prefix = name_space_prefix
                                    if(value_path == "egq-pqp-discard-mc-pkt-cnt"):
                                        self.egq_pqp_discard_mc_pkt_cnt = value
                                        self.egq_pqp_discard_mc_pkt_cnt.value_namespace = name_space
                                        self.egq_pqp_discard_mc_pkt_cnt.value_namespace_prefix = name_space_prefix
                                    if(value_path == "egq-pqp-discard-uc-pkt-cnt"):
                                        self.egq_pqp_discard_uc_pkt_cnt = value
                                        self.egq_pqp_discard_uc_pkt_cnt.value_namespace = name_space
                                        self.egq_pqp_discard_uc_pkt_cnt.value_namespace_prefix = name_space_prefix
                                    if(value_path == "egq-pqp-mc-bytes-cnt"):
                                        self.egq_pqp_mc_bytes_cnt = value
                                        self.egq_pqp_mc_bytes_cnt.value_namespace = name_space
                                        self.egq_pqp_mc_bytes_cnt.value_namespace_prefix = name_space_prefix
                                    if(value_path == "egq-pqp-mc-pkt-cnt"):
                                        self.egq_pqp_mc_pkt_cnt = value
                                        self.egq_pqp_mc_pkt_cnt.value_namespace = name_space
                                        self.egq_pqp_mc_pkt_cnt.value_namespace_prefix = name_space_prefix
                                    if(value_path == "egq-pqp-uc-bytes-cnt"):
                                        self.egq_pqp_uc_bytes_cnt = value
                                        self.egq_pqp_uc_bytes_cnt.value_namespace = name_space
                                        self.egq_pqp_uc_bytes_cnt.value_namespace_prefix = name_space_prefix
                                    if(value_path == "egq-pqp-uc-pkt-cnt"):
                                        self.egq_pqp_uc_pkt_cnt = value
                                        self.egq_pqp_uc_pkt_cnt.value_namespace = name_space
                                        self.egq_pqp_uc_pkt_cnt.value_namespace_prefix = name_space_prefix
                                    if(value_path == "epni-epe-byte-cnt"):
                                        self.epni_epe_byte_cnt = value
                                        self.epni_epe_byte_cnt.value_namespace = name_space
                                        self.epni_epe_byte_cnt.value_namespace_prefix = name_space_prefix
                                    if(value_path == "epni-epe-discard-cnt"):
                                        self.epni_epe_discard_cnt = value
                                        self.epni_epe_discard_cnt.value_namespace = name_space
                                        self.epni_epe_discard_cnt.value_namespace_prefix = name_space_prefix
                                    if(value_path == "epni-epe-pkt-cnt"):
                                        self.epni_epe_pkt_cnt = value
                                        self.epni_epe_pkt_cnt.value_namespace = name_space
                                        self.epni_epe_pkt_cnt.value_namespace_prefix = name_space_prefix
                                    if(value_path == "fda-cells-in-cnt-p1"):
                                        self.fda_cells_in_cnt_p1 = value
                                        self.fda_cells_in_cnt_p1.value_namespace = name_space
                                        self.fda_cells_in_cnt_p1.value_namespace_prefix = name_space_prefix
                                    if(value_path == "fda-cells-in-cnt-p2"):
                                        self.fda_cells_in_cnt_p2 = value
                                        self.fda_cells_in_cnt_p2.value_namespace = name_space
                                        self.fda_cells_in_cnt_p2.value_namespace_prefix = name_space_prefix
                                    if(value_path == "fda-cells-in-cnt-p3"):
                                        self.fda_cells_in_cnt_p3 = value
                                        self.fda_cells_in_cnt_p3.value_namespace = name_space
                                        self.fda_cells_in_cnt_p3.value_namespace_prefix = name_space_prefix
                                    if(value_path == "fda-cells-in-ipt-cnt"):
                                        self.fda_cells_in_ipt_cnt = value
                                        self.fda_cells_in_ipt_cnt.value_namespace = name_space
                                        self.fda_cells_in_ipt_cnt.value_namespace_prefix = name_space_prefix
                                    if(value_path == "fda-cells-in-meshmc-cnt"):
                                        self.fda_cells_in_meshmc_cnt = value
                                        self.fda_cells_in_meshmc_cnt.value_namespace = name_space
                                        self.fda_cells_in_meshmc_cnt.value_namespace_prefix = name_space_prefix
                                    if(value_path == "fda-cells-in-tdm-cnt"):
                                        self.fda_cells_in_tdm_cnt = value
                                        self.fda_cells_in_tdm_cnt.value_namespace = name_space
                                        self.fda_cells_in_tdm_cnt.value_namespace_prefix = name_space_prefix
                                    if(value_path == "fda-cells-out-cnt-p1"):
                                        self.fda_cells_out_cnt_p1 = value
                                        self.fda_cells_out_cnt_p1.value_namespace = name_space
                                        self.fda_cells_out_cnt_p1.value_namespace_prefix = name_space_prefix
                                    if(value_path == "fda-cells-out-cnt-p2"):
                                        self.fda_cells_out_cnt_p2 = value
                                        self.fda_cells_out_cnt_p2.value_namespace = name_space
                                        self.fda_cells_out_cnt_p2.value_namespace_prefix = name_space_prefix
                                    if(value_path == "fda-cells-out-cnt-p3"):
                                        self.fda_cells_out_cnt_p3 = value
                                        self.fda_cells_out_cnt_p3.value_namespace = name_space
                                        self.fda_cells_out_cnt_p3.value_namespace_prefix = name_space_prefix
                                    if(value_path == "fda-cells-out-ipt-cnt"):
                                        self.fda_cells_out_ipt_cnt = value
                                        self.fda_cells_out_ipt_cnt.value_namespace = name_space
                                        self.fda_cells_out_ipt_cnt.value_namespace_prefix = name_space_prefix
                                    if(value_path == "fda-cells-out-meshmc-cnt"):
                                        self.fda_cells_out_meshmc_cnt = value
                                        self.fda_cells_out_meshmc_cnt.value_namespace = name_space
                                        self.fda_cells_out_meshmc_cnt.value_namespace_prefix = name_space_prefix
                                    if(value_path == "fda-cells-out-tdm-cnt"):
                                        self.fda_cells_out_tdm_cnt = value
                                        self.fda_cells_out_tdm_cnt.value_namespace = name_space
                                        self.fda_cells_out_tdm_cnt.value_namespace_prefix = name_space_prefix
                                    if(value_path == "fda-egq-drop-cnt"):
                                        self.fda_egq_drop_cnt = value
                                        self.fda_egq_drop_cnt.value_namespace = name_space
                                        self.fda_egq_drop_cnt.value_namespace_prefix = name_space_prefix
                                    if(value_path == "fda-egq-meshmc-drop-cnt"):
                                        self.fda_egq_meshmc_drop_cnt = value
                                        self.fda_egq_meshmc_drop_cnt.value_namespace = name_space
                                        self.fda_egq_meshmc_drop_cnt.value_namespace_prefix = name_space_prefix
                                    if(value_path == "fdr-cell-in-cnt-total"):
                                        self.fdr_cell_in_cnt_total = value
                                        self.fdr_cell_in_cnt_total.value_namespace = name_space
                                        self.fdr_cell_in_cnt_total.value_namespace_prefix = name_space_prefix
                                    if(value_path == "fdr-p1-cell-in-cnt"):
                                        self.fdr_p1_cell_in_cnt = value
                                        self.fdr_p1_cell_in_cnt.value_namespace = name_space
                                        self.fdr_p1_cell_in_cnt.value_namespace_prefix = name_space_prefix
                                    if(value_path == "fdr-p2-cell-in-cnt"):
                                        self.fdr_p2_cell_in_cnt = value
                                        self.fdr_p2_cell_in_cnt.value_namespace = name_space
                                        self.fdr_p2_cell_in_cnt.value_namespace_prefix = name_space_prefix
                                    if(value_path == "fdr-p3-cell-in-cnt"):
                                        self.fdr_p3_cell_in_cnt = value
                                        self.fdr_p3_cell_in_cnt.value_namespace = name_space
                                        self.fdr_p3_cell_in_cnt.value_namespace_prefix = name_space_prefix
                                    if(value_path == "fdt-ipt-desc-cell-cnt"):
                                        self.fdt_ipt_desc_cell_cnt = value
                                        self.fdt_ipt_desc_cell_cnt.value_namespace = name_space
                                        self.fdt_ipt_desc_cell_cnt.value_namespace_prefix = name_space_prefix
                                    if(value_path == "fdt-ire-desc-cell-cnt"):
                                        self.fdt_ire_desc_cell_cnt = value
                                        self.fdt_ire_desc_cell_cnt.value_namespace = name_space
                                        self.fdt_ire_desc_cell_cnt.value_namespace_prefix = name_space_prefix
                                    if(value_path == "fdt-transmitted-data-cells-cnt"):
                                        self.fdt_transmitted_data_cells_cnt = value
                                        self.fdt_transmitted_data_cells_cnt.value_namespace = name_space
                                        self.fdt_transmitted_data_cells_cnt.value_namespace_prefix = name_space_prefix
                                    if(value_path == "idr-mmu-if-cnt"):
                                        self.idr_mmu_if_cnt = value
                                        self.idr_mmu_if_cnt.value_namespace = name_space
                                        self.idr_mmu_if_cnt.value_namespace_prefix = name_space_prefix
                                    if(value_path == "idr-ocb-if-cnt"):
                                        self.idr_ocb_if_cnt = value
                                        self.idr_ocb_if_cnt.value_namespace = name_space
                                        self.idr_ocb_if_cnt.value_namespace_prefix = name_space_prefix
                                    if(value_path == "ipt-cfg-byte-cnt"):
                                        self.ipt_cfg_byte_cnt = value
                                        self.ipt_cfg_byte_cnt.value_namespace = name_space
                                        self.ipt_cfg_byte_cnt.value_namespace_prefix = name_space_prefix
                                    if(value_path == "ipt-cfg-event-cnt"):
                                        self.ipt_cfg_event_cnt = value
                                        self.ipt_cfg_event_cnt.value_namespace = name_space
                                        self.ipt_cfg_event_cnt.value_namespace_prefix = name_space_prefix
                                    if(value_path == "ipt-egq-pkt-cnt"):
                                        self.ipt_egq_pkt_cnt = value
                                        self.ipt_egq_pkt_cnt.value_namespace = name_space
                                        self.ipt_egq_pkt_cnt.value_namespace_prefix = name_space_prefix
                                    if(value_path == "ipt-enq-pkt-cnt"):
                                        self.ipt_enq_pkt_cnt = value
                                        self.ipt_enq_pkt_cnt.value_namespace = name_space
                                        self.ipt_enq_pkt_cnt.value_namespace_prefix = name_space_prefix
                                    if(value_path == "ipt-fdt-pkt-cnt"):
                                        self.ipt_fdt_pkt_cnt = value
                                        self.ipt_fdt_pkt_cnt.value_namespace = name_space
                                        self.ipt_fdt_pkt_cnt.value_namespace_prefix = name_space_prefix
                                    if(value_path == "iqm-deleted-pkt-cnt"):
                                        self.iqm_deleted_pkt_cnt = value
                                        self.iqm_deleted_pkt_cnt.value_namespace = name_space
                                        self.iqm_deleted_pkt_cnt.value_namespace_prefix = name_space_prefix
                                    if(value_path == "iqm-dequeue-pkt-cnt"):
                                        self.iqm_dequeue_pkt_cnt = value
                                        self.iqm_dequeue_pkt_cnt.value_namespace = name_space
                                        self.iqm_dequeue_pkt_cnt.value_namespace_prefix = name_space_prefix
                                    if(value_path == "iqm-enq-discarded-pkt-cnt"):
                                        self.iqm_enq_discarded_pkt_cnt = value
                                        self.iqm_enq_discarded_pkt_cnt.value_namespace = name_space
                                        self.iqm_enq_discarded_pkt_cnt.value_namespace_prefix = name_space_prefix
                                    if(value_path == "iqm-enqueue-pkt-cnt"):
                                        self.iqm_enqueue_pkt_cnt = value
                                        self.iqm_enqueue_pkt_cnt.value_namespace = name_space
                                        self.iqm_enqueue_pkt_cnt.value_namespace_prefix = name_space_prefix
                                    if(value_path == "ire-cpu-pkt-cnt"):
                                        self.ire_cpu_pkt_cnt = value
                                        self.ire_cpu_pkt_cnt.value_namespace = name_space
                                        self.ire_cpu_pkt_cnt.value_namespace_prefix = name_space_prefix
                                    if(value_path == "ire-fdt-if-cnt"):
                                        self.ire_fdt_if_cnt = value
                                        self.ire_fdt_if_cnt.value_namespace = name_space
                                        self.ire_fdt_if_cnt.value_namespace_prefix = name_space_prefix
                                    if(value_path == "ire-nif-pkt-cnt"):
                                        self.ire_nif_pkt_cnt = value
                                        self.ire_nif_pkt_cnt.value_namespace = name_space
                                        self.ire_nif_pkt_cnt.value_namespace_prefix = name_space_prefix
                                    if(value_path == "ire-oamp-pkt-cnt"):
                                        self.ire_oamp_pkt_cnt = value
                                        self.ire_oamp_pkt_cnt.value_namespace = name_space
                                        self.ire_oamp_pkt_cnt.value_namespace_prefix = name_space_prefix
                                    if(value_path == "ire-olp-pkt-cnt"):
                                        self.ire_olp_pkt_cnt = value
                                        self.ire_olp_pkt_cnt.value_namespace = name_space
                                        self.ire_olp_pkt_cnt.value_namespace_prefix = name_space_prefix
                                    if(value_path == "ire-rcy-pkt-cnt"):
                                        self.ire_rcy_pkt_cnt = value
                                        self.ire_rcy_pkt_cnt.value_namespace = name_space
                                        self.ire_rcy_pkt_cnt.value_namespace_prefix = name_space_prefix
                                    if(value_path == "nbi-rx-total-byte-cnt"):
                                        self.nbi_rx_total_byte_cnt = value
                                        self.nbi_rx_total_byte_cnt.value_namespace = name_space
                                        self.nbi_rx_total_byte_cnt.value_namespace_prefix = name_space_prefix
                                    if(value_path == "nbi-rx-total-pkt-cnt"):
                                        self.nbi_rx_total_pkt_cnt = value
                                        self.nbi_rx_total_pkt_cnt.value_namespace = name_space
                                        self.nbi_rx_total_pkt_cnt.value_namespace_prefix = name_space_prefix
                                    if(value_path == "nbi-tx-total-byte-cnt"):
                                        self.nbi_tx_total_byte_cnt = value
                                        self.nbi_tx_total_byte_cnt.value_namespace = name_space
                                        self.nbi_tx_total_byte_cnt.value_namespace_prefix = name_space_prefix
                                    if(value_path == "nbi-tx-total-pkt-cnt"):
                                        self.nbi_tx_total_pkt_cnt = value
                                        self.nbi_tx_total_pkt_cnt.value_namespace = name_space
                                        self.nbi_tx_total_pkt_cnt.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                return (
                                    self.npu_id.is_set or
                                    self.asic_instance.is_set or
                                    self.chip_version.is_set or
                                    self.rack_number.is_set or
                                    self.slot_number.is_set or
                                    self.valid.is_set or
                                    (self.statistics is not None and self.statistics.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.npu_id.yfilter != YFilter.not_set or
                                    self.asic_instance.yfilter != YFilter.not_set or
                                    self.chip_version.yfilter != YFilter.not_set or
                                    self.rack_number.yfilter != YFilter.not_set or
                                    self.slot_number.yfilter != YFilter.not_set or
                                    self.valid.yfilter != YFilter.not_set or
                                    (self.statistics is not None and self.statistics.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "asic-statistics-for-npu-id" + "[npu-id='" + self.npu_id.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.npu_id.is_set or self.npu_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.npu_id.get_name_leafdata())
                                if (self.asic_instance.is_set or self.asic_instance.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.asic_instance.get_name_leafdata())
                                if (self.chip_version.is_set or self.chip_version.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.chip_version.get_name_leafdata())
                                if (self.rack_number.is_set or self.rack_number.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.rack_number.get_name_leafdata())
                                if (self.slot_number.is_set or self.slot_number.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.slot_number.get_name_leafdata())
                                if (self.valid.is_set or self.valid.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.valid.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "statistics"):
                                    if (self.statistics is None):
                                        self.statistics = Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsForNpuIds.AsicStatisticsForNpuId.Statistics()
                                        self.statistics.parent = self
                                        self._children_name_map["statistics"] = "statistics"
                                    return self.statistics

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "statistics" or name == "npu-id" or name == "asic-instance" or name == "chip-version" or name == "rack-number" or name == "slot-number" or name == "valid"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "npu-id"):
                                    self.npu_id = value
                                    self.npu_id.value_namespace = name_space
                                    self.npu_id.value_namespace_prefix = name_space_prefix
                                if(value_path == "asic-instance"):
                                    self.asic_instance = value
                                    self.asic_instance.value_namespace = name_space
                                    self.asic_instance.value_namespace_prefix = name_space_prefix
                                if(value_path == "chip-version"):
                                    self.chip_version = value
                                    self.chip_version.value_namespace = name_space
                                    self.chip_version.value_namespace_prefix = name_space_prefix
                                if(value_path == "rack-number"):
                                    self.rack_number = value
                                    self.rack_number.value_namespace = name_space
                                    self.rack_number.value_namespace_prefix = name_space_prefix
                                if(value_path == "slot-number"):
                                    self.slot_number = value
                                    self.slot_number.value_namespace = name_space
                                    self.slot_number.value_namespace_prefix = name_space_prefix
                                if(value_path == "valid"):
                                    self.valid = value
                                    self.valid.value_namespace = name_space
                                    self.valid.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.asic_statistics_for_npu_id:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.asic_statistics_for_npu_id:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "asic-statistics-for-npu-ids" + path_buffer

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

                            if (child_yang_name == "asic-statistics-for-npu-id"):
                                for c in self.asic_statistics_for_npu_id:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsForNpuIds.AsicStatisticsForNpuId()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.asic_statistics_for_npu_id.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "asic-statistics-for-npu-id"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass


                    class AsicStatisticsDetailForNpuIds(Entity):
                        """
                        Detailed ASIC statistics
                        
                        .. attribute:: asic_statistics_detail_for_npu_id
                        
                        	Detailed ASIC statistics for a particular NPU
                        	**type**\: list of    :py:class:`AsicStatisticsDetailForNpuId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_hw_resources_oper.Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId>`
                        
                        

                        """

                        _prefix = 'fretta-bcm-dpa-hw-resources-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds, self).__init__()

                            self.yang_name = "asic-statistics-detail-for-npu-ids"
                            self.yang_parent_name = "asic-statistics"

                            self.asic_statistics_detail_for_npu_id = YList(self)

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
                                        super(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds, self).__setattr__(name, value)


                        class AsicStatisticsDetailForNpuId(Entity):
                            """
                            Detailed ASIC statistics for a particular
                            NPU
                            
                            .. attribute:: npu_id  <key>
                            
                            	NPU number
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: asic_instance
                            
                            	ASIC instance
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: chip_version
                            
                            	Chip version
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: rack_number
                            
                            	Rack number
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: slot_number
                            
                            	Slot number
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: statistics
                            
                            	Statistics
                            	**type**\:   :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_hw_resources_oper.Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId.Statistics>`
                            
                            .. attribute:: valid
                            
                            	Flag to indicate if data is valid
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'fretta-bcm-dpa-hw-resources-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId, self).__init__()

                                self.yang_name = "asic-statistics-detail-for-npu-id"
                                self.yang_parent_name = "asic-statistics-detail-for-npu-ids"

                                self.npu_id = YLeaf(YType.int32, "npu-id")

                                self.asic_instance = YLeaf(YType.uint32, "asic-instance")

                                self.chip_version = YLeaf(YType.uint16, "chip-version")

                                self.rack_number = YLeaf(YType.uint32, "rack-number")

                                self.slot_number = YLeaf(YType.uint32, "slot-number")

                                self.valid = YLeaf(YType.boolean, "valid")

                                self.statistics = Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId.Statistics()
                                self.statistics.parent = self
                                self._children_name_map["statistics"] = "statistics"
                                self._children_yang_names.add("statistics")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("npu_id",
                                                "asic_instance",
                                                "chip_version",
                                                "rack_number",
                                                "slot_number",
                                                "valid") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId, self).__setattr__(name, value)


                            class Statistics(Entity):
                                """
                                Statistics
                                
                                .. attribute:: block_info
                                
                                	Block information
                                	**type**\: list of    :py:class:`BlockInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_hw_resources_oper.Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId.Statistics.BlockInfo>`
                                
                                .. attribute:: num_blocks
                                
                                	Number of blocks
                                	**type**\:  int
                                
                                	**range:** 0..255
                                
                                

                                """

                                _prefix = 'fretta-bcm-dpa-hw-resources-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId.Statistics, self).__init__()

                                    self.yang_name = "statistics"
                                    self.yang_parent_name = "asic-statistics-detail-for-npu-id"

                                    self.num_blocks = YLeaf(YType.uint8, "num-blocks")

                                    self.block_info = YList(self)

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("num_blocks") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId.Statistics, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId.Statistics, self).__setattr__(name, value)


                                class BlockInfo(Entity):
                                    """
                                    Block information
                                    
                                    .. attribute:: block_name
                                    
                                    	Block name
                                    	**type**\:  str
                                    
                                    	**length:** 0..10
                                    
                                    .. attribute:: field_info
                                    
                                    	Field information
                                    	**type**\: list of    :py:class:`FieldInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_hw_resources_oper.Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId.Statistics.BlockInfo.FieldInfo>`
                                    
                                    .. attribute:: num_fields
                                    
                                    	Number of fields
                                    	**type**\:  int
                                    
                                    	**range:** 0..255
                                    
                                    

                                    """

                                    _prefix = 'fretta-bcm-dpa-hw-resources-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId.Statistics.BlockInfo, self).__init__()

                                        self.yang_name = "block-info"
                                        self.yang_parent_name = "statistics"

                                        self.block_name = YLeaf(YType.str, "block-name")

                                        self.num_fields = YLeaf(YType.uint8, "num-fields")

                                        self.field_info = YList(self)

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("block_name",
                                                        "num_fields") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId.Statistics.BlockInfo, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId.Statistics.BlockInfo, self).__setattr__(name, value)


                                    class FieldInfo(Entity):
                                        """
                                        Field information
                                        
                                        .. attribute:: field_name
                                        
                                        	Field name
                                        	**type**\:  str
                                        
                                        	**length:** 0..80
                                        
                                        .. attribute:: field_value
                                        
                                        	Field value
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: is_overflow
                                        
                                        	Flag to indicate overflow
                                        	**type**\:  bool
                                        
                                        

                                        """

                                        _prefix = 'fretta-bcm-dpa-hw-resources-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId.Statistics.BlockInfo.FieldInfo, self).__init__()

                                            self.yang_name = "field-info"
                                            self.yang_parent_name = "block-info"

                                            self.field_name = YLeaf(YType.str, "field-name")

                                            self.field_value = YLeaf(YType.uint64, "field-value")

                                            self.is_overflow = YLeaf(YType.boolean, "is-overflow")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("field_name",
                                                            "field_value",
                                                            "is_overflow") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId.Statistics.BlockInfo.FieldInfo, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId.Statistics.BlockInfo.FieldInfo, self).__setattr__(name, value)

                                        def has_data(self):
                                            return (
                                                self.field_name.is_set or
                                                self.field_value.is_set or
                                                self.is_overflow.is_set)

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.field_name.yfilter != YFilter.not_set or
                                                self.field_value.yfilter != YFilter.not_set or
                                                self.is_overflow.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "field-info" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.field_name.is_set or self.field_name.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.field_name.get_name_leafdata())
                                            if (self.field_value.is_set or self.field_value.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.field_value.get_name_leafdata())
                                            if (self.is_overflow.is_set or self.is_overflow.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.is_overflow.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "field-name" or name == "field-value" or name == "is-overflow"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "field-name"):
                                                self.field_name = value
                                                self.field_name.value_namespace = name_space
                                                self.field_name.value_namespace_prefix = name_space_prefix
                                            if(value_path == "field-value"):
                                                self.field_value = value
                                                self.field_value.value_namespace = name_space
                                                self.field_value.value_namespace_prefix = name_space_prefix
                                            if(value_path == "is-overflow"):
                                                self.is_overflow = value
                                                self.is_overflow.value_namespace = name_space
                                                self.is_overflow.value_namespace_prefix = name_space_prefix

                                    def has_data(self):
                                        for c in self.field_info:
                                            if (c.has_data()):
                                                return True
                                        return (
                                            self.block_name.is_set or
                                            self.num_fields.is_set)

                                    def has_operation(self):
                                        for c in self.field_info:
                                            if (c.has_operation()):
                                                return True
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.block_name.yfilter != YFilter.not_set or
                                            self.num_fields.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "block-info" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.block_name.is_set or self.block_name.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.block_name.get_name_leafdata())
                                        if (self.num_fields.is_set or self.num_fields.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.num_fields.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        if (child_yang_name == "field-info"):
                                            for c in self.field_info:
                                                segment = c.get_segment_path()
                                                if (segment_path == segment):
                                                    return c
                                            c = Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId.Statistics.BlockInfo.FieldInfo()
                                            c.parent = self
                                            local_reference_key = "ydk::seg::%s" % segment_path
                                            self._local_refs[local_reference_key] = c
                                            self.field_info.append(c)
                                            return c

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "field-info" or name == "block-name" or name == "num-fields"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "block-name"):
                                            self.block_name = value
                                            self.block_name.value_namespace = name_space
                                            self.block_name.value_namespace_prefix = name_space_prefix
                                        if(value_path == "num-fields"):
                                            self.num_fields = value
                                            self.num_fields.value_namespace = name_space
                                            self.num_fields.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    for c in self.block_info:
                                        if (c.has_data()):
                                            return True
                                    return self.num_blocks.is_set

                                def has_operation(self):
                                    for c in self.block_info:
                                        if (c.has_operation()):
                                            return True
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.num_blocks.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "statistics" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.num_blocks.is_set or self.num_blocks.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.num_blocks.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "block-info"):
                                        for c in self.block_info:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId.Statistics.BlockInfo()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.block_info.append(c)
                                        return c

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "block-info" or name == "num-blocks"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "num-blocks"):
                                        self.num_blocks = value
                                        self.num_blocks.value_namespace = name_space
                                        self.num_blocks.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                return (
                                    self.npu_id.is_set or
                                    self.asic_instance.is_set or
                                    self.chip_version.is_set or
                                    self.rack_number.is_set or
                                    self.slot_number.is_set or
                                    self.valid.is_set or
                                    (self.statistics is not None and self.statistics.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.npu_id.yfilter != YFilter.not_set or
                                    self.asic_instance.yfilter != YFilter.not_set or
                                    self.chip_version.yfilter != YFilter.not_set or
                                    self.rack_number.yfilter != YFilter.not_set or
                                    self.slot_number.yfilter != YFilter.not_set or
                                    self.valid.yfilter != YFilter.not_set or
                                    (self.statistics is not None and self.statistics.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "asic-statistics-detail-for-npu-id" + "[npu-id='" + self.npu_id.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.npu_id.is_set or self.npu_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.npu_id.get_name_leafdata())
                                if (self.asic_instance.is_set or self.asic_instance.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.asic_instance.get_name_leafdata())
                                if (self.chip_version.is_set or self.chip_version.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.chip_version.get_name_leafdata())
                                if (self.rack_number.is_set or self.rack_number.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.rack_number.get_name_leafdata())
                                if (self.slot_number.is_set or self.slot_number.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.slot_number.get_name_leafdata())
                                if (self.valid.is_set or self.valid.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.valid.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "statistics"):
                                    if (self.statistics is None):
                                        self.statistics = Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId.Statistics()
                                        self.statistics.parent = self
                                        self._children_name_map["statistics"] = "statistics"
                                    return self.statistics

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "statistics" or name == "npu-id" or name == "asic-instance" or name == "chip-version" or name == "rack-number" or name == "slot-number" or name == "valid"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "npu-id"):
                                    self.npu_id = value
                                    self.npu_id.value_namespace = name_space
                                    self.npu_id.value_namespace_prefix = name_space_prefix
                                if(value_path == "asic-instance"):
                                    self.asic_instance = value
                                    self.asic_instance.value_namespace = name_space
                                    self.asic_instance.value_namespace_prefix = name_space_prefix
                                if(value_path == "chip-version"):
                                    self.chip_version = value
                                    self.chip_version.value_namespace = name_space
                                    self.chip_version.value_namespace_prefix = name_space_prefix
                                if(value_path == "rack-number"):
                                    self.rack_number = value
                                    self.rack_number.value_namespace = name_space
                                    self.rack_number.value_namespace_prefix = name_space_prefix
                                if(value_path == "slot-number"):
                                    self.slot_number = value
                                    self.slot_number.value_namespace = name_space
                                    self.slot_number.value_namespace_prefix = name_space_prefix
                                if(value_path == "valid"):
                                    self.valid = value
                                    self.valid.value_namespace = name_space
                                    self.valid.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.asic_statistics_detail_for_npu_id:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.asic_statistics_detail_for_npu_id:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "asic-statistics-detail-for-npu-ids" + path_buffer

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

                            if (child_yang_name == "asic-statistics-detail-for-npu-id"):
                                for c in self.asic_statistics_detail_for_npu_id:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.asic_statistics_detail_for_npu_id.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "asic-statistics-detail-for-npu-id"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (
                            (self.asic_statistics_detail_for_npu_ids is not None and self.asic_statistics_detail_for_npu_ids.has_data()) or
                            (self.asic_statistics_for_npu_ids is not None and self.asic_statistics_for_npu_ids.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.asic_statistics_detail_for_npu_ids is not None and self.asic_statistics_detail_for_npu_ids.has_operation()) or
                            (self.asic_statistics_for_npu_ids is not None and self.asic_statistics_for_npu_ids.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "asic-statistics" + path_buffer

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

                        if (child_yang_name == "asic-statistics-detail-for-npu-ids"):
                            if (self.asic_statistics_detail_for_npu_ids is None):
                                self.asic_statistics_detail_for_npu_ids = Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds()
                                self.asic_statistics_detail_for_npu_ids.parent = self
                                self._children_name_map["asic_statistics_detail_for_npu_ids"] = "asic-statistics-detail-for-npu-ids"
                            return self.asic_statistics_detail_for_npu_ids

                        if (child_yang_name == "asic-statistics-for-npu-ids"):
                            if (self.asic_statistics_for_npu_ids is None):
                                self.asic_statistics_for_npu_ids = Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsForNpuIds()
                                self.asic_statistics_for_npu_ids.parent = self
                                self._children_name_map["asic_statistics_for_npu_ids"] = "asic-statistics-for-npu-ids"
                            return self.asic_statistics_for_npu_ids

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "asic-statistics-detail-for-npu-ids" or name == "asic-statistics-for-npu-ids"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class NpuNumbers(Entity):
                    """
                    Ingress Stats
                    
                    .. attribute:: npu_number
                    
                    	Stats for a particular npu
                    	**type**\: list of    :py:class:`NpuNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_hw_resources_oper.Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber>`
                    
                    

                    """

                    _prefix = 'fretta-bcm-dpa-hw-resources-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Dpa.Stats.Nodes.Node.NpuNumbers, self).__init__()

                        self.yang_name = "npu-numbers"
                        self.yang_parent_name = "node"

                        self.npu_number = YList(self)

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
                                    super(Dpa.Stats.Nodes.Node.NpuNumbers, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Dpa.Stats.Nodes.Node.NpuNumbers, self).__setattr__(name, value)


                    class NpuNumber(Entity):
                        """
                        Stats for a particular npu
                        
                        .. attribute:: npu_id  <key>
                        
                        	Npu number
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: display
                        
                        	show npu specific voq or trap stats
                        	**type**\:   :py:class:`Display <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_hw_resources_oper.Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display>`
                        
                        

                        """

                        _prefix = 'fretta-bcm-dpa-hw-resources-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber, self).__init__()

                            self.yang_name = "npu-number"
                            self.yang_parent_name = "npu-numbers"

                            self.npu_id = YLeaf(YType.int32, "npu-id")

                            self.display = Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display()
                            self.display.parent = self
                            self._children_name_map["display"] = "display"
                            self._children_yang_names.add("display")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("npu_id") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber, self).__setattr__(name, value)


                        class Display(Entity):
                            """
                            show npu specific voq or trap stats
                            
                            .. attribute:: base_numbers
                            
                            	Voq stats grouped by voq base numbers
                            	**type**\:   :py:class:`BaseNumbers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_hw_resources_oper.Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.BaseNumbers>`
                            
                            .. attribute:: interface_handles
                            
                            	Voq stats grouped by interface handle
                            	**type**\:   :py:class:`InterfaceHandles <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_hw_resources_oper.Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.InterfaceHandles>`
                            
                            .. attribute:: trap_ids
                            
                            	Trap stats for a particular npu
                            	**type**\:   :py:class:`TrapIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_hw_resources_oper.Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.TrapIds>`
                            
                            

                            """

                            _prefix = 'fretta-bcm-dpa-hw-resources-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display, self).__init__()

                                self.yang_name = "display"
                                self.yang_parent_name = "npu-number"

                                self.base_numbers = Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.BaseNumbers()
                                self.base_numbers.parent = self
                                self._children_name_map["base_numbers"] = "base-numbers"
                                self._children_yang_names.add("base-numbers")

                                self.interface_handles = Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.InterfaceHandles()
                                self.interface_handles.parent = self
                                self._children_name_map["interface_handles"] = "interface-handles"
                                self._children_yang_names.add("interface-handles")

                                self.trap_ids = Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.TrapIds()
                                self.trap_ids.parent = self
                                self._children_name_map["trap_ids"] = "trap-ids"
                                self._children_yang_names.add("trap-ids")


                            class BaseNumbers(Entity):
                                """
                                Voq stats grouped by voq base numbers
                                
                                .. attribute:: base_number
                                
                                	Voq Base Number for a particular voq
                                	**type**\: list of    :py:class:`BaseNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_hw_resources_oper.Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.BaseNumbers.BaseNumber>`
                                
                                

                                """

                                _prefix = 'fretta-bcm-dpa-hw-resources-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.BaseNumbers, self).__init__()

                                    self.yang_name = "base-numbers"
                                    self.yang_parent_name = "display"

                                    self.base_number = YList(self)

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
                                                super(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.BaseNumbers, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.BaseNumbers, self).__setattr__(name, value)


                                class BaseNumber(Entity):
                                    """
                                    Voq Base Number for a particular voq
                                    
                                    .. attribute:: base_number  <key>
                                    
                                    	Interface handle
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: connector_id
                                    
                                    	Connector id of port
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: if_handle
                                    
                                    	IfHandle of port
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: in_use
                                    
                                    	Flag to indicate if port is in use
                                    	**type**\:  bool
                                    
                                    .. attribute:: is_local_port
                                    
                                    	Flag to indicate if port is local to the node
                                    	**type**\:  bool
                                    
                                    .. attribute:: npu_core
                                    
                                    	NPU core of port
                                    	**type**\:  int
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: npu_num
                                    
                                    	NPU of port
                                    	**type**\:  int
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: port_num
                                    
                                    	Port Number of port
                                    	**type**\:  int
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: port_speed
                                    
                                    	Port speed of port
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: pp_port
                                    
                                    	PP Port number of port
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: rack_num
                                    
                                    	Rack of port
                                    	**type**\:  int
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: slot_num
                                    
                                    	Slot of port
                                    	**type**\:  int
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: sys_port
                                    
                                    	System port of port
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: voq_base
                                    
                                    	Voq Base number of port
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: voq_stat
                                    
                                    	Keeps a record of the received and dropped packets and bytes on the port
                                    	**type**\: list of    :py:class:`VoqStat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_hw_resources_oper.Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.BaseNumbers.BaseNumber.VoqStat>`
                                    
                                    

                                    """

                                    _prefix = 'fretta-bcm-dpa-hw-resources-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.BaseNumbers.BaseNumber, self).__init__()

                                        self.yang_name = "base-number"
                                        self.yang_parent_name = "base-numbers"

                                        self.base_number = YLeaf(YType.uint32, "base-number")

                                        self.connector_id = YLeaf(YType.uint32, "connector-id")

                                        self.if_handle = YLeaf(YType.uint32, "if-handle")

                                        self.in_use = YLeaf(YType.boolean, "in-use")

                                        self.is_local_port = YLeaf(YType.boolean, "is-local-port")

                                        self.npu_core = YLeaf(YType.uint8, "npu-core")

                                        self.npu_num = YLeaf(YType.uint8, "npu-num")

                                        self.port_num = YLeaf(YType.uint8, "port-num")

                                        self.port_speed = YLeaf(YType.uint32, "port-speed")

                                        self.pp_port = YLeaf(YType.uint32, "pp-port")

                                        self.rack_num = YLeaf(YType.uint8, "rack-num")

                                        self.slot_num = YLeaf(YType.uint8, "slot-num")

                                        self.sys_port = YLeaf(YType.uint32, "sys-port")

                                        self.voq_base = YLeaf(YType.uint32, "voq-base")

                                        self.voq_stat = YList(self)

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("base_number",
                                                        "connector_id",
                                                        "if_handle",
                                                        "in_use",
                                                        "is_local_port",
                                                        "npu_core",
                                                        "npu_num",
                                                        "port_num",
                                                        "port_speed",
                                                        "pp_port",
                                                        "rack_num",
                                                        "slot_num",
                                                        "sys_port",
                                                        "voq_base") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.BaseNumbers.BaseNumber, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.BaseNumbers.BaseNumber, self).__setattr__(name, value)


                                    class VoqStat(Entity):
                                        """
                                        Keeps a record of the received and dropped
                                        packets and bytes on the port
                                        
                                        .. attribute:: dropped_bytes
                                        
                                        	Bytes Dropped on the port
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: dropped_packets
                                        
                                        	Packets Dropeed on the port
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: received_bytes
                                        
                                        	Bytes Received on the port
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: received_packets
                                        
                                        	Packets Received on the port
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        

                                        """

                                        _prefix = 'fretta-bcm-dpa-hw-resources-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.BaseNumbers.BaseNumber.VoqStat, self).__init__()

                                            self.yang_name = "voq-stat"
                                            self.yang_parent_name = "base-number"

                                            self.dropped_bytes = YLeaf(YType.uint64, "dropped-bytes")

                                            self.dropped_packets = YLeaf(YType.uint64, "dropped-packets")

                                            self.received_bytes = YLeaf(YType.uint64, "received-bytes")

                                            self.received_packets = YLeaf(YType.uint64, "received-packets")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("dropped_bytes",
                                                            "dropped_packets",
                                                            "received_bytes",
                                                            "received_packets") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.BaseNumbers.BaseNumber.VoqStat, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.BaseNumbers.BaseNumber.VoqStat, self).__setattr__(name, value)

                                        def has_data(self):
                                            return (
                                                self.dropped_bytes.is_set or
                                                self.dropped_packets.is_set or
                                                self.received_bytes.is_set or
                                                self.received_packets.is_set)

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.dropped_bytes.yfilter != YFilter.not_set or
                                                self.dropped_packets.yfilter != YFilter.not_set or
                                                self.received_bytes.yfilter != YFilter.not_set or
                                                self.received_packets.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "voq-stat" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.dropped_bytes.is_set or self.dropped_bytes.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.dropped_bytes.get_name_leafdata())
                                            if (self.dropped_packets.is_set or self.dropped_packets.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.dropped_packets.get_name_leafdata())
                                            if (self.received_bytes.is_set or self.received_bytes.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.received_bytes.get_name_leafdata())
                                            if (self.received_packets.is_set or self.received_packets.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.received_packets.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "dropped-bytes" or name == "dropped-packets" or name == "received-bytes" or name == "received-packets"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "dropped-bytes"):
                                                self.dropped_bytes = value
                                                self.dropped_bytes.value_namespace = name_space
                                                self.dropped_bytes.value_namespace_prefix = name_space_prefix
                                            if(value_path == "dropped-packets"):
                                                self.dropped_packets = value
                                                self.dropped_packets.value_namespace = name_space
                                                self.dropped_packets.value_namespace_prefix = name_space_prefix
                                            if(value_path == "received-bytes"):
                                                self.received_bytes = value
                                                self.received_bytes.value_namespace = name_space
                                                self.received_bytes.value_namespace_prefix = name_space_prefix
                                            if(value_path == "received-packets"):
                                                self.received_packets = value
                                                self.received_packets.value_namespace = name_space
                                                self.received_packets.value_namespace_prefix = name_space_prefix

                                    def has_data(self):
                                        for c in self.voq_stat:
                                            if (c.has_data()):
                                                return True
                                        return (
                                            self.base_number.is_set or
                                            self.connector_id.is_set or
                                            self.if_handle.is_set or
                                            self.in_use.is_set or
                                            self.is_local_port.is_set or
                                            self.npu_core.is_set or
                                            self.npu_num.is_set or
                                            self.port_num.is_set or
                                            self.port_speed.is_set or
                                            self.pp_port.is_set or
                                            self.rack_num.is_set or
                                            self.slot_num.is_set or
                                            self.sys_port.is_set or
                                            self.voq_base.is_set)

                                    def has_operation(self):
                                        for c in self.voq_stat:
                                            if (c.has_operation()):
                                                return True
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.base_number.yfilter != YFilter.not_set or
                                            self.connector_id.yfilter != YFilter.not_set or
                                            self.if_handle.yfilter != YFilter.not_set or
                                            self.in_use.yfilter != YFilter.not_set or
                                            self.is_local_port.yfilter != YFilter.not_set or
                                            self.npu_core.yfilter != YFilter.not_set or
                                            self.npu_num.yfilter != YFilter.not_set or
                                            self.port_num.yfilter != YFilter.not_set or
                                            self.port_speed.yfilter != YFilter.not_set or
                                            self.pp_port.yfilter != YFilter.not_set or
                                            self.rack_num.yfilter != YFilter.not_set or
                                            self.slot_num.yfilter != YFilter.not_set or
                                            self.sys_port.yfilter != YFilter.not_set or
                                            self.voq_base.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "base-number" + "[base-number='" + self.base_number.get() + "']" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.base_number.is_set or self.base_number.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.base_number.get_name_leafdata())
                                        if (self.connector_id.is_set or self.connector_id.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.connector_id.get_name_leafdata())
                                        if (self.if_handle.is_set or self.if_handle.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.if_handle.get_name_leafdata())
                                        if (self.in_use.is_set or self.in_use.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.in_use.get_name_leafdata())
                                        if (self.is_local_port.is_set or self.is_local_port.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.is_local_port.get_name_leafdata())
                                        if (self.npu_core.is_set or self.npu_core.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.npu_core.get_name_leafdata())
                                        if (self.npu_num.is_set or self.npu_num.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.npu_num.get_name_leafdata())
                                        if (self.port_num.is_set or self.port_num.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.port_num.get_name_leafdata())
                                        if (self.port_speed.is_set or self.port_speed.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.port_speed.get_name_leafdata())
                                        if (self.pp_port.is_set or self.pp_port.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.pp_port.get_name_leafdata())
                                        if (self.rack_num.is_set or self.rack_num.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.rack_num.get_name_leafdata())
                                        if (self.slot_num.is_set or self.slot_num.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.slot_num.get_name_leafdata())
                                        if (self.sys_port.is_set or self.sys_port.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.sys_port.get_name_leafdata())
                                        if (self.voq_base.is_set or self.voq_base.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.voq_base.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        if (child_yang_name == "voq-stat"):
                                            for c in self.voq_stat:
                                                segment = c.get_segment_path()
                                                if (segment_path == segment):
                                                    return c
                                            c = Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.BaseNumbers.BaseNumber.VoqStat()
                                            c.parent = self
                                            local_reference_key = "ydk::seg::%s" % segment_path
                                            self._local_refs[local_reference_key] = c
                                            self.voq_stat.append(c)
                                            return c

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "voq-stat" or name == "base-number" or name == "connector-id" or name == "if-handle" or name == "in-use" or name == "is-local-port" or name == "npu-core" or name == "npu-num" or name == "port-num" or name == "port-speed" or name == "pp-port" or name == "rack-num" or name == "slot-num" or name == "sys-port" or name == "voq-base"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "base-number"):
                                            self.base_number = value
                                            self.base_number.value_namespace = name_space
                                            self.base_number.value_namespace_prefix = name_space_prefix
                                        if(value_path == "connector-id"):
                                            self.connector_id = value
                                            self.connector_id.value_namespace = name_space
                                            self.connector_id.value_namespace_prefix = name_space_prefix
                                        if(value_path == "if-handle"):
                                            self.if_handle = value
                                            self.if_handle.value_namespace = name_space
                                            self.if_handle.value_namespace_prefix = name_space_prefix
                                        if(value_path == "in-use"):
                                            self.in_use = value
                                            self.in_use.value_namespace = name_space
                                            self.in_use.value_namespace_prefix = name_space_prefix
                                        if(value_path == "is-local-port"):
                                            self.is_local_port = value
                                            self.is_local_port.value_namespace = name_space
                                            self.is_local_port.value_namespace_prefix = name_space_prefix
                                        if(value_path == "npu-core"):
                                            self.npu_core = value
                                            self.npu_core.value_namespace = name_space
                                            self.npu_core.value_namespace_prefix = name_space_prefix
                                        if(value_path == "npu-num"):
                                            self.npu_num = value
                                            self.npu_num.value_namespace = name_space
                                            self.npu_num.value_namespace_prefix = name_space_prefix
                                        if(value_path == "port-num"):
                                            self.port_num = value
                                            self.port_num.value_namespace = name_space
                                            self.port_num.value_namespace_prefix = name_space_prefix
                                        if(value_path == "port-speed"):
                                            self.port_speed = value
                                            self.port_speed.value_namespace = name_space
                                            self.port_speed.value_namespace_prefix = name_space_prefix
                                        if(value_path == "pp-port"):
                                            self.pp_port = value
                                            self.pp_port.value_namespace = name_space
                                            self.pp_port.value_namespace_prefix = name_space_prefix
                                        if(value_path == "rack-num"):
                                            self.rack_num = value
                                            self.rack_num.value_namespace = name_space
                                            self.rack_num.value_namespace_prefix = name_space_prefix
                                        if(value_path == "slot-num"):
                                            self.slot_num = value
                                            self.slot_num.value_namespace = name_space
                                            self.slot_num.value_namespace_prefix = name_space_prefix
                                        if(value_path == "sys-port"):
                                            self.sys_port = value
                                            self.sys_port.value_namespace = name_space
                                            self.sys_port.value_namespace_prefix = name_space_prefix
                                        if(value_path == "voq-base"):
                                            self.voq_base = value
                                            self.voq_base.value_namespace = name_space
                                            self.voq_base.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    for c in self.base_number:
                                        if (c.has_data()):
                                            return True
                                    return False

                                def has_operation(self):
                                    for c in self.base_number:
                                        if (c.has_operation()):
                                            return True
                                    return self.yfilter != YFilter.not_set

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "base-numbers" + path_buffer

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

                                    if (child_yang_name == "base-number"):
                                        for c in self.base_number:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.BaseNumbers.BaseNumber()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.base_number.append(c)
                                        return c

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "base-number"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    pass


                            class TrapIds(Entity):
                                """
                                Trap stats for a particular npu
                                
                                .. attribute:: trap_id
                                
                                	Filter by specific trap id
                                	**type**\: list of    :py:class:`TrapId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_hw_resources_oper.Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.TrapIds.TrapId>`
                                
                                

                                """

                                _prefix = 'fretta-bcm-dpa-hw-resources-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.TrapIds, self).__init__()

                                    self.yang_name = "trap-ids"
                                    self.yang_parent_name = "display"

                                    self.trap_id = YList(self)

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
                                                super(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.TrapIds, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.TrapIds, self).__setattr__(name, value)


                                class TrapId(Entity):
                                    """
                                    Filter by specific trap id
                                    
                                    .. attribute:: trap_id  <key>
                                    
                                    	Trap ID
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: encap_id
                                    
                                    	Encap Id of the trap
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: fec_id
                                    
                                    	Fec id of the trap
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: gport
                                    
                                    	Gport of the trap
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: id
                                    
                                    	Id for internal use
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: mc_group
                                    
                                    	McGroup of the trap
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: npu_id
                                    
                                    	NpuId on which trap is enabled
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: offset
                                    
                                    	Offset for internal use
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: packet_accepted
                                    
                                    	Number of packets accepted after hitting the trap
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: packet_dropped
                                    
                                    	Number of packets dropped after hitting the trap
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: policer_id
                                    
                                    	Id of the policer on the trap
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: priority
                                    
                                    	Priority of the trap
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: stats_id
                                    
                                    	Stats Id of the trap
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: trap_id_xr
                                    
                                    	Id of the trap
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: trap_strength
                                    
                                    	Trap Strength of the trap
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: trap_string
                                    
                                    	Name String of the trap
                                    	**type**\:  str
                                    
                                    

                                    """

                                    _prefix = 'fretta-bcm-dpa-hw-resources-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.TrapIds.TrapId, self).__init__()

                                        self.yang_name = "trap-id"
                                        self.yang_parent_name = "trap-ids"

                                        self.trap_id = YLeaf(YType.uint32, "trap-id")

                                        self.encap_id = YLeaf(YType.uint32, "encap-id")

                                        self.fec_id = YLeaf(YType.uint32, "fec-id")

                                        self.gport = YLeaf(YType.uint32, "gport")

                                        self.id = YLeaf(YType.uint32, "id")

                                        self.mc_group = YLeaf(YType.uint32, "mc-group")

                                        self.npu_id = YLeaf(YType.uint64, "npu-id")

                                        self.offset = YLeaf(YType.uint64, "offset")

                                        self.packet_accepted = YLeaf(YType.uint64, "packet-accepted")

                                        self.packet_dropped = YLeaf(YType.uint64, "packet-dropped")

                                        self.policer_id = YLeaf(YType.uint32, "policer-id")

                                        self.priority = YLeaf(YType.uint32, "priority")

                                        self.stats_id = YLeaf(YType.uint32, "stats-id")

                                        self.trap_id_xr = YLeaf(YType.uint32, "trap-id-xr")

                                        self.trap_strength = YLeaf(YType.uint32, "trap-strength")

                                        self.trap_string = YLeaf(YType.str, "trap-string")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("trap_id",
                                                        "encap_id",
                                                        "fec_id",
                                                        "gport",
                                                        "id",
                                                        "mc_group",
                                                        "npu_id",
                                                        "offset",
                                                        "packet_accepted",
                                                        "packet_dropped",
                                                        "policer_id",
                                                        "priority",
                                                        "stats_id",
                                                        "trap_id_xr",
                                                        "trap_strength",
                                                        "trap_string") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.TrapIds.TrapId, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.TrapIds.TrapId, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.trap_id.is_set or
                                            self.encap_id.is_set or
                                            self.fec_id.is_set or
                                            self.gport.is_set or
                                            self.id.is_set or
                                            self.mc_group.is_set or
                                            self.npu_id.is_set or
                                            self.offset.is_set or
                                            self.packet_accepted.is_set or
                                            self.packet_dropped.is_set or
                                            self.policer_id.is_set or
                                            self.priority.is_set or
                                            self.stats_id.is_set or
                                            self.trap_id_xr.is_set or
                                            self.trap_strength.is_set or
                                            self.trap_string.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.trap_id.yfilter != YFilter.not_set or
                                            self.encap_id.yfilter != YFilter.not_set or
                                            self.fec_id.yfilter != YFilter.not_set or
                                            self.gport.yfilter != YFilter.not_set or
                                            self.id.yfilter != YFilter.not_set or
                                            self.mc_group.yfilter != YFilter.not_set or
                                            self.npu_id.yfilter != YFilter.not_set or
                                            self.offset.yfilter != YFilter.not_set or
                                            self.packet_accepted.yfilter != YFilter.not_set or
                                            self.packet_dropped.yfilter != YFilter.not_set or
                                            self.policer_id.yfilter != YFilter.not_set or
                                            self.priority.yfilter != YFilter.not_set or
                                            self.stats_id.yfilter != YFilter.not_set or
                                            self.trap_id_xr.yfilter != YFilter.not_set or
                                            self.trap_strength.yfilter != YFilter.not_set or
                                            self.trap_string.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "trap-id" + "[trap-id='" + self.trap_id.get() + "']" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.trap_id.is_set or self.trap_id.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.trap_id.get_name_leafdata())
                                        if (self.encap_id.is_set or self.encap_id.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.encap_id.get_name_leafdata())
                                        if (self.fec_id.is_set or self.fec_id.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.fec_id.get_name_leafdata())
                                        if (self.gport.is_set or self.gport.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.gport.get_name_leafdata())
                                        if (self.id.is_set or self.id.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.id.get_name_leafdata())
                                        if (self.mc_group.is_set or self.mc_group.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.mc_group.get_name_leafdata())
                                        if (self.npu_id.is_set or self.npu_id.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.npu_id.get_name_leafdata())
                                        if (self.offset.is_set or self.offset.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.offset.get_name_leafdata())
                                        if (self.packet_accepted.is_set or self.packet_accepted.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.packet_accepted.get_name_leafdata())
                                        if (self.packet_dropped.is_set or self.packet_dropped.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.packet_dropped.get_name_leafdata())
                                        if (self.policer_id.is_set or self.policer_id.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.policer_id.get_name_leafdata())
                                        if (self.priority.is_set or self.priority.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.priority.get_name_leafdata())
                                        if (self.stats_id.is_set or self.stats_id.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.stats_id.get_name_leafdata())
                                        if (self.trap_id_xr.is_set or self.trap_id_xr.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.trap_id_xr.get_name_leafdata())
                                        if (self.trap_strength.is_set or self.trap_strength.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.trap_strength.get_name_leafdata())
                                        if (self.trap_string.is_set or self.trap_string.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.trap_string.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "trap-id" or name == "encap-id" or name == "fec-id" or name == "gport" or name == "id" or name == "mc-group" or name == "npu-id" or name == "offset" or name == "packet-accepted" or name == "packet-dropped" or name == "policer-id" or name == "priority" or name == "stats-id" or name == "trap-id-xr" or name == "trap-strength" or name == "trap-string"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "trap-id"):
                                            self.trap_id = value
                                            self.trap_id.value_namespace = name_space
                                            self.trap_id.value_namespace_prefix = name_space_prefix
                                        if(value_path == "encap-id"):
                                            self.encap_id = value
                                            self.encap_id.value_namespace = name_space
                                            self.encap_id.value_namespace_prefix = name_space_prefix
                                        if(value_path == "fec-id"):
                                            self.fec_id = value
                                            self.fec_id.value_namespace = name_space
                                            self.fec_id.value_namespace_prefix = name_space_prefix
                                        if(value_path == "gport"):
                                            self.gport = value
                                            self.gport.value_namespace = name_space
                                            self.gport.value_namespace_prefix = name_space_prefix
                                        if(value_path == "id"):
                                            self.id = value
                                            self.id.value_namespace = name_space
                                            self.id.value_namespace_prefix = name_space_prefix
                                        if(value_path == "mc-group"):
                                            self.mc_group = value
                                            self.mc_group.value_namespace = name_space
                                            self.mc_group.value_namespace_prefix = name_space_prefix
                                        if(value_path == "npu-id"):
                                            self.npu_id = value
                                            self.npu_id.value_namespace = name_space
                                            self.npu_id.value_namespace_prefix = name_space_prefix
                                        if(value_path == "offset"):
                                            self.offset = value
                                            self.offset.value_namespace = name_space
                                            self.offset.value_namespace_prefix = name_space_prefix
                                        if(value_path == "packet-accepted"):
                                            self.packet_accepted = value
                                            self.packet_accepted.value_namespace = name_space
                                            self.packet_accepted.value_namespace_prefix = name_space_prefix
                                        if(value_path == "packet-dropped"):
                                            self.packet_dropped = value
                                            self.packet_dropped.value_namespace = name_space
                                            self.packet_dropped.value_namespace_prefix = name_space_prefix
                                        if(value_path == "policer-id"):
                                            self.policer_id = value
                                            self.policer_id.value_namespace = name_space
                                            self.policer_id.value_namespace_prefix = name_space_prefix
                                        if(value_path == "priority"):
                                            self.priority = value
                                            self.priority.value_namespace = name_space
                                            self.priority.value_namespace_prefix = name_space_prefix
                                        if(value_path == "stats-id"):
                                            self.stats_id = value
                                            self.stats_id.value_namespace = name_space
                                            self.stats_id.value_namespace_prefix = name_space_prefix
                                        if(value_path == "trap-id-xr"):
                                            self.trap_id_xr = value
                                            self.trap_id_xr.value_namespace = name_space
                                            self.trap_id_xr.value_namespace_prefix = name_space_prefix
                                        if(value_path == "trap-strength"):
                                            self.trap_strength = value
                                            self.trap_strength.value_namespace = name_space
                                            self.trap_strength.value_namespace_prefix = name_space_prefix
                                        if(value_path == "trap-string"):
                                            self.trap_string = value
                                            self.trap_string.value_namespace = name_space
                                            self.trap_string.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    for c in self.trap_id:
                                        if (c.has_data()):
                                            return True
                                    return False

                                def has_operation(self):
                                    for c in self.trap_id:
                                        if (c.has_operation()):
                                            return True
                                    return self.yfilter != YFilter.not_set

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "trap-ids" + path_buffer

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

                                    if (child_yang_name == "trap-id"):
                                        for c in self.trap_id:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.TrapIds.TrapId()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.trap_id.append(c)
                                        return c

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "trap-id"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    pass


                            class InterfaceHandles(Entity):
                                """
                                Voq stats grouped by interface handle
                                
                                .. attribute:: interface_handle
                                
                                	Voq stats for a particular interface handle
                                	**type**\: list of    :py:class:`InterfaceHandle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_hw_resources_oper.Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.InterfaceHandles.InterfaceHandle>`
                                
                                

                                """

                                _prefix = 'fretta-bcm-dpa-hw-resources-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.InterfaceHandles, self).__init__()

                                    self.yang_name = "interface-handles"
                                    self.yang_parent_name = "display"

                                    self.interface_handle = YList(self)

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
                                                super(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.InterfaceHandles, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.InterfaceHandles, self).__setattr__(name, value)


                                class InterfaceHandle(Entity):
                                    """
                                    Voq stats for a particular interface
                                    handle
                                    
                                    .. attribute:: interface_handle  <key>
                                    
                                    	Interface Handle
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: connector_id
                                    
                                    	Connector id of port
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: if_handle
                                    
                                    	IfHandle of port
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: in_use
                                    
                                    	Flag to indicate if port is in use
                                    	**type**\:  bool
                                    
                                    .. attribute:: is_local_port
                                    
                                    	Flag to indicate if port is local to the node
                                    	**type**\:  bool
                                    
                                    .. attribute:: npu_core
                                    
                                    	NPU core of port
                                    	**type**\:  int
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: npu_num
                                    
                                    	NPU of port
                                    	**type**\:  int
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: port_num
                                    
                                    	Port Number of port
                                    	**type**\:  int
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: port_speed
                                    
                                    	Port speed of port
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: pp_port
                                    
                                    	PP Port number of port
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: rack_num
                                    
                                    	Rack of port
                                    	**type**\:  int
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: slot_num
                                    
                                    	Slot of port
                                    	**type**\:  int
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: sys_port
                                    
                                    	System port of port
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: voq_base
                                    
                                    	Voq Base number of port
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: voq_stat
                                    
                                    	Keeps a record of the received and dropped packets and bytes on the port
                                    	**type**\: list of    :py:class:`VoqStat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_hw_resources_oper.Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.InterfaceHandles.InterfaceHandle.VoqStat>`
                                    
                                    

                                    """

                                    _prefix = 'fretta-bcm-dpa-hw-resources-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.InterfaceHandles.InterfaceHandle, self).__init__()

                                        self.yang_name = "interface-handle"
                                        self.yang_parent_name = "interface-handles"

                                        self.interface_handle = YLeaf(YType.uint32, "interface-handle")

                                        self.connector_id = YLeaf(YType.uint32, "connector-id")

                                        self.if_handle = YLeaf(YType.uint32, "if-handle")

                                        self.in_use = YLeaf(YType.boolean, "in-use")

                                        self.is_local_port = YLeaf(YType.boolean, "is-local-port")

                                        self.npu_core = YLeaf(YType.uint8, "npu-core")

                                        self.npu_num = YLeaf(YType.uint8, "npu-num")

                                        self.port_num = YLeaf(YType.uint8, "port-num")

                                        self.port_speed = YLeaf(YType.uint32, "port-speed")

                                        self.pp_port = YLeaf(YType.uint32, "pp-port")

                                        self.rack_num = YLeaf(YType.uint8, "rack-num")

                                        self.slot_num = YLeaf(YType.uint8, "slot-num")

                                        self.sys_port = YLeaf(YType.uint32, "sys-port")

                                        self.voq_base = YLeaf(YType.uint32, "voq-base")

                                        self.voq_stat = YList(self)

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("interface_handle",
                                                        "connector_id",
                                                        "if_handle",
                                                        "in_use",
                                                        "is_local_port",
                                                        "npu_core",
                                                        "npu_num",
                                                        "port_num",
                                                        "port_speed",
                                                        "pp_port",
                                                        "rack_num",
                                                        "slot_num",
                                                        "sys_port",
                                                        "voq_base") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.InterfaceHandles.InterfaceHandle, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.InterfaceHandles.InterfaceHandle, self).__setattr__(name, value)


                                    class VoqStat(Entity):
                                        """
                                        Keeps a record of the received and dropped
                                        packets and bytes on the port
                                        
                                        .. attribute:: dropped_bytes
                                        
                                        	Bytes Dropped on the port
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: dropped_packets
                                        
                                        	Packets Dropeed on the port
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: received_bytes
                                        
                                        	Bytes Received on the port
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: received_packets
                                        
                                        	Packets Received on the port
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        

                                        """

                                        _prefix = 'fretta-bcm-dpa-hw-resources-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.InterfaceHandles.InterfaceHandle.VoqStat, self).__init__()

                                            self.yang_name = "voq-stat"
                                            self.yang_parent_name = "interface-handle"

                                            self.dropped_bytes = YLeaf(YType.uint64, "dropped-bytes")

                                            self.dropped_packets = YLeaf(YType.uint64, "dropped-packets")

                                            self.received_bytes = YLeaf(YType.uint64, "received-bytes")

                                            self.received_packets = YLeaf(YType.uint64, "received-packets")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("dropped_bytes",
                                                            "dropped_packets",
                                                            "received_bytes",
                                                            "received_packets") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.InterfaceHandles.InterfaceHandle.VoqStat, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.InterfaceHandles.InterfaceHandle.VoqStat, self).__setattr__(name, value)

                                        def has_data(self):
                                            return (
                                                self.dropped_bytes.is_set or
                                                self.dropped_packets.is_set or
                                                self.received_bytes.is_set or
                                                self.received_packets.is_set)

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.dropped_bytes.yfilter != YFilter.not_set or
                                                self.dropped_packets.yfilter != YFilter.not_set or
                                                self.received_bytes.yfilter != YFilter.not_set or
                                                self.received_packets.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "voq-stat" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.dropped_bytes.is_set or self.dropped_bytes.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.dropped_bytes.get_name_leafdata())
                                            if (self.dropped_packets.is_set or self.dropped_packets.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.dropped_packets.get_name_leafdata())
                                            if (self.received_bytes.is_set or self.received_bytes.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.received_bytes.get_name_leafdata())
                                            if (self.received_packets.is_set or self.received_packets.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.received_packets.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "dropped-bytes" or name == "dropped-packets" or name == "received-bytes" or name == "received-packets"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "dropped-bytes"):
                                                self.dropped_bytes = value
                                                self.dropped_bytes.value_namespace = name_space
                                                self.dropped_bytes.value_namespace_prefix = name_space_prefix
                                            if(value_path == "dropped-packets"):
                                                self.dropped_packets = value
                                                self.dropped_packets.value_namespace = name_space
                                                self.dropped_packets.value_namespace_prefix = name_space_prefix
                                            if(value_path == "received-bytes"):
                                                self.received_bytes = value
                                                self.received_bytes.value_namespace = name_space
                                                self.received_bytes.value_namespace_prefix = name_space_prefix
                                            if(value_path == "received-packets"):
                                                self.received_packets = value
                                                self.received_packets.value_namespace = name_space
                                                self.received_packets.value_namespace_prefix = name_space_prefix

                                    def has_data(self):
                                        for c in self.voq_stat:
                                            if (c.has_data()):
                                                return True
                                        return (
                                            self.interface_handle.is_set or
                                            self.connector_id.is_set or
                                            self.if_handle.is_set or
                                            self.in_use.is_set or
                                            self.is_local_port.is_set or
                                            self.npu_core.is_set or
                                            self.npu_num.is_set or
                                            self.port_num.is_set or
                                            self.port_speed.is_set or
                                            self.pp_port.is_set or
                                            self.rack_num.is_set or
                                            self.slot_num.is_set or
                                            self.sys_port.is_set or
                                            self.voq_base.is_set)

                                    def has_operation(self):
                                        for c in self.voq_stat:
                                            if (c.has_operation()):
                                                return True
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.interface_handle.yfilter != YFilter.not_set or
                                            self.connector_id.yfilter != YFilter.not_set or
                                            self.if_handle.yfilter != YFilter.not_set or
                                            self.in_use.yfilter != YFilter.not_set or
                                            self.is_local_port.yfilter != YFilter.not_set or
                                            self.npu_core.yfilter != YFilter.not_set or
                                            self.npu_num.yfilter != YFilter.not_set or
                                            self.port_num.yfilter != YFilter.not_set or
                                            self.port_speed.yfilter != YFilter.not_set or
                                            self.pp_port.yfilter != YFilter.not_set or
                                            self.rack_num.yfilter != YFilter.not_set or
                                            self.slot_num.yfilter != YFilter.not_set or
                                            self.sys_port.yfilter != YFilter.not_set or
                                            self.voq_base.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "interface-handle" + "[interface-handle='" + self.interface_handle.get() + "']" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.interface_handle.is_set or self.interface_handle.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.interface_handle.get_name_leafdata())
                                        if (self.connector_id.is_set or self.connector_id.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.connector_id.get_name_leafdata())
                                        if (self.if_handle.is_set or self.if_handle.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.if_handle.get_name_leafdata())
                                        if (self.in_use.is_set or self.in_use.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.in_use.get_name_leafdata())
                                        if (self.is_local_port.is_set or self.is_local_port.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.is_local_port.get_name_leafdata())
                                        if (self.npu_core.is_set or self.npu_core.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.npu_core.get_name_leafdata())
                                        if (self.npu_num.is_set or self.npu_num.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.npu_num.get_name_leafdata())
                                        if (self.port_num.is_set or self.port_num.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.port_num.get_name_leafdata())
                                        if (self.port_speed.is_set or self.port_speed.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.port_speed.get_name_leafdata())
                                        if (self.pp_port.is_set or self.pp_port.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.pp_port.get_name_leafdata())
                                        if (self.rack_num.is_set or self.rack_num.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.rack_num.get_name_leafdata())
                                        if (self.slot_num.is_set or self.slot_num.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.slot_num.get_name_leafdata())
                                        if (self.sys_port.is_set or self.sys_port.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.sys_port.get_name_leafdata())
                                        if (self.voq_base.is_set or self.voq_base.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.voq_base.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        if (child_yang_name == "voq-stat"):
                                            for c in self.voq_stat:
                                                segment = c.get_segment_path()
                                                if (segment_path == segment):
                                                    return c
                                            c = Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.InterfaceHandles.InterfaceHandle.VoqStat()
                                            c.parent = self
                                            local_reference_key = "ydk::seg::%s" % segment_path
                                            self._local_refs[local_reference_key] = c
                                            self.voq_stat.append(c)
                                            return c

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "voq-stat" or name == "interface-handle" or name == "connector-id" or name == "if-handle" or name == "in-use" or name == "is-local-port" or name == "npu-core" or name == "npu-num" or name == "port-num" or name == "port-speed" or name == "pp-port" or name == "rack-num" or name == "slot-num" or name == "sys-port" or name == "voq-base"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "interface-handle"):
                                            self.interface_handle = value
                                            self.interface_handle.value_namespace = name_space
                                            self.interface_handle.value_namespace_prefix = name_space_prefix
                                        if(value_path == "connector-id"):
                                            self.connector_id = value
                                            self.connector_id.value_namespace = name_space
                                            self.connector_id.value_namespace_prefix = name_space_prefix
                                        if(value_path == "if-handle"):
                                            self.if_handle = value
                                            self.if_handle.value_namespace = name_space
                                            self.if_handle.value_namespace_prefix = name_space_prefix
                                        if(value_path == "in-use"):
                                            self.in_use = value
                                            self.in_use.value_namespace = name_space
                                            self.in_use.value_namespace_prefix = name_space_prefix
                                        if(value_path == "is-local-port"):
                                            self.is_local_port = value
                                            self.is_local_port.value_namespace = name_space
                                            self.is_local_port.value_namespace_prefix = name_space_prefix
                                        if(value_path == "npu-core"):
                                            self.npu_core = value
                                            self.npu_core.value_namespace = name_space
                                            self.npu_core.value_namespace_prefix = name_space_prefix
                                        if(value_path == "npu-num"):
                                            self.npu_num = value
                                            self.npu_num.value_namespace = name_space
                                            self.npu_num.value_namespace_prefix = name_space_prefix
                                        if(value_path == "port-num"):
                                            self.port_num = value
                                            self.port_num.value_namespace = name_space
                                            self.port_num.value_namespace_prefix = name_space_prefix
                                        if(value_path == "port-speed"):
                                            self.port_speed = value
                                            self.port_speed.value_namespace = name_space
                                            self.port_speed.value_namespace_prefix = name_space_prefix
                                        if(value_path == "pp-port"):
                                            self.pp_port = value
                                            self.pp_port.value_namespace = name_space
                                            self.pp_port.value_namespace_prefix = name_space_prefix
                                        if(value_path == "rack-num"):
                                            self.rack_num = value
                                            self.rack_num.value_namespace = name_space
                                            self.rack_num.value_namespace_prefix = name_space_prefix
                                        if(value_path == "slot-num"):
                                            self.slot_num = value
                                            self.slot_num.value_namespace = name_space
                                            self.slot_num.value_namespace_prefix = name_space_prefix
                                        if(value_path == "sys-port"):
                                            self.sys_port = value
                                            self.sys_port.value_namespace = name_space
                                            self.sys_port.value_namespace_prefix = name_space_prefix
                                        if(value_path == "voq-base"):
                                            self.voq_base = value
                                            self.voq_base.value_namespace = name_space
                                            self.voq_base.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    for c in self.interface_handle:
                                        if (c.has_data()):
                                            return True
                                    return False

                                def has_operation(self):
                                    for c in self.interface_handle:
                                        if (c.has_operation()):
                                            return True
                                    return self.yfilter != YFilter.not_set

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "interface-handles" + path_buffer

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

                                    if (child_yang_name == "interface-handle"):
                                        for c in self.interface_handle:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.InterfaceHandles.InterfaceHandle()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.interface_handle.append(c)
                                        return c

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "interface-handle"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    pass

                            def has_data(self):
                                return (
                                    (self.base_numbers is not None and self.base_numbers.has_data()) or
                                    (self.interface_handles is not None and self.interface_handles.has_data()) or
                                    (self.trap_ids is not None and self.trap_ids.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    (self.base_numbers is not None and self.base_numbers.has_operation()) or
                                    (self.interface_handles is not None and self.interface_handles.has_operation()) or
                                    (self.trap_ids is not None and self.trap_ids.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "display" + path_buffer

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

                                if (child_yang_name == "base-numbers"):
                                    if (self.base_numbers is None):
                                        self.base_numbers = Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.BaseNumbers()
                                        self.base_numbers.parent = self
                                        self._children_name_map["base_numbers"] = "base-numbers"
                                    return self.base_numbers

                                if (child_yang_name == "interface-handles"):
                                    if (self.interface_handles is None):
                                        self.interface_handles = Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.InterfaceHandles()
                                        self.interface_handles.parent = self
                                        self._children_name_map["interface_handles"] = "interface-handles"
                                    return self.interface_handles

                                if (child_yang_name == "trap-ids"):
                                    if (self.trap_ids is None):
                                        self.trap_ids = Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.TrapIds()
                                        self.trap_ids.parent = self
                                        self._children_name_map["trap_ids"] = "trap-ids"
                                    return self.trap_ids

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "base-numbers" or name == "interface-handles" or name == "trap-ids"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass

                        def has_data(self):
                            return (
                                self.npu_id.is_set or
                                (self.display is not None and self.display.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.npu_id.yfilter != YFilter.not_set or
                                (self.display is not None and self.display.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "npu-number" + "[npu-id='" + self.npu_id.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.npu_id.is_set or self.npu_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.npu_id.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "display"):
                                if (self.display is None):
                                    self.display = Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display()
                                    self.display.parent = self
                                    self._children_name_map["display"] = "display"
                                return self.display

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "display" or name == "npu-id"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "npu-id"):
                                self.npu_id = value
                                self.npu_id.value_namespace = name_space
                                self.npu_id.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.npu_number:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.npu_number:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "npu-numbers" + path_buffer

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

                        if (child_yang_name == "npu-number"):
                            for c in self.npu_number:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.npu_number.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "npu-number"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class NpuIds(Entity):
                    """
                    DPA stats hw resources info 
                    
                    .. attribute:: npu_id
                    
                    	Stats Hardware Info for particular NPU
                    	**type**\: list of    :py:class:`NpuId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_hw_resources_oper.Dpa.Stats.Nodes.Node.NpuIds.NpuId>`
                    
                    

                    """

                    _prefix = 'fretta-bcm-dpa-hw-resources-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Dpa.Stats.Nodes.Node.NpuIds, self).__init__()

                        self.yang_name = "npu-ids"
                        self.yang_parent_name = "node"

                        self.npu_id = YList(self)

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
                                    super(Dpa.Stats.Nodes.Node.NpuIds, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Dpa.Stats.Nodes.Node.NpuIds, self).__setattr__(name, value)


                    class NpuId(Entity):
                        """
                        Stats Hardware Info for particular NPU
                        
                        .. attribute:: npu_id  <key>
                        
                        	NPU number
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: cntr_engine
                        
                        	cntr engine
                        	**type**\: list of    :py:class:`CntrEngine <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_hw_resources_oper.Dpa.Stats.Nodes.Node.NpuIds.NpuId.CntrEngine>`
                        
                        .. attribute:: next_avail_cp_id
                        
                        	next avail cp id
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: num_cntr_engines
                        
                        	num cntr engines
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sys_cp_cnfg_prof
                        
                        	sys cp cnfg prof
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'fretta-bcm-dpa-hw-resources-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Dpa.Stats.Nodes.Node.NpuIds.NpuId, self).__init__()

                            self.yang_name = "npu-id"
                            self.yang_parent_name = "npu-ids"

                            self.npu_id = YLeaf(YType.int32, "npu-id")

                            self.next_avail_cp_id = YLeaf(YType.uint32, "next-avail-cp-id")

                            self.num_cntr_engines = YLeaf(YType.uint32, "num-cntr-engines")

                            self.sys_cp_cnfg_prof = YLeaf(YType.uint32, "sys-cp-cnfg-prof")

                            self.cntr_engine = YList(self)

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("npu_id",
                                            "next_avail_cp_id",
                                            "num_cntr_engines",
                                            "sys_cp_cnfg_prof") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Dpa.Stats.Nodes.Node.NpuIds.NpuId, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Dpa.Stats.Nodes.Node.NpuIds.NpuId, self).__setattr__(name, value)


                        class CntrEngine(Entity):
                            """
                            cntr engine
                            
                            .. attribute:: apps_info
                            
                            	apps info
                            	**type**\: list of    :py:class:`AppsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_hw_resources_oper.Dpa.Stats.Nodes.Node.NpuIds.NpuId.CntrEngine.AppsInfo>`
                            
                            .. attribute:: core_id
                            
                            	core id
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: state
                            
                            	state
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'fretta-bcm-dpa-hw-resources-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dpa.Stats.Nodes.Node.NpuIds.NpuId.CntrEngine, self).__init__()

                                self.yang_name = "cntr-engine"
                                self.yang_parent_name = "npu-id"

                                self.core_id = YLeaf(YType.uint32, "core-id")

                                self.state = YLeaf(YType.uint32, "state")

                                self.apps_info = YList(self)

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("core_id",
                                                "state") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Dpa.Stats.Nodes.Node.NpuIds.NpuId.CntrEngine, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Dpa.Stats.Nodes.Node.NpuIds.NpuId.CntrEngine, self).__setattr__(name, value)


                            class AppsInfo(Entity):
                                """
                                apps info
                                
                                .. attribute:: app_type
                                
                                	app type
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: num_cntrs_for_app
                                
                                	num cntrs for app
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: num_cntrs_used
                                
                                	num cntrs used
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'fretta-bcm-dpa-hw-resources-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dpa.Stats.Nodes.Node.NpuIds.NpuId.CntrEngine.AppsInfo, self).__init__()

                                    self.yang_name = "apps-info"
                                    self.yang_parent_name = "cntr-engine"

                                    self.app_type = YLeaf(YType.uint32, "app-type")

                                    self.num_cntrs_for_app = YLeaf(YType.uint32, "num-cntrs-for-app")

                                    self.num_cntrs_used = YLeaf(YType.uint32, "num-cntrs-used")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("app_type",
                                                    "num_cntrs_for_app",
                                                    "num_cntrs_used") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Dpa.Stats.Nodes.Node.NpuIds.NpuId.CntrEngine.AppsInfo, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Dpa.Stats.Nodes.Node.NpuIds.NpuId.CntrEngine.AppsInfo, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.app_type.is_set or
                                        self.num_cntrs_for_app.is_set or
                                        self.num_cntrs_used.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.app_type.yfilter != YFilter.not_set or
                                        self.num_cntrs_for_app.yfilter != YFilter.not_set or
                                        self.num_cntrs_used.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "apps-info" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.app_type.is_set or self.app_type.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.app_type.get_name_leafdata())
                                    if (self.num_cntrs_for_app.is_set or self.num_cntrs_for_app.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.num_cntrs_for_app.get_name_leafdata())
                                    if (self.num_cntrs_used.is_set or self.num_cntrs_used.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.num_cntrs_used.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "app-type" or name == "num-cntrs-for-app" or name == "num-cntrs-used"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "app-type"):
                                        self.app_type = value
                                        self.app_type.value_namespace = name_space
                                        self.app_type.value_namespace_prefix = name_space_prefix
                                    if(value_path == "num-cntrs-for-app"):
                                        self.num_cntrs_for_app = value
                                        self.num_cntrs_for_app.value_namespace = name_space
                                        self.num_cntrs_for_app.value_namespace_prefix = name_space_prefix
                                    if(value_path == "num-cntrs-used"):
                                        self.num_cntrs_used = value
                                        self.num_cntrs_used.value_namespace = name_space
                                        self.num_cntrs_used.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                for c in self.apps_info:
                                    if (c.has_data()):
                                        return True
                                return (
                                    self.core_id.is_set or
                                    self.state.is_set)

                            def has_operation(self):
                                for c in self.apps_info:
                                    if (c.has_operation()):
                                        return True
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.core_id.yfilter != YFilter.not_set or
                                    self.state.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "cntr-engine" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.core_id.is_set or self.core_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.core_id.get_name_leafdata())
                                if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.state.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "apps-info"):
                                    for c in self.apps_info:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = Dpa.Stats.Nodes.Node.NpuIds.NpuId.CntrEngine.AppsInfo()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.apps_info.append(c)
                                    return c

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "apps-info" or name == "core-id" or name == "state"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "core-id"):
                                    self.core_id = value
                                    self.core_id.value_namespace = name_space
                                    self.core_id.value_namespace_prefix = name_space_prefix
                                if(value_path == "state"):
                                    self.state = value
                                    self.state.value_namespace = name_space
                                    self.state.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.cntr_engine:
                                if (c.has_data()):
                                    return True
                            return (
                                self.npu_id.is_set or
                                self.next_avail_cp_id.is_set or
                                self.num_cntr_engines.is_set or
                                self.sys_cp_cnfg_prof.is_set)

                        def has_operation(self):
                            for c in self.cntr_engine:
                                if (c.has_operation()):
                                    return True
                            return (
                                self.yfilter != YFilter.not_set or
                                self.npu_id.yfilter != YFilter.not_set or
                                self.next_avail_cp_id.yfilter != YFilter.not_set or
                                self.num_cntr_engines.yfilter != YFilter.not_set or
                                self.sys_cp_cnfg_prof.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "npu-id" + "[npu-id='" + self.npu_id.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.npu_id.is_set or self.npu_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.npu_id.get_name_leafdata())
                            if (self.next_avail_cp_id.is_set or self.next_avail_cp_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.next_avail_cp_id.get_name_leafdata())
                            if (self.num_cntr_engines.is_set or self.num_cntr_engines.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.num_cntr_engines.get_name_leafdata())
                            if (self.sys_cp_cnfg_prof.is_set or self.sys_cp_cnfg_prof.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.sys_cp_cnfg_prof.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "cntr-engine"):
                                for c in self.cntr_engine:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Dpa.Stats.Nodes.Node.NpuIds.NpuId.CntrEngine()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.cntr_engine.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "cntr-engine" or name == "npu-id" or name == "next-avail-cp-id" or name == "num-cntr-engines" or name == "sys-cp-cnfg-prof"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "npu-id"):
                                self.npu_id = value
                                self.npu_id.value_namespace = name_space
                                self.npu_id.value_namespace_prefix = name_space_prefix
                            if(value_path == "next-avail-cp-id"):
                                self.next_avail_cp_id = value
                                self.next_avail_cp_id.value_namespace = name_space
                                self.next_avail_cp_id.value_namespace_prefix = name_space_prefix
                            if(value_path == "num-cntr-engines"):
                                self.num_cntr_engines = value
                                self.num_cntr_engines.value_namespace = name_space
                                self.num_cntr_engines.value_namespace_prefix = name_space_prefix
                            if(value_path == "sys-cp-cnfg-prof"):
                                self.sys_cp_cnfg_prof = value
                                self.sys_cp_cnfg_prof.value_namespace = name_space
                                self.sys_cp_cnfg_prof.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.npu_id:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.npu_id:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "npu-ids" + path_buffer

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

                        if (child_yang_name == "npu-id"):
                            for c in self.npu_id:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Dpa.Stats.Nodes.Node.NpuIds.NpuId()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.npu_id.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "npu-id"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        self.node_name.is_set or
                        (self.asic_statistics is not None and self.asic_statistics.has_data()) or
                        (self.hw_resources_datas is not None and self.hw_resources_datas.has_data()) or
                        (self.npu_ids is not None and self.npu_ids.has_data()) or
                        (self.npu_numbers is not None and self.npu_numbers.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.node_name.yfilter != YFilter.not_set or
                        (self.asic_statistics is not None and self.asic_statistics.has_operation()) or
                        (self.hw_resources_datas is not None and self.hw_resources_datas.has_operation()) or
                        (self.npu_ids is not None and self.npu_ids.has_operation()) or
                        (self.npu_numbers is not None and self.npu_numbers.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "node" + "[node-name='" + self.node_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-fretta-bcm-dpa-hw-resources-oper:dpa/stats/nodes/%s" % self.get_segment_path()
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

                    if (child_yang_name == "asic-statistics"):
                        if (self.asic_statistics is None):
                            self.asic_statistics = Dpa.Stats.Nodes.Node.AsicStatistics()
                            self.asic_statistics.parent = self
                            self._children_name_map["asic_statistics"] = "asic-statistics"
                        return self.asic_statistics

                    if (child_yang_name == "hw-resources-datas"):
                        if (self.hw_resources_datas is None):
                            self.hw_resources_datas = Dpa.Stats.Nodes.Node.HwResourcesDatas()
                            self.hw_resources_datas.parent = self
                            self._children_name_map["hw_resources_datas"] = "hw-resources-datas"
                        return self.hw_resources_datas

                    if (child_yang_name == "npu-ids"):
                        if (self.npu_ids is None):
                            self.npu_ids = Dpa.Stats.Nodes.Node.NpuIds()
                            self.npu_ids.parent = self
                            self._children_name_map["npu_ids"] = "npu-ids"
                        return self.npu_ids

                    if (child_yang_name == "npu-numbers"):
                        if (self.npu_numbers is None):
                            self.npu_numbers = Dpa.Stats.Nodes.Node.NpuNumbers()
                            self.npu_numbers.parent = self
                            self._children_name_map["npu_numbers"] = "npu-numbers"
                        return self.npu_numbers

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "asic-statistics" or name == "hw-resources-datas" or name == "npu-ids" or name == "npu-numbers" or name == "node-name"):
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
                    path_buffer = "Cisco-IOS-XR-fretta-bcm-dpa-hw-resources-oper:dpa/stats/%s" % self.get_segment_path()
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
                    c = Dpa.Stats.Nodes.Node()
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
            path_buffer = "stats" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-fretta-bcm-dpa-hw-resources-oper:dpa/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "nodes"):
                if (self.nodes is None):
                    self.nodes = Dpa.Stats.Nodes()
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

    def has_data(self):
        return (self.stats is not None and self.stats.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.stats is not None and self.stats.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-fretta-bcm-dpa-hw-resources-oper:dpa" + path_buffer

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

        if (child_yang_name == "stats"):
            if (self.stats is None):
                self.stats = Dpa.Stats()
                self.stats.parent = self
                self._children_name_map["stats"] = "stats"
            return self.stats

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "stats"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Dpa()
        return self._top_entity

