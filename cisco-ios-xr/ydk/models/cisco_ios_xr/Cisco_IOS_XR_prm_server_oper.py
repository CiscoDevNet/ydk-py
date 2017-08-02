""" Cisco_IOS_XR_prm_server_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR prm\-server package operational data.

This module contains definitions
for the following management objects\:
  hardware\-module\: PRM data
  prm\: prm

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class HardwareModule(Entity):
    """
    PRM data
    
    .. attribute:: nodes
    
    	List of PRM Nodes
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper.HardwareModule.Nodes>`
    
    

    """

    _prefix = 'prm-server-oper'
    _revision = '2016-02-22'

    def __init__(self):
        super(HardwareModule, self).__init__()
        self._top_entity = None

        self.yang_name = "hardware-module"
        self.yang_parent_name = "Cisco-IOS-XR-prm-server-oper"

        self.nodes = HardwareModule.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")


    class Nodes(Entity):
        """
        List of PRM Nodes
        
        .. attribute:: node
        
        	Node Information
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper.HardwareModule.Nodes.Node>`
        
        

        """

        _prefix = 'prm-server-oper'
        _revision = '2016-02-22'

        def __init__(self):
            super(HardwareModule.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "hardware-module"

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
                        super(HardwareModule.Nodes, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(HardwareModule.Nodes, self).__setattr__(name, value)


        class Node(Entity):
            """
            Node Information
            
            .. attribute:: node_name  <key>
            
            	The node name
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: np
            
            	Server specific
            	**type**\:   :py:class:`Np <ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper.HardwareModule.Nodes.Node.Np>`
            
            

            """

            _prefix = 'prm-server-oper'
            _revision = '2016-02-22'

            def __init__(self):
                super(HardwareModule.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"

                self.node_name = YLeaf(YType.str, "node-name")

                self.np = HardwareModule.Nodes.Node.Np()
                self.np.parent = self
                self._children_name_map["np"] = "np"
                self._children_yang_names.add("np")

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
                            super(HardwareModule.Nodes.Node, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(HardwareModule.Nodes.Node, self).__setattr__(name, value)


            class Np(Entity):
                """
                Server specific
                
                .. attribute:: cpu
                
                	Resource specific
                	**type**\:   :py:class:`Cpu <ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper.HardwareModule.Nodes.Node.Np.Cpu>`
                
                .. attribute:: platform_drop
                
                	Platform drops
                	**type**\:   :py:class:`PlatformDrop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper.HardwareModule.Nodes.Node.Np.PlatformDrop>`
                
                

                """

                _prefix = 'prm-server-oper'
                _revision = '2016-02-22'

                def __init__(self):
                    super(HardwareModule.Nodes.Node.Np, self).__init__()

                    self.yang_name = "np"
                    self.yang_parent_name = "node"

                    self.cpu = HardwareModule.Nodes.Node.Np.Cpu()
                    self.cpu.parent = self
                    self._children_name_map["cpu"] = "cpu"
                    self._children_yang_names.add("cpu")

                    self.platform_drop = HardwareModule.Nodes.Node.Np.PlatformDrop()
                    self.platform_drop.parent = self
                    self._children_name_map["platform_drop"] = "platform-drop"
                    self._children_yang_names.add("platform-drop")


                class Cpu(Entity):
                    """
                    Resource specific
                    
                    .. attribute:: indexes
                    
                    	Data for software resource
                    	**type**\:   :py:class:`Indexes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper.HardwareModule.Nodes.Node.Np.Cpu.Indexes>`
                    
                    

                    """

                    _prefix = 'prm-server-oper'
                    _revision = '2016-02-22'

                    def __init__(self):
                        super(HardwareModule.Nodes.Node.Np.Cpu, self).__init__()

                        self.yang_name = "cpu"
                        self.yang_parent_name = "np"

                        self.indexes = HardwareModule.Nodes.Node.Np.Cpu.Indexes()
                        self.indexes.parent = self
                        self._children_name_map["indexes"] = "indexes"
                        self._children_yang_names.add("indexes")


                    class Indexes(Entity):
                        """
                        Data for software resource
                        
                        .. attribute:: index
                        
                        	Queue Stats
                        	**type**\: list of    :py:class:`Index <ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper.HardwareModule.Nodes.Node.Np.Cpu.Indexes.Index>`
                        
                        

                        """

                        _prefix = 'prm-server-oper'
                        _revision = '2016-02-22'

                        def __init__(self):
                            super(HardwareModule.Nodes.Node.Np.Cpu.Indexes, self).__init__()

                            self.yang_name = "indexes"
                            self.yang_parent_name = "cpu"

                            self.index = YList(self)

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
                                        super(HardwareModule.Nodes.Node.Np.Cpu.Indexes, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(HardwareModule.Nodes.Node.Np.Cpu.Indexes, self).__setattr__(name, value)


                        class Index(Entity):
                            """
                            Queue Stats
                            
                            .. attribute:: index  <key>
                            
                            	Index value
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: accepted
                            
                            	Accepted
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: burst
                            
                            	Burst
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: cos_q
                            
                            	CosQ No
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: cos_q_name
                            
                            	CosQ Name
                            	**type**\:  str
                            
                            	**length:** 0..1024
                            
                            .. attribute:: dropped
                            
                            	Dropped
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: flow_rate
                            
                            	Flow Rate
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: rx_channel
                            
                            	Rx DMA Channel
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'prm-server-oper'
                            _revision = '2016-02-22'

                            def __init__(self):
                                super(HardwareModule.Nodes.Node.Np.Cpu.Indexes.Index, self).__init__()

                                self.yang_name = "index"
                                self.yang_parent_name = "indexes"

                                self.index = YLeaf(YType.int32, "index")

                                self.accepted = YLeaf(YType.uint64, "accepted")

                                self.burst = YLeaf(YType.uint32, "burst")

                                self.cos_q = YLeaf(YType.uint8, "cos-q")

                                self.cos_q_name = YLeaf(YType.str, "cos-q-name")

                                self.dropped = YLeaf(YType.uint64, "dropped")

                                self.flow_rate = YLeaf(YType.uint32, "flow-rate")

                                self.rx_channel = YLeaf(YType.uint32, "rx-channel")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("index",
                                                "accepted",
                                                "burst",
                                                "cos_q",
                                                "cos_q_name",
                                                "dropped",
                                                "flow_rate",
                                                "rx_channel") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(HardwareModule.Nodes.Node.Np.Cpu.Indexes.Index, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(HardwareModule.Nodes.Node.Np.Cpu.Indexes.Index, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.index.is_set or
                                    self.accepted.is_set or
                                    self.burst.is_set or
                                    self.cos_q.is_set or
                                    self.cos_q_name.is_set or
                                    self.dropped.is_set or
                                    self.flow_rate.is_set or
                                    self.rx_channel.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.index.yfilter != YFilter.not_set or
                                    self.accepted.yfilter != YFilter.not_set or
                                    self.burst.yfilter != YFilter.not_set or
                                    self.cos_q.yfilter != YFilter.not_set or
                                    self.cos_q_name.yfilter != YFilter.not_set or
                                    self.dropped.yfilter != YFilter.not_set or
                                    self.flow_rate.yfilter != YFilter.not_set or
                                    self.rx_channel.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "index" + "[index='" + self.index.get() + "']" + path_buffer

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
                                if (self.accepted.is_set or self.accepted.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.accepted.get_name_leafdata())
                                if (self.burst.is_set or self.burst.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.burst.get_name_leafdata())
                                if (self.cos_q.is_set or self.cos_q.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.cos_q.get_name_leafdata())
                                if (self.cos_q_name.is_set or self.cos_q_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.cos_q_name.get_name_leafdata())
                                if (self.dropped.is_set or self.dropped.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.dropped.get_name_leafdata())
                                if (self.flow_rate.is_set or self.flow_rate.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.flow_rate.get_name_leafdata())
                                if (self.rx_channel.is_set or self.rx_channel.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.rx_channel.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "index" or name == "accepted" or name == "burst" or name == "cos-q" or name == "cos-q-name" or name == "dropped" or name == "flow-rate" or name == "rx-channel"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "index"):
                                    self.index = value
                                    self.index.value_namespace = name_space
                                    self.index.value_namespace_prefix = name_space_prefix
                                if(value_path == "accepted"):
                                    self.accepted = value
                                    self.accepted.value_namespace = name_space
                                    self.accepted.value_namespace_prefix = name_space_prefix
                                if(value_path == "burst"):
                                    self.burst = value
                                    self.burst.value_namespace = name_space
                                    self.burst.value_namespace_prefix = name_space_prefix
                                if(value_path == "cos-q"):
                                    self.cos_q = value
                                    self.cos_q.value_namespace = name_space
                                    self.cos_q.value_namespace_prefix = name_space_prefix
                                if(value_path == "cos-q-name"):
                                    self.cos_q_name = value
                                    self.cos_q_name.value_namespace = name_space
                                    self.cos_q_name.value_namespace_prefix = name_space_prefix
                                if(value_path == "dropped"):
                                    self.dropped = value
                                    self.dropped.value_namespace = name_space
                                    self.dropped.value_namespace_prefix = name_space_prefix
                                if(value_path == "flow-rate"):
                                    self.flow_rate = value
                                    self.flow_rate.value_namespace = name_space
                                    self.flow_rate.value_namespace_prefix = name_space_prefix
                                if(value_path == "rx-channel"):
                                    self.rx_channel = value
                                    self.rx_channel.value_namespace = name_space
                                    self.rx_channel.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.index:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.index:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "indexes" + path_buffer

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

                            if (child_yang_name == "index"):
                                for c in self.index:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = HardwareModule.Nodes.Node.Np.Cpu.Indexes.Index()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.index.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "index"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (self.indexes is not None and self.indexes.has_data())

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.indexes is not None and self.indexes.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "cpu" + path_buffer

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

                        if (child_yang_name == "indexes"):
                            if (self.indexes is None):
                                self.indexes = HardwareModule.Nodes.Node.Np.Cpu.Indexes()
                                self.indexes.parent = self
                                self._children_name_map["indexes"] = "indexes"
                            return self.indexes

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "indexes"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class PlatformDrop(Entity):
                    """
                    Platform drops
                    
                    .. attribute:: idxes
                    
                    	Stats for Drop packets
                    	**type**\:   :py:class:`Idxes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper.HardwareModule.Nodes.Node.Np.PlatformDrop.Idxes>`
                    
                    .. attribute:: indxes
                    
                    	Captured Packets
                    	**type**\:   :py:class:`Indxes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper.HardwareModule.Nodes.Node.Np.PlatformDrop.Indxes>`
                    
                    

                    """

                    _prefix = 'prm-server-oper'
                    _revision = '2016-02-22'

                    def __init__(self):
                        super(HardwareModule.Nodes.Node.Np.PlatformDrop, self).__init__()

                        self.yang_name = "platform-drop"
                        self.yang_parent_name = "np"

                        self.idxes = HardwareModule.Nodes.Node.Np.PlatformDrop.Idxes()
                        self.idxes.parent = self
                        self._children_name_map["idxes"] = "idxes"
                        self._children_yang_names.add("idxes")

                        self.indxes = HardwareModule.Nodes.Node.Np.PlatformDrop.Indxes()
                        self.indxes.parent = self
                        self._children_name_map["indxes"] = "indxes"
                        self._children_yang_names.add("indxes")


                    class Indxes(Entity):
                        """
                        Captured Packets
                        
                        .. attribute:: indx
                        
                        	Captured packets
                        	**type**\: list of    :py:class:`Indx <ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper.HardwareModule.Nodes.Node.Np.PlatformDrop.Indxes.Indx>`
                        
                        

                        """

                        _prefix = 'prm-server-oper'
                        _revision = '2016-02-22'

                        def __init__(self):
                            super(HardwareModule.Nodes.Node.Np.PlatformDrop.Indxes, self).__init__()

                            self.yang_name = "indxes"
                            self.yang_parent_name = "platform-drop"

                            self.indx = YList(self)

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
                                        super(HardwareModule.Nodes.Node.Np.PlatformDrop.Indxes, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(HardwareModule.Nodes.Node.Np.PlatformDrop.Indxes, self).__setattr__(name, value)


                        class Indx(Entity):
                            """
                            Captured packets
                            
                            .. attribute:: index  <key>
                            
                            	Index value
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: buffer_len
                            
                            	Buffer Length
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: captured_pak
                            
                            	Captured Packet
                            	**type**\:  str
                            
                            	**length:** 0..1024
                            
                            .. attribute:: days
                            
                            	Days
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: day
                            
                            .. attribute:: hours
                            
                            	Hours
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: hour
                            
                            .. attribute:: ifhandle
                            
                            	If Handle
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mins
                            
                            	Minutes
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: minute
                            
                            .. attribute:: pkt_index
                            
                            	Packet Index
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: reason
                            
                            	Reason
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: reason_hi
                            
                            	Reason Hi
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: secs
                            
                            	Seconds
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: second
                            
                            .. attribute:: total_captured
                            
                            	Total packets Captured
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: years
                            
                            	Year
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'prm-server-oper'
                            _revision = '2016-02-22'

                            def __init__(self):
                                super(HardwareModule.Nodes.Node.Np.PlatformDrop.Indxes.Indx, self).__init__()

                                self.yang_name = "indx"
                                self.yang_parent_name = "indxes"

                                self.index = YLeaf(YType.int32, "index")

                                self.buffer_len = YLeaf(YType.uint32, "buffer-len")

                                self.captured_pak = YLeaf(YType.str, "captured-pak")

                                self.days = YLeaf(YType.uint64, "days")

                                self.hours = YLeaf(YType.uint64, "hours")

                                self.ifhandle = YLeaf(YType.uint32, "ifhandle")

                                self.mins = YLeaf(YType.uint64, "mins")

                                self.pkt_index = YLeaf(YType.uint8, "pkt-index")

                                self.reason = YLeaf(YType.uint32, "reason")

                                self.reason_hi = YLeaf(YType.uint32, "reason-hi")

                                self.secs = YLeaf(YType.uint64, "secs")

                                self.total_captured = YLeaf(YType.uint32, "total-captured")

                                self.years = YLeaf(YType.uint64, "years")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("index",
                                                "buffer_len",
                                                "captured_pak",
                                                "days",
                                                "hours",
                                                "ifhandle",
                                                "mins",
                                                "pkt_index",
                                                "reason",
                                                "reason_hi",
                                                "secs",
                                                "total_captured",
                                                "years") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(HardwareModule.Nodes.Node.Np.PlatformDrop.Indxes.Indx, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(HardwareModule.Nodes.Node.Np.PlatformDrop.Indxes.Indx, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.index.is_set or
                                    self.buffer_len.is_set or
                                    self.captured_pak.is_set or
                                    self.days.is_set or
                                    self.hours.is_set or
                                    self.ifhandle.is_set or
                                    self.mins.is_set or
                                    self.pkt_index.is_set or
                                    self.reason.is_set or
                                    self.reason_hi.is_set or
                                    self.secs.is_set or
                                    self.total_captured.is_set or
                                    self.years.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.index.yfilter != YFilter.not_set or
                                    self.buffer_len.yfilter != YFilter.not_set or
                                    self.captured_pak.yfilter != YFilter.not_set or
                                    self.days.yfilter != YFilter.not_set or
                                    self.hours.yfilter != YFilter.not_set or
                                    self.ifhandle.yfilter != YFilter.not_set or
                                    self.mins.yfilter != YFilter.not_set or
                                    self.pkt_index.yfilter != YFilter.not_set or
                                    self.reason.yfilter != YFilter.not_set or
                                    self.reason_hi.yfilter != YFilter.not_set or
                                    self.secs.yfilter != YFilter.not_set or
                                    self.total_captured.yfilter != YFilter.not_set or
                                    self.years.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "indx" + "[index='" + self.index.get() + "']" + path_buffer

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
                                if (self.buffer_len.is_set or self.buffer_len.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.buffer_len.get_name_leafdata())
                                if (self.captured_pak.is_set or self.captured_pak.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.captured_pak.get_name_leafdata())
                                if (self.days.is_set or self.days.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.days.get_name_leafdata())
                                if (self.hours.is_set or self.hours.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.hours.get_name_leafdata())
                                if (self.ifhandle.is_set or self.ifhandle.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ifhandle.get_name_leafdata())
                                if (self.mins.is_set or self.mins.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.mins.get_name_leafdata())
                                if (self.pkt_index.is_set or self.pkt_index.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pkt_index.get_name_leafdata())
                                if (self.reason.is_set or self.reason.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.reason.get_name_leafdata())
                                if (self.reason_hi.is_set or self.reason_hi.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.reason_hi.get_name_leafdata())
                                if (self.secs.is_set or self.secs.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.secs.get_name_leafdata())
                                if (self.total_captured.is_set or self.total_captured.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.total_captured.get_name_leafdata())
                                if (self.years.is_set or self.years.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.years.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "index" or name == "buffer-len" or name == "captured-pak" or name == "days" or name == "hours" or name == "ifhandle" or name == "mins" or name == "pkt-index" or name == "reason" or name == "reason-hi" or name == "secs" or name == "total-captured" or name == "years"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "index"):
                                    self.index = value
                                    self.index.value_namespace = name_space
                                    self.index.value_namespace_prefix = name_space_prefix
                                if(value_path == "buffer-len"):
                                    self.buffer_len = value
                                    self.buffer_len.value_namespace = name_space
                                    self.buffer_len.value_namespace_prefix = name_space_prefix
                                if(value_path == "captured-pak"):
                                    self.captured_pak = value
                                    self.captured_pak.value_namespace = name_space
                                    self.captured_pak.value_namespace_prefix = name_space_prefix
                                if(value_path == "days"):
                                    self.days = value
                                    self.days.value_namespace = name_space
                                    self.days.value_namespace_prefix = name_space_prefix
                                if(value_path == "hours"):
                                    self.hours = value
                                    self.hours.value_namespace = name_space
                                    self.hours.value_namespace_prefix = name_space_prefix
                                if(value_path == "ifhandle"):
                                    self.ifhandle = value
                                    self.ifhandle.value_namespace = name_space
                                    self.ifhandle.value_namespace_prefix = name_space_prefix
                                if(value_path == "mins"):
                                    self.mins = value
                                    self.mins.value_namespace = name_space
                                    self.mins.value_namespace_prefix = name_space_prefix
                                if(value_path == "pkt-index"):
                                    self.pkt_index = value
                                    self.pkt_index.value_namespace = name_space
                                    self.pkt_index.value_namespace_prefix = name_space_prefix
                                if(value_path == "reason"):
                                    self.reason = value
                                    self.reason.value_namespace = name_space
                                    self.reason.value_namespace_prefix = name_space_prefix
                                if(value_path == "reason-hi"):
                                    self.reason_hi = value
                                    self.reason_hi.value_namespace = name_space
                                    self.reason_hi.value_namespace_prefix = name_space_prefix
                                if(value_path == "secs"):
                                    self.secs = value
                                    self.secs.value_namespace = name_space
                                    self.secs.value_namespace_prefix = name_space_prefix
                                if(value_path == "total-captured"):
                                    self.total_captured = value
                                    self.total_captured.value_namespace = name_space
                                    self.total_captured.value_namespace_prefix = name_space_prefix
                                if(value_path == "years"):
                                    self.years = value
                                    self.years.value_namespace = name_space
                                    self.years.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.indx:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.indx:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "indxes" + path_buffer

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

                            if (child_yang_name == "indx"):
                                for c in self.indx:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = HardwareModule.Nodes.Node.Np.PlatformDrop.Indxes.Indx()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.indx.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "indx"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass


                    class Idxes(Entity):
                        """
                        Stats for Drop packets
                        
                        .. attribute:: idx
                        
                        	Drop Stats
                        	**type**\: list of    :py:class:`Idx <ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper.HardwareModule.Nodes.Node.Np.PlatformDrop.Idxes.Idx>`
                        
                        

                        """

                        _prefix = 'prm-server-oper'
                        _revision = '2016-02-22'

                        def __init__(self):
                            super(HardwareModule.Nodes.Node.Np.PlatformDrop.Idxes, self).__init__()

                            self.yang_name = "idxes"
                            self.yang_parent_name = "platform-drop"

                            self.idx = YList(self)

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
                                        super(HardwareModule.Nodes.Node.Np.PlatformDrop.Idxes, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(HardwareModule.Nodes.Node.Np.PlatformDrop.Idxes, self).__setattr__(name, value)


                        class Idx(Entity):
                            """
                            Drop Stats
                            
                            .. attribute:: index  <key>
                            
                            	Index value
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: counters
                            
                            	Counter
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: drop_reason
                            
                            	Drop Reason
                            	**type**\:  str
                            
                            	**length:** 0..1024
                            
                            

                            """

                            _prefix = 'prm-server-oper'
                            _revision = '2016-02-22'

                            def __init__(self):
                                super(HardwareModule.Nodes.Node.Np.PlatformDrop.Idxes.Idx, self).__init__()

                                self.yang_name = "idx"
                                self.yang_parent_name = "idxes"

                                self.index = YLeaf(YType.int32, "index")

                                self.counters = YLeaf(YType.uint32, "counters")

                                self.drop_reason = YLeaf(YType.str, "drop-reason")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("index",
                                                "counters",
                                                "drop_reason") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(HardwareModule.Nodes.Node.Np.PlatformDrop.Idxes.Idx, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(HardwareModule.Nodes.Node.Np.PlatformDrop.Idxes.Idx, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.index.is_set or
                                    self.counters.is_set or
                                    self.drop_reason.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.index.yfilter != YFilter.not_set or
                                    self.counters.yfilter != YFilter.not_set or
                                    self.drop_reason.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "idx" + "[index='" + self.index.get() + "']" + path_buffer

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
                                if (self.counters.is_set or self.counters.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.counters.get_name_leafdata())
                                if (self.drop_reason.is_set or self.drop_reason.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.drop_reason.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "index" or name == "counters" or name == "drop-reason"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "index"):
                                    self.index = value
                                    self.index.value_namespace = name_space
                                    self.index.value_namespace_prefix = name_space_prefix
                                if(value_path == "counters"):
                                    self.counters = value
                                    self.counters.value_namespace = name_space
                                    self.counters.value_namespace_prefix = name_space_prefix
                                if(value_path == "drop-reason"):
                                    self.drop_reason = value
                                    self.drop_reason.value_namespace = name_space
                                    self.drop_reason.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.idx:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.idx:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "idxes" + path_buffer

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

                            if (child_yang_name == "idx"):
                                for c in self.idx:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = HardwareModule.Nodes.Node.Np.PlatformDrop.Idxes.Idx()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.idx.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "idx"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (
                            (self.idxes is not None and self.idxes.has_data()) or
                            (self.indxes is not None and self.indxes.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.idxes is not None and self.idxes.has_operation()) or
                            (self.indxes is not None and self.indxes.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "platform-drop" + path_buffer

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

                        if (child_yang_name == "idxes"):
                            if (self.idxes is None):
                                self.idxes = HardwareModule.Nodes.Node.Np.PlatformDrop.Idxes()
                                self.idxes.parent = self
                                self._children_name_map["idxes"] = "idxes"
                            return self.idxes

                        if (child_yang_name == "indxes"):
                            if (self.indxes is None):
                                self.indxes = HardwareModule.Nodes.Node.Np.PlatformDrop.Indxes()
                                self.indxes.parent = self
                                self._children_name_map["indxes"] = "indxes"
                            return self.indxes

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "idxes" or name == "indxes"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        (self.cpu is not None and self.cpu.has_data()) or
                        (self.platform_drop is not None and self.platform_drop.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.cpu is not None and self.cpu.has_operation()) or
                        (self.platform_drop is not None and self.platform_drop.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "np" + path_buffer

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

                    if (child_yang_name == "cpu"):
                        if (self.cpu is None):
                            self.cpu = HardwareModule.Nodes.Node.Np.Cpu()
                            self.cpu.parent = self
                            self._children_name_map["cpu"] = "cpu"
                        return self.cpu

                    if (child_yang_name == "platform-drop"):
                        if (self.platform_drop is None):
                            self.platform_drop = HardwareModule.Nodes.Node.Np.PlatformDrop()
                            self.platform_drop.parent = self
                            self._children_name_map["platform_drop"] = "platform-drop"
                        return self.platform_drop

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "cpu" or name == "platform-drop"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.node_name.is_set or
                    (self.np is not None and self.np.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.node_name.yfilter != YFilter.not_set or
                    (self.np is not None and self.np.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "node" + "[node-name='" + self.node_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-prm-server-oper:hardware-module/nodes/%s" % self.get_segment_path()
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

                if (child_yang_name == "np"):
                    if (self.np is None):
                        self.np = HardwareModule.Nodes.Node.Np()
                        self.np.parent = self
                        self._children_name_map["np"] = "np"
                    return self.np

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "np" or name == "node-name"):
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
                path_buffer = "Cisco-IOS-XR-prm-server-oper:hardware-module/%s" % self.get_segment_path()
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
                c = HardwareModule.Nodes.Node()
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
        path_buffer = "Cisco-IOS-XR-prm-server-oper:hardware-module" + path_buffer

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
                self.nodes = HardwareModule.Nodes()
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
        self._top_entity = HardwareModule()
        return self._top_entity

class Prm(Entity):
    """
    prm
    
    .. attribute:: nodes
    
    	List of PRM Nodes
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper.Prm.Nodes>`
    
    

    """

    _prefix = 'prm-server-oper'
    _revision = '2016-02-22'

    def __init__(self):
        super(Prm, self).__init__()
        self._top_entity = None

        self.yang_name = "prm"
        self.yang_parent_name = "Cisco-IOS-XR-prm-server-oper"

        self.nodes = Prm.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")


    class Nodes(Entity):
        """
        List of PRM Nodes
        
        .. attribute:: node
        
        	Node Information
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper.Prm.Nodes.Node>`
        
        

        """

        _prefix = 'prm-server-oper'
        _revision = '2016-02-22'

        def __init__(self):
            super(Prm.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "prm"

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
                        super(Prm.Nodes, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Prm.Nodes, self).__setattr__(name, value)


        class Node(Entity):
            """
            Node Information
            
            .. attribute:: node_name  <key>
            
            	The node name
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: server
            
            	Server specific
            	**type**\:   :py:class:`Server <ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper.Prm.Nodes.Node.Server>`
            
            

            """

            _prefix = 'prm-server-oper'
            _revision = '2016-02-22'

            def __init__(self):
                super(Prm.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"

                self.node_name = YLeaf(YType.str, "node-name")

                self.server = Prm.Nodes.Node.Server()
                self.server.parent = self
                self._children_name_map["server"] = "server"
                self._children_yang_names.add("server")

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
                            super(Prm.Nodes.Node, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Prm.Nodes.Node, self).__setattr__(name, value)


            class Server(Entity):
                """
                Server specific
                
                .. attribute:: resource
                
                	Resource specific
                	**type**\:   :py:class:`Resource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper.Prm.Nodes.Node.Server.Resource>`
                
                

                """

                _prefix = 'prm-server-oper'
                _revision = '2016-02-22'

                def __init__(self):
                    super(Prm.Nodes.Node.Server, self).__init__()

                    self.yang_name = "server"
                    self.yang_parent_name = "node"

                    self.resource = Prm.Nodes.Node.Server.Resource()
                    self.resource.parent = self
                    self._children_name_map["resource"] = "resource"
                    self._children_yang_names.add("resource")


                class Resource(Entity):
                    """
                    Resource specific
                    
                    .. attribute:: indexes
                    
                    	Data for software resource
                    	**type**\:   :py:class:`Indexes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper.Prm.Nodes.Node.Server.Resource.Indexes>`
                    
                    

                    """

                    _prefix = 'prm-server-oper'
                    _revision = '2016-02-22'

                    def __init__(self):
                        super(Prm.Nodes.Node.Server.Resource, self).__init__()

                        self.yang_name = "resource"
                        self.yang_parent_name = "server"

                        self.indexes = Prm.Nodes.Node.Server.Resource.Indexes()
                        self.indexes.parent = self
                        self._children_name_map["indexes"] = "indexes"
                        self._children_yang_names.add("indexes")


                    class Indexes(Entity):
                        """
                        Data for software resource
                        
                        .. attribute:: index
                        
                        	Data for software resource
                        	**type**\: list of    :py:class:`Index <ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper.Prm.Nodes.Node.Server.Resource.Indexes.Index>`
                        
                        

                        """

                        _prefix = 'prm-server-oper'
                        _revision = '2016-02-22'

                        def __init__(self):
                            super(Prm.Nodes.Node.Server.Resource.Indexes, self).__init__()

                            self.yang_name = "indexes"
                            self.yang_parent_name = "resource"

                            self.index = YList(self)

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
                                        super(Prm.Nodes.Node.Server.Resource.Indexes, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Prm.Nodes.Node.Server.Resource.Indexes, self).__setattr__(name, value)


                        class Index(Entity):
                            """
                            Data for software resource
                            
                            .. attribute:: index  <key>
                            
                            	Index value
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: availability_status
                            
                            	Availability Status
                            	**type**\:  bool
                            
                            .. attribute:: first_available_index
                            
                            	Next Free Index
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: flags
                            
                            	Resource Flags
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: free_num
                            
                            	Free Resource Count
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: inconsistent
                            
                            	Inconsistice Flags
                            	**type**\:  bool
                            
                            .. attribute:: resource_name
                            
                            	Resource Name
                            	**type**\:  str
                            
                            	**length:** 0..1024
                            
                            .. attribute:: resource_type
                            
                            	Resource Type
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: start_index
                            
                            	Start Index
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: total_num
                            
                            	Total Resource Count
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'prm-server-oper'
                            _revision = '2016-02-22'

                            def __init__(self):
                                super(Prm.Nodes.Node.Server.Resource.Indexes.Index, self).__init__()

                                self.yang_name = "index"
                                self.yang_parent_name = "indexes"

                                self.index = YLeaf(YType.int32, "index")

                                self.availability_status = YLeaf(YType.boolean, "availability-status")

                                self.first_available_index = YLeaf(YType.uint32, "first-available-index")

                                self.flags = YLeaf(YType.uint8, "flags")

                                self.free_num = YLeaf(YType.uint32, "free-num")

                                self.inconsistent = YLeaf(YType.boolean, "inconsistent")

                                self.resource_name = YLeaf(YType.str, "resource-name")

                                self.resource_type = YLeaf(YType.uint32, "resource-type")

                                self.start_index = YLeaf(YType.uint32, "start-index")

                                self.total_num = YLeaf(YType.uint32, "total-num")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("index",
                                                "availability_status",
                                                "first_available_index",
                                                "flags",
                                                "free_num",
                                                "inconsistent",
                                                "resource_name",
                                                "resource_type",
                                                "start_index",
                                                "total_num") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Prm.Nodes.Node.Server.Resource.Indexes.Index, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Prm.Nodes.Node.Server.Resource.Indexes.Index, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.index.is_set or
                                    self.availability_status.is_set or
                                    self.first_available_index.is_set or
                                    self.flags.is_set or
                                    self.free_num.is_set or
                                    self.inconsistent.is_set or
                                    self.resource_name.is_set or
                                    self.resource_type.is_set or
                                    self.start_index.is_set or
                                    self.total_num.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.index.yfilter != YFilter.not_set or
                                    self.availability_status.yfilter != YFilter.not_set or
                                    self.first_available_index.yfilter != YFilter.not_set or
                                    self.flags.yfilter != YFilter.not_set or
                                    self.free_num.yfilter != YFilter.not_set or
                                    self.inconsistent.yfilter != YFilter.not_set or
                                    self.resource_name.yfilter != YFilter.not_set or
                                    self.resource_type.yfilter != YFilter.not_set or
                                    self.start_index.yfilter != YFilter.not_set or
                                    self.total_num.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "index" + "[index='" + self.index.get() + "']" + path_buffer

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
                                if (self.availability_status.is_set or self.availability_status.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.availability_status.get_name_leafdata())
                                if (self.first_available_index.is_set or self.first_available_index.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.first_available_index.get_name_leafdata())
                                if (self.flags.is_set or self.flags.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.flags.get_name_leafdata())
                                if (self.free_num.is_set or self.free_num.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.free_num.get_name_leafdata())
                                if (self.inconsistent.is_set or self.inconsistent.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.inconsistent.get_name_leafdata())
                                if (self.resource_name.is_set or self.resource_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.resource_name.get_name_leafdata())
                                if (self.resource_type.is_set or self.resource_type.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.resource_type.get_name_leafdata())
                                if (self.start_index.is_set or self.start_index.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.start_index.get_name_leafdata())
                                if (self.total_num.is_set or self.total_num.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.total_num.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "index" or name == "availability-status" or name == "first-available-index" or name == "flags" or name == "free-num" or name == "inconsistent" or name == "resource-name" or name == "resource-type" or name == "start-index" or name == "total-num"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "index"):
                                    self.index = value
                                    self.index.value_namespace = name_space
                                    self.index.value_namespace_prefix = name_space_prefix
                                if(value_path == "availability-status"):
                                    self.availability_status = value
                                    self.availability_status.value_namespace = name_space
                                    self.availability_status.value_namespace_prefix = name_space_prefix
                                if(value_path == "first-available-index"):
                                    self.first_available_index = value
                                    self.first_available_index.value_namespace = name_space
                                    self.first_available_index.value_namespace_prefix = name_space_prefix
                                if(value_path == "flags"):
                                    self.flags = value
                                    self.flags.value_namespace = name_space
                                    self.flags.value_namespace_prefix = name_space_prefix
                                if(value_path == "free-num"):
                                    self.free_num = value
                                    self.free_num.value_namespace = name_space
                                    self.free_num.value_namespace_prefix = name_space_prefix
                                if(value_path == "inconsistent"):
                                    self.inconsistent = value
                                    self.inconsistent.value_namespace = name_space
                                    self.inconsistent.value_namespace_prefix = name_space_prefix
                                if(value_path == "resource-name"):
                                    self.resource_name = value
                                    self.resource_name.value_namespace = name_space
                                    self.resource_name.value_namespace_prefix = name_space_prefix
                                if(value_path == "resource-type"):
                                    self.resource_type = value
                                    self.resource_type.value_namespace = name_space
                                    self.resource_type.value_namespace_prefix = name_space_prefix
                                if(value_path == "start-index"):
                                    self.start_index = value
                                    self.start_index.value_namespace = name_space
                                    self.start_index.value_namespace_prefix = name_space_prefix
                                if(value_path == "total-num"):
                                    self.total_num = value
                                    self.total_num.value_namespace = name_space
                                    self.total_num.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.index:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.index:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "indexes" + path_buffer

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

                            if (child_yang_name == "index"):
                                for c in self.index:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Prm.Nodes.Node.Server.Resource.Indexes.Index()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.index.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "index"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (self.indexes is not None and self.indexes.has_data())

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.indexes is not None and self.indexes.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "resource" + path_buffer

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

                        if (child_yang_name == "indexes"):
                            if (self.indexes is None):
                                self.indexes = Prm.Nodes.Node.Server.Resource.Indexes()
                                self.indexes.parent = self
                                self._children_name_map["indexes"] = "indexes"
                            return self.indexes

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "indexes"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (self.resource is not None and self.resource.has_data())

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.resource is not None and self.resource.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "server" + path_buffer

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

                    if (child_yang_name == "resource"):
                        if (self.resource is None):
                            self.resource = Prm.Nodes.Node.Server.Resource()
                            self.resource.parent = self
                            self._children_name_map["resource"] = "resource"
                        return self.resource

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "resource"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.node_name.is_set or
                    (self.server is not None and self.server.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.node_name.yfilter != YFilter.not_set or
                    (self.server is not None and self.server.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "node" + "[node-name='" + self.node_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-prm-server-oper:prm/nodes/%s" % self.get_segment_path()
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

                if (child_yang_name == "server"):
                    if (self.server is None):
                        self.server = Prm.Nodes.Node.Server()
                        self.server.parent = self
                        self._children_name_map["server"] = "server"
                    return self.server

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "server" or name == "node-name"):
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
                path_buffer = "Cisco-IOS-XR-prm-server-oper:prm/%s" % self.get_segment_path()
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
                c = Prm.Nodes.Node()
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
        path_buffer = "Cisco-IOS-XR-prm-server-oper:prm" + path_buffer

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
                self.nodes = Prm.Nodes()
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
        self._top_entity = Prm()
        return self._top_entity

