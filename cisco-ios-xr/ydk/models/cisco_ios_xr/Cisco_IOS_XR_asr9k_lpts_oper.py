""" Cisco_IOS_XR_asr9k_lpts_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR asr9k\-lpts package operational data.

This module contains definitions
for the following management objects\:
  platform\-lptsp\-ifib\-static\: ASR9K platform ifib operational
    data 
  platform\-lptsp\-ifib\: platform lptsp ifib
  platform\-lptsp\-ifib\-np\-stats\: platform lptsp ifib np stats

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class PlatformLptspIfibStatic(Entity):
    """
    ASR9K platform ifib operational data 
    
    .. attribute:: node_statics
    
    	List of nodes with platform specific lpts operation data
    	**type**\:   :py:class:`NodeStatics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lpts_oper.PlatformLptspIfibStatic.NodeStatics>`
    
    

    """

    _prefix = 'asr9k-lpts-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(PlatformLptspIfibStatic, self).__init__()
        self._top_entity = None

        self.yang_name = "platform-lptsp-ifib-static"
        self.yang_parent_name = "Cisco-IOS-XR-asr9k-lpts-oper"

        self.node_statics = PlatformLptspIfibStatic.NodeStatics()
        self.node_statics.parent = self
        self._children_name_map["node_statics"] = "node-statics"
        self._children_yang_names.add("node-statics")


    class NodeStatics(Entity):
        """
        List of nodes with platform specific lpts
        operation data
        
        .. attribute:: node_static
        
        	Node with platform specific lpts data
        	**type**\: list of    :py:class:`NodeStatic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lpts_oper.PlatformLptspIfibStatic.NodeStatics.NodeStatic>`
        
        

        """

        _prefix = 'asr9k-lpts-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(PlatformLptspIfibStatic.NodeStatics, self).__init__()

            self.yang_name = "node-statics"
            self.yang_parent_name = "platform-lptsp-ifib-static"

            self.node_static = YList(self)

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
                        super(PlatformLptspIfibStatic.NodeStatics, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(PlatformLptspIfibStatic.NodeStatics, self).__setattr__(name, value)


        class NodeStatic(Entity):
            """
            Node with platform specific lpts data
            
            .. attribute:: node_name  <key>
            
            	Node name
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: police
            
            	pl\_pifib police data
            	**type**\:   :py:class:`Police <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lpts_oper.PlatformLptspIfibStatic.NodeStatics.NodeStatic.Police>`
            
            .. attribute:: stats
            
            	pl\_pifib stats
            	**type**\:   :py:class:`Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lpts_oper.PlatformLptspIfibStatic.NodeStatics.NodeStatic.Stats>`
            
            

            """

            _prefix = 'asr9k-lpts-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(PlatformLptspIfibStatic.NodeStatics.NodeStatic, self).__init__()

                self.yang_name = "node-static"
                self.yang_parent_name = "node-statics"

                self.node_name = YLeaf(YType.str, "node-name")

                self.police = PlatformLptspIfibStatic.NodeStatics.NodeStatic.Police()
                self.police.parent = self
                self._children_name_map["police"] = "police"
                self._children_yang_names.add("police")

                self.stats = PlatformLptspIfibStatic.NodeStatics.NodeStatic.Stats()
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
                    if name in ("node_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(PlatformLptspIfibStatic.NodeStatics.NodeStatic, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(PlatformLptspIfibStatic.NodeStatics.NodeStatic, self).__setattr__(name, value)


            class Police(Entity):
                """
                pl\_pifib police data
                
                .. attribute:: static_info
                
                	Per punt reason info
                	**type**\: list of    :py:class:`StaticInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lpts_oper.PlatformLptspIfibStatic.NodeStatics.NodeStatic.Police.StaticInfo>`
                
                

                """

                _prefix = 'asr9k-lpts-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(PlatformLptspIfibStatic.NodeStatics.NodeStatic.Police, self).__init__()

                    self.yang_name = "police"
                    self.yang_parent_name = "node-static"

                    self.static_info = YList(self)

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
                                super(PlatformLptspIfibStatic.NodeStatics.NodeStatic.Police, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(PlatformLptspIfibStatic.NodeStatics.NodeStatic.Police, self).__setattr__(name, value)


                class StaticInfo(Entity):
                    """
                    Per punt reason info
                    
                    .. attribute:: accepted
                    
                    	accepted
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: burst_rate
                    
                    	burst rate
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: change_type
                    
                    	change type
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: dropped
                    
                    	dropped
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: flow_rate
                    
                    	flow rate
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: punt_reason
                    
                    	punt reason
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: punt_reason_string
                    
                    	punt reason string
                    	**type**\:  str
                    
                    	**length:** 0..50
                    
                    .. attribute:: sid
                    
                    	sid
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'asr9k-lpts-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PlatformLptspIfibStatic.NodeStatics.NodeStatic.Police.StaticInfo, self).__init__()

                        self.yang_name = "static-info"
                        self.yang_parent_name = "police"

                        self.accepted = YLeaf(YType.uint64, "accepted")

                        self.burst_rate = YLeaf(YType.uint32, "burst-rate")

                        self.change_type = YLeaf(YType.uint8, "change-type")

                        self.dropped = YLeaf(YType.uint64, "dropped")

                        self.flow_rate = YLeaf(YType.uint32, "flow-rate")

                        self.punt_reason = YLeaf(YType.uint32, "punt-reason")

                        self.punt_reason_string = YLeaf(YType.str, "punt-reason-string")

                        self.sid = YLeaf(YType.uint32, "sid")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("accepted",
                                        "burst_rate",
                                        "change_type",
                                        "dropped",
                                        "flow_rate",
                                        "punt_reason",
                                        "punt_reason_string",
                                        "sid") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PlatformLptspIfibStatic.NodeStatics.NodeStatic.Police.StaticInfo, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PlatformLptspIfibStatic.NodeStatics.NodeStatic.Police.StaticInfo, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.accepted.is_set or
                            self.burst_rate.is_set or
                            self.change_type.is_set or
                            self.dropped.is_set or
                            self.flow_rate.is_set or
                            self.punt_reason.is_set or
                            self.punt_reason_string.is_set or
                            self.sid.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.accepted.yfilter != YFilter.not_set or
                            self.burst_rate.yfilter != YFilter.not_set or
                            self.change_type.yfilter != YFilter.not_set or
                            self.dropped.yfilter != YFilter.not_set or
                            self.flow_rate.yfilter != YFilter.not_set or
                            self.punt_reason.yfilter != YFilter.not_set or
                            self.punt_reason_string.yfilter != YFilter.not_set or
                            self.sid.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "static-info" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.accepted.is_set or self.accepted.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.accepted.get_name_leafdata())
                        if (self.burst_rate.is_set or self.burst_rate.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.burst_rate.get_name_leafdata())
                        if (self.change_type.is_set or self.change_type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.change_type.get_name_leafdata())
                        if (self.dropped.is_set or self.dropped.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.dropped.get_name_leafdata())
                        if (self.flow_rate.is_set or self.flow_rate.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.flow_rate.get_name_leafdata())
                        if (self.punt_reason.is_set or self.punt_reason.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.punt_reason.get_name_leafdata())
                        if (self.punt_reason_string.is_set or self.punt_reason_string.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.punt_reason_string.get_name_leafdata())
                        if (self.sid.is_set or self.sid.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.sid.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "accepted" or name == "burst-rate" or name == "change-type" or name == "dropped" or name == "flow-rate" or name == "punt-reason" or name == "punt-reason-string" or name == "sid"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "accepted"):
                            self.accepted = value
                            self.accepted.value_namespace = name_space
                            self.accepted.value_namespace_prefix = name_space_prefix
                        if(value_path == "burst-rate"):
                            self.burst_rate = value
                            self.burst_rate.value_namespace = name_space
                            self.burst_rate.value_namespace_prefix = name_space_prefix
                        if(value_path == "change-type"):
                            self.change_type = value
                            self.change_type.value_namespace = name_space
                            self.change_type.value_namespace_prefix = name_space_prefix
                        if(value_path == "dropped"):
                            self.dropped = value
                            self.dropped.value_namespace = name_space
                            self.dropped.value_namespace_prefix = name_space_prefix
                        if(value_path == "flow-rate"):
                            self.flow_rate = value
                            self.flow_rate.value_namespace = name_space
                            self.flow_rate.value_namespace_prefix = name_space_prefix
                        if(value_path == "punt-reason"):
                            self.punt_reason = value
                            self.punt_reason.value_namespace = name_space
                            self.punt_reason.value_namespace_prefix = name_space_prefix
                        if(value_path == "punt-reason-string"):
                            self.punt_reason_string = value
                            self.punt_reason_string.value_namespace = name_space
                            self.punt_reason_string.value_namespace_prefix = name_space_prefix
                        if(value_path == "sid"):
                            self.sid = value
                            self.sid.value_namespace = name_space
                            self.sid.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.static_info:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.static_info:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "police" + path_buffer

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

                    if (child_yang_name == "static-info"):
                        for c in self.static_info:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = PlatformLptspIfibStatic.NodeStatics.NodeStatic.Police.StaticInfo()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.static_info.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "static-info"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Stats(Entity):
                """
                pl\_pifib stats
                
                .. attribute:: accepted
                
                	Deleted\-entry accepted packets counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: clear_ts
                
                	Statistics clear timestamp
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: dropped
                
                	Deleted\-entry dropped packets counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: no_stats_mem_err
                
                	No statistics memory error
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'asr9k-lpts-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(PlatformLptspIfibStatic.NodeStatics.NodeStatic.Stats, self).__init__()

                    self.yang_name = "stats"
                    self.yang_parent_name = "node-static"

                    self.accepted = YLeaf(YType.uint64, "accepted")

                    self.clear_ts = YLeaf(YType.uint64, "clear-ts")

                    self.dropped = YLeaf(YType.uint64, "dropped")

                    self.no_stats_mem_err = YLeaf(YType.uint64, "no-stats-mem-err")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("accepted",
                                    "clear_ts",
                                    "dropped",
                                    "no_stats_mem_err") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(PlatformLptspIfibStatic.NodeStatics.NodeStatic.Stats, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(PlatformLptspIfibStatic.NodeStatics.NodeStatic.Stats, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.accepted.is_set or
                        self.clear_ts.is_set or
                        self.dropped.is_set or
                        self.no_stats_mem_err.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.accepted.yfilter != YFilter.not_set or
                        self.clear_ts.yfilter != YFilter.not_set or
                        self.dropped.yfilter != YFilter.not_set or
                        self.no_stats_mem_err.yfilter != YFilter.not_set)

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
                    if (self.accepted.is_set or self.accepted.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.accepted.get_name_leafdata())
                    if (self.clear_ts.is_set or self.clear_ts.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.clear_ts.get_name_leafdata())
                    if (self.dropped.is_set or self.dropped.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.dropped.get_name_leafdata())
                    if (self.no_stats_mem_err.is_set or self.no_stats_mem_err.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.no_stats_mem_err.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "accepted" or name == "clear-ts" or name == "dropped" or name == "no-stats-mem-err"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "accepted"):
                        self.accepted = value
                        self.accepted.value_namespace = name_space
                        self.accepted.value_namespace_prefix = name_space_prefix
                    if(value_path == "clear-ts"):
                        self.clear_ts = value
                        self.clear_ts.value_namespace = name_space
                        self.clear_ts.value_namespace_prefix = name_space_prefix
                    if(value_path == "dropped"):
                        self.dropped = value
                        self.dropped.value_namespace = name_space
                        self.dropped.value_namespace_prefix = name_space_prefix
                    if(value_path == "no-stats-mem-err"):
                        self.no_stats_mem_err = value
                        self.no_stats_mem_err.value_namespace = name_space
                        self.no_stats_mem_err.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.node_name.is_set or
                    (self.police is not None and self.police.has_data()) or
                    (self.stats is not None and self.stats.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.node_name.yfilter != YFilter.not_set or
                    (self.police is not None and self.police.has_operation()) or
                    (self.stats is not None and self.stats.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "node-static" + "[node-name='" + self.node_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-asr9k-lpts-oper:platform-lptsp-ifib-static/node-statics/%s" % self.get_segment_path()
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

                if (child_yang_name == "police"):
                    if (self.police is None):
                        self.police = PlatformLptspIfibStatic.NodeStatics.NodeStatic.Police()
                        self.police.parent = self
                        self._children_name_map["police"] = "police"
                    return self.police

                if (child_yang_name == "stats"):
                    if (self.stats is None):
                        self.stats = PlatformLptspIfibStatic.NodeStatics.NodeStatic.Stats()
                        self.stats.parent = self
                        self._children_name_map["stats"] = "stats"
                    return self.stats

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "police" or name == "stats" or name == "node-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "node-name"):
                    self.node_name = value
                    self.node_name.value_namespace = name_space
                    self.node_name.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.node_static:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.node_static:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "node-statics" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-asr9k-lpts-oper:platform-lptsp-ifib-static/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "node-static"):
                for c in self.node_static:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = PlatformLptspIfibStatic.NodeStatics.NodeStatic()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.node_static.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "node-static"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.node_statics is not None and self.node_statics.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.node_statics is not None and self.node_statics.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-asr9k-lpts-oper:platform-lptsp-ifib-static" + path_buffer

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

        if (child_yang_name == "node-statics"):
            if (self.node_statics is None):
                self.node_statics = PlatformLptspIfibStatic.NodeStatics()
                self.node_statics.parent = self
                self._children_name_map["node_statics"] = "node-statics"
            return self.node_statics

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "node-statics"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = PlatformLptspIfibStatic()
        return self._top_entity

class PlatformLptspIfib(Entity):
    """
    platform lptsp ifib
    
    .. attribute:: nodes
    
    	List of nodes with platform specific lpts operation data
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lpts_oper.PlatformLptspIfib.Nodes>`
    
    

    """

    _prefix = 'asr9k-lpts-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(PlatformLptspIfib, self).__init__()
        self._top_entity = None

        self.yang_name = "platform-lptsp-ifib"
        self.yang_parent_name = "Cisco-IOS-XR-asr9k-lpts-oper"

        self.nodes = PlatformLptspIfib.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")


    class Nodes(Entity):
        """
        List of nodes with platform specific lpts
        operation data
        
        .. attribute:: node
        
        	Node with platform specific lpts data
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lpts_oper.PlatformLptspIfib.Nodes.Node>`
        
        

        """

        _prefix = 'asr9k-lpts-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(PlatformLptspIfib.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "platform-lptsp-ifib"

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
                        super(PlatformLptspIfib.Nodes, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(PlatformLptspIfib.Nodes, self).__setattr__(name, value)


        class Node(Entity):
            """
            Node with platform specific lpts data
            
            .. attribute:: node_name  <key>
            
            	Node name
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: police
            
            	pl\_pifib police data
            	**type**\:   :py:class:`Police <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lpts_oper.PlatformLptspIfib.Nodes.Node.Police>`
            
            .. attribute:: stats
            
            	pl\_pifib stats
            	**type**\:   :py:class:`Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lpts_oper.PlatformLptspIfib.Nodes.Node.Stats>`
            
            

            """

            _prefix = 'asr9k-lpts-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(PlatformLptspIfib.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"

                self.node_name = YLeaf(YType.str, "node-name")

                self.police = PlatformLptspIfib.Nodes.Node.Police()
                self.police.parent = self
                self._children_name_map["police"] = "police"
                self._children_yang_names.add("police")

                self.stats = PlatformLptspIfib.Nodes.Node.Stats()
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
                    if name in ("node_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(PlatformLptspIfib.Nodes.Node, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(PlatformLptspIfib.Nodes.Node, self).__setattr__(name, value)


            class Police(Entity):
                """
                pl\_pifib police data
                
                .. attribute:: police_info
                
                	Per flow type police info
                	**type**\: list of    :py:class:`PoliceInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lpts_oper.PlatformLptspIfib.Nodes.Node.Police.PoliceInfo>`
                
                

                """

                _prefix = 'asr9k-lpts-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(PlatformLptspIfib.Nodes.Node.Police, self).__init__()

                    self.yang_name = "police"
                    self.yang_parent_name = "node"

                    self.police_info = YList(self)

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
                                super(PlatformLptspIfib.Nodes.Node.Police, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(PlatformLptspIfib.Nodes.Node.Police, self).__setattr__(name, value)


                class PoliceInfo(Entity):
                    """
                    Per flow type police info
                    
                    .. attribute:: accepted_stats
                    
                    	accepted stats
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: acl_config
                    
                    	acl config
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: acl_str
                    
                    	acl str
                    	**type**\:  str
                    
                    	**length:** 0..50
                    
                    .. attribute:: avgrate
                    
                    	avgrate
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: avgrate_type
                    
                    	avgrate type
                    	**type**\:  str
                    
                    	**length:** 0..50
                    
                    .. attribute:: burst
                    
                    	burst
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: change_type
                    
                    	change type
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: dropped_stats
                    
                    	dropped stats
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: flow_type
                    
                    	flow type
                    	**type**\:  str
                    
                    	**length:** 0..50
                    
                    .. attribute:: policer
                    
                    	policer
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: static_avgrate
                    
                    	static avgrate
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: str_iptos_val
                    
                    	str iptos val
                    	**type**\:  str
                    
                    	**length:** 0..8
                    
                    

                    """

                    _prefix = 'asr9k-lpts-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PlatformLptspIfib.Nodes.Node.Police.PoliceInfo, self).__init__()

                        self.yang_name = "police-info"
                        self.yang_parent_name = "police"

                        self.accepted_stats = YLeaf(YType.uint64, "accepted-stats")

                        self.acl_config = YLeaf(YType.uint8, "acl-config")

                        self.acl_str = YLeaf(YType.str, "acl-str")

                        self.avgrate = YLeaf(YType.uint32, "avgrate")

                        self.avgrate_type = YLeaf(YType.str, "avgrate-type")

                        self.burst = YLeaf(YType.uint32, "burst")

                        self.change_type = YLeaf(YType.uint8, "change-type")

                        self.dropped_stats = YLeaf(YType.uint64, "dropped-stats")

                        self.flow_type = YLeaf(YType.str, "flow-type")

                        self.policer = YLeaf(YType.uint32, "policer")

                        self.static_avgrate = YLeaf(YType.uint32, "static-avgrate")

                        self.str_iptos_val = YLeaf(YType.str, "str-iptos-val")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("accepted_stats",
                                        "acl_config",
                                        "acl_str",
                                        "avgrate",
                                        "avgrate_type",
                                        "burst",
                                        "change_type",
                                        "dropped_stats",
                                        "flow_type",
                                        "policer",
                                        "static_avgrate",
                                        "str_iptos_val") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PlatformLptspIfib.Nodes.Node.Police.PoliceInfo, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PlatformLptspIfib.Nodes.Node.Police.PoliceInfo, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.accepted_stats.is_set or
                            self.acl_config.is_set or
                            self.acl_str.is_set or
                            self.avgrate.is_set or
                            self.avgrate_type.is_set or
                            self.burst.is_set or
                            self.change_type.is_set or
                            self.dropped_stats.is_set or
                            self.flow_type.is_set or
                            self.policer.is_set or
                            self.static_avgrate.is_set or
                            self.str_iptos_val.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.accepted_stats.yfilter != YFilter.not_set or
                            self.acl_config.yfilter != YFilter.not_set or
                            self.acl_str.yfilter != YFilter.not_set or
                            self.avgrate.yfilter != YFilter.not_set or
                            self.avgrate_type.yfilter != YFilter.not_set or
                            self.burst.yfilter != YFilter.not_set or
                            self.change_type.yfilter != YFilter.not_set or
                            self.dropped_stats.yfilter != YFilter.not_set or
                            self.flow_type.yfilter != YFilter.not_set or
                            self.policer.yfilter != YFilter.not_set or
                            self.static_avgrate.yfilter != YFilter.not_set or
                            self.str_iptos_val.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "police-info" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.accepted_stats.is_set or self.accepted_stats.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.accepted_stats.get_name_leafdata())
                        if (self.acl_config.is_set or self.acl_config.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.acl_config.get_name_leafdata())
                        if (self.acl_str.is_set or self.acl_str.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.acl_str.get_name_leafdata())
                        if (self.avgrate.is_set or self.avgrate.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.avgrate.get_name_leafdata())
                        if (self.avgrate_type.is_set or self.avgrate_type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.avgrate_type.get_name_leafdata())
                        if (self.burst.is_set or self.burst.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.burst.get_name_leafdata())
                        if (self.change_type.is_set or self.change_type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.change_type.get_name_leafdata())
                        if (self.dropped_stats.is_set or self.dropped_stats.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.dropped_stats.get_name_leafdata())
                        if (self.flow_type.is_set or self.flow_type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.flow_type.get_name_leafdata())
                        if (self.policer.is_set or self.policer.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.policer.get_name_leafdata())
                        if (self.static_avgrate.is_set or self.static_avgrate.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.static_avgrate.get_name_leafdata())
                        if (self.str_iptos_val.is_set or self.str_iptos_val.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.str_iptos_val.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "accepted-stats" or name == "acl-config" or name == "acl-str" or name == "avgrate" or name == "avgrate-type" or name == "burst" or name == "change-type" or name == "dropped-stats" or name == "flow-type" or name == "policer" or name == "static-avgrate" or name == "str-iptos-val"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "accepted-stats"):
                            self.accepted_stats = value
                            self.accepted_stats.value_namespace = name_space
                            self.accepted_stats.value_namespace_prefix = name_space_prefix
                        if(value_path == "acl-config"):
                            self.acl_config = value
                            self.acl_config.value_namespace = name_space
                            self.acl_config.value_namespace_prefix = name_space_prefix
                        if(value_path == "acl-str"):
                            self.acl_str = value
                            self.acl_str.value_namespace = name_space
                            self.acl_str.value_namespace_prefix = name_space_prefix
                        if(value_path == "avgrate"):
                            self.avgrate = value
                            self.avgrate.value_namespace = name_space
                            self.avgrate.value_namespace_prefix = name_space_prefix
                        if(value_path == "avgrate-type"):
                            self.avgrate_type = value
                            self.avgrate_type.value_namespace = name_space
                            self.avgrate_type.value_namespace_prefix = name_space_prefix
                        if(value_path == "burst"):
                            self.burst = value
                            self.burst.value_namespace = name_space
                            self.burst.value_namespace_prefix = name_space_prefix
                        if(value_path == "change-type"):
                            self.change_type = value
                            self.change_type.value_namespace = name_space
                            self.change_type.value_namespace_prefix = name_space_prefix
                        if(value_path == "dropped-stats"):
                            self.dropped_stats = value
                            self.dropped_stats.value_namespace = name_space
                            self.dropped_stats.value_namespace_prefix = name_space_prefix
                        if(value_path == "flow-type"):
                            self.flow_type = value
                            self.flow_type.value_namespace = name_space
                            self.flow_type.value_namespace_prefix = name_space_prefix
                        if(value_path == "policer"):
                            self.policer = value
                            self.policer.value_namespace = name_space
                            self.policer.value_namespace_prefix = name_space_prefix
                        if(value_path == "static-avgrate"):
                            self.static_avgrate = value
                            self.static_avgrate.value_namespace = name_space
                            self.static_avgrate.value_namespace_prefix = name_space_prefix
                        if(value_path == "str-iptos-val"):
                            self.str_iptos_val = value
                            self.str_iptos_val.value_namespace = name_space
                            self.str_iptos_val.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.police_info:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.police_info:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "police" + path_buffer

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

                    if (child_yang_name == "police-info"):
                        for c in self.police_info:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = PlatformLptspIfib.Nodes.Node.Police.PoliceInfo()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.police_info.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "police-info"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Stats(Entity):
                """
                pl\_pifib stats
                
                .. attribute:: accepted
                
                	Deleted\-entry accepted packets counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: clear_ts
                
                	Statistics clear timestamp
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: dropped
                
                	Deleted\-entry dropped packets counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: no_stats_mem_err
                
                	No statistics memory error
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'asr9k-lpts-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(PlatformLptspIfib.Nodes.Node.Stats, self).__init__()

                    self.yang_name = "stats"
                    self.yang_parent_name = "node"

                    self.accepted = YLeaf(YType.uint64, "accepted")

                    self.clear_ts = YLeaf(YType.uint64, "clear-ts")

                    self.dropped = YLeaf(YType.uint64, "dropped")

                    self.no_stats_mem_err = YLeaf(YType.uint64, "no-stats-mem-err")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("accepted",
                                    "clear_ts",
                                    "dropped",
                                    "no_stats_mem_err") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(PlatformLptspIfib.Nodes.Node.Stats, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(PlatformLptspIfib.Nodes.Node.Stats, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.accepted.is_set or
                        self.clear_ts.is_set or
                        self.dropped.is_set or
                        self.no_stats_mem_err.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.accepted.yfilter != YFilter.not_set or
                        self.clear_ts.yfilter != YFilter.not_set or
                        self.dropped.yfilter != YFilter.not_set or
                        self.no_stats_mem_err.yfilter != YFilter.not_set)

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
                    if (self.accepted.is_set or self.accepted.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.accepted.get_name_leafdata())
                    if (self.clear_ts.is_set or self.clear_ts.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.clear_ts.get_name_leafdata())
                    if (self.dropped.is_set or self.dropped.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.dropped.get_name_leafdata())
                    if (self.no_stats_mem_err.is_set or self.no_stats_mem_err.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.no_stats_mem_err.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "accepted" or name == "clear-ts" or name == "dropped" or name == "no-stats-mem-err"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "accepted"):
                        self.accepted = value
                        self.accepted.value_namespace = name_space
                        self.accepted.value_namespace_prefix = name_space_prefix
                    if(value_path == "clear-ts"):
                        self.clear_ts = value
                        self.clear_ts.value_namespace = name_space
                        self.clear_ts.value_namespace_prefix = name_space_prefix
                    if(value_path == "dropped"):
                        self.dropped = value
                        self.dropped.value_namespace = name_space
                        self.dropped.value_namespace_prefix = name_space_prefix
                    if(value_path == "no-stats-mem-err"):
                        self.no_stats_mem_err = value
                        self.no_stats_mem_err.value_namespace = name_space
                        self.no_stats_mem_err.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.node_name.is_set or
                    (self.police is not None and self.police.has_data()) or
                    (self.stats is not None and self.stats.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.node_name.yfilter != YFilter.not_set or
                    (self.police is not None and self.police.has_operation()) or
                    (self.stats is not None and self.stats.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "node" + "[node-name='" + self.node_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-asr9k-lpts-oper:platform-lptsp-ifib/nodes/%s" % self.get_segment_path()
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

                if (child_yang_name == "police"):
                    if (self.police is None):
                        self.police = PlatformLptspIfib.Nodes.Node.Police()
                        self.police.parent = self
                        self._children_name_map["police"] = "police"
                    return self.police

                if (child_yang_name == "stats"):
                    if (self.stats is None):
                        self.stats = PlatformLptspIfib.Nodes.Node.Stats()
                        self.stats.parent = self
                        self._children_name_map["stats"] = "stats"
                    return self.stats

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "police" or name == "stats" or name == "node-name"):
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
                path_buffer = "Cisco-IOS-XR-asr9k-lpts-oper:platform-lptsp-ifib/%s" % self.get_segment_path()
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
                c = PlatformLptspIfib.Nodes.Node()
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
        path_buffer = "Cisco-IOS-XR-asr9k-lpts-oper:platform-lptsp-ifib" + path_buffer

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
                self.nodes = PlatformLptspIfib.Nodes()
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
        self._top_entity = PlatformLptspIfib()
        return self._top_entity

class PlatformLptspIfibNpStats(Entity):
    """
    platform lptsp ifib np stats
    
    .. attribute:: node_np_stats
    
    	List of nodes with platform specific lpts operation data
    	**type**\:   :py:class:`NodeNpStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lpts_oper.PlatformLptspIfibNpStats.NodeNpStats>`
    
    

    """

    _prefix = 'asr9k-lpts-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(PlatformLptspIfibNpStats, self).__init__()
        self._top_entity = None

        self.yang_name = "platform-lptsp-ifib-np-stats"
        self.yang_parent_name = "Cisco-IOS-XR-asr9k-lpts-oper"

        self.node_np_stats = PlatformLptspIfibNpStats.NodeNpStats()
        self.node_np_stats.parent = self
        self._children_name_map["node_np_stats"] = "node-np-stats"
        self._children_yang_names.add("node-np-stats")


    class NodeNpStats(Entity):
        """
        List of nodes with platform specific lpts
        operation data
        
        .. attribute:: node_np_stat
        
        	Node with platform specific lpts data
        	**type**\: list of    :py:class:`NodeNpStat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lpts_oper.PlatformLptspIfibNpStats.NodeNpStats.NodeNpStat>`
        
        

        """

        _prefix = 'asr9k-lpts-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(PlatformLptspIfibNpStats.NodeNpStats, self).__init__()

            self.yang_name = "node-np-stats"
            self.yang_parent_name = "platform-lptsp-ifib-np-stats"

            self.node_np_stat = YList(self)

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
                        super(PlatformLptspIfibNpStats.NodeNpStats, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(PlatformLptspIfibNpStats.NodeNpStats, self).__setattr__(name, value)


        class NodeNpStat(Entity):
            """
            Node with platform specific lpts data
            
            .. attribute:: node_name  <key>
            
            	Node name
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: nps
            
            	List of all NP
            	**type**\:   :py:class:`Nps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lpts_oper.PlatformLptspIfibNpStats.NodeNpStats.NodeNpStat.Nps>`
            
            

            """

            _prefix = 'asr9k-lpts-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(PlatformLptspIfibNpStats.NodeNpStats.NodeNpStat, self).__init__()

                self.yang_name = "node-np-stat"
                self.yang_parent_name = "node-np-stats"

                self.node_name = YLeaf(YType.str, "node-name")

                self.nps = PlatformLptspIfibNpStats.NodeNpStats.NodeNpStat.Nps()
                self.nps.parent = self
                self._children_name_map["nps"] = "nps"
                self._children_yang_names.add("nps")

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
                            super(PlatformLptspIfibNpStats.NodeNpStats.NodeNpStat, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(PlatformLptspIfibNpStats.NodeNpStats.NodeNpStat, self).__setattr__(name, value)


            class Nps(Entity):
                """
                List of all NP
                
                .. attribute:: np
                
                	np0 to np7
                	**type**\: list of    :py:class:`Np <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lpts_oper.PlatformLptspIfibNpStats.NodeNpStats.NodeNpStat.Nps.Np>`
                
                

                """

                _prefix = 'asr9k-lpts-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(PlatformLptspIfibNpStats.NodeNpStats.NodeNpStat.Nps, self).__init__()

                    self.yang_name = "nps"
                    self.yang_parent_name = "node-np-stat"

                    self.np = YList(self)

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
                                super(PlatformLptspIfibNpStats.NodeNpStats.NodeNpStat.Nps, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(PlatformLptspIfibNpStats.NodeNpStats.NodeNpStat.Nps, self).__setattr__(name, value)


                class Np(Entity):
                    """
                    np0 to np7
                    
                    .. attribute:: np_name  <key>
                    
                    	NP name
                    	**type**\:  str
                    
                    	**pattern:** (np0)\|(np1)\|(np2)\|(np3)\|(np4)\|(np5)\|(np6)\|(np7)
                    
                    .. attribute:: np_police
                    
                    	pl\_pifib police data
                    	**type**\:   :py:class:`NpPolice <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lpts_oper.PlatformLptspIfibNpStats.NodeNpStats.NodeNpStat.Nps.Np.NpPolice>`
                    
                    

                    """

                    _prefix = 'asr9k-lpts-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PlatformLptspIfibNpStats.NodeNpStats.NodeNpStat.Nps.Np, self).__init__()

                        self.yang_name = "np"
                        self.yang_parent_name = "nps"

                        self.np_name = YLeaf(YType.str, "np-name")

                        self.np_police = PlatformLptspIfibNpStats.NodeNpStats.NodeNpStat.Nps.Np.NpPolice()
                        self.np_police.parent = self
                        self._children_name_map["np_police"] = "np-police"
                        self._children_yang_names.add("np-police")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("np_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PlatformLptspIfibNpStats.NodeNpStats.NodeNpStat.Nps.Np, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PlatformLptspIfibNpStats.NodeNpStats.NodeNpStat.Nps.Np, self).__setattr__(name, value)


                    class NpPolice(Entity):
                        """
                        pl\_pifib police data
                        
                        .. attribute:: police_info
                        
                        	Per flow type police info
                        	**type**\: list of    :py:class:`PoliceInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lpts_oper.PlatformLptspIfibNpStats.NodeNpStats.NodeNpStat.Nps.Np.NpPolice.PoliceInfo>`
                        
                        

                        """

                        _prefix = 'asr9k-lpts-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(PlatformLptspIfibNpStats.NodeNpStats.NodeNpStat.Nps.Np.NpPolice, self).__init__()

                            self.yang_name = "np-police"
                            self.yang_parent_name = "np"

                            self.police_info = YList(self)

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
                                        super(PlatformLptspIfibNpStats.NodeNpStats.NodeNpStat.Nps.Np.NpPolice, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(PlatformLptspIfibNpStats.NodeNpStats.NodeNpStat.Nps.Np.NpPolice, self).__setattr__(name, value)


                        class PoliceInfo(Entity):
                            """
                            Per flow type police info
                            
                            .. attribute:: accepted_stats
                            
                            	accepted stats
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: acl_config
                            
                            	acl config
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: acl_str
                            
                            	acl str
                            	**type**\:  str
                            
                            	**length:** 0..50
                            
                            .. attribute:: avgrate
                            
                            	avgrate
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: avgrate_type
                            
                            	avgrate type
                            	**type**\:  str
                            
                            	**length:** 0..50
                            
                            .. attribute:: burst
                            
                            	burst
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: change_type
                            
                            	change type
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: dropped_stats
                            
                            	dropped stats
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: flow_type
                            
                            	flow type
                            	**type**\:  str
                            
                            	**length:** 0..50
                            
                            .. attribute:: policer
                            
                            	policer
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: static_avgrate
                            
                            	static avgrate
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: str_iptos_val
                            
                            	str iptos val
                            	**type**\:  str
                            
                            	**length:** 0..8
                            
                            

                            """

                            _prefix = 'asr9k-lpts-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(PlatformLptspIfibNpStats.NodeNpStats.NodeNpStat.Nps.Np.NpPolice.PoliceInfo, self).__init__()

                                self.yang_name = "police-info"
                                self.yang_parent_name = "np-police"

                                self.accepted_stats = YLeaf(YType.uint64, "accepted-stats")

                                self.acl_config = YLeaf(YType.uint8, "acl-config")

                                self.acl_str = YLeaf(YType.str, "acl-str")

                                self.avgrate = YLeaf(YType.uint32, "avgrate")

                                self.avgrate_type = YLeaf(YType.str, "avgrate-type")

                                self.burst = YLeaf(YType.uint32, "burst")

                                self.change_type = YLeaf(YType.uint8, "change-type")

                                self.dropped_stats = YLeaf(YType.uint64, "dropped-stats")

                                self.flow_type = YLeaf(YType.str, "flow-type")

                                self.policer = YLeaf(YType.uint32, "policer")

                                self.static_avgrate = YLeaf(YType.uint32, "static-avgrate")

                                self.str_iptos_val = YLeaf(YType.str, "str-iptos-val")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("accepted_stats",
                                                "acl_config",
                                                "acl_str",
                                                "avgrate",
                                                "avgrate_type",
                                                "burst",
                                                "change_type",
                                                "dropped_stats",
                                                "flow_type",
                                                "policer",
                                                "static_avgrate",
                                                "str_iptos_val") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(PlatformLptspIfibNpStats.NodeNpStats.NodeNpStat.Nps.Np.NpPolice.PoliceInfo, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(PlatformLptspIfibNpStats.NodeNpStats.NodeNpStat.Nps.Np.NpPolice.PoliceInfo, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.accepted_stats.is_set or
                                    self.acl_config.is_set or
                                    self.acl_str.is_set or
                                    self.avgrate.is_set or
                                    self.avgrate_type.is_set or
                                    self.burst.is_set or
                                    self.change_type.is_set or
                                    self.dropped_stats.is_set or
                                    self.flow_type.is_set or
                                    self.policer.is_set or
                                    self.static_avgrate.is_set or
                                    self.str_iptos_val.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.accepted_stats.yfilter != YFilter.not_set or
                                    self.acl_config.yfilter != YFilter.not_set or
                                    self.acl_str.yfilter != YFilter.not_set or
                                    self.avgrate.yfilter != YFilter.not_set or
                                    self.avgrate_type.yfilter != YFilter.not_set or
                                    self.burst.yfilter != YFilter.not_set or
                                    self.change_type.yfilter != YFilter.not_set or
                                    self.dropped_stats.yfilter != YFilter.not_set or
                                    self.flow_type.yfilter != YFilter.not_set or
                                    self.policer.yfilter != YFilter.not_set or
                                    self.static_avgrate.yfilter != YFilter.not_set or
                                    self.str_iptos_val.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "police-info" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.accepted_stats.is_set or self.accepted_stats.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.accepted_stats.get_name_leafdata())
                                if (self.acl_config.is_set or self.acl_config.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.acl_config.get_name_leafdata())
                                if (self.acl_str.is_set or self.acl_str.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.acl_str.get_name_leafdata())
                                if (self.avgrate.is_set or self.avgrate.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.avgrate.get_name_leafdata())
                                if (self.avgrate_type.is_set or self.avgrate_type.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.avgrate_type.get_name_leafdata())
                                if (self.burst.is_set or self.burst.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.burst.get_name_leafdata())
                                if (self.change_type.is_set or self.change_type.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.change_type.get_name_leafdata())
                                if (self.dropped_stats.is_set or self.dropped_stats.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.dropped_stats.get_name_leafdata())
                                if (self.flow_type.is_set or self.flow_type.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.flow_type.get_name_leafdata())
                                if (self.policer.is_set or self.policer.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.policer.get_name_leafdata())
                                if (self.static_avgrate.is_set or self.static_avgrate.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.static_avgrate.get_name_leafdata())
                                if (self.str_iptos_val.is_set or self.str_iptos_val.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.str_iptos_val.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "accepted-stats" or name == "acl-config" or name == "acl-str" or name == "avgrate" or name == "avgrate-type" or name == "burst" or name == "change-type" or name == "dropped-stats" or name == "flow-type" or name == "policer" or name == "static-avgrate" or name == "str-iptos-val"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "accepted-stats"):
                                    self.accepted_stats = value
                                    self.accepted_stats.value_namespace = name_space
                                    self.accepted_stats.value_namespace_prefix = name_space_prefix
                                if(value_path == "acl-config"):
                                    self.acl_config = value
                                    self.acl_config.value_namespace = name_space
                                    self.acl_config.value_namespace_prefix = name_space_prefix
                                if(value_path == "acl-str"):
                                    self.acl_str = value
                                    self.acl_str.value_namespace = name_space
                                    self.acl_str.value_namespace_prefix = name_space_prefix
                                if(value_path == "avgrate"):
                                    self.avgrate = value
                                    self.avgrate.value_namespace = name_space
                                    self.avgrate.value_namespace_prefix = name_space_prefix
                                if(value_path == "avgrate-type"):
                                    self.avgrate_type = value
                                    self.avgrate_type.value_namespace = name_space
                                    self.avgrate_type.value_namespace_prefix = name_space_prefix
                                if(value_path == "burst"):
                                    self.burst = value
                                    self.burst.value_namespace = name_space
                                    self.burst.value_namespace_prefix = name_space_prefix
                                if(value_path == "change-type"):
                                    self.change_type = value
                                    self.change_type.value_namespace = name_space
                                    self.change_type.value_namespace_prefix = name_space_prefix
                                if(value_path == "dropped-stats"):
                                    self.dropped_stats = value
                                    self.dropped_stats.value_namespace = name_space
                                    self.dropped_stats.value_namespace_prefix = name_space_prefix
                                if(value_path == "flow-type"):
                                    self.flow_type = value
                                    self.flow_type.value_namespace = name_space
                                    self.flow_type.value_namespace_prefix = name_space_prefix
                                if(value_path == "policer"):
                                    self.policer = value
                                    self.policer.value_namespace = name_space
                                    self.policer.value_namespace_prefix = name_space_prefix
                                if(value_path == "static-avgrate"):
                                    self.static_avgrate = value
                                    self.static_avgrate.value_namespace = name_space
                                    self.static_avgrate.value_namespace_prefix = name_space_prefix
                                if(value_path == "str-iptos-val"):
                                    self.str_iptos_val = value
                                    self.str_iptos_val.value_namespace = name_space
                                    self.str_iptos_val.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.police_info:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.police_info:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "np-police" + path_buffer

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

                            if (child_yang_name == "police-info"):
                                for c in self.police_info:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = PlatformLptspIfibNpStats.NodeNpStats.NodeNpStat.Nps.Np.NpPolice.PoliceInfo()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.police_info.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "police-info"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (
                            self.np_name.is_set or
                            (self.np_police is not None and self.np_police.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.np_name.yfilter != YFilter.not_set or
                            (self.np_police is not None and self.np_police.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "np" + "[np-name='" + self.np_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.np_name.is_set or self.np_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.np_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "np-police"):
                            if (self.np_police is None):
                                self.np_police = PlatformLptspIfibNpStats.NodeNpStats.NodeNpStat.Nps.Np.NpPolice()
                                self.np_police.parent = self
                                self._children_name_map["np_police"] = "np-police"
                            return self.np_police

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "np-police" or name == "np-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "np-name"):
                            self.np_name = value
                            self.np_name.value_namespace = name_space
                            self.np_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.np:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.np:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "nps" + path_buffer

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

                    if (child_yang_name == "np"):
                        for c in self.np:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = PlatformLptspIfibNpStats.NodeNpStats.NodeNpStat.Nps.Np()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.np.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "np"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.node_name.is_set or
                    (self.nps is not None and self.nps.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.node_name.yfilter != YFilter.not_set or
                    (self.nps is not None and self.nps.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "node-np-stat" + "[node-name='" + self.node_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-asr9k-lpts-oper:platform-lptsp-ifib-np-stats/node-np-stats/%s" % self.get_segment_path()
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

                if (child_yang_name == "nps"):
                    if (self.nps is None):
                        self.nps = PlatformLptspIfibNpStats.NodeNpStats.NodeNpStat.Nps()
                        self.nps.parent = self
                        self._children_name_map["nps"] = "nps"
                    return self.nps

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "nps" or name == "node-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "node-name"):
                    self.node_name = value
                    self.node_name.value_namespace = name_space
                    self.node_name.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.node_np_stat:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.node_np_stat:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "node-np-stats" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-asr9k-lpts-oper:platform-lptsp-ifib-np-stats/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "node-np-stat"):
                for c in self.node_np_stat:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = PlatformLptspIfibNpStats.NodeNpStats.NodeNpStat()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.node_np_stat.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "node-np-stat"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.node_np_stats is not None and self.node_np_stats.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.node_np_stats is not None and self.node_np_stats.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-asr9k-lpts-oper:platform-lptsp-ifib-np-stats" + path_buffer

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

        if (child_yang_name == "node-np-stats"):
            if (self.node_np_stats is None):
                self.node_np_stats = PlatformLptspIfibNpStats.NodeNpStats()
                self.node_np_stats.parent = self
                self._children_name_map["node_np_stats"] = "node-np-stats"
            return self.node_np_stats

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "node-np-stats"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = PlatformLptspIfibNpStats()
        return self._top_entity

