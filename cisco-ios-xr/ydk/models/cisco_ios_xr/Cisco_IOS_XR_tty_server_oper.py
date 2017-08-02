""" Cisco_IOS_XR_tty_server_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR tty\-server package operational data.

This module contains definitions
for the following management objects\:
  tty\: TTY Line Configuration

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class LineState(Enum):
    """
    LineState

    Line state

    .. data:: none = 0

    	Line not connected

    .. data:: registered = 1

    	Line registered

    .. data:: in_use = 2

    	Line active and in use

    """

    none = Enum.YLeaf(0, "none")

    registered = Enum.YLeaf(1, "registered")

    in_use = Enum.YLeaf(2, "in-use")


class SessionOperation(Enum):
    """
    SessionOperation

    Session operation

    .. data:: none = 0

    	No sessions on the line

    .. data:: setup = 1

    	Session getting set up

    .. data:: shell = 2

    	Session active with a shell

    .. data:: transitioning = 3

    	Session in transitioning phase

    .. data:: packet = 4

    	Session ready to receive packets

    """

    none = Enum.YLeaf(0, "none")

    setup = Enum.YLeaf(1, "setup")

    shell = Enum.YLeaf(2, "shell")

    transitioning = Enum.YLeaf(3, "transitioning")

    packet = Enum.YLeaf(4, "packet")



class Tty(Entity):
    """
    TTY Line Configuration
    
    .. attribute:: auxiliary_nodes
    
    	List of Nodes attached with an auxiliary line
    	**type**\:   :py:class:`AuxiliaryNodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.AuxiliaryNodes>`
    
    .. attribute:: console_nodes
    
    	List of Nodes for console
    	**type**\:   :py:class:`ConsoleNodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.ConsoleNodes>`
    
    .. attribute:: vty_lines
    
    	List of VTY lines
    	**type**\:   :py:class:`VtyLines <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.VtyLines>`
    
    

    """

    _prefix = 'tty-server-oper'
    _revision = '2015-07-30'

    def __init__(self):
        super(Tty, self).__init__()
        self._top_entity = None

        self.yang_name = "tty"
        self.yang_parent_name = "Cisco-IOS-XR-tty-server-oper"

        self.auxiliary_nodes = Tty.AuxiliaryNodes()
        self.auxiliary_nodes.parent = self
        self._children_name_map["auxiliary_nodes"] = "auxiliary-nodes"
        self._children_yang_names.add("auxiliary-nodes")

        self.console_nodes = Tty.ConsoleNodes()
        self.console_nodes.parent = self
        self._children_name_map["console_nodes"] = "console-nodes"
        self._children_yang_names.add("console-nodes")

        self.vty_lines = Tty.VtyLines()
        self.vty_lines.parent = self
        self._children_name_map["vty_lines"] = "vty-lines"
        self._children_yang_names.add("vty-lines")


    class ConsoleNodes(Entity):
        """
        List of Nodes for console
        
        .. attribute:: console_node
        
        	Console line configuration on a node
        	**type**\: list of    :py:class:`ConsoleNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.ConsoleNodes.ConsoleNode>`
        
        

        """

        _prefix = 'tty-server-oper'
        _revision = '2015-07-30'

        def __init__(self):
            super(Tty.ConsoleNodes, self).__init__()

            self.yang_name = "console-nodes"
            self.yang_parent_name = "tty"

            self.console_node = YList(self)

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
                        super(Tty.ConsoleNodes, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Tty.ConsoleNodes, self).__setattr__(name, value)


        class ConsoleNode(Entity):
            """
            Console line configuration on a node
            
            .. attribute:: id  <key>
            
            	Node ID
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: console_line
            
            	Console line
            	**type**\:   :py:class:`ConsoleLine <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.ConsoleNodes.ConsoleNode.ConsoleLine>`
            
            

            """

            _prefix = 'tty-server-oper'
            _revision = '2015-07-30'

            def __init__(self):
                super(Tty.ConsoleNodes.ConsoleNode, self).__init__()

                self.yang_name = "console-node"
                self.yang_parent_name = "console-nodes"

                self.id = YLeaf(YType.str, "id")

                self.console_line = Tty.ConsoleNodes.ConsoleNode.ConsoleLine()
                self.console_line.parent = self
                self._children_name_map["console_line"] = "console-line"
                self._children_yang_names.add("console-line")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("id") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Tty.ConsoleNodes.ConsoleNode, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Tty.ConsoleNodes.ConsoleNode, self).__setattr__(name, value)


            class ConsoleLine(Entity):
                """
                Console line
                
                .. attribute:: configuration
                
                	Configuration information of the line
                	**type**\:   :py:class:`Configuration <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.ConsoleNodes.ConsoleNode.ConsoleLine.Configuration>`
                
                .. attribute:: console_statistics
                
                	Statistics of the console line
                	**type**\:   :py:class:`ConsoleStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics>`
                
                .. attribute:: state
                
                	Line state information
                	**type**\:   :py:class:`State <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.ConsoleNodes.ConsoleNode.ConsoleLine.State>`
                
                

                """

                _prefix = 'tty-server-oper'
                _revision = '2015-07-30'

                def __init__(self):
                    super(Tty.ConsoleNodes.ConsoleNode.ConsoleLine, self).__init__()

                    self.yang_name = "console-line"
                    self.yang_parent_name = "console-node"

                    self.configuration = Tty.ConsoleNodes.ConsoleNode.ConsoleLine.Configuration()
                    self.configuration.parent = self
                    self._children_name_map["configuration"] = "configuration"
                    self._children_yang_names.add("configuration")

                    self.console_statistics = Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics()
                    self.console_statistics.parent = self
                    self._children_name_map["console_statistics"] = "console-statistics"
                    self._children_yang_names.add("console-statistics")

                    self.state = Tty.ConsoleNodes.ConsoleNode.ConsoleLine.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._children_yang_names.add("state")


                class ConsoleStatistics(Entity):
                    """
                    Statistics of the console line
                    
                    .. attribute:: aaa
                    
                    	AAA related statistics
                    	**type**\:   :py:class:`Aaa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.Aaa>`
                    
                    .. attribute:: exec_
                    
                    	Exec related statistics
                    	**type**\:   :py:class:`Exec_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.Exec_>`
                    
                    .. attribute:: general_statistics
                    
                    	General statistics of line
                    	**type**\:   :py:class:`GeneralStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.GeneralStatistics>`
                    
                    .. attribute:: rs232
                    
                    	RS232 statistics of console line
                    	**type**\:   :py:class:`Rs232 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.Rs232>`
                    
                    

                    """

                    _prefix = 'tty-server-oper'
                    _revision = '2015-07-30'

                    def __init__(self):
                        super(Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics, self).__init__()

                        self.yang_name = "console-statistics"
                        self.yang_parent_name = "console-line"

                        self.aaa = Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.Aaa()
                        self.aaa.parent = self
                        self._children_name_map["aaa"] = "aaa"
                        self._children_yang_names.add("aaa")

                        self.exec_ = Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.Exec_()
                        self.exec_.parent = self
                        self._children_name_map["exec_"] = "exec"
                        self._children_yang_names.add("exec")

                        self.general_statistics = Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.GeneralStatistics()
                        self.general_statistics.parent = self
                        self._children_name_map["general_statistics"] = "general-statistics"
                        self._children_yang_names.add("general-statistics")

                        self.rs232 = Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.Rs232()
                        self.rs232.parent = self
                        self._children_name_map["rs232"] = "rs232"
                        self._children_yang_names.add("rs232")


                    class Rs232(Entity):
                        """
                        RS232 statistics of console line
                        
                        .. attribute:: baud_rate
                        
                        	Inbound/Outbound baud rate in bps
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: bit/s
                        
                        .. attribute:: data_bits
                        
                        	Number of databits
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: bit
                        
                        .. attribute:: exec_disabled
                        
                        	Exec disabled on TTY
                        	**type**\:  bool
                        
                        .. attribute:: framing_error_count
                        
                        	Framing error count
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: hardware_flow_control_status
                        
                        	Hardware flow control status
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: overrun_error_count
                        
                        	Overrun error count
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: parity_error_count
                        
                        	Parity error count
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: parity_status
                        
                        	Parity status
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: stop_bits
                        
                        	Number of stopbits
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: bit
                        
                        

                        """

                        _prefix = 'tty-server-oper'
                        _revision = '2015-07-30'

                        def __init__(self):
                            super(Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.Rs232, self).__init__()

                            self.yang_name = "rs232"
                            self.yang_parent_name = "console-statistics"

                            self.baud_rate = YLeaf(YType.uint32, "baud-rate")

                            self.data_bits = YLeaf(YType.uint32, "data-bits")

                            self.exec_disabled = YLeaf(YType.boolean, "exec-disabled")

                            self.framing_error_count = YLeaf(YType.uint32, "framing-error-count")

                            self.hardware_flow_control_status = YLeaf(YType.uint32, "hardware-flow-control-status")

                            self.overrun_error_count = YLeaf(YType.uint32, "overrun-error-count")

                            self.parity_error_count = YLeaf(YType.uint32, "parity-error-count")

                            self.parity_status = YLeaf(YType.uint32, "parity-status")

                            self.stop_bits = YLeaf(YType.uint32, "stop-bits")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("baud_rate",
                                            "data_bits",
                                            "exec_disabled",
                                            "framing_error_count",
                                            "hardware_flow_control_status",
                                            "overrun_error_count",
                                            "parity_error_count",
                                            "parity_status",
                                            "stop_bits") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.Rs232, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.Rs232, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.baud_rate.is_set or
                                self.data_bits.is_set or
                                self.exec_disabled.is_set or
                                self.framing_error_count.is_set or
                                self.hardware_flow_control_status.is_set or
                                self.overrun_error_count.is_set or
                                self.parity_error_count.is_set or
                                self.parity_status.is_set or
                                self.stop_bits.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.baud_rate.yfilter != YFilter.not_set or
                                self.data_bits.yfilter != YFilter.not_set or
                                self.exec_disabled.yfilter != YFilter.not_set or
                                self.framing_error_count.yfilter != YFilter.not_set or
                                self.hardware_flow_control_status.yfilter != YFilter.not_set or
                                self.overrun_error_count.yfilter != YFilter.not_set or
                                self.parity_error_count.yfilter != YFilter.not_set or
                                self.parity_status.yfilter != YFilter.not_set or
                                self.stop_bits.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "rs232" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.baud_rate.is_set or self.baud_rate.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.baud_rate.get_name_leafdata())
                            if (self.data_bits.is_set or self.data_bits.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.data_bits.get_name_leafdata())
                            if (self.exec_disabled.is_set or self.exec_disabled.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.exec_disabled.get_name_leafdata())
                            if (self.framing_error_count.is_set or self.framing_error_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.framing_error_count.get_name_leafdata())
                            if (self.hardware_flow_control_status.is_set or self.hardware_flow_control_status.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.hardware_flow_control_status.get_name_leafdata())
                            if (self.overrun_error_count.is_set or self.overrun_error_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.overrun_error_count.get_name_leafdata())
                            if (self.parity_error_count.is_set or self.parity_error_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.parity_error_count.get_name_leafdata())
                            if (self.parity_status.is_set or self.parity_status.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.parity_status.get_name_leafdata())
                            if (self.stop_bits.is_set or self.stop_bits.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.stop_bits.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "baud-rate" or name == "data-bits" or name == "exec-disabled" or name == "framing-error-count" or name == "hardware-flow-control-status" or name == "overrun-error-count" or name == "parity-error-count" or name == "parity-status" or name == "stop-bits"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "baud-rate"):
                                self.baud_rate = value
                                self.baud_rate.value_namespace = name_space
                                self.baud_rate.value_namespace_prefix = name_space_prefix
                            if(value_path == "data-bits"):
                                self.data_bits = value
                                self.data_bits.value_namespace = name_space
                                self.data_bits.value_namespace_prefix = name_space_prefix
                            if(value_path == "exec-disabled"):
                                self.exec_disabled = value
                                self.exec_disabled.value_namespace = name_space
                                self.exec_disabled.value_namespace_prefix = name_space_prefix
                            if(value_path == "framing-error-count"):
                                self.framing_error_count = value
                                self.framing_error_count.value_namespace = name_space
                                self.framing_error_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "hardware-flow-control-status"):
                                self.hardware_flow_control_status = value
                                self.hardware_flow_control_status.value_namespace = name_space
                                self.hardware_flow_control_status.value_namespace_prefix = name_space_prefix
                            if(value_path == "overrun-error-count"):
                                self.overrun_error_count = value
                                self.overrun_error_count.value_namespace = name_space
                                self.overrun_error_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "parity-error-count"):
                                self.parity_error_count = value
                                self.parity_error_count.value_namespace = name_space
                                self.parity_error_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "parity-status"):
                                self.parity_status = value
                                self.parity_status.value_namespace = name_space
                                self.parity_status.value_namespace_prefix = name_space_prefix
                            if(value_path == "stop-bits"):
                                self.stop_bits = value
                                self.stop_bits.value_namespace = name_space
                                self.stop_bits.value_namespace_prefix = name_space_prefix


                    class GeneralStatistics(Entity):
                        """
                        General statistics of line
                        
                        .. attribute:: absolute_timeout
                        
                        	Absolute timeout period
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: async_interface
                        
                        	Usable as async interface
                        	**type**\:  bool
                        
                        .. attribute:: domain_lookup_enabled
                        
                        	DNS resolution enabled
                        	**type**\:  bool
                        
                        .. attribute:: flow_control_start_character
                        
                        	Software flow control start char
                        	**type**\:  int
                        
                        	**range:** \-128..127
                        
                        .. attribute:: flow_control_stop_character
                        
                        	Software flow control stop char
                        	**type**\:  int
                        
                        	**range:** \-128..127
                        
                        .. attribute:: idle_time
                        
                        	TTY idle time
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: motd_banner_enabled
                        
                        	MOTD banner enabled
                        	**type**\:  bool
                        
                        .. attribute:: private_flag
                        
                        	TTY private flag
                        	**type**\:  bool
                        
                        .. attribute:: terminal_length
                        
                        	Terminal length
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: terminal_type
                        
                        	Terminal type
                        	**type**\:  str
                        
                        .. attribute:: terminal_width
                        
                        	Line width
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'tty-server-oper'
                        _revision = '2015-07-30'

                        def __init__(self):
                            super(Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.GeneralStatistics, self).__init__()

                            self.yang_name = "general-statistics"
                            self.yang_parent_name = "console-statistics"

                            self.absolute_timeout = YLeaf(YType.uint32, "absolute-timeout")

                            self.async_interface = YLeaf(YType.boolean, "async-interface")

                            self.domain_lookup_enabled = YLeaf(YType.boolean, "domain-lookup-enabled")

                            self.flow_control_start_character = YLeaf(YType.int8, "flow-control-start-character")

                            self.flow_control_stop_character = YLeaf(YType.int8, "flow-control-stop-character")

                            self.idle_time = YLeaf(YType.uint32, "idle-time")

                            self.motd_banner_enabled = YLeaf(YType.boolean, "motd-banner-enabled")

                            self.private_flag = YLeaf(YType.boolean, "private-flag")

                            self.terminal_length = YLeaf(YType.uint32, "terminal-length")

                            self.terminal_type = YLeaf(YType.str, "terminal-type")

                            self.terminal_width = YLeaf(YType.uint32, "terminal-width")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("absolute_timeout",
                                            "async_interface",
                                            "domain_lookup_enabled",
                                            "flow_control_start_character",
                                            "flow_control_stop_character",
                                            "idle_time",
                                            "motd_banner_enabled",
                                            "private_flag",
                                            "terminal_length",
                                            "terminal_type",
                                            "terminal_width") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.GeneralStatistics, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.GeneralStatistics, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.absolute_timeout.is_set or
                                self.async_interface.is_set or
                                self.domain_lookup_enabled.is_set or
                                self.flow_control_start_character.is_set or
                                self.flow_control_stop_character.is_set or
                                self.idle_time.is_set or
                                self.motd_banner_enabled.is_set or
                                self.private_flag.is_set or
                                self.terminal_length.is_set or
                                self.terminal_type.is_set or
                                self.terminal_width.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.absolute_timeout.yfilter != YFilter.not_set or
                                self.async_interface.yfilter != YFilter.not_set or
                                self.domain_lookup_enabled.yfilter != YFilter.not_set or
                                self.flow_control_start_character.yfilter != YFilter.not_set or
                                self.flow_control_stop_character.yfilter != YFilter.not_set or
                                self.idle_time.yfilter != YFilter.not_set or
                                self.motd_banner_enabled.yfilter != YFilter.not_set or
                                self.private_flag.yfilter != YFilter.not_set or
                                self.terminal_length.yfilter != YFilter.not_set or
                                self.terminal_type.yfilter != YFilter.not_set or
                                self.terminal_width.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "general-statistics" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.absolute_timeout.is_set or self.absolute_timeout.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.absolute_timeout.get_name_leafdata())
                            if (self.async_interface.is_set or self.async_interface.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.async_interface.get_name_leafdata())
                            if (self.domain_lookup_enabled.is_set or self.domain_lookup_enabled.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.domain_lookup_enabled.get_name_leafdata())
                            if (self.flow_control_start_character.is_set or self.flow_control_start_character.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.flow_control_start_character.get_name_leafdata())
                            if (self.flow_control_stop_character.is_set or self.flow_control_stop_character.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.flow_control_stop_character.get_name_leafdata())
                            if (self.idle_time.is_set or self.idle_time.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.idle_time.get_name_leafdata())
                            if (self.motd_banner_enabled.is_set or self.motd_banner_enabled.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.motd_banner_enabled.get_name_leafdata())
                            if (self.private_flag.is_set or self.private_flag.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.private_flag.get_name_leafdata())
                            if (self.terminal_length.is_set or self.terminal_length.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.terminal_length.get_name_leafdata())
                            if (self.terminal_type.is_set or self.terminal_type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.terminal_type.get_name_leafdata())
                            if (self.terminal_width.is_set or self.terminal_width.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.terminal_width.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "absolute-timeout" or name == "async-interface" or name == "domain-lookup-enabled" or name == "flow-control-start-character" or name == "flow-control-stop-character" or name == "idle-time" or name == "motd-banner-enabled" or name == "private-flag" or name == "terminal-length" or name == "terminal-type" or name == "terminal-width"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "absolute-timeout"):
                                self.absolute_timeout = value
                                self.absolute_timeout.value_namespace = name_space
                                self.absolute_timeout.value_namespace_prefix = name_space_prefix
                            if(value_path == "async-interface"):
                                self.async_interface = value
                                self.async_interface.value_namespace = name_space
                                self.async_interface.value_namespace_prefix = name_space_prefix
                            if(value_path == "domain-lookup-enabled"):
                                self.domain_lookup_enabled = value
                                self.domain_lookup_enabled.value_namespace = name_space
                                self.domain_lookup_enabled.value_namespace_prefix = name_space_prefix
                            if(value_path == "flow-control-start-character"):
                                self.flow_control_start_character = value
                                self.flow_control_start_character.value_namespace = name_space
                                self.flow_control_start_character.value_namespace_prefix = name_space_prefix
                            if(value_path == "flow-control-stop-character"):
                                self.flow_control_stop_character = value
                                self.flow_control_stop_character.value_namespace = name_space
                                self.flow_control_stop_character.value_namespace_prefix = name_space_prefix
                            if(value_path == "idle-time"):
                                self.idle_time = value
                                self.idle_time.value_namespace = name_space
                                self.idle_time.value_namespace_prefix = name_space_prefix
                            if(value_path == "motd-banner-enabled"):
                                self.motd_banner_enabled = value
                                self.motd_banner_enabled.value_namespace = name_space
                                self.motd_banner_enabled.value_namespace_prefix = name_space_prefix
                            if(value_path == "private-flag"):
                                self.private_flag = value
                                self.private_flag.value_namespace = name_space
                                self.private_flag.value_namespace_prefix = name_space_prefix
                            if(value_path == "terminal-length"):
                                self.terminal_length = value
                                self.terminal_length.value_namespace = name_space
                                self.terminal_length.value_namespace_prefix = name_space_prefix
                            if(value_path == "terminal-type"):
                                self.terminal_type = value
                                self.terminal_type.value_namespace = name_space
                                self.terminal_type.value_namespace_prefix = name_space_prefix
                            if(value_path == "terminal-width"):
                                self.terminal_width = value
                                self.terminal_width.value_namespace = name_space
                                self.terminal_width.value_namespace_prefix = name_space_prefix


                    class Exec_(Entity):
                        """
                        Exec related statistics
                        
                        .. attribute:: time_stamp_enabled
                        
                        	Specifies whether timestamp is enabled or not
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'tty-server-oper'
                        _revision = '2015-07-30'

                        def __init__(self):
                            super(Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.Exec_, self).__init__()

                            self.yang_name = "exec"
                            self.yang_parent_name = "console-statistics"

                            self.time_stamp_enabled = YLeaf(YType.boolean, "time-stamp-enabled")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("time_stamp_enabled") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.Exec_, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.Exec_, self).__setattr__(name, value)

                        def has_data(self):
                            return self.time_stamp_enabled.is_set

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.time_stamp_enabled.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "exec" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.time_stamp_enabled.is_set or self.time_stamp_enabled.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.time_stamp_enabled.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "time-stamp-enabled"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "time-stamp-enabled"):
                                self.time_stamp_enabled = value
                                self.time_stamp_enabled.value_namespace = name_space
                                self.time_stamp_enabled.value_namespace_prefix = name_space_prefix


                    class Aaa(Entity):
                        """
                        AAA related statistics
                        
                        .. attribute:: user_name
                        
                        	The authenticated username
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'tty-server-oper'
                        _revision = '2015-07-30'

                        def __init__(self):
                            super(Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.Aaa, self).__init__()

                            self.yang_name = "aaa"
                            self.yang_parent_name = "console-statistics"

                            self.user_name = YLeaf(YType.str, "user-name")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("user_name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.Aaa, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.Aaa, self).__setattr__(name, value)

                        def has_data(self):
                            return self.user_name.is_set

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.user_name.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "aaa" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.user_name.is_set or self.user_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.user_name.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "user-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "user-name"):
                                self.user_name = value
                                self.user_name.value_namespace = name_space
                                self.user_name.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            (self.aaa is not None and self.aaa.has_data()) or
                            (self.exec_ is not None and self.exec_.has_data()) or
                            (self.general_statistics is not None and self.general_statistics.has_data()) or
                            (self.rs232 is not None and self.rs232.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.aaa is not None and self.aaa.has_operation()) or
                            (self.exec_ is not None and self.exec_.has_operation()) or
                            (self.general_statistics is not None and self.general_statistics.has_operation()) or
                            (self.rs232 is not None and self.rs232.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "console-statistics" + path_buffer

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

                        if (child_yang_name == "aaa"):
                            if (self.aaa is None):
                                self.aaa = Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.Aaa()
                                self.aaa.parent = self
                                self._children_name_map["aaa"] = "aaa"
                            return self.aaa

                        if (child_yang_name == "exec"):
                            if (self.exec_ is None):
                                self.exec_ = Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.Exec_()
                                self.exec_.parent = self
                                self._children_name_map["exec_"] = "exec"
                            return self.exec_

                        if (child_yang_name == "general-statistics"):
                            if (self.general_statistics is None):
                                self.general_statistics = Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.GeneralStatistics()
                                self.general_statistics.parent = self
                                self._children_name_map["general_statistics"] = "general-statistics"
                            return self.general_statistics

                        if (child_yang_name == "rs232"):
                            if (self.rs232 is None):
                                self.rs232 = Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.Rs232()
                                self.rs232.parent = self
                                self._children_name_map["rs232"] = "rs232"
                            return self.rs232

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "aaa" or name == "exec" or name == "general-statistics" or name == "rs232"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class State(Entity):
                    """
                    Line state information
                    
                    .. attribute:: general
                    
                    	General information
                    	**type**\:   :py:class:`General <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.ConsoleNodes.ConsoleNode.ConsoleLine.State.General>`
                    
                    .. attribute:: template
                    
                    	Information related to template applied to the line
                    	**type**\:   :py:class:`Template <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.ConsoleNodes.ConsoleNode.ConsoleLine.State.Template>`
                    
                    

                    """

                    _prefix = 'tty-server-oper'
                    _revision = '2015-07-30'

                    def __init__(self):
                        super(Tty.ConsoleNodes.ConsoleNode.ConsoleLine.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "console-line"

                        self.general = Tty.ConsoleNodes.ConsoleNode.ConsoleLine.State.General()
                        self.general.parent = self
                        self._children_name_map["general"] = "general"
                        self._children_yang_names.add("general")

                        self.template = Tty.ConsoleNodes.ConsoleNode.ConsoleLine.State.Template()
                        self.template.parent = self
                        self._children_name_map["template"] = "template"
                        self._children_yang_names.add("template")


                    class Template(Entity):
                        """
                        Information related to template applied to the
                        line
                        
                        .. attribute:: name
                        
                        	Name of the template
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'tty-server-oper'
                        _revision = '2015-07-30'

                        def __init__(self):
                            super(Tty.ConsoleNodes.ConsoleNode.ConsoleLine.State.Template, self).__init__()

                            self.yang_name = "template"
                            self.yang_parent_name = "state"

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
                                if name in ("name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Tty.ConsoleNodes.ConsoleNode.ConsoleLine.State.Template, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Tty.ConsoleNodes.ConsoleNode.ConsoleLine.State.Template, self).__setattr__(name, value)

                        def has_data(self):
                            return self.name.is_set

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.name.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "template" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
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
                            if(name == "name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "name"):
                                self.name = value
                                self.name.value_namespace = name_space
                                self.name.value_namespace_prefix = name_space_prefix


                    class General(Entity):
                        """
                        General information
                        
                        .. attribute:: general_state
                        
                        	State of the line
                        	**type**\:   :py:class:`LineState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.LineState>`
                        
                        .. attribute:: operation_
                        
                        	application running of on the tty line
                        	**type**\:   :py:class:`SessionOperation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.SessionOperation>`
                        
                        

                        """

                        _prefix = 'tty-server-oper'
                        _revision = '2015-07-30'

                        def __init__(self):
                            super(Tty.ConsoleNodes.ConsoleNode.ConsoleLine.State.General, self).__init__()

                            self.yang_name = "general"
                            self.yang_parent_name = "state"

                            self.general_state = YLeaf(YType.enumeration, "general-state")

                            self.operation_ = YLeaf(YType.enumeration, "operation")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("general_state",
                                            "operation_") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Tty.ConsoleNodes.ConsoleNode.ConsoleLine.State.General, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Tty.ConsoleNodes.ConsoleNode.ConsoleLine.State.General, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.general_state.is_set or
                                self.operation_.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.general_state.yfilter != YFilter.not_set or
                                self.operation_.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "general" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.general_state.is_set or self.general_state.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.general_state.get_name_leafdata())
                            if (self.operation_.is_set or self.operation_.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.operation_.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "general-state" or name == "operation"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "general-state"):
                                self.general_state = value
                                self.general_state.value_namespace = name_space
                                self.general_state.value_namespace_prefix = name_space_prefix
                            if(value_path == "operation"):
                                self.operation_ = value
                                self.operation_.value_namespace = name_space
                                self.operation_.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            (self.general is not None and self.general.has_data()) or
                            (self.template is not None and self.template.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.general is not None and self.general.has_operation()) or
                            (self.template is not None and self.template.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "state" + path_buffer

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

                        if (child_yang_name == "general"):
                            if (self.general is None):
                                self.general = Tty.ConsoleNodes.ConsoleNode.ConsoleLine.State.General()
                                self.general.parent = self
                                self._children_name_map["general"] = "general"
                            return self.general

                        if (child_yang_name == "template"):
                            if (self.template is None):
                                self.template = Tty.ConsoleNodes.ConsoleNode.ConsoleLine.State.Template()
                                self.template.parent = self
                                self._children_name_map["template"] = "template"
                            return self.template

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "general" or name == "template"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class Configuration(Entity):
                    """
                    Configuration information of the line
                    
                    .. attribute:: connection_configuration
                    
                    	Conection configuration information
                    	**type**\:   :py:class:`ConnectionConfiguration <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.ConsoleNodes.ConsoleNode.ConsoleLine.Configuration.ConnectionConfiguration>`
                    
                    

                    """

                    _prefix = 'tty-server-oper'
                    _revision = '2015-07-30'

                    def __init__(self):
                        super(Tty.ConsoleNodes.ConsoleNode.ConsoleLine.Configuration, self).__init__()

                        self.yang_name = "configuration"
                        self.yang_parent_name = "console-line"

                        self.connection_configuration = Tty.ConsoleNodes.ConsoleNode.ConsoleLine.Configuration.ConnectionConfiguration()
                        self.connection_configuration.parent = self
                        self._children_name_map["connection_configuration"] = "connection-configuration"
                        self._children_yang_names.add("connection-configuration")


                    class ConnectionConfiguration(Entity):
                        """
                        Conection configuration information
                        
                        .. attribute:: acl_in
                        
                        	ACL for inbound traffic
                        	**type**\:  str
                        
                        .. attribute:: acl_out
                        
                        	ACL for outbound traffic
                        	**type**\:  str
                        
                        .. attribute:: transport_input
                        
                        	Protocols to use when connecting to the terminal server
                        	**type**\:   :py:class:`TransportInput <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.ConsoleNodes.ConsoleNode.ConsoleLine.Configuration.ConnectionConfiguration.TransportInput>`
                        
                        

                        """

                        _prefix = 'tty-server-oper'
                        _revision = '2015-07-30'

                        def __init__(self):
                            super(Tty.ConsoleNodes.ConsoleNode.ConsoleLine.Configuration.ConnectionConfiguration, self).__init__()

                            self.yang_name = "connection-configuration"
                            self.yang_parent_name = "configuration"

                            self.acl_in = YLeaf(YType.str, "acl-in")

                            self.acl_out = YLeaf(YType.str, "acl-out")

                            self.transport_input = Tty.ConsoleNodes.ConsoleNode.ConsoleLine.Configuration.ConnectionConfiguration.TransportInput()
                            self.transport_input.parent = self
                            self._children_name_map["transport_input"] = "transport-input"
                            self._children_yang_names.add("transport-input")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("acl_in",
                                            "acl_out") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Tty.ConsoleNodes.ConsoleNode.ConsoleLine.Configuration.ConnectionConfiguration, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Tty.ConsoleNodes.ConsoleNode.ConsoleLine.Configuration.ConnectionConfiguration, self).__setattr__(name, value)


                        class TransportInput(Entity):
                            """
                            Protocols to use when connecting to the
                            terminal server
                            
                            .. attribute:: none
                            
                            	Not used
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: protocol1
                            
                            	Transport protocol1
                            	**type**\:   :py:class:`TtyTransportProtocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes.TtyTransportProtocol>`
                            
                            .. attribute:: protocol2
                            
                            	Transport protocol2
                            	**type**\:   :py:class:`TtyTransportProtocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes.TtyTransportProtocol>`
                            
                            .. attribute:: select
                            
                            	Choose transport protocols
                            	**type**\:   :py:class:`TtyTransportProtocolSelect <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes.TtyTransportProtocolSelect>`
                            
                            	**default value**\: all
                            
                            

                            """

                            _prefix = 'tty-server-oper'
                            _revision = '2015-07-30'

                            def __init__(self):
                                super(Tty.ConsoleNodes.ConsoleNode.ConsoleLine.Configuration.ConnectionConfiguration.TransportInput, self).__init__()

                                self.yang_name = "transport-input"
                                self.yang_parent_name = "connection-configuration"

                                self.none = YLeaf(YType.int32, "none")

                                self.protocol1 = YLeaf(YType.enumeration, "protocol1")

                                self.protocol2 = YLeaf(YType.enumeration, "protocol2")

                                self.select = YLeaf(YType.enumeration, "select")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("none",
                                                "protocol1",
                                                "protocol2",
                                                "select") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Tty.ConsoleNodes.ConsoleNode.ConsoleLine.Configuration.ConnectionConfiguration.TransportInput, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Tty.ConsoleNodes.ConsoleNode.ConsoleLine.Configuration.ConnectionConfiguration.TransportInput, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.none.is_set or
                                    self.protocol1.is_set or
                                    self.protocol2.is_set or
                                    self.select.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.none.yfilter != YFilter.not_set or
                                    self.protocol1.yfilter != YFilter.not_set or
                                    self.protocol2.yfilter != YFilter.not_set or
                                    self.select.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "transport-input" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.none.is_set or self.none.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.none.get_name_leafdata())
                                if (self.protocol1.is_set or self.protocol1.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.protocol1.get_name_leafdata())
                                if (self.protocol2.is_set or self.protocol2.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.protocol2.get_name_leafdata())
                                if (self.select.is_set or self.select.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.select.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "none" or name == "protocol1" or name == "protocol2" or name == "select"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "none"):
                                    self.none = value
                                    self.none.value_namespace = name_space
                                    self.none.value_namespace_prefix = name_space_prefix
                                if(value_path == "protocol1"):
                                    self.protocol1 = value
                                    self.protocol1.value_namespace = name_space
                                    self.protocol1.value_namespace_prefix = name_space_prefix
                                if(value_path == "protocol2"):
                                    self.protocol2 = value
                                    self.protocol2.value_namespace = name_space
                                    self.protocol2.value_namespace_prefix = name_space_prefix
                                if(value_path == "select"):
                                    self.select = value
                                    self.select.value_namespace = name_space
                                    self.select.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.acl_in.is_set or
                                self.acl_out.is_set or
                                (self.transport_input is not None and self.transport_input.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.acl_in.yfilter != YFilter.not_set or
                                self.acl_out.yfilter != YFilter.not_set or
                                (self.transport_input is not None and self.transport_input.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "connection-configuration" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.acl_in.is_set or self.acl_in.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.acl_in.get_name_leafdata())
                            if (self.acl_out.is_set or self.acl_out.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.acl_out.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "transport-input"):
                                if (self.transport_input is None):
                                    self.transport_input = Tty.ConsoleNodes.ConsoleNode.ConsoleLine.Configuration.ConnectionConfiguration.TransportInput()
                                    self.transport_input.parent = self
                                    self._children_name_map["transport_input"] = "transport-input"
                                return self.transport_input

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "transport-input" or name == "acl-in" or name == "acl-out"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "acl-in"):
                                self.acl_in = value
                                self.acl_in.value_namespace = name_space
                                self.acl_in.value_namespace_prefix = name_space_prefix
                            if(value_path == "acl-out"):
                                self.acl_out = value
                                self.acl_out.value_namespace = name_space
                                self.acl_out.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (self.connection_configuration is not None and self.connection_configuration.has_data())

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.connection_configuration is not None and self.connection_configuration.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "configuration" + path_buffer

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

                        if (child_yang_name == "connection-configuration"):
                            if (self.connection_configuration is None):
                                self.connection_configuration = Tty.ConsoleNodes.ConsoleNode.ConsoleLine.Configuration.ConnectionConfiguration()
                                self.connection_configuration.parent = self
                                self._children_name_map["connection_configuration"] = "connection-configuration"
                            return self.connection_configuration

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "connection-configuration"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        (self.configuration is not None and self.configuration.has_data()) or
                        (self.console_statistics is not None and self.console_statistics.has_data()) or
                        (self.state is not None and self.state.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.configuration is not None and self.configuration.has_operation()) or
                        (self.console_statistics is not None and self.console_statistics.has_operation()) or
                        (self.state is not None and self.state.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "console-line" + path_buffer

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

                    if (child_yang_name == "configuration"):
                        if (self.configuration is None):
                            self.configuration = Tty.ConsoleNodes.ConsoleNode.ConsoleLine.Configuration()
                            self.configuration.parent = self
                            self._children_name_map["configuration"] = "configuration"
                        return self.configuration

                    if (child_yang_name == "console-statistics"):
                        if (self.console_statistics is None):
                            self.console_statistics = Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics()
                            self.console_statistics.parent = self
                            self._children_name_map["console_statistics"] = "console-statistics"
                        return self.console_statistics

                    if (child_yang_name == "state"):
                        if (self.state is None):
                            self.state = Tty.ConsoleNodes.ConsoleNode.ConsoleLine.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                        return self.state

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "configuration" or name == "console-statistics" or name == "state"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.id.is_set or
                    (self.console_line is not None and self.console_line.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.id.yfilter != YFilter.not_set or
                    (self.console_line is not None and self.console_line.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "console-node" + "[id='" + self.id.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-tty-server-oper:tty/console-nodes/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.id.is_set or self.id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.id.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "console-line"):
                    if (self.console_line is None):
                        self.console_line = Tty.ConsoleNodes.ConsoleNode.ConsoleLine()
                        self.console_line.parent = self
                        self._children_name_map["console_line"] = "console-line"
                    return self.console_line

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "console-line" or name == "id"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "id"):
                    self.id = value
                    self.id.value_namespace = name_space
                    self.id.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.console_node:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.console_node:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "console-nodes" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-tty-server-oper:tty/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "console-node"):
                for c in self.console_node:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Tty.ConsoleNodes.ConsoleNode()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.console_node.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "console-node"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class VtyLines(Entity):
        """
        List of VTY lines
        
        .. attribute:: vty_line
        
        	VTY Line
        	**type**\: list of    :py:class:`VtyLine <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.VtyLines.VtyLine>`
        
        

        """

        _prefix = 'tty-server-oper'
        _revision = '2015-07-30'

        def __init__(self):
            super(Tty.VtyLines, self).__init__()

            self.yang_name = "vty-lines"
            self.yang_parent_name = "tty"

            self.vty_line = YList(self)

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
                        super(Tty.VtyLines, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Tty.VtyLines, self).__setattr__(name, value)


        class VtyLine(Entity):
            """
            VTY Line
            
            .. attribute:: line_number  <key>
            
            	VTY Line number
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: configuration
            
            	Configuration information of the line
            	**type**\:   :py:class:`Configuration <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.VtyLines.VtyLine.Configuration>`
            
            .. attribute:: sessions
            
            	Outgoing sessions
            	**type**\:   :py:class:`Sessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.VtyLines.VtyLine.Sessions>`
            
            .. attribute:: state
            
            	Line state information
            	**type**\:   :py:class:`State <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.VtyLines.VtyLine.State>`
            
            .. attribute:: vty_statistics
            
            	Statistics of the VTY line
            	**type**\:   :py:class:`VtyStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.VtyLines.VtyLine.VtyStatistics>`
            
            

            """

            _prefix = 'tty-server-oper'
            _revision = '2015-07-30'

            def __init__(self):
                super(Tty.VtyLines.VtyLine, self).__init__()

                self.yang_name = "vty-line"
                self.yang_parent_name = "vty-lines"

                self.line_number = YLeaf(YType.int32, "line-number")

                self.configuration = Tty.VtyLines.VtyLine.Configuration()
                self.configuration.parent = self
                self._children_name_map["configuration"] = "configuration"
                self._children_yang_names.add("configuration")

                self.sessions = Tty.VtyLines.VtyLine.Sessions()
                self.sessions.parent = self
                self._children_name_map["sessions"] = "sessions"
                self._children_yang_names.add("sessions")

                self.state = Tty.VtyLines.VtyLine.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"
                self._children_yang_names.add("state")

                self.vty_statistics = Tty.VtyLines.VtyLine.VtyStatistics()
                self.vty_statistics.parent = self
                self._children_name_map["vty_statistics"] = "vty-statistics"
                self._children_yang_names.add("vty-statistics")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("line_number") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Tty.VtyLines.VtyLine, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Tty.VtyLines.VtyLine, self).__setattr__(name, value)


            class VtyStatistics(Entity):
                """
                Statistics of the VTY line
                
                .. attribute:: aaa
                
                	AAA related statistics
                	**type**\:   :py:class:`Aaa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.VtyLines.VtyLine.VtyStatistics.Aaa>`
                
                .. attribute:: connection
                
                	Connection related statistics
                	**type**\:   :py:class:`Connection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.VtyLines.VtyLine.VtyStatistics.Connection>`
                
                .. attribute:: exec_
                
                	Exec related statistics
                	**type**\:   :py:class:`Exec_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.VtyLines.VtyLine.VtyStatistics.Exec_>`
                
                .. attribute:: general_statistics
                
                	General statistics of line
                	**type**\:   :py:class:`GeneralStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.VtyLines.VtyLine.VtyStatistics.GeneralStatistics>`
                
                

                """

                _prefix = 'tty-server-oper'
                _revision = '2015-07-30'

                def __init__(self):
                    super(Tty.VtyLines.VtyLine.VtyStatistics, self).__init__()

                    self.yang_name = "vty-statistics"
                    self.yang_parent_name = "vty-line"

                    self.aaa = Tty.VtyLines.VtyLine.VtyStatistics.Aaa()
                    self.aaa.parent = self
                    self._children_name_map["aaa"] = "aaa"
                    self._children_yang_names.add("aaa")

                    self.connection = Tty.VtyLines.VtyLine.VtyStatistics.Connection()
                    self.connection.parent = self
                    self._children_name_map["connection"] = "connection"
                    self._children_yang_names.add("connection")

                    self.exec_ = Tty.VtyLines.VtyLine.VtyStatistics.Exec_()
                    self.exec_.parent = self
                    self._children_name_map["exec_"] = "exec"
                    self._children_yang_names.add("exec")

                    self.general_statistics = Tty.VtyLines.VtyLine.VtyStatistics.GeneralStatistics()
                    self.general_statistics.parent = self
                    self._children_name_map["general_statistics"] = "general-statistics"
                    self._children_yang_names.add("general-statistics")


                class Connection(Entity):
                    """
                    Connection related statistics
                    
                    .. attribute:: host_address_family
                    
                    	Incoming host address family
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: incoming_host_address
                    
                    	Incoming host address(max)
                    	**type**\:  str
                    
                    	**length:** 0..46
                    
                    .. attribute:: service
                    
                    	Input transport
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'tty-server-oper'
                    _revision = '2015-07-30'

                    def __init__(self):
                        super(Tty.VtyLines.VtyLine.VtyStatistics.Connection, self).__init__()

                        self.yang_name = "connection"
                        self.yang_parent_name = "vty-statistics"

                        self.host_address_family = YLeaf(YType.uint32, "host-address-family")

                        self.incoming_host_address = YLeaf(YType.str, "incoming-host-address")

                        self.service = YLeaf(YType.uint32, "service")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("host_address_family",
                                        "incoming_host_address",
                                        "service") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Tty.VtyLines.VtyLine.VtyStatistics.Connection, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Tty.VtyLines.VtyLine.VtyStatistics.Connection, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.host_address_family.is_set or
                            self.incoming_host_address.is_set or
                            self.service.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.host_address_family.yfilter != YFilter.not_set or
                            self.incoming_host_address.yfilter != YFilter.not_set or
                            self.service.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "connection" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.host_address_family.is_set or self.host_address_family.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.host_address_family.get_name_leafdata())
                        if (self.incoming_host_address.is_set or self.incoming_host_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.incoming_host_address.get_name_leafdata())
                        if (self.service.is_set or self.service.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.service.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "host-address-family" or name == "incoming-host-address" or name == "service"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "host-address-family"):
                            self.host_address_family = value
                            self.host_address_family.value_namespace = name_space
                            self.host_address_family.value_namespace_prefix = name_space_prefix
                        if(value_path == "incoming-host-address"):
                            self.incoming_host_address = value
                            self.incoming_host_address.value_namespace = name_space
                            self.incoming_host_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "service"):
                            self.service = value
                            self.service.value_namespace = name_space
                            self.service.value_namespace_prefix = name_space_prefix


                class GeneralStatistics(Entity):
                    """
                    General statistics of line
                    
                    .. attribute:: absolute_timeout
                    
                    	Absolute timeout period
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: async_interface
                    
                    	Usable as async interface
                    	**type**\:  bool
                    
                    .. attribute:: domain_lookup_enabled
                    
                    	DNS resolution enabled
                    	**type**\:  bool
                    
                    .. attribute:: flow_control_start_character
                    
                    	Software flow control start char
                    	**type**\:  int
                    
                    	**range:** \-128..127
                    
                    .. attribute:: flow_control_stop_character
                    
                    	Software flow control stop char
                    	**type**\:  int
                    
                    	**range:** \-128..127
                    
                    .. attribute:: idle_time
                    
                    	TTY idle time
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: motd_banner_enabled
                    
                    	MOTD banner enabled
                    	**type**\:  bool
                    
                    .. attribute:: private_flag
                    
                    	TTY private flag
                    	**type**\:  bool
                    
                    .. attribute:: terminal_length
                    
                    	Terminal length
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: terminal_type
                    
                    	Terminal type
                    	**type**\:  str
                    
                    .. attribute:: terminal_width
                    
                    	Line width
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'tty-server-oper'
                    _revision = '2015-07-30'

                    def __init__(self):
                        super(Tty.VtyLines.VtyLine.VtyStatistics.GeneralStatistics, self).__init__()

                        self.yang_name = "general-statistics"
                        self.yang_parent_name = "vty-statistics"

                        self.absolute_timeout = YLeaf(YType.uint32, "absolute-timeout")

                        self.async_interface = YLeaf(YType.boolean, "async-interface")

                        self.domain_lookup_enabled = YLeaf(YType.boolean, "domain-lookup-enabled")

                        self.flow_control_start_character = YLeaf(YType.int8, "flow-control-start-character")

                        self.flow_control_stop_character = YLeaf(YType.int8, "flow-control-stop-character")

                        self.idle_time = YLeaf(YType.uint32, "idle-time")

                        self.motd_banner_enabled = YLeaf(YType.boolean, "motd-banner-enabled")

                        self.private_flag = YLeaf(YType.boolean, "private-flag")

                        self.terminal_length = YLeaf(YType.uint32, "terminal-length")

                        self.terminal_type = YLeaf(YType.str, "terminal-type")

                        self.terminal_width = YLeaf(YType.uint32, "terminal-width")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("absolute_timeout",
                                        "async_interface",
                                        "domain_lookup_enabled",
                                        "flow_control_start_character",
                                        "flow_control_stop_character",
                                        "idle_time",
                                        "motd_banner_enabled",
                                        "private_flag",
                                        "terminal_length",
                                        "terminal_type",
                                        "terminal_width") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Tty.VtyLines.VtyLine.VtyStatistics.GeneralStatistics, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Tty.VtyLines.VtyLine.VtyStatistics.GeneralStatistics, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.absolute_timeout.is_set or
                            self.async_interface.is_set or
                            self.domain_lookup_enabled.is_set or
                            self.flow_control_start_character.is_set or
                            self.flow_control_stop_character.is_set or
                            self.idle_time.is_set or
                            self.motd_banner_enabled.is_set or
                            self.private_flag.is_set or
                            self.terminal_length.is_set or
                            self.terminal_type.is_set or
                            self.terminal_width.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.absolute_timeout.yfilter != YFilter.not_set or
                            self.async_interface.yfilter != YFilter.not_set or
                            self.domain_lookup_enabled.yfilter != YFilter.not_set or
                            self.flow_control_start_character.yfilter != YFilter.not_set or
                            self.flow_control_stop_character.yfilter != YFilter.not_set or
                            self.idle_time.yfilter != YFilter.not_set or
                            self.motd_banner_enabled.yfilter != YFilter.not_set or
                            self.private_flag.yfilter != YFilter.not_set or
                            self.terminal_length.yfilter != YFilter.not_set or
                            self.terminal_type.yfilter != YFilter.not_set or
                            self.terminal_width.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "general-statistics" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.absolute_timeout.is_set or self.absolute_timeout.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.absolute_timeout.get_name_leafdata())
                        if (self.async_interface.is_set or self.async_interface.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.async_interface.get_name_leafdata())
                        if (self.domain_lookup_enabled.is_set or self.domain_lookup_enabled.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.domain_lookup_enabled.get_name_leafdata())
                        if (self.flow_control_start_character.is_set or self.flow_control_start_character.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.flow_control_start_character.get_name_leafdata())
                        if (self.flow_control_stop_character.is_set or self.flow_control_stop_character.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.flow_control_stop_character.get_name_leafdata())
                        if (self.idle_time.is_set or self.idle_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.idle_time.get_name_leafdata())
                        if (self.motd_banner_enabled.is_set or self.motd_banner_enabled.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.motd_banner_enabled.get_name_leafdata())
                        if (self.private_flag.is_set or self.private_flag.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.private_flag.get_name_leafdata())
                        if (self.terminal_length.is_set or self.terminal_length.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.terminal_length.get_name_leafdata())
                        if (self.terminal_type.is_set or self.terminal_type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.terminal_type.get_name_leafdata())
                        if (self.terminal_width.is_set or self.terminal_width.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.terminal_width.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "absolute-timeout" or name == "async-interface" or name == "domain-lookup-enabled" or name == "flow-control-start-character" or name == "flow-control-stop-character" or name == "idle-time" or name == "motd-banner-enabled" or name == "private-flag" or name == "terminal-length" or name == "terminal-type" or name == "terminal-width"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "absolute-timeout"):
                            self.absolute_timeout = value
                            self.absolute_timeout.value_namespace = name_space
                            self.absolute_timeout.value_namespace_prefix = name_space_prefix
                        if(value_path == "async-interface"):
                            self.async_interface = value
                            self.async_interface.value_namespace = name_space
                            self.async_interface.value_namespace_prefix = name_space_prefix
                        if(value_path == "domain-lookup-enabled"):
                            self.domain_lookup_enabled = value
                            self.domain_lookup_enabled.value_namespace = name_space
                            self.domain_lookup_enabled.value_namespace_prefix = name_space_prefix
                        if(value_path == "flow-control-start-character"):
                            self.flow_control_start_character = value
                            self.flow_control_start_character.value_namespace = name_space
                            self.flow_control_start_character.value_namespace_prefix = name_space_prefix
                        if(value_path == "flow-control-stop-character"):
                            self.flow_control_stop_character = value
                            self.flow_control_stop_character.value_namespace = name_space
                            self.flow_control_stop_character.value_namespace_prefix = name_space_prefix
                        if(value_path == "idle-time"):
                            self.idle_time = value
                            self.idle_time.value_namespace = name_space
                            self.idle_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "motd-banner-enabled"):
                            self.motd_banner_enabled = value
                            self.motd_banner_enabled.value_namespace = name_space
                            self.motd_banner_enabled.value_namespace_prefix = name_space_prefix
                        if(value_path == "private-flag"):
                            self.private_flag = value
                            self.private_flag.value_namespace = name_space
                            self.private_flag.value_namespace_prefix = name_space_prefix
                        if(value_path == "terminal-length"):
                            self.terminal_length = value
                            self.terminal_length.value_namespace = name_space
                            self.terminal_length.value_namespace_prefix = name_space_prefix
                        if(value_path == "terminal-type"):
                            self.terminal_type = value
                            self.terminal_type.value_namespace = name_space
                            self.terminal_type.value_namespace_prefix = name_space_prefix
                        if(value_path == "terminal-width"):
                            self.terminal_width = value
                            self.terminal_width.value_namespace = name_space
                            self.terminal_width.value_namespace_prefix = name_space_prefix


                class Exec_(Entity):
                    """
                    Exec related statistics
                    
                    .. attribute:: time_stamp_enabled
                    
                    	Specifies whether timestamp is enabled or not
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'tty-server-oper'
                    _revision = '2015-07-30'

                    def __init__(self):
                        super(Tty.VtyLines.VtyLine.VtyStatistics.Exec_, self).__init__()

                        self.yang_name = "exec"
                        self.yang_parent_name = "vty-statistics"

                        self.time_stamp_enabled = YLeaf(YType.boolean, "time-stamp-enabled")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("time_stamp_enabled") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Tty.VtyLines.VtyLine.VtyStatistics.Exec_, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Tty.VtyLines.VtyLine.VtyStatistics.Exec_, self).__setattr__(name, value)

                    def has_data(self):
                        return self.time_stamp_enabled.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.time_stamp_enabled.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "exec" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.time_stamp_enabled.is_set or self.time_stamp_enabled.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.time_stamp_enabled.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "time-stamp-enabled"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "time-stamp-enabled"):
                            self.time_stamp_enabled = value
                            self.time_stamp_enabled.value_namespace = name_space
                            self.time_stamp_enabled.value_namespace_prefix = name_space_prefix


                class Aaa(Entity):
                    """
                    AAA related statistics
                    
                    .. attribute:: user_name
                    
                    	The authenticated username
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'tty-server-oper'
                    _revision = '2015-07-30'

                    def __init__(self):
                        super(Tty.VtyLines.VtyLine.VtyStatistics.Aaa, self).__init__()

                        self.yang_name = "aaa"
                        self.yang_parent_name = "vty-statistics"

                        self.user_name = YLeaf(YType.str, "user-name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("user_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Tty.VtyLines.VtyLine.VtyStatistics.Aaa, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Tty.VtyLines.VtyLine.VtyStatistics.Aaa, self).__setattr__(name, value)

                    def has_data(self):
                        return self.user_name.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.user_name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "aaa" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.user_name.is_set or self.user_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.user_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "user-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "user-name"):
                            self.user_name = value
                            self.user_name.value_namespace = name_space
                            self.user_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        (self.aaa is not None and self.aaa.has_data()) or
                        (self.connection is not None and self.connection.has_data()) or
                        (self.exec_ is not None and self.exec_.has_data()) or
                        (self.general_statistics is not None and self.general_statistics.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.aaa is not None and self.aaa.has_operation()) or
                        (self.connection is not None and self.connection.has_operation()) or
                        (self.exec_ is not None and self.exec_.has_operation()) or
                        (self.general_statistics is not None and self.general_statistics.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "vty-statistics" + path_buffer

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

                    if (child_yang_name == "aaa"):
                        if (self.aaa is None):
                            self.aaa = Tty.VtyLines.VtyLine.VtyStatistics.Aaa()
                            self.aaa.parent = self
                            self._children_name_map["aaa"] = "aaa"
                        return self.aaa

                    if (child_yang_name == "connection"):
                        if (self.connection is None):
                            self.connection = Tty.VtyLines.VtyLine.VtyStatistics.Connection()
                            self.connection.parent = self
                            self._children_name_map["connection"] = "connection"
                        return self.connection

                    if (child_yang_name == "exec"):
                        if (self.exec_ is None):
                            self.exec_ = Tty.VtyLines.VtyLine.VtyStatistics.Exec_()
                            self.exec_.parent = self
                            self._children_name_map["exec_"] = "exec"
                        return self.exec_

                    if (child_yang_name == "general-statistics"):
                        if (self.general_statistics is None):
                            self.general_statistics = Tty.VtyLines.VtyLine.VtyStatistics.GeneralStatistics()
                            self.general_statistics.parent = self
                            self._children_name_map["general_statistics"] = "general-statistics"
                        return self.general_statistics

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "aaa" or name == "connection" or name == "exec" or name == "general-statistics"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class State(Entity):
                """
                Line state information
                
                .. attribute:: general
                
                	General information
                	**type**\:   :py:class:`General <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.VtyLines.VtyLine.State.General>`
                
                .. attribute:: template
                
                	Information related to template applied to the line
                	**type**\:   :py:class:`Template <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.VtyLines.VtyLine.State.Template>`
                
                

                """

                _prefix = 'tty-server-oper'
                _revision = '2015-07-30'

                def __init__(self):
                    super(Tty.VtyLines.VtyLine.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "vty-line"

                    self.general = Tty.VtyLines.VtyLine.State.General()
                    self.general.parent = self
                    self._children_name_map["general"] = "general"
                    self._children_yang_names.add("general")

                    self.template = Tty.VtyLines.VtyLine.State.Template()
                    self.template.parent = self
                    self._children_name_map["template"] = "template"
                    self._children_yang_names.add("template")


                class Template(Entity):
                    """
                    Information related to template applied to the
                    line
                    
                    .. attribute:: name
                    
                    	Name of the template
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'tty-server-oper'
                    _revision = '2015-07-30'

                    def __init__(self):
                        super(Tty.VtyLines.VtyLine.State.Template, self).__init__()

                        self.yang_name = "template"
                        self.yang_parent_name = "state"

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
                            if name in ("name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Tty.VtyLines.VtyLine.State.Template, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Tty.VtyLines.VtyLine.State.Template, self).__setattr__(name, value)

                    def has_data(self):
                        return self.name.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "template" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
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
                        if(name == "name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "name"):
                            self.name = value
                            self.name.value_namespace = name_space
                            self.name.value_namespace_prefix = name_space_prefix


                class General(Entity):
                    """
                    General information
                    
                    .. attribute:: general_state
                    
                    	State of the line
                    	**type**\:   :py:class:`LineState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.LineState>`
                    
                    .. attribute:: operation_
                    
                    	application running of on the tty line
                    	**type**\:   :py:class:`SessionOperation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.SessionOperation>`
                    
                    

                    """

                    _prefix = 'tty-server-oper'
                    _revision = '2015-07-30'

                    def __init__(self):
                        super(Tty.VtyLines.VtyLine.State.General, self).__init__()

                        self.yang_name = "general"
                        self.yang_parent_name = "state"

                        self.general_state = YLeaf(YType.enumeration, "general-state")

                        self.operation_ = YLeaf(YType.enumeration, "operation")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("general_state",
                                        "operation_") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Tty.VtyLines.VtyLine.State.General, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Tty.VtyLines.VtyLine.State.General, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.general_state.is_set or
                            self.operation_.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.general_state.yfilter != YFilter.not_set or
                            self.operation_.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "general" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.general_state.is_set or self.general_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.general_state.get_name_leafdata())
                        if (self.operation_.is_set or self.operation_.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.operation_.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "general-state" or name == "operation"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "general-state"):
                            self.general_state = value
                            self.general_state.value_namespace = name_space
                            self.general_state.value_namespace_prefix = name_space_prefix
                        if(value_path == "operation"):
                            self.operation_ = value
                            self.operation_.value_namespace = name_space
                            self.operation_.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        (self.general is not None and self.general.has_data()) or
                        (self.template is not None and self.template.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.general is not None and self.general.has_operation()) or
                        (self.template is not None and self.template.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "state" + path_buffer

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

                    if (child_yang_name == "general"):
                        if (self.general is None):
                            self.general = Tty.VtyLines.VtyLine.State.General()
                            self.general.parent = self
                            self._children_name_map["general"] = "general"
                        return self.general

                    if (child_yang_name == "template"):
                        if (self.template is None):
                            self.template = Tty.VtyLines.VtyLine.State.Template()
                            self.template.parent = self
                            self._children_name_map["template"] = "template"
                        return self.template

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "general" or name == "template"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Configuration(Entity):
                """
                Configuration information of the line
                
                .. attribute:: connection_configuration
                
                	Conection configuration information
                	**type**\:   :py:class:`ConnectionConfiguration <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.VtyLines.VtyLine.Configuration.ConnectionConfiguration>`
                
                

                """

                _prefix = 'tty-server-oper'
                _revision = '2015-07-30'

                def __init__(self):
                    super(Tty.VtyLines.VtyLine.Configuration, self).__init__()

                    self.yang_name = "configuration"
                    self.yang_parent_name = "vty-line"

                    self.connection_configuration = Tty.VtyLines.VtyLine.Configuration.ConnectionConfiguration()
                    self.connection_configuration.parent = self
                    self._children_name_map["connection_configuration"] = "connection-configuration"
                    self._children_yang_names.add("connection-configuration")


                class ConnectionConfiguration(Entity):
                    """
                    Conection configuration information
                    
                    .. attribute:: acl_in
                    
                    	ACL for inbound traffic
                    	**type**\:  str
                    
                    .. attribute:: acl_out
                    
                    	ACL for outbound traffic
                    	**type**\:  str
                    
                    .. attribute:: transport_input
                    
                    	Protocols to use when connecting to the terminal server
                    	**type**\:   :py:class:`TransportInput <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.VtyLines.VtyLine.Configuration.ConnectionConfiguration.TransportInput>`
                    
                    

                    """

                    _prefix = 'tty-server-oper'
                    _revision = '2015-07-30'

                    def __init__(self):
                        super(Tty.VtyLines.VtyLine.Configuration.ConnectionConfiguration, self).__init__()

                        self.yang_name = "connection-configuration"
                        self.yang_parent_name = "configuration"

                        self.acl_in = YLeaf(YType.str, "acl-in")

                        self.acl_out = YLeaf(YType.str, "acl-out")

                        self.transport_input = Tty.VtyLines.VtyLine.Configuration.ConnectionConfiguration.TransportInput()
                        self.transport_input.parent = self
                        self._children_name_map["transport_input"] = "transport-input"
                        self._children_yang_names.add("transport-input")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("acl_in",
                                        "acl_out") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Tty.VtyLines.VtyLine.Configuration.ConnectionConfiguration, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Tty.VtyLines.VtyLine.Configuration.ConnectionConfiguration, self).__setattr__(name, value)


                    class TransportInput(Entity):
                        """
                        Protocols to use when connecting to the
                        terminal server
                        
                        .. attribute:: none
                        
                        	Not used
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: protocol1
                        
                        	Transport protocol1
                        	**type**\:   :py:class:`TtyTransportProtocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes.TtyTransportProtocol>`
                        
                        .. attribute:: protocol2
                        
                        	Transport protocol2
                        	**type**\:   :py:class:`TtyTransportProtocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes.TtyTransportProtocol>`
                        
                        .. attribute:: select
                        
                        	Choose transport protocols
                        	**type**\:   :py:class:`TtyTransportProtocolSelect <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes.TtyTransportProtocolSelect>`
                        
                        	**default value**\: all
                        
                        

                        """

                        _prefix = 'tty-server-oper'
                        _revision = '2015-07-30'

                        def __init__(self):
                            super(Tty.VtyLines.VtyLine.Configuration.ConnectionConfiguration.TransportInput, self).__init__()

                            self.yang_name = "transport-input"
                            self.yang_parent_name = "connection-configuration"

                            self.none = YLeaf(YType.int32, "none")

                            self.protocol1 = YLeaf(YType.enumeration, "protocol1")

                            self.protocol2 = YLeaf(YType.enumeration, "protocol2")

                            self.select = YLeaf(YType.enumeration, "select")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("none",
                                            "protocol1",
                                            "protocol2",
                                            "select") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Tty.VtyLines.VtyLine.Configuration.ConnectionConfiguration.TransportInput, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Tty.VtyLines.VtyLine.Configuration.ConnectionConfiguration.TransportInput, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.none.is_set or
                                self.protocol1.is_set or
                                self.protocol2.is_set or
                                self.select.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.none.yfilter != YFilter.not_set or
                                self.protocol1.yfilter != YFilter.not_set or
                                self.protocol2.yfilter != YFilter.not_set or
                                self.select.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "transport-input" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.none.is_set or self.none.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.none.get_name_leafdata())
                            if (self.protocol1.is_set or self.protocol1.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.protocol1.get_name_leafdata())
                            if (self.protocol2.is_set or self.protocol2.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.protocol2.get_name_leafdata())
                            if (self.select.is_set or self.select.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.select.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "none" or name == "protocol1" or name == "protocol2" or name == "select"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "none"):
                                self.none = value
                                self.none.value_namespace = name_space
                                self.none.value_namespace_prefix = name_space_prefix
                            if(value_path == "protocol1"):
                                self.protocol1 = value
                                self.protocol1.value_namespace = name_space
                                self.protocol1.value_namespace_prefix = name_space_prefix
                            if(value_path == "protocol2"):
                                self.protocol2 = value
                                self.protocol2.value_namespace = name_space
                                self.protocol2.value_namespace_prefix = name_space_prefix
                            if(value_path == "select"):
                                self.select = value
                                self.select.value_namespace = name_space
                                self.select.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.acl_in.is_set or
                            self.acl_out.is_set or
                            (self.transport_input is not None and self.transport_input.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.acl_in.yfilter != YFilter.not_set or
                            self.acl_out.yfilter != YFilter.not_set or
                            (self.transport_input is not None and self.transport_input.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "connection-configuration" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.acl_in.is_set or self.acl_in.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.acl_in.get_name_leafdata())
                        if (self.acl_out.is_set or self.acl_out.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.acl_out.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "transport-input"):
                            if (self.transport_input is None):
                                self.transport_input = Tty.VtyLines.VtyLine.Configuration.ConnectionConfiguration.TransportInput()
                                self.transport_input.parent = self
                                self._children_name_map["transport_input"] = "transport-input"
                            return self.transport_input

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "transport-input" or name == "acl-in" or name == "acl-out"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "acl-in"):
                            self.acl_in = value
                            self.acl_in.value_namespace = name_space
                            self.acl_in.value_namespace_prefix = name_space_prefix
                        if(value_path == "acl-out"):
                            self.acl_out = value
                            self.acl_out.value_namespace = name_space
                            self.acl_out.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (self.connection_configuration is not None and self.connection_configuration.has_data())

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.connection_configuration is not None and self.connection_configuration.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "configuration" + path_buffer

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

                    if (child_yang_name == "connection-configuration"):
                        if (self.connection_configuration is None):
                            self.connection_configuration = Tty.VtyLines.VtyLine.Configuration.ConnectionConfiguration()
                            self.connection_configuration.parent = self
                            self._children_name_map["connection_configuration"] = "connection-configuration"
                        return self.connection_configuration

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "connection-configuration"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Sessions(Entity):
                """
                Outgoing sessions
                
                .. attribute:: outgoing_connection
                
                	List of outgoing sessions
                	**type**\: list of    :py:class:`OutgoingConnection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.VtyLines.VtyLine.Sessions.OutgoingConnection>`
                
                

                """

                _prefix = 'tty-management-oper'
                _revision = '2015-01-07'

                def __init__(self):
                    super(Tty.VtyLines.VtyLine.Sessions, self).__init__()

                    self.yang_name = "sessions"
                    self.yang_parent_name = "vty-line"

                    self.outgoing_connection = YList(self)

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
                                super(Tty.VtyLines.VtyLine.Sessions, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Tty.VtyLines.VtyLine.Sessions, self).__setattr__(name, value)


                class OutgoingConnection(Entity):
                    """
                    List of outgoing sessions
                    
                    .. attribute:: connection_id
                    
                    	Connection ID [1\-20]
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: host_address
                    
                    	Host address
                    	**type**\:   :py:class:`HostAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.VtyLines.VtyLine.Sessions.OutgoingConnection.HostAddress>`
                    
                    .. attribute:: host_name
                    
                    	Host name
                    	**type**\:  str
                    
                    .. attribute:: idle_time
                    
                    	Elapsed time since session was suspended (in seconds)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: is_last_active_session
                    
                    	True indicates last active session
                    	**type**\:  bool
                    
                    .. attribute:: transport_protocol
                    
                    	Session transport protocol
                    	**type**\:   :py:class:`TransportService <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_oper.TransportService>`
                    
                    

                    """

                    _prefix = 'tty-management-oper'
                    _revision = '2015-01-07'

                    def __init__(self):
                        super(Tty.VtyLines.VtyLine.Sessions.OutgoingConnection, self).__init__()

                        self.yang_name = "outgoing-connection"
                        self.yang_parent_name = "sessions"

                        self.connection_id = YLeaf(YType.uint8, "connection-id")

                        self.host_name = YLeaf(YType.str, "host-name")

                        self.idle_time = YLeaf(YType.uint32, "idle-time")

                        self.is_last_active_session = YLeaf(YType.boolean, "is-last-active-session")

                        self.transport_protocol = YLeaf(YType.enumeration, "transport-protocol")

                        self.host_address = Tty.VtyLines.VtyLine.Sessions.OutgoingConnection.HostAddress()
                        self.host_address.parent = self
                        self._children_name_map["host_address"] = "host-address"
                        self._children_yang_names.add("host-address")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("connection_id",
                                        "host_name",
                                        "idle_time",
                                        "is_last_active_session",
                                        "transport_protocol") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Tty.VtyLines.VtyLine.Sessions.OutgoingConnection, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Tty.VtyLines.VtyLine.Sessions.OutgoingConnection, self).__setattr__(name, value)


                    class HostAddress(Entity):
                        """
                        Host address
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\:   :py:class:`HostAfIdBase <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_oper.HostAfIdBase>`
                        
                        .. attribute:: ipv4_address
                        
                        	IPv4 address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6_address
                        
                        	IPv6 address
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'tty-management-oper'
                        _revision = '2015-01-07'

                        def __init__(self):
                            super(Tty.VtyLines.VtyLine.Sessions.OutgoingConnection.HostAddress, self).__init__()

                            self.yang_name = "host-address"
                            self.yang_parent_name = "outgoing-connection"

                            self.af_name = YLeaf(YType.identityref, "af-name")

                            self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                            self.ipv6_address = YLeaf(YType.str, "ipv6-address")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("af_name",
                                            "ipv4_address",
                                            "ipv6_address") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Tty.VtyLines.VtyLine.Sessions.OutgoingConnection.HostAddress, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Tty.VtyLines.VtyLine.Sessions.OutgoingConnection.HostAddress, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.af_name.is_set or
                                self.ipv4_address.is_set or
                                self.ipv6_address.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.af_name.yfilter != YFilter.not_set or
                                self.ipv4_address.yfilter != YFilter.not_set or
                                self.ipv6_address.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "host-address" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.af_name.is_set or self.af_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.af_name.get_name_leafdata())
                            if (self.ipv4_address.is_set or self.ipv4_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ipv4_address.get_name_leafdata())
                            if (self.ipv6_address.is_set or self.ipv6_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ipv6_address.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "af-name" or name == "ipv4-address" or name == "ipv6-address"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "af-name"):
                                self.af_name = value
                                self.af_name.value_namespace = name_space
                                self.af_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "ipv4-address"):
                                self.ipv4_address = value
                                self.ipv4_address.value_namespace = name_space
                                self.ipv4_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "ipv6-address"):
                                self.ipv6_address = value
                                self.ipv6_address.value_namespace = name_space
                                self.ipv6_address.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.connection_id.is_set or
                            self.host_name.is_set or
                            self.idle_time.is_set or
                            self.is_last_active_session.is_set or
                            self.transport_protocol.is_set or
                            (self.host_address is not None and self.host_address.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.connection_id.yfilter != YFilter.not_set or
                            self.host_name.yfilter != YFilter.not_set or
                            self.idle_time.yfilter != YFilter.not_set or
                            self.is_last_active_session.yfilter != YFilter.not_set or
                            self.transport_protocol.yfilter != YFilter.not_set or
                            (self.host_address is not None and self.host_address.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "outgoing-connection" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.connection_id.is_set or self.connection_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.connection_id.get_name_leafdata())
                        if (self.host_name.is_set or self.host_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.host_name.get_name_leafdata())
                        if (self.idle_time.is_set or self.idle_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.idle_time.get_name_leafdata())
                        if (self.is_last_active_session.is_set or self.is_last_active_session.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.is_last_active_session.get_name_leafdata())
                        if (self.transport_protocol.is_set or self.transport_protocol.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.transport_protocol.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "host-address"):
                            if (self.host_address is None):
                                self.host_address = Tty.VtyLines.VtyLine.Sessions.OutgoingConnection.HostAddress()
                                self.host_address.parent = self
                                self._children_name_map["host_address"] = "host-address"
                            return self.host_address

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "host-address" or name == "connection-id" or name == "host-name" or name == "idle-time" or name == "is-last-active-session" or name == "transport-protocol"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "connection-id"):
                            self.connection_id = value
                            self.connection_id.value_namespace = name_space
                            self.connection_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "host-name"):
                            self.host_name = value
                            self.host_name.value_namespace = name_space
                            self.host_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "idle-time"):
                            self.idle_time = value
                            self.idle_time.value_namespace = name_space
                            self.idle_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "is-last-active-session"):
                            self.is_last_active_session = value
                            self.is_last_active_session.value_namespace = name_space
                            self.is_last_active_session.value_namespace_prefix = name_space_prefix
                        if(value_path == "transport-protocol"):
                            self.transport_protocol = value
                            self.transport_protocol.value_namespace = name_space
                            self.transport_protocol.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.outgoing_connection:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.outgoing_connection:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "Cisco-IOS-XR-tty-management-oper:sessions" + path_buffer

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

                    if (child_yang_name == "outgoing-connection"):
                        for c in self.outgoing_connection:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Tty.VtyLines.VtyLine.Sessions.OutgoingConnection()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.outgoing_connection.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "outgoing-connection"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.line_number.is_set or
                    (self.configuration is not None and self.configuration.has_data()) or
                    (self.sessions is not None and self.sessions.has_data()) or
                    (self.state is not None and self.state.has_data()) or
                    (self.vty_statistics is not None and self.vty_statistics.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.line_number.yfilter != YFilter.not_set or
                    (self.configuration is not None and self.configuration.has_operation()) or
                    (self.sessions is not None and self.sessions.has_operation()) or
                    (self.state is not None and self.state.has_operation()) or
                    (self.vty_statistics is not None and self.vty_statistics.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "vty-line" + "[line-number='" + self.line_number.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-tty-server-oper:tty/vty-lines/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.line_number.is_set or self.line_number.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.line_number.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "configuration"):
                    if (self.configuration is None):
                        self.configuration = Tty.VtyLines.VtyLine.Configuration()
                        self.configuration.parent = self
                        self._children_name_map["configuration"] = "configuration"
                    return self.configuration

                if (child_yang_name == "sessions"):
                    if (self.sessions is None):
                        self.sessions = Tty.VtyLines.VtyLine.Sessions()
                        self.sessions.parent = self
                        self._children_name_map["sessions"] = "sessions"
                    return self.sessions

                if (child_yang_name == "state"):
                    if (self.state is None):
                        self.state = Tty.VtyLines.VtyLine.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                    return self.state

                if (child_yang_name == "vty-statistics"):
                    if (self.vty_statistics is None):
                        self.vty_statistics = Tty.VtyLines.VtyLine.VtyStatistics()
                        self.vty_statistics.parent = self
                        self._children_name_map["vty_statistics"] = "vty-statistics"
                    return self.vty_statistics

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "configuration" or name == "sessions" or name == "state" or name == "vty-statistics" or name == "line-number"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "line-number"):
                    self.line_number = value
                    self.line_number.value_namespace = name_space
                    self.line_number.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.vty_line:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.vty_line:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "vty-lines" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-tty-server-oper:tty/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "vty-line"):
                for c in self.vty_line:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Tty.VtyLines.VtyLine()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.vty_line.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "vty-line"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class AuxiliaryNodes(Entity):
        """
        List of Nodes attached with an auxiliary line
        
        .. attribute:: auxiliary_node
        
        	Line configuration on a node
        	**type**\: list of    :py:class:`AuxiliaryNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.AuxiliaryNodes.AuxiliaryNode>`
        
        

        """

        _prefix = 'tty-server-oper'
        _revision = '2015-07-30'

        def __init__(self):
            super(Tty.AuxiliaryNodes, self).__init__()

            self.yang_name = "auxiliary-nodes"
            self.yang_parent_name = "tty"

            self.auxiliary_node = YList(self)

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
                        super(Tty.AuxiliaryNodes, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Tty.AuxiliaryNodes, self).__setattr__(name, value)


        class AuxiliaryNode(Entity):
            """
            Line configuration on a node
            
            .. attribute:: id  <key>
            
            	Node ID
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: auxiliary_line
            
            	Auxiliary line
            	**type**\:   :py:class:`AuxiliaryLine <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine>`
            
            

            """

            _prefix = 'tty-server-oper'
            _revision = '2015-07-30'

            def __init__(self):
                super(Tty.AuxiliaryNodes.AuxiliaryNode, self).__init__()

                self.yang_name = "auxiliary-node"
                self.yang_parent_name = "auxiliary-nodes"

                self.id = YLeaf(YType.str, "id")

                self.auxiliary_line = Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine()
                self.auxiliary_line.parent = self
                self._children_name_map["auxiliary_line"] = "auxiliary-line"
                self._children_yang_names.add("auxiliary-line")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("id") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Tty.AuxiliaryNodes.AuxiliaryNode, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Tty.AuxiliaryNodes.AuxiliaryNode, self).__setattr__(name, value)


            class AuxiliaryLine(Entity):
                """
                Auxiliary line
                
                .. attribute:: auxiliary_statistics
                
                	Statistics of the auxiliary line
                	**type**\:   :py:class:`AuxiliaryStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics>`
                
                .. attribute:: configuration
                
                	Configuration information of the line
                	**type**\:   :py:class:`Configuration <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.Configuration>`
                
                .. attribute:: state
                
                	Line state information
                	**type**\:   :py:class:`State <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.State>`
                
                

                """

                _prefix = 'tty-server-oper'
                _revision = '2015-07-30'

                def __init__(self):
                    super(Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine, self).__init__()

                    self.yang_name = "auxiliary-line"
                    self.yang_parent_name = "auxiliary-node"

                    self.auxiliary_statistics = Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics()
                    self.auxiliary_statistics.parent = self
                    self._children_name_map["auxiliary_statistics"] = "auxiliary-statistics"
                    self._children_yang_names.add("auxiliary-statistics")

                    self.configuration = Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.Configuration()
                    self.configuration.parent = self
                    self._children_name_map["configuration"] = "configuration"
                    self._children_yang_names.add("configuration")

                    self.state = Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._children_yang_names.add("state")


                class AuxiliaryStatistics(Entity):
                    """
                    Statistics of the auxiliary line
                    
                    .. attribute:: aaa
                    
                    	AAA related statistics
                    	**type**\:   :py:class:`Aaa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.Aaa>`
                    
                    .. attribute:: exec_
                    
                    	Exec related statistics
                    	**type**\:   :py:class:`Exec_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.Exec_>`
                    
                    .. attribute:: general_statistics
                    
                    	General statistics of line
                    	**type**\:   :py:class:`GeneralStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.GeneralStatistics>`
                    
                    .. attribute:: rs232
                    
                    	RS232 statistics of console line
                    	**type**\:   :py:class:`Rs232 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.Rs232>`
                    
                    

                    """

                    _prefix = 'tty-server-oper'
                    _revision = '2015-07-30'

                    def __init__(self):
                        super(Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics, self).__init__()

                        self.yang_name = "auxiliary-statistics"
                        self.yang_parent_name = "auxiliary-line"

                        self.aaa = Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.Aaa()
                        self.aaa.parent = self
                        self._children_name_map["aaa"] = "aaa"
                        self._children_yang_names.add("aaa")

                        self.exec_ = Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.Exec_()
                        self.exec_.parent = self
                        self._children_name_map["exec_"] = "exec"
                        self._children_yang_names.add("exec")

                        self.general_statistics = Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.GeneralStatistics()
                        self.general_statistics.parent = self
                        self._children_name_map["general_statistics"] = "general-statistics"
                        self._children_yang_names.add("general-statistics")

                        self.rs232 = Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.Rs232()
                        self.rs232.parent = self
                        self._children_name_map["rs232"] = "rs232"
                        self._children_yang_names.add("rs232")


                    class Rs232(Entity):
                        """
                        RS232 statistics of console line
                        
                        .. attribute:: baud_rate
                        
                        	Inbound/Outbound baud rate in bps
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: bit/s
                        
                        .. attribute:: data_bits
                        
                        	Number of databits
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: bit
                        
                        .. attribute:: exec_disabled
                        
                        	Exec disabled on TTY
                        	**type**\:  bool
                        
                        .. attribute:: framing_error_count
                        
                        	Framing error count
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: hardware_flow_control_status
                        
                        	Hardware flow control status
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: overrun_error_count
                        
                        	Overrun error count
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: parity_error_count
                        
                        	Parity error count
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: parity_status
                        
                        	Parity status
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: stop_bits
                        
                        	Number of stopbits
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: bit
                        
                        

                        """

                        _prefix = 'tty-server-oper'
                        _revision = '2015-07-30'

                        def __init__(self):
                            super(Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.Rs232, self).__init__()

                            self.yang_name = "rs232"
                            self.yang_parent_name = "auxiliary-statistics"

                            self.baud_rate = YLeaf(YType.uint32, "baud-rate")

                            self.data_bits = YLeaf(YType.uint32, "data-bits")

                            self.exec_disabled = YLeaf(YType.boolean, "exec-disabled")

                            self.framing_error_count = YLeaf(YType.uint32, "framing-error-count")

                            self.hardware_flow_control_status = YLeaf(YType.uint32, "hardware-flow-control-status")

                            self.overrun_error_count = YLeaf(YType.uint32, "overrun-error-count")

                            self.parity_error_count = YLeaf(YType.uint32, "parity-error-count")

                            self.parity_status = YLeaf(YType.uint32, "parity-status")

                            self.stop_bits = YLeaf(YType.uint32, "stop-bits")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("baud_rate",
                                            "data_bits",
                                            "exec_disabled",
                                            "framing_error_count",
                                            "hardware_flow_control_status",
                                            "overrun_error_count",
                                            "parity_error_count",
                                            "parity_status",
                                            "stop_bits") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.Rs232, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.Rs232, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.baud_rate.is_set or
                                self.data_bits.is_set or
                                self.exec_disabled.is_set or
                                self.framing_error_count.is_set or
                                self.hardware_flow_control_status.is_set or
                                self.overrun_error_count.is_set or
                                self.parity_error_count.is_set or
                                self.parity_status.is_set or
                                self.stop_bits.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.baud_rate.yfilter != YFilter.not_set or
                                self.data_bits.yfilter != YFilter.not_set or
                                self.exec_disabled.yfilter != YFilter.not_set or
                                self.framing_error_count.yfilter != YFilter.not_set or
                                self.hardware_flow_control_status.yfilter != YFilter.not_set or
                                self.overrun_error_count.yfilter != YFilter.not_set or
                                self.parity_error_count.yfilter != YFilter.not_set or
                                self.parity_status.yfilter != YFilter.not_set or
                                self.stop_bits.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "rs232" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.baud_rate.is_set or self.baud_rate.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.baud_rate.get_name_leafdata())
                            if (self.data_bits.is_set or self.data_bits.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.data_bits.get_name_leafdata())
                            if (self.exec_disabled.is_set or self.exec_disabled.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.exec_disabled.get_name_leafdata())
                            if (self.framing_error_count.is_set or self.framing_error_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.framing_error_count.get_name_leafdata())
                            if (self.hardware_flow_control_status.is_set or self.hardware_flow_control_status.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.hardware_flow_control_status.get_name_leafdata())
                            if (self.overrun_error_count.is_set or self.overrun_error_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.overrun_error_count.get_name_leafdata())
                            if (self.parity_error_count.is_set or self.parity_error_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.parity_error_count.get_name_leafdata())
                            if (self.parity_status.is_set or self.parity_status.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.parity_status.get_name_leafdata())
                            if (self.stop_bits.is_set or self.stop_bits.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.stop_bits.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "baud-rate" or name == "data-bits" or name == "exec-disabled" or name == "framing-error-count" or name == "hardware-flow-control-status" or name == "overrun-error-count" or name == "parity-error-count" or name == "parity-status" or name == "stop-bits"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "baud-rate"):
                                self.baud_rate = value
                                self.baud_rate.value_namespace = name_space
                                self.baud_rate.value_namespace_prefix = name_space_prefix
                            if(value_path == "data-bits"):
                                self.data_bits = value
                                self.data_bits.value_namespace = name_space
                                self.data_bits.value_namespace_prefix = name_space_prefix
                            if(value_path == "exec-disabled"):
                                self.exec_disabled = value
                                self.exec_disabled.value_namespace = name_space
                                self.exec_disabled.value_namespace_prefix = name_space_prefix
                            if(value_path == "framing-error-count"):
                                self.framing_error_count = value
                                self.framing_error_count.value_namespace = name_space
                                self.framing_error_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "hardware-flow-control-status"):
                                self.hardware_flow_control_status = value
                                self.hardware_flow_control_status.value_namespace = name_space
                                self.hardware_flow_control_status.value_namespace_prefix = name_space_prefix
                            if(value_path == "overrun-error-count"):
                                self.overrun_error_count = value
                                self.overrun_error_count.value_namespace = name_space
                                self.overrun_error_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "parity-error-count"):
                                self.parity_error_count = value
                                self.parity_error_count.value_namespace = name_space
                                self.parity_error_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "parity-status"):
                                self.parity_status = value
                                self.parity_status.value_namespace = name_space
                                self.parity_status.value_namespace_prefix = name_space_prefix
                            if(value_path == "stop-bits"):
                                self.stop_bits = value
                                self.stop_bits.value_namespace = name_space
                                self.stop_bits.value_namespace_prefix = name_space_prefix


                    class GeneralStatistics(Entity):
                        """
                        General statistics of line
                        
                        .. attribute:: absolute_timeout
                        
                        	Absolute timeout period
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: async_interface
                        
                        	Usable as async interface
                        	**type**\:  bool
                        
                        .. attribute:: domain_lookup_enabled
                        
                        	DNS resolution enabled
                        	**type**\:  bool
                        
                        .. attribute:: flow_control_start_character
                        
                        	Software flow control start char
                        	**type**\:  int
                        
                        	**range:** \-128..127
                        
                        .. attribute:: flow_control_stop_character
                        
                        	Software flow control stop char
                        	**type**\:  int
                        
                        	**range:** \-128..127
                        
                        .. attribute:: idle_time
                        
                        	TTY idle time
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: motd_banner_enabled
                        
                        	MOTD banner enabled
                        	**type**\:  bool
                        
                        .. attribute:: private_flag
                        
                        	TTY private flag
                        	**type**\:  bool
                        
                        .. attribute:: terminal_length
                        
                        	Terminal length
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: terminal_type
                        
                        	Terminal type
                        	**type**\:  str
                        
                        .. attribute:: terminal_width
                        
                        	Line width
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'tty-server-oper'
                        _revision = '2015-07-30'

                        def __init__(self):
                            super(Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.GeneralStatistics, self).__init__()

                            self.yang_name = "general-statistics"
                            self.yang_parent_name = "auxiliary-statistics"

                            self.absolute_timeout = YLeaf(YType.uint32, "absolute-timeout")

                            self.async_interface = YLeaf(YType.boolean, "async-interface")

                            self.domain_lookup_enabled = YLeaf(YType.boolean, "domain-lookup-enabled")

                            self.flow_control_start_character = YLeaf(YType.int8, "flow-control-start-character")

                            self.flow_control_stop_character = YLeaf(YType.int8, "flow-control-stop-character")

                            self.idle_time = YLeaf(YType.uint32, "idle-time")

                            self.motd_banner_enabled = YLeaf(YType.boolean, "motd-banner-enabled")

                            self.private_flag = YLeaf(YType.boolean, "private-flag")

                            self.terminal_length = YLeaf(YType.uint32, "terminal-length")

                            self.terminal_type = YLeaf(YType.str, "terminal-type")

                            self.terminal_width = YLeaf(YType.uint32, "terminal-width")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("absolute_timeout",
                                            "async_interface",
                                            "domain_lookup_enabled",
                                            "flow_control_start_character",
                                            "flow_control_stop_character",
                                            "idle_time",
                                            "motd_banner_enabled",
                                            "private_flag",
                                            "terminal_length",
                                            "terminal_type",
                                            "terminal_width") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.GeneralStatistics, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.GeneralStatistics, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.absolute_timeout.is_set or
                                self.async_interface.is_set or
                                self.domain_lookup_enabled.is_set or
                                self.flow_control_start_character.is_set or
                                self.flow_control_stop_character.is_set or
                                self.idle_time.is_set or
                                self.motd_banner_enabled.is_set or
                                self.private_flag.is_set or
                                self.terminal_length.is_set or
                                self.terminal_type.is_set or
                                self.terminal_width.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.absolute_timeout.yfilter != YFilter.not_set or
                                self.async_interface.yfilter != YFilter.not_set or
                                self.domain_lookup_enabled.yfilter != YFilter.not_set or
                                self.flow_control_start_character.yfilter != YFilter.not_set or
                                self.flow_control_stop_character.yfilter != YFilter.not_set or
                                self.idle_time.yfilter != YFilter.not_set or
                                self.motd_banner_enabled.yfilter != YFilter.not_set or
                                self.private_flag.yfilter != YFilter.not_set or
                                self.terminal_length.yfilter != YFilter.not_set or
                                self.terminal_type.yfilter != YFilter.not_set or
                                self.terminal_width.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "general-statistics" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.absolute_timeout.is_set or self.absolute_timeout.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.absolute_timeout.get_name_leafdata())
                            if (self.async_interface.is_set or self.async_interface.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.async_interface.get_name_leafdata())
                            if (self.domain_lookup_enabled.is_set or self.domain_lookup_enabled.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.domain_lookup_enabled.get_name_leafdata())
                            if (self.flow_control_start_character.is_set or self.flow_control_start_character.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.flow_control_start_character.get_name_leafdata())
                            if (self.flow_control_stop_character.is_set or self.flow_control_stop_character.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.flow_control_stop_character.get_name_leafdata())
                            if (self.idle_time.is_set or self.idle_time.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.idle_time.get_name_leafdata())
                            if (self.motd_banner_enabled.is_set or self.motd_banner_enabled.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.motd_banner_enabled.get_name_leafdata())
                            if (self.private_flag.is_set or self.private_flag.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.private_flag.get_name_leafdata())
                            if (self.terminal_length.is_set or self.terminal_length.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.terminal_length.get_name_leafdata())
                            if (self.terminal_type.is_set or self.terminal_type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.terminal_type.get_name_leafdata())
                            if (self.terminal_width.is_set or self.terminal_width.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.terminal_width.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "absolute-timeout" or name == "async-interface" or name == "domain-lookup-enabled" or name == "flow-control-start-character" or name == "flow-control-stop-character" or name == "idle-time" or name == "motd-banner-enabled" or name == "private-flag" or name == "terminal-length" or name == "terminal-type" or name == "terminal-width"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "absolute-timeout"):
                                self.absolute_timeout = value
                                self.absolute_timeout.value_namespace = name_space
                                self.absolute_timeout.value_namespace_prefix = name_space_prefix
                            if(value_path == "async-interface"):
                                self.async_interface = value
                                self.async_interface.value_namespace = name_space
                                self.async_interface.value_namespace_prefix = name_space_prefix
                            if(value_path == "domain-lookup-enabled"):
                                self.domain_lookup_enabled = value
                                self.domain_lookup_enabled.value_namespace = name_space
                                self.domain_lookup_enabled.value_namespace_prefix = name_space_prefix
                            if(value_path == "flow-control-start-character"):
                                self.flow_control_start_character = value
                                self.flow_control_start_character.value_namespace = name_space
                                self.flow_control_start_character.value_namespace_prefix = name_space_prefix
                            if(value_path == "flow-control-stop-character"):
                                self.flow_control_stop_character = value
                                self.flow_control_stop_character.value_namespace = name_space
                                self.flow_control_stop_character.value_namespace_prefix = name_space_prefix
                            if(value_path == "idle-time"):
                                self.idle_time = value
                                self.idle_time.value_namespace = name_space
                                self.idle_time.value_namespace_prefix = name_space_prefix
                            if(value_path == "motd-banner-enabled"):
                                self.motd_banner_enabled = value
                                self.motd_banner_enabled.value_namespace = name_space
                                self.motd_banner_enabled.value_namespace_prefix = name_space_prefix
                            if(value_path == "private-flag"):
                                self.private_flag = value
                                self.private_flag.value_namespace = name_space
                                self.private_flag.value_namespace_prefix = name_space_prefix
                            if(value_path == "terminal-length"):
                                self.terminal_length = value
                                self.terminal_length.value_namespace = name_space
                                self.terminal_length.value_namespace_prefix = name_space_prefix
                            if(value_path == "terminal-type"):
                                self.terminal_type = value
                                self.terminal_type.value_namespace = name_space
                                self.terminal_type.value_namespace_prefix = name_space_prefix
                            if(value_path == "terminal-width"):
                                self.terminal_width = value
                                self.terminal_width.value_namespace = name_space
                                self.terminal_width.value_namespace_prefix = name_space_prefix


                    class Exec_(Entity):
                        """
                        Exec related statistics
                        
                        .. attribute:: time_stamp_enabled
                        
                        	Specifies whether timestamp is enabled or not
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'tty-server-oper'
                        _revision = '2015-07-30'

                        def __init__(self):
                            super(Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.Exec_, self).__init__()

                            self.yang_name = "exec"
                            self.yang_parent_name = "auxiliary-statistics"

                            self.time_stamp_enabled = YLeaf(YType.boolean, "time-stamp-enabled")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("time_stamp_enabled") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.Exec_, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.Exec_, self).__setattr__(name, value)

                        def has_data(self):
                            return self.time_stamp_enabled.is_set

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.time_stamp_enabled.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "exec" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.time_stamp_enabled.is_set or self.time_stamp_enabled.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.time_stamp_enabled.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "time-stamp-enabled"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "time-stamp-enabled"):
                                self.time_stamp_enabled = value
                                self.time_stamp_enabled.value_namespace = name_space
                                self.time_stamp_enabled.value_namespace_prefix = name_space_prefix


                    class Aaa(Entity):
                        """
                        AAA related statistics
                        
                        .. attribute:: user_name
                        
                        	The authenticated username
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'tty-server-oper'
                        _revision = '2015-07-30'

                        def __init__(self):
                            super(Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.Aaa, self).__init__()

                            self.yang_name = "aaa"
                            self.yang_parent_name = "auxiliary-statistics"

                            self.user_name = YLeaf(YType.str, "user-name")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("user_name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.Aaa, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.Aaa, self).__setattr__(name, value)

                        def has_data(self):
                            return self.user_name.is_set

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.user_name.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "aaa" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.user_name.is_set or self.user_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.user_name.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "user-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "user-name"):
                                self.user_name = value
                                self.user_name.value_namespace = name_space
                                self.user_name.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            (self.aaa is not None and self.aaa.has_data()) or
                            (self.exec_ is not None and self.exec_.has_data()) or
                            (self.general_statistics is not None and self.general_statistics.has_data()) or
                            (self.rs232 is not None and self.rs232.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.aaa is not None and self.aaa.has_operation()) or
                            (self.exec_ is not None and self.exec_.has_operation()) or
                            (self.general_statistics is not None and self.general_statistics.has_operation()) or
                            (self.rs232 is not None and self.rs232.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "auxiliary-statistics" + path_buffer

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

                        if (child_yang_name == "aaa"):
                            if (self.aaa is None):
                                self.aaa = Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.Aaa()
                                self.aaa.parent = self
                                self._children_name_map["aaa"] = "aaa"
                            return self.aaa

                        if (child_yang_name == "exec"):
                            if (self.exec_ is None):
                                self.exec_ = Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.Exec_()
                                self.exec_.parent = self
                                self._children_name_map["exec_"] = "exec"
                            return self.exec_

                        if (child_yang_name == "general-statistics"):
                            if (self.general_statistics is None):
                                self.general_statistics = Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.GeneralStatistics()
                                self.general_statistics.parent = self
                                self._children_name_map["general_statistics"] = "general-statistics"
                            return self.general_statistics

                        if (child_yang_name == "rs232"):
                            if (self.rs232 is None):
                                self.rs232 = Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.Rs232()
                                self.rs232.parent = self
                                self._children_name_map["rs232"] = "rs232"
                            return self.rs232

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "aaa" or name == "exec" or name == "general-statistics" or name == "rs232"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class State(Entity):
                    """
                    Line state information
                    
                    .. attribute:: general
                    
                    	General information
                    	**type**\:   :py:class:`General <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.State.General>`
                    
                    .. attribute:: template
                    
                    	Information related to template applied to the line
                    	**type**\:   :py:class:`Template <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.State.Template>`
                    
                    

                    """

                    _prefix = 'tty-server-oper'
                    _revision = '2015-07-30'

                    def __init__(self):
                        super(Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "auxiliary-line"

                        self.general = Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.State.General()
                        self.general.parent = self
                        self._children_name_map["general"] = "general"
                        self._children_yang_names.add("general")

                        self.template = Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.State.Template()
                        self.template.parent = self
                        self._children_name_map["template"] = "template"
                        self._children_yang_names.add("template")


                    class Template(Entity):
                        """
                        Information related to template applied to the
                        line
                        
                        .. attribute:: name
                        
                        	Name of the template
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'tty-server-oper'
                        _revision = '2015-07-30'

                        def __init__(self):
                            super(Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.State.Template, self).__init__()

                            self.yang_name = "template"
                            self.yang_parent_name = "state"

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
                                if name in ("name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.State.Template, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.State.Template, self).__setattr__(name, value)

                        def has_data(self):
                            return self.name.is_set

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.name.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "template" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
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
                            if(name == "name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "name"):
                                self.name = value
                                self.name.value_namespace = name_space
                                self.name.value_namespace_prefix = name_space_prefix


                    class General(Entity):
                        """
                        General information
                        
                        .. attribute:: general_state
                        
                        	State of the line
                        	**type**\:   :py:class:`LineState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.LineState>`
                        
                        .. attribute:: operation_
                        
                        	application running of on the tty line
                        	**type**\:   :py:class:`SessionOperation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.SessionOperation>`
                        
                        

                        """

                        _prefix = 'tty-server-oper'
                        _revision = '2015-07-30'

                        def __init__(self):
                            super(Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.State.General, self).__init__()

                            self.yang_name = "general"
                            self.yang_parent_name = "state"

                            self.general_state = YLeaf(YType.enumeration, "general-state")

                            self.operation_ = YLeaf(YType.enumeration, "operation")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("general_state",
                                            "operation_") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.State.General, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.State.General, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.general_state.is_set or
                                self.operation_.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.general_state.yfilter != YFilter.not_set or
                                self.operation_.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "general" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.general_state.is_set or self.general_state.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.general_state.get_name_leafdata())
                            if (self.operation_.is_set or self.operation_.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.operation_.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "general-state" or name == "operation"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "general-state"):
                                self.general_state = value
                                self.general_state.value_namespace = name_space
                                self.general_state.value_namespace_prefix = name_space_prefix
                            if(value_path == "operation"):
                                self.operation_ = value
                                self.operation_.value_namespace = name_space
                                self.operation_.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            (self.general is not None and self.general.has_data()) or
                            (self.template is not None and self.template.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.general is not None and self.general.has_operation()) or
                            (self.template is not None and self.template.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "state" + path_buffer

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

                        if (child_yang_name == "general"):
                            if (self.general is None):
                                self.general = Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.State.General()
                                self.general.parent = self
                                self._children_name_map["general"] = "general"
                            return self.general

                        if (child_yang_name == "template"):
                            if (self.template is None):
                                self.template = Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.State.Template()
                                self.template.parent = self
                                self._children_name_map["template"] = "template"
                            return self.template

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "general" or name == "template"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class Configuration(Entity):
                    """
                    Configuration information of the line
                    
                    .. attribute:: connection_configuration
                    
                    	Conection configuration information
                    	**type**\:   :py:class:`ConnectionConfiguration <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.Configuration.ConnectionConfiguration>`
                    
                    

                    """

                    _prefix = 'tty-server-oper'
                    _revision = '2015-07-30'

                    def __init__(self):
                        super(Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.Configuration, self).__init__()

                        self.yang_name = "configuration"
                        self.yang_parent_name = "auxiliary-line"

                        self.connection_configuration = Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.Configuration.ConnectionConfiguration()
                        self.connection_configuration.parent = self
                        self._children_name_map["connection_configuration"] = "connection-configuration"
                        self._children_yang_names.add("connection-configuration")


                    class ConnectionConfiguration(Entity):
                        """
                        Conection configuration information
                        
                        .. attribute:: acl_in
                        
                        	ACL for inbound traffic
                        	**type**\:  str
                        
                        .. attribute:: acl_out
                        
                        	ACL for outbound traffic
                        	**type**\:  str
                        
                        .. attribute:: transport_input
                        
                        	Protocols to use when connecting to the terminal server
                        	**type**\:   :py:class:`TransportInput <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.Configuration.ConnectionConfiguration.TransportInput>`
                        
                        

                        """

                        _prefix = 'tty-server-oper'
                        _revision = '2015-07-30'

                        def __init__(self):
                            super(Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.Configuration.ConnectionConfiguration, self).__init__()

                            self.yang_name = "connection-configuration"
                            self.yang_parent_name = "configuration"

                            self.acl_in = YLeaf(YType.str, "acl-in")

                            self.acl_out = YLeaf(YType.str, "acl-out")

                            self.transport_input = Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.Configuration.ConnectionConfiguration.TransportInput()
                            self.transport_input.parent = self
                            self._children_name_map["transport_input"] = "transport-input"
                            self._children_yang_names.add("transport-input")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("acl_in",
                                            "acl_out") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.Configuration.ConnectionConfiguration, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.Configuration.ConnectionConfiguration, self).__setattr__(name, value)


                        class TransportInput(Entity):
                            """
                            Protocols to use when connecting to the
                            terminal server
                            
                            .. attribute:: none
                            
                            	Not used
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: protocol1
                            
                            	Transport protocol1
                            	**type**\:   :py:class:`TtyTransportProtocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes.TtyTransportProtocol>`
                            
                            .. attribute:: protocol2
                            
                            	Transport protocol2
                            	**type**\:   :py:class:`TtyTransportProtocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes.TtyTransportProtocol>`
                            
                            .. attribute:: select
                            
                            	Choose transport protocols
                            	**type**\:   :py:class:`TtyTransportProtocolSelect <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes.TtyTransportProtocolSelect>`
                            
                            	**default value**\: all
                            
                            

                            """

                            _prefix = 'tty-server-oper'
                            _revision = '2015-07-30'

                            def __init__(self):
                                super(Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.Configuration.ConnectionConfiguration.TransportInput, self).__init__()

                                self.yang_name = "transport-input"
                                self.yang_parent_name = "connection-configuration"

                                self.none = YLeaf(YType.int32, "none")

                                self.protocol1 = YLeaf(YType.enumeration, "protocol1")

                                self.protocol2 = YLeaf(YType.enumeration, "protocol2")

                                self.select = YLeaf(YType.enumeration, "select")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("none",
                                                "protocol1",
                                                "protocol2",
                                                "select") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.Configuration.ConnectionConfiguration.TransportInput, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.Configuration.ConnectionConfiguration.TransportInput, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.none.is_set or
                                    self.protocol1.is_set or
                                    self.protocol2.is_set or
                                    self.select.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.none.yfilter != YFilter.not_set or
                                    self.protocol1.yfilter != YFilter.not_set or
                                    self.protocol2.yfilter != YFilter.not_set or
                                    self.select.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "transport-input" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.none.is_set or self.none.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.none.get_name_leafdata())
                                if (self.protocol1.is_set or self.protocol1.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.protocol1.get_name_leafdata())
                                if (self.protocol2.is_set or self.protocol2.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.protocol2.get_name_leafdata())
                                if (self.select.is_set or self.select.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.select.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "none" or name == "protocol1" or name == "protocol2" or name == "select"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "none"):
                                    self.none = value
                                    self.none.value_namespace = name_space
                                    self.none.value_namespace_prefix = name_space_prefix
                                if(value_path == "protocol1"):
                                    self.protocol1 = value
                                    self.protocol1.value_namespace = name_space
                                    self.protocol1.value_namespace_prefix = name_space_prefix
                                if(value_path == "protocol2"):
                                    self.protocol2 = value
                                    self.protocol2.value_namespace = name_space
                                    self.protocol2.value_namespace_prefix = name_space_prefix
                                if(value_path == "select"):
                                    self.select = value
                                    self.select.value_namespace = name_space
                                    self.select.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.acl_in.is_set or
                                self.acl_out.is_set or
                                (self.transport_input is not None and self.transport_input.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.acl_in.yfilter != YFilter.not_set or
                                self.acl_out.yfilter != YFilter.not_set or
                                (self.transport_input is not None and self.transport_input.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "connection-configuration" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.acl_in.is_set or self.acl_in.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.acl_in.get_name_leafdata())
                            if (self.acl_out.is_set or self.acl_out.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.acl_out.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "transport-input"):
                                if (self.transport_input is None):
                                    self.transport_input = Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.Configuration.ConnectionConfiguration.TransportInput()
                                    self.transport_input.parent = self
                                    self._children_name_map["transport_input"] = "transport-input"
                                return self.transport_input

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "transport-input" or name == "acl-in" or name == "acl-out"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "acl-in"):
                                self.acl_in = value
                                self.acl_in.value_namespace = name_space
                                self.acl_in.value_namespace_prefix = name_space_prefix
                            if(value_path == "acl-out"):
                                self.acl_out = value
                                self.acl_out.value_namespace = name_space
                                self.acl_out.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (self.connection_configuration is not None and self.connection_configuration.has_data())

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.connection_configuration is not None and self.connection_configuration.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "configuration" + path_buffer

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

                        if (child_yang_name == "connection-configuration"):
                            if (self.connection_configuration is None):
                                self.connection_configuration = Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.Configuration.ConnectionConfiguration()
                                self.connection_configuration.parent = self
                                self._children_name_map["connection_configuration"] = "connection-configuration"
                            return self.connection_configuration

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "connection-configuration"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        (self.auxiliary_statistics is not None and self.auxiliary_statistics.has_data()) or
                        (self.configuration is not None and self.configuration.has_data()) or
                        (self.state is not None and self.state.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.auxiliary_statistics is not None and self.auxiliary_statistics.has_operation()) or
                        (self.configuration is not None and self.configuration.has_operation()) or
                        (self.state is not None and self.state.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "auxiliary-line" + path_buffer

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

                    if (child_yang_name == "auxiliary-statistics"):
                        if (self.auxiliary_statistics is None):
                            self.auxiliary_statistics = Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics()
                            self.auxiliary_statistics.parent = self
                            self._children_name_map["auxiliary_statistics"] = "auxiliary-statistics"
                        return self.auxiliary_statistics

                    if (child_yang_name == "configuration"):
                        if (self.configuration is None):
                            self.configuration = Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.Configuration()
                            self.configuration.parent = self
                            self._children_name_map["configuration"] = "configuration"
                        return self.configuration

                    if (child_yang_name == "state"):
                        if (self.state is None):
                            self.state = Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                        return self.state

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "auxiliary-statistics" or name == "configuration" or name == "state"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.id.is_set or
                    (self.auxiliary_line is not None and self.auxiliary_line.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.id.yfilter != YFilter.not_set or
                    (self.auxiliary_line is not None and self.auxiliary_line.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "auxiliary-node" + "[id='" + self.id.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-tty-server-oper:tty/auxiliary-nodes/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.id.is_set or self.id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.id.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "auxiliary-line"):
                    if (self.auxiliary_line is None):
                        self.auxiliary_line = Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine()
                        self.auxiliary_line.parent = self
                        self._children_name_map["auxiliary_line"] = "auxiliary-line"
                    return self.auxiliary_line

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "auxiliary-line" or name == "id"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "id"):
                    self.id = value
                    self.id.value_namespace = name_space
                    self.id.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.auxiliary_node:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.auxiliary_node:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "auxiliary-nodes" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-tty-server-oper:tty/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "auxiliary-node"):
                for c in self.auxiliary_node:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Tty.AuxiliaryNodes.AuxiliaryNode()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.auxiliary_node.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "auxiliary-node"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.auxiliary_nodes is not None and self.auxiliary_nodes.has_data()) or
            (self.console_nodes is not None and self.console_nodes.has_data()) or
            (self.vty_lines is not None and self.vty_lines.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.auxiliary_nodes is not None and self.auxiliary_nodes.has_operation()) or
            (self.console_nodes is not None and self.console_nodes.has_operation()) or
            (self.vty_lines is not None and self.vty_lines.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-tty-server-oper:tty" + path_buffer

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

        if (child_yang_name == "auxiliary-nodes"):
            if (self.auxiliary_nodes is None):
                self.auxiliary_nodes = Tty.AuxiliaryNodes()
                self.auxiliary_nodes.parent = self
                self._children_name_map["auxiliary_nodes"] = "auxiliary-nodes"
            return self.auxiliary_nodes

        if (child_yang_name == "console-nodes"):
            if (self.console_nodes is None):
                self.console_nodes = Tty.ConsoleNodes()
                self.console_nodes.parent = self
                self._children_name_map["console_nodes"] = "console-nodes"
            return self.console_nodes

        if (child_yang_name == "vty-lines"):
            if (self.vty_lines is None):
                self.vty_lines = Tty.VtyLines()
                self.vty_lines.parent = self
                self._children_name_map["vty_lines"] = "vty-lines"
            return self.vty_lines

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "auxiliary-nodes" or name == "console-nodes" or name == "vty-lines"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Tty()
        return self._top_entity

