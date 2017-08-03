""" Cisco_IOS_XR_asr9k_np_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR asr9k\-np package operational data.

This module contains definitions
for the following management objects\:
  hardware\-module\-np\: Hardware NP Counters

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class HardwareModuleNp(Entity):
    """
    Hardware NP Counters
    
    .. attribute:: nodes
    
    	Table of nodes
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes>`
    
    

    """

    _prefix = 'asr9k-np-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(HardwareModuleNp, self).__init__()
        self._top_entity = None

        self.yang_name = "hardware-module-np"
        self.yang_parent_name = "Cisco-IOS-XR-asr9k-np-oper"

        self.nodes = HardwareModuleNp.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")


    class Nodes(Entity):
        """
        Table of nodes
        
        .. attribute:: node
        
        	Number
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node>`
        
        

        """

        _prefix = 'asr9k-np-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(HardwareModuleNp.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "hardware-module-np"

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
                        super(HardwareModuleNp.Nodes, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(HardwareModuleNp.Nodes, self).__setattr__(name, value)


        class Node(Entity):
            """
            Number
            
            .. attribute:: node_name  <key>
            
            	node number
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: nps
            
            	List of all NP
            	**type**\:   :py:class:`Nps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps>`
            
            

            """

            _prefix = 'asr9k-np-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(HardwareModuleNp.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"

                self.node_name = YLeaf(YType.str, "node-name")

                self.nps = HardwareModuleNp.Nodes.Node.Nps()
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
                            super(HardwareModuleNp.Nodes.Node, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(HardwareModuleNp.Nodes.Node, self).__setattr__(name, value)


            class Nps(Entity):
                """
                List of all NP
                
                .. attribute:: np
                
                	np0 to np7
                	**type**\: list of    :py:class:`Np <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np>`
                
                

                """

                _prefix = 'asr9k-np-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(HardwareModuleNp.Nodes.Node.Nps, self).__init__()

                    self.yang_name = "nps"
                    self.yang_parent_name = "node"

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
                                super(HardwareModuleNp.Nodes.Node.Nps, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(HardwareModuleNp.Nodes.Node.Nps, self).__setattr__(name, value)


                class Np(Entity):
                    """
                    np0 to np7
                    
                    .. attribute:: np_name  <key>
                    
                    	NP name
                    	**type**\:  str
                    
                    	**pattern:** (np0)\|(np1)\|(np2)\|(np3)\|(np4)\|(np5)\|(np6)\|(np7)
                    
                    .. attribute:: chn_load
                    
                    	prm channel load info
                    	**type**\:   :py:class:`ChnLoad <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.ChnLoad>`
                    
                    .. attribute:: counters
                    
                    	prm counters info
                    	**type**\:   :py:class:`Counters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.Counters>`
                    
                    .. attribute:: fast_drop
                    
                    	prm fast drop counters info
                    	**type**\:   :py:class:`FastDrop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.FastDrop>`
                    
                    .. attribute:: tcam_summary
                    
                    	prm tcam summary info
                    	**type**\:   :py:class:`TcamSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary>`
                    
                    

                    """

                    _prefix = 'asr9k-np-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(HardwareModuleNp.Nodes.Node.Nps.Np, self).__init__()

                        self.yang_name = "np"
                        self.yang_parent_name = "nps"

                        self.np_name = YLeaf(YType.str, "np-name")

                        self.chn_load = HardwareModuleNp.Nodes.Node.Nps.Np.ChnLoad()
                        self.chn_load.parent = self
                        self._children_name_map["chn_load"] = "chn-load"
                        self._children_yang_names.add("chn-load")

                        self.counters = HardwareModuleNp.Nodes.Node.Nps.Np.Counters()
                        self.counters.parent = self
                        self._children_name_map["counters"] = "counters"
                        self._children_yang_names.add("counters")

                        self.fast_drop = HardwareModuleNp.Nodes.Node.Nps.Np.FastDrop()
                        self.fast_drop.parent = self
                        self._children_name_map["fast_drop"] = "fast-drop"
                        self._children_yang_names.add("fast-drop")

                        self.tcam_summary = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary()
                        self.tcam_summary.parent = self
                        self._children_name_map["tcam_summary"] = "tcam-summary"
                        self._children_yang_names.add("tcam-summary")

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
                                    super(HardwareModuleNp.Nodes.Node.Nps.Np, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(HardwareModuleNp.Nodes.Node.Nps.Np, self).__setattr__(name, value)


                    class ChnLoad(Entity):
                        """
                        prm channel load info
                        
                        .. attribute:: np_chn_load
                        
                        	Array of NP Channel load counters
                        	**type**\: list of    :py:class:`NpChnLoad <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.ChnLoad.NpChnLoad>`
                        
                        

                        """

                        _prefix = 'asr9k-np-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(HardwareModuleNp.Nodes.Node.Nps.Np.ChnLoad, self).__init__()

                            self.yang_name = "chn-load"
                            self.yang_parent_name = "np"

                            self.np_chn_load = YList(self)

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
                                        super(HardwareModuleNp.Nodes.Node.Nps.Np.ChnLoad, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(HardwareModuleNp.Nodes.Node.Nps.Np.ChnLoad, self).__setattr__(name, value)


                        class NpChnLoad(Entity):
                            """
                            Array of NP Channel load counters
                            
                            .. attribute:: avg_guar_rfd_usage
                            
                            	Average of garanteed RFD usage
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: avg_rfd_usage
                            
                            	Average RFD Usage
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: flow_ctr_counter
                            
                            	Flow control counters
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: interface_name
                            
                            	Inerface Name
                            	**type**\:  str
                            
                            .. attribute:: peak_guar_rfd_usage
                            
                            	Peak of garanteed RFD usage
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: peak_rfd_usage
                            
                            	Peak RFD Usage
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'asr9k-np-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(HardwareModuleNp.Nodes.Node.Nps.Np.ChnLoad.NpChnLoad, self).__init__()

                                self.yang_name = "np-chn-load"
                                self.yang_parent_name = "chn-load"

                                self.avg_guar_rfd_usage = YLeaf(YType.uint32, "avg-guar-rfd-usage")

                                self.avg_rfd_usage = YLeaf(YType.uint32, "avg-rfd-usage")

                                self.flow_ctr_counter = YLeaf(YType.uint32, "flow-ctr-counter")

                                self.interface_name = YLeaf(YType.str, "interface-name")

                                self.peak_guar_rfd_usage = YLeaf(YType.uint32, "peak-guar-rfd-usage")

                                self.peak_rfd_usage = YLeaf(YType.uint32, "peak-rfd-usage")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("avg_guar_rfd_usage",
                                                "avg_rfd_usage",
                                                "flow_ctr_counter",
                                                "interface_name",
                                                "peak_guar_rfd_usage",
                                                "peak_rfd_usage") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(HardwareModuleNp.Nodes.Node.Nps.Np.ChnLoad.NpChnLoad, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(HardwareModuleNp.Nodes.Node.Nps.Np.ChnLoad.NpChnLoad, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.avg_guar_rfd_usage.is_set or
                                    self.avg_rfd_usage.is_set or
                                    self.flow_ctr_counter.is_set or
                                    self.interface_name.is_set or
                                    self.peak_guar_rfd_usage.is_set or
                                    self.peak_rfd_usage.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.avg_guar_rfd_usage.yfilter != YFilter.not_set or
                                    self.avg_rfd_usage.yfilter != YFilter.not_set or
                                    self.flow_ctr_counter.yfilter != YFilter.not_set or
                                    self.interface_name.yfilter != YFilter.not_set or
                                    self.peak_guar_rfd_usage.yfilter != YFilter.not_set or
                                    self.peak_rfd_usage.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "np-chn-load" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.avg_guar_rfd_usage.is_set or self.avg_guar_rfd_usage.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.avg_guar_rfd_usage.get_name_leafdata())
                                if (self.avg_rfd_usage.is_set or self.avg_rfd_usage.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.avg_rfd_usage.get_name_leafdata())
                                if (self.flow_ctr_counter.is_set or self.flow_ctr_counter.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.flow_ctr_counter.get_name_leafdata())
                                if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.interface_name.get_name_leafdata())
                                if (self.peak_guar_rfd_usage.is_set or self.peak_guar_rfd_usage.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.peak_guar_rfd_usage.get_name_leafdata())
                                if (self.peak_rfd_usage.is_set or self.peak_rfd_usage.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.peak_rfd_usage.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "avg-guar-rfd-usage" or name == "avg-rfd-usage" or name == "flow-ctr-counter" or name == "interface-name" or name == "peak-guar-rfd-usage" or name == "peak-rfd-usage"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "avg-guar-rfd-usage"):
                                    self.avg_guar_rfd_usage = value
                                    self.avg_guar_rfd_usage.value_namespace = name_space
                                    self.avg_guar_rfd_usage.value_namespace_prefix = name_space_prefix
                                if(value_path == "avg-rfd-usage"):
                                    self.avg_rfd_usage = value
                                    self.avg_rfd_usage.value_namespace = name_space
                                    self.avg_rfd_usage.value_namespace_prefix = name_space_prefix
                                if(value_path == "flow-ctr-counter"):
                                    self.flow_ctr_counter = value
                                    self.flow_ctr_counter.value_namespace = name_space
                                    self.flow_ctr_counter.value_namespace_prefix = name_space_prefix
                                if(value_path == "interface-name"):
                                    self.interface_name = value
                                    self.interface_name.value_namespace = name_space
                                    self.interface_name.value_namespace_prefix = name_space_prefix
                                if(value_path == "peak-guar-rfd-usage"):
                                    self.peak_guar_rfd_usage = value
                                    self.peak_guar_rfd_usage.value_namespace = name_space
                                    self.peak_guar_rfd_usage.value_namespace_prefix = name_space_prefix
                                if(value_path == "peak-rfd-usage"):
                                    self.peak_rfd_usage = value
                                    self.peak_rfd_usage.value_namespace = name_space
                                    self.peak_rfd_usage.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.np_chn_load:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.np_chn_load:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "chn-load" + path_buffer

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

                            if (child_yang_name == "np-chn-load"):
                                for c in self.np_chn_load:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = HardwareModuleNp.Nodes.Node.Nps.Np.ChnLoad.NpChnLoad()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.np_chn_load.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "np-chn-load"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass


                    class TcamSummary(Entity):
                        """
                        prm tcam summary info
                        
                        .. attribute:: internal_tcam_info
                        
                        	Internal tcam summary info
                        	**type**\:   :py:class:`InternalTcamInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo>`
                        
                        .. attribute:: tcam_info
                        
                        	External tcam summary info
                        	**type**\:   :py:class:`TcamInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo>`
                        
                        

                        """

                        _prefix = 'asr9k-np-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary, self).__init__()

                            self.yang_name = "tcam-summary"
                            self.yang_parent_name = "np"

                            self.internal_tcam_info = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo()
                            self.internal_tcam_info.parent = self
                            self._children_name_map["internal_tcam_info"] = "internal-tcam-info"
                            self._children_yang_names.add("internal-tcam-info")

                            self.tcam_info = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo()
                            self.tcam_info.parent = self
                            self._children_name_map["tcam_info"] = "tcam-info"
                            self._children_yang_names.add("tcam-info")


                        class InternalTcamInfo(Entity):
                            """
                            Internal tcam summary info
                            
                            .. attribute:: tcam_lt_l2
                            
                            	Array of TCAM LT L2 partition summaries
                            	**type**\: list of    :py:class:`TcamLtL2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtL2>`
                            
                            .. attribute:: tcam_lt_ods2
                            
                            	TCAM LT ODS 2 summary
                            	**type**\:   :py:class:`TcamLtOds2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2>`
                            
                            .. attribute:: tcam_lt_ods8
                            
                            	TCAM LT\_ODS 8 summary
                            	**type**\:   :py:class:`TcamLtOds8 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8>`
                            
                            

                            """

                            _prefix = 'asr9k-np-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo, self).__init__()

                                self.yang_name = "internal-tcam-info"
                                self.yang_parent_name = "tcam-summary"

                                self.tcam_lt_ods2 = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2()
                                self.tcam_lt_ods2.parent = self
                                self._children_name_map["tcam_lt_ods2"] = "tcam-lt-ods2"
                                self._children_yang_names.add("tcam-lt-ods2")

                                self.tcam_lt_ods8 = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8()
                                self.tcam_lt_ods8.parent = self
                                self._children_name_map["tcam_lt_ods8"] = "tcam-lt-ods8"
                                self._children_yang_names.add("tcam-lt-ods8")

                                self.tcam_lt_l2 = YList(self)

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
                                            super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo, self).__setattr__(name, value)


                            class TcamLtOds2(Entity):
                                """
                                TCAM LT ODS 2 summary
                                
                                .. attribute:: app_id_acl
                                
                                	app acl entry
                                	**type**\:   :py:class:`AppIdAcl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdAcl>`
                                
                                .. attribute:: app_id_afmon
                                
                                	app afmon entry
                                	**type**\:   :py:class:`AppIdAfmon <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdAfmon>`
                                
                                .. attribute:: app_id_ifib
                                
                                	app IFIB entry
                                	**type**\:   :py:class:`AppIdIfib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdIfib>`
                                
                                .. attribute:: app_id_li
                                
                                	app LI entry
                                	**type**\:   :py:class:`AppIdLi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdLi>`
                                
                                .. attribute:: app_id_pbr
                                
                                	app PBR entry
                                	**type**\:   :py:class:`AppIdPbr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdPbr>`
                                
                                .. attribute:: app_id_qos
                                
                                	app qos entry
                                	**type**\:   :py:class:`AppIdQos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdQos>`
                                
                                .. attribute:: application_edpl_entry
                                
                                	app EDPL entry
                                	**type**\:   :py:class:`ApplicationEdplEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.ApplicationEdplEntry>`
                                
                                .. attribute:: free_entries
                                
                                	free entries
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: max_entries
                                
                                	Max entries
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'asr9k-np-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2, self).__init__()

                                    self.yang_name = "tcam-lt-ods2"
                                    self.yang_parent_name = "internal-tcam-info"

                                    self.free_entries = YLeaf(YType.uint32, "free-entries")

                                    self.max_entries = YLeaf(YType.uint32, "max-entries")

                                    self.app_id_acl = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdAcl()
                                    self.app_id_acl.parent = self
                                    self._children_name_map["app_id_acl"] = "app-id-acl"
                                    self._children_yang_names.add("app-id-acl")

                                    self.app_id_afmon = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdAfmon()
                                    self.app_id_afmon.parent = self
                                    self._children_name_map["app_id_afmon"] = "app-id-afmon"
                                    self._children_yang_names.add("app-id-afmon")

                                    self.app_id_ifib = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdIfib()
                                    self.app_id_ifib.parent = self
                                    self._children_name_map["app_id_ifib"] = "app-id-ifib"
                                    self._children_yang_names.add("app-id-ifib")

                                    self.app_id_li = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdLi()
                                    self.app_id_li.parent = self
                                    self._children_name_map["app_id_li"] = "app-id-li"
                                    self._children_yang_names.add("app-id-li")

                                    self.app_id_pbr = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdPbr()
                                    self.app_id_pbr.parent = self
                                    self._children_name_map["app_id_pbr"] = "app-id-pbr"
                                    self._children_yang_names.add("app-id-pbr")

                                    self.app_id_qos = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdQos()
                                    self.app_id_qos.parent = self
                                    self._children_name_map["app_id_qos"] = "app-id-qos"
                                    self._children_yang_names.add("app-id-qos")

                                    self.application_edpl_entry = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.ApplicationEdplEntry()
                                    self.application_edpl_entry.parent = self
                                    self._children_name_map["application_edpl_entry"] = "application-edpl-entry"
                                    self._children_yang_names.add("application-edpl-entry")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("free_entries",
                                                    "max_entries") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2, self).__setattr__(name, value)


                                class AppIdIfib(Entity):
                                    """
                                    app IFIB entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_used_entries
                                    
                                    	number of used vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdIfib, self).__init__()

                                        self.yang_name = "app-id-ifib"
                                        self.yang_parent_name = "tcam-lt-ods2"

                                        self.num_vmr_ids = YLeaf(YType.uint32, "num-vmr-ids")

                                        self.total_allocated_entries = YLeaf(YType.uint32, "total-allocated-entries")

                                        self.total_used_entries = YLeaf(YType.uint32, "total-used-entries")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("num_vmr_ids",
                                                        "total_allocated_entries",
                                                        "total_used_entries") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdIfib, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdIfib, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.num_vmr_ids.is_set or
                                            self.total_allocated_entries.is_set or
                                            self.total_used_entries.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.num_vmr_ids.yfilter != YFilter.not_set or
                                            self.total_allocated_entries.yfilter != YFilter.not_set or
                                            self.total_used_entries.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "app-id-ifib" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.num_vmr_ids.is_set or self.num_vmr_ids.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.num_vmr_ids.get_name_leafdata())
                                        if (self.total_allocated_entries.is_set or self.total_allocated_entries.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.total_allocated_entries.get_name_leafdata())
                                        if (self.total_used_entries.is_set or self.total_used_entries.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.total_used_entries.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "num-vmr-ids" or name == "total-allocated-entries" or name == "total-used-entries"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "num-vmr-ids"):
                                            self.num_vmr_ids = value
                                            self.num_vmr_ids.value_namespace = name_space
                                            self.num_vmr_ids.value_namespace_prefix = name_space_prefix
                                        if(value_path == "total-allocated-entries"):
                                            self.total_allocated_entries = value
                                            self.total_allocated_entries.value_namespace = name_space
                                            self.total_allocated_entries.value_namespace_prefix = name_space_prefix
                                        if(value_path == "total-used-entries"):
                                            self.total_used_entries = value
                                            self.total_used_entries.value_namespace = name_space
                                            self.total_used_entries.value_namespace_prefix = name_space_prefix


                                class AppIdQos(Entity):
                                    """
                                    app qos entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_used_entries
                                    
                                    	number of used vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdQos, self).__init__()

                                        self.yang_name = "app-id-qos"
                                        self.yang_parent_name = "tcam-lt-ods2"

                                        self.num_vmr_ids = YLeaf(YType.uint32, "num-vmr-ids")

                                        self.total_allocated_entries = YLeaf(YType.uint32, "total-allocated-entries")

                                        self.total_used_entries = YLeaf(YType.uint32, "total-used-entries")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("num_vmr_ids",
                                                        "total_allocated_entries",
                                                        "total_used_entries") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdQos, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdQos, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.num_vmr_ids.is_set or
                                            self.total_allocated_entries.is_set or
                                            self.total_used_entries.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.num_vmr_ids.yfilter != YFilter.not_set or
                                            self.total_allocated_entries.yfilter != YFilter.not_set or
                                            self.total_used_entries.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "app-id-qos" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.num_vmr_ids.is_set or self.num_vmr_ids.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.num_vmr_ids.get_name_leafdata())
                                        if (self.total_allocated_entries.is_set or self.total_allocated_entries.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.total_allocated_entries.get_name_leafdata())
                                        if (self.total_used_entries.is_set or self.total_used_entries.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.total_used_entries.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "num-vmr-ids" or name == "total-allocated-entries" or name == "total-used-entries"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "num-vmr-ids"):
                                            self.num_vmr_ids = value
                                            self.num_vmr_ids.value_namespace = name_space
                                            self.num_vmr_ids.value_namespace_prefix = name_space_prefix
                                        if(value_path == "total-allocated-entries"):
                                            self.total_allocated_entries = value
                                            self.total_allocated_entries.value_namespace = name_space
                                            self.total_allocated_entries.value_namespace_prefix = name_space_prefix
                                        if(value_path == "total-used-entries"):
                                            self.total_used_entries = value
                                            self.total_used_entries.value_namespace = name_space
                                            self.total_used_entries.value_namespace_prefix = name_space_prefix


                                class AppIdAcl(Entity):
                                    """
                                    app acl entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_used_entries
                                    
                                    	number of used vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdAcl, self).__init__()

                                        self.yang_name = "app-id-acl"
                                        self.yang_parent_name = "tcam-lt-ods2"

                                        self.num_vmr_ids = YLeaf(YType.uint32, "num-vmr-ids")

                                        self.total_allocated_entries = YLeaf(YType.uint32, "total-allocated-entries")

                                        self.total_used_entries = YLeaf(YType.uint32, "total-used-entries")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("num_vmr_ids",
                                                        "total_allocated_entries",
                                                        "total_used_entries") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdAcl, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdAcl, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.num_vmr_ids.is_set or
                                            self.total_allocated_entries.is_set or
                                            self.total_used_entries.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.num_vmr_ids.yfilter != YFilter.not_set or
                                            self.total_allocated_entries.yfilter != YFilter.not_set or
                                            self.total_used_entries.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "app-id-acl" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.num_vmr_ids.is_set or self.num_vmr_ids.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.num_vmr_ids.get_name_leafdata())
                                        if (self.total_allocated_entries.is_set or self.total_allocated_entries.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.total_allocated_entries.get_name_leafdata())
                                        if (self.total_used_entries.is_set or self.total_used_entries.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.total_used_entries.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "num-vmr-ids" or name == "total-allocated-entries" or name == "total-used-entries"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "num-vmr-ids"):
                                            self.num_vmr_ids = value
                                            self.num_vmr_ids.value_namespace = name_space
                                            self.num_vmr_ids.value_namespace_prefix = name_space_prefix
                                        if(value_path == "total-allocated-entries"):
                                            self.total_allocated_entries = value
                                            self.total_allocated_entries.value_namespace = name_space
                                            self.total_allocated_entries.value_namespace_prefix = name_space_prefix
                                        if(value_path == "total-used-entries"):
                                            self.total_used_entries = value
                                            self.total_used_entries.value_namespace = name_space
                                            self.total_used_entries.value_namespace_prefix = name_space_prefix


                                class AppIdAfmon(Entity):
                                    """
                                    app afmon entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_used_entries
                                    
                                    	number of used vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdAfmon, self).__init__()

                                        self.yang_name = "app-id-afmon"
                                        self.yang_parent_name = "tcam-lt-ods2"

                                        self.num_vmr_ids = YLeaf(YType.uint32, "num-vmr-ids")

                                        self.total_allocated_entries = YLeaf(YType.uint32, "total-allocated-entries")

                                        self.total_used_entries = YLeaf(YType.uint32, "total-used-entries")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("num_vmr_ids",
                                                        "total_allocated_entries",
                                                        "total_used_entries") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdAfmon, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdAfmon, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.num_vmr_ids.is_set or
                                            self.total_allocated_entries.is_set or
                                            self.total_used_entries.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.num_vmr_ids.yfilter != YFilter.not_set or
                                            self.total_allocated_entries.yfilter != YFilter.not_set or
                                            self.total_used_entries.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "app-id-afmon" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.num_vmr_ids.is_set or self.num_vmr_ids.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.num_vmr_ids.get_name_leafdata())
                                        if (self.total_allocated_entries.is_set or self.total_allocated_entries.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.total_allocated_entries.get_name_leafdata())
                                        if (self.total_used_entries.is_set or self.total_used_entries.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.total_used_entries.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "num-vmr-ids" or name == "total-allocated-entries" or name == "total-used-entries"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "num-vmr-ids"):
                                            self.num_vmr_ids = value
                                            self.num_vmr_ids.value_namespace = name_space
                                            self.num_vmr_ids.value_namespace_prefix = name_space_prefix
                                        if(value_path == "total-allocated-entries"):
                                            self.total_allocated_entries = value
                                            self.total_allocated_entries.value_namespace = name_space
                                            self.total_allocated_entries.value_namespace_prefix = name_space_prefix
                                        if(value_path == "total-used-entries"):
                                            self.total_used_entries = value
                                            self.total_used_entries.value_namespace = name_space
                                            self.total_used_entries.value_namespace_prefix = name_space_prefix


                                class AppIdLi(Entity):
                                    """
                                    app LI entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_used_entries
                                    
                                    	number of used vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdLi, self).__init__()

                                        self.yang_name = "app-id-li"
                                        self.yang_parent_name = "tcam-lt-ods2"

                                        self.num_vmr_ids = YLeaf(YType.uint32, "num-vmr-ids")

                                        self.total_allocated_entries = YLeaf(YType.uint32, "total-allocated-entries")

                                        self.total_used_entries = YLeaf(YType.uint32, "total-used-entries")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("num_vmr_ids",
                                                        "total_allocated_entries",
                                                        "total_used_entries") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdLi, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdLi, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.num_vmr_ids.is_set or
                                            self.total_allocated_entries.is_set or
                                            self.total_used_entries.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.num_vmr_ids.yfilter != YFilter.not_set or
                                            self.total_allocated_entries.yfilter != YFilter.not_set or
                                            self.total_used_entries.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "app-id-li" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.num_vmr_ids.is_set or self.num_vmr_ids.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.num_vmr_ids.get_name_leafdata())
                                        if (self.total_allocated_entries.is_set or self.total_allocated_entries.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.total_allocated_entries.get_name_leafdata())
                                        if (self.total_used_entries.is_set or self.total_used_entries.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.total_used_entries.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "num-vmr-ids" or name == "total-allocated-entries" or name == "total-used-entries"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "num-vmr-ids"):
                                            self.num_vmr_ids = value
                                            self.num_vmr_ids.value_namespace = name_space
                                            self.num_vmr_ids.value_namespace_prefix = name_space_prefix
                                        if(value_path == "total-allocated-entries"):
                                            self.total_allocated_entries = value
                                            self.total_allocated_entries.value_namespace = name_space
                                            self.total_allocated_entries.value_namespace_prefix = name_space_prefix
                                        if(value_path == "total-used-entries"):
                                            self.total_used_entries = value
                                            self.total_used_entries.value_namespace = name_space
                                            self.total_used_entries.value_namespace_prefix = name_space_prefix


                                class AppIdPbr(Entity):
                                    """
                                    app PBR entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_used_entries
                                    
                                    	number of used vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdPbr, self).__init__()

                                        self.yang_name = "app-id-pbr"
                                        self.yang_parent_name = "tcam-lt-ods2"

                                        self.num_vmr_ids = YLeaf(YType.uint32, "num-vmr-ids")

                                        self.total_allocated_entries = YLeaf(YType.uint32, "total-allocated-entries")

                                        self.total_used_entries = YLeaf(YType.uint32, "total-used-entries")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("num_vmr_ids",
                                                        "total_allocated_entries",
                                                        "total_used_entries") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdPbr, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdPbr, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.num_vmr_ids.is_set or
                                            self.total_allocated_entries.is_set or
                                            self.total_used_entries.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.num_vmr_ids.yfilter != YFilter.not_set or
                                            self.total_allocated_entries.yfilter != YFilter.not_set or
                                            self.total_used_entries.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "app-id-pbr" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.num_vmr_ids.is_set or self.num_vmr_ids.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.num_vmr_ids.get_name_leafdata())
                                        if (self.total_allocated_entries.is_set or self.total_allocated_entries.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.total_allocated_entries.get_name_leafdata())
                                        if (self.total_used_entries.is_set or self.total_used_entries.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.total_used_entries.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "num-vmr-ids" or name == "total-allocated-entries" or name == "total-used-entries"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "num-vmr-ids"):
                                            self.num_vmr_ids = value
                                            self.num_vmr_ids.value_namespace = name_space
                                            self.num_vmr_ids.value_namespace_prefix = name_space_prefix
                                        if(value_path == "total-allocated-entries"):
                                            self.total_allocated_entries = value
                                            self.total_allocated_entries.value_namespace = name_space
                                            self.total_allocated_entries.value_namespace_prefix = name_space_prefix
                                        if(value_path == "total-used-entries"):
                                            self.total_used_entries = value
                                            self.total_used_entries.value_namespace = name_space
                                            self.total_used_entries.value_namespace_prefix = name_space_prefix


                                class ApplicationEdplEntry(Entity):
                                    """
                                    app EDPL entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_used_entries
                                    
                                    	number of used vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.ApplicationEdplEntry, self).__init__()

                                        self.yang_name = "application-edpl-entry"
                                        self.yang_parent_name = "tcam-lt-ods2"

                                        self.num_vmr_ids = YLeaf(YType.uint32, "num-vmr-ids")

                                        self.total_allocated_entries = YLeaf(YType.uint32, "total-allocated-entries")

                                        self.total_used_entries = YLeaf(YType.uint32, "total-used-entries")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("num_vmr_ids",
                                                        "total_allocated_entries",
                                                        "total_used_entries") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.ApplicationEdplEntry, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.ApplicationEdplEntry, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.num_vmr_ids.is_set or
                                            self.total_allocated_entries.is_set or
                                            self.total_used_entries.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.num_vmr_ids.yfilter != YFilter.not_set or
                                            self.total_allocated_entries.yfilter != YFilter.not_set or
                                            self.total_used_entries.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "application-edpl-entry" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.num_vmr_ids.is_set or self.num_vmr_ids.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.num_vmr_ids.get_name_leafdata())
                                        if (self.total_allocated_entries.is_set or self.total_allocated_entries.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.total_allocated_entries.get_name_leafdata())
                                        if (self.total_used_entries.is_set or self.total_used_entries.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.total_used_entries.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "num-vmr-ids" or name == "total-allocated-entries" or name == "total-used-entries"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "num-vmr-ids"):
                                            self.num_vmr_ids = value
                                            self.num_vmr_ids.value_namespace = name_space
                                            self.num_vmr_ids.value_namespace_prefix = name_space_prefix
                                        if(value_path == "total-allocated-entries"):
                                            self.total_allocated_entries = value
                                            self.total_allocated_entries.value_namespace = name_space
                                            self.total_allocated_entries.value_namespace_prefix = name_space_prefix
                                        if(value_path == "total-used-entries"):
                                            self.total_used_entries = value
                                            self.total_used_entries.value_namespace = name_space
                                            self.total_used_entries.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    return (
                                        self.free_entries.is_set or
                                        self.max_entries.is_set or
                                        (self.app_id_acl is not None and self.app_id_acl.has_data()) or
                                        (self.app_id_afmon is not None and self.app_id_afmon.has_data()) or
                                        (self.app_id_ifib is not None and self.app_id_ifib.has_data()) or
                                        (self.app_id_li is not None and self.app_id_li.has_data()) or
                                        (self.app_id_pbr is not None and self.app_id_pbr.has_data()) or
                                        (self.app_id_qos is not None and self.app_id_qos.has_data()) or
                                        (self.application_edpl_entry is not None and self.application_edpl_entry.has_data()))

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.free_entries.yfilter != YFilter.not_set or
                                        self.max_entries.yfilter != YFilter.not_set or
                                        (self.app_id_acl is not None and self.app_id_acl.has_operation()) or
                                        (self.app_id_afmon is not None and self.app_id_afmon.has_operation()) or
                                        (self.app_id_ifib is not None and self.app_id_ifib.has_operation()) or
                                        (self.app_id_li is not None and self.app_id_li.has_operation()) or
                                        (self.app_id_pbr is not None and self.app_id_pbr.has_operation()) or
                                        (self.app_id_qos is not None and self.app_id_qos.has_operation()) or
                                        (self.application_edpl_entry is not None and self.application_edpl_entry.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "tcam-lt-ods2" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.free_entries.is_set or self.free_entries.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.free_entries.get_name_leafdata())
                                    if (self.max_entries.is_set or self.max_entries.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.max_entries.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "app-id-acl"):
                                        if (self.app_id_acl is None):
                                            self.app_id_acl = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdAcl()
                                            self.app_id_acl.parent = self
                                            self._children_name_map["app_id_acl"] = "app-id-acl"
                                        return self.app_id_acl

                                    if (child_yang_name == "app-id-afmon"):
                                        if (self.app_id_afmon is None):
                                            self.app_id_afmon = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdAfmon()
                                            self.app_id_afmon.parent = self
                                            self._children_name_map["app_id_afmon"] = "app-id-afmon"
                                        return self.app_id_afmon

                                    if (child_yang_name == "app-id-ifib"):
                                        if (self.app_id_ifib is None):
                                            self.app_id_ifib = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdIfib()
                                            self.app_id_ifib.parent = self
                                            self._children_name_map["app_id_ifib"] = "app-id-ifib"
                                        return self.app_id_ifib

                                    if (child_yang_name == "app-id-li"):
                                        if (self.app_id_li is None):
                                            self.app_id_li = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdLi()
                                            self.app_id_li.parent = self
                                            self._children_name_map["app_id_li"] = "app-id-li"
                                        return self.app_id_li

                                    if (child_yang_name == "app-id-pbr"):
                                        if (self.app_id_pbr is None):
                                            self.app_id_pbr = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdPbr()
                                            self.app_id_pbr.parent = self
                                            self._children_name_map["app_id_pbr"] = "app-id-pbr"
                                        return self.app_id_pbr

                                    if (child_yang_name == "app-id-qos"):
                                        if (self.app_id_qos is None):
                                            self.app_id_qos = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdQos()
                                            self.app_id_qos.parent = self
                                            self._children_name_map["app_id_qos"] = "app-id-qos"
                                        return self.app_id_qos

                                    if (child_yang_name == "application-edpl-entry"):
                                        if (self.application_edpl_entry is None):
                                            self.application_edpl_entry = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.ApplicationEdplEntry()
                                            self.application_edpl_entry.parent = self
                                            self._children_name_map["application_edpl_entry"] = "application-edpl-entry"
                                        return self.application_edpl_entry

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "app-id-acl" or name == "app-id-afmon" or name == "app-id-ifib" or name == "app-id-li" or name == "app-id-pbr" or name == "app-id-qos" or name == "application-edpl-entry" or name == "free-entries" or name == "max-entries"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "free-entries"):
                                        self.free_entries = value
                                        self.free_entries.value_namespace = name_space
                                        self.free_entries.value_namespace_prefix = name_space_prefix
                                    if(value_path == "max-entries"):
                                        self.max_entries = value
                                        self.max_entries.value_namespace = name_space
                                        self.max_entries.value_namespace_prefix = name_space_prefix


                            class TcamLtOds8(Entity):
                                """
                                TCAM LT\_ODS 8 summary
                                
                                .. attribute:: app_id_acl
                                
                                	app acl entry
                                	**type**\:   :py:class:`AppIdAcl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdAcl>`
                                
                                .. attribute:: app_id_afmon
                                
                                	app afmon entry
                                	**type**\:   :py:class:`AppIdAfmon <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdAfmon>`
                                
                                .. attribute:: app_id_ifib
                                
                                	app IFIB entry
                                	**type**\:   :py:class:`AppIdIfib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdIfib>`
                                
                                .. attribute:: app_id_li
                                
                                	app LI entry
                                	**type**\:   :py:class:`AppIdLi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdLi>`
                                
                                .. attribute:: app_id_pbr
                                
                                	app PBR entry
                                	**type**\:   :py:class:`AppIdPbr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdPbr>`
                                
                                .. attribute:: app_id_qos
                                
                                	app qos entry
                                	**type**\:   :py:class:`AppIdQos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdQos>`
                                
                                .. attribute:: application_edpl_entry
                                
                                	app EDPL entry
                                	**type**\:   :py:class:`ApplicationEdplEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.ApplicationEdplEntry>`
                                
                                .. attribute:: free_entries
                                
                                	free entries
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: max_entries
                                
                                	Max entries
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'asr9k-np-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8, self).__init__()

                                    self.yang_name = "tcam-lt-ods8"
                                    self.yang_parent_name = "internal-tcam-info"

                                    self.free_entries = YLeaf(YType.uint32, "free-entries")

                                    self.max_entries = YLeaf(YType.uint32, "max-entries")

                                    self.app_id_acl = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdAcl()
                                    self.app_id_acl.parent = self
                                    self._children_name_map["app_id_acl"] = "app-id-acl"
                                    self._children_yang_names.add("app-id-acl")

                                    self.app_id_afmon = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdAfmon()
                                    self.app_id_afmon.parent = self
                                    self._children_name_map["app_id_afmon"] = "app-id-afmon"
                                    self._children_yang_names.add("app-id-afmon")

                                    self.app_id_ifib = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdIfib()
                                    self.app_id_ifib.parent = self
                                    self._children_name_map["app_id_ifib"] = "app-id-ifib"
                                    self._children_yang_names.add("app-id-ifib")

                                    self.app_id_li = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdLi()
                                    self.app_id_li.parent = self
                                    self._children_name_map["app_id_li"] = "app-id-li"
                                    self._children_yang_names.add("app-id-li")

                                    self.app_id_pbr = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdPbr()
                                    self.app_id_pbr.parent = self
                                    self._children_name_map["app_id_pbr"] = "app-id-pbr"
                                    self._children_yang_names.add("app-id-pbr")

                                    self.app_id_qos = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdQos()
                                    self.app_id_qos.parent = self
                                    self._children_name_map["app_id_qos"] = "app-id-qos"
                                    self._children_yang_names.add("app-id-qos")

                                    self.application_edpl_entry = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.ApplicationEdplEntry()
                                    self.application_edpl_entry.parent = self
                                    self._children_name_map["application_edpl_entry"] = "application-edpl-entry"
                                    self._children_yang_names.add("application-edpl-entry")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("free_entries",
                                                    "max_entries") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8, self).__setattr__(name, value)


                                class AppIdIfib(Entity):
                                    """
                                    app IFIB entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_used_entries
                                    
                                    	number of used vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdIfib, self).__init__()

                                        self.yang_name = "app-id-ifib"
                                        self.yang_parent_name = "tcam-lt-ods8"

                                        self.num_vmr_ids = YLeaf(YType.uint32, "num-vmr-ids")

                                        self.total_allocated_entries = YLeaf(YType.uint32, "total-allocated-entries")

                                        self.total_used_entries = YLeaf(YType.uint32, "total-used-entries")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("num_vmr_ids",
                                                        "total_allocated_entries",
                                                        "total_used_entries") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdIfib, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdIfib, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.num_vmr_ids.is_set or
                                            self.total_allocated_entries.is_set or
                                            self.total_used_entries.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.num_vmr_ids.yfilter != YFilter.not_set or
                                            self.total_allocated_entries.yfilter != YFilter.not_set or
                                            self.total_used_entries.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "app-id-ifib" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.num_vmr_ids.is_set or self.num_vmr_ids.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.num_vmr_ids.get_name_leafdata())
                                        if (self.total_allocated_entries.is_set or self.total_allocated_entries.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.total_allocated_entries.get_name_leafdata())
                                        if (self.total_used_entries.is_set or self.total_used_entries.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.total_used_entries.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "num-vmr-ids" or name == "total-allocated-entries" or name == "total-used-entries"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "num-vmr-ids"):
                                            self.num_vmr_ids = value
                                            self.num_vmr_ids.value_namespace = name_space
                                            self.num_vmr_ids.value_namespace_prefix = name_space_prefix
                                        if(value_path == "total-allocated-entries"):
                                            self.total_allocated_entries = value
                                            self.total_allocated_entries.value_namespace = name_space
                                            self.total_allocated_entries.value_namespace_prefix = name_space_prefix
                                        if(value_path == "total-used-entries"):
                                            self.total_used_entries = value
                                            self.total_used_entries.value_namespace = name_space
                                            self.total_used_entries.value_namespace_prefix = name_space_prefix


                                class AppIdQos(Entity):
                                    """
                                    app qos entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_used_entries
                                    
                                    	number of used vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdQos, self).__init__()

                                        self.yang_name = "app-id-qos"
                                        self.yang_parent_name = "tcam-lt-ods8"

                                        self.num_vmr_ids = YLeaf(YType.uint32, "num-vmr-ids")

                                        self.total_allocated_entries = YLeaf(YType.uint32, "total-allocated-entries")

                                        self.total_used_entries = YLeaf(YType.uint32, "total-used-entries")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("num_vmr_ids",
                                                        "total_allocated_entries",
                                                        "total_used_entries") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdQos, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdQos, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.num_vmr_ids.is_set or
                                            self.total_allocated_entries.is_set or
                                            self.total_used_entries.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.num_vmr_ids.yfilter != YFilter.not_set or
                                            self.total_allocated_entries.yfilter != YFilter.not_set or
                                            self.total_used_entries.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "app-id-qos" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.num_vmr_ids.is_set or self.num_vmr_ids.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.num_vmr_ids.get_name_leafdata())
                                        if (self.total_allocated_entries.is_set or self.total_allocated_entries.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.total_allocated_entries.get_name_leafdata())
                                        if (self.total_used_entries.is_set or self.total_used_entries.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.total_used_entries.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "num-vmr-ids" or name == "total-allocated-entries" or name == "total-used-entries"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "num-vmr-ids"):
                                            self.num_vmr_ids = value
                                            self.num_vmr_ids.value_namespace = name_space
                                            self.num_vmr_ids.value_namespace_prefix = name_space_prefix
                                        if(value_path == "total-allocated-entries"):
                                            self.total_allocated_entries = value
                                            self.total_allocated_entries.value_namespace = name_space
                                            self.total_allocated_entries.value_namespace_prefix = name_space_prefix
                                        if(value_path == "total-used-entries"):
                                            self.total_used_entries = value
                                            self.total_used_entries.value_namespace = name_space
                                            self.total_used_entries.value_namespace_prefix = name_space_prefix


                                class AppIdAcl(Entity):
                                    """
                                    app acl entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_used_entries
                                    
                                    	number of used vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdAcl, self).__init__()

                                        self.yang_name = "app-id-acl"
                                        self.yang_parent_name = "tcam-lt-ods8"

                                        self.num_vmr_ids = YLeaf(YType.uint32, "num-vmr-ids")

                                        self.total_allocated_entries = YLeaf(YType.uint32, "total-allocated-entries")

                                        self.total_used_entries = YLeaf(YType.uint32, "total-used-entries")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("num_vmr_ids",
                                                        "total_allocated_entries",
                                                        "total_used_entries") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdAcl, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdAcl, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.num_vmr_ids.is_set or
                                            self.total_allocated_entries.is_set or
                                            self.total_used_entries.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.num_vmr_ids.yfilter != YFilter.not_set or
                                            self.total_allocated_entries.yfilter != YFilter.not_set or
                                            self.total_used_entries.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "app-id-acl" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.num_vmr_ids.is_set or self.num_vmr_ids.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.num_vmr_ids.get_name_leafdata())
                                        if (self.total_allocated_entries.is_set or self.total_allocated_entries.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.total_allocated_entries.get_name_leafdata())
                                        if (self.total_used_entries.is_set or self.total_used_entries.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.total_used_entries.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "num-vmr-ids" or name == "total-allocated-entries" or name == "total-used-entries"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "num-vmr-ids"):
                                            self.num_vmr_ids = value
                                            self.num_vmr_ids.value_namespace = name_space
                                            self.num_vmr_ids.value_namespace_prefix = name_space_prefix
                                        if(value_path == "total-allocated-entries"):
                                            self.total_allocated_entries = value
                                            self.total_allocated_entries.value_namespace = name_space
                                            self.total_allocated_entries.value_namespace_prefix = name_space_prefix
                                        if(value_path == "total-used-entries"):
                                            self.total_used_entries = value
                                            self.total_used_entries.value_namespace = name_space
                                            self.total_used_entries.value_namespace_prefix = name_space_prefix


                                class AppIdAfmon(Entity):
                                    """
                                    app afmon entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_used_entries
                                    
                                    	number of used vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdAfmon, self).__init__()

                                        self.yang_name = "app-id-afmon"
                                        self.yang_parent_name = "tcam-lt-ods8"

                                        self.num_vmr_ids = YLeaf(YType.uint32, "num-vmr-ids")

                                        self.total_allocated_entries = YLeaf(YType.uint32, "total-allocated-entries")

                                        self.total_used_entries = YLeaf(YType.uint32, "total-used-entries")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("num_vmr_ids",
                                                        "total_allocated_entries",
                                                        "total_used_entries") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdAfmon, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdAfmon, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.num_vmr_ids.is_set or
                                            self.total_allocated_entries.is_set or
                                            self.total_used_entries.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.num_vmr_ids.yfilter != YFilter.not_set or
                                            self.total_allocated_entries.yfilter != YFilter.not_set or
                                            self.total_used_entries.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "app-id-afmon" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.num_vmr_ids.is_set or self.num_vmr_ids.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.num_vmr_ids.get_name_leafdata())
                                        if (self.total_allocated_entries.is_set or self.total_allocated_entries.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.total_allocated_entries.get_name_leafdata())
                                        if (self.total_used_entries.is_set or self.total_used_entries.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.total_used_entries.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "num-vmr-ids" or name == "total-allocated-entries" or name == "total-used-entries"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "num-vmr-ids"):
                                            self.num_vmr_ids = value
                                            self.num_vmr_ids.value_namespace = name_space
                                            self.num_vmr_ids.value_namespace_prefix = name_space_prefix
                                        if(value_path == "total-allocated-entries"):
                                            self.total_allocated_entries = value
                                            self.total_allocated_entries.value_namespace = name_space
                                            self.total_allocated_entries.value_namespace_prefix = name_space_prefix
                                        if(value_path == "total-used-entries"):
                                            self.total_used_entries = value
                                            self.total_used_entries.value_namespace = name_space
                                            self.total_used_entries.value_namespace_prefix = name_space_prefix


                                class AppIdLi(Entity):
                                    """
                                    app LI entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_used_entries
                                    
                                    	number of used vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdLi, self).__init__()

                                        self.yang_name = "app-id-li"
                                        self.yang_parent_name = "tcam-lt-ods8"

                                        self.num_vmr_ids = YLeaf(YType.uint32, "num-vmr-ids")

                                        self.total_allocated_entries = YLeaf(YType.uint32, "total-allocated-entries")

                                        self.total_used_entries = YLeaf(YType.uint32, "total-used-entries")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("num_vmr_ids",
                                                        "total_allocated_entries",
                                                        "total_used_entries") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdLi, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdLi, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.num_vmr_ids.is_set or
                                            self.total_allocated_entries.is_set or
                                            self.total_used_entries.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.num_vmr_ids.yfilter != YFilter.not_set or
                                            self.total_allocated_entries.yfilter != YFilter.not_set or
                                            self.total_used_entries.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "app-id-li" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.num_vmr_ids.is_set or self.num_vmr_ids.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.num_vmr_ids.get_name_leafdata())
                                        if (self.total_allocated_entries.is_set or self.total_allocated_entries.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.total_allocated_entries.get_name_leafdata())
                                        if (self.total_used_entries.is_set or self.total_used_entries.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.total_used_entries.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "num-vmr-ids" or name == "total-allocated-entries" or name == "total-used-entries"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "num-vmr-ids"):
                                            self.num_vmr_ids = value
                                            self.num_vmr_ids.value_namespace = name_space
                                            self.num_vmr_ids.value_namespace_prefix = name_space_prefix
                                        if(value_path == "total-allocated-entries"):
                                            self.total_allocated_entries = value
                                            self.total_allocated_entries.value_namespace = name_space
                                            self.total_allocated_entries.value_namespace_prefix = name_space_prefix
                                        if(value_path == "total-used-entries"):
                                            self.total_used_entries = value
                                            self.total_used_entries.value_namespace = name_space
                                            self.total_used_entries.value_namespace_prefix = name_space_prefix


                                class AppIdPbr(Entity):
                                    """
                                    app PBR entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_used_entries
                                    
                                    	number of used vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdPbr, self).__init__()

                                        self.yang_name = "app-id-pbr"
                                        self.yang_parent_name = "tcam-lt-ods8"

                                        self.num_vmr_ids = YLeaf(YType.uint32, "num-vmr-ids")

                                        self.total_allocated_entries = YLeaf(YType.uint32, "total-allocated-entries")

                                        self.total_used_entries = YLeaf(YType.uint32, "total-used-entries")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("num_vmr_ids",
                                                        "total_allocated_entries",
                                                        "total_used_entries") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdPbr, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdPbr, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.num_vmr_ids.is_set or
                                            self.total_allocated_entries.is_set or
                                            self.total_used_entries.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.num_vmr_ids.yfilter != YFilter.not_set or
                                            self.total_allocated_entries.yfilter != YFilter.not_set or
                                            self.total_used_entries.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "app-id-pbr" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.num_vmr_ids.is_set or self.num_vmr_ids.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.num_vmr_ids.get_name_leafdata())
                                        if (self.total_allocated_entries.is_set or self.total_allocated_entries.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.total_allocated_entries.get_name_leafdata())
                                        if (self.total_used_entries.is_set or self.total_used_entries.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.total_used_entries.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "num-vmr-ids" or name == "total-allocated-entries" or name == "total-used-entries"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "num-vmr-ids"):
                                            self.num_vmr_ids = value
                                            self.num_vmr_ids.value_namespace = name_space
                                            self.num_vmr_ids.value_namespace_prefix = name_space_prefix
                                        if(value_path == "total-allocated-entries"):
                                            self.total_allocated_entries = value
                                            self.total_allocated_entries.value_namespace = name_space
                                            self.total_allocated_entries.value_namespace_prefix = name_space_prefix
                                        if(value_path == "total-used-entries"):
                                            self.total_used_entries = value
                                            self.total_used_entries.value_namespace = name_space
                                            self.total_used_entries.value_namespace_prefix = name_space_prefix


                                class ApplicationEdplEntry(Entity):
                                    """
                                    app EDPL entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_used_entries
                                    
                                    	number of used vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.ApplicationEdplEntry, self).__init__()

                                        self.yang_name = "application-edpl-entry"
                                        self.yang_parent_name = "tcam-lt-ods8"

                                        self.num_vmr_ids = YLeaf(YType.uint32, "num-vmr-ids")

                                        self.total_allocated_entries = YLeaf(YType.uint32, "total-allocated-entries")

                                        self.total_used_entries = YLeaf(YType.uint32, "total-used-entries")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("num_vmr_ids",
                                                        "total_allocated_entries",
                                                        "total_used_entries") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.ApplicationEdplEntry, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.ApplicationEdplEntry, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.num_vmr_ids.is_set or
                                            self.total_allocated_entries.is_set or
                                            self.total_used_entries.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.num_vmr_ids.yfilter != YFilter.not_set or
                                            self.total_allocated_entries.yfilter != YFilter.not_set or
                                            self.total_used_entries.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "application-edpl-entry" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.num_vmr_ids.is_set or self.num_vmr_ids.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.num_vmr_ids.get_name_leafdata())
                                        if (self.total_allocated_entries.is_set or self.total_allocated_entries.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.total_allocated_entries.get_name_leafdata())
                                        if (self.total_used_entries.is_set or self.total_used_entries.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.total_used_entries.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "num-vmr-ids" or name == "total-allocated-entries" or name == "total-used-entries"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "num-vmr-ids"):
                                            self.num_vmr_ids = value
                                            self.num_vmr_ids.value_namespace = name_space
                                            self.num_vmr_ids.value_namespace_prefix = name_space_prefix
                                        if(value_path == "total-allocated-entries"):
                                            self.total_allocated_entries = value
                                            self.total_allocated_entries.value_namespace = name_space
                                            self.total_allocated_entries.value_namespace_prefix = name_space_prefix
                                        if(value_path == "total-used-entries"):
                                            self.total_used_entries = value
                                            self.total_used_entries.value_namespace = name_space
                                            self.total_used_entries.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    return (
                                        self.free_entries.is_set or
                                        self.max_entries.is_set or
                                        (self.app_id_acl is not None and self.app_id_acl.has_data()) or
                                        (self.app_id_afmon is not None and self.app_id_afmon.has_data()) or
                                        (self.app_id_ifib is not None and self.app_id_ifib.has_data()) or
                                        (self.app_id_li is not None and self.app_id_li.has_data()) or
                                        (self.app_id_pbr is not None and self.app_id_pbr.has_data()) or
                                        (self.app_id_qos is not None and self.app_id_qos.has_data()) or
                                        (self.application_edpl_entry is not None and self.application_edpl_entry.has_data()))

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.free_entries.yfilter != YFilter.not_set or
                                        self.max_entries.yfilter != YFilter.not_set or
                                        (self.app_id_acl is not None and self.app_id_acl.has_operation()) or
                                        (self.app_id_afmon is not None and self.app_id_afmon.has_operation()) or
                                        (self.app_id_ifib is not None and self.app_id_ifib.has_operation()) or
                                        (self.app_id_li is not None and self.app_id_li.has_operation()) or
                                        (self.app_id_pbr is not None and self.app_id_pbr.has_operation()) or
                                        (self.app_id_qos is not None and self.app_id_qos.has_operation()) or
                                        (self.application_edpl_entry is not None and self.application_edpl_entry.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "tcam-lt-ods8" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.free_entries.is_set or self.free_entries.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.free_entries.get_name_leafdata())
                                    if (self.max_entries.is_set or self.max_entries.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.max_entries.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "app-id-acl"):
                                        if (self.app_id_acl is None):
                                            self.app_id_acl = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdAcl()
                                            self.app_id_acl.parent = self
                                            self._children_name_map["app_id_acl"] = "app-id-acl"
                                        return self.app_id_acl

                                    if (child_yang_name == "app-id-afmon"):
                                        if (self.app_id_afmon is None):
                                            self.app_id_afmon = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdAfmon()
                                            self.app_id_afmon.parent = self
                                            self._children_name_map["app_id_afmon"] = "app-id-afmon"
                                        return self.app_id_afmon

                                    if (child_yang_name == "app-id-ifib"):
                                        if (self.app_id_ifib is None):
                                            self.app_id_ifib = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdIfib()
                                            self.app_id_ifib.parent = self
                                            self._children_name_map["app_id_ifib"] = "app-id-ifib"
                                        return self.app_id_ifib

                                    if (child_yang_name == "app-id-li"):
                                        if (self.app_id_li is None):
                                            self.app_id_li = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdLi()
                                            self.app_id_li.parent = self
                                            self._children_name_map["app_id_li"] = "app-id-li"
                                        return self.app_id_li

                                    if (child_yang_name == "app-id-pbr"):
                                        if (self.app_id_pbr is None):
                                            self.app_id_pbr = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdPbr()
                                            self.app_id_pbr.parent = self
                                            self._children_name_map["app_id_pbr"] = "app-id-pbr"
                                        return self.app_id_pbr

                                    if (child_yang_name == "app-id-qos"):
                                        if (self.app_id_qos is None):
                                            self.app_id_qos = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdQos()
                                            self.app_id_qos.parent = self
                                            self._children_name_map["app_id_qos"] = "app-id-qos"
                                        return self.app_id_qos

                                    if (child_yang_name == "application-edpl-entry"):
                                        if (self.application_edpl_entry is None):
                                            self.application_edpl_entry = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.ApplicationEdplEntry()
                                            self.application_edpl_entry.parent = self
                                            self._children_name_map["application_edpl_entry"] = "application-edpl-entry"
                                        return self.application_edpl_entry

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "app-id-acl" or name == "app-id-afmon" or name == "app-id-ifib" or name == "app-id-li" or name == "app-id-pbr" or name == "app-id-qos" or name == "application-edpl-entry" or name == "free-entries" or name == "max-entries"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "free-entries"):
                                        self.free_entries = value
                                        self.free_entries.value_namespace = name_space
                                        self.free_entries.value_namespace_prefix = name_space_prefix
                                    if(value_path == "max-entries"):
                                        self.max_entries = value
                                        self.max_entries.value_namespace = name_space
                                        self.max_entries.value_namespace_prefix = name_space_prefix


                            class TcamLtL2(Entity):
                                """
                                Array of TCAM LT L2 partition summaries
                                
                                .. attribute:: free_entries
                                
                                	Free Entries
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: partition_id
                                
                                	PartitionID
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: valid_entries
                                
                                	Valid Entries
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'asr9k-np-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtL2, self).__init__()

                                    self.yang_name = "tcam-lt-l2"
                                    self.yang_parent_name = "internal-tcam-info"

                                    self.free_entries = YLeaf(YType.uint32, "free-entries")

                                    self.partition_id = YLeaf(YType.uint32, "partition-id")

                                    self.valid_entries = YLeaf(YType.uint32, "valid-entries")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("free_entries",
                                                    "partition_id",
                                                    "valid_entries") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtL2, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtL2, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.free_entries.is_set or
                                        self.partition_id.is_set or
                                        self.valid_entries.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.free_entries.yfilter != YFilter.not_set or
                                        self.partition_id.yfilter != YFilter.not_set or
                                        self.valid_entries.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "tcam-lt-l2" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.free_entries.is_set or self.free_entries.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.free_entries.get_name_leafdata())
                                    if (self.partition_id.is_set or self.partition_id.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.partition_id.get_name_leafdata())
                                    if (self.valid_entries.is_set or self.valid_entries.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.valid_entries.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "free-entries" or name == "partition-id" or name == "valid-entries"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "free-entries"):
                                        self.free_entries = value
                                        self.free_entries.value_namespace = name_space
                                        self.free_entries.value_namespace_prefix = name_space_prefix
                                    if(value_path == "partition-id"):
                                        self.partition_id = value
                                        self.partition_id.value_namespace = name_space
                                        self.partition_id.value_namespace_prefix = name_space_prefix
                                    if(value_path == "valid-entries"):
                                        self.valid_entries = value
                                        self.valid_entries.value_namespace = name_space
                                        self.valid_entries.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                for c in self.tcam_lt_l2:
                                    if (c.has_data()):
                                        return True
                                return (
                                    (self.tcam_lt_ods2 is not None and self.tcam_lt_ods2.has_data()) or
                                    (self.tcam_lt_ods8 is not None and self.tcam_lt_ods8.has_data()))

                            def has_operation(self):
                                for c in self.tcam_lt_l2:
                                    if (c.has_operation()):
                                        return True
                                return (
                                    self.yfilter != YFilter.not_set or
                                    (self.tcam_lt_ods2 is not None and self.tcam_lt_ods2.has_operation()) or
                                    (self.tcam_lt_ods8 is not None and self.tcam_lt_ods8.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "internal-tcam-info" + path_buffer

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

                                if (child_yang_name == "tcam-lt-l2"):
                                    for c in self.tcam_lt_l2:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtL2()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.tcam_lt_l2.append(c)
                                    return c

                                if (child_yang_name == "tcam-lt-ods2"):
                                    if (self.tcam_lt_ods2 is None):
                                        self.tcam_lt_ods2 = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2()
                                        self.tcam_lt_ods2.parent = self
                                        self._children_name_map["tcam_lt_ods2"] = "tcam-lt-ods2"
                                    return self.tcam_lt_ods2

                                if (child_yang_name == "tcam-lt-ods8"):
                                    if (self.tcam_lt_ods8 is None):
                                        self.tcam_lt_ods8 = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8()
                                        self.tcam_lt_ods8.parent = self
                                        self._children_name_map["tcam_lt_ods8"] = "tcam-lt-ods8"
                                    return self.tcam_lt_ods8

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "tcam-lt-l2" or name == "tcam-lt-ods2" or name == "tcam-lt-ods8"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass


                        class TcamInfo(Entity):
                            """
                            External tcam summary info
                            
                            .. attribute:: tcam_lt_l2
                            
                            	Array of TCAM L2 partition summaries
                            	**type**\: list of    :py:class:`TcamLtL2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtL2>`
                            
                            .. attribute:: tcam_lt_ods2
                            
                            	TCAM ODS2 partition summary
                            	**type**\:   :py:class:`TcamLtOds2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2>`
                            
                            .. attribute:: tcam_lt_ods8
                            
                            	TCAM ODS8 partition summary
                            	**type**\:   :py:class:`TcamLtOds8 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8>`
                            
                            

                            """

                            _prefix = 'asr9k-np-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo, self).__init__()

                                self.yang_name = "tcam-info"
                                self.yang_parent_name = "tcam-summary"

                                self.tcam_lt_ods2 = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2()
                                self.tcam_lt_ods2.parent = self
                                self._children_name_map["tcam_lt_ods2"] = "tcam-lt-ods2"
                                self._children_yang_names.add("tcam-lt-ods2")

                                self.tcam_lt_ods8 = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8()
                                self.tcam_lt_ods8.parent = self
                                self._children_name_map["tcam_lt_ods8"] = "tcam-lt-ods8"
                                self._children_yang_names.add("tcam-lt-ods8")

                                self.tcam_lt_l2 = YList(self)

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
                                            super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo, self).__setattr__(name, value)


                            class TcamLtOds2(Entity):
                                """
                                TCAM ODS2 partition summary
                                
                                .. attribute:: acl_common
                                
                                	ACL common region
                                	**type**\:   :py:class:`AclCommon <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AclCommon>`
                                
                                .. attribute:: app_id_acl
                                
                                	app acl entry
                                	**type**\:   :py:class:`AppIdAcl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdAcl>`
                                
                                .. attribute:: app_id_afmon
                                
                                	app afmon entry
                                	**type**\:   :py:class:`AppIdAfmon <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdAfmon>`
                                
                                .. attribute:: app_id_edpl
                                
                                	app EDPL entry
                                	**type**\:   :py:class:`AppIdEdpl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdEdpl>`
                                
                                .. attribute:: app_id_ifib
                                
                                	app IFIB entry
                                	**type**\:   :py:class:`AppIdIfib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdIfib>`
                                
                                .. attribute:: app_id_li
                                
                                	app LI entry
                                	**type**\:   :py:class:`AppIdLi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdLi>`
                                
                                .. attribute:: app_id_pbr
                                
                                	app PBR entry
                                	**type**\:   :py:class:`AppIdPbr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdPbr>`
                                
                                .. attribute:: app_id_qos
                                
                                	app qos entry
                                	**type**\:   :py:class:`AppIdQos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdQos>`
                                
                                .. attribute:: free_entries
                                
                                	Free entries in the table
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: reserved_entries
                                
                                	The number of active vmr entries
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'asr9k-np-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2, self).__init__()

                                    self.yang_name = "tcam-lt-ods2"
                                    self.yang_parent_name = "tcam-info"

                                    self.free_entries = YLeaf(YType.uint32, "free-entries")

                                    self.reserved_entries = YLeaf(YType.uint32, "reserved-entries")

                                    self.acl_common = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AclCommon()
                                    self.acl_common.parent = self
                                    self._children_name_map["acl_common"] = "acl-common"
                                    self._children_yang_names.add("acl-common")

                                    self.app_id_acl = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdAcl()
                                    self.app_id_acl.parent = self
                                    self._children_name_map["app_id_acl"] = "app-id-acl"
                                    self._children_yang_names.add("app-id-acl")

                                    self.app_id_afmon = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdAfmon()
                                    self.app_id_afmon.parent = self
                                    self._children_name_map["app_id_afmon"] = "app-id-afmon"
                                    self._children_yang_names.add("app-id-afmon")

                                    self.app_id_edpl = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdEdpl()
                                    self.app_id_edpl.parent = self
                                    self._children_name_map["app_id_edpl"] = "app-id-edpl"
                                    self._children_yang_names.add("app-id-edpl")

                                    self.app_id_ifib = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdIfib()
                                    self.app_id_ifib.parent = self
                                    self._children_name_map["app_id_ifib"] = "app-id-ifib"
                                    self._children_yang_names.add("app-id-ifib")

                                    self.app_id_li = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdLi()
                                    self.app_id_li.parent = self
                                    self._children_name_map["app_id_li"] = "app-id-li"
                                    self._children_yang_names.add("app-id-li")

                                    self.app_id_pbr = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdPbr()
                                    self.app_id_pbr.parent = self
                                    self._children_name_map["app_id_pbr"] = "app-id-pbr"
                                    self._children_yang_names.add("app-id-pbr")

                                    self.app_id_qos = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdQos()
                                    self.app_id_qos.parent = self
                                    self._children_name_map["app_id_qos"] = "app-id-qos"
                                    self._children_yang_names.add("app-id-qos")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("free_entries",
                                                    "reserved_entries") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2, self).__setattr__(name, value)


                                class AclCommon(Entity):
                                    """
                                    ACL common region
                                    
                                    .. attribute:: allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: free_entries
                                    
                                    	Free entries in the table
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AclCommon, self).__init__()

                                        self.yang_name = "acl-common"
                                        self.yang_parent_name = "tcam-lt-ods2"

                                        self.allocated_entries = YLeaf(YType.uint32, "allocated-entries")

                                        self.free_entries = YLeaf(YType.uint32, "free-entries")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("allocated_entries",
                                                        "free_entries") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AclCommon, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AclCommon, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.allocated_entries.is_set or
                                            self.free_entries.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.allocated_entries.yfilter != YFilter.not_set or
                                            self.free_entries.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "acl-common" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.allocated_entries.is_set or self.allocated_entries.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.allocated_entries.get_name_leafdata())
                                        if (self.free_entries.is_set or self.free_entries.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.free_entries.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "allocated-entries" or name == "free-entries"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "allocated-entries"):
                                            self.allocated_entries = value
                                            self.allocated_entries.value_namespace = name_space
                                            self.allocated_entries.value_namespace_prefix = name_space_prefix
                                        if(value_path == "free-entries"):
                                            self.free_entries = value
                                            self.free_entries.value_namespace = name_space
                                            self.free_entries.value_namespace_prefix = name_space_prefix


                                class AppIdIfib(Entity):
                                    """
                                    app IFIB entry
                                    
                                    .. attribute:: num_active_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdIfib, self).__init__()

                                        self.yang_name = "app-id-ifib"
                                        self.yang_parent_name = "tcam-lt-ods2"

                                        self.num_active_entries = YLeaf(YType.uint32, "num-active-entries")

                                        self.num_allocated_entries = YLeaf(YType.uint32, "num-allocated-entries")

                                        self.num_vmr_ids = YLeaf(YType.uint32, "num-vmr-ids")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("num_active_entries",
                                                        "num_allocated_entries",
                                                        "num_vmr_ids") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdIfib, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdIfib, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.num_active_entries.is_set or
                                            self.num_allocated_entries.is_set or
                                            self.num_vmr_ids.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.num_active_entries.yfilter != YFilter.not_set or
                                            self.num_allocated_entries.yfilter != YFilter.not_set or
                                            self.num_vmr_ids.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "app-id-ifib" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.num_active_entries.is_set or self.num_active_entries.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.num_active_entries.get_name_leafdata())
                                        if (self.num_allocated_entries.is_set or self.num_allocated_entries.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.num_allocated_entries.get_name_leafdata())
                                        if (self.num_vmr_ids.is_set or self.num_vmr_ids.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.num_vmr_ids.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "num-active-entries" or name == "num-allocated-entries" or name == "num-vmr-ids"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "num-active-entries"):
                                            self.num_active_entries = value
                                            self.num_active_entries.value_namespace = name_space
                                            self.num_active_entries.value_namespace_prefix = name_space_prefix
                                        if(value_path == "num-allocated-entries"):
                                            self.num_allocated_entries = value
                                            self.num_allocated_entries.value_namespace = name_space
                                            self.num_allocated_entries.value_namespace_prefix = name_space_prefix
                                        if(value_path == "num-vmr-ids"):
                                            self.num_vmr_ids = value
                                            self.num_vmr_ids.value_namespace = name_space
                                            self.num_vmr_ids.value_namespace_prefix = name_space_prefix


                                class AppIdQos(Entity):
                                    """
                                    app qos entry
                                    
                                    .. attribute:: num_active_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdQos, self).__init__()

                                        self.yang_name = "app-id-qos"
                                        self.yang_parent_name = "tcam-lt-ods2"

                                        self.num_active_entries = YLeaf(YType.uint32, "num-active-entries")

                                        self.num_allocated_entries = YLeaf(YType.uint32, "num-allocated-entries")

                                        self.num_vmr_ids = YLeaf(YType.uint32, "num-vmr-ids")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("num_active_entries",
                                                        "num_allocated_entries",
                                                        "num_vmr_ids") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdQos, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdQos, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.num_active_entries.is_set or
                                            self.num_allocated_entries.is_set or
                                            self.num_vmr_ids.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.num_active_entries.yfilter != YFilter.not_set or
                                            self.num_allocated_entries.yfilter != YFilter.not_set or
                                            self.num_vmr_ids.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "app-id-qos" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.num_active_entries.is_set or self.num_active_entries.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.num_active_entries.get_name_leafdata())
                                        if (self.num_allocated_entries.is_set or self.num_allocated_entries.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.num_allocated_entries.get_name_leafdata())
                                        if (self.num_vmr_ids.is_set or self.num_vmr_ids.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.num_vmr_ids.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "num-active-entries" or name == "num-allocated-entries" or name == "num-vmr-ids"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "num-active-entries"):
                                            self.num_active_entries = value
                                            self.num_active_entries.value_namespace = name_space
                                            self.num_active_entries.value_namespace_prefix = name_space_prefix
                                        if(value_path == "num-allocated-entries"):
                                            self.num_allocated_entries = value
                                            self.num_allocated_entries.value_namespace = name_space
                                            self.num_allocated_entries.value_namespace_prefix = name_space_prefix
                                        if(value_path == "num-vmr-ids"):
                                            self.num_vmr_ids = value
                                            self.num_vmr_ids.value_namespace = name_space
                                            self.num_vmr_ids.value_namespace_prefix = name_space_prefix


                                class AppIdAcl(Entity):
                                    """
                                    app acl entry
                                    
                                    .. attribute:: num_active_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdAcl, self).__init__()

                                        self.yang_name = "app-id-acl"
                                        self.yang_parent_name = "tcam-lt-ods2"

                                        self.num_active_entries = YLeaf(YType.uint32, "num-active-entries")

                                        self.num_allocated_entries = YLeaf(YType.uint32, "num-allocated-entries")

                                        self.num_vmr_ids = YLeaf(YType.uint32, "num-vmr-ids")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("num_active_entries",
                                                        "num_allocated_entries",
                                                        "num_vmr_ids") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdAcl, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdAcl, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.num_active_entries.is_set or
                                            self.num_allocated_entries.is_set or
                                            self.num_vmr_ids.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.num_active_entries.yfilter != YFilter.not_set or
                                            self.num_allocated_entries.yfilter != YFilter.not_set or
                                            self.num_vmr_ids.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "app-id-acl" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.num_active_entries.is_set or self.num_active_entries.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.num_active_entries.get_name_leafdata())
                                        if (self.num_allocated_entries.is_set or self.num_allocated_entries.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.num_allocated_entries.get_name_leafdata())
                                        if (self.num_vmr_ids.is_set or self.num_vmr_ids.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.num_vmr_ids.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "num-active-entries" or name == "num-allocated-entries" or name == "num-vmr-ids"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "num-active-entries"):
                                            self.num_active_entries = value
                                            self.num_active_entries.value_namespace = name_space
                                            self.num_active_entries.value_namespace_prefix = name_space_prefix
                                        if(value_path == "num-allocated-entries"):
                                            self.num_allocated_entries = value
                                            self.num_allocated_entries.value_namespace = name_space
                                            self.num_allocated_entries.value_namespace_prefix = name_space_prefix
                                        if(value_path == "num-vmr-ids"):
                                            self.num_vmr_ids = value
                                            self.num_vmr_ids.value_namespace = name_space
                                            self.num_vmr_ids.value_namespace_prefix = name_space_prefix


                                class AppIdAfmon(Entity):
                                    """
                                    app afmon entry
                                    
                                    .. attribute:: num_active_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdAfmon, self).__init__()

                                        self.yang_name = "app-id-afmon"
                                        self.yang_parent_name = "tcam-lt-ods2"

                                        self.num_active_entries = YLeaf(YType.uint32, "num-active-entries")

                                        self.num_allocated_entries = YLeaf(YType.uint32, "num-allocated-entries")

                                        self.num_vmr_ids = YLeaf(YType.uint32, "num-vmr-ids")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("num_active_entries",
                                                        "num_allocated_entries",
                                                        "num_vmr_ids") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdAfmon, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdAfmon, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.num_active_entries.is_set or
                                            self.num_allocated_entries.is_set or
                                            self.num_vmr_ids.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.num_active_entries.yfilter != YFilter.not_set or
                                            self.num_allocated_entries.yfilter != YFilter.not_set or
                                            self.num_vmr_ids.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "app-id-afmon" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.num_active_entries.is_set or self.num_active_entries.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.num_active_entries.get_name_leafdata())
                                        if (self.num_allocated_entries.is_set or self.num_allocated_entries.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.num_allocated_entries.get_name_leafdata())
                                        if (self.num_vmr_ids.is_set or self.num_vmr_ids.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.num_vmr_ids.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "num-active-entries" or name == "num-allocated-entries" or name == "num-vmr-ids"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "num-active-entries"):
                                            self.num_active_entries = value
                                            self.num_active_entries.value_namespace = name_space
                                            self.num_active_entries.value_namespace_prefix = name_space_prefix
                                        if(value_path == "num-allocated-entries"):
                                            self.num_allocated_entries = value
                                            self.num_allocated_entries.value_namespace = name_space
                                            self.num_allocated_entries.value_namespace_prefix = name_space_prefix
                                        if(value_path == "num-vmr-ids"):
                                            self.num_vmr_ids = value
                                            self.num_vmr_ids.value_namespace = name_space
                                            self.num_vmr_ids.value_namespace_prefix = name_space_prefix


                                class AppIdLi(Entity):
                                    """
                                    app LI entry
                                    
                                    .. attribute:: num_active_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdLi, self).__init__()

                                        self.yang_name = "app-id-li"
                                        self.yang_parent_name = "tcam-lt-ods2"

                                        self.num_active_entries = YLeaf(YType.uint32, "num-active-entries")

                                        self.num_allocated_entries = YLeaf(YType.uint32, "num-allocated-entries")

                                        self.num_vmr_ids = YLeaf(YType.uint32, "num-vmr-ids")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("num_active_entries",
                                                        "num_allocated_entries",
                                                        "num_vmr_ids") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdLi, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdLi, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.num_active_entries.is_set or
                                            self.num_allocated_entries.is_set or
                                            self.num_vmr_ids.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.num_active_entries.yfilter != YFilter.not_set or
                                            self.num_allocated_entries.yfilter != YFilter.not_set or
                                            self.num_vmr_ids.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "app-id-li" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.num_active_entries.is_set or self.num_active_entries.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.num_active_entries.get_name_leafdata())
                                        if (self.num_allocated_entries.is_set or self.num_allocated_entries.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.num_allocated_entries.get_name_leafdata())
                                        if (self.num_vmr_ids.is_set or self.num_vmr_ids.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.num_vmr_ids.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "num-active-entries" or name == "num-allocated-entries" or name == "num-vmr-ids"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "num-active-entries"):
                                            self.num_active_entries = value
                                            self.num_active_entries.value_namespace = name_space
                                            self.num_active_entries.value_namespace_prefix = name_space_prefix
                                        if(value_path == "num-allocated-entries"):
                                            self.num_allocated_entries = value
                                            self.num_allocated_entries.value_namespace = name_space
                                            self.num_allocated_entries.value_namespace_prefix = name_space_prefix
                                        if(value_path == "num-vmr-ids"):
                                            self.num_vmr_ids = value
                                            self.num_vmr_ids.value_namespace = name_space
                                            self.num_vmr_ids.value_namespace_prefix = name_space_prefix


                                class AppIdPbr(Entity):
                                    """
                                    app PBR entry
                                    
                                    .. attribute:: num_active_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdPbr, self).__init__()

                                        self.yang_name = "app-id-pbr"
                                        self.yang_parent_name = "tcam-lt-ods2"

                                        self.num_active_entries = YLeaf(YType.uint32, "num-active-entries")

                                        self.num_allocated_entries = YLeaf(YType.uint32, "num-allocated-entries")

                                        self.num_vmr_ids = YLeaf(YType.uint32, "num-vmr-ids")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("num_active_entries",
                                                        "num_allocated_entries",
                                                        "num_vmr_ids") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdPbr, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdPbr, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.num_active_entries.is_set or
                                            self.num_allocated_entries.is_set or
                                            self.num_vmr_ids.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.num_active_entries.yfilter != YFilter.not_set or
                                            self.num_allocated_entries.yfilter != YFilter.not_set or
                                            self.num_vmr_ids.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "app-id-pbr" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.num_active_entries.is_set or self.num_active_entries.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.num_active_entries.get_name_leafdata())
                                        if (self.num_allocated_entries.is_set or self.num_allocated_entries.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.num_allocated_entries.get_name_leafdata())
                                        if (self.num_vmr_ids.is_set or self.num_vmr_ids.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.num_vmr_ids.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "num-active-entries" or name == "num-allocated-entries" or name == "num-vmr-ids"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "num-active-entries"):
                                            self.num_active_entries = value
                                            self.num_active_entries.value_namespace = name_space
                                            self.num_active_entries.value_namespace_prefix = name_space_prefix
                                        if(value_path == "num-allocated-entries"):
                                            self.num_allocated_entries = value
                                            self.num_allocated_entries.value_namespace = name_space
                                            self.num_allocated_entries.value_namespace_prefix = name_space_prefix
                                        if(value_path == "num-vmr-ids"):
                                            self.num_vmr_ids = value
                                            self.num_vmr_ids.value_namespace = name_space
                                            self.num_vmr_ids.value_namespace_prefix = name_space_prefix


                                class AppIdEdpl(Entity):
                                    """
                                    app EDPL entry
                                    
                                    .. attribute:: num_active_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdEdpl, self).__init__()

                                        self.yang_name = "app-id-edpl"
                                        self.yang_parent_name = "tcam-lt-ods2"

                                        self.num_active_entries = YLeaf(YType.uint32, "num-active-entries")

                                        self.num_allocated_entries = YLeaf(YType.uint32, "num-allocated-entries")

                                        self.num_vmr_ids = YLeaf(YType.uint32, "num-vmr-ids")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("num_active_entries",
                                                        "num_allocated_entries",
                                                        "num_vmr_ids") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdEdpl, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdEdpl, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.num_active_entries.is_set or
                                            self.num_allocated_entries.is_set or
                                            self.num_vmr_ids.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.num_active_entries.yfilter != YFilter.not_set or
                                            self.num_allocated_entries.yfilter != YFilter.not_set or
                                            self.num_vmr_ids.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "app-id-edpl" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.num_active_entries.is_set or self.num_active_entries.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.num_active_entries.get_name_leafdata())
                                        if (self.num_allocated_entries.is_set or self.num_allocated_entries.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.num_allocated_entries.get_name_leafdata())
                                        if (self.num_vmr_ids.is_set or self.num_vmr_ids.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.num_vmr_ids.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "num-active-entries" or name == "num-allocated-entries" or name == "num-vmr-ids"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "num-active-entries"):
                                            self.num_active_entries = value
                                            self.num_active_entries.value_namespace = name_space
                                            self.num_active_entries.value_namespace_prefix = name_space_prefix
                                        if(value_path == "num-allocated-entries"):
                                            self.num_allocated_entries = value
                                            self.num_allocated_entries.value_namespace = name_space
                                            self.num_allocated_entries.value_namespace_prefix = name_space_prefix
                                        if(value_path == "num-vmr-ids"):
                                            self.num_vmr_ids = value
                                            self.num_vmr_ids.value_namespace = name_space
                                            self.num_vmr_ids.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    return (
                                        self.free_entries.is_set or
                                        self.reserved_entries.is_set or
                                        (self.acl_common is not None and self.acl_common.has_data()) or
                                        (self.app_id_acl is not None and self.app_id_acl.has_data()) or
                                        (self.app_id_afmon is not None and self.app_id_afmon.has_data()) or
                                        (self.app_id_edpl is not None and self.app_id_edpl.has_data()) or
                                        (self.app_id_ifib is not None and self.app_id_ifib.has_data()) or
                                        (self.app_id_li is not None and self.app_id_li.has_data()) or
                                        (self.app_id_pbr is not None and self.app_id_pbr.has_data()) or
                                        (self.app_id_qos is not None and self.app_id_qos.has_data()))

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.free_entries.yfilter != YFilter.not_set or
                                        self.reserved_entries.yfilter != YFilter.not_set or
                                        (self.acl_common is not None and self.acl_common.has_operation()) or
                                        (self.app_id_acl is not None and self.app_id_acl.has_operation()) or
                                        (self.app_id_afmon is not None and self.app_id_afmon.has_operation()) or
                                        (self.app_id_edpl is not None and self.app_id_edpl.has_operation()) or
                                        (self.app_id_ifib is not None and self.app_id_ifib.has_operation()) or
                                        (self.app_id_li is not None and self.app_id_li.has_operation()) or
                                        (self.app_id_pbr is not None and self.app_id_pbr.has_operation()) or
                                        (self.app_id_qos is not None and self.app_id_qos.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "tcam-lt-ods2" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.free_entries.is_set or self.free_entries.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.free_entries.get_name_leafdata())
                                    if (self.reserved_entries.is_set or self.reserved_entries.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.reserved_entries.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "acl-common"):
                                        if (self.acl_common is None):
                                            self.acl_common = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AclCommon()
                                            self.acl_common.parent = self
                                            self._children_name_map["acl_common"] = "acl-common"
                                        return self.acl_common

                                    if (child_yang_name == "app-id-acl"):
                                        if (self.app_id_acl is None):
                                            self.app_id_acl = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdAcl()
                                            self.app_id_acl.parent = self
                                            self._children_name_map["app_id_acl"] = "app-id-acl"
                                        return self.app_id_acl

                                    if (child_yang_name == "app-id-afmon"):
                                        if (self.app_id_afmon is None):
                                            self.app_id_afmon = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdAfmon()
                                            self.app_id_afmon.parent = self
                                            self._children_name_map["app_id_afmon"] = "app-id-afmon"
                                        return self.app_id_afmon

                                    if (child_yang_name == "app-id-edpl"):
                                        if (self.app_id_edpl is None):
                                            self.app_id_edpl = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdEdpl()
                                            self.app_id_edpl.parent = self
                                            self._children_name_map["app_id_edpl"] = "app-id-edpl"
                                        return self.app_id_edpl

                                    if (child_yang_name == "app-id-ifib"):
                                        if (self.app_id_ifib is None):
                                            self.app_id_ifib = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdIfib()
                                            self.app_id_ifib.parent = self
                                            self._children_name_map["app_id_ifib"] = "app-id-ifib"
                                        return self.app_id_ifib

                                    if (child_yang_name == "app-id-li"):
                                        if (self.app_id_li is None):
                                            self.app_id_li = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdLi()
                                            self.app_id_li.parent = self
                                            self._children_name_map["app_id_li"] = "app-id-li"
                                        return self.app_id_li

                                    if (child_yang_name == "app-id-pbr"):
                                        if (self.app_id_pbr is None):
                                            self.app_id_pbr = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdPbr()
                                            self.app_id_pbr.parent = self
                                            self._children_name_map["app_id_pbr"] = "app-id-pbr"
                                        return self.app_id_pbr

                                    if (child_yang_name == "app-id-qos"):
                                        if (self.app_id_qos is None):
                                            self.app_id_qos = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdQos()
                                            self.app_id_qos.parent = self
                                            self._children_name_map["app_id_qos"] = "app-id-qos"
                                        return self.app_id_qos

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "acl-common" or name == "app-id-acl" or name == "app-id-afmon" or name == "app-id-edpl" or name == "app-id-ifib" or name == "app-id-li" or name == "app-id-pbr" or name == "app-id-qos" or name == "free-entries" or name == "reserved-entries"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "free-entries"):
                                        self.free_entries = value
                                        self.free_entries.value_namespace = name_space
                                        self.free_entries.value_namespace_prefix = name_space_prefix
                                    if(value_path == "reserved-entries"):
                                        self.reserved_entries = value
                                        self.reserved_entries.value_namespace = name_space
                                        self.reserved_entries.value_namespace_prefix = name_space_prefix


                            class TcamLtOds8(Entity):
                                """
                                TCAM ODS8 partition summary
                                
                                .. attribute:: acl_common
                                
                                	ACL common region
                                	**type**\:   :py:class:`AclCommon <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AclCommon>`
                                
                                .. attribute:: app_id_acl
                                
                                	app acl entry
                                	**type**\:   :py:class:`AppIdAcl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdAcl>`
                                
                                .. attribute:: app_id_afmon
                                
                                	app afmon entry
                                	**type**\:   :py:class:`AppIdAfmon <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdAfmon>`
                                
                                .. attribute:: app_id_edpl
                                
                                	app EDPL entry
                                	**type**\:   :py:class:`AppIdEdpl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdEdpl>`
                                
                                .. attribute:: app_id_ifib
                                
                                	app IFIB entry
                                	**type**\:   :py:class:`AppIdIfib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdIfib>`
                                
                                .. attribute:: app_id_li
                                
                                	app LI entry
                                	**type**\:   :py:class:`AppIdLi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdLi>`
                                
                                .. attribute:: app_id_pbr
                                
                                	app PBR entry
                                	**type**\:   :py:class:`AppIdPbr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdPbr>`
                                
                                .. attribute:: app_id_qos
                                
                                	app qos entry
                                	**type**\:   :py:class:`AppIdQos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdQos>`
                                
                                .. attribute:: free_entries
                                
                                	Free entries in the table
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: reserved_entries
                                
                                	The number of active vmr entries
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'asr9k-np-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8, self).__init__()

                                    self.yang_name = "tcam-lt-ods8"
                                    self.yang_parent_name = "tcam-info"

                                    self.free_entries = YLeaf(YType.uint32, "free-entries")

                                    self.reserved_entries = YLeaf(YType.uint32, "reserved-entries")

                                    self.acl_common = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AclCommon()
                                    self.acl_common.parent = self
                                    self._children_name_map["acl_common"] = "acl-common"
                                    self._children_yang_names.add("acl-common")

                                    self.app_id_acl = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdAcl()
                                    self.app_id_acl.parent = self
                                    self._children_name_map["app_id_acl"] = "app-id-acl"
                                    self._children_yang_names.add("app-id-acl")

                                    self.app_id_afmon = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdAfmon()
                                    self.app_id_afmon.parent = self
                                    self._children_name_map["app_id_afmon"] = "app-id-afmon"
                                    self._children_yang_names.add("app-id-afmon")

                                    self.app_id_edpl = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdEdpl()
                                    self.app_id_edpl.parent = self
                                    self._children_name_map["app_id_edpl"] = "app-id-edpl"
                                    self._children_yang_names.add("app-id-edpl")

                                    self.app_id_ifib = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdIfib()
                                    self.app_id_ifib.parent = self
                                    self._children_name_map["app_id_ifib"] = "app-id-ifib"
                                    self._children_yang_names.add("app-id-ifib")

                                    self.app_id_li = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdLi()
                                    self.app_id_li.parent = self
                                    self._children_name_map["app_id_li"] = "app-id-li"
                                    self._children_yang_names.add("app-id-li")

                                    self.app_id_pbr = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdPbr()
                                    self.app_id_pbr.parent = self
                                    self._children_name_map["app_id_pbr"] = "app-id-pbr"
                                    self._children_yang_names.add("app-id-pbr")

                                    self.app_id_qos = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdQos()
                                    self.app_id_qos.parent = self
                                    self._children_name_map["app_id_qos"] = "app-id-qos"
                                    self._children_yang_names.add("app-id-qos")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("free_entries",
                                                    "reserved_entries") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8, self).__setattr__(name, value)


                                class AclCommon(Entity):
                                    """
                                    ACL common region
                                    
                                    .. attribute:: allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: free_entries
                                    
                                    	Free entries in the table
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AclCommon, self).__init__()

                                        self.yang_name = "acl-common"
                                        self.yang_parent_name = "tcam-lt-ods8"

                                        self.allocated_entries = YLeaf(YType.uint32, "allocated-entries")

                                        self.free_entries = YLeaf(YType.uint32, "free-entries")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("allocated_entries",
                                                        "free_entries") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AclCommon, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AclCommon, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.allocated_entries.is_set or
                                            self.free_entries.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.allocated_entries.yfilter != YFilter.not_set or
                                            self.free_entries.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "acl-common" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.allocated_entries.is_set or self.allocated_entries.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.allocated_entries.get_name_leafdata())
                                        if (self.free_entries.is_set or self.free_entries.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.free_entries.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "allocated-entries" or name == "free-entries"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "allocated-entries"):
                                            self.allocated_entries = value
                                            self.allocated_entries.value_namespace = name_space
                                            self.allocated_entries.value_namespace_prefix = name_space_prefix
                                        if(value_path == "free-entries"):
                                            self.free_entries = value
                                            self.free_entries.value_namespace = name_space
                                            self.free_entries.value_namespace_prefix = name_space_prefix


                                class AppIdIfib(Entity):
                                    """
                                    app IFIB entry
                                    
                                    .. attribute:: num_active_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdIfib, self).__init__()

                                        self.yang_name = "app-id-ifib"
                                        self.yang_parent_name = "tcam-lt-ods8"

                                        self.num_active_entries = YLeaf(YType.uint32, "num-active-entries")

                                        self.num_allocated_entries = YLeaf(YType.uint32, "num-allocated-entries")

                                        self.num_vmr_ids = YLeaf(YType.uint32, "num-vmr-ids")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("num_active_entries",
                                                        "num_allocated_entries",
                                                        "num_vmr_ids") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdIfib, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdIfib, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.num_active_entries.is_set or
                                            self.num_allocated_entries.is_set or
                                            self.num_vmr_ids.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.num_active_entries.yfilter != YFilter.not_set or
                                            self.num_allocated_entries.yfilter != YFilter.not_set or
                                            self.num_vmr_ids.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "app-id-ifib" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.num_active_entries.is_set or self.num_active_entries.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.num_active_entries.get_name_leafdata())
                                        if (self.num_allocated_entries.is_set or self.num_allocated_entries.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.num_allocated_entries.get_name_leafdata())
                                        if (self.num_vmr_ids.is_set or self.num_vmr_ids.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.num_vmr_ids.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "num-active-entries" or name == "num-allocated-entries" or name == "num-vmr-ids"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "num-active-entries"):
                                            self.num_active_entries = value
                                            self.num_active_entries.value_namespace = name_space
                                            self.num_active_entries.value_namespace_prefix = name_space_prefix
                                        if(value_path == "num-allocated-entries"):
                                            self.num_allocated_entries = value
                                            self.num_allocated_entries.value_namespace = name_space
                                            self.num_allocated_entries.value_namespace_prefix = name_space_prefix
                                        if(value_path == "num-vmr-ids"):
                                            self.num_vmr_ids = value
                                            self.num_vmr_ids.value_namespace = name_space
                                            self.num_vmr_ids.value_namespace_prefix = name_space_prefix


                                class AppIdQos(Entity):
                                    """
                                    app qos entry
                                    
                                    .. attribute:: num_active_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdQos, self).__init__()

                                        self.yang_name = "app-id-qos"
                                        self.yang_parent_name = "tcam-lt-ods8"

                                        self.num_active_entries = YLeaf(YType.uint32, "num-active-entries")

                                        self.num_allocated_entries = YLeaf(YType.uint32, "num-allocated-entries")

                                        self.num_vmr_ids = YLeaf(YType.uint32, "num-vmr-ids")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("num_active_entries",
                                                        "num_allocated_entries",
                                                        "num_vmr_ids") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdQos, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdQos, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.num_active_entries.is_set or
                                            self.num_allocated_entries.is_set or
                                            self.num_vmr_ids.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.num_active_entries.yfilter != YFilter.not_set or
                                            self.num_allocated_entries.yfilter != YFilter.not_set or
                                            self.num_vmr_ids.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "app-id-qos" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.num_active_entries.is_set or self.num_active_entries.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.num_active_entries.get_name_leafdata())
                                        if (self.num_allocated_entries.is_set or self.num_allocated_entries.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.num_allocated_entries.get_name_leafdata())
                                        if (self.num_vmr_ids.is_set or self.num_vmr_ids.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.num_vmr_ids.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "num-active-entries" or name == "num-allocated-entries" or name == "num-vmr-ids"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "num-active-entries"):
                                            self.num_active_entries = value
                                            self.num_active_entries.value_namespace = name_space
                                            self.num_active_entries.value_namespace_prefix = name_space_prefix
                                        if(value_path == "num-allocated-entries"):
                                            self.num_allocated_entries = value
                                            self.num_allocated_entries.value_namespace = name_space
                                            self.num_allocated_entries.value_namespace_prefix = name_space_prefix
                                        if(value_path == "num-vmr-ids"):
                                            self.num_vmr_ids = value
                                            self.num_vmr_ids.value_namespace = name_space
                                            self.num_vmr_ids.value_namespace_prefix = name_space_prefix


                                class AppIdAcl(Entity):
                                    """
                                    app acl entry
                                    
                                    .. attribute:: num_active_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdAcl, self).__init__()

                                        self.yang_name = "app-id-acl"
                                        self.yang_parent_name = "tcam-lt-ods8"

                                        self.num_active_entries = YLeaf(YType.uint32, "num-active-entries")

                                        self.num_allocated_entries = YLeaf(YType.uint32, "num-allocated-entries")

                                        self.num_vmr_ids = YLeaf(YType.uint32, "num-vmr-ids")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("num_active_entries",
                                                        "num_allocated_entries",
                                                        "num_vmr_ids") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdAcl, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdAcl, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.num_active_entries.is_set or
                                            self.num_allocated_entries.is_set or
                                            self.num_vmr_ids.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.num_active_entries.yfilter != YFilter.not_set or
                                            self.num_allocated_entries.yfilter != YFilter.not_set or
                                            self.num_vmr_ids.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "app-id-acl" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.num_active_entries.is_set or self.num_active_entries.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.num_active_entries.get_name_leafdata())
                                        if (self.num_allocated_entries.is_set or self.num_allocated_entries.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.num_allocated_entries.get_name_leafdata())
                                        if (self.num_vmr_ids.is_set or self.num_vmr_ids.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.num_vmr_ids.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "num-active-entries" or name == "num-allocated-entries" or name == "num-vmr-ids"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "num-active-entries"):
                                            self.num_active_entries = value
                                            self.num_active_entries.value_namespace = name_space
                                            self.num_active_entries.value_namespace_prefix = name_space_prefix
                                        if(value_path == "num-allocated-entries"):
                                            self.num_allocated_entries = value
                                            self.num_allocated_entries.value_namespace = name_space
                                            self.num_allocated_entries.value_namespace_prefix = name_space_prefix
                                        if(value_path == "num-vmr-ids"):
                                            self.num_vmr_ids = value
                                            self.num_vmr_ids.value_namespace = name_space
                                            self.num_vmr_ids.value_namespace_prefix = name_space_prefix


                                class AppIdAfmon(Entity):
                                    """
                                    app afmon entry
                                    
                                    .. attribute:: num_active_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdAfmon, self).__init__()

                                        self.yang_name = "app-id-afmon"
                                        self.yang_parent_name = "tcam-lt-ods8"

                                        self.num_active_entries = YLeaf(YType.uint32, "num-active-entries")

                                        self.num_allocated_entries = YLeaf(YType.uint32, "num-allocated-entries")

                                        self.num_vmr_ids = YLeaf(YType.uint32, "num-vmr-ids")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("num_active_entries",
                                                        "num_allocated_entries",
                                                        "num_vmr_ids") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdAfmon, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdAfmon, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.num_active_entries.is_set or
                                            self.num_allocated_entries.is_set or
                                            self.num_vmr_ids.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.num_active_entries.yfilter != YFilter.not_set or
                                            self.num_allocated_entries.yfilter != YFilter.not_set or
                                            self.num_vmr_ids.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "app-id-afmon" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.num_active_entries.is_set or self.num_active_entries.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.num_active_entries.get_name_leafdata())
                                        if (self.num_allocated_entries.is_set or self.num_allocated_entries.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.num_allocated_entries.get_name_leafdata())
                                        if (self.num_vmr_ids.is_set or self.num_vmr_ids.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.num_vmr_ids.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "num-active-entries" or name == "num-allocated-entries" or name == "num-vmr-ids"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "num-active-entries"):
                                            self.num_active_entries = value
                                            self.num_active_entries.value_namespace = name_space
                                            self.num_active_entries.value_namespace_prefix = name_space_prefix
                                        if(value_path == "num-allocated-entries"):
                                            self.num_allocated_entries = value
                                            self.num_allocated_entries.value_namespace = name_space
                                            self.num_allocated_entries.value_namespace_prefix = name_space_prefix
                                        if(value_path == "num-vmr-ids"):
                                            self.num_vmr_ids = value
                                            self.num_vmr_ids.value_namespace = name_space
                                            self.num_vmr_ids.value_namespace_prefix = name_space_prefix


                                class AppIdLi(Entity):
                                    """
                                    app LI entry
                                    
                                    .. attribute:: num_active_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdLi, self).__init__()

                                        self.yang_name = "app-id-li"
                                        self.yang_parent_name = "tcam-lt-ods8"

                                        self.num_active_entries = YLeaf(YType.uint32, "num-active-entries")

                                        self.num_allocated_entries = YLeaf(YType.uint32, "num-allocated-entries")

                                        self.num_vmr_ids = YLeaf(YType.uint32, "num-vmr-ids")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("num_active_entries",
                                                        "num_allocated_entries",
                                                        "num_vmr_ids") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdLi, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdLi, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.num_active_entries.is_set or
                                            self.num_allocated_entries.is_set or
                                            self.num_vmr_ids.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.num_active_entries.yfilter != YFilter.not_set or
                                            self.num_allocated_entries.yfilter != YFilter.not_set or
                                            self.num_vmr_ids.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "app-id-li" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.num_active_entries.is_set or self.num_active_entries.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.num_active_entries.get_name_leafdata())
                                        if (self.num_allocated_entries.is_set or self.num_allocated_entries.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.num_allocated_entries.get_name_leafdata())
                                        if (self.num_vmr_ids.is_set or self.num_vmr_ids.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.num_vmr_ids.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "num-active-entries" or name == "num-allocated-entries" or name == "num-vmr-ids"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "num-active-entries"):
                                            self.num_active_entries = value
                                            self.num_active_entries.value_namespace = name_space
                                            self.num_active_entries.value_namespace_prefix = name_space_prefix
                                        if(value_path == "num-allocated-entries"):
                                            self.num_allocated_entries = value
                                            self.num_allocated_entries.value_namespace = name_space
                                            self.num_allocated_entries.value_namespace_prefix = name_space_prefix
                                        if(value_path == "num-vmr-ids"):
                                            self.num_vmr_ids = value
                                            self.num_vmr_ids.value_namespace = name_space
                                            self.num_vmr_ids.value_namespace_prefix = name_space_prefix


                                class AppIdPbr(Entity):
                                    """
                                    app PBR entry
                                    
                                    .. attribute:: num_active_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdPbr, self).__init__()

                                        self.yang_name = "app-id-pbr"
                                        self.yang_parent_name = "tcam-lt-ods8"

                                        self.num_active_entries = YLeaf(YType.uint32, "num-active-entries")

                                        self.num_allocated_entries = YLeaf(YType.uint32, "num-allocated-entries")

                                        self.num_vmr_ids = YLeaf(YType.uint32, "num-vmr-ids")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("num_active_entries",
                                                        "num_allocated_entries",
                                                        "num_vmr_ids") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdPbr, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdPbr, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.num_active_entries.is_set or
                                            self.num_allocated_entries.is_set or
                                            self.num_vmr_ids.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.num_active_entries.yfilter != YFilter.not_set or
                                            self.num_allocated_entries.yfilter != YFilter.not_set or
                                            self.num_vmr_ids.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "app-id-pbr" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.num_active_entries.is_set or self.num_active_entries.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.num_active_entries.get_name_leafdata())
                                        if (self.num_allocated_entries.is_set or self.num_allocated_entries.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.num_allocated_entries.get_name_leafdata())
                                        if (self.num_vmr_ids.is_set or self.num_vmr_ids.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.num_vmr_ids.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "num-active-entries" or name == "num-allocated-entries" or name == "num-vmr-ids"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "num-active-entries"):
                                            self.num_active_entries = value
                                            self.num_active_entries.value_namespace = name_space
                                            self.num_active_entries.value_namespace_prefix = name_space_prefix
                                        if(value_path == "num-allocated-entries"):
                                            self.num_allocated_entries = value
                                            self.num_allocated_entries.value_namespace = name_space
                                            self.num_allocated_entries.value_namespace_prefix = name_space_prefix
                                        if(value_path == "num-vmr-ids"):
                                            self.num_vmr_ids = value
                                            self.num_vmr_ids.value_namespace = name_space
                                            self.num_vmr_ids.value_namespace_prefix = name_space_prefix


                                class AppIdEdpl(Entity):
                                    """
                                    app EDPL entry
                                    
                                    .. attribute:: num_active_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdEdpl, self).__init__()

                                        self.yang_name = "app-id-edpl"
                                        self.yang_parent_name = "tcam-lt-ods8"

                                        self.num_active_entries = YLeaf(YType.uint32, "num-active-entries")

                                        self.num_allocated_entries = YLeaf(YType.uint32, "num-allocated-entries")

                                        self.num_vmr_ids = YLeaf(YType.uint32, "num-vmr-ids")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("num_active_entries",
                                                        "num_allocated_entries",
                                                        "num_vmr_ids") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdEdpl, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdEdpl, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.num_active_entries.is_set or
                                            self.num_allocated_entries.is_set or
                                            self.num_vmr_ids.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.num_active_entries.yfilter != YFilter.not_set or
                                            self.num_allocated_entries.yfilter != YFilter.not_set or
                                            self.num_vmr_ids.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "app-id-edpl" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.num_active_entries.is_set or self.num_active_entries.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.num_active_entries.get_name_leafdata())
                                        if (self.num_allocated_entries.is_set or self.num_allocated_entries.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.num_allocated_entries.get_name_leafdata())
                                        if (self.num_vmr_ids.is_set or self.num_vmr_ids.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.num_vmr_ids.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "num-active-entries" or name == "num-allocated-entries" or name == "num-vmr-ids"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "num-active-entries"):
                                            self.num_active_entries = value
                                            self.num_active_entries.value_namespace = name_space
                                            self.num_active_entries.value_namespace_prefix = name_space_prefix
                                        if(value_path == "num-allocated-entries"):
                                            self.num_allocated_entries = value
                                            self.num_allocated_entries.value_namespace = name_space
                                            self.num_allocated_entries.value_namespace_prefix = name_space_prefix
                                        if(value_path == "num-vmr-ids"):
                                            self.num_vmr_ids = value
                                            self.num_vmr_ids.value_namespace = name_space
                                            self.num_vmr_ids.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    return (
                                        self.free_entries.is_set or
                                        self.reserved_entries.is_set or
                                        (self.acl_common is not None and self.acl_common.has_data()) or
                                        (self.app_id_acl is not None and self.app_id_acl.has_data()) or
                                        (self.app_id_afmon is not None and self.app_id_afmon.has_data()) or
                                        (self.app_id_edpl is not None and self.app_id_edpl.has_data()) or
                                        (self.app_id_ifib is not None and self.app_id_ifib.has_data()) or
                                        (self.app_id_li is not None and self.app_id_li.has_data()) or
                                        (self.app_id_pbr is not None and self.app_id_pbr.has_data()) or
                                        (self.app_id_qos is not None and self.app_id_qos.has_data()))

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.free_entries.yfilter != YFilter.not_set or
                                        self.reserved_entries.yfilter != YFilter.not_set or
                                        (self.acl_common is not None and self.acl_common.has_operation()) or
                                        (self.app_id_acl is not None and self.app_id_acl.has_operation()) or
                                        (self.app_id_afmon is not None and self.app_id_afmon.has_operation()) or
                                        (self.app_id_edpl is not None and self.app_id_edpl.has_operation()) or
                                        (self.app_id_ifib is not None and self.app_id_ifib.has_operation()) or
                                        (self.app_id_li is not None and self.app_id_li.has_operation()) or
                                        (self.app_id_pbr is not None and self.app_id_pbr.has_operation()) or
                                        (self.app_id_qos is not None and self.app_id_qos.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "tcam-lt-ods8" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.free_entries.is_set or self.free_entries.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.free_entries.get_name_leafdata())
                                    if (self.reserved_entries.is_set or self.reserved_entries.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.reserved_entries.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "acl-common"):
                                        if (self.acl_common is None):
                                            self.acl_common = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AclCommon()
                                            self.acl_common.parent = self
                                            self._children_name_map["acl_common"] = "acl-common"
                                        return self.acl_common

                                    if (child_yang_name == "app-id-acl"):
                                        if (self.app_id_acl is None):
                                            self.app_id_acl = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdAcl()
                                            self.app_id_acl.parent = self
                                            self._children_name_map["app_id_acl"] = "app-id-acl"
                                        return self.app_id_acl

                                    if (child_yang_name == "app-id-afmon"):
                                        if (self.app_id_afmon is None):
                                            self.app_id_afmon = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdAfmon()
                                            self.app_id_afmon.parent = self
                                            self._children_name_map["app_id_afmon"] = "app-id-afmon"
                                        return self.app_id_afmon

                                    if (child_yang_name == "app-id-edpl"):
                                        if (self.app_id_edpl is None):
                                            self.app_id_edpl = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdEdpl()
                                            self.app_id_edpl.parent = self
                                            self._children_name_map["app_id_edpl"] = "app-id-edpl"
                                        return self.app_id_edpl

                                    if (child_yang_name == "app-id-ifib"):
                                        if (self.app_id_ifib is None):
                                            self.app_id_ifib = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdIfib()
                                            self.app_id_ifib.parent = self
                                            self._children_name_map["app_id_ifib"] = "app-id-ifib"
                                        return self.app_id_ifib

                                    if (child_yang_name == "app-id-li"):
                                        if (self.app_id_li is None):
                                            self.app_id_li = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdLi()
                                            self.app_id_li.parent = self
                                            self._children_name_map["app_id_li"] = "app-id-li"
                                        return self.app_id_li

                                    if (child_yang_name == "app-id-pbr"):
                                        if (self.app_id_pbr is None):
                                            self.app_id_pbr = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdPbr()
                                            self.app_id_pbr.parent = self
                                            self._children_name_map["app_id_pbr"] = "app-id-pbr"
                                        return self.app_id_pbr

                                    if (child_yang_name == "app-id-qos"):
                                        if (self.app_id_qos is None):
                                            self.app_id_qos = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdQos()
                                            self.app_id_qos.parent = self
                                            self._children_name_map["app_id_qos"] = "app-id-qos"
                                        return self.app_id_qos

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "acl-common" or name == "app-id-acl" or name == "app-id-afmon" or name == "app-id-edpl" or name == "app-id-ifib" or name == "app-id-li" or name == "app-id-pbr" or name == "app-id-qos" or name == "free-entries" or name == "reserved-entries"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "free-entries"):
                                        self.free_entries = value
                                        self.free_entries.value_namespace = name_space
                                        self.free_entries.value_namespace_prefix = name_space_prefix
                                    if(value_path == "reserved-entries"):
                                        self.reserved_entries = value
                                        self.reserved_entries.value_namespace = name_space
                                        self.reserved_entries.value_namespace_prefix = name_space_prefix


                            class TcamLtL2(Entity):
                                """
                                Array of TCAM L2 partition summaries
                                
                                .. attribute:: free_entries
                                
                                	Free Entries
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: partition_id
                                
                                	PartitionID
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: priority
                                
                                	Priority
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: valid_entries
                                
                                	Valid Entries
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'asr9k-np-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtL2, self).__init__()

                                    self.yang_name = "tcam-lt-l2"
                                    self.yang_parent_name = "tcam-info"

                                    self.free_entries = YLeaf(YType.uint32, "free-entries")

                                    self.partition_id = YLeaf(YType.uint32, "partition-id")

                                    self.priority = YLeaf(YType.uint32, "priority")

                                    self.valid_entries = YLeaf(YType.uint32, "valid-entries")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("free_entries",
                                                    "partition_id",
                                                    "priority",
                                                    "valid_entries") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtL2, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtL2, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.free_entries.is_set or
                                        self.partition_id.is_set or
                                        self.priority.is_set or
                                        self.valid_entries.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.free_entries.yfilter != YFilter.not_set or
                                        self.partition_id.yfilter != YFilter.not_set or
                                        self.priority.yfilter != YFilter.not_set or
                                        self.valid_entries.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "tcam-lt-l2" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.free_entries.is_set or self.free_entries.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.free_entries.get_name_leafdata())
                                    if (self.partition_id.is_set or self.partition_id.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.partition_id.get_name_leafdata())
                                    if (self.priority.is_set or self.priority.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.priority.get_name_leafdata())
                                    if (self.valid_entries.is_set or self.valid_entries.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.valid_entries.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "free-entries" or name == "partition-id" or name == "priority" or name == "valid-entries"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "free-entries"):
                                        self.free_entries = value
                                        self.free_entries.value_namespace = name_space
                                        self.free_entries.value_namespace_prefix = name_space_prefix
                                    if(value_path == "partition-id"):
                                        self.partition_id = value
                                        self.partition_id.value_namespace = name_space
                                        self.partition_id.value_namespace_prefix = name_space_prefix
                                    if(value_path == "priority"):
                                        self.priority = value
                                        self.priority.value_namespace = name_space
                                        self.priority.value_namespace_prefix = name_space_prefix
                                    if(value_path == "valid-entries"):
                                        self.valid_entries = value
                                        self.valid_entries.value_namespace = name_space
                                        self.valid_entries.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                for c in self.tcam_lt_l2:
                                    if (c.has_data()):
                                        return True
                                return (
                                    (self.tcam_lt_ods2 is not None and self.tcam_lt_ods2.has_data()) or
                                    (self.tcam_lt_ods8 is not None and self.tcam_lt_ods8.has_data()))

                            def has_operation(self):
                                for c in self.tcam_lt_l2:
                                    if (c.has_operation()):
                                        return True
                                return (
                                    self.yfilter != YFilter.not_set or
                                    (self.tcam_lt_ods2 is not None and self.tcam_lt_ods2.has_operation()) or
                                    (self.tcam_lt_ods8 is not None and self.tcam_lt_ods8.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "tcam-info" + path_buffer

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

                                if (child_yang_name == "tcam-lt-l2"):
                                    for c in self.tcam_lt_l2:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtL2()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.tcam_lt_l2.append(c)
                                    return c

                                if (child_yang_name == "tcam-lt-ods2"):
                                    if (self.tcam_lt_ods2 is None):
                                        self.tcam_lt_ods2 = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2()
                                        self.tcam_lt_ods2.parent = self
                                        self._children_name_map["tcam_lt_ods2"] = "tcam-lt-ods2"
                                    return self.tcam_lt_ods2

                                if (child_yang_name == "tcam-lt-ods8"):
                                    if (self.tcam_lt_ods8 is None):
                                        self.tcam_lt_ods8 = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8()
                                        self.tcam_lt_ods8.parent = self
                                        self._children_name_map["tcam_lt_ods8"] = "tcam-lt-ods8"
                                    return self.tcam_lt_ods8

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "tcam-lt-l2" or name == "tcam-lt-ods2" or name == "tcam-lt-ods8"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass

                        def has_data(self):
                            return (
                                (self.internal_tcam_info is not None and self.internal_tcam_info.has_data()) or
                                (self.tcam_info is not None and self.tcam_info.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                (self.internal_tcam_info is not None and self.internal_tcam_info.has_operation()) or
                                (self.tcam_info is not None and self.tcam_info.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "tcam-summary" + path_buffer

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

                            if (child_yang_name == "internal-tcam-info"):
                                if (self.internal_tcam_info is None):
                                    self.internal_tcam_info = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo()
                                    self.internal_tcam_info.parent = self
                                    self._children_name_map["internal_tcam_info"] = "internal-tcam-info"
                                return self.internal_tcam_info

                            if (child_yang_name == "tcam-info"):
                                if (self.tcam_info is None):
                                    self.tcam_info = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo()
                                    self.tcam_info.parent = self
                                    self._children_name_map["tcam_info"] = "tcam-info"
                                return self.tcam_info

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "internal-tcam-info" or name == "tcam-info"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass


                    class Counters(Entity):
                        """
                        prm counters info
                        
                        .. attribute:: np_counter
                        
                        	Array of NP Counters
                        	**type**\: list of    :py:class:`NpCounter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.Counters.NpCounter>`
                        
                        

                        """

                        _prefix = 'asr9k-np-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(HardwareModuleNp.Nodes.Node.Nps.Np.Counters, self).__init__()

                            self.yang_name = "counters"
                            self.yang_parent_name = "np"

                            self.np_counter = YList(self)

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
                                        super(HardwareModuleNp.Nodes.Node.Nps.Np.Counters, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(HardwareModuleNp.Nodes.Node.Nps.Np.Counters, self).__setattr__(name, value)


                        class NpCounter(Entity):
                            """
                            Array of NP Counters
                            
                            .. attribute:: counter_index
                            
                            	Counter Index
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: counter_name
                            
                            	Counter name
                            	**type**\:  str
                            
                            .. attribute:: counter_type
                            
                            	Counter TypeDROP\: Drop counterPUNT\: Punt counterFWD\:  Forward or generic counterUNKNOWN\: Counter type unknown
                            	**type**\:  str
                            
                            .. attribute:: counter_value
                            
                            	The accurate value of the counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: rate
                            
                            	Rate in Packets Per Second
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: packet/s
                            
                            

                            """

                            _prefix = 'asr9k-np-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(HardwareModuleNp.Nodes.Node.Nps.Np.Counters.NpCounter, self).__init__()

                                self.yang_name = "np-counter"
                                self.yang_parent_name = "counters"

                                self.counter_index = YLeaf(YType.uint32, "counter-index")

                                self.counter_name = YLeaf(YType.str, "counter-name")

                                self.counter_type = YLeaf(YType.str, "counter-type")

                                self.counter_value = YLeaf(YType.uint64, "counter-value")

                                self.rate = YLeaf(YType.uint32, "rate")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("counter_index",
                                                "counter_name",
                                                "counter_type",
                                                "counter_value",
                                                "rate") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(HardwareModuleNp.Nodes.Node.Nps.Np.Counters.NpCounter, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(HardwareModuleNp.Nodes.Node.Nps.Np.Counters.NpCounter, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.counter_index.is_set or
                                    self.counter_name.is_set or
                                    self.counter_type.is_set or
                                    self.counter_value.is_set or
                                    self.rate.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.counter_index.yfilter != YFilter.not_set or
                                    self.counter_name.yfilter != YFilter.not_set or
                                    self.counter_type.yfilter != YFilter.not_set or
                                    self.counter_value.yfilter != YFilter.not_set or
                                    self.rate.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "np-counter" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.counter_index.is_set or self.counter_index.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.counter_index.get_name_leafdata())
                                if (self.counter_name.is_set or self.counter_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.counter_name.get_name_leafdata())
                                if (self.counter_type.is_set or self.counter_type.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.counter_type.get_name_leafdata())
                                if (self.counter_value.is_set or self.counter_value.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.counter_value.get_name_leafdata())
                                if (self.rate.is_set or self.rate.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.rate.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "counter-index" or name == "counter-name" or name == "counter-type" or name == "counter-value" or name == "rate"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "counter-index"):
                                    self.counter_index = value
                                    self.counter_index.value_namespace = name_space
                                    self.counter_index.value_namespace_prefix = name_space_prefix
                                if(value_path == "counter-name"):
                                    self.counter_name = value
                                    self.counter_name.value_namespace = name_space
                                    self.counter_name.value_namespace_prefix = name_space_prefix
                                if(value_path == "counter-type"):
                                    self.counter_type = value
                                    self.counter_type.value_namespace = name_space
                                    self.counter_type.value_namespace_prefix = name_space_prefix
                                if(value_path == "counter-value"):
                                    self.counter_value = value
                                    self.counter_value.value_namespace = name_space
                                    self.counter_value.value_namespace_prefix = name_space_prefix
                                if(value_path == "rate"):
                                    self.rate = value
                                    self.rate.value_namespace = name_space
                                    self.rate.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.np_counter:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.np_counter:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "counters" + path_buffer

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

                            if (child_yang_name == "np-counter"):
                                for c in self.np_counter:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = HardwareModuleNp.Nodes.Node.Nps.Np.Counters.NpCounter()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.np_counter.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "np-counter"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass


                    class FastDrop(Entity):
                        """
                        prm fast drop counters info
                        
                        .. attribute:: np_fast_drop
                        
                        	Array of NP Fast Drop Counters
                        	**type**\: list of    :py:class:`NpFastDrop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.FastDrop.NpFastDrop>`
                        
                        

                        """

                        _prefix = 'asr9k-np-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(HardwareModuleNp.Nodes.Node.Nps.Np.FastDrop, self).__init__()

                            self.yang_name = "fast-drop"
                            self.yang_parent_name = "np"

                            self.np_fast_drop = YList(self)

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
                                        super(HardwareModuleNp.Nodes.Node.Nps.Np.FastDrop, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(HardwareModuleNp.Nodes.Node.Nps.Np.FastDrop, self).__setattr__(name, value)


                        class NpFastDrop(Entity):
                            """
                            Array of NP Fast Drop Counters
                            
                            .. attribute:: counter_value
                            
                            	The Value of the counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: interface_name
                            
                            	Interface name
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'asr9k-np-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(HardwareModuleNp.Nodes.Node.Nps.Np.FastDrop.NpFastDrop, self).__init__()

                                self.yang_name = "np-fast-drop"
                                self.yang_parent_name = "fast-drop"

                                self.counter_value = YLeaf(YType.uint64, "counter-value")

                                self.interface_name = YLeaf(YType.str, "interface-name")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("counter_value",
                                                "interface_name") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(HardwareModuleNp.Nodes.Node.Nps.Np.FastDrop.NpFastDrop, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(HardwareModuleNp.Nodes.Node.Nps.Np.FastDrop.NpFastDrop, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.counter_value.is_set or
                                    self.interface_name.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.counter_value.yfilter != YFilter.not_set or
                                    self.interface_name.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "np-fast-drop" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.counter_value.is_set or self.counter_value.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.counter_value.get_name_leafdata())
                                if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.interface_name.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "counter-value" or name == "interface-name"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "counter-value"):
                                    self.counter_value = value
                                    self.counter_value.value_namespace = name_space
                                    self.counter_value.value_namespace_prefix = name_space_prefix
                                if(value_path == "interface-name"):
                                    self.interface_name = value
                                    self.interface_name.value_namespace = name_space
                                    self.interface_name.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.np_fast_drop:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.np_fast_drop:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "fast-drop" + path_buffer

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

                            if (child_yang_name == "np-fast-drop"):
                                for c in self.np_fast_drop:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = HardwareModuleNp.Nodes.Node.Nps.Np.FastDrop.NpFastDrop()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.np_fast_drop.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "np-fast-drop"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (
                            self.np_name.is_set or
                            (self.chn_load is not None and self.chn_load.has_data()) or
                            (self.counters is not None and self.counters.has_data()) or
                            (self.fast_drop is not None and self.fast_drop.has_data()) or
                            (self.tcam_summary is not None and self.tcam_summary.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.np_name.yfilter != YFilter.not_set or
                            (self.chn_load is not None and self.chn_load.has_operation()) or
                            (self.counters is not None and self.counters.has_operation()) or
                            (self.fast_drop is not None and self.fast_drop.has_operation()) or
                            (self.tcam_summary is not None and self.tcam_summary.has_operation()))

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

                        if (child_yang_name == "chn-load"):
                            if (self.chn_load is None):
                                self.chn_load = HardwareModuleNp.Nodes.Node.Nps.Np.ChnLoad()
                                self.chn_load.parent = self
                                self._children_name_map["chn_load"] = "chn-load"
                            return self.chn_load

                        if (child_yang_name == "counters"):
                            if (self.counters is None):
                                self.counters = HardwareModuleNp.Nodes.Node.Nps.Np.Counters()
                                self.counters.parent = self
                                self._children_name_map["counters"] = "counters"
                            return self.counters

                        if (child_yang_name == "fast-drop"):
                            if (self.fast_drop is None):
                                self.fast_drop = HardwareModuleNp.Nodes.Node.Nps.Np.FastDrop()
                                self.fast_drop.parent = self
                                self._children_name_map["fast_drop"] = "fast-drop"
                            return self.fast_drop

                        if (child_yang_name == "tcam-summary"):
                            if (self.tcam_summary is None):
                                self.tcam_summary = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary()
                                self.tcam_summary.parent = self
                                self._children_name_map["tcam_summary"] = "tcam-summary"
                            return self.tcam_summary

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "chn-load" or name == "counters" or name == "fast-drop" or name == "tcam-summary" or name == "np-name"):
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
                        c = HardwareModuleNp.Nodes.Node.Nps.Np()
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
                path_buffer = "node" + "[node-name='" + self.node_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-asr9k-np-oper:hardware-module-np/nodes/%s" % self.get_segment_path()
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
                        self.nps = HardwareModuleNp.Nodes.Node.Nps()
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
                path_buffer = "Cisco-IOS-XR-asr9k-np-oper:hardware-module-np/%s" % self.get_segment_path()
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
                c = HardwareModuleNp.Nodes.Node()
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
        path_buffer = "Cisco-IOS-XR-asr9k-np-oper:hardware-module-np" + path_buffer

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
                self.nodes = HardwareModuleNp.Nodes()
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
        self._top_entity = HardwareModuleNp()
        return self._top_entity

