""" Cisco_IOS_XR_asr9k_lc_ethctrl_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR asr9k\-lc\-ethctrl package operational data.

This module contains definitions
for the following management objects\:
  mlan\: Management LAN Operational data space

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Mlan(Entity):
    """
    Management LAN Operational data space
    
    .. attribute:: nodes
    
    	Table of nodes
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper.Mlan.Nodes>`
    
    

    """

    _prefix = 'asr9k-lc-ethctrl-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Mlan, self).__init__()
        self._top_entity = None

        self.yang_name = "mlan"
        self.yang_parent_name = "Cisco-IOS-XR-asr9k-lc-ethctrl-oper"

        self.nodes = Mlan.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")


    class Nodes(Entity):
        """
        Table of nodes
        
        .. attribute:: node
        
        	Number
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper.Mlan.Nodes.Node>`
        
        

        """

        _prefix = 'asr9k-lc-ethctrl-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Mlan.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "mlan"

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
                        super(Mlan.Nodes, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Mlan.Nodes, self).__setattr__(name, value)


        class Node(Entity):
            """
            Number
            
            .. attribute:: node  <key>
            
            	node number
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: atu_entry_numbers
            
            	Table of switch ATU
            	**type**\:   :py:class:`AtuEntryNumbers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper.Mlan.Nodes.Node.AtuEntryNumbers>`
            
            .. attribute:: port_counters_numbers
            
            	Table of port counters
            	**type**\:   :py:class:`PortCountersNumbers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper.Mlan.Nodes.Node.PortCountersNumbers>`
            
            .. attribute:: port_status_numbers
            
            	Table of port status
            	**type**\:   :py:class:`PortStatusNumbers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper.Mlan.Nodes.Node.PortStatusNumbers>`
            
            .. attribute:: switch_status_table
            
            	Table of switch status
            	**type**\:   :py:class:`SwitchStatusTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper.Mlan.Nodes.Node.SwitchStatusTable>`
            
            

            """

            _prefix = 'asr9k-lc-ethctrl-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Mlan.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"

                self.node = YLeaf(YType.str, "node")

                self.atu_entry_numbers = Mlan.Nodes.Node.AtuEntryNumbers()
                self.atu_entry_numbers.parent = self
                self._children_name_map["atu_entry_numbers"] = "atu-entry-numbers"
                self._children_yang_names.add("atu-entry-numbers")

                self.port_counters_numbers = Mlan.Nodes.Node.PortCountersNumbers()
                self.port_counters_numbers.parent = self
                self._children_name_map["port_counters_numbers"] = "port-counters-numbers"
                self._children_yang_names.add("port-counters-numbers")

                self.port_status_numbers = Mlan.Nodes.Node.PortStatusNumbers()
                self.port_status_numbers.parent = self
                self._children_name_map["port_status_numbers"] = "port-status-numbers"
                self._children_yang_names.add("port-status-numbers")

                self.switch_status_table = Mlan.Nodes.Node.SwitchStatusTable()
                self.switch_status_table.parent = self
                self._children_name_map["switch_status_table"] = "switch-status-table"
                self._children_yang_names.add("switch-status-table")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("node") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Mlan.Nodes.Node, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Mlan.Nodes.Node, self).__setattr__(name, value)


            class PortStatusNumbers(Entity):
                """
                Table of port status
                
                .. attribute:: port_status_number
                
                	Number
                	**type**\: list of    :py:class:`PortStatusNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper.Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber>`
                
                

                """

                _prefix = 'asr9k-lc-ethctrl-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Mlan.Nodes.Node.PortStatusNumbers, self).__init__()

                    self.yang_name = "port-status-numbers"
                    self.yang_parent_name = "node"

                    self.port_status_number = YList(self)

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
                                super(Mlan.Nodes.Node.PortStatusNumbers, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Mlan.Nodes.Node.PortStatusNumbers, self).__setattr__(name, value)


                class PortStatusNumber(Entity):
                    """
                    Number
                    
                    .. attribute:: number  <key>
                    
                    	port number
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: port_status
                    
                    	mlan port status info
                    	**type**\:   :py:class:`PortStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper.Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus>`
                    
                    

                    """

                    _prefix = 'asr9k-lc-ethctrl-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber, self).__init__()

                        self.yang_name = "port-status-number"
                        self.yang_parent_name = "port-status-numbers"

                        self.number = YLeaf(YType.int32, "number")

                        self.port_status = Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus()
                        self.port_status.parent = self
                        self._children_name_map["port_status"] = "port-status"
                        self._children_yang_names.add("port-status")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("number") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber, self).__setattr__(name, value)


                    class PortStatus(Entity):
                        """
                        mlan port status info
                        
                        .. attribute:: config
                        
                        	Configuration Data
                        	**type**\:   :py:class:`Config <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper.Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus.Config>`
                        
                        .. attribute:: mac
                        
                        	MAC Registers
                        	**type**\:   :py:class:`Mac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper.Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus.Mac>`
                        
                        .. attribute:: mac_valid
                        
                        	MAC data valid
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: phy
                        
                        	PHY Registers
                        	**type**\:   :py:class:`Phy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper.Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus.Phy>`
                        
                        .. attribute:: phy_valid
                        
                        	PHY data valid
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: port_num
                        
                        	Port Number
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: serdes
                        
                        	SERDES Registers
                        	**type**\:   :py:class:`Serdes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper.Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus.Serdes>`
                        
                        .. attribute:: serdes_valid
                        
                        	SERDES data valid
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'asr9k-lc-ethctrl-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus, self).__init__()

                            self.yang_name = "port-status"
                            self.yang_parent_name = "port-status-number"

                            self.mac_valid = YLeaf(YType.uint32, "mac-valid")

                            self.phy_valid = YLeaf(YType.uint32, "phy-valid")

                            self.port_num = YLeaf(YType.uint32, "port-num")

                            self.serdes_valid = YLeaf(YType.uint32, "serdes-valid")

                            self.config = Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"
                            self._children_yang_names.add("config")

                            self.mac = Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus.Mac()
                            self.mac.parent = self
                            self._children_name_map["mac"] = "mac"
                            self._children_yang_names.add("mac")

                            self.phy = Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus.Phy()
                            self.phy.parent = self
                            self._children_name_map["phy"] = "phy"
                            self._children_yang_names.add("phy")

                            self.serdes = Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus.Serdes()
                            self.serdes.parent = self
                            self._children_name_map["serdes"] = "serdes"
                            self._children_yang_names.add("serdes")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("mac_valid",
                                            "phy_valid",
                                            "port_num",
                                            "serdes_valid") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus, self).__setattr__(name, value)


                        class Config(Entity):
                            """
                            Configuration Data
                            
                            .. attribute:: duplex
                            
                            	duplex
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: loopback
                            
                            	loopback
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: my_pause
                            
                            	myPause
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: pause
                            
                            	pauseEn
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: speed
                            
                            	speed
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'asr9k-lc-ethctrl-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "port-status"

                                self.duplex = YLeaf(YType.uint32, "duplex")

                                self.loopback = YLeaf(YType.uint32, "loopback")

                                self.my_pause = YLeaf(YType.uint16, "my-pause")

                                self.pause = YLeaf(YType.uint16, "pause")

                                self.speed = YLeaf(YType.uint32, "speed")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("duplex",
                                                "loopback",
                                                "my_pause",
                                                "pause",
                                                "speed") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus.Config, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus.Config, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.duplex.is_set or
                                    self.loopback.is_set or
                                    self.my_pause.is_set or
                                    self.pause.is_set or
                                    self.speed.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.duplex.yfilter != YFilter.not_set or
                                    self.loopback.yfilter != YFilter.not_set or
                                    self.my_pause.yfilter != YFilter.not_set or
                                    self.pause.yfilter != YFilter.not_set or
                                    self.speed.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "config" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.duplex.is_set or self.duplex.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.duplex.get_name_leafdata())
                                if (self.loopback.is_set or self.loopback.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.loopback.get_name_leafdata())
                                if (self.my_pause.is_set or self.my_pause.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.my_pause.get_name_leafdata())
                                if (self.pause.is_set or self.pause.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pause.get_name_leafdata())
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
                                if(name == "duplex" or name == "loopback" or name == "my-pause" or name == "pause" or name == "speed"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "duplex"):
                                    self.duplex = value
                                    self.duplex.value_namespace = name_space
                                    self.duplex.value_namespace_prefix = name_space_prefix
                                if(value_path == "loopback"):
                                    self.loopback = value
                                    self.loopback.value_namespace = name_space
                                    self.loopback.value_namespace_prefix = name_space_prefix
                                if(value_path == "my-pause"):
                                    self.my_pause = value
                                    self.my_pause.value_namespace = name_space
                                    self.my_pause.value_namespace_prefix = name_space_prefix
                                if(value_path == "pause"):
                                    self.pause = value
                                    self.pause.value_namespace = name_space
                                    self.pause.value_namespace_prefix = name_space_prefix
                                if(value_path == "speed"):
                                    self.speed = value
                                    self.speed.value_namespace = name_space
                                    self.speed.value_namespace_prefix = name_space_prefix


                        class Phy(Entity):
                            """
                            PHY Registers
                            
                            .. attribute:: reg
                            
                            	reg
                            	**type**\:  list of int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'asr9k-lc-ethctrl-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus.Phy, self).__init__()

                                self.yang_name = "phy"
                                self.yang_parent_name = "port-status"

                                self.reg = YLeafList(YType.uint16, "reg")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("reg") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus.Phy, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus.Phy, self).__setattr__(name, value)

                            def has_data(self):
                                for leaf in self.reg.getYLeafs():
                                    if (leaf.yfilter != YFilter.not_set):
                                        return True
                                return False

                            def has_operation(self):
                                for leaf in self.reg.getYLeafs():
                                    if (leaf.is_set):
                                        return True
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.reg.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "phy" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()

                                leaf_name_data.extend(self.reg.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "reg"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "reg"):
                                    self.reg.append(value)


                        class Serdes(Entity):
                            """
                            SERDES Registers
                            
                            .. attribute:: reg
                            
                            	reg
                            	**type**\:  list of int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'asr9k-lc-ethctrl-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus.Serdes, self).__init__()

                                self.yang_name = "serdes"
                                self.yang_parent_name = "port-status"

                                self.reg = YLeafList(YType.uint16, "reg")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("reg") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus.Serdes, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus.Serdes, self).__setattr__(name, value)

                            def has_data(self):
                                for leaf in self.reg.getYLeafs():
                                    if (leaf.yfilter != YFilter.not_set):
                                        return True
                                return False

                            def has_operation(self):
                                for leaf in self.reg.getYLeafs():
                                    if (leaf.is_set):
                                        return True
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.reg.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "serdes" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()

                                leaf_name_data.extend(self.reg.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "reg"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "reg"):
                                    self.reg.append(value)


                        class Mac(Entity):
                            """
                            MAC Registers
                            
                            .. attribute:: reg
                            
                            	reg
                            	**type**\:  list of int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'asr9k-lc-ethctrl-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus.Mac, self).__init__()

                                self.yang_name = "mac"
                                self.yang_parent_name = "port-status"

                                self.reg = YLeafList(YType.uint16, "reg")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("reg") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus.Mac, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus.Mac, self).__setattr__(name, value)

                            def has_data(self):
                                for leaf in self.reg.getYLeafs():
                                    if (leaf.yfilter != YFilter.not_set):
                                        return True
                                return False

                            def has_operation(self):
                                for leaf in self.reg.getYLeafs():
                                    if (leaf.is_set):
                                        return True
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.reg.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "mac" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()

                                leaf_name_data.extend(self.reg.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "reg"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "reg"):
                                    self.reg.append(value)

                        def has_data(self):
                            return (
                                self.mac_valid.is_set or
                                self.phy_valid.is_set or
                                self.port_num.is_set or
                                self.serdes_valid.is_set or
                                (self.config is not None and self.config.has_data()) or
                                (self.mac is not None and self.mac.has_data()) or
                                (self.phy is not None and self.phy.has_data()) or
                                (self.serdes is not None and self.serdes.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.mac_valid.yfilter != YFilter.not_set or
                                self.phy_valid.yfilter != YFilter.not_set or
                                self.port_num.yfilter != YFilter.not_set or
                                self.serdes_valid.yfilter != YFilter.not_set or
                                (self.config is not None and self.config.has_operation()) or
                                (self.mac is not None and self.mac.has_operation()) or
                                (self.phy is not None and self.phy.has_operation()) or
                                (self.serdes is not None and self.serdes.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "port-status" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.mac_valid.is_set or self.mac_valid.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.mac_valid.get_name_leafdata())
                            if (self.phy_valid.is_set or self.phy_valid.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.phy_valid.get_name_leafdata())
                            if (self.port_num.is_set or self.port_num.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.port_num.get_name_leafdata())
                            if (self.serdes_valid.is_set or self.serdes_valid.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.serdes_valid.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "config"):
                                if (self.config is None):
                                    self.config = Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus.Config()
                                    self.config.parent = self
                                    self._children_name_map["config"] = "config"
                                return self.config

                            if (child_yang_name == "mac"):
                                if (self.mac is None):
                                    self.mac = Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus.Mac()
                                    self.mac.parent = self
                                    self._children_name_map["mac"] = "mac"
                                return self.mac

                            if (child_yang_name == "phy"):
                                if (self.phy is None):
                                    self.phy = Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus.Phy()
                                    self.phy.parent = self
                                    self._children_name_map["phy"] = "phy"
                                return self.phy

                            if (child_yang_name == "serdes"):
                                if (self.serdes is None):
                                    self.serdes = Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus.Serdes()
                                    self.serdes.parent = self
                                    self._children_name_map["serdes"] = "serdes"
                                return self.serdes

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "config" or name == "mac" or name == "phy" or name == "serdes" or name == "mac-valid" or name == "phy-valid" or name == "port-num" or name == "serdes-valid"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "mac-valid"):
                                self.mac_valid = value
                                self.mac_valid.value_namespace = name_space
                                self.mac_valid.value_namespace_prefix = name_space_prefix
                            if(value_path == "phy-valid"):
                                self.phy_valid = value
                                self.phy_valid.value_namespace = name_space
                                self.phy_valid.value_namespace_prefix = name_space_prefix
                            if(value_path == "port-num"):
                                self.port_num = value
                                self.port_num.value_namespace = name_space
                                self.port_num.value_namespace_prefix = name_space_prefix
                            if(value_path == "serdes-valid"):
                                self.serdes_valid = value
                                self.serdes_valid.value_namespace = name_space
                                self.serdes_valid.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.number.is_set or
                            (self.port_status is not None and self.port_status.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.number.yfilter != YFilter.not_set or
                            (self.port_status is not None and self.port_status.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "port-status-number" + "[number='" + self.number.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.number.is_set or self.number.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.number.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "port-status"):
                            if (self.port_status is None):
                                self.port_status = Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus()
                                self.port_status.parent = self
                                self._children_name_map["port_status"] = "port-status"
                            return self.port_status

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "port-status" or name == "number"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "number"):
                            self.number = value
                            self.number.value_namespace = name_space
                            self.number.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.port_status_number:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.port_status_number:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "port-status-numbers" + path_buffer

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

                    if (child_yang_name == "port-status-number"):
                        for c in self.port_status_number:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.port_status_number.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "port-status-number"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class SwitchStatusTable(Entity):
                """
                Table of switch status
                
                .. attribute:: switch_status
                
                	mlan switch status info
                	**type**\:   :py:class:`SwitchStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper.Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus>`
                
                

                """

                _prefix = 'asr9k-lc-ethctrl-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Mlan.Nodes.Node.SwitchStatusTable, self).__init__()

                    self.yang_name = "switch-status-table"
                    self.yang_parent_name = "node"

                    self.switch_status = Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus()
                    self.switch_status.parent = self
                    self._children_name_map["switch_status"] = "switch-status"
                    self._children_yang_names.add("switch-status")


                class SwitchStatus(Entity):
                    """
                    mlan switch status info
                    
                    .. attribute:: rate_limit
                    
                    	CPU Interface Rate Limit
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: sw_reg_1
                    
                    	Switch Global Registers
                    	**type**\:   :py:class:`SwReg1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper.Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus.SwReg1>`
                    
                    .. attribute:: sw_reg_2
                    
                    	Switch Global Registers
                    	**type**\:   :py:class:`SwReg2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper.Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus.SwReg2>`
                    
                    .. attribute:: sw_status
                    
                    	Switch Status Data
                    	**type**\:   :py:class:`SwStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper.Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus.SwStatus>`
                    
                    

                    """

                    _prefix = 'asr9k-lc-ethctrl-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus, self).__init__()

                        self.yang_name = "switch-status"
                        self.yang_parent_name = "switch-status-table"

                        self.rate_limit = YLeaf(YType.int32, "rate-limit")

                        self.sw_reg_1 = Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus.SwReg1()
                        self.sw_reg_1.parent = self
                        self._children_name_map["sw_reg_1"] = "sw-reg-1"
                        self._children_yang_names.add("sw-reg-1")

                        self.sw_reg_2 = Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus.SwReg2()
                        self.sw_reg_2.parent = self
                        self._children_name_map["sw_reg_2"] = "sw-reg-2"
                        self._children_yang_names.add("sw-reg-2")

                        self.sw_status = Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus.SwStatus()
                        self.sw_status.parent = self
                        self._children_name_map["sw_status"] = "sw-status"
                        self._children_yang_names.add("sw-status")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("rate_limit") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus, self).__setattr__(name, value)


                    class SwReg1(Entity):
                        """
                        Switch Global Registers
                        
                        .. attribute:: reg
                        
                        	reg
                        	**type**\:  list of int
                        
                        	**range:** 0..65535
                        
                        

                        """

                        _prefix = 'asr9k-lc-ethctrl-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus.SwReg1, self).__init__()

                            self.yang_name = "sw-reg-1"
                            self.yang_parent_name = "switch-status"

                            self.reg = YLeafList(YType.uint16, "reg")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("reg") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus.SwReg1, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus.SwReg1, self).__setattr__(name, value)

                        def has_data(self):
                            for leaf in self.reg.getYLeafs():
                                if (leaf.yfilter != YFilter.not_set):
                                    return True
                            return False

                        def has_operation(self):
                            for leaf in self.reg.getYLeafs():
                                if (leaf.is_set):
                                    return True
                            return (
                                self.yfilter != YFilter.not_set or
                                self.reg.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "sw-reg-1" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            leaf_name_data.extend(self.reg.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "reg"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "reg"):
                                self.reg.append(value)


                    class SwReg2(Entity):
                        """
                        Switch Global Registers
                        
                        .. attribute:: reg
                        
                        	reg
                        	**type**\:  list of int
                        
                        	**range:** 0..65535
                        
                        

                        """

                        _prefix = 'asr9k-lc-ethctrl-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus.SwReg2, self).__init__()

                            self.yang_name = "sw-reg-2"
                            self.yang_parent_name = "switch-status"

                            self.reg = YLeafList(YType.uint16, "reg")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("reg") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus.SwReg2, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus.SwReg2, self).__setattr__(name, value)

                        def has_data(self):
                            for leaf in self.reg.getYLeafs():
                                if (leaf.yfilter != YFilter.not_set):
                                    return True
                            return False

                        def has_operation(self):
                            for leaf in self.reg.getYLeafs():
                                if (leaf.is_set):
                                    return True
                            return (
                                self.yfilter != YFilter.not_set or
                                self.reg.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "sw-reg-2" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            leaf_name_data.extend(self.reg.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "reg"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "reg"):
                                self.reg.append(value)


                    class SwStatus(Entity):
                        """
                        Switch Status Data
                        
                        .. attribute:: cpu_mac
                        
                        	cpu mac
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: cpu_port
                        
                        	cpu port
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: initialized
                        
                        	initialized
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: mac
                        
                        	mac
                        	**type**\:  str
                        
                        	**length:** 0..6
                        
                        .. attribute:: mtu
                        
                        	mtu
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ppu
                        
                        	ppu
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: restarted
                        
                        	restarted
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        

                        """

                        _prefix = 'asr9k-lc-ethctrl-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus.SwStatus, self).__init__()

                            self.yang_name = "sw-status"
                            self.yang_parent_name = "switch-status"

                            self.cpu_mac = YLeaf(YType.uint16, "cpu-mac")

                            self.cpu_port = YLeaf(YType.uint16, "cpu-port")

                            self.initialized = YLeaf(YType.uint16, "initialized")

                            self.mac = YLeaf(YType.str, "mac")

                            self.mtu = YLeaf(YType.uint32, "mtu")

                            self.ppu = YLeaf(YType.uint32, "ppu")

                            self.restarted = YLeaf(YType.uint16, "restarted")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("cpu_mac",
                                            "cpu_port",
                                            "initialized",
                                            "mac",
                                            "mtu",
                                            "ppu",
                                            "restarted") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus.SwStatus, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus.SwStatus, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.cpu_mac.is_set or
                                self.cpu_port.is_set or
                                self.initialized.is_set or
                                self.mac.is_set or
                                self.mtu.is_set or
                                self.ppu.is_set or
                                self.restarted.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.cpu_mac.yfilter != YFilter.not_set or
                                self.cpu_port.yfilter != YFilter.not_set or
                                self.initialized.yfilter != YFilter.not_set or
                                self.mac.yfilter != YFilter.not_set or
                                self.mtu.yfilter != YFilter.not_set or
                                self.ppu.yfilter != YFilter.not_set or
                                self.restarted.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "sw-status" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.cpu_mac.is_set or self.cpu_mac.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.cpu_mac.get_name_leafdata())
                            if (self.cpu_port.is_set or self.cpu_port.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.cpu_port.get_name_leafdata())
                            if (self.initialized.is_set or self.initialized.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.initialized.get_name_leafdata())
                            if (self.mac.is_set or self.mac.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.mac.get_name_leafdata())
                            if (self.mtu.is_set or self.mtu.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.mtu.get_name_leafdata())
                            if (self.ppu.is_set or self.ppu.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ppu.get_name_leafdata())
                            if (self.restarted.is_set or self.restarted.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.restarted.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "cpu-mac" or name == "cpu-port" or name == "initialized" or name == "mac" or name == "mtu" or name == "ppu" or name == "restarted"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "cpu-mac"):
                                self.cpu_mac = value
                                self.cpu_mac.value_namespace = name_space
                                self.cpu_mac.value_namespace_prefix = name_space_prefix
                            if(value_path == "cpu-port"):
                                self.cpu_port = value
                                self.cpu_port.value_namespace = name_space
                                self.cpu_port.value_namespace_prefix = name_space_prefix
                            if(value_path == "initialized"):
                                self.initialized = value
                                self.initialized.value_namespace = name_space
                                self.initialized.value_namespace_prefix = name_space_prefix
                            if(value_path == "mac"):
                                self.mac = value
                                self.mac.value_namespace = name_space
                                self.mac.value_namespace_prefix = name_space_prefix
                            if(value_path == "mtu"):
                                self.mtu = value
                                self.mtu.value_namespace = name_space
                                self.mtu.value_namespace_prefix = name_space_prefix
                            if(value_path == "ppu"):
                                self.ppu = value
                                self.ppu.value_namespace = name_space
                                self.ppu.value_namespace_prefix = name_space_prefix
                            if(value_path == "restarted"):
                                self.restarted = value
                                self.restarted.value_namespace = name_space
                                self.restarted.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.rate_limit.is_set or
                            (self.sw_reg_1 is not None and self.sw_reg_1.has_data()) or
                            (self.sw_reg_2 is not None and self.sw_reg_2.has_data()) or
                            (self.sw_status is not None and self.sw_status.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.rate_limit.yfilter != YFilter.not_set or
                            (self.sw_reg_1 is not None and self.sw_reg_1.has_operation()) or
                            (self.sw_reg_2 is not None and self.sw_reg_2.has_operation()) or
                            (self.sw_status is not None and self.sw_status.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "switch-status" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.rate_limit.is_set or self.rate_limit.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.rate_limit.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "sw-reg-1"):
                            if (self.sw_reg_1 is None):
                                self.sw_reg_1 = Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus.SwReg1()
                                self.sw_reg_1.parent = self
                                self._children_name_map["sw_reg_1"] = "sw-reg-1"
                            return self.sw_reg_1

                        if (child_yang_name == "sw-reg-2"):
                            if (self.sw_reg_2 is None):
                                self.sw_reg_2 = Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus.SwReg2()
                                self.sw_reg_2.parent = self
                                self._children_name_map["sw_reg_2"] = "sw-reg-2"
                            return self.sw_reg_2

                        if (child_yang_name == "sw-status"):
                            if (self.sw_status is None):
                                self.sw_status = Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus.SwStatus()
                                self.sw_status.parent = self
                                self._children_name_map["sw_status"] = "sw-status"
                            return self.sw_status

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "sw-reg-1" or name == "sw-reg-2" or name == "sw-status" or name == "rate-limit"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "rate-limit"):
                            self.rate_limit = value
                            self.rate_limit.value_namespace = name_space
                            self.rate_limit.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (self.switch_status is not None and self.switch_status.has_data())

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.switch_status is not None and self.switch_status.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "switch-status-table" + path_buffer

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

                    if (child_yang_name == "switch-status"):
                        if (self.switch_status is None):
                            self.switch_status = Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus()
                            self.switch_status.parent = self
                            self._children_name_map["switch_status"] = "switch-status"
                        return self.switch_status

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "switch-status"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class PortCountersNumbers(Entity):
                """
                Table of port counters
                
                .. attribute:: port_counters_number
                
                	Number
                	**type**\: list of    :py:class:`PortCountersNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper.Mlan.Nodes.Node.PortCountersNumbers.PortCountersNumber>`
                
                

                """

                _prefix = 'asr9k-lc-ethctrl-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Mlan.Nodes.Node.PortCountersNumbers, self).__init__()

                    self.yang_name = "port-counters-numbers"
                    self.yang_parent_name = "node"

                    self.port_counters_number = YList(self)

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
                                super(Mlan.Nodes.Node.PortCountersNumbers, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Mlan.Nodes.Node.PortCountersNumbers, self).__setattr__(name, value)


                class PortCountersNumber(Entity):
                    """
                    Number
                    
                    .. attribute:: number  <key>
                    
                    	port number
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: port_counters
                    
                    	mlan port counters info
                    	**type**\:   :py:class:`PortCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper.Mlan.Nodes.Node.PortCountersNumbers.PortCountersNumber.PortCounters>`
                    
                    

                    """

                    _prefix = 'asr9k-lc-ethctrl-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Mlan.Nodes.Node.PortCountersNumbers.PortCountersNumber, self).__init__()

                        self.yang_name = "port-counters-number"
                        self.yang_parent_name = "port-counters-numbers"

                        self.number = YLeaf(YType.int32, "number")

                        self.port_counters = Mlan.Nodes.Node.PortCountersNumbers.PortCountersNumber.PortCounters()
                        self.port_counters.parent = self
                        self._children_name_map["port_counters"] = "port-counters"
                        self._children_yang_names.add("port-counters")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("number") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Mlan.Nodes.Node.PortCountersNumbers.PortCountersNumber, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Mlan.Nodes.Node.PortCountersNumbers.PortCountersNumber, self).__setattr__(name, value)


                    class PortCounters(Entity):
                        """
                        mlan port counters info
                        
                        .. attribute:: mlan_stats
                        
                        	Switch Port Statistics
                        	**type**\:   :py:class:`MlanStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper.Mlan.Nodes.Node.PortCountersNumbers.PortCountersNumber.PortCounters.MlanStats>`
                        
                        .. attribute:: port_num
                        
                        	Port Number
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'asr9k-lc-ethctrl-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Mlan.Nodes.Node.PortCountersNumbers.PortCountersNumber.PortCounters, self).__init__()

                            self.yang_name = "port-counters"
                            self.yang_parent_name = "port-counters-number"

                            self.port_num = YLeaf(YType.uint32, "port-num")

                            self.mlan_stats = Mlan.Nodes.Node.PortCountersNumbers.PortCountersNumber.PortCounters.MlanStats()
                            self.mlan_stats.parent = self
                            self._children_name_map["mlan_stats"] = "mlan-stats"
                            self._children_yang_names.add("mlan-stats")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("port_num") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Mlan.Nodes.Node.PortCountersNumbers.PortCountersNumber.PortCounters, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Mlan.Nodes.Node.PortCountersNumbers.PortCountersNumber.PortCounters, self).__setattr__(name, value)


                        class MlanStats(Entity):
                            """
                            Switch Port Statistics
                            
                            .. attribute:: collisions
                            
                            	collisions
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: deferred
                            
                            	deferred
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: excessive
                            
                            	excessive
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: in_bad_octets
                            
                            	inBadOctets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: in_bcast_pkt
                            
                            	inBcastPkt
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: in_discards
                            
                            	inDiscards
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: in_fcs_err
                            
                            	inFcsErr
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: in_filtered
                            
                            	inFiltered
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: in_fragments
                            
                            	inFragments
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: in_good_octets
                            
                            	inGoodOctets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: in_good_octets_hi
                            
                            	inGoodOctets hi
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: in_jabber
                            
                            	inJabber
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: in_mcast_pkt
                            
                            	inMcastPkt
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: in_oversize
                            
                            	inOversize
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: in_pause_pkt
                            
                            	inPausePkt
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: in_rx_err
                            
                            	inRxErr
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: in_undersize_pkt
                            
                            	inUndersizePkt
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: in_unicast_pkt
                            
                            	inUnicastPkt
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: late
                            
                            	late
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: multiple
                            
                            	multiple
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: out_bcast_pkt
                            
                            	outBcastPkt
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: out_fcs_err
                            
                            	outFcsErr
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: out_filtered
                            
                            	outFiltered
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: out_mcast_pkt
                            
                            	outMcastPkt
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: out_octets
                            
                            	outOctets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: out_octets_hi
                            
                            	outOctets hi
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: out_pause_pkt
                            
                            	outPausePkt
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: out_unicast_pkt
                            
                            	outUnicastPkt
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: rx_tx_1024_max_octets
                            
                            	rx tx 1024 Max Octets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: rx_tx_128_255_octets
                            
                            	rx tx 128 255 Octets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: rx_tx_256_511_octets
                            
                            	rx tx 256 511 Octets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: rx_tx_512_1023_octets
                            
                            	rx tx 512 1023 Octets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: rx_tx_64_octets
                            
                            	rx tx 64 Octets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: rx_tx_65_127_octets
                            
                            	rx tx 65 127 Octets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: single
                            
                            	single
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'asr9k-lc-ethctrl-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Mlan.Nodes.Node.PortCountersNumbers.PortCountersNumber.PortCounters.MlanStats, self).__init__()

                                self.yang_name = "mlan-stats"
                                self.yang_parent_name = "port-counters"

                                self.collisions = YLeaf(YType.uint32, "collisions")

                                self.deferred = YLeaf(YType.uint32, "deferred")

                                self.excessive = YLeaf(YType.uint32, "excessive")

                                self.in_bad_octets = YLeaf(YType.uint32, "in-bad-octets")

                                self.in_bcast_pkt = YLeaf(YType.uint32, "in-bcast-pkt")

                                self.in_discards = YLeaf(YType.uint32, "in-discards")

                                self.in_fcs_err = YLeaf(YType.uint32, "in-fcs-err")

                                self.in_filtered = YLeaf(YType.uint32, "in-filtered")

                                self.in_fragments = YLeaf(YType.uint32, "in-fragments")

                                self.in_good_octets = YLeaf(YType.uint32, "in-good-octets")

                                self.in_good_octets_hi = YLeaf(YType.uint32, "in-good-octets-hi")

                                self.in_jabber = YLeaf(YType.uint32, "in-jabber")

                                self.in_mcast_pkt = YLeaf(YType.uint32, "in-mcast-pkt")

                                self.in_oversize = YLeaf(YType.uint32, "in-oversize")

                                self.in_pause_pkt = YLeaf(YType.uint32, "in-pause-pkt")

                                self.in_rx_err = YLeaf(YType.uint32, "in-rx-err")

                                self.in_undersize_pkt = YLeaf(YType.uint32, "in-undersize-pkt")

                                self.in_unicast_pkt = YLeaf(YType.uint32, "in-unicast-pkt")

                                self.late = YLeaf(YType.uint32, "late")

                                self.multiple = YLeaf(YType.uint32, "multiple")

                                self.out_bcast_pkt = YLeaf(YType.uint32, "out-bcast-pkt")

                                self.out_fcs_err = YLeaf(YType.uint32, "out-fcs-err")

                                self.out_filtered = YLeaf(YType.uint32, "out-filtered")

                                self.out_mcast_pkt = YLeaf(YType.uint32, "out-mcast-pkt")

                                self.out_octets = YLeaf(YType.uint32, "out-octets")

                                self.out_octets_hi = YLeaf(YType.uint32, "out-octets-hi")

                                self.out_pause_pkt = YLeaf(YType.uint32, "out-pause-pkt")

                                self.out_unicast_pkt = YLeaf(YType.uint32, "out-unicast-pkt")

                                self.rx_tx_1024_max_octets = YLeaf(YType.uint32, "rx-tx-1024-max-octets")

                                self.rx_tx_128_255_octets = YLeaf(YType.uint32, "rx-tx-128-255-octets")

                                self.rx_tx_256_511_octets = YLeaf(YType.uint32, "rx-tx-256-511-octets")

                                self.rx_tx_512_1023_octets = YLeaf(YType.uint32, "rx-tx-512-1023-octets")

                                self.rx_tx_64_octets = YLeaf(YType.uint32, "rx-tx-64-octets")

                                self.rx_tx_65_127_octets = YLeaf(YType.uint32, "rx-tx-65-127-octets")

                                self.single = YLeaf(YType.uint32, "single")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("collisions",
                                                "deferred",
                                                "excessive",
                                                "in_bad_octets",
                                                "in_bcast_pkt",
                                                "in_discards",
                                                "in_fcs_err",
                                                "in_filtered",
                                                "in_fragments",
                                                "in_good_octets",
                                                "in_good_octets_hi",
                                                "in_jabber",
                                                "in_mcast_pkt",
                                                "in_oversize",
                                                "in_pause_pkt",
                                                "in_rx_err",
                                                "in_undersize_pkt",
                                                "in_unicast_pkt",
                                                "late",
                                                "multiple",
                                                "out_bcast_pkt",
                                                "out_fcs_err",
                                                "out_filtered",
                                                "out_mcast_pkt",
                                                "out_octets",
                                                "out_octets_hi",
                                                "out_pause_pkt",
                                                "out_unicast_pkt",
                                                "rx_tx_1024_max_octets",
                                                "rx_tx_128_255_octets",
                                                "rx_tx_256_511_octets",
                                                "rx_tx_512_1023_octets",
                                                "rx_tx_64_octets",
                                                "rx_tx_65_127_octets",
                                                "single") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Mlan.Nodes.Node.PortCountersNumbers.PortCountersNumber.PortCounters.MlanStats, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Mlan.Nodes.Node.PortCountersNumbers.PortCountersNumber.PortCounters.MlanStats, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.collisions.is_set or
                                    self.deferred.is_set or
                                    self.excessive.is_set or
                                    self.in_bad_octets.is_set or
                                    self.in_bcast_pkt.is_set or
                                    self.in_discards.is_set or
                                    self.in_fcs_err.is_set or
                                    self.in_filtered.is_set or
                                    self.in_fragments.is_set or
                                    self.in_good_octets.is_set or
                                    self.in_good_octets_hi.is_set or
                                    self.in_jabber.is_set or
                                    self.in_mcast_pkt.is_set or
                                    self.in_oversize.is_set or
                                    self.in_pause_pkt.is_set or
                                    self.in_rx_err.is_set or
                                    self.in_undersize_pkt.is_set or
                                    self.in_unicast_pkt.is_set or
                                    self.late.is_set or
                                    self.multiple.is_set or
                                    self.out_bcast_pkt.is_set or
                                    self.out_fcs_err.is_set or
                                    self.out_filtered.is_set or
                                    self.out_mcast_pkt.is_set or
                                    self.out_octets.is_set or
                                    self.out_octets_hi.is_set or
                                    self.out_pause_pkt.is_set or
                                    self.out_unicast_pkt.is_set or
                                    self.rx_tx_1024_max_octets.is_set or
                                    self.rx_tx_128_255_octets.is_set or
                                    self.rx_tx_256_511_octets.is_set or
                                    self.rx_tx_512_1023_octets.is_set or
                                    self.rx_tx_64_octets.is_set or
                                    self.rx_tx_65_127_octets.is_set or
                                    self.single.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.collisions.yfilter != YFilter.not_set or
                                    self.deferred.yfilter != YFilter.not_set or
                                    self.excessive.yfilter != YFilter.not_set or
                                    self.in_bad_octets.yfilter != YFilter.not_set or
                                    self.in_bcast_pkt.yfilter != YFilter.not_set or
                                    self.in_discards.yfilter != YFilter.not_set or
                                    self.in_fcs_err.yfilter != YFilter.not_set or
                                    self.in_filtered.yfilter != YFilter.not_set or
                                    self.in_fragments.yfilter != YFilter.not_set or
                                    self.in_good_octets.yfilter != YFilter.not_set or
                                    self.in_good_octets_hi.yfilter != YFilter.not_set or
                                    self.in_jabber.yfilter != YFilter.not_set or
                                    self.in_mcast_pkt.yfilter != YFilter.not_set or
                                    self.in_oversize.yfilter != YFilter.not_set or
                                    self.in_pause_pkt.yfilter != YFilter.not_set or
                                    self.in_rx_err.yfilter != YFilter.not_set or
                                    self.in_undersize_pkt.yfilter != YFilter.not_set or
                                    self.in_unicast_pkt.yfilter != YFilter.not_set or
                                    self.late.yfilter != YFilter.not_set or
                                    self.multiple.yfilter != YFilter.not_set or
                                    self.out_bcast_pkt.yfilter != YFilter.not_set or
                                    self.out_fcs_err.yfilter != YFilter.not_set or
                                    self.out_filtered.yfilter != YFilter.not_set or
                                    self.out_mcast_pkt.yfilter != YFilter.not_set or
                                    self.out_octets.yfilter != YFilter.not_set or
                                    self.out_octets_hi.yfilter != YFilter.not_set or
                                    self.out_pause_pkt.yfilter != YFilter.not_set or
                                    self.out_unicast_pkt.yfilter != YFilter.not_set or
                                    self.rx_tx_1024_max_octets.yfilter != YFilter.not_set or
                                    self.rx_tx_128_255_octets.yfilter != YFilter.not_set or
                                    self.rx_tx_256_511_octets.yfilter != YFilter.not_set or
                                    self.rx_tx_512_1023_octets.yfilter != YFilter.not_set or
                                    self.rx_tx_64_octets.yfilter != YFilter.not_set or
                                    self.rx_tx_65_127_octets.yfilter != YFilter.not_set or
                                    self.single.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "mlan-stats" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.collisions.is_set or self.collisions.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.collisions.get_name_leafdata())
                                if (self.deferred.is_set or self.deferred.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.deferred.get_name_leafdata())
                                if (self.excessive.is_set or self.excessive.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.excessive.get_name_leafdata())
                                if (self.in_bad_octets.is_set or self.in_bad_octets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.in_bad_octets.get_name_leafdata())
                                if (self.in_bcast_pkt.is_set or self.in_bcast_pkt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.in_bcast_pkt.get_name_leafdata())
                                if (self.in_discards.is_set or self.in_discards.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.in_discards.get_name_leafdata())
                                if (self.in_fcs_err.is_set or self.in_fcs_err.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.in_fcs_err.get_name_leafdata())
                                if (self.in_filtered.is_set or self.in_filtered.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.in_filtered.get_name_leafdata())
                                if (self.in_fragments.is_set or self.in_fragments.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.in_fragments.get_name_leafdata())
                                if (self.in_good_octets.is_set or self.in_good_octets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.in_good_octets.get_name_leafdata())
                                if (self.in_good_octets_hi.is_set or self.in_good_octets_hi.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.in_good_octets_hi.get_name_leafdata())
                                if (self.in_jabber.is_set or self.in_jabber.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.in_jabber.get_name_leafdata())
                                if (self.in_mcast_pkt.is_set or self.in_mcast_pkt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.in_mcast_pkt.get_name_leafdata())
                                if (self.in_oversize.is_set or self.in_oversize.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.in_oversize.get_name_leafdata())
                                if (self.in_pause_pkt.is_set or self.in_pause_pkt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.in_pause_pkt.get_name_leafdata())
                                if (self.in_rx_err.is_set or self.in_rx_err.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.in_rx_err.get_name_leafdata())
                                if (self.in_undersize_pkt.is_set or self.in_undersize_pkt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.in_undersize_pkt.get_name_leafdata())
                                if (self.in_unicast_pkt.is_set or self.in_unicast_pkt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.in_unicast_pkt.get_name_leafdata())
                                if (self.late.is_set or self.late.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.late.get_name_leafdata())
                                if (self.multiple.is_set or self.multiple.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.multiple.get_name_leafdata())
                                if (self.out_bcast_pkt.is_set or self.out_bcast_pkt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.out_bcast_pkt.get_name_leafdata())
                                if (self.out_fcs_err.is_set or self.out_fcs_err.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.out_fcs_err.get_name_leafdata())
                                if (self.out_filtered.is_set or self.out_filtered.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.out_filtered.get_name_leafdata())
                                if (self.out_mcast_pkt.is_set or self.out_mcast_pkt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.out_mcast_pkt.get_name_leafdata())
                                if (self.out_octets.is_set or self.out_octets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.out_octets.get_name_leafdata())
                                if (self.out_octets_hi.is_set or self.out_octets_hi.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.out_octets_hi.get_name_leafdata())
                                if (self.out_pause_pkt.is_set or self.out_pause_pkt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.out_pause_pkt.get_name_leafdata())
                                if (self.out_unicast_pkt.is_set or self.out_unicast_pkt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.out_unicast_pkt.get_name_leafdata())
                                if (self.rx_tx_1024_max_octets.is_set or self.rx_tx_1024_max_octets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.rx_tx_1024_max_octets.get_name_leafdata())
                                if (self.rx_tx_128_255_octets.is_set or self.rx_tx_128_255_octets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.rx_tx_128_255_octets.get_name_leafdata())
                                if (self.rx_tx_256_511_octets.is_set or self.rx_tx_256_511_octets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.rx_tx_256_511_octets.get_name_leafdata())
                                if (self.rx_tx_512_1023_octets.is_set or self.rx_tx_512_1023_octets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.rx_tx_512_1023_octets.get_name_leafdata())
                                if (self.rx_tx_64_octets.is_set or self.rx_tx_64_octets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.rx_tx_64_octets.get_name_leafdata())
                                if (self.rx_tx_65_127_octets.is_set or self.rx_tx_65_127_octets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.rx_tx_65_127_octets.get_name_leafdata())
                                if (self.single.is_set or self.single.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.single.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "collisions" or name == "deferred" or name == "excessive" or name == "in-bad-octets" or name == "in-bcast-pkt" or name == "in-discards" or name == "in-fcs-err" or name == "in-filtered" or name == "in-fragments" or name == "in-good-octets" or name == "in-good-octets-hi" or name == "in-jabber" or name == "in-mcast-pkt" or name == "in-oversize" or name == "in-pause-pkt" or name == "in-rx-err" or name == "in-undersize-pkt" or name == "in-unicast-pkt" or name == "late" or name == "multiple" or name == "out-bcast-pkt" or name == "out-fcs-err" or name == "out-filtered" or name == "out-mcast-pkt" or name == "out-octets" or name == "out-octets-hi" or name == "out-pause-pkt" or name == "out-unicast-pkt" or name == "rx-tx-1024-max-octets" or name == "rx-tx-128-255-octets" or name == "rx-tx-256-511-octets" or name == "rx-tx-512-1023-octets" or name == "rx-tx-64-octets" or name == "rx-tx-65-127-octets" or name == "single"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "collisions"):
                                    self.collisions = value
                                    self.collisions.value_namespace = name_space
                                    self.collisions.value_namespace_prefix = name_space_prefix
                                if(value_path == "deferred"):
                                    self.deferred = value
                                    self.deferred.value_namespace = name_space
                                    self.deferred.value_namespace_prefix = name_space_prefix
                                if(value_path == "excessive"):
                                    self.excessive = value
                                    self.excessive.value_namespace = name_space
                                    self.excessive.value_namespace_prefix = name_space_prefix
                                if(value_path == "in-bad-octets"):
                                    self.in_bad_octets = value
                                    self.in_bad_octets.value_namespace = name_space
                                    self.in_bad_octets.value_namespace_prefix = name_space_prefix
                                if(value_path == "in-bcast-pkt"):
                                    self.in_bcast_pkt = value
                                    self.in_bcast_pkt.value_namespace = name_space
                                    self.in_bcast_pkt.value_namespace_prefix = name_space_prefix
                                if(value_path == "in-discards"):
                                    self.in_discards = value
                                    self.in_discards.value_namespace = name_space
                                    self.in_discards.value_namespace_prefix = name_space_prefix
                                if(value_path == "in-fcs-err"):
                                    self.in_fcs_err = value
                                    self.in_fcs_err.value_namespace = name_space
                                    self.in_fcs_err.value_namespace_prefix = name_space_prefix
                                if(value_path == "in-filtered"):
                                    self.in_filtered = value
                                    self.in_filtered.value_namespace = name_space
                                    self.in_filtered.value_namespace_prefix = name_space_prefix
                                if(value_path == "in-fragments"):
                                    self.in_fragments = value
                                    self.in_fragments.value_namespace = name_space
                                    self.in_fragments.value_namespace_prefix = name_space_prefix
                                if(value_path == "in-good-octets"):
                                    self.in_good_octets = value
                                    self.in_good_octets.value_namespace = name_space
                                    self.in_good_octets.value_namespace_prefix = name_space_prefix
                                if(value_path == "in-good-octets-hi"):
                                    self.in_good_octets_hi = value
                                    self.in_good_octets_hi.value_namespace = name_space
                                    self.in_good_octets_hi.value_namespace_prefix = name_space_prefix
                                if(value_path == "in-jabber"):
                                    self.in_jabber = value
                                    self.in_jabber.value_namespace = name_space
                                    self.in_jabber.value_namespace_prefix = name_space_prefix
                                if(value_path == "in-mcast-pkt"):
                                    self.in_mcast_pkt = value
                                    self.in_mcast_pkt.value_namespace = name_space
                                    self.in_mcast_pkt.value_namespace_prefix = name_space_prefix
                                if(value_path == "in-oversize"):
                                    self.in_oversize = value
                                    self.in_oversize.value_namespace = name_space
                                    self.in_oversize.value_namespace_prefix = name_space_prefix
                                if(value_path == "in-pause-pkt"):
                                    self.in_pause_pkt = value
                                    self.in_pause_pkt.value_namespace = name_space
                                    self.in_pause_pkt.value_namespace_prefix = name_space_prefix
                                if(value_path == "in-rx-err"):
                                    self.in_rx_err = value
                                    self.in_rx_err.value_namespace = name_space
                                    self.in_rx_err.value_namespace_prefix = name_space_prefix
                                if(value_path == "in-undersize-pkt"):
                                    self.in_undersize_pkt = value
                                    self.in_undersize_pkt.value_namespace = name_space
                                    self.in_undersize_pkt.value_namespace_prefix = name_space_prefix
                                if(value_path == "in-unicast-pkt"):
                                    self.in_unicast_pkt = value
                                    self.in_unicast_pkt.value_namespace = name_space
                                    self.in_unicast_pkt.value_namespace_prefix = name_space_prefix
                                if(value_path == "late"):
                                    self.late = value
                                    self.late.value_namespace = name_space
                                    self.late.value_namespace_prefix = name_space_prefix
                                if(value_path == "multiple"):
                                    self.multiple = value
                                    self.multiple.value_namespace = name_space
                                    self.multiple.value_namespace_prefix = name_space_prefix
                                if(value_path == "out-bcast-pkt"):
                                    self.out_bcast_pkt = value
                                    self.out_bcast_pkt.value_namespace = name_space
                                    self.out_bcast_pkt.value_namespace_prefix = name_space_prefix
                                if(value_path == "out-fcs-err"):
                                    self.out_fcs_err = value
                                    self.out_fcs_err.value_namespace = name_space
                                    self.out_fcs_err.value_namespace_prefix = name_space_prefix
                                if(value_path == "out-filtered"):
                                    self.out_filtered = value
                                    self.out_filtered.value_namespace = name_space
                                    self.out_filtered.value_namespace_prefix = name_space_prefix
                                if(value_path == "out-mcast-pkt"):
                                    self.out_mcast_pkt = value
                                    self.out_mcast_pkt.value_namespace = name_space
                                    self.out_mcast_pkt.value_namespace_prefix = name_space_prefix
                                if(value_path == "out-octets"):
                                    self.out_octets = value
                                    self.out_octets.value_namespace = name_space
                                    self.out_octets.value_namespace_prefix = name_space_prefix
                                if(value_path == "out-octets-hi"):
                                    self.out_octets_hi = value
                                    self.out_octets_hi.value_namespace = name_space
                                    self.out_octets_hi.value_namespace_prefix = name_space_prefix
                                if(value_path == "out-pause-pkt"):
                                    self.out_pause_pkt = value
                                    self.out_pause_pkt.value_namespace = name_space
                                    self.out_pause_pkt.value_namespace_prefix = name_space_prefix
                                if(value_path == "out-unicast-pkt"):
                                    self.out_unicast_pkt = value
                                    self.out_unicast_pkt.value_namespace = name_space
                                    self.out_unicast_pkt.value_namespace_prefix = name_space_prefix
                                if(value_path == "rx-tx-1024-max-octets"):
                                    self.rx_tx_1024_max_octets = value
                                    self.rx_tx_1024_max_octets.value_namespace = name_space
                                    self.rx_tx_1024_max_octets.value_namespace_prefix = name_space_prefix
                                if(value_path == "rx-tx-128-255-octets"):
                                    self.rx_tx_128_255_octets = value
                                    self.rx_tx_128_255_octets.value_namespace = name_space
                                    self.rx_tx_128_255_octets.value_namespace_prefix = name_space_prefix
                                if(value_path == "rx-tx-256-511-octets"):
                                    self.rx_tx_256_511_octets = value
                                    self.rx_tx_256_511_octets.value_namespace = name_space
                                    self.rx_tx_256_511_octets.value_namespace_prefix = name_space_prefix
                                if(value_path == "rx-tx-512-1023-octets"):
                                    self.rx_tx_512_1023_octets = value
                                    self.rx_tx_512_1023_octets.value_namespace = name_space
                                    self.rx_tx_512_1023_octets.value_namespace_prefix = name_space_prefix
                                if(value_path == "rx-tx-64-octets"):
                                    self.rx_tx_64_octets = value
                                    self.rx_tx_64_octets.value_namespace = name_space
                                    self.rx_tx_64_octets.value_namespace_prefix = name_space_prefix
                                if(value_path == "rx-tx-65-127-octets"):
                                    self.rx_tx_65_127_octets = value
                                    self.rx_tx_65_127_octets.value_namespace = name_space
                                    self.rx_tx_65_127_octets.value_namespace_prefix = name_space_prefix
                                if(value_path == "single"):
                                    self.single = value
                                    self.single.value_namespace = name_space
                                    self.single.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.port_num.is_set or
                                (self.mlan_stats is not None and self.mlan_stats.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.port_num.yfilter != YFilter.not_set or
                                (self.mlan_stats is not None and self.mlan_stats.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "port-counters" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.port_num.is_set or self.port_num.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.port_num.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "mlan-stats"):
                                if (self.mlan_stats is None):
                                    self.mlan_stats = Mlan.Nodes.Node.PortCountersNumbers.PortCountersNumber.PortCounters.MlanStats()
                                    self.mlan_stats.parent = self
                                    self._children_name_map["mlan_stats"] = "mlan-stats"
                                return self.mlan_stats

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "mlan-stats" or name == "port-num"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "port-num"):
                                self.port_num = value
                                self.port_num.value_namespace = name_space
                                self.port_num.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.number.is_set or
                            (self.port_counters is not None and self.port_counters.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.number.yfilter != YFilter.not_set or
                            (self.port_counters is not None and self.port_counters.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "port-counters-number" + "[number='" + self.number.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.number.is_set or self.number.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.number.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "port-counters"):
                            if (self.port_counters is None):
                                self.port_counters = Mlan.Nodes.Node.PortCountersNumbers.PortCountersNumber.PortCounters()
                                self.port_counters.parent = self
                                self._children_name_map["port_counters"] = "port-counters"
                            return self.port_counters

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "port-counters" or name == "number"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "number"):
                            self.number = value
                            self.number.value_namespace = name_space
                            self.number.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.port_counters_number:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.port_counters_number:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "port-counters-numbers" + path_buffer

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

                    if (child_yang_name == "port-counters-number"):
                        for c in self.port_counters_number:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Mlan.Nodes.Node.PortCountersNumbers.PortCountersNumber()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.port_counters_number.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "port-counters-number"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class AtuEntryNumbers(Entity):
                """
                Table of switch ATU
                
                .. attribute:: atu_entry_number
                
                	Entry number
                	**type**\: list of    :py:class:`AtuEntryNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper.Mlan.Nodes.Node.AtuEntryNumbers.AtuEntryNumber>`
                
                

                """

                _prefix = 'asr9k-lc-ethctrl-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Mlan.Nodes.Node.AtuEntryNumbers, self).__init__()

                    self.yang_name = "atu-entry-numbers"
                    self.yang_parent_name = "node"

                    self.atu_entry_number = YList(self)

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
                                super(Mlan.Nodes.Node.AtuEntryNumbers, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Mlan.Nodes.Node.AtuEntryNumbers, self).__setattr__(name, value)


                class AtuEntryNumber(Entity):
                    """
                    Entry number
                    
                    .. attribute:: entry  <key>
                    
                    	entry number
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: switch_counters
                    
                    	mlan switch counters info
                    	**type**\:   :py:class:`SwitchCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper.Mlan.Nodes.Node.AtuEntryNumbers.AtuEntryNumber.SwitchCounters>`
                    
                    

                    """

                    _prefix = 'asr9k-lc-ethctrl-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Mlan.Nodes.Node.AtuEntryNumbers.AtuEntryNumber, self).__init__()

                        self.yang_name = "atu-entry-number"
                        self.yang_parent_name = "atu-entry-numbers"

                        self.entry = YLeaf(YType.int32, "entry")

                        self.switch_counters = Mlan.Nodes.Node.AtuEntryNumbers.AtuEntryNumber.SwitchCounters()
                        self.switch_counters.parent = self
                        self._children_name_map["switch_counters"] = "switch-counters"
                        self._children_yang_names.add("switch-counters")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("entry") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Mlan.Nodes.Node.AtuEntryNumbers.AtuEntryNumber, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Mlan.Nodes.Node.AtuEntryNumbers.AtuEntryNumber, self).__setattr__(name, value)


                    class SwitchCounters(Entity):
                        """
                        mlan switch counters info
                        
                        .. attribute:: atu
                        
                        	Switch ATU Data
                        	**type**\:   :py:class:`Atu <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper.Mlan.Nodes.Node.AtuEntryNumbers.AtuEntryNumber.SwitchCounters.Atu>`
                        
                        .. attribute:: entry_num
                        
                        	Index of ATU Entry
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'asr9k-lc-ethctrl-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Mlan.Nodes.Node.AtuEntryNumbers.AtuEntryNumber.SwitchCounters, self).__init__()

                            self.yang_name = "switch-counters"
                            self.yang_parent_name = "atu-entry-number"

                            self.entry_num = YLeaf(YType.uint32, "entry-num")

                            self.atu = Mlan.Nodes.Node.AtuEntryNumbers.AtuEntryNumber.SwitchCounters.Atu()
                            self.atu.parent = self
                            self._children_name_map["atu"] = "atu"
                            self._children_yang_names.add("atu")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("entry_num") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Mlan.Nodes.Node.AtuEntryNumbers.AtuEntryNumber.SwitchCounters, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Mlan.Nodes.Node.AtuEntryNumbers.AtuEntryNumber.SwitchCounters, self).__setattr__(name, value)


                        class Atu(Entity):
                            """
                            Switch ATU Data
                            
                            .. attribute:: db_num
                            
                            	dbNum
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: dpv
                            
                            	dpv
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: es
                            
                            	es
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: macaddr
                            
                            	macaddr
                            	**type**\:  list of int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: priority
                            
                            	priority
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: trunk
                            
                            	trunk
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'asr9k-lc-ethctrl-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Mlan.Nodes.Node.AtuEntryNumbers.AtuEntryNumber.SwitchCounters.Atu, self).__init__()

                                self.yang_name = "atu"
                                self.yang_parent_name = "switch-counters"

                                self.db_num = YLeaf(YType.uint16, "db-num")

                                self.dpv = YLeaf(YType.uint8, "dpv")

                                self.es = YLeaf(YType.uint8, "es")

                                self.macaddr = YLeafList(YType.uint16, "macaddr")

                                self.priority = YLeaf(YType.uint8, "priority")

                                self.trunk = YLeaf(YType.boolean, "trunk")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("db_num",
                                                "dpv",
                                                "es",
                                                "macaddr",
                                                "priority",
                                                "trunk") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Mlan.Nodes.Node.AtuEntryNumbers.AtuEntryNumber.SwitchCounters.Atu, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Mlan.Nodes.Node.AtuEntryNumbers.AtuEntryNumber.SwitchCounters.Atu, self).__setattr__(name, value)

                            def has_data(self):
                                for leaf in self.macaddr.getYLeafs():
                                    if (leaf.yfilter != YFilter.not_set):
                                        return True
                                return (
                                    self.db_num.is_set or
                                    self.dpv.is_set or
                                    self.es.is_set or
                                    self.priority.is_set or
                                    self.trunk.is_set)

                            def has_operation(self):
                                for leaf in self.macaddr.getYLeafs():
                                    if (leaf.is_set):
                                        return True
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.db_num.yfilter != YFilter.not_set or
                                    self.dpv.yfilter != YFilter.not_set or
                                    self.es.yfilter != YFilter.not_set or
                                    self.macaddr.yfilter != YFilter.not_set or
                                    self.priority.yfilter != YFilter.not_set or
                                    self.trunk.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "atu" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.db_num.is_set or self.db_num.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.db_num.get_name_leafdata())
                                if (self.dpv.is_set or self.dpv.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.dpv.get_name_leafdata())
                                if (self.es.is_set or self.es.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.es.get_name_leafdata())
                                if (self.priority.is_set or self.priority.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.priority.get_name_leafdata())
                                if (self.trunk.is_set or self.trunk.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.trunk.get_name_leafdata())

                                leaf_name_data.extend(self.macaddr.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "db-num" or name == "dpv" or name == "es" or name == "macaddr" or name == "priority" or name == "trunk"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "db-num"):
                                    self.db_num = value
                                    self.db_num.value_namespace = name_space
                                    self.db_num.value_namespace_prefix = name_space_prefix
                                if(value_path == "dpv"):
                                    self.dpv = value
                                    self.dpv.value_namespace = name_space
                                    self.dpv.value_namespace_prefix = name_space_prefix
                                if(value_path == "es"):
                                    self.es = value
                                    self.es.value_namespace = name_space
                                    self.es.value_namespace_prefix = name_space_prefix
                                if(value_path == "macaddr"):
                                    self.macaddr.append(value)
                                if(value_path == "priority"):
                                    self.priority = value
                                    self.priority.value_namespace = name_space
                                    self.priority.value_namespace_prefix = name_space_prefix
                                if(value_path == "trunk"):
                                    self.trunk = value
                                    self.trunk.value_namespace = name_space
                                    self.trunk.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.entry_num.is_set or
                                (self.atu is not None and self.atu.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.entry_num.yfilter != YFilter.not_set or
                                (self.atu is not None and self.atu.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "switch-counters" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.entry_num.is_set or self.entry_num.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.entry_num.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "atu"):
                                if (self.atu is None):
                                    self.atu = Mlan.Nodes.Node.AtuEntryNumbers.AtuEntryNumber.SwitchCounters.Atu()
                                    self.atu.parent = self
                                    self._children_name_map["atu"] = "atu"
                                return self.atu

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "atu" or name == "entry-num"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "entry-num"):
                                self.entry_num = value
                                self.entry_num.value_namespace = name_space
                                self.entry_num.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.entry.is_set or
                            (self.switch_counters is not None and self.switch_counters.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.entry.yfilter != YFilter.not_set or
                            (self.switch_counters is not None and self.switch_counters.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "atu-entry-number" + "[entry='" + self.entry.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.entry.is_set or self.entry.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.entry.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "switch-counters"):
                            if (self.switch_counters is None):
                                self.switch_counters = Mlan.Nodes.Node.AtuEntryNumbers.AtuEntryNumber.SwitchCounters()
                                self.switch_counters.parent = self
                                self._children_name_map["switch_counters"] = "switch-counters"
                            return self.switch_counters

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "switch-counters" or name == "entry"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "entry"):
                            self.entry = value
                            self.entry.value_namespace = name_space
                            self.entry.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.atu_entry_number:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.atu_entry_number:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "atu-entry-numbers" + path_buffer

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

                    if (child_yang_name == "atu-entry-number"):
                        for c in self.atu_entry_number:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Mlan.Nodes.Node.AtuEntryNumbers.AtuEntryNumber()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.atu_entry_number.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "atu-entry-number"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.node.is_set or
                    (self.atu_entry_numbers is not None and self.atu_entry_numbers.has_data()) or
                    (self.port_counters_numbers is not None and self.port_counters_numbers.has_data()) or
                    (self.port_status_numbers is not None and self.port_status_numbers.has_data()) or
                    (self.switch_status_table is not None and self.switch_status_table.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.node.yfilter != YFilter.not_set or
                    (self.atu_entry_numbers is not None and self.atu_entry_numbers.has_operation()) or
                    (self.port_counters_numbers is not None and self.port_counters_numbers.has_operation()) or
                    (self.port_status_numbers is not None and self.port_status_numbers.has_operation()) or
                    (self.switch_status_table is not None and self.switch_status_table.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "node" + "[node='" + self.node.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-asr9k-lc-ethctrl-oper:mlan/nodes/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.node.is_set or self.node.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.node.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "atu-entry-numbers"):
                    if (self.atu_entry_numbers is None):
                        self.atu_entry_numbers = Mlan.Nodes.Node.AtuEntryNumbers()
                        self.atu_entry_numbers.parent = self
                        self._children_name_map["atu_entry_numbers"] = "atu-entry-numbers"
                    return self.atu_entry_numbers

                if (child_yang_name == "port-counters-numbers"):
                    if (self.port_counters_numbers is None):
                        self.port_counters_numbers = Mlan.Nodes.Node.PortCountersNumbers()
                        self.port_counters_numbers.parent = self
                        self._children_name_map["port_counters_numbers"] = "port-counters-numbers"
                    return self.port_counters_numbers

                if (child_yang_name == "port-status-numbers"):
                    if (self.port_status_numbers is None):
                        self.port_status_numbers = Mlan.Nodes.Node.PortStatusNumbers()
                        self.port_status_numbers.parent = self
                        self._children_name_map["port_status_numbers"] = "port-status-numbers"
                    return self.port_status_numbers

                if (child_yang_name == "switch-status-table"):
                    if (self.switch_status_table is None):
                        self.switch_status_table = Mlan.Nodes.Node.SwitchStatusTable()
                        self.switch_status_table.parent = self
                        self._children_name_map["switch_status_table"] = "switch-status-table"
                    return self.switch_status_table

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "atu-entry-numbers" or name == "port-counters-numbers" or name == "port-status-numbers" or name == "switch-status-table" or name == "node"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "node"):
                    self.node = value
                    self.node.value_namespace = name_space
                    self.node.value_namespace_prefix = name_space_prefix

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
                path_buffer = "Cisco-IOS-XR-asr9k-lc-ethctrl-oper:mlan/%s" % self.get_segment_path()
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
                c = Mlan.Nodes.Node()
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
        path_buffer = "Cisco-IOS-XR-asr9k-lc-ethctrl-oper:mlan" + path_buffer

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
                self.nodes = Mlan.Nodes()
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
        self._top_entity = Mlan()
        return self._top_entity

