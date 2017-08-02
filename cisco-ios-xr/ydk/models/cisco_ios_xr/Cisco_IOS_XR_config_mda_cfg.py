""" Cisco_IOS_XR_config_mda_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR config\-mda package configuration.

This module contains definitions
for the following management objects\:
  active\-nodes\: Per\-node configuration for active nodes
  preconfigured\-nodes\: preconfigured nodes

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class ActiveNodes(Entity):
    """
    Per\-node configuration for active nodes
    
    .. attribute:: active_node
    
    	The configuration for an active node
    	**type**\: list of    :py:class:`ActiveNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode>`
    
    

    """

    _prefix = 'config-mda-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(ActiveNodes, self).__init__()
        self._top_entity = None

        self.yang_name = "active-nodes"
        self.yang_parent_name = "Cisco-IOS-XR-config-mda-cfg"

        self.active_node = YList(self)

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
                    super(ActiveNodes, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(ActiveNodes, self).__setattr__(name, value)


    class ActiveNode(Entity):
        """
        The configuration for an active node
        
        .. attribute:: node_name  <key>
        
        	The identifier for this node
        	**type**\:  str
        
        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
        
        .. attribute:: cisco_ios_xr_watchd_cfg_watchdog_node_threshold
        
        	watchdog node threshold
        	**type**\:   :py:class:`CiscoIosXrWatchdCfg_WatchdogNodeThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.CiscoIosXrWatchdCfg_WatchdogNodeThreshold>`
        
        .. attribute:: cisco_ios_xr_wd_cfg_watchdog_node_threshold
        
        	Watchdog threshold configuration
        	**type**\:   :py:class:`CiscoIosXrWdCfg_WatchdogNodeThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.CiscoIosXrWdCfg_WatchdogNodeThreshold>`
        
        .. attribute:: lpts_local
        
        	lpts node specific configuration commands
        	**type**\:   :py:class:`LptsLocal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal>`
        
        .. attribute:: ltrace
        
        	Ltrace Memory configuration
        	**type**\:   :py:class:`Ltrace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.Ltrace>`
        
        .. attribute:: ssrp_group
        
        	Per\-node SSRP configuration data
        	**type**\:   :py:class:`SsrpGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.SsrpGroup>`
        
        

        """

        _prefix = 'config-mda-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(ActiveNodes.ActiveNode, self).__init__()

            self.yang_name = "active-node"
            self.yang_parent_name = "active-nodes"

            self.node_name = YLeaf(YType.str, "node-name")

            self.cisco_ios_xr_watchd_cfg_watchdog_node_threshold = ActiveNodes.ActiveNode.CiscoIosXrWatchdCfg_WatchdogNodeThreshold()
            self.cisco_ios_xr_watchd_cfg_watchdog_node_threshold.parent = self
            self._children_name_map["cisco_ios_xr_watchd_cfg_watchdog_node_threshold"] = "Cisco-IOS-XR-watchd-cfg_watchdog-node-threshold"
            self._children_yang_names.add("Cisco-IOS-XR-watchd-cfg_watchdog-node-threshold")

            self.cisco_ios_xr_wd_cfg_watchdog_node_threshold = ActiveNodes.ActiveNode.CiscoIosXrWdCfg_WatchdogNodeThreshold()
            self.cisco_ios_xr_wd_cfg_watchdog_node_threshold.parent = self
            self._children_name_map["cisco_ios_xr_wd_cfg_watchdog_node_threshold"] = "Cisco-IOS-XR-wd-cfg_watchdog-node-threshold"
            self._children_yang_names.add("Cisco-IOS-XR-wd-cfg_watchdog-node-threshold")

            self.lpts_local = ActiveNodes.ActiveNode.LptsLocal()
            self.lpts_local.parent = self
            self._children_name_map["lpts_local"] = "lpts-local"
            self._children_yang_names.add("lpts-local")

            self.ltrace = ActiveNodes.ActiveNode.Ltrace()
            self.ltrace.parent = self
            self._children_name_map["ltrace"] = "ltrace"
            self._children_yang_names.add("ltrace")

            self.ssrp_group = ActiveNodes.ActiveNode.SsrpGroup()
            self.ssrp_group.parent = self
            self._children_name_map["ssrp_group"] = "ssrp-group"
            self._children_yang_names.add("ssrp-group")

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
                        super(ActiveNodes.ActiveNode, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(ActiveNodes.ActiveNode, self).__setattr__(name, value)


        class Ltrace(Entity):
            """
            Ltrace Memory configuration
            
            .. attribute:: allocation_params
            
            	Select Ltrace mode and scale\-factor
            	**type**\:   :py:class:`AllocationParams <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.Ltrace.AllocationParams>`
            
            

            """

            _prefix = 'infra-ltrace-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(ActiveNodes.ActiveNode.Ltrace, self).__init__()

                self.yang_name = "ltrace"
                self.yang_parent_name = "active-node"

                self.allocation_params = ActiveNodes.ActiveNode.Ltrace.AllocationParams()
                self.allocation_params.parent = self
                self._children_name_map["allocation_params"] = "allocation-params"
                self._children_yang_names.add("allocation-params")


            class AllocationParams(Entity):
                """
                Select Ltrace mode and scale\-factor
                
                .. attribute:: mode
                
                	Select an allocation mode (static\:1, dynamic \:2)
                	**type**\:   :py:class:`InfraLtraceMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_ltrace_cfg.InfraLtraceMode>`
                
                .. attribute:: scale_factor
                
                	Select a scaling down factor
                	**type**\:   :py:class:`InfraLtraceScale <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_ltrace_cfg.InfraLtraceScale>`
                
                

                """

                _prefix = 'infra-ltrace-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ActiveNodes.ActiveNode.Ltrace.AllocationParams, self).__init__()

                    self.yang_name = "allocation-params"
                    self.yang_parent_name = "ltrace"

                    self.mode = YLeaf(YType.enumeration, "mode")

                    self.scale_factor = YLeaf(YType.enumeration, "scale-factor")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("mode",
                                    "scale_factor") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(ActiveNodes.ActiveNode.Ltrace.AllocationParams, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(ActiveNodes.ActiveNode.Ltrace.AllocationParams, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.mode.is_set or
                        self.scale_factor.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.mode.yfilter != YFilter.not_set or
                        self.scale_factor.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "allocation-params" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.mode.is_set or self.mode.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.mode.get_name_leafdata())
                    if (self.scale_factor.is_set or self.scale_factor.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.scale_factor.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "mode" or name == "scale-factor"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "mode"):
                        self.mode = value
                        self.mode.value_namespace = name_space
                        self.mode.value_namespace_prefix = name_space_prefix
                    if(value_path == "scale-factor"):
                        self.scale_factor = value
                        self.scale_factor.value_namespace = name_space
                        self.scale_factor.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (self.allocation_params is not None and self.allocation_params.has_data())

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.allocation_params is not None and self.allocation_params.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "Cisco-IOS-XR-infra-ltrace-cfg:ltrace" + path_buffer

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

                if (child_yang_name == "allocation-params"):
                    if (self.allocation_params is None):
                        self.allocation_params = ActiveNodes.ActiveNode.Ltrace.AllocationParams()
                        self.allocation_params.parent = self
                        self._children_name_map["allocation_params"] = "allocation-params"
                    return self.allocation_params

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "allocation-params"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class LptsLocal(Entity):
            """
            lpts node specific configuration commands
            
            .. attribute:: ipolicer_local
            
            	Node specific Pre IFIB (Internal Forwarding Information Base) Configuration
            	**type**\:   :py:class:`IpolicerLocal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal>`
            
            	**presence node**\: True
            
            .. attribute:: ipolicer_local_tables
            
            	Node specific Pre IFIB (Internal Forwarding Information Base) Configuration
            	**type**\:   :py:class:`IpolicerLocalTables <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables>`
            
            

            """

            _prefix = 'lpts-pre-ifib-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(ActiveNodes.ActiveNode.LptsLocal, self).__init__()

                self.yang_name = "lpts-local"
                self.yang_parent_name = "active-node"

                self.ipolicer_local = None
                self._children_name_map["ipolicer_local"] = "ipolicer-local"
                self._children_yang_names.add("ipolicer-local")

                self.ipolicer_local_tables = ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables()
                self.ipolicer_local_tables.parent = self
                self._children_name_map["ipolicer_local_tables"] = "ipolicer-local-tables"
                self._children_yang_names.add("ipolicer-local-tables")


            class IpolicerLocalTables(Entity):
                """
                Node specific Pre IFIB (Internal Forwarding
                Information Base) Configuration
                
                .. attribute:: ipolicer_local_table
                
                	Pre IFIB (Internal Forwarding Information Base) configuration table
                	**type**\: list of    :py:class:`IpolicerLocalTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable>`
                
                

                """

                _prefix = 'lpts-pre-ifib-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables, self).__init__()

                    self.yang_name = "ipolicer-local-tables"
                    self.yang_parent_name = "lpts-local"

                    self.ipolicer_local_table = YList(self)

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
                                super(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables, self).__setattr__(name, value)


                class IpolicerLocalTable(Entity):
                    """
                    Pre IFIB (Internal Forwarding Information
                    Base) configuration table
                    
                    .. attribute:: id1  <key>
                    
                    	none
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: nps
                    
                    	NP name
                    	**type**\:   :py:class:`Nps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps>`
                    
                    

                    """

                    _prefix = 'lpts-pre-ifib-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable, self).__init__()

                        self.yang_name = "ipolicer-local-table"
                        self.yang_parent_name = "ipolicer-local-tables"

                        self.id1 = YLeaf(YType.str, "id1")

                        self.nps = ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps()
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
                            if name in ("id1") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable, self).__setattr__(name, value)


                    class Nps(Entity):
                        """
                        NP name
                        
                        .. attribute:: np
                        
                        	Table of NP names
                        	**type**\: list of    :py:class:`Np <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps.Np>`
                        
                        

                        """

                        _prefix = 'lpts-pre-ifib-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps, self).__init__()

                            self.yang_name = "nps"
                            self.yang_parent_name = "ipolicer-local-table"

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
                                        super(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps, self).__setattr__(name, value)


                        class Np(Entity):
                            """
                            Table of NP names
                            
                            .. attribute:: id1  <key>
                            
                            	none
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: rate
                            
                            	Packets per second
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**units**\: packet/s
                            
                            

                            """

                            _prefix = 'lpts-pre-ifib-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps.Np, self).__init__()

                                self.yang_name = "np"
                                self.yang_parent_name = "nps"

                                self.id1 = YLeaf(YType.int32, "id1")

                                self.rate = YLeaf(YType.int32, "rate")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("id1",
                                                "rate") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps.Np, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps.Np, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.id1.is_set or
                                    self.rate.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.id1.yfilter != YFilter.not_set or
                                    self.rate.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "np" + "[id1='" + self.id1.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.id1.is_set or self.id1.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.id1.get_name_leafdata())
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
                                if(name == "id1" or name == "rate"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "id1"):
                                    self.id1 = value
                                    self.id1.value_namespace = name_space
                                    self.id1.value_namespace_prefix = name_space_prefix
                                if(value_path == "rate"):
                                    self.rate = value
                                    self.rate.value_namespace = name_space
                                    self.rate.value_namespace_prefix = name_space_prefix

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
                                c = ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps.Np()
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
                            self.id1.is_set or
                            (self.nps is not None and self.nps.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.id1.yfilter != YFilter.not_set or
                            (self.nps is not None and self.nps.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ipolicer-local-table" + "[id1='" + self.id1.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.id1.is_set or self.id1.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.id1.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "nps"):
                            if (self.nps is None):
                                self.nps = ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps()
                                self.nps.parent = self
                                self._children_name_map["nps"] = "nps"
                            return self.nps

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "nps" or name == "id1"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "id1"):
                            self.id1 = value
                            self.id1.value_namespace = name_space
                            self.id1.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.ipolicer_local_table:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.ipolicer_local_table:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "ipolicer-local-tables" + path_buffer

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

                    if (child_yang_name == "ipolicer-local-table"):
                        for c in self.ipolicer_local_table:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.ipolicer_local_table.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "ipolicer-local-table"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class IpolicerLocal(Entity):
                """
                Node specific Pre IFIB (Internal Forwarding
                Information Base) Configuration
                
                .. attribute:: enable
                
                	Enabled
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                	**mandatory**\: True
                
                .. attribute:: flows
                
                	Table for Flows
                	**type**\:   :py:class:`Flows <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows>`
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'lpts-pre-ifib-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal, self).__init__()

                    self.yang_name = "ipolicer-local"
                    self.yang_parent_name = "lpts-local"
                    self.is_presence_container = True

                    self.enable = YLeaf(YType.empty, "enable")

                    self.flows = ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows()
                    self.flows.parent = self
                    self._children_name_map["flows"] = "flows"
                    self._children_yang_names.add("flows")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("enable") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal, self).__setattr__(name, value)


                class Flows(Entity):
                    """
                    Table for Flows
                    
                    .. attribute:: flow
                    
                    	selected flow type
                    	**type**\: list of    :py:class:`Flow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows.Flow>`
                    
                    

                    """

                    _prefix = 'lpts-pre-ifib-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows, self).__init__()

                        self.yang_name = "flows"
                        self.yang_parent_name = "ipolicer-local"

                        self.flow = YList(self)

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
                                    super(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows, self).__setattr__(name, value)


                    class Flow(Entity):
                        """
                        selected flow type
                        
                        .. attribute:: flow_type  <key>
                        
                        	LPTS Flow Type
                        	**type**\:   :py:class:`LptsFlow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg.LptsFlow>`
                        
                        .. attribute:: precedences
                        
                        	TOS Precedence value(s)
                        	**type**\:   :py:class:`Precedences <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows.Flow.Precedences>`
                        
                        .. attribute:: rate
                        
                        	Configured rate value
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        

                        """

                        _prefix = 'lpts-pre-ifib-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows.Flow, self).__init__()

                            self.yang_name = "flow"
                            self.yang_parent_name = "flows"

                            self.flow_type = YLeaf(YType.enumeration, "flow-type")

                            self.rate = YLeaf(YType.int32, "rate")

                            self.precedences = ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows.Flow.Precedences()
                            self.precedences.parent = self
                            self._children_name_map["precedences"] = "precedences"
                            self._children_yang_names.add("precedences")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("flow_type",
                                            "rate") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows.Flow, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows.Flow, self).__setattr__(name, value)


                        class Precedences(Entity):
                            """
                            TOS Precedence value(s)
                            
                            .. attribute:: precedence
                            
                            	Precedence values
                            	**type**\: one of the below types:
                            
                            	**type**\:  list of   :py:class:`LptsPreIFibPrecedenceNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg.LptsPreIFibPrecedenceNumber>`
                            
                            
                            ----
                            	**type**\:  list of int
                            
                            	**range:** 0..7
                            
                            
                            ----
                            

                            """

                            _prefix = 'lpts-pre-ifib-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows.Flow.Precedences, self).__init__()

                                self.yang_name = "precedences"
                                self.yang_parent_name = "flow"

                                self.precedence = YLeafList(YType.str, "precedence")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("precedence") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows.Flow.Precedences, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows.Flow.Precedences, self).__setattr__(name, value)

                            def has_data(self):
                                for leaf in self.precedence.getYLeafs():
                                    if (leaf.yfilter != YFilter.not_set):
                                        return True
                                return False

                            def has_operation(self):
                                for leaf in self.precedence.getYLeafs():
                                    if (leaf.is_set):
                                        return True
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.precedence.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "precedences" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()

                                leaf_name_data.extend(self.precedence.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "precedence"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "precedence"):
                                    self.precedence.append(value)

                        def has_data(self):
                            return (
                                self.flow_type.is_set or
                                self.rate.is_set or
                                (self.precedences is not None and self.precedences.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.flow_type.yfilter != YFilter.not_set or
                                self.rate.yfilter != YFilter.not_set or
                                (self.precedences is not None and self.precedences.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "flow" + "[flow-type='" + self.flow_type.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.flow_type.is_set or self.flow_type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.flow_type.get_name_leafdata())
                            if (self.rate.is_set or self.rate.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.rate.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "precedences"):
                                if (self.precedences is None):
                                    self.precedences = ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows.Flow.Precedences()
                                    self.precedences.parent = self
                                    self._children_name_map["precedences"] = "precedences"
                                return self.precedences

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "precedences" or name == "flow-type" or name == "rate"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "flow-type"):
                                self.flow_type = value
                                self.flow_type.value_namespace = name_space
                                self.flow_type.value_namespace_prefix = name_space_prefix
                            if(value_path == "rate"):
                                self.rate = value
                                self.rate.value_namespace = name_space
                                self.rate.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.flow:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.flow:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "flows" + path_buffer

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

                        if (child_yang_name == "flow"):
                            for c in self.flow:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows.Flow()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.flow.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "flow"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        self.enable.is_set or
                        (self.flows is not None and self.flows.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.enable.yfilter != YFilter.not_set or
                        (self.flows is not None and self.flows.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "ipolicer-local" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.enable.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "flows"):
                        if (self.flows is None):
                            self.flows = ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows()
                            self.flows.parent = self
                            self._children_name_map["flows"] = "flows"
                        return self.flows

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "flows" or name == "enable"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "enable"):
                        self.enable = value
                        self.enable.value_namespace = name_space
                        self.enable.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    (self.ipolicer_local_tables is not None and self.ipolicer_local_tables.has_data()) or
                    (self.ipolicer_local is not None))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.ipolicer_local is not None and self.ipolicer_local.has_operation()) or
                    (self.ipolicer_local_tables is not None and self.ipolicer_local_tables.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "Cisco-IOS-XR-lpts-pre-ifib-cfg:lpts-local" + path_buffer

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

                if (child_yang_name == "ipolicer-local"):
                    if (self.ipolicer_local is None):
                        self.ipolicer_local = ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal()
                        self.ipolicer_local.parent = self
                        self._children_name_map["ipolicer_local"] = "ipolicer-local"
                    return self.ipolicer_local

                if (child_yang_name == "ipolicer-local-tables"):
                    if (self.ipolicer_local_tables is None):
                        self.ipolicer_local_tables = ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables()
                        self.ipolicer_local_tables.parent = self
                        self._children_name_map["ipolicer_local_tables"] = "ipolicer-local-tables"
                    return self.ipolicer_local_tables

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ipolicer-local" or name == "ipolicer-local-tables"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class SsrpGroup(Entity):
            """
            Per\-node SSRP configuration data
            
            .. attribute:: groups
            
            	Table of SSRP Group configuration
            	**type**\:   :py:class:`Groups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.SsrpGroup.Groups>`
            
            

            """

            _prefix = 'ppp-ma-ssrp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(ActiveNodes.ActiveNode.SsrpGroup, self).__init__()

                self.yang_name = "ssrp-group"
                self.yang_parent_name = "active-node"

                self.groups = ActiveNodes.ActiveNode.SsrpGroup.Groups()
                self.groups.parent = self
                self._children_name_map["groups"] = "groups"
                self._children_yang_names.add("groups")


            class Groups(Entity):
                """
                Table of SSRP Group configuration
                
                .. attribute:: group
                
                	SSRP Group configuration
                	**type**\: list of    :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.SsrpGroup.Groups.Group>`
                
                

                """

                _prefix = 'ppp-ma-ssrp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ActiveNodes.ActiveNode.SsrpGroup.Groups, self).__init__()

                    self.yang_name = "groups"
                    self.yang_parent_name = "ssrp-group"

                    self.group = YList(self)

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
                                super(ActiveNodes.ActiveNode.SsrpGroup.Groups, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(ActiveNodes.ActiveNode.SsrpGroup.Groups, self).__setattr__(name, value)


                class Group(Entity):
                    """
                    SSRP Group configuration
                    
                    .. attribute:: group_id  <key>
                    
                    	The identifier for this group
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    .. attribute:: profile
                    
                    	This specifies the SSRP profile to use for this group
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'ppp-ma-ssrp-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ActiveNodes.ActiveNode.SsrpGroup.Groups.Group, self).__init__()

                        self.yang_name = "group"
                        self.yang_parent_name = "groups"

                        self.group_id = YLeaf(YType.uint32, "group-id")

                        self.profile = YLeaf(YType.str, "profile")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("group_id",
                                        "profile") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ActiveNodes.ActiveNode.SsrpGroup.Groups.Group, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ActiveNodes.ActiveNode.SsrpGroup.Groups.Group, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.group_id.is_set or
                            self.profile.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.group_id.yfilter != YFilter.not_set or
                            self.profile.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "group" + "[group-id='" + self.group_id.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.group_id.is_set or self.group_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.group_id.get_name_leafdata())
                        if (self.profile.is_set or self.profile.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.profile.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "group-id" or name == "profile"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "group-id"):
                            self.group_id = value
                            self.group_id.value_namespace = name_space
                            self.group_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "profile"):
                            self.profile = value
                            self.profile.value_namespace = name_space
                            self.profile.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.group:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.group:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "groups" + path_buffer

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

                    if (child_yang_name == "group"):
                        for c in self.group:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = ActiveNodes.ActiveNode.SsrpGroup.Groups.Group()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.group.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "group"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (self.groups is not None and self.groups.has_data())

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.groups is not None and self.groups.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "Cisco-IOS-XR-ppp-ma-ssrp-cfg:ssrp-group" + path_buffer

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

                if (child_yang_name == "groups"):
                    if (self.groups is None):
                        self.groups = ActiveNodes.ActiveNode.SsrpGroup.Groups()
                        self.groups.parent = self
                        self._children_name_map["groups"] = "groups"
                    return self.groups

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "groups"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class CiscoIosXrWatchdCfg_WatchdogNodeThreshold(Entity):
            """
            watchdog node threshold
            
            .. attribute:: memory_threshold
            
            	Memory thresholds
            	**type**\:   :py:class:`MemoryThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.CiscoIosXrWatchdCfg_WatchdogNodeThreshold.MemoryThreshold>`
            
            

            """

            _prefix = 'watchd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(ActiveNodes.ActiveNode.CiscoIosXrWatchdCfg_WatchdogNodeThreshold, self).__init__()

                self.yang_name = "Cisco-IOS-XR-watchd-cfg_watchdog-node-threshold"
                self.yang_parent_name = "active-node"

                self.memory_threshold = ActiveNodes.ActiveNode.CiscoIosXrWatchdCfg_WatchdogNodeThreshold.MemoryThreshold()
                self.memory_threshold.parent = self
                self._children_name_map["memory_threshold"] = "memory-threshold"
                self._children_yang_names.add("memory-threshold")


            class MemoryThreshold(Entity):
                """
                Memory thresholds
                
                .. attribute:: critical
                
                	Threshold, Range(3, severe)
                	**type**\:  int
                
                	**range:** 3..40
                
                .. attribute:: minor
                
                	Threshold, Range(5, 40)
                	**type**\:  int
                
                	**range:** 5..40
                
                .. attribute:: severe
                
                	Threshold, Range(4, minor)
                	**type**\:  int
                
                	**range:** 4..40
                
                

                """

                _prefix = 'watchd-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ActiveNodes.ActiveNode.CiscoIosXrWatchdCfg_WatchdogNodeThreshold.MemoryThreshold, self).__init__()

                    self.yang_name = "memory-threshold"
                    self.yang_parent_name = "Cisco-IOS-XR-watchd-cfg_watchdog-node-threshold"

                    self.critical = YLeaf(YType.uint32, "critical")

                    self.minor = YLeaf(YType.uint32, "minor")

                    self.severe = YLeaf(YType.uint32, "severe")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("critical",
                                    "minor",
                                    "severe") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(ActiveNodes.ActiveNode.CiscoIosXrWatchdCfg_WatchdogNodeThreshold.MemoryThreshold, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(ActiveNodes.ActiveNode.CiscoIosXrWatchdCfg_WatchdogNodeThreshold.MemoryThreshold, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.critical.is_set or
                        self.minor.is_set or
                        self.severe.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.critical.yfilter != YFilter.not_set or
                        self.minor.yfilter != YFilter.not_set or
                        self.severe.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "memory-threshold" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.critical.is_set or self.critical.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.critical.get_name_leafdata())
                    if (self.minor.is_set or self.minor.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.minor.get_name_leafdata())
                    if (self.severe.is_set or self.severe.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.severe.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "critical" or name == "minor" or name == "severe"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "critical"):
                        self.critical = value
                        self.critical.value_namespace = name_space
                        self.critical.value_namespace_prefix = name_space_prefix
                    if(value_path == "minor"):
                        self.minor = value
                        self.minor.value_namespace = name_space
                        self.minor.value_namespace_prefix = name_space_prefix
                    if(value_path == "severe"):
                        self.severe = value
                        self.severe.value_namespace = name_space
                        self.severe.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (self.memory_threshold is not None and self.memory_threshold.has_data())

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.memory_threshold is not None and self.memory_threshold.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "Cisco-IOS-XR-watchd-cfg:Cisco-IOS-XR-watchd-cfg_watchdog-node-threshold" + path_buffer

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

                if (child_yang_name == "memory-threshold"):
                    if (self.memory_threshold is None):
                        self.memory_threshold = ActiveNodes.ActiveNode.CiscoIosXrWatchdCfg_WatchdogNodeThreshold.MemoryThreshold()
                        self.memory_threshold.parent = self
                        self._children_name_map["memory_threshold"] = "memory-threshold"
                    return self.memory_threshold

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "memory-threshold"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class CiscoIosXrWdCfg_WatchdogNodeThreshold(Entity):
            """
            Watchdog threshold configuration
            
            .. attribute:: memory_threshold
            
            	Memory thresholds
            	**type**\:   :py:class:`MemoryThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.CiscoIosXrWdCfg_WatchdogNodeThreshold.MemoryThreshold>`
            
            

            """

            _prefix = 'wd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(ActiveNodes.ActiveNode.CiscoIosXrWdCfg_WatchdogNodeThreshold, self).__init__()

                self.yang_name = "Cisco-IOS-XR-wd-cfg_watchdog-node-threshold"
                self.yang_parent_name = "active-node"

                self.memory_threshold = ActiveNodes.ActiveNode.CiscoIosXrWdCfg_WatchdogNodeThreshold.MemoryThreshold()
                self.memory_threshold.parent = self
                self._children_name_map["memory_threshold"] = "memory-threshold"
                self._children_yang_names.add("memory-threshold")


            class MemoryThreshold(Entity):
                """
                Memory thresholds
                
                .. attribute:: critical
                
                	Threshold, Range(3, severe)
                	**type**\:  int
                
                	**range:** 3..40
                
                .. attribute:: minor
                
                	Threshold, Range(5, 40)
                	**type**\:  int
                
                	**range:** 5..40
                
                .. attribute:: severe
                
                	Threshold, Range(4, minor)
                	**type**\:  int
                
                	**range:** 4..40
                
                

                """

                _prefix = 'wd-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ActiveNodes.ActiveNode.CiscoIosXrWdCfg_WatchdogNodeThreshold.MemoryThreshold, self).__init__()

                    self.yang_name = "memory-threshold"
                    self.yang_parent_name = "Cisco-IOS-XR-wd-cfg_watchdog-node-threshold"

                    self.critical = YLeaf(YType.uint32, "critical")

                    self.minor = YLeaf(YType.uint32, "minor")

                    self.severe = YLeaf(YType.uint32, "severe")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("critical",
                                    "minor",
                                    "severe") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(ActiveNodes.ActiveNode.CiscoIosXrWdCfg_WatchdogNodeThreshold.MemoryThreshold, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(ActiveNodes.ActiveNode.CiscoIosXrWdCfg_WatchdogNodeThreshold.MemoryThreshold, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.critical.is_set or
                        self.minor.is_set or
                        self.severe.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.critical.yfilter != YFilter.not_set or
                        self.minor.yfilter != YFilter.not_set or
                        self.severe.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "memory-threshold" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.critical.is_set or self.critical.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.critical.get_name_leafdata())
                    if (self.minor.is_set or self.minor.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.minor.get_name_leafdata())
                    if (self.severe.is_set or self.severe.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.severe.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "critical" or name == "minor" or name == "severe"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "critical"):
                        self.critical = value
                        self.critical.value_namespace = name_space
                        self.critical.value_namespace_prefix = name_space_prefix
                    if(value_path == "minor"):
                        self.minor = value
                        self.minor.value_namespace = name_space
                        self.minor.value_namespace_prefix = name_space_prefix
                    if(value_path == "severe"):
                        self.severe = value
                        self.severe.value_namespace = name_space
                        self.severe.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (self.memory_threshold is not None and self.memory_threshold.has_data())

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.memory_threshold is not None and self.memory_threshold.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "Cisco-IOS-XR-wd-cfg:Cisco-IOS-XR-wd-cfg_watchdog-node-threshold" + path_buffer

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

                if (child_yang_name == "memory-threshold"):
                    if (self.memory_threshold is None):
                        self.memory_threshold = ActiveNodes.ActiveNode.CiscoIosXrWdCfg_WatchdogNodeThreshold.MemoryThreshold()
                        self.memory_threshold.parent = self
                        self._children_name_map["memory_threshold"] = "memory-threshold"
                    return self.memory_threshold

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "memory-threshold"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                self.node_name.is_set or
                (self.cisco_ios_xr_watchd_cfg_watchdog_node_threshold is not None and self.cisco_ios_xr_watchd_cfg_watchdog_node_threshold.has_data()) or
                (self.cisco_ios_xr_wd_cfg_watchdog_node_threshold is not None and self.cisco_ios_xr_wd_cfg_watchdog_node_threshold.has_data()) or
                (self.lpts_local is not None and self.lpts_local.has_data()) or
                (self.ltrace is not None and self.ltrace.has_data()) or
                (self.ssrp_group is not None and self.ssrp_group.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.node_name.yfilter != YFilter.not_set or
                (self.cisco_ios_xr_watchd_cfg_watchdog_node_threshold is not None and self.cisco_ios_xr_watchd_cfg_watchdog_node_threshold.has_operation()) or
                (self.cisco_ios_xr_wd_cfg_watchdog_node_threshold is not None and self.cisco_ios_xr_wd_cfg_watchdog_node_threshold.has_operation()) or
                (self.lpts_local is not None and self.lpts_local.has_operation()) or
                (self.ltrace is not None and self.ltrace.has_operation()) or
                (self.ssrp_group is not None and self.ssrp_group.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "active-node" + "[node-name='" + self.node_name.get() + "']" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-config-mda-cfg:active-nodes/%s" % self.get_segment_path()
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

            if (child_yang_name == "Cisco-IOS-XR-watchd-cfg_watchdog-node-threshold"):
                if (self.cisco_ios_xr_watchd_cfg_watchdog_node_threshold is None):
                    self.cisco_ios_xr_watchd_cfg_watchdog_node_threshold = ActiveNodes.ActiveNode.CiscoIosXrWatchdCfg_WatchdogNodeThreshold()
                    self.cisco_ios_xr_watchd_cfg_watchdog_node_threshold.parent = self
                    self._children_name_map["cisco_ios_xr_watchd_cfg_watchdog_node_threshold"] = "Cisco-IOS-XR-watchd-cfg_watchdog-node-threshold"
                return self.cisco_ios_xr_watchd_cfg_watchdog_node_threshold

            if (child_yang_name == "Cisco-IOS-XR-wd-cfg_watchdog-node-threshold"):
                if (self.cisco_ios_xr_wd_cfg_watchdog_node_threshold is None):
                    self.cisco_ios_xr_wd_cfg_watchdog_node_threshold = ActiveNodes.ActiveNode.CiscoIosXrWdCfg_WatchdogNodeThreshold()
                    self.cisco_ios_xr_wd_cfg_watchdog_node_threshold.parent = self
                    self._children_name_map["cisco_ios_xr_wd_cfg_watchdog_node_threshold"] = "Cisco-IOS-XR-wd-cfg_watchdog-node-threshold"
                return self.cisco_ios_xr_wd_cfg_watchdog_node_threshold

            if (child_yang_name == "lpts-local"):
                if (self.lpts_local is None):
                    self.lpts_local = ActiveNodes.ActiveNode.LptsLocal()
                    self.lpts_local.parent = self
                    self._children_name_map["lpts_local"] = "lpts-local"
                return self.lpts_local

            if (child_yang_name == "ltrace"):
                if (self.ltrace is None):
                    self.ltrace = ActiveNodes.ActiveNode.Ltrace()
                    self.ltrace.parent = self
                    self._children_name_map["ltrace"] = "ltrace"
                return self.ltrace

            if (child_yang_name == "ssrp-group"):
                if (self.ssrp_group is None):
                    self.ssrp_group = ActiveNodes.ActiveNode.SsrpGroup()
                    self.ssrp_group.parent = self
                    self._children_name_map["ssrp_group"] = "ssrp-group"
                return self.ssrp_group

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "Cisco-IOS-XR-watchd-cfg_watchdog-node-threshold" or name == "Cisco-IOS-XR-wd-cfg_watchdog-node-threshold" or name == "lpts-local" or name == "ltrace" or name == "ssrp-group" or name == "node-name"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "node-name"):
                self.node_name = value
                self.node_name.value_namespace = name_space
                self.node_name.value_namespace_prefix = name_space_prefix

    def has_data(self):
        for c in self.active_node:
            if (c.has_data()):
                return True
        return False

    def has_operation(self):
        for c in self.active_node:
            if (c.has_operation()):
                return True
        return self.yfilter != YFilter.not_set

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-config-mda-cfg:active-nodes" + path_buffer

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

        if (child_yang_name == "active-node"):
            for c in self.active_node:
                segment = c.get_segment_path()
                if (segment_path == segment):
                    return c
            c = ActiveNodes.ActiveNode()
            c.parent = self
            local_reference_key = "ydk::seg::%s" % segment_path
            self._local_refs[local_reference_key] = c
            self.active_node.append(c)
            return c

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "active-node"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = ActiveNodes()
        return self._top_entity

class PreconfiguredNodes(Entity):
    """
    preconfigured nodes
    
    .. attribute:: preconfigured_node
    
    	The configuration for a non\-active node
    	**type**\: list of    :py:class:`PreconfiguredNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode>`
    
    

    """

    _prefix = 'config-mda-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(PreconfiguredNodes, self).__init__()
        self._top_entity = None

        self.yang_name = "preconfigured-nodes"
        self.yang_parent_name = "Cisco-IOS-XR-config-mda-cfg"

        self.preconfigured_node = YList(self)

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
                    super(PreconfiguredNodes, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(PreconfiguredNodes, self).__setattr__(name, value)


    class PreconfiguredNode(Entity):
        """
        The configuration for a non\-active node
        
        .. attribute:: node_name  <key>
        
        	The identifier for this node
        	**type**\:  str
        
        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
        
        .. attribute:: cisco_ios_xr_watchd_cfg_watchdog_node_threshold
        
        	watchdog node threshold
        	**type**\:   :py:class:`CiscoIosXrWatchdCfg_WatchdogNodeThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.CiscoIosXrWatchdCfg_WatchdogNodeThreshold>`
        
        .. attribute:: cisco_ios_xr_wd_cfg_watchdog_node_threshold
        
        	Watchdog threshold configuration
        	**type**\:   :py:class:`CiscoIosXrWdCfg_WatchdogNodeThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.CiscoIosXrWdCfg_WatchdogNodeThreshold>`
        
        .. attribute:: lpts_local
        
        	lpts node specific configuration commands
        	**type**\:   :py:class:`LptsLocal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal>`
        
        .. attribute:: ltrace
        
        	Ltrace Memory configuration
        	**type**\:   :py:class:`Ltrace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.Ltrace>`
        
        

        """

        _prefix = 'config-mda-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(PreconfiguredNodes.PreconfiguredNode, self).__init__()

            self.yang_name = "preconfigured-node"
            self.yang_parent_name = "preconfigured-nodes"

            self.node_name = YLeaf(YType.str, "node-name")

            self.cisco_ios_xr_watchd_cfg_watchdog_node_threshold = PreconfiguredNodes.PreconfiguredNode.CiscoIosXrWatchdCfg_WatchdogNodeThreshold()
            self.cisco_ios_xr_watchd_cfg_watchdog_node_threshold.parent = self
            self._children_name_map["cisco_ios_xr_watchd_cfg_watchdog_node_threshold"] = "Cisco-IOS-XR-watchd-cfg_watchdog-node-threshold"
            self._children_yang_names.add("Cisco-IOS-XR-watchd-cfg_watchdog-node-threshold")

            self.cisco_ios_xr_wd_cfg_watchdog_node_threshold = PreconfiguredNodes.PreconfiguredNode.CiscoIosXrWdCfg_WatchdogNodeThreshold()
            self.cisco_ios_xr_wd_cfg_watchdog_node_threshold.parent = self
            self._children_name_map["cisco_ios_xr_wd_cfg_watchdog_node_threshold"] = "Cisco-IOS-XR-wd-cfg_watchdog-node-threshold"
            self._children_yang_names.add("Cisco-IOS-XR-wd-cfg_watchdog-node-threshold")

            self.lpts_local = PreconfiguredNodes.PreconfiguredNode.LptsLocal()
            self.lpts_local.parent = self
            self._children_name_map["lpts_local"] = "lpts-local"
            self._children_yang_names.add("lpts-local")

            self.ltrace = PreconfiguredNodes.PreconfiguredNode.Ltrace()
            self.ltrace.parent = self
            self._children_name_map["ltrace"] = "ltrace"
            self._children_yang_names.add("ltrace")

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
                        super(PreconfiguredNodes.PreconfiguredNode, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(PreconfiguredNodes.PreconfiguredNode, self).__setattr__(name, value)


        class Ltrace(Entity):
            """
            Ltrace Memory configuration
            
            .. attribute:: allocation_params
            
            	Select Ltrace mode and scale\-factor
            	**type**\:   :py:class:`AllocationParams <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.Ltrace.AllocationParams>`
            
            

            """

            _prefix = 'infra-ltrace-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(PreconfiguredNodes.PreconfiguredNode.Ltrace, self).__init__()

                self.yang_name = "ltrace"
                self.yang_parent_name = "preconfigured-node"

                self.allocation_params = PreconfiguredNodes.PreconfiguredNode.Ltrace.AllocationParams()
                self.allocation_params.parent = self
                self._children_name_map["allocation_params"] = "allocation-params"
                self._children_yang_names.add("allocation-params")


            class AllocationParams(Entity):
                """
                Select Ltrace mode and scale\-factor
                
                .. attribute:: mode
                
                	Select an allocation mode (static\:1, dynamic \:2)
                	**type**\:   :py:class:`InfraLtraceMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_ltrace_cfg.InfraLtraceMode>`
                
                .. attribute:: scale_factor
                
                	Select a scaling down factor
                	**type**\:   :py:class:`InfraLtraceScale <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_ltrace_cfg.InfraLtraceScale>`
                
                

                """

                _prefix = 'infra-ltrace-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(PreconfiguredNodes.PreconfiguredNode.Ltrace.AllocationParams, self).__init__()

                    self.yang_name = "allocation-params"
                    self.yang_parent_name = "ltrace"

                    self.mode = YLeaf(YType.enumeration, "mode")

                    self.scale_factor = YLeaf(YType.enumeration, "scale-factor")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("mode",
                                    "scale_factor") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(PreconfiguredNodes.PreconfiguredNode.Ltrace.AllocationParams, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(PreconfiguredNodes.PreconfiguredNode.Ltrace.AllocationParams, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.mode.is_set or
                        self.scale_factor.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.mode.yfilter != YFilter.not_set or
                        self.scale_factor.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "allocation-params" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.mode.is_set or self.mode.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.mode.get_name_leafdata())
                    if (self.scale_factor.is_set or self.scale_factor.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.scale_factor.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "mode" or name == "scale-factor"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "mode"):
                        self.mode = value
                        self.mode.value_namespace = name_space
                        self.mode.value_namespace_prefix = name_space_prefix
                    if(value_path == "scale-factor"):
                        self.scale_factor = value
                        self.scale_factor.value_namespace = name_space
                        self.scale_factor.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (self.allocation_params is not None and self.allocation_params.has_data())

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.allocation_params is not None and self.allocation_params.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "Cisco-IOS-XR-infra-ltrace-cfg:ltrace" + path_buffer

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

                if (child_yang_name == "allocation-params"):
                    if (self.allocation_params is None):
                        self.allocation_params = PreconfiguredNodes.PreconfiguredNode.Ltrace.AllocationParams()
                        self.allocation_params.parent = self
                        self._children_name_map["allocation_params"] = "allocation-params"
                    return self.allocation_params

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "allocation-params"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class LptsLocal(Entity):
            """
            lpts node specific configuration commands
            
            .. attribute:: ipolicer_local
            
            	Node specific Pre IFIB (Internal Forwarding Information Base) Configuration
            	**type**\:   :py:class:`IpolicerLocal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal>`
            
            	**presence node**\: True
            
            .. attribute:: ipolicer_local_tables
            
            	Node specific Pre IFIB (Internal Forwarding Information Base) Configuration
            	**type**\:   :py:class:`IpolicerLocalTables <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables>`
            
            

            """

            _prefix = 'lpts-pre-ifib-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(PreconfiguredNodes.PreconfiguredNode.LptsLocal, self).__init__()

                self.yang_name = "lpts-local"
                self.yang_parent_name = "preconfigured-node"

                self.ipolicer_local = None
                self._children_name_map["ipolicer_local"] = "ipolicer-local"
                self._children_yang_names.add("ipolicer-local")

                self.ipolicer_local_tables = PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables()
                self.ipolicer_local_tables.parent = self
                self._children_name_map["ipolicer_local_tables"] = "ipolicer-local-tables"
                self._children_yang_names.add("ipolicer-local-tables")


            class IpolicerLocalTables(Entity):
                """
                Node specific Pre IFIB (Internal Forwarding
                Information Base) Configuration
                
                .. attribute:: ipolicer_local_table
                
                	Pre IFIB (Internal Forwarding Information Base) configuration table
                	**type**\: list of    :py:class:`IpolicerLocalTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable>`
                
                

                """

                _prefix = 'lpts-pre-ifib-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables, self).__init__()

                    self.yang_name = "ipolicer-local-tables"
                    self.yang_parent_name = "lpts-local"

                    self.ipolicer_local_table = YList(self)

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
                                super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables, self).__setattr__(name, value)


                class IpolicerLocalTable(Entity):
                    """
                    Pre IFIB (Internal Forwarding Information
                    Base) configuration table
                    
                    .. attribute:: id1  <key>
                    
                    	none
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: nps
                    
                    	NP name
                    	**type**\:   :py:class:`Nps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps>`
                    
                    

                    """

                    _prefix = 'lpts-pre-ifib-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable, self).__init__()

                        self.yang_name = "ipolicer-local-table"
                        self.yang_parent_name = "ipolicer-local-tables"

                        self.id1 = YLeaf(YType.str, "id1")

                        self.nps = PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps()
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
                            if name in ("id1") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable, self).__setattr__(name, value)


                    class Nps(Entity):
                        """
                        NP name
                        
                        .. attribute:: np
                        
                        	Table of NP names
                        	**type**\: list of    :py:class:`Np <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps.Np>`
                        
                        

                        """

                        _prefix = 'lpts-pre-ifib-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps, self).__init__()

                            self.yang_name = "nps"
                            self.yang_parent_name = "ipolicer-local-table"

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
                                        super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps, self).__setattr__(name, value)


                        class Np(Entity):
                            """
                            Table of NP names
                            
                            .. attribute:: id1  <key>
                            
                            	none
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: rate
                            
                            	Packets per second
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**units**\: packet/s
                            
                            

                            """

                            _prefix = 'lpts-pre-ifib-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps.Np, self).__init__()

                                self.yang_name = "np"
                                self.yang_parent_name = "nps"

                                self.id1 = YLeaf(YType.int32, "id1")

                                self.rate = YLeaf(YType.int32, "rate")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("id1",
                                                "rate") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps.Np, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps.Np, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.id1.is_set or
                                    self.rate.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.id1.yfilter != YFilter.not_set or
                                    self.rate.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "np" + "[id1='" + self.id1.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.id1.is_set or self.id1.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.id1.get_name_leafdata())
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
                                if(name == "id1" or name == "rate"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "id1"):
                                    self.id1 = value
                                    self.id1.value_namespace = name_space
                                    self.id1.value_namespace_prefix = name_space_prefix
                                if(value_path == "rate"):
                                    self.rate = value
                                    self.rate.value_namespace = name_space
                                    self.rate.value_namespace_prefix = name_space_prefix

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
                                c = PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps.Np()
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
                            self.id1.is_set or
                            (self.nps is not None and self.nps.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.id1.yfilter != YFilter.not_set or
                            (self.nps is not None and self.nps.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ipolicer-local-table" + "[id1='" + self.id1.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.id1.is_set or self.id1.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.id1.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "nps"):
                            if (self.nps is None):
                                self.nps = PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps()
                                self.nps.parent = self
                                self._children_name_map["nps"] = "nps"
                            return self.nps

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "nps" or name == "id1"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "id1"):
                            self.id1 = value
                            self.id1.value_namespace = name_space
                            self.id1.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.ipolicer_local_table:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.ipolicer_local_table:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "ipolicer-local-tables" + path_buffer

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

                    if (child_yang_name == "ipolicer-local-table"):
                        for c in self.ipolicer_local_table:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.ipolicer_local_table.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "ipolicer-local-table"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class IpolicerLocal(Entity):
                """
                Node specific Pre IFIB (Internal Forwarding
                Information Base) Configuration
                
                .. attribute:: enable
                
                	Enabled
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                	**mandatory**\: True
                
                .. attribute:: flows
                
                	Table for Flows
                	**type**\:   :py:class:`Flows <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows>`
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'lpts-pre-ifib-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal, self).__init__()

                    self.yang_name = "ipolicer-local"
                    self.yang_parent_name = "lpts-local"
                    self.is_presence_container = True

                    self.enable = YLeaf(YType.empty, "enable")

                    self.flows = PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows()
                    self.flows.parent = self
                    self._children_name_map["flows"] = "flows"
                    self._children_yang_names.add("flows")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("enable") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal, self).__setattr__(name, value)


                class Flows(Entity):
                    """
                    Table for Flows
                    
                    .. attribute:: flow
                    
                    	selected flow type
                    	**type**\: list of    :py:class:`Flow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows.Flow>`
                    
                    

                    """

                    _prefix = 'lpts-pre-ifib-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows, self).__init__()

                        self.yang_name = "flows"
                        self.yang_parent_name = "ipolicer-local"

                        self.flow = YList(self)

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
                                    super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows, self).__setattr__(name, value)


                    class Flow(Entity):
                        """
                        selected flow type
                        
                        .. attribute:: flow_type  <key>
                        
                        	LPTS Flow Type
                        	**type**\:   :py:class:`LptsFlow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg.LptsFlow>`
                        
                        .. attribute:: precedences
                        
                        	TOS Precedence value(s)
                        	**type**\:   :py:class:`Precedences <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows.Flow.Precedences>`
                        
                        .. attribute:: rate
                        
                        	Configured rate value
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        

                        """

                        _prefix = 'lpts-pre-ifib-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows.Flow, self).__init__()

                            self.yang_name = "flow"
                            self.yang_parent_name = "flows"

                            self.flow_type = YLeaf(YType.enumeration, "flow-type")

                            self.rate = YLeaf(YType.int32, "rate")

                            self.precedences = PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows.Flow.Precedences()
                            self.precedences.parent = self
                            self._children_name_map["precedences"] = "precedences"
                            self._children_yang_names.add("precedences")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("flow_type",
                                            "rate") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows.Flow, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows.Flow, self).__setattr__(name, value)


                        class Precedences(Entity):
                            """
                            TOS Precedence value(s)
                            
                            .. attribute:: precedence
                            
                            	Precedence values
                            	**type**\: one of the below types:
                            
                            	**type**\:  list of   :py:class:`LptsPreIFibPrecedenceNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg.LptsPreIFibPrecedenceNumber>`
                            
                            
                            ----
                            	**type**\:  list of int
                            
                            	**range:** 0..7
                            
                            
                            ----
                            

                            """

                            _prefix = 'lpts-pre-ifib-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows.Flow.Precedences, self).__init__()

                                self.yang_name = "precedences"
                                self.yang_parent_name = "flow"

                                self.precedence = YLeafList(YType.str, "precedence")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("precedence") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows.Flow.Precedences, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows.Flow.Precedences, self).__setattr__(name, value)

                            def has_data(self):
                                for leaf in self.precedence.getYLeafs():
                                    if (leaf.yfilter != YFilter.not_set):
                                        return True
                                return False

                            def has_operation(self):
                                for leaf in self.precedence.getYLeafs():
                                    if (leaf.is_set):
                                        return True
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.precedence.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "precedences" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()

                                leaf_name_data.extend(self.precedence.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "precedence"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "precedence"):
                                    self.precedence.append(value)

                        def has_data(self):
                            return (
                                self.flow_type.is_set or
                                self.rate.is_set or
                                (self.precedences is not None and self.precedences.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.flow_type.yfilter != YFilter.not_set or
                                self.rate.yfilter != YFilter.not_set or
                                (self.precedences is not None and self.precedences.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "flow" + "[flow-type='" + self.flow_type.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.flow_type.is_set or self.flow_type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.flow_type.get_name_leafdata())
                            if (self.rate.is_set or self.rate.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.rate.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "precedences"):
                                if (self.precedences is None):
                                    self.precedences = PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows.Flow.Precedences()
                                    self.precedences.parent = self
                                    self._children_name_map["precedences"] = "precedences"
                                return self.precedences

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "precedences" or name == "flow-type" or name == "rate"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "flow-type"):
                                self.flow_type = value
                                self.flow_type.value_namespace = name_space
                                self.flow_type.value_namespace_prefix = name_space_prefix
                            if(value_path == "rate"):
                                self.rate = value
                                self.rate.value_namespace = name_space
                                self.rate.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.flow:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.flow:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "flows" + path_buffer

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

                        if (child_yang_name == "flow"):
                            for c in self.flow:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows.Flow()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.flow.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "flow"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        self.enable.is_set or
                        (self.flows is not None and self.flows.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.enable.yfilter != YFilter.not_set or
                        (self.flows is not None and self.flows.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "ipolicer-local" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.enable.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "flows"):
                        if (self.flows is None):
                            self.flows = PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows()
                            self.flows.parent = self
                            self._children_name_map["flows"] = "flows"
                        return self.flows

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "flows" or name == "enable"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "enable"):
                        self.enable = value
                        self.enable.value_namespace = name_space
                        self.enable.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    (self.ipolicer_local_tables is not None and self.ipolicer_local_tables.has_data()) or
                    (self.ipolicer_local is not None))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.ipolicer_local is not None and self.ipolicer_local.has_operation()) or
                    (self.ipolicer_local_tables is not None and self.ipolicer_local_tables.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "Cisco-IOS-XR-lpts-pre-ifib-cfg:lpts-local" + path_buffer

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

                if (child_yang_name == "ipolicer-local"):
                    if (self.ipolicer_local is None):
                        self.ipolicer_local = PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal()
                        self.ipolicer_local.parent = self
                        self._children_name_map["ipolicer_local"] = "ipolicer-local"
                    return self.ipolicer_local

                if (child_yang_name == "ipolicer-local-tables"):
                    if (self.ipolicer_local_tables is None):
                        self.ipolicer_local_tables = PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables()
                        self.ipolicer_local_tables.parent = self
                        self._children_name_map["ipolicer_local_tables"] = "ipolicer-local-tables"
                    return self.ipolicer_local_tables

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ipolicer-local" or name == "ipolicer-local-tables"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class CiscoIosXrWatchdCfg_WatchdogNodeThreshold(Entity):
            """
            watchdog node threshold
            
            .. attribute:: memory_threshold
            
            	Memory thresholds
            	**type**\:   :py:class:`MemoryThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.CiscoIosXrWatchdCfg_WatchdogNodeThreshold.MemoryThreshold>`
            
            

            """

            _prefix = 'watchd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(PreconfiguredNodes.PreconfiguredNode.CiscoIosXrWatchdCfg_WatchdogNodeThreshold, self).__init__()

                self.yang_name = "Cisco-IOS-XR-watchd-cfg_watchdog-node-threshold"
                self.yang_parent_name = "preconfigured-node"

                self.memory_threshold = PreconfiguredNodes.PreconfiguredNode.CiscoIosXrWatchdCfg_WatchdogNodeThreshold.MemoryThreshold()
                self.memory_threshold.parent = self
                self._children_name_map["memory_threshold"] = "memory-threshold"
                self._children_yang_names.add("memory-threshold")


            class MemoryThreshold(Entity):
                """
                Memory thresholds
                
                .. attribute:: critical
                
                	Threshold, Range(3, severe)
                	**type**\:  int
                
                	**range:** 3..40
                
                .. attribute:: minor
                
                	Threshold, Range(5, 40)
                	**type**\:  int
                
                	**range:** 5..40
                
                .. attribute:: severe
                
                	Threshold, Range(4, minor)
                	**type**\:  int
                
                	**range:** 4..40
                
                

                """

                _prefix = 'watchd-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(PreconfiguredNodes.PreconfiguredNode.CiscoIosXrWatchdCfg_WatchdogNodeThreshold.MemoryThreshold, self).__init__()

                    self.yang_name = "memory-threshold"
                    self.yang_parent_name = "Cisco-IOS-XR-watchd-cfg_watchdog-node-threshold"

                    self.critical = YLeaf(YType.uint32, "critical")

                    self.minor = YLeaf(YType.uint32, "minor")

                    self.severe = YLeaf(YType.uint32, "severe")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("critical",
                                    "minor",
                                    "severe") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(PreconfiguredNodes.PreconfiguredNode.CiscoIosXrWatchdCfg_WatchdogNodeThreshold.MemoryThreshold, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(PreconfiguredNodes.PreconfiguredNode.CiscoIosXrWatchdCfg_WatchdogNodeThreshold.MemoryThreshold, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.critical.is_set or
                        self.minor.is_set or
                        self.severe.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.critical.yfilter != YFilter.not_set or
                        self.minor.yfilter != YFilter.not_set or
                        self.severe.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "memory-threshold" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.critical.is_set or self.critical.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.critical.get_name_leafdata())
                    if (self.minor.is_set or self.minor.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.minor.get_name_leafdata())
                    if (self.severe.is_set or self.severe.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.severe.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "critical" or name == "minor" or name == "severe"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "critical"):
                        self.critical = value
                        self.critical.value_namespace = name_space
                        self.critical.value_namespace_prefix = name_space_prefix
                    if(value_path == "minor"):
                        self.minor = value
                        self.minor.value_namespace = name_space
                        self.minor.value_namespace_prefix = name_space_prefix
                    if(value_path == "severe"):
                        self.severe = value
                        self.severe.value_namespace = name_space
                        self.severe.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (self.memory_threshold is not None and self.memory_threshold.has_data())

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.memory_threshold is not None and self.memory_threshold.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "Cisco-IOS-XR-watchd-cfg:Cisco-IOS-XR-watchd-cfg_watchdog-node-threshold" + path_buffer

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

                if (child_yang_name == "memory-threshold"):
                    if (self.memory_threshold is None):
                        self.memory_threshold = PreconfiguredNodes.PreconfiguredNode.CiscoIosXrWatchdCfg_WatchdogNodeThreshold.MemoryThreshold()
                        self.memory_threshold.parent = self
                        self._children_name_map["memory_threshold"] = "memory-threshold"
                    return self.memory_threshold

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "memory-threshold"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class CiscoIosXrWdCfg_WatchdogNodeThreshold(Entity):
            """
            Watchdog threshold configuration
            
            .. attribute:: memory_threshold
            
            	Memory thresholds
            	**type**\:   :py:class:`MemoryThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.CiscoIosXrWdCfg_WatchdogNodeThreshold.MemoryThreshold>`
            
            

            """

            _prefix = 'wd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(PreconfiguredNodes.PreconfiguredNode.CiscoIosXrWdCfg_WatchdogNodeThreshold, self).__init__()

                self.yang_name = "Cisco-IOS-XR-wd-cfg_watchdog-node-threshold"
                self.yang_parent_name = "preconfigured-node"

                self.memory_threshold = PreconfiguredNodes.PreconfiguredNode.CiscoIosXrWdCfg_WatchdogNodeThreshold.MemoryThreshold()
                self.memory_threshold.parent = self
                self._children_name_map["memory_threshold"] = "memory-threshold"
                self._children_yang_names.add("memory-threshold")


            class MemoryThreshold(Entity):
                """
                Memory thresholds
                
                .. attribute:: critical
                
                	Threshold, Range(3, severe)
                	**type**\:  int
                
                	**range:** 3..40
                
                .. attribute:: minor
                
                	Threshold, Range(5, 40)
                	**type**\:  int
                
                	**range:** 5..40
                
                .. attribute:: severe
                
                	Threshold, Range(4, minor)
                	**type**\:  int
                
                	**range:** 4..40
                
                

                """

                _prefix = 'wd-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(PreconfiguredNodes.PreconfiguredNode.CiscoIosXrWdCfg_WatchdogNodeThreshold.MemoryThreshold, self).__init__()

                    self.yang_name = "memory-threshold"
                    self.yang_parent_name = "Cisco-IOS-XR-wd-cfg_watchdog-node-threshold"

                    self.critical = YLeaf(YType.uint32, "critical")

                    self.minor = YLeaf(YType.uint32, "minor")

                    self.severe = YLeaf(YType.uint32, "severe")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("critical",
                                    "minor",
                                    "severe") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(PreconfiguredNodes.PreconfiguredNode.CiscoIosXrWdCfg_WatchdogNodeThreshold.MemoryThreshold, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(PreconfiguredNodes.PreconfiguredNode.CiscoIosXrWdCfg_WatchdogNodeThreshold.MemoryThreshold, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.critical.is_set or
                        self.minor.is_set or
                        self.severe.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.critical.yfilter != YFilter.not_set or
                        self.minor.yfilter != YFilter.not_set or
                        self.severe.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "memory-threshold" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.critical.is_set or self.critical.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.critical.get_name_leafdata())
                    if (self.minor.is_set or self.minor.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.minor.get_name_leafdata())
                    if (self.severe.is_set or self.severe.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.severe.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "critical" or name == "minor" or name == "severe"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "critical"):
                        self.critical = value
                        self.critical.value_namespace = name_space
                        self.critical.value_namespace_prefix = name_space_prefix
                    if(value_path == "minor"):
                        self.minor = value
                        self.minor.value_namespace = name_space
                        self.minor.value_namespace_prefix = name_space_prefix
                    if(value_path == "severe"):
                        self.severe = value
                        self.severe.value_namespace = name_space
                        self.severe.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (self.memory_threshold is not None and self.memory_threshold.has_data())

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.memory_threshold is not None and self.memory_threshold.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "Cisco-IOS-XR-wd-cfg:Cisco-IOS-XR-wd-cfg_watchdog-node-threshold" + path_buffer

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

                if (child_yang_name == "memory-threshold"):
                    if (self.memory_threshold is None):
                        self.memory_threshold = PreconfiguredNodes.PreconfiguredNode.CiscoIosXrWdCfg_WatchdogNodeThreshold.MemoryThreshold()
                        self.memory_threshold.parent = self
                        self._children_name_map["memory_threshold"] = "memory-threshold"
                    return self.memory_threshold

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "memory-threshold"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                self.node_name.is_set or
                (self.cisco_ios_xr_watchd_cfg_watchdog_node_threshold is not None and self.cisco_ios_xr_watchd_cfg_watchdog_node_threshold.has_data()) or
                (self.cisco_ios_xr_wd_cfg_watchdog_node_threshold is not None and self.cisco_ios_xr_wd_cfg_watchdog_node_threshold.has_data()) or
                (self.lpts_local is not None and self.lpts_local.has_data()) or
                (self.ltrace is not None and self.ltrace.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.node_name.yfilter != YFilter.not_set or
                (self.cisco_ios_xr_watchd_cfg_watchdog_node_threshold is not None and self.cisco_ios_xr_watchd_cfg_watchdog_node_threshold.has_operation()) or
                (self.cisco_ios_xr_wd_cfg_watchdog_node_threshold is not None and self.cisco_ios_xr_wd_cfg_watchdog_node_threshold.has_operation()) or
                (self.lpts_local is not None and self.lpts_local.has_operation()) or
                (self.ltrace is not None and self.ltrace.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "preconfigured-node" + "[node-name='" + self.node_name.get() + "']" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-config-mda-cfg:preconfigured-nodes/%s" % self.get_segment_path()
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

            if (child_yang_name == "Cisco-IOS-XR-watchd-cfg_watchdog-node-threshold"):
                if (self.cisco_ios_xr_watchd_cfg_watchdog_node_threshold is None):
                    self.cisco_ios_xr_watchd_cfg_watchdog_node_threshold = PreconfiguredNodes.PreconfiguredNode.CiscoIosXrWatchdCfg_WatchdogNodeThreshold()
                    self.cisco_ios_xr_watchd_cfg_watchdog_node_threshold.parent = self
                    self._children_name_map["cisco_ios_xr_watchd_cfg_watchdog_node_threshold"] = "Cisco-IOS-XR-watchd-cfg_watchdog-node-threshold"
                return self.cisco_ios_xr_watchd_cfg_watchdog_node_threshold

            if (child_yang_name == "Cisco-IOS-XR-wd-cfg_watchdog-node-threshold"):
                if (self.cisco_ios_xr_wd_cfg_watchdog_node_threshold is None):
                    self.cisco_ios_xr_wd_cfg_watchdog_node_threshold = PreconfiguredNodes.PreconfiguredNode.CiscoIosXrWdCfg_WatchdogNodeThreshold()
                    self.cisco_ios_xr_wd_cfg_watchdog_node_threshold.parent = self
                    self._children_name_map["cisco_ios_xr_wd_cfg_watchdog_node_threshold"] = "Cisco-IOS-XR-wd-cfg_watchdog-node-threshold"
                return self.cisco_ios_xr_wd_cfg_watchdog_node_threshold

            if (child_yang_name == "lpts-local"):
                if (self.lpts_local is None):
                    self.lpts_local = PreconfiguredNodes.PreconfiguredNode.LptsLocal()
                    self.lpts_local.parent = self
                    self._children_name_map["lpts_local"] = "lpts-local"
                return self.lpts_local

            if (child_yang_name == "ltrace"):
                if (self.ltrace is None):
                    self.ltrace = PreconfiguredNodes.PreconfiguredNode.Ltrace()
                    self.ltrace.parent = self
                    self._children_name_map["ltrace"] = "ltrace"
                return self.ltrace

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "Cisco-IOS-XR-watchd-cfg_watchdog-node-threshold" or name == "Cisco-IOS-XR-wd-cfg_watchdog-node-threshold" or name == "lpts-local" or name == "ltrace" or name == "node-name"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "node-name"):
                self.node_name = value
                self.node_name.value_namespace = name_space
                self.node_name.value_namespace_prefix = name_space_prefix

    def has_data(self):
        for c in self.preconfigured_node:
            if (c.has_data()):
                return True
        return False

    def has_operation(self):
        for c in self.preconfigured_node:
            if (c.has_operation()):
                return True
        return self.yfilter != YFilter.not_set

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-config-mda-cfg:preconfigured-nodes" + path_buffer

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

        if (child_yang_name == "preconfigured-node"):
            for c in self.preconfigured_node:
                segment = c.get_segment_path()
                if (segment_path == segment):
                    return c
            c = PreconfiguredNodes.PreconfiguredNode()
            c.parent = self
            local_reference_key = "ydk::seg::%s" % segment_path
            self._local_refs[local_reference_key] = c
            self.preconfigured_node.append(c)
            return c

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "preconfigured-node"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = PreconfiguredNodes()
        return self._top_entity

