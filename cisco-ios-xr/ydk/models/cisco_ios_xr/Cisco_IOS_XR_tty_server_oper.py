""" Cisco_IOS_XR_tty_server_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR tty\-server package operational data.

This module contains definitions
for the following management objects\:
  tty\: TTY Line Configuration

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
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
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"auxiliary-nodes" : ("auxiliary_nodes", Tty.AuxiliaryNodes), "console-nodes" : ("console_nodes", Tty.ConsoleNodes), "vty-lines" : ("vty_lines", Tty.VtyLines)}
        self._child_list_classes = {}

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
        self._segment_path = lambda: "Cisco-IOS-XR-tty-server-oper:tty"


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
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"auxiliary-node" : ("auxiliary_node", Tty.AuxiliaryNodes.AuxiliaryNode)}

            self.auxiliary_node = YList(self)
            self._segment_path = lambda: "auxiliary-nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-tty-server-oper:tty/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Tty.AuxiliaryNodes, [], name, value)


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
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"auxiliary-line" : ("auxiliary_line", Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine)}
                self._child_list_classes = {}

                self.id = YLeaf(YType.str, "id")

                self.auxiliary_line = Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine()
                self.auxiliary_line.parent = self
                self._children_name_map["auxiliary_line"] = "auxiliary-line"
                self._children_yang_names.add("auxiliary-line")
                self._segment_path = lambda: "auxiliary-node" + "[id='" + self.id.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-tty-server-oper:tty/auxiliary-nodes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Tty.AuxiliaryNodes.AuxiliaryNode, ['id'], name, value)


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
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"auxiliary-statistics" : ("auxiliary_statistics", Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics), "configuration" : ("configuration", Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.Configuration), "state" : ("state", Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.State)}
                    self._child_list_classes = {}

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
                    self._segment_path = lambda: "auxiliary-line"


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
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"aaa" : ("aaa", Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.Aaa), "exec" : ("exec_", Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.Exec_), "general-statistics" : ("general_statistics", Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.GeneralStatistics), "rs232" : ("rs232", Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.Rs232)}
                        self._child_list_classes = {}

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
                        self._segment_path = lambda: "auxiliary-statistics"


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
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.user_name = YLeaf(YType.str, "user-name")
                            self._segment_path = lambda: "aaa"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.Aaa, ['user_name'], name, value)


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
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.time_stamp_enabled = YLeaf(YType.boolean, "time-stamp-enabled")
                            self._segment_path = lambda: "exec"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.Exec_, ['time_stamp_enabled'], name, value)


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
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

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
                            self._segment_path = lambda: "general-statistics"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.GeneralStatistics, ['absolute_timeout', 'async_interface', 'domain_lookup_enabled', 'flow_control_start_character', 'flow_control_stop_character', 'idle_time', 'motd_banner_enabled', 'private_flag', 'terminal_length', 'terminal_type', 'terminal_width'], name, value)


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
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.baud_rate = YLeaf(YType.uint32, "baud-rate")

                            self.data_bits = YLeaf(YType.uint32, "data-bits")

                            self.exec_disabled = YLeaf(YType.boolean, "exec-disabled")

                            self.framing_error_count = YLeaf(YType.uint32, "framing-error-count")

                            self.hardware_flow_control_status = YLeaf(YType.uint32, "hardware-flow-control-status")

                            self.overrun_error_count = YLeaf(YType.uint32, "overrun-error-count")

                            self.parity_error_count = YLeaf(YType.uint32, "parity-error-count")

                            self.parity_status = YLeaf(YType.uint32, "parity-status")

                            self.stop_bits = YLeaf(YType.uint32, "stop-bits")
                            self._segment_path = lambda: "rs232"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.Rs232, ['baud_rate', 'data_bits', 'exec_disabled', 'framing_error_count', 'hardware_flow_control_status', 'overrun_error_count', 'parity_error_count', 'parity_status', 'stop_bits'], name, value)


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
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"connection-configuration" : ("connection_configuration", Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.Configuration.ConnectionConfiguration)}
                        self._child_list_classes = {}

                        self.connection_configuration = Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.Configuration.ConnectionConfiguration()
                        self.connection_configuration.parent = self
                        self._children_name_map["connection_configuration"] = "connection-configuration"
                        self._children_yang_names.add("connection-configuration")
                        self._segment_path = lambda: "configuration"


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
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"transport-input" : ("transport_input", Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.Configuration.ConnectionConfiguration.TransportInput)}
                            self._child_list_classes = {}

                            self.acl_in = YLeaf(YType.str, "acl-in")

                            self.acl_out = YLeaf(YType.str, "acl-out")

                            self.transport_input = Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.Configuration.ConnectionConfiguration.TransportInput()
                            self.transport_input.parent = self
                            self._children_name_map["transport_input"] = "transport-input"
                            self._children_yang_names.add("transport-input")
                            self._segment_path = lambda: "connection-configuration"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.Configuration.ConnectionConfiguration, ['acl_in', 'acl_out'], name, value)


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
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.none = YLeaf(YType.int32, "none")

                                self.protocol1 = YLeaf(YType.enumeration, "protocol1")

                                self.protocol2 = YLeaf(YType.enumeration, "protocol2")

                                self.select = YLeaf(YType.enumeration, "select")
                                self._segment_path = lambda: "transport-input"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.Configuration.ConnectionConfiguration.TransportInput, ['none', 'protocol1', 'protocol2', 'select'], name, value)


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
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"general" : ("general", Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.State.General), "template" : ("template", Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.State.Template)}
                        self._child_list_classes = {}

                        self.general = Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.State.General()
                        self.general.parent = self
                        self._children_name_map["general"] = "general"
                        self._children_yang_names.add("general")

                        self.template = Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.State.Template()
                        self.template.parent = self
                        self._children_name_map["template"] = "template"
                        self._children_yang_names.add("template")
                        self._segment_path = lambda: "state"


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
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.general_state = YLeaf(YType.enumeration, "general-state")

                            self.operation_ = YLeaf(YType.enumeration, "operation")
                            self._segment_path = lambda: "general"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.State.General, ['general_state', 'operation_'], name, value)


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
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.name = YLeaf(YType.str, "name")
                            self._segment_path = lambda: "template"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.State.Template, ['name'], name, value)


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
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"console-node" : ("console_node", Tty.ConsoleNodes.ConsoleNode)}

            self.console_node = YList(self)
            self._segment_path = lambda: "console-nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-tty-server-oper:tty/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Tty.ConsoleNodes, [], name, value)


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
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"console-line" : ("console_line", Tty.ConsoleNodes.ConsoleNode.ConsoleLine)}
                self._child_list_classes = {}

                self.id = YLeaf(YType.str, "id")

                self.console_line = Tty.ConsoleNodes.ConsoleNode.ConsoleLine()
                self.console_line.parent = self
                self._children_name_map["console_line"] = "console-line"
                self._children_yang_names.add("console-line")
                self._segment_path = lambda: "console-node" + "[id='" + self.id.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-tty-server-oper:tty/console-nodes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Tty.ConsoleNodes.ConsoleNode, ['id'], name, value)


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
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"configuration" : ("configuration", Tty.ConsoleNodes.ConsoleNode.ConsoleLine.Configuration), "console-statistics" : ("console_statistics", Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics), "state" : ("state", Tty.ConsoleNodes.ConsoleNode.ConsoleLine.State)}
                    self._child_list_classes = {}

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
                    self._segment_path = lambda: "console-line"


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
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"connection-configuration" : ("connection_configuration", Tty.ConsoleNodes.ConsoleNode.ConsoleLine.Configuration.ConnectionConfiguration)}
                        self._child_list_classes = {}

                        self.connection_configuration = Tty.ConsoleNodes.ConsoleNode.ConsoleLine.Configuration.ConnectionConfiguration()
                        self.connection_configuration.parent = self
                        self._children_name_map["connection_configuration"] = "connection-configuration"
                        self._children_yang_names.add("connection-configuration")
                        self._segment_path = lambda: "configuration"


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
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"transport-input" : ("transport_input", Tty.ConsoleNodes.ConsoleNode.ConsoleLine.Configuration.ConnectionConfiguration.TransportInput)}
                            self._child_list_classes = {}

                            self.acl_in = YLeaf(YType.str, "acl-in")

                            self.acl_out = YLeaf(YType.str, "acl-out")

                            self.transport_input = Tty.ConsoleNodes.ConsoleNode.ConsoleLine.Configuration.ConnectionConfiguration.TransportInput()
                            self.transport_input.parent = self
                            self._children_name_map["transport_input"] = "transport-input"
                            self._children_yang_names.add("transport-input")
                            self._segment_path = lambda: "connection-configuration"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Tty.ConsoleNodes.ConsoleNode.ConsoleLine.Configuration.ConnectionConfiguration, ['acl_in', 'acl_out'], name, value)


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
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.none = YLeaf(YType.int32, "none")

                                self.protocol1 = YLeaf(YType.enumeration, "protocol1")

                                self.protocol2 = YLeaf(YType.enumeration, "protocol2")

                                self.select = YLeaf(YType.enumeration, "select")
                                self._segment_path = lambda: "transport-input"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Tty.ConsoleNodes.ConsoleNode.ConsoleLine.Configuration.ConnectionConfiguration.TransportInput, ['none', 'protocol1', 'protocol2', 'select'], name, value)


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
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"aaa" : ("aaa", Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.Aaa), "exec" : ("exec_", Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.Exec_), "general-statistics" : ("general_statistics", Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.GeneralStatistics), "rs232" : ("rs232", Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.Rs232)}
                        self._child_list_classes = {}

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
                        self._segment_path = lambda: "console-statistics"


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
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.user_name = YLeaf(YType.str, "user-name")
                            self._segment_path = lambda: "aaa"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.Aaa, ['user_name'], name, value)


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
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.time_stamp_enabled = YLeaf(YType.boolean, "time-stamp-enabled")
                            self._segment_path = lambda: "exec"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.Exec_, ['time_stamp_enabled'], name, value)


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
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

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
                            self._segment_path = lambda: "general-statistics"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.GeneralStatistics, ['absolute_timeout', 'async_interface', 'domain_lookup_enabled', 'flow_control_start_character', 'flow_control_stop_character', 'idle_time', 'motd_banner_enabled', 'private_flag', 'terminal_length', 'terminal_type', 'terminal_width'], name, value)


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
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.baud_rate = YLeaf(YType.uint32, "baud-rate")

                            self.data_bits = YLeaf(YType.uint32, "data-bits")

                            self.exec_disabled = YLeaf(YType.boolean, "exec-disabled")

                            self.framing_error_count = YLeaf(YType.uint32, "framing-error-count")

                            self.hardware_flow_control_status = YLeaf(YType.uint32, "hardware-flow-control-status")

                            self.overrun_error_count = YLeaf(YType.uint32, "overrun-error-count")

                            self.parity_error_count = YLeaf(YType.uint32, "parity-error-count")

                            self.parity_status = YLeaf(YType.uint32, "parity-status")

                            self.stop_bits = YLeaf(YType.uint32, "stop-bits")
                            self._segment_path = lambda: "rs232"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.Rs232, ['baud_rate', 'data_bits', 'exec_disabled', 'framing_error_count', 'hardware_flow_control_status', 'overrun_error_count', 'parity_error_count', 'parity_status', 'stop_bits'], name, value)


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
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"general" : ("general", Tty.ConsoleNodes.ConsoleNode.ConsoleLine.State.General), "template" : ("template", Tty.ConsoleNodes.ConsoleNode.ConsoleLine.State.Template)}
                        self._child_list_classes = {}

                        self.general = Tty.ConsoleNodes.ConsoleNode.ConsoleLine.State.General()
                        self.general.parent = self
                        self._children_name_map["general"] = "general"
                        self._children_yang_names.add("general")

                        self.template = Tty.ConsoleNodes.ConsoleNode.ConsoleLine.State.Template()
                        self.template.parent = self
                        self._children_name_map["template"] = "template"
                        self._children_yang_names.add("template")
                        self._segment_path = lambda: "state"


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
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.general_state = YLeaf(YType.enumeration, "general-state")

                            self.operation_ = YLeaf(YType.enumeration, "operation")
                            self._segment_path = lambda: "general"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Tty.ConsoleNodes.ConsoleNode.ConsoleLine.State.General, ['general_state', 'operation_'], name, value)


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
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.name = YLeaf(YType.str, "name")
                            self._segment_path = lambda: "template"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Tty.ConsoleNodes.ConsoleNode.ConsoleLine.State.Template, ['name'], name, value)


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
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"vty-line" : ("vty_line", Tty.VtyLines.VtyLine)}

            self.vty_line = YList(self)
            self._segment_path = lambda: "vty-lines"
            self._absolute_path = lambda: "Cisco-IOS-XR-tty-server-oper:tty/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Tty.VtyLines, [], name, value)


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
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"configuration" : ("configuration", Tty.VtyLines.VtyLine.Configuration), "sessions" : ("sessions", Tty.VtyLines.VtyLine.Sessions), "state" : ("state", Tty.VtyLines.VtyLine.State), "vty-statistics" : ("vty_statistics", Tty.VtyLines.VtyLine.VtyStatistics)}
                self._child_list_classes = {}

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
                self._segment_path = lambda: "vty-line" + "[line-number='" + self.line_number.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-tty-server-oper:tty/vty-lines/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Tty.VtyLines.VtyLine, ['line_number'], name, value)


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
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"connection-configuration" : ("connection_configuration", Tty.VtyLines.VtyLine.Configuration.ConnectionConfiguration)}
                    self._child_list_classes = {}

                    self.connection_configuration = Tty.VtyLines.VtyLine.Configuration.ConnectionConfiguration()
                    self.connection_configuration.parent = self
                    self._children_name_map["connection_configuration"] = "connection-configuration"
                    self._children_yang_names.add("connection-configuration")
                    self._segment_path = lambda: "configuration"


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
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"transport-input" : ("transport_input", Tty.VtyLines.VtyLine.Configuration.ConnectionConfiguration.TransportInput)}
                        self._child_list_classes = {}

                        self.acl_in = YLeaf(YType.str, "acl-in")

                        self.acl_out = YLeaf(YType.str, "acl-out")

                        self.transport_input = Tty.VtyLines.VtyLine.Configuration.ConnectionConfiguration.TransportInput()
                        self.transport_input.parent = self
                        self._children_name_map["transport_input"] = "transport-input"
                        self._children_yang_names.add("transport-input")
                        self._segment_path = lambda: "connection-configuration"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Tty.VtyLines.VtyLine.Configuration.ConnectionConfiguration, ['acl_in', 'acl_out'], name, value)


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
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.none = YLeaf(YType.int32, "none")

                            self.protocol1 = YLeaf(YType.enumeration, "protocol1")

                            self.protocol2 = YLeaf(YType.enumeration, "protocol2")

                            self.select = YLeaf(YType.enumeration, "select")
                            self._segment_path = lambda: "transport-input"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Tty.VtyLines.VtyLine.Configuration.ConnectionConfiguration.TransportInput, ['none', 'protocol1', 'protocol2', 'select'], name, value)


            class Sessions(Entity):
                """
                Outgoing sessions
                
                .. attribute:: outgoing_connection
                
                	List of outgoing sessions
                	**type**\: list of    :py:class:`OutgoingConnection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.VtyLines.VtyLine.Sessions.OutgoingConnection>`
                
                

                """

                _prefix = 'tty-management-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Tty.VtyLines.VtyLine.Sessions, self).__init__()

                    self.yang_name = "sessions"
                    self.yang_parent_name = "vty-line"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"outgoing-connection" : ("outgoing_connection", Tty.VtyLines.VtyLine.Sessions.OutgoingConnection)}

                    self.outgoing_connection = YList(self)
                    self._segment_path = lambda: "Cisco-IOS-XR-tty-management-oper:sessions"

                def __setattr__(self, name, value):
                    self._perform_setattr(Tty.VtyLines.VtyLine.Sessions, [], name, value)


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
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Tty.VtyLines.VtyLine.Sessions.OutgoingConnection, self).__init__()

                        self.yang_name = "outgoing-connection"
                        self.yang_parent_name = "sessions"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"host-address" : ("host_address", Tty.VtyLines.VtyLine.Sessions.OutgoingConnection.HostAddress)}
                        self._child_list_classes = {}

                        self.connection_id = YLeaf(YType.uint8, "connection-id")

                        self.host_name = YLeaf(YType.str, "host-name")

                        self.idle_time = YLeaf(YType.uint32, "idle-time")

                        self.is_last_active_session = YLeaf(YType.boolean, "is-last-active-session")

                        self.transport_protocol = YLeaf(YType.enumeration, "transport-protocol")

                        self.host_address = Tty.VtyLines.VtyLine.Sessions.OutgoingConnection.HostAddress()
                        self.host_address.parent = self
                        self._children_name_map["host_address"] = "host-address"
                        self._children_yang_names.add("host-address")
                        self._segment_path = lambda: "outgoing-connection"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Tty.VtyLines.VtyLine.Sessions.OutgoingConnection, ['connection_id', 'host_name', 'idle_time', 'is_last_active_session', 'transport_protocol'], name, value)


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
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Tty.VtyLines.VtyLine.Sessions.OutgoingConnection.HostAddress, self).__init__()

                            self.yang_name = "host-address"
                            self.yang_parent_name = "outgoing-connection"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.af_name = YLeaf(YType.identityref, "af-name")

                            self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                            self.ipv6_address = YLeaf(YType.str, "ipv6-address")
                            self._segment_path = lambda: "host-address"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Tty.VtyLines.VtyLine.Sessions.OutgoingConnection.HostAddress, ['af_name', 'ipv4_address', 'ipv6_address'], name, value)


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
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"general" : ("general", Tty.VtyLines.VtyLine.State.General), "template" : ("template", Tty.VtyLines.VtyLine.State.Template)}
                    self._child_list_classes = {}

                    self.general = Tty.VtyLines.VtyLine.State.General()
                    self.general.parent = self
                    self._children_name_map["general"] = "general"
                    self._children_yang_names.add("general")

                    self.template = Tty.VtyLines.VtyLine.State.Template()
                    self.template.parent = self
                    self._children_name_map["template"] = "template"
                    self._children_yang_names.add("template")
                    self._segment_path = lambda: "state"


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
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.general_state = YLeaf(YType.enumeration, "general-state")

                        self.operation_ = YLeaf(YType.enumeration, "operation")
                        self._segment_path = lambda: "general"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Tty.VtyLines.VtyLine.State.General, ['general_state', 'operation_'], name, value)


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
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.name = YLeaf(YType.str, "name")
                        self._segment_path = lambda: "template"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Tty.VtyLines.VtyLine.State.Template, ['name'], name, value)


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
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"aaa" : ("aaa", Tty.VtyLines.VtyLine.VtyStatistics.Aaa), "connection" : ("connection", Tty.VtyLines.VtyLine.VtyStatistics.Connection), "exec" : ("exec_", Tty.VtyLines.VtyLine.VtyStatistics.Exec_), "general-statistics" : ("general_statistics", Tty.VtyLines.VtyLine.VtyStatistics.GeneralStatistics)}
                    self._child_list_classes = {}

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
                    self._segment_path = lambda: "vty-statistics"


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
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.user_name = YLeaf(YType.str, "user-name")
                        self._segment_path = lambda: "aaa"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Tty.VtyLines.VtyLine.VtyStatistics.Aaa, ['user_name'], name, value)


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
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.host_address_family = YLeaf(YType.uint32, "host-address-family")

                        self.incoming_host_address = YLeaf(YType.str, "incoming-host-address")

                        self.service = YLeaf(YType.uint32, "service")
                        self._segment_path = lambda: "connection"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Tty.VtyLines.VtyLine.VtyStatistics.Connection, ['host_address_family', 'incoming_host_address', 'service'], name, value)


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
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.time_stamp_enabled = YLeaf(YType.boolean, "time-stamp-enabled")
                        self._segment_path = lambda: "exec"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Tty.VtyLines.VtyLine.VtyStatistics.Exec_, ['time_stamp_enabled'], name, value)


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
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

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
                        self._segment_path = lambda: "general-statistics"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Tty.VtyLines.VtyLine.VtyStatistics.GeneralStatistics, ['absolute_timeout', 'async_interface', 'domain_lookup_enabled', 'flow_control_start_character', 'flow_control_stop_character', 'idle_time', 'motd_banner_enabled', 'private_flag', 'terminal_length', 'terminal_type', 'terminal_width'], name, value)

    def clone_ptr(self):
        self._top_entity = Tty()
        return self._top_entity

