""" Cisco_IOS_XR_asr9k_asic_errors_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR asr9k\-asic\-errors package operational data.

This module contains definitions
for the following management objects\:
  asic\-error\-stats\: Asic error stats operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class AsicErrorStats(Entity):
    """
    Asic error stats operational data
    
    .. attribute:: nodes
    
    	Table of Nodes
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_asic_errors_oper.AsicErrorStats.Nodes>`
    
    

    """

    _prefix = 'asr9k-asic-errors-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(AsicErrorStats, self).__init__()
        self._top_entity = None

        self.yang_name = "asic-error-stats"
        self.yang_parent_name = "Cisco-IOS-XR-asr9k-asic-errors-oper"

        self.nodes = AsicErrorStats.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")


    class Nodes(Entity):
        """
        Table of Nodes
        
        .. attribute:: node
        
        	Information about a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_asic_errors_oper.AsicErrorStats.Nodes.Node>`
        
        

        """

        _prefix = 'asr9k-asic-errors-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(AsicErrorStats.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "asic-error-stats"

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
                        super(AsicErrorStats.Nodes, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(AsicErrorStats.Nodes, self).__setattr__(name, value)


        class Node(Entity):
            """
            Information about a particular node
            
            .. attribute:: node_name  <key>
            
            	Node name
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: counts
            
            	Table of all Asic Types information on a node
            	**type**\:   :py:class:`Counts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_asic_errors_oper.AsicErrorStats.Nodes.Node.Counts>`
            
            

            """

            _prefix = 'asr9k-asic-errors-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(AsicErrorStats.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"

                self.node_name = YLeaf(YType.str, "node-name")

                self.counts = AsicErrorStats.Nodes.Node.Counts()
                self.counts.parent = self
                self._children_name_map["counts"] = "counts"
                self._children_yang_names.add("counts")

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
                            super(AsicErrorStats.Nodes.Node, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(AsicErrorStats.Nodes.Node, self).__setattr__(name, value)


            class Counts(Entity):
                """
                Table of all Asic Types information on a node
                
                .. attribute:: count
                
                	Summary Asic error counts for a Asic Type
                	**type**\: list of    :py:class:`Count <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_asic_errors_oper.AsicErrorStats.Nodes.Node.Counts.Count>`
                
                

                """

                _prefix = 'asr9k-asic-errors-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(AsicErrorStats.Nodes.Node.Counts, self).__init__()

                    self.yang_name = "counts"
                    self.yang_parent_name = "node"

                    self.count = YList(self)

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
                                super(AsicErrorStats.Nodes.Node.Counts, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(AsicErrorStats.Nodes.Node.Counts, self).__setattr__(name, value)


                class Count(Entity):
                    """
                    Summary Asic error counts for a Asic Type
                    
                    .. attribute:: type  <key>
                    
                    	Asic Type
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: sum_data
                    
                    	sum data
                    	**type**\: list of    :py:class:`SumData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_asic_errors_oper.AsicErrorStats.Nodes.Node.Counts.Count.SumData>`
                    
                    

                    """

                    _prefix = 'asr9k-asic-errors-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(AsicErrorStats.Nodes.Node.Counts.Count, self).__init__()

                        self.yang_name = "count"
                        self.yang_parent_name = "counts"

                        self.type = YLeaf(YType.str, "type")

                        self.sum_data = YList(self)

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
                                    super(AsicErrorStats.Nodes.Node.Counts.Count, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(AsicErrorStats.Nodes.Node.Counts.Count, self).__setattr__(name, value)


                    class SumData(Entity):
                        """
                        sum data
                        
                        .. attribute:: crc_err_count
                        
                        	crc err count
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: gen_err_count
                        
                        	gen err count
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: instance
                        
                        	instance
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: mbe_err_count
                        
                        	mbe err count
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: node_key
                        
                        	node key
                        	**type**\:  list of int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: num_nodes
                        
                        	num nodes
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: par_err_count
                        
                        	par err count
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: reset_err_count
                        
                        	reset err count
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sbe_err_count
                        
                        	sbe err count
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'asr9k-asic-errors-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(AsicErrorStats.Nodes.Node.Counts.Count.SumData, self).__init__()

                            self.yang_name = "sum-data"
                            self.yang_parent_name = "count"

                            self.crc_err_count = YLeaf(YType.uint32, "crc-err-count")

                            self.gen_err_count = YLeaf(YType.uint32, "gen-err-count")

                            self.instance = YLeaf(YType.uint32, "instance")

                            self.mbe_err_count = YLeaf(YType.uint32, "mbe-err-count")

                            self.node_key = YLeafList(YType.uint32, "node-key")

                            self.num_nodes = YLeaf(YType.uint32, "num-nodes")

                            self.par_err_count = YLeaf(YType.uint32, "par-err-count")

                            self.reset_err_count = YLeaf(YType.uint32, "reset-err-count")

                            self.sbe_err_count = YLeaf(YType.uint32, "sbe-err-count")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("crc_err_count",
                                            "gen_err_count",
                                            "instance",
                                            "mbe_err_count",
                                            "node_key",
                                            "num_nodes",
                                            "par_err_count",
                                            "reset_err_count",
                                            "sbe_err_count") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(AsicErrorStats.Nodes.Node.Counts.Count.SumData, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(AsicErrorStats.Nodes.Node.Counts.Count.SumData, self).__setattr__(name, value)

                        def has_data(self):
                            for leaf in self.node_key.getYLeafs():
                                if (leaf.yfilter != YFilter.not_set):
                                    return True
                            return (
                                self.crc_err_count.is_set or
                                self.gen_err_count.is_set or
                                self.instance.is_set or
                                self.mbe_err_count.is_set or
                                self.num_nodes.is_set or
                                self.par_err_count.is_set or
                                self.reset_err_count.is_set or
                                self.sbe_err_count.is_set)

                        def has_operation(self):
                            for leaf in self.node_key.getYLeafs():
                                if (leaf.is_set):
                                    return True
                            return (
                                self.yfilter != YFilter.not_set or
                                self.crc_err_count.yfilter != YFilter.not_set or
                                self.gen_err_count.yfilter != YFilter.not_set or
                                self.instance.yfilter != YFilter.not_set or
                                self.mbe_err_count.yfilter != YFilter.not_set or
                                self.node_key.yfilter != YFilter.not_set or
                                self.num_nodes.yfilter != YFilter.not_set or
                                self.par_err_count.yfilter != YFilter.not_set or
                                self.reset_err_count.yfilter != YFilter.not_set or
                                self.sbe_err_count.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "sum-data" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.crc_err_count.is_set or self.crc_err_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.crc_err_count.get_name_leafdata())
                            if (self.gen_err_count.is_set or self.gen_err_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.gen_err_count.get_name_leafdata())
                            if (self.instance.is_set or self.instance.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.instance.get_name_leafdata())
                            if (self.mbe_err_count.is_set or self.mbe_err_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.mbe_err_count.get_name_leafdata())
                            if (self.num_nodes.is_set or self.num_nodes.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.num_nodes.get_name_leafdata())
                            if (self.par_err_count.is_set or self.par_err_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.par_err_count.get_name_leafdata())
                            if (self.reset_err_count.is_set or self.reset_err_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.reset_err_count.get_name_leafdata())
                            if (self.sbe_err_count.is_set or self.sbe_err_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.sbe_err_count.get_name_leafdata())

                            leaf_name_data.extend(self.node_key.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "crc-err-count" or name == "gen-err-count" or name == "instance" or name == "mbe-err-count" or name == "node-key" or name == "num-nodes" or name == "par-err-count" or name == "reset-err-count" or name == "sbe-err-count"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "crc-err-count"):
                                self.crc_err_count = value
                                self.crc_err_count.value_namespace = name_space
                                self.crc_err_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "gen-err-count"):
                                self.gen_err_count = value
                                self.gen_err_count.value_namespace = name_space
                                self.gen_err_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "instance"):
                                self.instance = value
                                self.instance.value_namespace = name_space
                                self.instance.value_namespace_prefix = name_space_prefix
                            if(value_path == "mbe-err-count"):
                                self.mbe_err_count = value
                                self.mbe_err_count.value_namespace = name_space
                                self.mbe_err_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "node-key"):
                                self.node_key.append(value)
                            if(value_path == "num-nodes"):
                                self.num_nodes = value
                                self.num_nodes.value_namespace = name_space
                                self.num_nodes.value_namespace_prefix = name_space_prefix
                            if(value_path == "par-err-count"):
                                self.par_err_count = value
                                self.par_err_count.value_namespace = name_space
                                self.par_err_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "reset-err-count"):
                                self.reset_err_count = value
                                self.reset_err_count.value_namespace = name_space
                                self.reset_err_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "sbe-err-count"):
                                self.sbe_err_count = value
                                self.sbe_err_count.value_namespace = name_space
                                self.sbe_err_count.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.sum_data:
                            if (c.has_data()):
                                return True
                        return self.type.is_set

                    def has_operation(self):
                        for c in self.sum_data:
                            if (c.has_operation()):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.type.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "count" + "[type='" + self.type.get() + "']" + path_buffer

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

                        if (child_yang_name == "sum-data"):
                            for c in self.sum_data:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = AsicErrorStats.Nodes.Node.Counts.Count.SumData()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.sum_data.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "sum-data" or name == "type"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "type"):
                            self.type = value
                            self.type.value_namespace = name_space
                            self.type.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.count:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.count:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "counts" + path_buffer

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

                    if (child_yang_name == "count"):
                        for c in self.count:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = AsicErrorStats.Nodes.Node.Counts.Count()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.count.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "count"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.node_name.is_set or
                    (self.counts is not None and self.counts.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.node_name.yfilter != YFilter.not_set or
                    (self.counts is not None and self.counts.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "node" + "[node-name='" + self.node_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-asr9k-asic-errors-oper:asic-error-stats/nodes/%s" % self.get_segment_path()
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

                if (child_yang_name == "counts"):
                    if (self.counts is None):
                        self.counts = AsicErrorStats.Nodes.Node.Counts()
                        self.counts.parent = self
                        self._children_name_map["counts"] = "counts"
                    return self.counts

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "counts" or name == "node-name"):
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
                path_buffer = "Cisco-IOS-XR-asr9k-asic-errors-oper:asic-error-stats/%s" % self.get_segment_path()
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
                c = AsicErrorStats.Nodes.Node()
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
        path_buffer = "Cisco-IOS-XR-asr9k-asic-errors-oper:asic-error-stats" + path_buffer

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
                self.nodes = AsicErrorStats.Nodes()
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
        self._top_entity = AsicErrorStats()
        return self._top_entity

