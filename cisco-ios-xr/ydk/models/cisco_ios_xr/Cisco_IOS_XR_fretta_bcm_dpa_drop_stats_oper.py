""" Cisco_IOS_XR_fretta_bcm_dpa_drop_stats_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR fretta\-bcm\-dpa\-drop\-stats package operational data.

This module contains definitions
for the following management objects\:
  drop\: Drop stats data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Drop(Entity):
    """
    Drop stats data
    
    .. attribute:: nodes
    
    	Drop data per node
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_drop_stats_oper.Drop.Nodes>`
    
    

    """

    _prefix = 'fretta-bcm-dpa-drop-stats-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Drop, self).__init__()
        self._top_entity = None

        self.yang_name = "drop"
        self.yang_parent_name = "Cisco-IOS-XR-fretta-bcm-dpa-drop-stats-oper"

        self.nodes = Drop.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")


    class Nodes(Entity):
        """
        Drop data per node
        
        .. attribute:: node
        
        	Drop stats data for a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_drop_stats_oper.Drop.Nodes.Node>`
        
        

        """

        _prefix = 'fretta-bcm-dpa-drop-stats-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Drop.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "drop"

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
                        super(Drop.Nodes, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Drop.Nodes, self).__setattr__(name, value)


        class Node(Entity):
            """
            Drop stats data for a particular node
            
            .. attribute:: node_name  <key>
            
            	Node ID
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: npu_number_for_drop_stats
            
            	NPU drop stats
            	**type**\:   :py:class:`NpuNumberForDropStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_drop_stats_oper.Drop.Nodes.Node.NpuNumberForDropStats>`
            
            

            """

            _prefix = 'fretta-bcm-dpa-drop-stats-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Drop.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"

                self.node_name = YLeaf(YType.str, "node-name")

                self.npu_number_for_drop_stats = Drop.Nodes.Node.NpuNumberForDropStats()
                self.npu_number_for_drop_stats.parent = self
                self._children_name_map["npu_number_for_drop_stats"] = "npu-number-for-drop-stats"
                self._children_yang_names.add("npu-number-for-drop-stats")

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
                            super(Drop.Nodes.Node, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Drop.Nodes.Node, self).__setattr__(name, value)


            class NpuNumberForDropStats(Entity):
                """
                NPU drop stats
                
                .. attribute:: npu_number_for_drop_stat
                
                	All drop stats for a particular NPU
                	**type**\: list of    :py:class:`NpuNumberForDropStat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_drop_stats_oper.Drop.Nodes.Node.NpuNumberForDropStats.NpuNumberForDropStat>`
                
                

                """

                _prefix = 'fretta-bcm-dpa-drop-stats-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Drop.Nodes.Node.NpuNumberForDropStats, self).__init__()

                    self.yang_name = "npu-number-for-drop-stats"
                    self.yang_parent_name = "node"

                    self.npu_number_for_drop_stat = YList(self)

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
                                super(Drop.Nodes.Node.NpuNumberForDropStats, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Drop.Nodes.Node.NpuNumberForDropStats, self).__setattr__(name, value)


                class NpuNumberForDropStat(Entity):
                    """
                    All drop stats for a particular NPU
                    
                    .. attribute:: npu_id  <key>
                    
                    	NPU number
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: drop_specific_stats_data
                    
                    	Second argument to the module
                    	**type**\: list of    :py:class:`DropSpecificStatsData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_drop_stats_oper.Drop.Nodes.Node.NpuNumberForDropStats.NpuNumberForDropStat.DropSpecificStatsData>`
                    
                    

                    """

                    _prefix = 'fretta-bcm-dpa-drop-stats-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Drop.Nodes.Node.NpuNumberForDropStats.NpuNumberForDropStat, self).__init__()

                        self.yang_name = "npu-number-for-drop-stat"
                        self.yang_parent_name = "npu-number-for-drop-stats"

                        self.npu_id = YLeaf(YType.int32, "npu-id")

                        self.drop_specific_stats_data = YList(self)

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
                                    super(Drop.Nodes.Node.NpuNumberForDropStats.NpuNumberForDropStat, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Drop.Nodes.Node.NpuNumberForDropStats.NpuNumberForDropStat, self).__setattr__(name, value)


                    class DropSpecificStatsData(Entity):
                        """
                        Second argument to the module
                        
                        .. attribute:: drop_data  <key>
                        
                        	Drop ID
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: count
                        
                        	count
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: id
                        
                        	id
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: name
                        
                        	name
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'fretta-bcm-dpa-drop-stats-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Drop.Nodes.Node.NpuNumberForDropStats.NpuNumberForDropStat.DropSpecificStatsData, self).__init__()

                            self.yang_name = "drop-specific-stats-data"
                            self.yang_parent_name = "npu-number-for-drop-stat"

                            self.drop_data = YLeaf(YType.int32, "drop-data")

                            self.count = YLeaf(YType.uint64, "count")

                            self.id = YLeaf(YType.uint32, "id")

                            self.name = YLeaf(YType.str, "name")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("drop_data",
                                            "count",
                                            "id",
                                            "name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Drop.Nodes.Node.NpuNumberForDropStats.NpuNumberForDropStat.DropSpecificStatsData, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Drop.Nodes.Node.NpuNumberForDropStats.NpuNumberForDropStat.DropSpecificStatsData, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.drop_data.is_set or
                                self.count.is_set or
                                self.id.is_set or
                                self.name.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.drop_data.yfilter != YFilter.not_set or
                                self.count.yfilter != YFilter.not_set or
                                self.id.yfilter != YFilter.not_set or
                                self.name.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "drop-specific-stats-data" + "[drop-data='" + self.drop_data.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.drop_data.is_set or self.drop_data.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.drop_data.get_name_leafdata())
                            if (self.count.is_set or self.count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.count.get_name_leafdata())
                            if (self.id.is_set or self.id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.id.get_name_leafdata())
                            if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.name.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "drop-data" or name == "count" or name == "id" or name == "name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "drop-data"):
                                self.drop_data = value
                                self.drop_data.value_namespace = name_space
                                self.drop_data.value_namespace_prefix = name_space_prefix
                            if(value_path == "count"):
                                self.count = value
                                self.count.value_namespace = name_space
                                self.count.value_namespace_prefix = name_space_prefix
                            if(value_path == "id"):
                                self.id = value
                                self.id.value_namespace = name_space
                                self.id.value_namespace_prefix = name_space_prefix
                            if(value_path == "name"):
                                self.name = value
                                self.name.value_namespace = name_space
                                self.name.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.drop_specific_stats_data:
                            if (c.has_data()):
                                return True
                        return self.npu_id.is_set

                    def has_operation(self):
                        for c in self.drop_specific_stats_data:
                            if (c.has_operation()):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.npu_id.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "npu-number-for-drop-stat" + "[npu-id='" + self.npu_id.get() + "']" + path_buffer

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

                        if (child_yang_name == "drop-specific-stats-data"):
                            for c in self.drop_specific_stats_data:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Drop.Nodes.Node.NpuNumberForDropStats.NpuNumberForDropStat.DropSpecificStatsData()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.drop_specific_stats_data.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "drop-specific-stats-data" or name == "npu-id"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "npu-id"):
                            self.npu_id = value
                            self.npu_id.value_namespace = name_space
                            self.npu_id.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.npu_number_for_drop_stat:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.npu_number_for_drop_stat:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "npu-number-for-drop-stats" + path_buffer

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

                    if (child_yang_name == "npu-number-for-drop-stat"):
                        for c in self.npu_number_for_drop_stat:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Drop.Nodes.Node.NpuNumberForDropStats.NpuNumberForDropStat()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.npu_number_for_drop_stat.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "npu-number-for-drop-stat"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.node_name.is_set or
                    (self.npu_number_for_drop_stats is not None and self.npu_number_for_drop_stats.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.node_name.yfilter != YFilter.not_set or
                    (self.npu_number_for_drop_stats is not None and self.npu_number_for_drop_stats.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "node" + "[node-name='" + self.node_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-fretta-bcm-dpa-drop-stats-oper:drop/nodes/%s" % self.get_segment_path()
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

                if (child_yang_name == "npu-number-for-drop-stats"):
                    if (self.npu_number_for_drop_stats is None):
                        self.npu_number_for_drop_stats = Drop.Nodes.Node.NpuNumberForDropStats()
                        self.npu_number_for_drop_stats.parent = self
                        self._children_name_map["npu_number_for_drop_stats"] = "npu-number-for-drop-stats"
                    return self.npu_number_for_drop_stats

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "npu-number-for-drop-stats" or name == "node-name"):
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
                path_buffer = "Cisco-IOS-XR-fretta-bcm-dpa-drop-stats-oper:drop/%s" % self.get_segment_path()
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
                c = Drop.Nodes.Node()
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
        path_buffer = "Cisco-IOS-XR-fretta-bcm-dpa-drop-stats-oper:drop" + path_buffer

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
                self.nodes = Drop.Nodes()
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
        self._top_entity = Drop()
        return self._top_entity

