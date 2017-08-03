""" Cisco_IOS_XR_ncs5500_coherent_node_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ncs5500\-coherent\-node package operational data.

This module contains definitions
for the following management objects\:
  coherent\: Coherent node  operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Coherent(Entity):
    """
    Coherent node  operational data
    
    .. attribute:: nodes
    
    	Coherent list of nodes
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes>`
    
    

    """

    _prefix = 'ncs5500-coherent-node-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Coherent, self).__init__()
        self._top_entity = None

        self.yang_name = "coherent"
        self.yang_parent_name = "Cisco-IOS-XR-ncs5500-coherent-node-oper"

        self.nodes = Coherent.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")


    class Nodes(Entity):
        """
        Coherent list of nodes
        
        .. attribute:: node
        
        	Coherent discovery operational data for a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node>`
        
        

        """

        _prefix = 'ncs5500-coherent-node-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Coherent.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "coherent"

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
                        super(Coherent.Nodes, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Coherent.Nodes, self).__setattr__(name, value)


        class Node(Entity):
            """
            Coherent discovery operational data for a
            particular node
            
            .. attribute:: node_name  <key>
            
            	The node name
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: coherent_time_stats
            
            	Coherent driver performace information
            	**type**\:   :py:class:`CoherentTimeStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.CoherentTimeStats>`
            
            .. attribute:: coherenthealth
            
            	Coherent node data for driver health
            	**type**\:   :py:class:`Coherenthealth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.Coherenthealth>`
            
            .. attribute:: devicemapping
            
            	Coherent node data for device \_mapping
            	**type**\:   :py:class:`Devicemapping <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.Devicemapping>`
            
            .. attribute:: port_mode_all_info
            
            	PortMode all operational data
            	**type**\:   :py:class:`PortModeAllInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.PortModeAllInfo>`
            
            

            """

            _prefix = 'ncs5500-coherent-node-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Coherent.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"

                self.node_name = YLeaf(YType.str, "node-name")

                self.coherent_time_stats = Coherent.Nodes.Node.CoherentTimeStats()
                self.coherent_time_stats.parent = self
                self._children_name_map["coherent_time_stats"] = "coherent-time-stats"
                self._children_yang_names.add("coherent-time-stats")

                self.coherenthealth = Coherent.Nodes.Node.Coherenthealth()
                self.coherenthealth.parent = self
                self._children_name_map["coherenthealth"] = "coherenthealth"
                self._children_yang_names.add("coherenthealth")

                self.devicemapping = Coherent.Nodes.Node.Devicemapping()
                self.devicemapping.parent = self
                self._children_name_map["devicemapping"] = "devicemapping"
                self._children_yang_names.add("devicemapping")

                self.port_mode_all_info = Coherent.Nodes.Node.PortModeAllInfo()
                self.port_mode_all_info.parent = self
                self._children_name_map["port_mode_all_info"] = "port-mode-all-info"
                self._children_yang_names.add("port-mode-all-info")

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
                            super(Coherent.Nodes.Node, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Coherent.Nodes.Node, self).__setattr__(name, value)


            class CoherentTimeStats(Entity):
                """
                Coherent driver performace information
                
                .. attribute:: device_created
                
                	device created
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: driver_init
                
                	driver init
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: driver_operational
                
                	driver operational
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: dsp_controllers_created
                
                	dsp controllers created
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: dsp_ea_bulk_create
                
                	dsp ea bulk create
                	**type**\:   :py:class:`DspEaBulkCreate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.CoherentTimeStats.DspEaBulkCreate>`
                
                .. attribute:: dsp_ea_bulk_update
                
                	dsp ea bulk update
                	**type**\:   :py:class:`DspEaBulkUpdate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.CoherentTimeStats.DspEaBulkUpdate>`
                
                .. attribute:: eth_intf_created
                
                	eth intf created
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: optics_controllers_created
                
                	optics controllers created
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: opts_ea_bulk_create
                
                	opts ea bulk create
                	**type**\:   :py:class:`OptsEaBulkCreate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.CoherentTimeStats.OptsEaBulkCreate>`
                
                .. attribute:: opts_ea_bulk_update
                
                	opts ea bulk update
                	**type**\:   :py:class:`OptsEaBulkUpdate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.CoherentTimeStats.OptsEaBulkUpdate>`
                
                .. attribute:: port_stat
                
                	port stat
                	**type**\: list of    :py:class:`PortStat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.CoherentTimeStats.PortStat>`
                
                

                """

                _prefix = 'ncs5500-coherent-node-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Coherent.Nodes.Node.CoherentTimeStats, self).__init__()

                    self.yang_name = "coherent-time-stats"
                    self.yang_parent_name = "node"

                    self.device_created = YLeaf(YType.str, "device-created")

                    self.driver_init = YLeaf(YType.str, "driver-init")

                    self.driver_operational = YLeaf(YType.str, "driver-operational")

                    self.dsp_controllers_created = YLeaf(YType.str, "dsp-controllers-created")

                    self.eth_intf_created = YLeaf(YType.str, "eth-intf-created")

                    self.optics_controllers_created = YLeaf(YType.str, "optics-controllers-created")

                    self.dsp_ea_bulk_create = Coherent.Nodes.Node.CoherentTimeStats.DspEaBulkCreate()
                    self.dsp_ea_bulk_create.parent = self
                    self._children_name_map["dsp_ea_bulk_create"] = "dsp-ea-bulk-create"
                    self._children_yang_names.add("dsp-ea-bulk-create")

                    self.dsp_ea_bulk_update = Coherent.Nodes.Node.CoherentTimeStats.DspEaBulkUpdate()
                    self.dsp_ea_bulk_update.parent = self
                    self._children_name_map["dsp_ea_bulk_update"] = "dsp-ea-bulk-update"
                    self._children_yang_names.add("dsp-ea-bulk-update")

                    self.opts_ea_bulk_create = Coherent.Nodes.Node.CoherentTimeStats.OptsEaBulkCreate()
                    self.opts_ea_bulk_create.parent = self
                    self._children_name_map["opts_ea_bulk_create"] = "opts-ea-bulk-create"
                    self._children_yang_names.add("opts-ea-bulk-create")

                    self.opts_ea_bulk_update = Coherent.Nodes.Node.CoherentTimeStats.OptsEaBulkUpdate()
                    self.opts_ea_bulk_update.parent = self
                    self._children_name_map["opts_ea_bulk_update"] = "opts-ea-bulk-update"
                    self._children_yang_names.add("opts-ea-bulk-update")

                    self.port_stat = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("device_created",
                                    "driver_init",
                                    "driver_operational",
                                    "dsp_controllers_created",
                                    "eth_intf_created",
                                    "optics_controllers_created") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Coherent.Nodes.Node.CoherentTimeStats, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Coherent.Nodes.Node.CoherentTimeStats, self).__setattr__(name, value)


                class OptsEaBulkCreate(Entity):
                    """
                    opts ea bulk create
                    
                    .. attribute:: end
                    
                    	end
                    	**type**\:  str
                    
                    	**length:** 0..255
                    
                    .. attribute:: start
                    
                    	start
                    	**type**\:  str
                    
                    	**length:** 0..255
                    
                    .. attribute:: time_taken
                    
                    	time taken
                    	**type**\:  str
                    
                    	**length:** 0..255
                    
                    .. attribute:: worst_time
                    
                    	worst time
                    	**type**\:  str
                    
                    	**length:** 0..255
                    
                    

                    """

                    _prefix = 'ncs5500-coherent-node-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Coherent.Nodes.Node.CoherentTimeStats.OptsEaBulkCreate, self).__init__()

                        self.yang_name = "opts-ea-bulk-create"
                        self.yang_parent_name = "coherent-time-stats"

                        self.end = YLeaf(YType.str, "end")

                        self.start = YLeaf(YType.str, "start")

                        self.time_taken = YLeaf(YType.str, "time-taken")

                        self.worst_time = YLeaf(YType.str, "worst-time")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("end",
                                        "start",
                                        "time_taken",
                                        "worst_time") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Coherent.Nodes.Node.CoherentTimeStats.OptsEaBulkCreate, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Coherent.Nodes.Node.CoherentTimeStats.OptsEaBulkCreate, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.end.is_set or
                            self.start.is_set or
                            self.time_taken.is_set or
                            self.worst_time.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.end.yfilter != YFilter.not_set or
                            self.start.yfilter != YFilter.not_set or
                            self.time_taken.yfilter != YFilter.not_set or
                            self.worst_time.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "opts-ea-bulk-create" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.end.is_set or self.end.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.end.get_name_leafdata())
                        if (self.start.is_set or self.start.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.start.get_name_leafdata())
                        if (self.time_taken.is_set or self.time_taken.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.time_taken.get_name_leafdata())
                        if (self.worst_time.is_set or self.worst_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.worst_time.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "end" or name == "start" or name == "time-taken" or name == "worst-time"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "end"):
                            self.end = value
                            self.end.value_namespace = name_space
                            self.end.value_namespace_prefix = name_space_prefix
                        if(value_path == "start"):
                            self.start = value
                            self.start.value_namespace = name_space
                            self.start.value_namespace_prefix = name_space_prefix
                        if(value_path == "time-taken"):
                            self.time_taken = value
                            self.time_taken.value_namespace = name_space
                            self.time_taken.value_namespace_prefix = name_space_prefix
                        if(value_path == "worst-time"):
                            self.worst_time = value
                            self.worst_time.value_namespace = name_space
                            self.worst_time.value_namespace_prefix = name_space_prefix


                class OptsEaBulkUpdate(Entity):
                    """
                    opts ea bulk update
                    
                    .. attribute:: end
                    
                    	end
                    	**type**\:  str
                    
                    	**length:** 0..255
                    
                    .. attribute:: start
                    
                    	start
                    	**type**\:  str
                    
                    	**length:** 0..255
                    
                    .. attribute:: time_taken
                    
                    	time taken
                    	**type**\:  str
                    
                    	**length:** 0..255
                    
                    .. attribute:: worst_time
                    
                    	worst time
                    	**type**\:  str
                    
                    	**length:** 0..255
                    
                    

                    """

                    _prefix = 'ncs5500-coherent-node-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Coherent.Nodes.Node.CoherentTimeStats.OptsEaBulkUpdate, self).__init__()

                        self.yang_name = "opts-ea-bulk-update"
                        self.yang_parent_name = "coherent-time-stats"

                        self.end = YLeaf(YType.str, "end")

                        self.start = YLeaf(YType.str, "start")

                        self.time_taken = YLeaf(YType.str, "time-taken")

                        self.worst_time = YLeaf(YType.str, "worst-time")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("end",
                                        "start",
                                        "time_taken",
                                        "worst_time") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Coherent.Nodes.Node.CoherentTimeStats.OptsEaBulkUpdate, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Coherent.Nodes.Node.CoherentTimeStats.OptsEaBulkUpdate, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.end.is_set or
                            self.start.is_set or
                            self.time_taken.is_set or
                            self.worst_time.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.end.yfilter != YFilter.not_set or
                            self.start.yfilter != YFilter.not_set or
                            self.time_taken.yfilter != YFilter.not_set or
                            self.worst_time.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "opts-ea-bulk-update" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.end.is_set or self.end.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.end.get_name_leafdata())
                        if (self.start.is_set or self.start.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.start.get_name_leafdata())
                        if (self.time_taken.is_set or self.time_taken.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.time_taken.get_name_leafdata())
                        if (self.worst_time.is_set or self.worst_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.worst_time.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "end" or name == "start" or name == "time-taken" or name == "worst-time"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "end"):
                            self.end = value
                            self.end.value_namespace = name_space
                            self.end.value_namespace_prefix = name_space_prefix
                        if(value_path == "start"):
                            self.start = value
                            self.start.value_namespace = name_space
                            self.start.value_namespace_prefix = name_space_prefix
                        if(value_path == "time-taken"):
                            self.time_taken = value
                            self.time_taken.value_namespace = name_space
                            self.time_taken.value_namespace_prefix = name_space_prefix
                        if(value_path == "worst-time"):
                            self.worst_time = value
                            self.worst_time.value_namespace = name_space
                            self.worst_time.value_namespace_prefix = name_space_prefix


                class DspEaBulkCreate(Entity):
                    """
                    dsp ea bulk create
                    
                    .. attribute:: end
                    
                    	end
                    	**type**\:  str
                    
                    	**length:** 0..255
                    
                    .. attribute:: start
                    
                    	start
                    	**type**\:  str
                    
                    	**length:** 0..255
                    
                    .. attribute:: time_taken
                    
                    	time taken
                    	**type**\:  str
                    
                    	**length:** 0..255
                    
                    .. attribute:: worst_time
                    
                    	worst time
                    	**type**\:  str
                    
                    	**length:** 0..255
                    
                    

                    """

                    _prefix = 'ncs5500-coherent-node-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Coherent.Nodes.Node.CoherentTimeStats.DspEaBulkCreate, self).__init__()

                        self.yang_name = "dsp-ea-bulk-create"
                        self.yang_parent_name = "coherent-time-stats"

                        self.end = YLeaf(YType.str, "end")

                        self.start = YLeaf(YType.str, "start")

                        self.time_taken = YLeaf(YType.str, "time-taken")

                        self.worst_time = YLeaf(YType.str, "worst-time")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("end",
                                        "start",
                                        "time_taken",
                                        "worst_time") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Coherent.Nodes.Node.CoherentTimeStats.DspEaBulkCreate, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Coherent.Nodes.Node.CoherentTimeStats.DspEaBulkCreate, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.end.is_set or
                            self.start.is_set or
                            self.time_taken.is_set or
                            self.worst_time.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.end.yfilter != YFilter.not_set or
                            self.start.yfilter != YFilter.not_set or
                            self.time_taken.yfilter != YFilter.not_set or
                            self.worst_time.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "dsp-ea-bulk-create" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.end.is_set or self.end.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.end.get_name_leafdata())
                        if (self.start.is_set or self.start.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.start.get_name_leafdata())
                        if (self.time_taken.is_set or self.time_taken.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.time_taken.get_name_leafdata())
                        if (self.worst_time.is_set or self.worst_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.worst_time.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "end" or name == "start" or name == "time-taken" or name == "worst-time"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "end"):
                            self.end = value
                            self.end.value_namespace = name_space
                            self.end.value_namespace_prefix = name_space_prefix
                        if(value_path == "start"):
                            self.start = value
                            self.start.value_namespace = name_space
                            self.start.value_namespace_prefix = name_space_prefix
                        if(value_path == "time-taken"):
                            self.time_taken = value
                            self.time_taken.value_namespace = name_space
                            self.time_taken.value_namespace_prefix = name_space_prefix
                        if(value_path == "worst-time"):
                            self.worst_time = value
                            self.worst_time.value_namespace = name_space
                            self.worst_time.value_namespace_prefix = name_space_prefix


                class DspEaBulkUpdate(Entity):
                    """
                    dsp ea bulk update
                    
                    .. attribute:: end
                    
                    	end
                    	**type**\:  str
                    
                    	**length:** 0..255
                    
                    .. attribute:: start
                    
                    	start
                    	**type**\:  str
                    
                    	**length:** 0..255
                    
                    .. attribute:: time_taken
                    
                    	time taken
                    	**type**\:  str
                    
                    	**length:** 0..255
                    
                    .. attribute:: worst_time
                    
                    	worst time
                    	**type**\:  str
                    
                    	**length:** 0..255
                    
                    

                    """

                    _prefix = 'ncs5500-coherent-node-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Coherent.Nodes.Node.CoherentTimeStats.DspEaBulkUpdate, self).__init__()

                        self.yang_name = "dsp-ea-bulk-update"
                        self.yang_parent_name = "coherent-time-stats"

                        self.end = YLeaf(YType.str, "end")

                        self.start = YLeaf(YType.str, "start")

                        self.time_taken = YLeaf(YType.str, "time-taken")

                        self.worst_time = YLeaf(YType.str, "worst-time")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("end",
                                        "start",
                                        "time_taken",
                                        "worst_time") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Coherent.Nodes.Node.CoherentTimeStats.DspEaBulkUpdate, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Coherent.Nodes.Node.CoherentTimeStats.DspEaBulkUpdate, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.end.is_set or
                            self.start.is_set or
                            self.time_taken.is_set or
                            self.worst_time.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.end.yfilter != YFilter.not_set or
                            self.start.yfilter != YFilter.not_set or
                            self.time_taken.yfilter != YFilter.not_set or
                            self.worst_time.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "dsp-ea-bulk-update" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.end.is_set or self.end.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.end.get_name_leafdata())
                        if (self.start.is_set or self.start.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.start.get_name_leafdata())
                        if (self.time_taken.is_set or self.time_taken.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.time_taken.get_name_leafdata())
                        if (self.worst_time.is_set or self.worst_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.worst_time.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "end" or name == "start" or name == "time-taken" or name == "worst-time"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "end"):
                            self.end = value
                            self.end.value_namespace = name_space
                            self.end.value_namespace_prefix = name_space_prefix
                        if(value_path == "start"):
                            self.start = value
                            self.start.value_namespace = name_space
                            self.start.value_namespace_prefix = name_space_prefix
                        if(value_path == "time-taken"):
                            self.time_taken = value
                            self.time_taken.value_namespace = name_space
                            self.time_taken.value_namespace_prefix = name_space_prefix
                        if(value_path == "worst-time"):
                            self.worst_time = value
                            self.worst_time.value_namespace = name_space
                            self.worst_time.value_namespace_prefix = name_space_prefix


                class PortStat(Entity):
                    """
                    port stat
                    
                    .. attribute:: cd_max
                    
                    	cd max
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: cd_min
                    
                    	cd min
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: cdmax_op_stats
                    
                    	cdmax op stats
                    	**type**\:   :py:class:`CdmaxOpStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.CoherentTimeStats.PortStat.CdmaxOpStats>`
                    
                    .. attribute:: cdmin_op_stats
                    
                    	cdmin op stats
                    	**type**\:   :py:class:`CdminOpStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.CoherentTimeStats.PortStat.CdminOpStats>`
                    
                    .. attribute:: laser_off_stats
                    
                    	laser off stats
                    	**type**\:   :py:class:`LaserOffStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.CoherentTimeStats.PortStat.LaserOffStats>`
                    
                    .. attribute:: laser_on_stats
                    
                    	laser on stats
                    	**type**\:   :py:class:`LaserOnStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.CoherentTimeStats.PortStat.LaserOnStats>`
                    
                    .. attribute:: laser_state
                    
                    	laser state
                    	**type**\:  bool
                    
                    .. attribute:: provisioned_frequency
                    
                    	provisioned frequency
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: traffic_type
                    
                    	traffic type
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: traffictype_op_stats
                    
                    	traffictype op stats
                    	**type**\:   :py:class:`TraffictypeOpStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.CoherentTimeStats.PortStat.TraffictypeOpStats>`
                    
                    .. attribute:: tx_power
                    
                    	tx power
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: txpwr_op_stats
                    
                    	txpwr op stats
                    	**type**\:   :py:class:`TxpwrOpStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.CoherentTimeStats.PortStat.TxpwrOpStats>`
                    
                    .. attribute:: wl_op_stats
                    
                    	wl op stats
                    	**type**\:   :py:class:`WlOpStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.CoherentTimeStats.PortStat.WlOpStats>`
                    
                    

                    """

                    _prefix = 'ncs5500-coherent-node-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Coherent.Nodes.Node.CoherentTimeStats.PortStat, self).__init__()

                        self.yang_name = "port-stat"
                        self.yang_parent_name = "coherent-time-stats"

                        self.cd_max = YLeaf(YType.uint32, "cd-max")

                        self.cd_min = YLeaf(YType.uint32, "cd-min")

                        self.laser_state = YLeaf(YType.boolean, "laser-state")

                        self.provisioned_frequency = YLeaf(YType.uint32, "provisioned-frequency")

                        self.traffic_type = YLeaf(YType.uint32, "traffic-type")

                        self.tx_power = YLeaf(YType.uint32, "tx-power")

                        self.cdmax_op_stats = Coherent.Nodes.Node.CoherentTimeStats.PortStat.CdmaxOpStats()
                        self.cdmax_op_stats.parent = self
                        self._children_name_map["cdmax_op_stats"] = "cdmax-op-stats"
                        self._children_yang_names.add("cdmax-op-stats")

                        self.cdmin_op_stats = Coherent.Nodes.Node.CoherentTimeStats.PortStat.CdminOpStats()
                        self.cdmin_op_stats.parent = self
                        self._children_name_map["cdmin_op_stats"] = "cdmin-op-stats"
                        self._children_yang_names.add("cdmin-op-stats")

                        self.laser_off_stats = Coherent.Nodes.Node.CoherentTimeStats.PortStat.LaserOffStats()
                        self.laser_off_stats.parent = self
                        self._children_name_map["laser_off_stats"] = "laser-off-stats"
                        self._children_yang_names.add("laser-off-stats")

                        self.laser_on_stats = Coherent.Nodes.Node.CoherentTimeStats.PortStat.LaserOnStats()
                        self.laser_on_stats.parent = self
                        self._children_name_map["laser_on_stats"] = "laser-on-stats"
                        self._children_yang_names.add("laser-on-stats")

                        self.traffictype_op_stats = Coherent.Nodes.Node.CoherentTimeStats.PortStat.TraffictypeOpStats()
                        self.traffictype_op_stats.parent = self
                        self._children_name_map["traffictype_op_stats"] = "traffictype-op-stats"
                        self._children_yang_names.add("traffictype-op-stats")

                        self.txpwr_op_stats = Coherent.Nodes.Node.CoherentTimeStats.PortStat.TxpwrOpStats()
                        self.txpwr_op_stats.parent = self
                        self._children_name_map["txpwr_op_stats"] = "txpwr-op-stats"
                        self._children_yang_names.add("txpwr-op-stats")

                        self.wl_op_stats = Coherent.Nodes.Node.CoherentTimeStats.PortStat.WlOpStats()
                        self.wl_op_stats.parent = self
                        self._children_name_map["wl_op_stats"] = "wl-op-stats"
                        self._children_yang_names.add("wl-op-stats")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("cd_max",
                                        "cd_min",
                                        "laser_state",
                                        "provisioned_frequency",
                                        "traffic_type",
                                        "tx_power") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Coherent.Nodes.Node.CoherentTimeStats.PortStat, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Coherent.Nodes.Node.CoherentTimeStats.PortStat, self).__setattr__(name, value)


                    class LaserOnStats(Entity):
                        """
                        laser on stats
                        
                        .. attribute:: end
                        
                        	end
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        .. attribute:: start
                        
                        	start
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        .. attribute:: time_taken
                        
                        	time taken
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        .. attribute:: worst_time
                        
                        	worst time
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        

                        """

                        _prefix = 'ncs5500-coherent-node-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Coherent.Nodes.Node.CoherentTimeStats.PortStat.LaserOnStats, self).__init__()

                            self.yang_name = "laser-on-stats"
                            self.yang_parent_name = "port-stat"

                            self.end = YLeaf(YType.str, "end")

                            self.start = YLeaf(YType.str, "start")

                            self.time_taken = YLeaf(YType.str, "time-taken")

                            self.worst_time = YLeaf(YType.str, "worst-time")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("end",
                                            "start",
                                            "time_taken",
                                            "worst_time") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Coherent.Nodes.Node.CoherentTimeStats.PortStat.LaserOnStats, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Coherent.Nodes.Node.CoherentTimeStats.PortStat.LaserOnStats, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.end.is_set or
                                self.start.is_set or
                                self.time_taken.is_set or
                                self.worst_time.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.end.yfilter != YFilter.not_set or
                                self.start.yfilter != YFilter.not_set or
                                self.time_taken.yfilter != YFilter.not_set or
                                self.worst_time.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "laser-on-stats" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.end.is_set or self.end.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.end.get_name_leafdata())
                            if (self.start.is_set or self.start.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.start.get_name_leafdata())
                            if (self.time_taken.is_set or self.time_taken.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.time_taken.get_name_leafdata())
                            if (self.worst_time.is_set or self.worst_time.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.worst_time.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "end" or name == "start" or name == "time-taken" or name == "worst-time"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "end"):
                                self.end = value
                                self.end.value_namespace = name_space
                                self.end.value_namespace_prefix = name_space_prefix
                            if(value_path == "start"):
                                self.start = value
                                self.start.value_namespace = name_space
                                self.start.value_namespace_prefix = name_space_prefix
                            if(value_path == "time-taken"):
                                self.time_taken = value
                                self.time_taken.value_namespace = name_space
                                self.time_taken.value_namespace_prefix = name_space_prefix
                            if(value_path == "worst-time"):
                                self.worst_time = value
                                self.worst_time.value_namespace = name_space
                                self.worst_time.value_namespace_prefix = name_space_prefix


                    class LaserOffStats(Entity):
                        """
                        laser off stats
                        
                        .. attribute:: end
                        
                        	end
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        .. attribute:: start
                        
                        	start
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        .. attribute:: time_taken
                        
                        	time taken
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        .. attribute:: worst_time
                        
                        	worst time
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        

                        """

                        _prefix = 'ncs5500-coherent-node-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Coherent.Nodes.Node.CoherentTimeStats.PortStat.LaserOffStats, self).__init__()

                            self.yang_name = "laser-off-stats"
                            self.yang_parent_name = "port-stat"

                            self.end = YLeaf(YType.str, "end")

                            self.start = YLeaf(YType.str, "start")

                            self.time_taken = YLeaf(YType.str, "time-taken")

                            self.worst_time = YLeaf(YType.str, "worst-time")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("end",
                                            "start",
                                            "time_taken",
                                            "worst_time") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Coherent.Nodes.Node.CoherentTimeStats.PortStat.LaserOffStats, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Coherent.Nodes.Node.CoherentTimeStats.PortStat.LaserOffStats, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.end.is_set or
                                self.start.is_set or
                                self.time_taken.is_set or
                                self.worst_time.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.end.yfilter != YFilter.not_set or
                                self.start.yfilter != YFilter.not_set or
                                self.time_taken.yfilter != YFilter.not_set or
                                self.worst_time.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "laser-off-stats" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.end.is_set or self.end.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.end.get_name_leafdata())
                            if (self.start.is_set or self.start.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.start.get_name_leafdata())
                            if (self.time_taken.is_set or self.time_taken.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.time_taken.get_name_leafdata())
                            if (self.worst_time.is_set or self.worst_time.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.worst_time.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "end" or name == "start" or name == "time-taken" or name == "worst-time"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "end"):
                                self.end = value
                                self.end.value_namespace = name_space
                                self.end.value_namespace_prefix = name_space_prefix
                            if(value_path == "start"):
                                self.start = value
                                self.start.value_namespace = name_space
                                self.start.value_namespace_prefix = name_space_prefix
                            if(value_path == "time-taken"):
                                self.time_taken = value
                                self.time_taken.value_namespace = name_space
                                self.time_taken.value_namespace_prefix = name_space_prefix
                            if(value_path == "worst-time"):
                                self.worst_time = value
                                self.worst_time.value_namespace = name_space
                                self.worst_time.value_namespace_prefix = name_space_prefix


                    class WlOpStats(Entity):
                        """
                        wl op stats
                        
                        .. attribute:: end
                        
                        	end
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        .. attribute:: start
                        
                        	start
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        .. attribute:: time_taken
                        
                        	time taken
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        .. attribute:: worst_time
                        
                        	worst time
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        

                        """

                        _prefix = 'ncs5500-coherent-node-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Coherent.Nodes.Node.CoherentTimeStats.PortStat.WlOpStats, self).__init__()

                            self.yang_name = "wl-op-stats"
                            self.yang_parent_name = "port-stat"

                            self.end = YLeaf(YType.str, "end")

                            self.start = YLeaf(YType.str, "start")

                            self.time_taken = YLeaf(YType.str, "time-taken")

                            self.worst_time = YLeaf(YType.str, "worst-time")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("end",
                                            "start",
                                            "time_taken",
                                            "worst_time") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Coherent.Nodes.Node.CoherentTimeStats.PortStat.WlOpStats, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Coherent.Nodes.Node.CoherentTimeStats.PortStat.WlOpStats, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.end.is_set or
                                self.start.is_set or
                                self.time_taken.is_set or
                                self.worst_time.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.end.yfilter != YFilter.not_set or
                                self.start.yfilter != YFilter.not_set or
                                self.time_taken.yfilter != YFilter.not_set or
                                self.worst_time.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "wl-op-stats" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.end.is_set or self.end.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.end.get_name_leafdata())
                            if (self.start.is_set or self.start.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.start.get_name_leafdata())
                            if (self.time_taken.is_set or self.time_taken.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.time_taken.get_name_leafdata())
                            if (self.worst_time.is_set or self.worst_time.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.worst_time.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "end" or name == "start" or name == "time-taken" or name == "worst-time"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "end"):
                                self.end = value
                                self.end.value_namespace = name_space
                                self.end.value_namespace_prefix = name_space_prefix
                            if(value_path == "start"):
                                self.start = value
                                self.start.value_namespace = name_space
                                self.start.value_namespace_prefix = name_space_prefix
                            if(value_path == "time-taken"):
                                self.time_taken = value
                                self.time_taken.value_namespace = name_space
                                self.time_taken.value_namespace_prefix = name_space_prefix
                            if(value_path == "worst-time"):
                                self.worst_time = value
                                self.worst_time.value_namespace = name_space
                                self.worst_time.value_namespace_prefix = name_space_prefix


                    class TxpwrOpStats(Entity):
                        """
                        txpwr op stats
                        
                        .. attribute:: end
                        
                        	end
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        .. attribute:: start
                        
                        	start
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        .. attribute:: time_taken
                        
                        	time taken
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        .. attribute:: worst_time
                        
                        	worst time
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        

                        """

                        _prefix = 'ncs5500-coherent-node-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Coherent.Nodes.Node.CoherentTimeStats.PortStat.TxpwrOpStats, self).__init__()

                            self.yang_name = "txpwr-op-stats"
                            self.yang_parent_name = "port-stat"

                            self.end = YLeaf(YType.str, "end")

                            self.start = YLeaf(YType.str, "start")

                            self.time_taken = YLeaf(YType.str, "time-taken")

                            self.worst_time = YLeaf(YType.str, "worst-time")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("end",
                                            "start",
                                            "time_taken",
                                            "worst_time") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Coherent.Nodes.Node.CoherentTimeStats.PortStat.TxpwrOpStats, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Coherent.Nodes.Node.CoherentTimeStats.PortStat.TxpwrOpStats, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.end.is_set or
                                self.start.is_set or
                                self.time_taken.is_set or
                                self.worst_time.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.end.yfilter != YFilter.not_set or
                                self.start.yfilter != YFilter.not_set or
                                self.time_taken.yfilter != YFilter.not_set or
                                self.worst_time.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "txpwr-op-stats" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.end.is_set or self.end.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.end.get_name_leafdata())
                            if (self.start.is_set or self.start.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.start.get_name_leafdata())
                            if (self.time_taken.is_set or self.time_taken.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.time_taken.get_name_leafdata())
                            if (self.worst_time.is_set or self.worst_time.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.worst_time.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "end" or name == "start" or name == "time-taken" or name == "worst-time"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "end"):
                                self.end = value
                                self.end.value_namespace = name_space
                                self.end.value_namespace_prefix = name_space_prefix
                            if(value_path == "start"):
                                self.start = value
                                self.start.value_namespace = name_space
                                self.start.value_namespace_prefix = name_space_prefix
                            if(value_path == "time-taken"):
                                self.time_taken = value
                                self.time_taken.value_namespace = name_space
                                self.time_taken.value_namespace_prefix = name_space_prefix
                            if(value_path == "worst-time"):
                                self.worst_time = value
                                self.worst_time.value_namespace = name_space
                                self.worst_time.value_namespace_prefix = name_space_prefix


                    class CdminOpStats(Entity):
                        """
                        cdmin op stats
                        
                        .. attribute:: end
                        
                        	end
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        .. attribute:: start
                        
                        	start
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        .. attribute:: time_taken
                        
                        	time taken
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        .. attribute:: worst_time
                        
                        	worst time
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        

                        """

                        _prefix = 'ncs5500-coherent-node-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Coherent.Nodes.Node.CoherentTimeStats.PortStat.CdminOpStats, self).__init__()

                            self.yang_name = "cdmin-op-stats"
                            self.yang_parent_name = "port-stat"

                            self.end = YLeaf(YType.str, "end")

                            self.start = YLeaf(YType.str, "start")

                            self.time_taken = YLeaf(YType.str, "time-taken")

                            self.worst_time = YLeaf(YType.str, "worst-time")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("end",
                                            "start",
                                            "time_taken",
                                            "worst_time") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Coherent.Nodes.Node.CoherentTimeStats.PortStat.CdminOpStats, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Coherent.Nodes.Node.CoherentTimeStats.PortStat.CdminOpStats, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.end.is_set or
                                self.start.is_set or
                                self.time_taken.is_set or
                                self.worst_time.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.end.yfilter != YFilter.not_set or
                                self.start.yfilter != YFilter.not_set or
                                self.time_taken.yfilter != YFilter.not_set or
                                self.worst_time.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "cdmin-op-stats" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.end.is_set or self.end.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.end.get_name_leafdata())
                            if (self.start.is_set or self.start.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.start.get_name_leafdata())
                            if (self.time_taken.is_set or self.time_taken.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.time_taken.get_name_leafdata())
                            if (self.worst_time.is_set or self.worst_time.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.worst_time.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "end" or name == "start" or name == "time-taken" or name == "worst-time"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "end"):
                                self.end = value
                                self.end.value_namespace = name_space
                                self.end.value_namespace_prefix = name_space_prefix
                            if(value_path == "start"):
                                self.start = value
                                self.start.value_namespace = name_space
                                self.start.value_namespace_prefix = name_space_prefix
                            if(value_path == "time-taken"):
                                self.time_taken = value
                                self.time_taken.value_namespace = name_space
                                self.time_taken.value_namespace_prefix = name_space_prefix
                            if(value_path == "worst-time"):
                                self.worst_time = value
                                self.worst_time.value_namespace = name_space
                                self.worst_time.value_namespace_prefix = name_space_prefix


                    class CdmaxOpStats(Entity):
                        """
                        cdmax op stats
                        
                        .. attribute:: end
                        
                        	end
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        .. attribute:: start
                        
                        	start
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        .. attribute:: time_taken
                        
                        	time taken
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        .. attribute:: worst_time
                        
                        	worst time
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        

                        """

                        _prefix = 'ncs5500-coherent-node-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Coherent.Nodes.Node.CoherentTimeStats.PortStat.CdmaxOpStats, self).__init__()

                            self.yang_name = "cdmax-op-stats"
                            self.yang_parent_name = "port-stat"

                            self.end = YLeaf(YType.str, "end")

                            self.start = YLeaf(YType.str, "start")

                            self.time_taken = YLeaf(YType.str, "time-taken")

                            self.worst_time = YLeaf(YType.str, "worst-time")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("end",
                                            "start",
                                            "time_taken",
                                            "worst_time") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Coherent.Nodes.Node.CoherentTimeStats.PortStat.CdmaxOpStats, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Coherent.Nodes.Node.CoherentTimeStats.PortStat.CdmaxOpStats, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.end.is_set or
                                self.start.is_set or
                                self.time_taken.is_set or
                                self.worst_time.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.end.yfilter != YFilter.not_set or
                                self.start.yfilter != YFilter.not_set or
                                self.time_taken.yfilter != YFilter.not_set or
                                self.worst_time.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "cdmax-op-stats" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.end.is_set or self.end.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.end.get_name_leafdata())
                            if (self.start.is_set or self.start.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.start.get_name_leafdata())
                            if (self.time_taken.is_set or self.time_taken.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.time_taken.get_name_leafdata())
                            if (self.worst_time.is_set or self.worst_time.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.worst_time.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "end" or name == "start" or name == "time-taken" or name == "worst-time"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "end"):
                                self.end = value
                                self.end.value_namespace = name_space
                                self.end.value_namespace_prefix = name_space_prefix
                            if(value_path == "start"):
                                self.start = value
                                self.start.value_namespace = name_space
                                self.start.value_namespace_prefix = name_space_prefix
                            if(value_path == "time-taken"):
                                self.time_taken = value
                                self.time_taken.value_namespace = name_space
                                self.time_taken.value_namespace_prefix = name_space_prefix
                            if(value_path == "worst-time"):
                                self.worst_time = value
                                self.worst_time.value_namespace = name_space
                                self.worst_time.value_namespace_prefix = name_space_prefix


                    class TraffictypeOpStats(Entity):
                        """
                        traffictype op stats
                        
                        .. attribute:: end
                        
                        	end
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        .. attribute:: start
                        
                        	start
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        .. attribute:: time_taken
                        
                        	time taken
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        .. attribute:: worst_time
                        
                        	worst time
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        

                        """

                        _prefix = 'ncs5500-coherent-node-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Coherent.Nodes.Node.CoherentTimeStats.PortStat.TraffictypeOpStats, self).__init__()

                            self.yang_name = "traffictype-op-stats"
                            self.yang_parent_name = "port-stat"

                            self.end = YLeaf(YType.str, "end")

                            self.start = YLeaf(YType.str, "start")

                            self.time_taken = YLeaf(YType.str, "time-taken")

                            self.worst_time = YLeaf(YType.str, "worst-time")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("end",
                                            "start",
                                            "time_taken",
                                            "worst_time") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Coherent.Nodes.Node.CoherentTimeStats.PortStat.TraffictypeOpStats, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Coherent.Nodes.Node.CoherentTimeStats.PortStat.TraffictypeOpStats, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.end.is_set or
                                self.start.is_set or
                                self.time_taken.is_set or
                                self.worst_time.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.end.yfilter != YFilter.not_set or
                                self.start.yfilter != YFilter.not_set or
                                self.time_taken.yfilter != YFilter.not_set or
                                self.worst_time.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "traffictype-op-stats" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.end.is_set or self.end.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.end.get_name_leafdata())
                            if (self.start.is_set or self.start.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.start.get_name_leafdata())
                            if (self.time_taken.is_set or self.time_taken.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.time_taken.get_name_leafdata())
                            if (self.worst_time.is_set or self.worst_time.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.worst_time.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "end" or name == "start" or name == "time-taken" or name == "worst-time"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "end"):
                                self.end = value
                                self.end.value_namespace = name_space
                                self.end.value_namespace_prefix = name_space_prefix
                            if(value_path == "start"):
                                self.start = value
                                self.start.value_namespace = name_space
                                self.start.value_namespace_prefix = name_space_prefix
                            if(value_path == "time-taken"):
                                self.time_taken = value
                                self.time_taken.value_namespace = name_space
                                self.time_taken.value_namespace_prefix = name_space_prefix
                            if(value_path == "worst-time"):
                                self.worst_time = value
                                self.worst_time.value_namespace = name_space
                                self.worst_time.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.cd_max.is_set or
                            self.cd_min.is_set or
                            self.laser_state.is_set or
                            self.provisioned_frequency.is_set or
                            self.traffic_type.is_set or
                            self.tx_power.is_set or
                            (self.cdmax_op_stats is not None and self.cdmax_op_stats.has_data()) or
                            (self.cdmin_op_stats is not None and self.cdmin_op_stats.has_data()) or
                            (self.laser_off_stats is not None and self.laser_off_stats.has_data()) or
                            (self.laser_on_stats is not None and self.laser_on_stats.has_data()) or
                            (self.traffictype_op_stats is not None and self.traffictype_op_stats.has_data()) or
                            (self.txpwr_op_stats is not None and self.txpwr_op_stats.has_data()) or
                            (self.wl_op_stats is not None and self.wl_op_stats.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.cd_max.yfilter != YFilter.not_set or
                            self.cd_min.yfilter != YFilter.not_set or
                            self.laser_state.yfilter != YFilter.not_set or
                            self.provisioned_frequency.yfilter != YFilter.not_set or
                            self.traffic_type.yfilter != YFilter.not_set or
                            self.tx_power.yfilter != YFilter.not_set or
                            (self.cdmax_op_stats is not None and self.cdmax_op_stats.has_operation()) or
                            (self.cdmin_op_stats is not None and self.cdmin_op_stats.has_operation()) or
                            (self.laser_off_stats is not None and self.laser_off_stats.has_operation()) or
                            (self.laser_on_stats is not None and self.laser_on_stats.has_operation()) or
                            (self.traffictype_op_stats is not None and self.traffictype_op_stats.has_operation()) or
                            (self.txpwr_op_stats is not None and self.txpwr_op_stats.has_operation()) or
                            (self.wl_op_stats is not None and self.wl_op_stats.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "port-stat" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.cd_max.is_set or self.cd_max.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.cd_max.get_name_leafdata())
                        if (self.cd_min.is_set or self.cd_min.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.cd_min.get_name_leafdata())
                        if (self.laser_state.is_set or self.laser_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.laser_state.get_name_leafdata())
                        if (self.provisioned_frequency.is_set or self.provisioned_frequency.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.provisioned_frequency.get_name_leafdata())
                        if (self.traffic_type.is_set or self.traffic_type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.traffic_type.get_name_leafdata())
                        if (self.tx_power.is_set or self.tx_power.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tx_power.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "cdmax-op-stats"):
                            if (self.cdmax_op_stats is None):
                                self.cdmax_op_stats = Coherent.Nodes.Node.CoherentTimeStats.PortStat.CdmaxOpStats()
                                self.cdmax_op_stats.parent = self
                                self._children_name_map["cdmax_op_stats"] = "cdmax-op-stats"
                            return self.cdmax_op_stats

                        if (child_yang_name == "cdmin-op-stats"):
                            if (self.cdmin_op_stats is None):
                                self.cdmin_op_stats = Coherent.Nodes.Node.CoherentTimeStats.PortStat.CdminOpStats()
                                self.cdmin_op_stats.parent = self
                                self._children_name_map["cdmin_op_stats"] = "cdmin-op-stats"
                            return self.cdmin_op_stats

                        if (child_yang_name == "laser-off-stats"):
                            if (self.laser_off_stats is None):
                                self.laser_off_stats = Coherent.Nodes.Node.CoherentTimeStats.PortStat.LaserOffStats()
                                self.laser_off_stats.parent = self
                                self._children_name_map["laser_off_stats"] = "laser-off-stats"
                            return self.laser_off_stats

                        if (child_yang_name == "laser-on-stats"):
                            if (self.laser_on_stats is None):
                                self.laser_on_stats = Coherent.Nodes.Node.CoherentTimeStats.PortStat.LaserOnStats()
                                self.laser_on_stats.parent = self
                                self._children_name_map["laser_on_stats"] = "laser-on-stats"
                            return self.laser_on_stats

                        if (child_yang_name == "traffictype-op-stats"):
                            if (self.traffictype_op_stats is None):
                                self.traffictype_op_stats = Coherent.Nodes.Node.CoherentTimeStats.PortStat.TraffictypeOpStats()
                                self.traffictype_op_stats.parent = self
                                self._children_name_map["traffictype_op_stats"] = "traffictype-op-stats"
                            return self.traffictype_op_stats

                        if (child_yang_name == "txpwr-op-stats"):
                            if (self.txpwr_op_stats is None):
                                self.txpwr_op_stats = Coherent.Nodes.Node.CoherentTimeStats.PortStat.TxpwrOpStats()
                                self.txpwr_op_stats.parent = self
                                self._children_name_map["txpwr_op_stats"] = "txpwr-op-stats"
                            return self.txpwr_op_stats

                        if (child_yang_name == "wl-op-stats"):
                            if (self.wl_op_stats is None):
                                self.wl_op_stats = Coherent.Nodes.Node.CoherentTimeStats.PortStat.WlOpStats()
                                self.wl_op_stats.parent = self
                                self._children_name_map["wl_op_stats"] = "wl-op-stats"
                            return self.wl_op_stats

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "cdmax-op-stats" or name == "cdmin-op-stats" or name == "laser-off-stats" or name == "laser-on-stats" or name == "traffictype-op-stats" or name == "txpwr-op-stats" or name == "wl-op-stats" or name == "cd-max" or name == "cd-min" or name == "laser-state" or name == "provisioned-frequency" or name == "traffic-type" or name == "tx-power"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "cd-max"):
                            self.cd_max = value
                            self.cd_max.value_namespace = name_space
                            self.cd_max.value_namespace_prefix = name_space_prefix
                        if(value_path == "cd-min"):
                            self.cd_min = value
                            self.cd_min.value_namespace = name_space
                            self.cd_min.value_namespace_prefix = name_space_prefix
                        if(value_path == "laser-state"):
                            self.laser_state = value
                            self.laser_state.value_namespace = name_space
                            self.laser_state.value_namespace_prefix = name_space_prefix
                        if(value_path == "provisioned-frequency"):
                            self.provisioned_frequency = value
                            self.provisioned_frequency.value_namespace = name_space
                            self.provisioned_frequency.value_namespace_prefix = name_space_prefix
                        if(value_path == "traffic-type"):
                            self.traffic_type = value
                            self.traffic_type.value_namespace = name_space
                            self.traffic_type.value_namespace_prefix = name_space_prefix
                        if(value_path == "tx-power"):
                            self.tx_power = value
                            self.tx_power.value_namespace = name_space
                            self.tx_power.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.port_stat:
                        if (c.has_data()):
                            return True
                    return (
                        self.device_created.is_set or
                        self.driver_init.is_set or
                        self.driver_operational.is_set or
                        self.dsp_controllers_created.is_set or
                        self.eth_intf_created.is_set or
                        self.optics_controllers_created.is_set or
                        (self.dsp_ea_bulk_create is not None and self.dsp_ea_bulk_create.has_data()) or
                        (self.dsp_ea_bulk_update is not None and self.dsp_ea_bulk_update.has_data()) or
                        (self.opts_ea_bulk_create is not None and self.opts_ea_bulk_create.has_data()) or
                        (self.opts_ea_bulk_update is not None and self.opts_ea_bulk_update.has_data()))

                def has_operation(self):
                    for c in self.port_stat:
                        if (c.has_operation()):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.device_created.yfilter != YFilter.not_set or
                        self.driver_init.yfilter != YFilter.not_set or
                        self.driver_operational.yfilter != YFilter.not_set or
                        self.dsp_controllers_created.yfilter != YFilter.not_set or
                        self.eth_intf_created.yfilter != YFilter.not_set or
                        self.optics_controllers_created.yfilter != YFilter.not_set or
                        (self.dsp_ea_bulk_create is not None and self.dsp_ea_bulk_create.has_operation()) or
                        (self.dsp_ea_bulk_update is not None and self.dsp_ea_bulk_update.has_operation()) or
                        (self.opts_ea_bulk_create is not None and self.opts_ea_bulk_create.has_operation()) or
                        (self.opts_ea_bulk_update is not None and self.opts_ea_bulk_update.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "coherent-time-stats" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.device_created.is_set or self.device_created.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.device_created.get_name_leafdata())
                    if (self.driver_init.is_set or self.driver_init.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.driver_init.get_name_leafdata())
                    if (self.driver_operational.is_set or self.driver_operational.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.driver_operational.get_name_leafdata())
                    if (self.dsp_controllers_created.is_set or self.dsp_controllers_created.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.dsp_controllers_created.get_name_leafdata())
                    if (self.eth_intf_created.is_set or self.eth_intf_created.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.eth_intf_created.get_name_leafdata())
                    if (self.optics_controllers_created.is_set or self.optics_controllers_created.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.optics_controllers_created.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "dsp-ea-bulk-create"):
                        if (self.dsp_ea_bulk_create is None):
                            self.dsp_ea_bulk_create = Coherent.Nodes.Node.CoherentTimeStats.DspEaBulkCreate()
                            self.dsp_ea_bulk_create.parent = self
                            self._children_name_map["dsp_ea_bulk_create"] = "dsp-ea-bulk-create"
                        return self.dsp_ea_bulk_create

                    if (child_yang_name == "dsp-ea-bulk-update"):
                        if (self.dsp_ea_bulk_update is None):
                            self.dsp_ea_bulk_update = Coherent.Nodes.Node.CoherentTimeStats.DspEaBulkUpdate()
                            self.dsp_ea_bulk_update.parent = self
                            self._children_name_map["dsp_ea_bulk_update"] = "dsp-ea-bulk-update"
                        return self.dsp_ea_bulk_update

                    if (child_yang_name == "opts-ea-bulk-create"):
                        if (self.opts_ea_bulk_create is None):
                            self.opts_ea_bulk_create = Coherent.Nodes.Node.CoherentTimeStats.OptsEaBulkCreate()
                            self.opts_ea_bulk_create.parent = self
                            self._children_name_map["opts_ea_bulk_create"] = "opts-ea-bulk-create"
                        return self.opts_ea_bulk_create

                    if (child_yang_name == "opts-ea-bulk-update"):
                        if (self.opts_ea_bulk_update is None):
                            self.opts_ea_bulk_update = Coherent.Nodes.Node.CoherentTimeStats.OptsEaBulkUpdate()
                            self.opts_ea_bulk_update.parent = self
                            self._children_name_map["opts_ea_bulk_update"] = "opts-ea-bulk-update"
                        return self.opts_ea_bulk_update

                    if (child_yang_name == "port-stat"):
                        for c in self.port_stat:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Coherent.Nodes.Node.CoherentTimeStats.PortStat()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.port_stat.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "dsp-ea-bulk-create" or name == "dsp-ea-bulk-update" or name == "opts-ea-bulk-create" or name == "opts-ea-bulk-update" or name == "port-stat" or name == "device-created" or name == "driver-init" or name == "driver-operational" or name == "dsp-controllers-created" or name == "eth-intf-created" or name == "optics-controllers-created"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "device-created"):
                        self.device_created = value
                        self.device_created.value_namespace = name_space
                        self.device_created.value_namespace_prefix = name_space_prefix
                    if(value_path == "driver-init"):
                        self.driver_init = value
                        self.driver_init.value_namespace = name_space
                        self.driver_init.value_namespace_prefix = name_space_prefix
                    if(value_path == "driver-operational"):
                        self.driver_operational = value
                        self.driver_operational.value_namespace = name_space
                        self.driver_operational.value_namespace_prefix = name_space_prefix
                    if(value_path == "dsp-controllers-created"):
                        self.dsp_controllers_created = value
                        self.dsp_controllers_created.value_namespace = name_space
                        self.dsp_controllers_created.value_namespace_prefix = name_space_prefix
                    if(value_path == "eth-intf-created"):
                        self.eth_intf_created = value
                        self.eth_intf_created.value_namespace = name_space
                        self.eth_intf_created.value_namespace_prefix = name_space_prefix
                    if(value_path == "optics-controllers-created"):
                        self.optics_controllers_created = value
                        self.optics_controllers_created.value_namespace = name_space
                        self.optics_controllers_created.value_namespace_prefix = name_space_prefix


            class Devicemapping(Entity):
                """
                Coherent node data for device \_mapping
                
                .. attribute:: dev_map
                
                	dev map
                	**type**\: list of    :py:class:`DevMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.Devicemapping.DevMap>`
                
                .. attribute:: num_entries
                
                	Number of dev map entries
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ncs5500-coherent-node-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Coherent.Nodes.Node.Devicemapping, self).__init__()

                    self.yang_name = "devicemapping"
                    self.yang_parent_name = "node"

                    self.num_entries = YLeaf(YType.uint32, "num-entries")

                    self.dev_map = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("num_entries") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Coherent.Nodes.Node.Devicemapping, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Coherent.Nodes.Node.Devicemapping, self).__setattr__(name, value)


                class DevMap(Entity):
                    """
                    dev map
                    
                    .. attribute:: device_address
                    
                    	Device address
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: ifhandle
                    
                    	Interface handle
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: intf_name
                    
                    	intf name
                    	**type**\:  str
                    
                    	**length:** 0..64
                    
                    

                    """

                    _prefix = 'ncs5500-coherent-node-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Coherent.Nodes.Node.Devicemapping.DevMap, self).__init__()

                        self.yang_name = "dev-map"
                        self.yang_parent_name = "devicemapping"

                        self.device_address = YLeaf(YType.uint32, "device-address")

                        self.ifhandle = YLeaf(YType.uint32, "ifhandle")

                        self.intf_name = YLeaf(YType.str, "intf-name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("device_address",
                                        "ifhandle",
                                        "intf_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Coherent.Nodes.Node.Devicemapping.DevMap, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Coherent.Nodes.Node.Devicemapping.DevMap, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.device_address.is_set or
                            self.ifhandle.is_set or
                            self.intf_name.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.device_address.yfilter != YFilter.not_set or
                            self.ifhandle.yfilter != YFilter.not_set or
                            self.intf_name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "dev-map" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.device_address.is_set or self.device_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.device_address.get_name_leafdata())
                        if (self.ifhandle.is_set or self.ifhandle.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ifhandle.get_name_leafdata())
                        if (self.intf_name.is_set or self.intf_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.intf_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "device-address" or name == "ifhandle" or name == "intf-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "device-address"):
                            self.device_address = value
                            self.device_address.value_namespace = name_space
                            self.device_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "ifhandle"):
                            self.ifhandle = value
                            self.ifhandle.value_namespace = name_space
                            self.ifhandle.value_namespace_prefix = name_space_prefix
                        if(value_path == "intf-name"):
                            self.intf_name = value
                            self.intf_name.value_namespace = name_space
                            self.intf_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.dev_map:
                        if (c.has_data()):
                            return True
                    return self.num_entries.is_set

                def has_operation(self):
                    for c in self.dev_map:
                        if (c.has_operation()):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.num_entries.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "devicemapping" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.num_entries.is_set or self.num_entries.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.num_entries.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "dev-map"):
                        for c in self.dev_map:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Coherent.Nodes.Node.Devicemapping.DevMap()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.dev_map.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "dev-map" or name == "num-entries"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "num-entries"):
                        self.num_entries = value
                        self.num_entries.value_namespace = name_space
                        self.num_entries.value_namespace_prefix = name_space_prefix


            class Coherenthealth(Entity):
                """
                Coherent node data for driver health
                
                .. attribute:: aipc_srvr_state
                
                	aipc srvr state
                	**type**\:  bool
                
                .. attribute:: board_type
                
                	board type
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: denali0_version
                
                	denali0 version
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: denali1_version
                
                	denali1 version
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: denali2_version
                
                	denali2 version
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: dsp_ea_conn
                
                	dsp ea conn
                	**type**\:  bool
                
                .. attribute:: fpd_in_progress
                
                	fpd in progress
                	**type**\:  bool
                
                .. attribute:: im_state
                
                	im state
                	**type**\:  bool
                
                .. attribute:: inside_prov_loop
                
                	inside prov loop
                	**type**\:  bool
                
                .. attribute:: jlink_op
                
                	jlink op
                	**type**\:  str
                
                	**length:** 0..6144
                
                .. attribute:: morgoth_alive
                
                	morgoth alive
                	**type**\:  bool
                
                .. attribute:: morgoth_downloaded_version
                
                	morgoth downloaded version
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: morgoth_golden_version
                
                	morgoth golden version
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: morgoth_running_version
                
                	morgoth running version
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: optics_ea_conn
                
                	optics ea conn
                	**type**\:  bool
                
                .. attribute:: pending_provision
                
                	pending provision
                	**type**\:  bool
                
                .. attribute:: pm_state
                
                	pm state
                	**type**\:  bool
                
                .. attribute:: port_data
                
                	port data
                	**type**\: list of    :py:class:`PortData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.Coherenthealth.PortData>`
                
                .. attribute:: prov_infra_state
                
                	prov infra state
                	**type**\:  bool
                
                .. attribute:: prov_run_count
                
                	prov run count
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pulse_sent
                
                	pulse sent
                	**type**\:  bool
                
                .. attribute:: sdk_fpga_compatible
                
                	sdk fpga compatible
                	**type**\:  bool
                
                .. attribute:: sdk_version
                
                	sdk version
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: sysdb_state
                
                	sysdb state
                	**type**\:  bool
                
                .. attribute:: vether_state
                
                	vether state
                	**type**\:  bool
                
                

                """

                _prefix = 'ncs5500-coherent-node-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Coherent.Nodes.Node.Coherenthealth, self).__init__()

                    self.yang_name = "coherenthealth"
                    self.yang_parent_name = "node"

                    self.aipc_srvr_state = YLeaf(YType.boolean, "aipc-srvr-state")

                    self.board_type = YLeaf(YType.str, "board-type")

                    self.denali0_version = YLeaf(YType.str, "denali0-version")

                    self.denali1_version = YLeaf(YType.str, "denali1-version")

                    self.denali2_version = YLeaf(YType.str, "denali2-version")

                    self.dsp_ea_conn = YLeaf(YType.boolean, "dsp-ea-conn")

                    self.fpd_in_progress = YLeaf(YType.boolean, "fpd-in-progress")

                    self.im_state = YLeaf(YType.boolean, "im-state")

                    self.inside_prov_loop = YLeaf(YType.boolean, "inside-prov-loop")

                    self.jlink_op = YLeaf(YType.str, "jlink-op")

                    self.morgoth_alive = YLeaf(YType.boolean, "morgoth-alive")

                    self.morgoth_downloaded_version = YLeaf(YType.str, "morgoth-downloaded-version")

                    self.morgoth_golden_version = YLeaf(YType.str, "morgoth-golden-version")

                    self.morgoth_running_version = YLeaf(YType.str, "morgoth-running-version")

                    self.optics_ea_conn = YLeaf(YType.boolean, "optics-ea-conn")

                    self.pending_provision = YLeaf(YType.boolean, "pending-provision")

                    self.pm_state = YLeaf(YType.boolean, "pm-state")

                    self.prov_infra_state = YLeaf(YType.boolean, "prov-infra-state")

                    self.prov_run_count = YLeaf(YType.uint32, "prov-run-count")

                    self.pulse_sent = YLeaf(YType.boolean, "pulse-sent")

                    self.sdk_fpga_compatible = YLeaf(YType.boolean, "sdk-fpga-compatible")

                    self.sdk_version = YLeaf(YType.str, "sdk-version")

                    self.sysdb_state = YLeaf(YType.boolean, "sysdb-state")

                    self.vether_state = YLeaf(YType.boolean, "vether-state")

                    self.port_data = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("aipc_srvr_state",
                                    "board_type",
                                    "denali0_version",
                                    "denali1_version",
                                    "denali2_version",
                                    "dsp_ea_conn",
                                    "fpd_in_progress",
                                    "im_state",
                                    "inside_prov_loop",
                                    "jlink_op",
                                    "morgoth_alive",
                                    "morgoth_downloaded_version",
                                    "morgoth_golden_version",
                                    "morgoth_running_version",
                                    "optics_ea_conn",
                                    "pending_provision",
                                    "pm_state",
                                    "prov_infra_state",
                                    "prov_run_count",
                                    "pulse_sent",
                                    "sdk_fpga_compatible",
                                    "sdk_version",
                                    "sysdb_state",
                                    "vether_state") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Coherent.Nodes.Node.Coherenthealth, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Coherent.Nodes.Node.Coherenthealth, self).__setattr__(name, value)


                class PortData(Entity):
                    """
                    port data
                    
                    .. attribute:: cd_max_op_rc
                    
                    	cd max op rc
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: cd_min_op_rc
                    
                    	cd min op rc
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: configured_cd_max
                    
                    	configured cd max
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: configured_cd_min
                    
                    	configured cd min
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: configured_frequency
                    
                    	configured frequency
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: configured_loopback_mode
                    
                    	configured loopback mode
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: configured_traffic_type
                    
                    	configured traffic type
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: configured_tx_power
                    
                    	configured tx power
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: ctp2_hw_alarms
                    
                    	ctp2 hw alarms
                    	**type**\:  str
                    
                    	**length:** 0..128
                    
                    .. attribute:: ctp_info
                    
                    	ctp info
                    	**type**\:   :py:class:`CtpInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.Coherenthealth.PortData.CtpInfo>`
                    
                    .. attribute:: denali_hw_alarms
                    
                    	denali hw alarms
                    	**type**\:  str
                    
                    	**length:** 0..256
                    
                    .. attribute:: dsp_admin_up
                    
                    	dsp admin up
                    	**type**\:  bool
                    
                    .. attribute:: dsp_ctrl_created
                    
                    	dsp ctrl created
                    	**type**\:  bool
                    
                    .. attribute:: expected_ctp2_led_state
                    
                    	expected ctp2 led state
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: force_reprovision
                    
                    	force reprovision
                    	**type**\:  bool
                    
                    .. attribute:: fp_port_idx
                    
                    	fp port idx
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: has_pluggable
                    
                    	has pluggable
                    	**type**\:  bool
                    
                    .. attribute:: interface_info
                    
                    	interface info
                    	**type**\:   :py:class:`InterfaceInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.Coherenthealth.PortData.InterfaceInfo>`
                    
                    .. attribute:: is_alarm_port_created_dsp
                    
                    	is alarm port created dsp
                    	**type**\:  bool
                    
                    .. attribute:: is_alarm_port_created_opt
                    
                    	is alarm port created opt
                    	**type**\:  bool
                    
                    .. attribute:: is_pm_port_created_dsp
                    
                    	is pm port created dsp
                    	**type**\:  bool
                    
                    .. attribute:: is_pm_port_created_opt
                    
                    	is pm port created opt
                    	**type**\:  bool
                    
                    .. attribute:: laser_on_pending
                    
                    	laser on pending
                    	**type**\:  bool
                    
                    .. attribute:: laser_op_rc
                    
                    	laser op rc
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: laser_state
                    
                    	laser state
                    	**type**\:  bool
                    
                    .. attribute:: led_op_rc
                    
                    	led op rc
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: loopback_op_rc
                    
                    	loopback op rc
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: optics_admin_up
                    
                    	optics admin up
                    	**type**\:  bool
                    
                    .. attribute:: optics_ctrl_created
                    
                    	optics ctrl created
                    	**type**\:  bool
                    
                    .. attribute:: pm_port_state_dsp
                    
                    	pm port state dsp
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: pm_port_state_opt
                    
                    	pm port state opt
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: provisioned_cd_max
                    
                    	provisioned cd max
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: provisioned_cd_min
                    
                    	provisioned cd min
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: provisioned_ctp2_led_state
                    
                    	provisioned ctp2 led state
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: provisioned_frequency
                    
                    	provisioned frequency
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: provisioned_loopback_mode
                    
                    	provisioned loopback mode
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: provisioned_traffic_type
                    
                    	provisioned traffic type
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: provisioned_tx_power
                    
                    	provisioned tx power
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: provisioning_failed
                    
                    	provisioning failed
                    	**type**\:  bool
                    
                    .. attribute:: provisioning_needed
                    
                    	provisioning needed
                    	**type**\:  bool
                    
                    .. attribute:: rc_alarm_port_dsp
                    
                    	rc alarm port dsp
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: rc_alarm_port_opt
                    
                    	rc alarm port opt
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: rc_pm_port_dsp
                    
                    	rc pm port dsp
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: rc_pm_port_opt
                    
                    	rc pm port opt
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: rc_pm_provision_dsp
                    
                    	rc pm provision dsp
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: rc_pm_provision_opt
                    
                    	rc pm provision opt
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: traffic_op_rc
                    
                    	traffic op rc
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: tx_power_op_rc
                    
                    	tx power op rc
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: wlen_op_rc
                    
                    	wlen op rc
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    

                    """

                    _prefix = 'ncs5500-coherent-node-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Coherent.Nodes.Node.Coherenthealth.PortData, self).__init__()

                        self.yang_name = "port-data"
                        self.yang_parent_name = "coherenthealth"

                        self.cd_max_op_rc = YLeaf(YType.int32, "cd-max-op-rc")

                        self.cd_min_op_rc = YLeaf(YType.int32, "cd-min-op-rc")

                        self.configured_cd_max = YLeaf(YType.uint32, "configured-cd-max")

                        self.configured_cd_min = YLeaf(YType.uint32, "configured-cd-min")

                        self.configured_frequency = YLeaf(YType.uint32, "configured-frequency")

                        self.configured_loopback_mode = YLeaf(YType.uint32, "configured-loopback-mode")

                        self.configured_traffic_type = YLeaf(YType.uint32, "configured-traffic-type")

                        self.configured_tx_power = YLeaf(YType.int32, "configured-tx-power")

                        self.ctp2_hw_alarms = YLeaf(YType.str, "ctp2-hw-alarms")

                        self.denali_hw_alarms = YLeaf(YType.str, "denali-hw-alarms")

                        self.dsp_admin_up = YLeaf(YType.boolean, "dsp-admin-up")

                        self.dsp_ctrl_created = YLeaf(YType.boolean, "dsp-ctrl-created")

                        self.expected_ctp2_led_state = YLeaf(YType.int32, "expected-ctp2-led-state")

                        self.force_reprovision = YLeaf(YType.boolean, "force-reprovision")

                        self.fp_port_idx = YLeaf(YType.uint32, "fp-port-idx")

                        self.has_pluggable = YLeaf(YType.boolean, "has-pluggable")

                        self.is_alarm_port_created_dsp = YLeaf(YType.boolean, "is-alarm-port-created-dsp")

                        self.is_alarm_port_created_opt = YLeaf(YType.boolean, "is-alarm-port-created-opt")

                        self.is_pm_port_created_dsp = YLeaf(YType.boolean, "is-pm-port-created-dsp")

                        self.is_pm_port_created_opt = YLeaf(YType.boolean, "is-pm-port-created-opt")

                        self.laser_on_pending = YLeaf(YType.boolean, "laser-on-pending")

                        self.laser_op_rc = YLeaf(YType.int32, "laser-op-rc")

                        self.laser_state = YLeaf(YType.boolean, "laser-state")

                        self.led_op_rc = YLeaf(YType.int32, "led-op-rc")

                        self.loopback_op_rc = YLeaf(YType.int32, "loopback-op-rc")

                        self.optics_admin_up = YLeaf(YType.boolean, "optics-admin-up")

                        self.optics_ctrl_created = YLeaf(YType.boolean, "optics-ctrl-created")

                        self.pm_port_state_dsp = YLeaf(YType.int32, "pm-port-state-dsp")

                        self.pm_port_state_opt = YLeaf(YType.int32, "pm-port-state-opt")

                        self.provisioned_cd_max = YLeaf(YType.uint32, "provisioned-cd-max")

                        self.provisioned_cd_min = YLeaf(YType.uint32, "provisioned-cd-min")

                        self.provisioned_ctp2_led_state = YLeaf(YType.int32, "provisioned-ctp2-led-state")

                        self.provisioned_frequency = YLeaf(YType.uint32, "provisioned-frequency")

                        self.provisioned_loopback_mode = YLeaf(YType.uint32, "provisioned-loopback-mode")

                        self.provisioned_traffic_type = YLeaf(YType.uint32, "provisioned-traffic-type")

                        self.provisioned_tx_power = YLeaf(YType.int32, "provisioned-tx-power")

                        self.provisioning_failed = YLeaf(YType.boolean, "provisioning-failed")

                        self.provisioning_needed = YLeaf(YType.boolean, "provisioning-needed")

                        self.rc_alarm_port_dsp = YLeaf(YType.int32, "rc-alarm-port-dsp")

                        self.rc_alarm_port_opt = YLeaf(YType.int32, "rc-alarm-port-opt")

                        self.rc_pm_port_dsp = YLeaf(YType.int32, "rc-pm-port-dsp")

                        self.rc_pm_port_opt = YLeaf(YType.int32, "rc-pm-port-opt")

                        self.rc_pm_provision_dsp = YLeaf(YType.int32, "rc-pm-provision-dsp")

                        self.rc_pm_provision_opt = YLeaf(YType.int32, "rc-pm-provision-opt")

                        self.traffic_op_rc = YLeaf(YType.int32, "traffic-op-rc")

                        self.tx_power_op_rc = YLeaf(YType.int32, "tx-power-op-rc")

                        self.wlen_op_rc = YLeaf(YType.int32, "wlen-op-rc")

                        self.ctp_info = Coherent.Nodes.Node.Coherenthealth.PortData.CtpInfo()
                        self.ctp_info.parent = self
                        self._children_name_map["ctp_info"] = "ctp-info"
                        self._children_yang_names.add("ctp-info")

                        self.interface_info = Coherent.Nodes.Node.Coherenthealth.PortData.InterfaceInfo()
                        self.interface_info.parent = self
                        self._children_name_map["interface_info"] = "interface-info"
                        self._children_yang_names.add("interface-info")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("cd_max_op_rc",
                                        "cd_min_op_rc",
                                        "configured_cd_max",
                                        "configured_cd_min",
                                        "configured_frequency",
                                        "configured_loopback_mode",
                                        "configured_traffic_type",
                                        "configured_tx_power",
                                        "ctp2_hw_alarms",
                                        "denali_hw_alarms",
                                        "dsp_admin_up",
                                        "dsp_ctrl_created",
                                        "expected_ctp2_led_state",
                                        "force_reprovision",
                                        "fp_port_idx",
                                        "has_pluggable",
                                        "is_alarm_port_created_dsp",
                                        "is_alarm_port_created_opt",
                                        "is_pm_port_created_dsp",
                                        "is_pm_port_created_opt",
                                        "laser_on_pending",
                                        "laser_op_rc",
                                        "laser_state",
                                        "led_op_rc",
                                        "loopback_op_rc",
                                        "optics_admin_up",
                                        "optics_ctrl_created",
                                        "pm_port_state_dsp",
                                        "pm_port_state_opt",
                                        "provisioned_cd_max",
                                        "provisioned_cd_min",
                                        "provisioned_ctp2_led_state",
                                        "provisioned_frequency",
                                        "provisioned_loopback_mode",
                                        "provisioned_traffic_type",
                                        "provisioned_tx_power",
                                        "provisioning_failed",
                                        "provisioning_needed",
                                        "rc_alarm_port_dsp",
                                        "rc_alarm_port_opt",
                                        "rc_pm_port_dsp",
                                        "rc_pm_port_opt",
                                        "rc_pm_provision_dsp",
                                        "rc_pm_provision_opt",
                                        "traffic_op_rc",
                                        "tx_power_op_rc",
                                        "wlen_op_rc") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Coherent.Nodes.Node.Coherenthealth.PortData, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Coherent.Nodes.Node.Coherenthealth.PortData, self).__setattr__(name, value)


                    class CtpInfo(Entity):
                        """
                        ctp info
                        
                        .. attribute:: clei_code_number
                        
                        	CLEI code number
                        	**type**\:  str
                        
                        	**length:** 0..10
                        
                        .. attribute:: ctp_type
                        
                        	ctp type
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: date_code_number
                        
                        	date code number
                        	**type**\:  str
                        
                        	**length:** 0..10
                        
                        .. attribute:: description
                        
                        	description
                        	**type**\:  str
                        
                        	**length:** 0..64
                        
                        .. attribute:: deviation
                        
                        	deviation
                        	**type**\:  str
                        
                        	**length:** 0..16
                        
                        .. attribute:: module_firmware_committed_version_number
                        
                        	module firmware committed version number
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: module_firmware_running_version_number
                        
                        	module firmware running version number
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: module_hardware_version_number
                        
                        	module hardware version number
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: part_number
                        
                        	part number
                        	**type**\:  str
                        
                        	**length:** 0..16
                        
                        .. attribute:: pid
                        
                        	pid
                        	**type**\:  str
                        
                        	**length:** 0..16
                        
                        .. attribute:: serial_number
                        
                        	serial number
                        	**type**\:  str
                        
                        	**length:** 0..16
                        
                        .. attribute:: vendorname
                        
                        	vendorname
                        	**type**\:  str
                        
                        	**length:** 0..16
                        
                        .. attribute:: vid
                        
                        	vid
                        	**type**\:  str
                        
                        	**length:** 0..16
                        
                        

                        """

                        _prefix = 'ncs5500-coherent-node-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Coherent.Nodes.Node.Coherenthealth.PortData.CtpInfo, self).__init__()

                            self.yang_name = "ctp-info"
                            self.yang_parent_name = "port-data"

                            self.clei_code_number = YLeaf(YType.str, "clei-code-number")

                            self.ctp_type = YLeaf(YType.uint32, "ctp-type")

                            self.date_code_number = YLeaf(YType.str, "date-code-number")

                            self.description = YLeaf(YType.str, "description")

                            self.deviation = YLeaf(YType.str, "deviation")

                            self.module_firmware_committed_version_number = YLeaf(YType.uint16, "module-firmware-committed-version-number")

                            self.module_firmware_running_version_number = YLeaf(YType.uint16, "module-firmware-running-version-number")

                            self.module_hardware_version_number = YLeaf(YType.uint16, "module-hardware-version-number")

                            self.part_number = YLeaf(YType.str, "part-number")

                            self.pid = YLeaf(YType.str, "pid")

                            self.serial_number = YLeaf(YType.str, "serial-number")

                            self.vendorname = YLeaf(YType.str, "vendorname")

                            self.vid = YLeaf(YType.str, "vid")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("clei_code_number",
                                            "ctp_type",
                                            "date_code_number",
                                            "description",
                                            "deviation",
                                            "module_firmware_committed_version_number",
                                            "module_firmware_running_version_number",
                                            "module_hardware_version_number",
                                            "part_number",
                                            "pid",
                                            "serial_number",
                                            "vendorname",
                                            "vid") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Coherent.Nodes.Node.Coherenthealth.PortData.CtpInfo, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Coherent.Nodes.Node.Coherenthealth.PortData.CtpInfo, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.clei_code_number.is_set or
                                self.ctp_type.is_set or
                                self.date_code_number.is_set or
                                self.description.is_set or
                                self.deviation.is_set or
                                self.module_firmware_committed_version_number.is_set or
                                self.module_firmware_running_version_number.is_set or
                                self.module_hardware_version_number.is_set or
                                self.part_number.is_set or
                                self.pid.is_set or
                                self.serial_number.is_set or
                                self.vendorname.is_set or
                                self.vid.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.clei_code_number.yfilter != YFilter.not_set or
                                self.ctp_type.yfilter != YFilter.not_set or
                                self.date_code_number.yfilter != YFilter.not_set or
                                self.description.yfilter != YFilter.not_set or
                                self.deviation.yfilter != YFilter.not_set or
                                self.module_firmware_committed_version_number.yfilter != YFilter.not_set or
                                self.module_firmware_running_version_number.yfilter != YFilter.not_set or
                                self.module_hardware_version_number.yfilter != YFilter.not_set or
                                self.part_number.yfilter != YFilter.not_set or
                                self.pid.yfilter != YFilter.not_set or
                                self.serial_number.yfilter != YFilter.not_set or
                                self.vendorname.yfilter != YFilter.not_set or
                                self.vid.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "ctp-info" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.clei_code_number.is_set or self.clei_code_number.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.clei_code_number.get_name_leafdata())
                            if (self.ctp_type.is_set or self.ctp_type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ctp_type.get_name_leafdata())
                            if (self.date_code_number.is_set or self.date_code_number.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.date_code_number.get_name_leafdata())
                            if (self.description.is_set or self.description.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.description.get_name_leafdata())
                            if (self.deviation.is_set or self.deviation.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.deviation.get_name_leafdata())
                            if (self.module_firmware_committed_version_number.is_set or self.module_firmware_committed_version_number.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.module_firmware_committed_version_number.get_name_leafdata())
                            if (self.module_firmware_running_version_number.is_set or self.module_firmware_running_version_number.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.module_firmware_running_version_number.get_name_leafdata())
                            if (self.module_hardware_version_number.is_set or self.module_hardware_version_number.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.module_hardware_version_number.get_name_leafdata())
                            if (self.part_number.is_set or self.part_number.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.part_number.get_name_leafdata())
                            if (self.pid.is_set or self.pid.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.pid.get_name_leafdata())
                            if (self.serial_number.is_set or self.serial_number.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.serial_number.get_name_leafdata())
                            if (self.vendorname.is_set or self.vendorname.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.vendorname.get_name_leafdata())
                            if (self.vid.is_set or self.vid.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.vid.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "clei-code-number" or name == "ctp-type" or name == "date-code-number" or name == "description" or name == "deviation" or name == "module-firmware-committed-version-number" or name == "module-firmware-running-version-number" or name == "module-hardware-version-number" or name == "part-number" or name == "pid" or name == "serial-number" or name == "vendorname" or name == "vid"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "clei-code-number"):
                                self.clei_code_number = value
                                self.clei_code_number.value_namespace = name_space
                                self.clei_code_number.value_namespace_prefix = name_space_prefix
                            if(value_path == "ctp-type"):
                                self.ctp_type = value
                                self.ctp_type.value_namespace = name_space
                                self.ctp_type.value_namespace_prefix = name_space_prefix
                            if(value_path == "date-code-number"):
                                self.date_code_number = value
                                self.date_code_number.value_namespace = name_space
                                self.date_code_number.value_namespace_prefix = name_space_prefix
                            if(value_path == "description"):
                                self.description = value
                                self.description.value_namespace = name_space
                                self.description.value_namespace_prefix = name_space_prefix
                            if(value_path == "deviation"):
                                self.deviation = value
                                self.deviation.value_namespace = name_space
                                self.deviation.value_namespace_prefix = name_space_prefix
                            if(value_path == "module-firmware-committed-version-number"):
                                self.module_firmware_committed_version_number = value
                                self.module_firmware_committed_version_number.value_namespace = name_space
                                self.module_firmware_committed_version_number.value_namespace_prefix = name_space_prefix
                            if(value_path == "module-firmware-running-version-number"):
                                self.module_firmware_running_version_number = value
                                self.module_firmware_running_version_number.value_namespace = name_space
                                self.module_firmware_running_version_number.value_namespace_prefix = name_space_prefix
                            if(value_path == "module-hardware-version-number"):
                                self.module_hardware_version_number = value
                                self.module_hardware_version_number.value_namespace = name_space
                                self.module_hardware_version_number.value_namespace_prefix = name_space_prefix
                            if(value_path == "part-number"):
                                self.part_number = value
                                self.part_number.value_namespace = name_space
                                self.part_number.value_namespace_prefix = name_space_prefix
                            if(value_path == "pid"):
                                self.pid = value
                                self.pid.value_namespace = name_space
                                self.pid.value_namespace_prefix = name_space_prefix
                            if(value_path == "serial-number"):
                                self.serial_number = value
                                self.serial_number.value_namespace = name_space
                                self.serial_number.value_namespace_prefix = name_space_prefix
                            if(value_path == "vendorname"):
                                self.vendorname = value
                                self.vendorname.value_namespace = name_space
                                self.vendorname.value_namespace_prefix = name_space_prefix
                            if(value_path == "vid"):
                                self.vid = value
                                self.vid.value_namespace = name_space
                                self.vid.value_namespace_prefix = name_space_prefix


                    class InterfaceInfo(Entity):
                        """
                        interface info
                        
                        .. attribute:: eth_data
                        
                        	eth data
                        	**type**\: list of    :py:class:`EthData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.Coherenthealth.PortData.InterfaceInfo.EthData>`
                        
                        

                        """

                        _prefix = 'ncs5500-coherent-node-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Coherent.Nodes.Node.Coherenthealth.PortData.InterfaceInfo, self).__init__()

                            self.yang_name = "interface-info"
                            self.yang_parent_name = "port-data"

                            self.eth_data = YList(self)

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
                                        super(Coherent.Nodes.Node.Coherenthealth.PortData.InterfaceInfo, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Coherent.Nodes.Node.Coherenthealth.PortData.InterfaceInfo, self).__setattr__(name, value)


                        class EthData(Entity):
                            """
                            eth data
                            
                            .. attribute:: admin_state
                            
                            	admin state
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: admin_up
                            
                            	admin up
                            	**type**\:  bool
                            
                            .. attribute:: ifname
                            
                            	ifname
                            	**type**\:  str
                            
                            	**length:** 0..64
                            
                            .. attribute:: intf_handle
                            
                            	intf handle
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: is_created
                            
                            	is created
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'ncs5500-coherent-node-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Coherent.Nodes.Node.Coherenthealth.PortData.InterfaceInfo.EthData, self).__init__()

                                self.yang_name = "eth-data"
                                self.yang_parent_name = "interface-info"

                                self.admin_state = YLeaf(YType.uint32, "admin-state")

                                self.admin_up = YLeaf(YType.boolean, "admin-up")

                                self.ifname = YLeaf(YType.str, "ifname")

                                self.intf_handle = YLeaf(YType.uint32, "intf-handle")

                                self.is_created = YLeaf(YType.boolean, "is-created")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("admin_state",
                                                "admin_up",
                                                "ifname",
                                                "intf_handle",
                                                "is_created") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Coherent.Nodes.Node.Coherenthealth.PortData.InterfaceInfo.EthData, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Coherent.Nodes.Node.Coherenthealth.PortData.InterfaceInfo.EthData, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.admin_state.is_set or
                                    self.admin_up.is_set or
                                    self.ifname.is_set or
                                    self.intf_handle.is_set or
                                    self.is_created.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.admin_state.yfilter != YFilter.not_set or
                                    self.admin_up.yfilter != YFilter.not_set or
                                    self.ifname.yfilter != YFilter.not_set or
                                    self.intf_handle.yfilter != YFilter.not_set or
                                    self.is_created.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "eth-data" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.admin_state.is_set or self.admin_state.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.admin_state.get_name_leafdata())
                                if (self.admin_up.is_set or self.admin_up.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.admin_up.get_name_leafdata())
                                if (self.ifname.is_set or self.ifname.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ifname.get_name_leafdata())
                                if (self.intf_handle.is_set or self.intf_handle.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.intf_handle.get_name_leafdata())
                                if (self.is_created.is_set or self.is_created.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.is_created.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "admin-state" or name == "admin-up" or name == "ifname" or name == "intf-handle" or name == "is-created"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "admin-state"):
                                    self.admin_state = value
                                    self.admin_state.value_namespace = name_space
                                    self.admin_state.value_namespace_prefix = name_space_prefix
                                if(value_path == "admin-up"):
                                    self.admin_up = value
                                    self.admin_up.value_namespace = name_space
                                    self.admin_up.value_namespace_prefix = name_space_prefix
                                if(value_path == "ifname"):
                                    self.ifname = value
                                    self.ifname.value_namespace = name_space
                                    self.ifname.value_namespace_prefix = name_space_prefix
                                if(value_path == "intf-handle"):
                                    self.intf_handle = value
                                    self.intf_handle.value_namespace = name_space
                                    self.intf_handle.value_namespace_prefix = name_space_prefix
                                if(value_path == "is-created"):
                                    self.is_created = value
                                    self.is_created.value_namespace = name_space
                                    self.is_created.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.eth_data:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.eth_data:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "interface-info" + path_buffer

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

                            if (child_yang_name == "eth-data"):
                                for c in self.eth_data:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Coherent.Nodes.Node.Coherenthealth.PortData.InterfaceInfo.EthData()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.eth_data.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "eth-data"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (
                            self.cd_max_op_rc.is_set or
                            self.cd_min_op_rc.is_set or
                            self.configured_cd_max.is_set or
                            self.configured_cd_min.is_set or
                            self.configured_frequency.is_set or
                            self.configured_loopback_mode.is_set or
                            self.configured_traffic_type.is_set or
                            self.configured_tx_power.is_set or
                            self.ctp2_hw_alarms.is_set or
                            self.denali_hw_alarms.is_set or
                            self.dsp_admin_up.is_set or
                            self.dsp_ctrl_created.is_set or
                            self.expected_ctp2_led_state.is_set or
                            self.force_reprovision.is_set or
                            self.fp_port_idx.is_set or
                            self.has_pluggable.is_set or
                            self.is_alarm_port_created_dsp.is_set or
                            self.is_alarm_port_created_opt.is_set or
                            self.is_pm_port_created_dsp.is_set or
                            self.is_pm_port_created_opt.is_set or
                            self.laser_on_pending.is_set or
                            self.laser_op_rc.is_set or
                            self.laser_state.is_set or
                            self.led_op_rc.is_set or
                            self.loopback_op_rc.is_set or
                            self.optics_admin_up.is_set or
                            self.optics_ctrl_created.is_set or
                            self.pm_port_state_dsp.is_set or
                            self.pm_port_state_opt.is_set or
                            self.provisioned_cd_max.is_set or
                            self.provisioned_cd_min.is_set or
                            self.provisioned_ctp2_led_state.is_set or
                            self.provisioned_frequency.is_set or
                            self.provisioned_loopback_mode.is_set or
                            self.provisioned_traffic_type.is_set or
                            self.provisioned_tx_power.is_set or
                            self.provisioning_failed.is_set or
                            self.provisioning_needed.is_set or
                            self.rc_alarm_port_dsp.is_set or
                            self.rc_alarm_port_opt.is_set or
                            self.rc_pm_port_dsp.is_set or
                            self.rc_pm_port_opt.is_set or
                            self.rc_pm_provision_dsp.is_set or
                            self.rc_pm_provision_opt.is_set or
                            self.traffic_op_rc.is_set or
                            self.tx_power_op_rc.is_set or
                            self.wlen_op_rc.is_set or
                            (self.ctp_info is not None and self.ctp_info.has_data()) or
                            (self.interface_info is not None and self.interface_info.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.cd_max_op_rc.yfilter != YFilter.not_set or
                            self.cd_min_op_rc.yfilter != YFilter.not_set or
                            self.configured_cd_max.yfilter != YFilter.not_set or
                            self.configured_cd_min.yfilter != YFilter.not_set or
                            self.configured_frequency.yfilter != YFilter.not_set or
                            self.configured_loopback_mode.yfilter != YFilter.not_set or
                            self.configured_traffic_type.yfilter != YFilter.not_set or
                            self.configured_tx_power.yfilter != YFilter.not_set or
                            self.ctp2_hw_alarms.yfilter != YFilter.not_set or
                            self.denali_hw_alarms.yfilter != YFilter.not_set or
                            self.dsp_admin_up.yfilter != YFilter.not_set or
                            self.dsp_ctrl_created.yfilter != YFilter.not_set or
                            self.expected_ctp2_led_state.yfilter != YFilter.not_set or
                            self.force_reprovision.yfilter != YFilter.not_set or
                            self.fp_port_idx.yfilter != YFilter.not_set or
                            self.has_pluggable.yfilter != YFilter.not_set or
                            self.is_alarm_port_created_dsp.yfilter != YFilter.not_set or
                            self.is_alarm_port_created_opt.yfilter != YFilter.not_set or
                            self.is_pm_port_created_dsp.yfilter != YFilter.not_set or
                            self.is_pm_port_created_opt.yfilter != YFilter.not_set or
                            self.laser_on_pending.yfilter != YFilter.not_set or
                            self.laser_op_rc.yfilter != YFilter.not_set or
                            self.laser_state.yfilter != YFilter.not_set or
                            self.led_op_rc.yfilter != YFilter.not_set or
                            self.loopback_op_rc.yfilter != YFilter.not_set or
                            self.optics_admin_up.yfilter != YFilter.not_set or
                            self.optics_ctrl_created.yfilter != YFilter.not_set or
                            self.pm_port_state_dsp.yfilter != YFilter.not_set or
                            self.pm_port_state_opt.yfilter != YFilter.not_set or
                            self.provisioned_cd_max.yfilter != YFilter.not_set or
                            self.provisioned_cd_min.yfilter != YFilter.not_set or
                            self.provisioned_ctp2_led_state.yfilter != YFilter.not_set or
                            self.provisioned_frequency.yfilter != YFilter.not_set or
                            self.provisioned_loopback_mode.yfilter != YFilter.not_set or
                            self.provisioned_traffic_type.yfilter != YFilter.not_set or
                            self.provisioned_tx_power.yfilter != YFilter.not_set or
                            self.provisioning_failed.yfilter != YFilter.not_set or
                            self.provisioning_needed.yfilter != YFilter.not_set or
                            self.rc_alarm_port_dsp.yfilter != YFilter.not_set or
                            self.rc_alarm_port_opt.yfilter != YFilter.not_set or
                            self.rc_pm_port_dsp.yfilter != YFilter.not_set or
                            self.rc_pm_port_opt.yfilter != YFilter.not_set or
                            self.rc_pm_provision_dsp.yfilter != YFilter.not_set or
                            self.rc_pm_provision_opt.yfilter != YFilter.not_set or
                            self.traffic_op_rc.yfilter != YFilter.not_set or
                            self.tx_power_op_rc.yfilter != YFilter.not_set or
                            self.wlen_op_rc.yfilter != YFilter.not_set or
                            (self.ctp_info is not None and self.ctp_info.has_operation()) or
                            (self.interface_info is not None and self.interface_info.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "port-data" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.cd_max_op_rc.is_set or self.cd_max_op_rc.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.cd_max_op_rc.get_name_leafdata())
                        if (self.cd_min_op_rc.is_set or self.cd_min_op_rc.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.cd_min_op_rc.get_name_leafdata())
                        if (self.configured_cd_max.is_set or self.configured_cd_max.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.configured_cd_max.get_name_leafdata())
                        if (self.configured_cd_min.is_set or self.configured_cd_min.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.configured_cd_min.get_name_leafdata())
                        if (self.configured_frequency.is_set or self.configured_frequency.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.configured_frequency.get_name_leafdata())
                        if (self.configured_loopback_mode.is_set or self.configured_loopback_mode.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.configured_loopback_mode.get_name_leafdata())
                        if (self.configured_traffic_type.is_set or self.configured_traffic_type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.configured_traffic_type.get_name_leafdata())
                        if (self.configured_tx_power.is_set or self.configured_tx_power.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.configured_tx_power.get_name_leafdata())
                        if (self.ctp2_hw_alarms.is_set or self.ctp2_hw_alarms.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ctp2_hw_alarms.get_name_leafdata())
                        if (self.denali_hw_alarms.is_set or self.denali_hw_alarms.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.denali_hw_alarms.get_name_leafdata())
                        if (self.dsp_admin_up.is_set or self.dsp_admin_up.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.dsp_admin_up.get_name_leafdata())
                        if (self.dsp_ctrl_created.is_set or self.dsp_ctrl_created.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.dsp_ctrl_created.get_name_leafdata())
                        if (self.expected_ctp2_led_state.is_set or self.expected_ctp2_led_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.expected_ctp2_led_state.get_name_leafdata())
                        if (self.force_reprovision.is_set or self.force_reprovision.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.force_reprovision.get_name_leafdata())
                        if (self.fp_port_idx.is_set or self.fp_port_idx.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.fp_port_idx.get_name_leafdata())
                        if (self.has_pluggable.is_set or self.has_pluggable.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.has_pluggable.get_name_leafdata())
                        if (self.is_alarm_port_created_dsp.is_set or self.is_alarm_port_created_dsp.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.is_alarm_port_created_dsp.get_name_leafdata())
                        if (self.is_alarm_port_created_opt.is_set or self.is_alarm_port_created_opt.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.is_alarm_port_created_opt.get_name_leafdata())
                        if (self.is_pm_port_created_dsp.is_set or self.is_pm_port_created_dsp.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.is_pm_port_created_dsp.get_name_leafdata())
                        if (self.is_pm_port_created_opt.is_set or self.is_pm_port_created_opt.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.is_pm_port_created_opt.get_name_leafdata())
                        if (self.laser_on_pending.is_set or self.laser_on_pending.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.laser_on_pending.get_name_leafdata())
                        if (self.laser_op_rc.is_set or self.laser_op_rc.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.laser_op_rc.get_name_leafdata())
                        if (self.laser_state.is_set or self.laser_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.laser_state.get_name_leafdata())
                        if (self.led_op_rc.is_set or self.led_op_rc.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.led_op_rc.get_name_leafdata())
                        if (self.loopback_op_rc.is_set or self.loopback_op_rc.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.loopback_op_rc.get_name_leafdata())
                        if (self.optics_admin_up.is_set or self.optics_admin_up.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.optics_admin_up.get_name_leafdata())
                        if (self.optics_ctrl_created.is_set or self.optics_ctrl_created.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.optics_ctrl_created.get_name_leafdata())
                        if (self.pm_port_state_dsp.is_set or self.pm_port_state_dsp.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pm_port_state_dsp.get_name_leafdata())
                        if (self.pm_port_state_opt.is_set or self.pm_port_state_opt.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pm_port_state_opt.get_name_leafdata())
                        if (self.provisioned_cd_max.is_set or self.provisioned_cd_max.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.provisioned_cd_max.get_name_leafdata())
                        if (self.provisioned_cd_min.is_set or self.provisioned_cd_min.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.provisioned_cd_min.get_name_leafdata())
                        if (self.provisioned_ctp2_led_state.is_set or self.provisioned_ctp2_led_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.provisioned_ctp2_led_state.get_name_leafdata())
                        if (self.provisioned_frequency.is_set or self.provisioned_frequency.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.provisioned_frequency.get_name_leafdata())
                        if (self.provisioned_loopback_mode.is_set or self.provisioned_loopback_mode.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.provisioned_loopback_mode.get_name_leafdata())
                        if (self.provisioned_traffic_type.is_set or self.provisioned_traffic_type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.provisioned_traffic_type.get_name_leafdata())
                        if (self.provisioned_tx_power.is_set or self.provisioned_tx_power.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.provisioned_tx_power.get_name_leafdata())
                        if (self.provisioning_failed.is_set or self.provisioning_failed.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.provisioning_failed.get_name_leafdata())
                        if (self.provisioning_needed.is_set or self.provisioning_needed.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.provisioning_needed.get_name_leafdata())
                        if (self.rc_alarm_port_dsp.is_set or self.rc_alarm_port_dsp.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.rc_alarm_port_dsp.get_name_leafdata())
                        if (self.rc_alarm_port_opt.is_set or self.rc_alarm_port_opt.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.rc_alarm_port_opt.get_name_leafdata())
                        if (self.rc_pm_port_dsp.is_set or self.rc_pm_port_dsp.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.rc_pm_port_dsp.get_name_leafdata())
                        if (self.rc_pm_port_opt.is_set or self.rc_pm_port_opt.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.rc_pm_port_opt.get_name_leafdata())
                        if (self.rc_pm_provision_dsp.is_set or self.rc_pm_provision_dsp.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.rc_pm_provision_dsp.get_name_leafdata())
                        if (self.rc_pm_provision_opt.is_set or self.rc_pm_provision_opt.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.rc_pm_provision_opt.get_name_leafdata())
                        if (self.traffic_op_rc.is_set or self.traffic_op_rc.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.traffic_op_rc.get_name_leafdata())
                        if (self.tx_power_op_rc.is_set or self.tx_power_op_rc.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tx_power_op_rc.get_name_leafdata())
                        if (self.wlen_op_rc.is_set or self.wlen_op_rc.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.wlen_op_rc.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "ctp-info"):
                            if (self.ctp_info is None):
                                self.ctp_info = Coherent.Nodes.Node.Coherenthealth.PortData.CtpInfo()
                                self.ctp_info.parent = self
                                self._children_name_map["ctp_info"] = "ctp-info"
                            return self.ctp_info

                        if (child_yang_name == "interface-info"):
                            if (self.interface_info is None):
                                self.interface_info = Coherent.Nodes.Node.Coherenthealth.PortData.InterfaceInfo()
                                self.interface_info.parent = self
                                self._children_name_map["interface_info"] = "interface-info"
                            return self.interface_info

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "ctp-info" or name == "interface-info" or name == "cd-max-op-rc" or name == "cd-min-op-rc" or name == "configured-cd-max" or name == "configured-cd-min" or name == "configured-frequency" or name == "configured-loopback-mode" or name == "configured-traffic-type" or name == "configured-tx-power" or name == "ctp2-hw-alarms" or name == "denali-hw-alarms" or name == "dsp-admin-up" or name == "dsp-ctrl-created" or name == "expected-ctp2-led-state" or name == "force-reprovision" or name == "fp-port-idx" or name == "has-pluggable" or name == "is-alarm-port-created-dsp" or name == "is-alarm-port-created-opt" or name == "is-pm-port-created-dsp" or name == "is-pm-port-created-opt" or name == "laser-on-pending" or name == "laser-op-rc" or name == "laser-state" or name == "led-op-rc" or name == "loopback-op-rc" or name == "optics-admin-up" or name == "optics-ctrl-created" or name == "pm-port-state-dsp" or name == "pm-port-state-opt" or name == "provisioned-cd-max" or name == "provisioned-cd-min" or name == "provisioned-ctp2-led-state" or name == "provisioned-frequency" or name == "provisioned-loopback-mode" or name == "provisioned-traffic-type" or name == "provisioned-tx-power" or name == "provisioning-failed" or name == "provisioning-needed" or name == "rc-alarm-port-dsp" or name == "rc-alarm-port-opt" or name == "rc-pm-port-dsp" or name == "rc-pm-port-opt" or name == "rc-pm-provision-dsp" or name == "rc-pm-provision-opt" or name == "traffic-op-rc" or name == "tx-power-op-rc" or name == "wlen-op-rc"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "cd-max-op-rc"):
                            self.cd_max_op_rc = value
                            self.cd_max_op_rc.value_namespace = name_space
                            self.cd_max_op_rc.value_namespace_prefix = name_space_prefix
                        if(value_path == "cd-min-op-rc"):
                            self.cd_min_op_rc = value
                            self.cd_min_op_rc.value_namespace = name_space
                            self.cd_min_op_rc.value_namespace_prefix = name_space_prefix
                        if(value_path == "configured-cd-max"):
                            self.configured_cd_max = value
                            self.configured_cd_max.value_namespace = name_space
                            self.configured_cd_max.value_namespace_prefix = name_space_prefix
                        if(value_path == "configured-cd-min"):
                            self.configured_cd_min = value
                            self.configured_cd_min.value_namespace = name_space
                            self.configured_cd_min.value_namespace_prefix = name_space_prefix
                        if(value_path == "configured-frequency"):
                            self.configured_frequency = value
                            self.configured_frequency.value_namespace = name_space
                            self.configured_frequency.value_namespace_prefix = name_space_prefix
                        if(value_path == "configured-loopback-mode"):
                            self.configured_loopback_mode = value
                            self.configured_loopback_mode.value_namespace = name_space
                            self.configured_loopback_mode.value_namespace_prefix = name_space_prefix
                        if(value_path == "configured-traffic-type"):
                            self.configured_traffic_type = value
                            self.configured_traffic_type.value_namespace = name_space
                            self.configured_traffic_type.value_namespace_prefix = name_space_prefix
                        if(value_path == "configured-tx-power"):
                            self.configured_tx_power = value
                            self.configured_tx_power.value_namespace = name_space
                            self.configured_tx_power.value_namespace_prefix = name_space_prefix
                        if(value_path == "ctp2-hw-alarms"):
                            self.ctp2_hw_alarms = value
                            self.ctp2_hw_alarms.value_namespace = name_space
                            self.ctp2_hw_alarms.value_namespace_prefix = name_space_prefix
                        if(value_path == "denali-hw-alarms"):
                            self.denali_hw_alarms = value
                            self.denali_hw_alarms.value_namespace = name_space
                            self.denali_hw_alarms.value_namespace_prefix = name_space_prefix
                        if(value_path == "dsp-admin-up"):
                            self.dsp_admin_up = value
                            self.dsp_admin_up.value_namespace = name_space
                            self.dsp_admin_up.value_namespace_prefix = name_space_prefix
                        if(value_path == "dsp-ctrl-created"):
                            self.dsp_ctrl_created = value
                            self.dsp_ctrl_created.value_namespace = name_space
                            self.dsp_ctrl_created.value_namespace_prefix = name_space_prefix
                        if(value_path == "expected-ctp2-led-state"):
                            self.expected_ctp2_led_state = value
                            self.expected_ctp2_led_state.value_namespace = name_space
                            self.expected_ctp2_led_state.value_namespace_prefix = name_space_prefix
                        if(value_path == "force-reprovision"):
                            self.force_reprovision = value
                            self.force_reprovision.value_namespace = name_space
                            self.force_reprovision.value_namespace_prefix = name_space_prefix
                        if(value_path == "fp-port-idx"):
                            self.fp_port_idx = value
                            self.fp_port_idx.value_namespace = name_space
                            self.fp_port_idx.value_namespace_prefix = name_space_prefix
                        if(value_path == "has-pluggable"):
                            self.has_pluggable = value
                            self.has_pluggable.value_namespace = name_space
                            self.has_pluggable.value_namespace_prefix = name_space_prefix
                        if(value_path == "is-alarm-port-created-dsp"):
                            self.is_alarm_port_created_dsp = value
                            self.is_alarm_port_created_dsp.value_namespace = name_space
                            self.is_alarm_port_created_dsp.value_namespace_prefix = name_space_prefix
                        if(value_path == "is-alarm-port-created-opt"):
                            self.is_alarm_port_created_opt = value
                            self.is_alarm_port_created_opt.value_namespace = name_space
                            self.is_alarm_port_created_opt.value_namespace_prefix = name_space_prefix
                        if(value_path == "is-pm-port-created-dsp"):
                            self.is_pm_port_created_dsp = value
                            self.is_pm_port_created_dsp.value_namespace = name_space
                            self.is_pm_port_created_dsp.value_namespace_prefix = name_space_prefix
                        if(value_path == "is-pm-port-created-opt"):
                            self.is_pm_port_created_opt = value
                            self.is_pm_port_created_opt.value_namespace = name_space
                            self.is_pm_port_created_opt.value_namespace_prefix = name_space_prefix
                        if(value_path == "laser-on-pending"):
                            self.laser_on_pending = value
                            self.laser_on_pending.value_namespace = name_space
                            self.laser_on_pending.value_namespace_prefix = name_space_prefix
                        if(value_path == "laser-op-rc"):
                            self.laser_op_rc = value
                            self.laser_op_rc.value_namespace = name_space
                            self.laser_op_rc.value_namespace_prefix = name_space_prefix
                        if(value_path == "laser-state"):
                            self.laser_state = value
                            self.laser_state.value_namespace = name_space
                            self.laser_state.value_namespace_prefix = name_space_prefix
                        if(value_path == "led-op-rc"):
                            self.led_op_rc = value
                            self.led_op_rc.value_namespace = name_space
                            self.led_op_rc.value_namespace_prefix = name_space_prefix
                        if(value_path == "loopback-op-rc"):
                            self.loopback_op_rc = value
                            self.loopback_op_rc.value_namespace = name_space
                            self.loopback_op_rc.value_namespace_prefix = name_space_prefix
                        if(value_path == "optics-admin-up"):
                            self.optics_admin_up = value
                            self.optics_admin_up.value_namespace = name_space
                            self.optics_admin_up.value_namespace_prefix = name_space_prefix
                        if(value_path == "optics-ctrl-created"):
                            self.optics_ctrl_created = value
                            self.optics_ctrl_created.value_namespace = name_space
                            self.optics_ctrl_created.value_namespace_prefix = name_space_prefix
                        if(value_path == "pm-port-state-dsp"):
                            self.pm_port_state_dsp = value
                            self.pm_port_state_dsp.value_namespace = name_space
                            self.pm_port_state_dsp.value_namespace_prefix = name_space_prefix
                        if(value_path == "pm-port-state-opt"):
                            self.pm_port_state_opt = value
                            self.pm_port_state_opt.value_namespace = name_space
                            self.pm_port_state_opt.value_namespace_prefix = name_space_prefix
                        if(value_path == "provisioned-cd-max"):
                            self.provisioned_cd_max = value
                            self.provisioned_cd_max.value_namespace = name_space
                            self.provisioned_cd_max.value_namespace_prefix = name_space_prefix
                        if(value_path == "provisioned-cd-min"):
                            self.provisioned_cd_min = value
                            self.provisioned_cd_min.value_namespace = name_space
                            self.provisioned_cd_min.value_namespace_prefix = name_space_prefix
                        if(value_path == "provisioned-ctp2-led-state"):
                            self.provisioned_ctp2_led_state = value
                            self.provisioned_ctp2_led_state.value_namespace = name_space
                            self.provisioned_ctp2_led_state.value_namespace_prefix = name_space_prefix
                        if(value_path == "provisioned-frequency"):
                            self.provisioned_frequency = value
                            self.provisioned_frequency.value_namespace = name_space
                            self.provisioned_frequency.value_namespace_prefix = name_space_prefix
                        if(value_path == "provisioned-loopback-mode"):
                            self.provisioned_loopback_mode = value
                            self.provisioned_loopback_mode.value_namespace = name_space
                            self.provisioned_loopback_mode.value_namespace_prefix = name_space_prefix
                        if(value_path == "provisioned-traffic-type"):
                            self.provisioned_traffic_type = value
                            self.provisioned_traffic_type.value_namespace = name_space
                            self.provisioned_traffic_type.value_namespace_prefix = name_space_prefix
                        if(value_path == "provisioned-tx-power"):
                            self.provisioned_tx_power = value
                            self.provisioned_tx_power.value_namespace = name_space
                            self.provisioned_tx_power.value_namespace_prefix = name_space_prefix
                        if(value_path == "provisioning-failed"):
                            self.provisioning_failed = value
                            self.provisioning_failed.value_namespace = name_space
                            self.provisioning_failed.value_namespace_prefix = name_space_prefix
                        if(value_path == "provisioning-needed"):
                            self.provisioning_needed = value
                            self.provisioning_needed.value_namespace = name_space
                            self.provisioning_needed.value_namespace_prefix = name_space_prefix
                        if(value_path == "rc-alarm-port-dsp"):
                            self.rc_alarm_port_dsp = value
                            self.rc_alarm_port_dsp.value_namespace = name_space
                            self.rc_alarm_port_dsp.value_namespace_prefix = name_space_prefix
                        if(value_path == "rc-alarm-port-opt"):
                            self.rc_alarm_port_opt = value
                            self.rc_alarm_port_opt.value_namespace = name_space
                            self.rc_alarm_port_opt.value_namespace_prefix = name_space_prefix
                        if(value_path == "rc-pm-port-dsp"):
                            self.rc_pm_port_dsp = value
                            self.rc_pm_port_dsp.value_namespace = name_space
                            self.rc_pm_port_dsp.value_namespace_prefix = name_space_prefix
                        if(value_path == "rc-pm-port-opt"):
                            self.rc_pm_port_opt = value
                            self.rc_pm_port_opt.value_namespace = name_space
                            self.rc_pm_port_opt.value_namespace_prefix = name_space_prefix
                        if(value_path == "rc-pm-provision-dsp"):
                            self.rc_pm_provision_dsp = value
                            self.rc_pm_provision_dsp.value_namespace = name_space
                            self.rc_pm_provision_dsp.value_namespace_prefix = name_space_prefix
                        if(value_path == "rc-pm-provision-opt"):
                            self.rc_pm_provision_opt = value
                            self.rc_pm_provision_opt.value_namespace = name_space
                            self.rc_pm_provision_opt.value_namespace_prefix = name_space_prefix
                        if(value_path == "traffic-op-rc"):
                            self.traffic_op_rc = value
                            self.traffic_op_rc.value_namespace = name_space
                            self.traffic_op_rc.value_namespace_prefix = name_space_prefix
                        if(value_path == "tx-power-op-rc"):
                            self.tx_power_op_rc = value
                            self.tx_power_op_rc.value_namespace = name_space
                            self.tx_power_op_rc.value_namespace_prefix = name_space_prefix
                        if(value_path == "wlen-op-rc"):
                            self.wlen_op_rc = value
                            self.wlen_op_rc.value_namespace = name_space
                            self.wlen_op_rc.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.port_data:
                        if (c.has_data()):
                            return True
                    return (
                        self.aipc_srvr_state.is_set or
                        self.board_type.is_set or
                        self.denali0_version.is_set or
                        self.denali1_version.is_set or
                        self.denali2_version.is_set or
                        self.dsp_ea_conn.is_set or
                        self.fpd_in_progress.is_set or
                        self.im_state.is_set or
                        self.inside_prov_loop.is_set or
                        self.jlink_op.is_set or
                        self.morgoth_alive.is_set or
                        self.morgoth_downloaded_version.is_set or
                        self.morgoth_golden_version.is_set or
                        self.morgoth_running_version.is_set or
                        self.optics_ea_conn.is_set or
                        self.pending_provision.is_set or
                        self.pm_state.is_set or
                        self.prov_infra_state.is_set or
                        self.prov_run_count.is_set or
                        self.pulse_sent.is_set or
                        self.sdk_fpga_compatible.is_set or
                        self.sdk_version.is_set or
                        self.sysdb_state.is_set or
                        self.vether_state.is_set)

                def has_operation(self):
                    for c in self.port_data:
                        if (c.has_operation()):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.aipc_srvr_state.yfilter != YFilter.not_set or
                        self.board_type.yfilter != YFilter.not_set or
                        self.denali0_version.yfilter != YFilter.not_set or
                        self.denali1_version.yfilter != YFilter.not_set or
                        self.denali2_version.yfilter != YFilter.not_set or
                        self.dsp_ea_conn.yfilter != YFilter.not_set or
                        self.fpd_in_progress.yfilter != YFilter.not_set or
                        self.im_state.yfilter != YFilter.not_set or
                        self.inside_prov_loop.yfilter != YFilter.not_set or
                        self.jlink_op.yfilter != YFilter.not_set or
                        self.morgoth_alive.yfilter != YFilter.not_set or
                        self.morgoth_downloaded_version.yfilter != YFilter.not_set or
                        self.morgoth_golden_version.yfilter != YFilter.not_set or
                        self.morgoth_running_version.yfilter != YFilter.not_set or
                        self.optics_ea_conn.yfilter != YFilter.not_set or
                        self.pending_provision.yfilter != YFilter.not_set or
                        self.pm_state.yfilter != YFilter.not_set or
                        self.prov_infra_state.yfilter != YFilter.not_set or
                        self.prov_run_count.yfilter != YFilter.not_set or
                        self.pulse_sent.yfilter != YFilter.not_set or
                        self.sdk_fpga_compatible.yfilter != YFilter.not_set or
                        self.sdk_version.yfilter != YFilter.not_set or
                        self.sysdb_state.yfilter != YFilter.not_set or
                        self.vether_state.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "coherenthealth" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.aipc_srvr_state.is_set or self.aipc_srvr_state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.aipc_srvr_state.get_name_leafdata())
                    if (self.board_type.is_set or self.board_type.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.board_type.get_name_leafdata())
                    if (self.denali0_version.is_set or self.denali0_version.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.denali0_version.get_name_leafdata())
                    if (self.denali1_version.is_set or self.denali1_version.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.denali1_version.get_name_leafdata())
                    if (self.denali2_version.is_set or self.denali2_version.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.denali2_version.get_name_leafdata())
                    if (self.dsp_ea_conn.is_set or self.dsp_ea_conn.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.dsp_ea_conn.get_name_leafdata())
                    if (self.fpd_in_progress.is_set or self.fpd_in_progress.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.fpd_in_progress.get_name_leafdata())
                    if (self.im_state.is_set or self.im_state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.im_state.get_name_leafdata())
                    if (self.inside_prov_loop.is_set or self.inside_prov_loop.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.inside_prov_loop.get_name_leafdata())
                    if (self.jlink_op.is_set or self.jlink_op.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.jlink_op.get_name_leafdata())
                    if (self.morgoth_alive.is_set or self.morgoth_alive.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.morgoth_alive.get_name_leafdata())
                    if (self.morgoth_downloaded_version.is_set or self.morgoth_downloaded_version.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.morgoth_downloaded_version.get_name_leafdata())
                    if (self.morgoth_golden_version.is_set or self.morgoth_golden_version.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.morgoth_golden_version.get_name_leafdata())
                    if (self.morgoth_running_version.is_set or self.morgoth_running_version.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.morgoth_running_version.get_name_leafdata())
                    if (self.optics_ea_conn.is_set or self.optics_ea_conn.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.optics_ea_conn.get_name_leafdata())
                    if (self.pending_provision.is_set or self.pending_provision.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.pending_provision.get_name_leafdata())
                    if (self.pm_state.is_set or self.pm_state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.pm_state.get_name_leafdata())
                    if (self.prov_infra_state.is_set or self.prov_infra_state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.prov_infra_state.get_name_leafdata())
                    if (self.prov_run_count.is_set or self.prov_run_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.prov_run_count.get_name_leafdata())
                    if (self.pulse_sent.is_set or self.pulse_sent.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.pulse_sent.get_name_leafdata())
                    if (self.sdk_fpga_compatible.is_set or self.sdk_fpga_compatible.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.sdk_fpga_compatible.get_name_leafdata())
                    if (self.sdk_version.is_set or self.sdk_version.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.sdk_version.get_name_leafdata())
                    if (self.sysdb_state.is_set or self.sysdb_state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.sysdb_state.get_name_leafdata())
                    if (self.vether_state.is_set or self.vether_state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.vether_state.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "port-data"):
                        for c in self.port_data:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Coherent.Nodes.Node.Coherenthealth.PortData()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.port_data.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "port-data" or name == "aipc-srvr-state" or name == "board-type" or name == "denali0-version" or name == "denali1-version" or name == "denali2-version" or name == "dsp-ea-conn" or name == "fpd-in-progress" or name == "im-state" or name == "inside-prov-loop" or name == "jlink-op" or name == "morgoth-alive" or name == "morgoth-downloaded-version" or name == "morgoth-golden-version" or name == "morgoth-running-version" or name == "optics-ea-conn" or name == "pending-provision" or name == "pm-state" or name == "prov-infra-state" or name == "prov-run-count" or name == "pulse-sent" or name == "sdk-fpga-compatible" or name == "sdk-version" or name == "sysdb-state" or name == "vether-state"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "aipc-srvr-state"):
                        self.aipc_srvr_state = value
                        self.aipc_srvr_state.value_namespace = name_space
                        self.aipc_srvr_state.value_namespace_prefix = name_space_prefix
                    if(value_path == "board-type"):
                        self.board_type = value
                        self.board_type.value_namespace = name_space
                        self.board_type.value_namespace_prefix = name_space_prefix
                    if(value_path == "denali0-version"):
                        self.denali0_version = value
                        self.denali0_version.value_namespace = name_space
                        self.denali0_version.value_namespace_prefix = name_space_prefix
                    if(value_path == "denali1-version"):
                        self.denali1_version = value
                        self.denali1_version.value_namespace = name_space
                        self.denali1_version.value_namespace_prefix = name_space_prefix
                    if(value_path == "denali2-version"):
                        self.denali2_version = value
                        self.denali2_version.value_namespace = name_space
                        self.denali2_version.value_namespace_prefix = name_space_prefix
                    if(value_path == "dsp-ea-conn"):
                        self.dsp_ea_conn = value
                        self.dsp_ea_conn.value_namespace = name_space
                        self.dsp_ea_conn.value_namespace_prefix = name_space_prefix
                    if(value_path == "fpd-in-progress"):
                        self.fpd_in_progress = value
                        self.fpd_in_progress.value_namespace = name_space
                        self.fpd_in_progress.value_namespace_prefix = name_space_prefix
                    if(value_path == "im-state"):
                        self.im_state = value
                        self.im_state.value_namespace = name_space
                        self.im_state.value_namespace_prefix = name_space_prefix
                    if(value_path == "inside-prov-loop"):
                        self.inside_prov_loop = value
                        self.inside_prov_loop.value_namespace = name_space
                        self.inside_prov_loop.value_namespace_prefix = name_space_prefix
                    if(value_path == "jlink-op"):
                        self.jlink_op = value
                        self.jlink_op.value_namespace = name_space
                        self.jlink_op.value_namespace_prefix = name_space_prefix
                    if(value_path == "morgoth-alive"):
                        self.morgoth_alive = value
                        self.morgoth_alive.value_namespace = name_space
                        self.morgoth_alive.value_namespace_prefix = name_space_prefix
                    if(value_path == "morgoth-downloaded-version"):
                        self.morgoth_downloaded_version = value
                        self.morgoth_downloaded_version.value_namespace = name_space
                        self.morgoth_downloaded_version.value_namespace_prefix = name_space_prefix
                    if(value_path == "morgoth-golden-version"):
                        self.morgoth_golden_version = value
                        self.morgoth_golden_version.value_namespace = name_space
                        self.morgoth_golden_version.value_namespace_prefix = name_space_prefix
                    if(value_path == "morgoth-running-version"):
                        self.morgoth_running_version = value
                        self.morgoth_running_version.value_namespace = name_space
                        self.morgoth_running_version.value_namespace_prefix = name_space_prefix
                    if(value_path == "optics-ea-conn"):
                        self.optics_ea_conn = value
                        self.optics_ea_conn.value_namespace = name_space
                        self.optics_ea_conn.value_namespace_prefix = name_space_prefix
                    if(value_path == "pending-provision"):
                        self.pending_provision = value
                        self.pending_provision.value_namespace = name_space
                        self.pending_provision.value_namespace_prefix = name_space_prefix
                    if(value_path == "pm-state"):
                        self.pm_state = value
                        self.pm_state.value_namespace = name_space
                        self.pm_state.value_namespace_prefix = name_space_prefix
                    if(value_path == "prov-infra-state"):
                        self.prov_infra_state = value
                        self.prov_infra_state.value_namespace = name_space
                        self.prov_infra_state.value_namespace_prefix = name_space_prefix
                    if(value_path == "prov-run-count"):
                        self.prov_run_count = value
                        self.prov_run_count.value_namespace = name_space
                        self.prov_run_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "pulse-sent"):
                        self.pulse_sent = value
                        self.pulse_sent.value_namespace = name_space
                        self.pulse_sent.value_namespace_prefix = name_space_prefix
                    if(value_path == "sdk-fpga-compatible"):
                        self.sdk_fpga_compatible = value
                        self.sdk_fpga_compatible.value_namespace = name_space
                        self.sdk_fpga_compatible.value_namespace_prefix = name_space_prefix
                    if(value_path == "sdk-version"):
                        self.sdk_version = value
                        self.sdk_version.value_namespace = name_space
                        self.sdk_version.value_namespace_prefix = name_space_prefix
                    if(value_path == "sysdb-state"):
                        self.sysdb_state = value
                        self.sysdb_state.value_namespace = name_space
                        self.sysdb_state.value_namespace_prefix = name_space_prefix
                    if(value_path == "vether-state"):
                        self.vether_state = value
                        self.vether_state.value_namespace = name_space
                        self.vether_state.value_namespace_prefix = name_space_prefix


            class PortModeAllInfo(Entity):
                """
                PortMode all operational data
                
                .. attribute:: num_entries
                
                	Number of dev map entries
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: portmode_entry
                
                	portmode entry
                	**type**\: list of    :py:class:`PortmodeEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.PortModeAllInfo.PortmodeEntry>`
                
                

                """

                _prefix = 'ncs5500-coherent-node-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Coherent.Nodes.Node.PortModeAllInfo, self).__init__()

                    self.yang_name = "port-mode-all-info"
                    self.yang_parent_name = "node"

                    self.num_entries = YLeaf(YType.uint32, "num-entries")

                    self.portmode_entry = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("num_entries") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Coherent.Nodes.Node.PortModeAllInfo, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Coherent.Nodes.Node.PortModeAllInfo, self).__setattr__(name, value)


                class PortmodeEntry(Entity):
                    """
                    portmode entry
                    
                    .. attribute:: diff
                    
                    	diff
                    	**type**\:  str
                    
                    	**length:** 0..128
                    
                    .. attribute:: fec
                    
                    	fec
                    	**type**\:  str
                    
                    	**length:** 0..128
                    
                    .. attribute:: intf_name
                    
                    	intf name
                    	**type**\:  str
                    
                    	**length:** 0..128
                    
                    .. attribute:: modulation
                    
                    	modulation
                    	**type**\:  str
                    
                    	**length:** 0..128
                    
                    .. attribute:: speed
                    
                    	speed
                    	**type**\:  str
                    
                    	**length:** 0..128
                    
                    

                    """

                    _prefix = 'ncs5500-coherent-node-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Coherent.Nodes.Node.PortModeAllInfo.PortmodeEntry, self).__init__()

                        self.yang_name = "portmode-entry"
                        self.yang_parent_name = "port-mode-all-info"

                        self.diff = YLeaf(YType.str, "diff")

                        self.fec = YLeaf(YType.str, "fec")

                        self.intf_name = YLeaf(YType.str, "intf-name")

                        self.modulation = YLeaf(YType.str, "modulation")

                        self.speed = YLeaf(YType.str, "speed")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("diff",
                                        "fec",
                                        "intf_name",
                                        "modulation",
                                        "speed") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Coherent.Nodes.Node.PortModeAllInfo.PortmodeEntry, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Coherent.Nodes.Node.PortModeAllInfo.PortmodeEntry, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.diff.is_set or
                            self.fec.is_set or
                            self.intf_name.is_set or
                            self.modulation.is_set or
                            self.speed.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.diff.yfilter != YFilter.not_set or
                            self.fec.yfilter != YFilter.not_set or
                            self.intf_name.yfilter != YFilter.not_set or
                            self.modulation.yfilter != YFilter.not_set or
                            self.speed.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "portmode-entry" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.diff.is_set or self.diff.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.diff.get_name_leafdata())
                        if (self.fec.is_set or self.fec.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.fec.get_name_leafdata())
                        if (self.intf_name.is_set or self.intf_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.intf_name.get_name_leafdata())
                        if (self.modulation.is_set or self.modulation.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.modulation.get_name_leafdata())
                        if (self.speed.is_set or self.speed.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.speed.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "diff" or name == "fec" or name == "intf-name" or name == "modulation" or name == "speed"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "diff"):
                            self.diff = value
                            self.diff.value_namespace = name_space
                            self.diff.value_namespace_prefix = name_space_prefix
                        if(value_path == "fec"):
                            self.fec = value
                            self.fec.value_namespace = name_space
                            self.fec.value_namespace_prefix = name_space_prefix
                        if(value_path == "intf-name"):
                            self.intf_name = value
                            self.intf_name.value_namespace = name_space
                            self.intf_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "modulation"):
                            self.modulation = value
                            self.modulation.value_namespace = name_space
                            self.modulation.value_namespace_prefix = name_space_prefix
                        if(value_path == "speed"):
                            self.speed = value
                            self.speed.value_namespace = name_space
                            self.speed.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.portmode_entry:
                        if (c.has_data()):
                            return True
                    return self.num_entries.is_set

                def has_operation(self):
                    for c in self.portmode_entry:
                        if (c.has_operation()):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.num_entries.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "port-mode-all-info" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.num_entries.is_set or self.num_entries.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.num_entries.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "portmode-entry"):
                        for c in self.portmode_entry:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Coherent.Nodes.Node.PortModeAllInfo.PortmodeEntry()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.portmode_entry.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "portmode-entry" or name == "num-entries"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "num-entries"):
                        self.num_entries = value
                        self.num_entries.value_namespace = name_space
                        self.num_entries.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.node_name.is_set or
                    (self.coherent_time_stats is not None and self.coherent_time_stats.has_data()) or
                    (self.coherenthealth is not None and self.coherenthealth.has_data()) or
                    (self.devicemapping is not None and self.devicemapping.has_data()) or
                    (self.port_mode_all_info is not None and self.port_mode_all_info.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.node_name.yfilter != YFilter.not_set or
                    (self.coherent_time_stats is not None and self.coherent_time_stats.has_operation()) or
                    (self.coherenthealth is not None and self.coherenthealth.has_operation()) or
                    (self.devicemapping is not None and self.devicemapping.has_operation()) or
                    (self.port_mode_all_info is not None and self.port_mode_all_info.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "node" + "[node-name='" + self.node_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ncs5500-coherent-node-oper:coherent/nodes/%s" % self.get_segment_path()
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

                if (child_yang_name == "coherent-time-stats"):
                    if (self.coherent_time_stats is None):
                        self.coherent_time_stats = Coherent.Nodes.Node.CoherentTimeStats()
                        self.coherent_time_stats.parent = self
                        self._children_name_map["coherent_time_stats"] = "coherent-time-stats"
                    return self.coherent_time_stats

                if (child_yang_name == "coherenthealth"):
                    if (self.coherenthealth is None):
                        self.coherenthealth = Coherent.Nodes.Node.Coherenthealth()
                        self.coherenthealth.parent = self
                        self._children_name_map["coherenthealth"] = "coherenthealth"
                    return self.coherenthealth

                if (child_yang_name == "devicemapping"):
                    if (self.devicemapping is None):
                        self.devicemapping = Coherent.Nodes.Node.Devicemapping()
                        self.devicemapping.parent = self
                        self._children_name_map["devicemapping"] = "devicemapping"
                    return self.devicemapping

                if (child_yang_name == "port-mode-all-info"):
                    if (self.port_mode_all_info is None):
                        self.port_mode_all_info = Coherent.Nodes.Node.PortModeAllInfo()
                        self.port_mode_all_info.parent = self
                        self._children_name_map["port_mode_all_info"] = "port-mode-all-info"
                    return self.port_mode_all_info

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "coherent-time-stats" or name == "coherenthealth" or name == "devicemapping" or name == "port-mode-all-info" or name == "node-name"):
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
                path_buffer = "Cisco-IOS-XR-ncs5500-coherent-node-oper:coherent/%s" % self.get_segment_path()
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
                c = Coherent.Nodes.Node()
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
        path_buffer = "Cisco-IOS-XR-ncs5500-coherent-node-oper:coherent" + path_buffer

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
                self.nodes = Coherent.Nodes()
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
        self._top_entity = Coherent()
        return self._top_entity

