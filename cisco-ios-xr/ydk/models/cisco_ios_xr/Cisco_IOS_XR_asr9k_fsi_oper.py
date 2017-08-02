""" Cisco_IOS_XR_asr9k_fsi_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR asr9k\-fsi package operational data.

This module contains definitions
for the following management objects\:
  fabric\-stats\: Fabric stats operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class FabricStats(Entity):
    """
    Fabric stats operational data
    
    .. attribute:: nodes
    
    	Table of Nodes
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_fsi_oper.FabricStats.Nodes>`
    
    

    """

    _prefix = 'asr9k-fsi-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(FabricStats, self).__init__()
        self._top_entity = None

        self.yang_name = "fabric-stats"
        self.yang_parent_name = "Cisco-IOS-XR-asr9k-fsi-oper"

        self.nodes = FabricStats.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")


    class Nodes(Entity):
        """
        Table of Nodes
        
        .. attribute:: node
        
        	Information about a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_fsi_oper.FabricStats.Nodes.Node>`
        
        

        """

        _prefix = 'asr9k-fsi-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(FabricStats.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "fabric-stats"

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
                        super(FabricStats.Nodes, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(FabricStats.Nodes, self).__setattr__(name, value)


        class Node(Entity):
            """
            Information about a particular node
            
            .. attribute:: node_name  <key>
            
            	Node name
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: statses
            
            	Table of stats information
            	**type**\:   :py:class:`Statses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_fsi_oper.FabricStats.Nodes.Node.Statses>`
            
            

            """

            _prefix = 'asr9k-fsi-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(FabricStats.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"

                self.node_name = YLeaf(YType.str, "node-name")

                self.statses = FabricStats.Nodes.Node.Statses()
                self.statses.parent = self
                self._children_name_map["statses"] = "statses"
                self._children_yang_names.add("statses")

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
                            super(FabricStats.Nodes.Node, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(FabricStats.Nodes.Node, self).__setattr__(name, value)


            class Statses(Entity):
                """
                Table of stats information
                
                .. attribute:: stats
                
                	Stats information for a particular type
                	**type**\: list of    :py:class:`Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_fsi_oper.FabricStats.Nodes.Node.Statses.Stats>`
                
                

                """

                _prefix = 'asr9k-fsi-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(FabricStats.Nodes.Node.Statses, self).__init__()

                    self.yang_name = "statses"
                    self.yang_parent_name = "node"

                    self.stats = YList(self)

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
                                super(FabricStats.Nodes.Node.Statses, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(FabricStats.Nodes.Node.Statses, self).__setattr__(name, value)


                class Stats(Entity):
                    """
                    Stats information for a particular type
                    
                    .. attribute:: type  <key>
                    
                    	Fabric asic type
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: stat_table_name
                    
                    	Stat Table Name
                    	**type**\:  str
                    
                    .. attribute:: stats_table
                    
                    	Array of counters 
                    	**type**\: list of    :py:class:`StatsTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_fsi_oper.FabricStats.Nodes.Node.Statses.Stats.StatsTable>`
                    
                    

                    """

                    _prefix = 'asr9k-fsi-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(FabricStats.Nodes.Node.Statses.Stats, self).__init__()

                        self.yang_name = "stats"
                        self.yang_parent_name = "statses"

                        self.type = YLeaf(YType.str, "type")

                        self.stat_table_name = YLeaf(YType.str, "stat-table-name")

                        self.stats_table = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("type",
                                        "stat_table_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(FabricStats.Nodes.Node.Statses.Stats, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(FabricStats.Nodes.Node.Statses.Stats, self).__setattr__(name, value)


                    class StatsTable(Entity):
                        """
                        Array of counters 
                        
                        .. attribute:: fsi_stat
                        
                        	Stats Table
                        	**type**\: list of    :py:class:`FsiStat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_fsi_oper.FabricStats.Nodes.Node.Statses.Stats.StatsTable.FsiStat>`
                        
                        

                        """

                        _prefix = 'asr9k-fsi-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(FabricStats.Nodes.Node.Statses.Stats.StatsTable, self).__init__()

                            self.yang_name = "stats-table"
                            self.yang_parent_name = "stats"

                            self.fsi_stat = YList(self)

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
                                        super(FabricStats.Nodes.Node.Statses.Stats.StatsTable, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(FabricStats.Nodes.Node.Statses.Stats.StatsTable, self).__setattr__(name, value)


                        class FsiStat(Entity):
                            """
                            Stats Table
                            
                            .. attribute:: count
                            
                            	Counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: counter_name
                            
                            	Counter Name
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'asr9k-fsi-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(FabricStats.Nodes.Node.Statses.Stats.StatsTable.FsiStat, self).__init__()

                                self.yang_name = "fsi-stat"
                                self.yang_parent_name = "stats-table"

                                self.count = YLeaf(YType.uint64, "count")

                                self.counter_name = YLeaf(YType.str, "counter-name")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("count",
                                                "counter_name") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(FabricStats.Nodes.Node.Statses.Stats.StatsTable.FsiStat, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(FabricStats.Nodes.Node.Statses.Stats.StatsTable.FsiStat, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.count.is_set or
                                    self.counter_name.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.count.yfilter != YFilter.not_set or
                                    self.counter_name.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "fsi-stat" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.count.is_set or self.count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.count.get_name_leafdata())
                                if (self.counter_name.is_set or self.counter_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.counter_name.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "count" or name == "counter-name"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "count"):
                                    self.count = value
                                    self.count.value_namespace = name_space
                                    self.count.value_namespace_prefix = name_space_prefix
                                if(value_path == "counter-name"):
                                    self.counter_name = value
                                    self.counter_name.value_namespace = name_space
                                    self.counter_name.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.fsi_stat:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.fsi_stat:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "stats-table" + path_buffer

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

                            if (child_yang_name == "fsi-stat"):
                                for c in self.fsi_stat:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = FabricStats.Nodes.Node.Statses.Stats.StatsTable.FsiStat()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.fsi_stat.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "fsi-stat"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        for c in self.stats_table:
                            if (c.has_data()):
                                return True
                        return (
                            self.type.is_set or
                            self.stat_table_name.is_set)

                    def has_operation(self):
                        for c in self.stats_table:
                            if (c.has_operation()):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.type.yfilter != YFilter.not_set or
                            self.stat_table_name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "stats" + "[type='" + self.type.get() + "']" + path_buffer

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
                        if (self.stat_table_name.is_set or self.stat_table_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.stat_table_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "stats-table"):
                            for c in self.stats_table:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = FabricStats.Nodes.Node.Statses.Stats.StatsTable()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.stats_table.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "stats-table" or name == "type" or name == "stat-table-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "type"):
                            self.type = value
                            self.type.value_namespace = name_space
                            self.type.value_namespace_prefix = name_space_prefix
                        if(value_path == "stat-table-name"):
                            self.stat_table_name = value
                            self.stat_table_name.value_namespace = name_space
                            self.stat_table_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.stats:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.stats:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "statses" + path_buffer

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

                    if (child_yang_name == "stats"):
                        for c in self.stats:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = FabricStats.Nodes.Node.Statses.Stats()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.stats.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "stats"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.node_name.is_set or
                    (self.statses is not None and self.statses.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.node_name.yfilter != YFilter.not_set or
                    (self.statses is not None and self.statses.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "node" + "[node-name='" + self.node_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-asr9k-fsi-oper:fabric-stats/nodes/%s" % self.get_segment_path()
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

                if (child_yang_name == "statses"):
                    if (self.statses is None):
                        self.statses = FabricStats.Nodes.Node.Statses()
                        self.statses.parent = self
                        self._children_name_map["statses"] = "statses"
                    return self.statses

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "statses" or name == "node-name"):
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
                path_buffer = "Cisco-IOS-XR-asr9k-fsi-oper:fabric-stats/%s" % self.get_segment_path()
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
                c = FabricStats.Nodes.Node()
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
        path_buffer = "Cisco-IOS-XR-asr9k-fsi-oper:fabric-stats" + path_buffer

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
                self.nodes = FabricStats.Nodes()
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
        self._top_entity = FabricStats()
        return self._top_entity

