""" Cisco_IOS_XR_tty_server_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR tty\-server package operational data.

This module contains definitions
for the following management objects\:
  tty\: TTY Line Configuration

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class LineState(Enum):
    """
    LineState (Enum Class)

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
    SessionOperation (Enum Class)

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
    
    .. attribute:: console_nodes
    
    	List of Nodes for console
    	**type**\:  :py:class:`ConsoleNodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.ConsoleNodes>`
    
    .. attribute:: vty_lines
    
    	List of VTY lines
    	**type**\:  :py:class:`VtyLines <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.VtyLines>`
    
    .. attribute:: auxiliary_nodes
    
    	List of Nodes attached with an auxiliary line
    	**type**\:  :py:class:`AuxiliaryNodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.AuxiliaryNodes>`
    
    

    """

    _prefix = 'tty-server-oper'
    _revision = '2017-09-07'

    def __init__(self):
        super(Tty, self).__init__()
        self._top_entity = None

        self.yang_name = "tty"
        self.yang_parent_name = "Cisco-IOS-XR-tty-server-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("console-nodes", ("console_nodes", Tty.ConsoleNodes)), ("vty-lines", ("vty_lines", Tty.VtyLines)), ("auxiliary-nodes", ("auxiliary_nodes", Tty.AuxiliaryNodes))])
        self._leafs = OrderedDict()

        self.console_nodes = Tty.ConsoleNodes()
        self.console_nodes.parent = self
        self._children_name_map["console_nodes"] = "console-nodes"

        self.vty_lines = Tty.VtyLines()
        self.vty_lines.parent = self
        self._children_name_map["vty_lines"] = "vty-lines"

        self.auxiliary_nodes = Tty.AuxiliaryNodes()
        self.auxiliary_nodes.parent = self
        self._children_name_map["auxiliary_nodes"] = "auxiliary-nodes"
        self._segment_path = lambda: "Cisco-IOS-XR-tty-server-oper:tty"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Tty, [], name, value)


    class ConsoleNodes(Entity):
        """
        List of Nodes for console
        
        .. attribute:: console_node
        
        	Console line configuration on a node
        	**type**\: list of  		 :py:class:`ConsoleNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.ConsoleNodes.ConsoleNode>`
        
        

        """

        _prefix = 'tty-server-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(Tty.ConsoleNodes, self).__init__()

            self.yang_name = "console-nodes"
            self.yang_parent_name = "tty"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("console-node", ("console_node", Tty.ConsoleNodes.ConsoleNode))])
            self._leafs = OrderedDict()

            self.console_node = YList(self)
            self._segment_path = lambda: "console-nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-tty-server-oper:tty/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Tty.ConsoleNodes, [], name, value)


        class ConsoleNode(Entity):
            """
            Console line configuration on a node
            
            .. attribute:: id  (key)
            
            	Node ID
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: console_line
            
            	Console line
            	**type**\:  :py:class:`ConsoleLine <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.ConsoleNodes.ConsoleNode.ConsoleLine>`
            
            

            """

            _prefix = 'tty-server-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(Tty.ConsoleNodes.ConsoleNode, self).__init__()

                self.yang_name = "console-node"
                self.yang_parent_name = "console-nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['id']
                self._child_classes = OrderedDict([("console-line", ("console_line", Tty.ConsoleNodes.ConsoleNode.ConsoleLine))])
                self._leafs = OrderedDict([
                    ('id', (YLeaf(YType.str, 'id'), ['str'])),
                ])
                self.id = None

                self.console_line = Tty.ConsoleNodes.ConsoleNode.ConsoleLine()
                self.console_line.parent = self
                self._children_name_map["console_line"] = "console-line"
                self._segment_path = lambda: "console-node" + "[id='" + str(self.id) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-tty-server-oper:tty/console-nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Tty.ConsoleNodes.ConsoleNode, ['id'], name, value)


            class ConsoleLine(Entity):
                """
                Console line
                
                .. attribute:: console_statistics
                
                	Statistics of the console line
                	**type**\:  :py:class:`ConsoleStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics>`
                
                .. attribute:: state
                
                	Line state information
                	**type**\:  :py:class:`State <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.ConsoleNodes.ConsoleNode.ConsoleLine.State>`
                
                .. attribute:: configuration
                
                	Configuration information of the line
                	**type**\:  :py:class:`Configuration <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.ConsoleNodes.ConsoleNode.ConsoleLine.Configuration>`
                
                

                """

                _prefix = 'tty-server-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Tty.ConsoleNodes.ConsoleNode.ConsoleLine, self).__init__()

                    self.yang_name = "console-line"
                    self.yang_parent_name = "console-node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("console-statistics", ("console_statistics", Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics)), ("state", ("state", Tty.ConsoleNodes.ConsoleNode.ConsoleLine.State)), ("configuration", ("configuration", Tty.ConsoleNodes.ConsoleNode.ConsoleLine.Configuration))])
                    self._leafs = OrderedDict()

                    self.console_statistics = Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics()
                    self.console_statistics.parent = self
                    self._children_name_map["console_statistics"] = "console-statistics"

                    self.state = Tty.ConsoleNodes.ConsoleNode.ConsoleLine.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"

                    self.configuration = Tty.ConsoleNodes.ConsoleNode.ConsoleLine.Configuration()
                    self.configuration.parent = self
                    self._children_name_map["configuration"] = "configuration"
                    self._segment_path = lambda: "console-line"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Tty.ConsoleNodes.ConsoleNode.ConsoleLine, [], name, value)


                class ConsoleStatistics(Entity):
                    """
                    Statistics of the console line
                    
                    .. attribute:: rs232
                    
                    	RS232 statistics of console line
                    	**type**\:  :py:class:`Rs232 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.Rs232>`
                    
                    .. attribute:: general_statistics
                    
                    	General statistics of line
                    	**type**\:  :py:class:`GeneralStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.GeneralStatistics>`
                    
                    .. attribute:: exec_
                    
                    	Exec related statistics
                    	**type**\:  :py:class:`Exec <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.Exec>`
                    
                    .. attribute:: aaa
                    
                    	AAA related statistics
                    	**type**\:  :py:class:`Aaa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.Aaa>`
                    
                    

                    """

                    _prefix = 'tty-server-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics, self).__init__()

                        self.yang_name = "console-statistics"
                        self.yang_parent_name = "console-line"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("rs232", ("rs232", Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.Rs232)), ("general-statistics", ("general_statistics", Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.GeneralStatistics)), ("exec", ("exec_", Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.Exec)), ("aaa", ("aaa", Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.Aaa))])
                        self._leafs = OrderedDict()

                        self.rs232 = Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.Rs232()
                        self.rs232.parent = self
                        self._children_name_map["rs232"] = "rs232"

                        self.general_statistics = Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.GeneralStatistics()
                        self.general_statistics.parent = self
                        self._children_name_map["general_statistics"] = "general-statistics"

                        self.exec_ = Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.Exec()
                        self.exec_.parent = self
                        self._children_name_map["exec_"] = "exec"

                        self.aaa = Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.Aaa()
                        self.aaa.parent = self
                        self._children_name_map["aaa"] = "aaa"
                        self._segment_path = lambda: "console-statistics"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics, [], name, value)


                    class Rs232(Entity):
                        """
                        RS232 statistics of console line
                        
                        .. attribute:: data_bits
                        
                        	Number of databits
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: bit
                        
                        .. attribute:: exec_disabled
                        
                        	Exec disabled on TTY
                        	**type**\: bool
                        
                        .. attribute:: hardware_flow_control_status
                        
                        	Hardware flow control status
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: parity_status
                        
                        	Parity status
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: baud_rate
                        
                        	Inbound/Outbound baud rate in bps
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: bit/s
                        
                        .. attribute:: stop_bits
                        
                        	Number of stopbits
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: bit
                        
                        .. attribute:: overrun_error_count
                        
                        	Overrun error count
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: framing_error_count
                        
                        	Framing error count
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: parity_error_count
                        
                        	Parity error count
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'tty-server-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.Rs232, self).__init__()

                            self.yang_name = "rs232"
                            self.yang_parent_name = "console-statistics"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('data_bits', (YLeaf(YType.uint32, 'data-bits'), ['int'])),
                                ('exec_disabled', (YLeaf(YType.boolean, 'exec-disabled'), ['bool'])),
                                ('hardware_flow_control_status', (YLeaf(YType.uint32, 'hardware-flow-control-status'), ['int'])),
                                ('parity_status', (YLeaf(YType.uint32, 'parity-status'), ['int'])),
                                ('baud_rate', (YLeaf(YType.uint32, 'baud-rate'), ['int'])),
                                ('stop_bits', (YLeaf(YType.uint32, 'stop-bits'), ['int'])),
                                ('overrun_error_count', (YLeaf(YType.uint32, 'overrun-error-count'), ['int'])),
                                ('framing_error_count', (YLeaf(YType.uint32, 'framing-error-count'), ['int'])),
                                ('parity_error_count', (YLeaf(YType.uint32, 'parity-error-count'), ['int'])),
                            ])
                            self.data_bits = None
                            self.exec_disabled = None
                            self.hardware_flow_control_status = None
                            self.parity_status = None
                            self.baud_rate = None
                            self.stop_bits = None
                            self.overrun_error_count = None
                            self.framing_error_count = None
                            self.parity_error_count = None
                            self._segment_path = lambda: "rs232"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.Rs232, [u'data_bits', u'exec_disabled', u'hardware_flow_control_status', u'parity_status', u'baud_rate', u'stop_bits', u'overrun_error_count', u'framing_error_count', u'parity_error_count'], name, value)


                    class GeneralStatistics(Entity):
                        """
                        General statistics of line
                        
                        .. attribute:: terminal_length
                        
                        	Terminal length
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: terminal_width
                        
                        	Line width
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: async_interface
                        
                        	Usable as async interface
                        	**type**\: bool
                        
                        .. attribute:: flow_control_start_character
                        
                        	Software flow control start char
                        	**type**\: int
                        
                        	**range:** \-128..127
                        
                        .. attribute:: flow_control_stop_character
                        
                        	Software flow control stop char
                        	**type**\: int
                        
                        	**range:** \-128..127
                        
                        .. attribute:: domain_lookup_enabled
                        
                        	DNS resolution enabled
                        	**type**\: bool
                        
                        .. attribute:: motd_banner_enabled
                        
                        	MOTD banner enabled
                        	**type**\: bool
                        
                        .. attribute:: private_flag
                        
                        	TTY private flag
                        	**type**\: bool
                        
                        .. attribute:: terminal_type
                        
                        	Terminal type
                        	**type**\: str
                        
                        .. attribute:: absolute_timeout
                        
                        	Absolute timeout period
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: idle_time
                        
                        	TTY idle time
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'tty-server-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.GeneralStatistics, self).__init__()

                            self.yang_name = "general-statistics"
                            self.yang_parent_name = "console-statistics"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('terminal_length', (YLeaf(YType.uint32, 'terminal-length'), ['int'])),
                                ('terminal_width', (YLeaf(YType.uint32, 'terminal-width'), ['int'])),
                                ('async_interface', (YLeaf(YType.boolean, 'async-interface'), ['bool'])),
                                ('flow_control_start_character', (YLeaf(YType.int8, 'flow-control-start-character'), ['int'])),
                                ('flow_control_stop_character', (YLeaf(YType.int8, 'flow-control-stop-character'), ['int'])),
                                ('domain_lookup_enabled', (YLeaf(YType.boolean, 'domain-lookup-enabled'), ['bool'])),
                                ('motd_banner_enabled', (YLeaf(YType.boolean, 'motd-banner-enabled'), ['bool'])),
                                ('private_flag', (YLeaf(YType.boolean, 'private-flag'), ['bool'])),
                                ('terminal_type', (YLeaf(YType.str, 'terminal-type'), ['str'])),
                                ('absolute_timeout', (YLeaf(YType.uint32, 'absolute-timeout'), ['int'])),
                                ('idle_time', (YLeaf(YType.uint32, 'idle-time'), ['int'])),
                            ])
                            self.terminal_length = None
                            self.terminal_width = None
                            self.async_interface = None
                            self.flow_control_start_character = None
                            self.flow_control_stop_character = None
                            self.domain_lookup_enabled = None
                            self.motd_banner_enabled = None
                            self.private_flag = None
                            self.terminal_type = None
                            self.absolute_timeout = None
                            self.idle_time = None
                            self._segment_path = lambda: "general-statistics"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.GeneralStatistics, ['terminal_length', 'terminal_width', 'async_interface', 'flow_control_start_character', 'flow_control_stop_character', 'domain_lookup_enabled', 'motd_banner_enabled', 'private_flag', 'terminal_type', 'absolute_timeout', 'idle_time'], name, value)


                    class Exec(Entity):
                        """
                        Exec related statistics
                        
                        .. attribute:: time_stamp_enabled
                        
                        	Specifies whether timestamp is enabled or not
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'tty-server-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.Exec, self).__init__()

                            self.yang_name = "exec"
                            self.yang_parent_name = "console-statistics"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('time_stamp_enabled', (YLeaf(YType.boolean, 'time-stamp-enabled'), ['bool'])),
                            ])
                            self.time_stamp_enabled = None
                            self._segment_path = lambda: "exec"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.Exec, [u'time_stamp_enabled'], name, value)


                    class Aaa(Entity):
                        """
                        AAA related statistics
                        
                        .. attribute:: user_name
                        
                        	The authenticated username
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'tty-server-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.Aaa, self).__init__()

                            self.yang_name = "aaa"
                            self.yang_parent_name = "console-statistics"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('user_name', (YLeaf(YType.str, 'user-name'), ['str'])),
                            ])
                            self.user_name = None
                            self._segment_path = lambda: "aaa"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.Aaa, [u'user_name'], name, value)


                class State(Entity):
                    """
                    Line state information
                    
                    .. attribute:: template
                    
                    	Information related to template applied to the line
                    	**type**\:  :py:class:`Template <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.ConsoleNodes.ConsoleNode.ConsoleLine.State.Template>`
                    
                    .. attribute:: general
                    
                    	General information
                    	**type**\:  :py:class:`General <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.ConsoleNodes.ConsoleNode.ConsoleLine.State.General>`
                    
                    

                    """

                    _prefix = 'tty-server-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Tty.ConsoleNodes.ConsoleNode.ConsoleLine.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "console-line"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("template", ("template", Tty.ConsoleNodes.ConsoleNode.ConsoleLine.State.Template)), ("general", ("general", Tty.ConsoleNodes.ConsoleNode.ConsoleLine.State.General))])
                        self._leafs = OrderedDict()

                        self.template = Tty.ConsoleNodes.ConsoleNode.ConsoleLine.State.Template()
                        self.template.parent = self
                        self._children_name_map["template"] = "template"

                        self.general = Tty.ConsoleNodes.ConsoleNode.ConsoleLine.State.General()
                        self.general.parent = self
                        self._children_name_map["general"] = "general"
                        self._segment_path = lambda: "state"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Tty.ConsoleNodes.ConsoleNode.ConsoleLine.State, [], name, value)


                    class Template(Entity):
                        """
                        Information related to template applied to the
                        line
                        
                        .. attribute:: name
                        
                        	Name of the template
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'tty-server-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(Tty.ConsoleNodes.ConsoleNode.ConsoleLine.State.Template, self).__init__()

                            self.yang_name = "template"
                            self.yang_parent_name = "state"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                            ])
                            self.name = None
                            self._segment_path = lambda: "template"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Tty.ConsoleNodes.ConsoleNode.ConsoleLine.State.Template, ['name'], name, value)


                    class General(Entity):
                        """
                        General information
                        
                        .. attribute:: operation_
                        
                        	application running of on the tty line
                        	**type**\:  :py:class:`SessionOperation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.SessionOperation>`
                        
                        .. attribute:: general_state
                        
                        	State of the line
                        	**type**\:  :py:class:`LineState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.LineState>`
                        
                        

                        """

                        _prefix = 'tty-server-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(Tty.ConsoleNodes.ConsoleNode.ConsoleLine.State.General, self).__init__()

                            self.yang_name = "general"
                            self.yang_parent_name = "state"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('operation_', (YLeaf(YType.enumeration, 'operation'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper', 'SessionOperation', '')])),
                                ('general_state', (YLeaf(YType.enumeration, 'general-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper', 'LineState', '')])),
                            ])
                            self.operation_ = None
                            self.general_state = None
                            self._segment_path = lambda: "general"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Tty.ConsoleNodes.ConsoleNode.ConsoleLine.State.General, ['operation_', 'general_state'], name, value)


                class Configuration(Entity):
                    """
                    Configuration information of the line
                    
                    .. attribute:: connection_configuration
                    
                    	Conection configuration information
                    	**type**\:  :py:class:`ConnectionConfiguration <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.ConsoleNodes.ConsoleNode.ConsoleLine.Configuration.ConnectionConfiguration>`
                    
                    

                    """

                    _prefix = 'tty-server-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Tty.ConsoleNodes.ConsoleNode.ConsoleLine.Configuration, self).__init__()

                        self.yang_name = "configuration"
                        self.yang_parent_name = "console-line"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("connection-configuration", ("connection_configuration", Tty.ConsoleNodes.ConsoleNode.ConsoleLine.Configuration.ConnectionConfiguration))])
                        self._leafs = OrderedDict()

                        self.connection_configuration = Tty.ConsoleNodes.ConsoleNode.ConsoleLine.Configuration.ConnectionConfiguration()
                        self.connection_configuration.parent = self
                        self._children_name_map["connection_configuration"] = "connection-configuration"
                        self._segment_path = lambda: "configuration"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Tty.ConsoleNodes.ConsoleNode.ConsoleLine.Configuration, [], name, value)


                    class ConnectionConfiguration(Entity):
                        """
                        Conection configuration information
                        
                        .. attribute:: transport_input
                        
                        	Protocols to use when connecting to the terminal server
                        	**type**\:  :py:class:`TransportInput <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.ConsoleNodes.ConsoleNode.ConsoleLine.Configuration.ConnectionConfiguration.TransportInput>`
                        
                        .. attribute:: acl_out
                        
                        	ACL for outbound traffic
                        	**type**\: str
                        
                        .. attribute:: acl_in
                        
                        	ACL for inbound traffic
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'tty-server-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(Tty.ConsoleNodes.ConsoleNode.ConsoleLine.Configuration.ConnectionConfiguration, self).__init__()

                            self.yang_name = "connection-configuration"
                            self.yang_parent_name = "configuration"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("transport-input", ("transport_input", Tty.ConsoleNodes.ConsoleNode.ConsoleLine.Configuration.ConnectionConfiguration.TransportInput))])
                            self._leafs = OrderedDict([
                                ('acl_out', (YLeaf(YType.str, 'acl-out'), ['str'])),
                                ('acl_in', (YLeaf(YType.str, 'acl-in'), ['str'])),
                            ])
                            self.acl_out = None
                            self.acl_in = None

                            self.transport_input = Tty.ConsoleNodes.ConsoleNode.ConsoleLine.Configuration.ConnectionConfiguration.TransportInput()
                            self.transport_input.parent = self
                            self._children_name_map["transport_input"] = "transport-input"
                            self._segment_path = lambda: "connection-configuration"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Tty.ConsoleNodes.ConsoleNode.ConsoleLine.Configuration.ConnectionConfiguration, ['acl_out', 'acl_in'], name, value)


                        class TransportInput(Entity):
                            """
                            Protocols to use when connecting to the
                            terminal server
                            
                            .. attribute:: select
                            
                            	Choose transport protocols
                            	**type**\:  :py:class:`TtyTransportProtocolSelect <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes.TtyTransportProtocolSelect>`
                            
                            	**default value**\: all
                            
                            .. attribute:: protocol1
                            
                            	Transport protocol1
                            	**type**\:  :py:class:`TtyTransportProtocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes.TtyTransportProtocol>`
                            
                            .. attribute:: protocol2
                            
                            	Transport protocol2
                            	**type**\:  :py:class:`TtyTransportProtocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes.TtyTransportProtocol>`
                            
                            .. attribute:: none
                            
                            	Not used
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'tty-server-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(Tty.ConsoleNodes.ConsoleNode.ConsoleLine.Configuration.ConnectionConfiguration.TransportInput, self).__init__()

                                self.yang_name = "transport-input"
                                self.yang_parent_name = "connection-configuration"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('select', (YLeaf(YType.enumeration, 'select'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes', 'TtyTransportProtocolSelect', '')])),
                                    ('protocol1', (YLeaf(YType.enumeration, 'protocol1'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes', 'TtyTransportProtocol', '')])),
                                    ('protocol2', (YLeaf(YType.enumeration, 'protocol2'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes', 'TtyTransportProtocol', '')])),
                                    ('none', (YLeaf(YType.uint32, 'none'), ['int'])),
                                ])
                                self.select = None
                                self.protocol1 = None
                                self.protocol2 = None
                                self.none = None
                                self._segment_path = lambda: "transport-input"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Tty.ConsoleNodes.ConsoleNode.ConsoleLine.Configuration.ConnectionConfiguration.TransportInput, ['select', 'protocol1', 'protocol2', 'none'], name, value)


    class VtyLines(Entity):
        """
        List of VTY lines
        
        .. attribute:: vty_line
        
        	VTY Line
        	**type**\: list of  		 :py:class:`VtyLine <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.VtyLines.VtyLine>`
        
        

        """

        _prefix = 'tty-server-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(Tty.VtyLines, self).__init__()

            self.yang_name = "vty-lines"
            self.yang_parent_name = "tty"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("vty-line", ("vty_line", Tty.VtyLines.VtyLine))])
            self._leafs = OrderedDict()

            self.vty_line = YList(self)
            self._segment_path = lambda: "vty-lines"
            self._absolute_path = lambda: "Cisco-IOS-XR-tty-server-oper:tty/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Tty.VtyLines, [], name, value)


        class VtyLine(Entity):
            """
            VTY Line
            
            .. attribute:: line_number  (key)
            
            	VTY Line number
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: vty_statistics
            
            	Statistics of the VTY line
            	**type**\:  :py:class:`VtyStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.VtyLines.VtyLine.VtyStatistics>`
            
            .. attribute:: state
            
            	Line state information
            	**type**\:  :py:class:`State <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.VtyLines.VtyLine.State>`
            
            .. attribute:: configuration
            
            	Configuration information of the line
            	**type**\:  :py:class:`Configuration <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.VtyLines.VtyLine.Configuration>`
            
            .. attribute:: sessions
            
            	Outgoing sessions
            	**type**\:  :py:class:`Sessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.VtyLines.VtyLine.Sessions>`
            
            

            """

            _prefix = 'tty-server-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(Tty.VtyLines.VtyLine, self).__init__()

                self.yang_name = "vty-line"
                self.yang_parent_name = "vty-lines"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['line_number']
                self._child_classes = OrderedDict([("vty-statistics", ("vty_statistics", Tty.VtyLines.VtyLine.VtyStatistics)), ("state", ("state", Tty.VtyLines.VtyLine.State)), ("configuration", ("configuration", Tty.VtyLines.VtyLine.Configuration)), ("Cisco-IOS-XR-tty-management-oper:sessions", ("sessions", Tty.VtyLines.VtyLine.Sessions))])
                self._leafs = OrderedDict([
                    ('line_number', (YLeaf(YType.uint32, 'line-number'), ['int'])),
                ])
                self.line_number = None

                self.vty_statistics = Tty.VtyLines.VtyLine.VtyStatistics()
                self.vty_statistics.parent = self
                self._children_name_map["vty_statistics"] = "vty-statistics"

                self.state = Tty.VtyLines.VtyLine.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"

                self.configuration = Tty.VtyLines.VtyLine.Configuration()
                self.configuration.parent = self
                self._children_name_map["configuration"] = "configuration"

                self.sessions = Tty.VtyLines.VtyLine.Sessions()
                self.sessions.parent = self
                self._children_name_map["sessions"] = "Cisco-IOS-XR-tty-management-oper:sessions"
                self._segment_path = lambda: "vty-line" + "[line-number='" + str(self.line_number) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-tty-server-oper:tty/vty-lines/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Tty.VtyLines.VtyLine, ['line_number'], name, value)


            class VtyStatistics(Entity):
                """
                Statistics of the VTY line
                
                .. attribute:: connection
                
                	Connection related statistics
                	**type**\:  :py:class:`Connection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.VtyLines.VtyLine.VtyStatistics.Connection>`
                
                .. attribute:: general_statistics
                
                	General statistics of line
                	**type**\:  :py:class:`GeneralStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.VtyLines.VtyLine.VtyStatistics.GeneralStatistics>`
                
                .. attribute:: exec_
                
                	Exec related statistics
                	**type**\:  :py:class:`Exec <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.VtyLines.VtyLine.VtyStatistics.Exec>`
                
                .. attribute:: aaa
                
                	AAA related statistics
                	**type**\:  :py:class:`Aaa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.VtyLines.VtyLine.VtyStatistics.Aaa>`
                
                

                """

                _prefix = 'tty-server-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Tty.VtyLines.VtyLine.VtyStatistics, self).__init__()

                    self.yang_name = "vty-statistics"
                    self.yang_parent_name = "vty-line"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("connection", ("connection", Tty.VtyLines.VtyLine.VtyStatistics.Connection)), ("general-statistics", ("general_statistics", Tty.VtyLines.VtyLine.VtyStatistics.GeneralStatistics)), ("exec", ("exec_", Tty.VtyLines.VtyLine.VtyStatistics.Exec)), ("aaa", ("aaa", Tty.VtyLines.VtyLine.VtyStatistics.Aaa))])
                    self._leafs = OrderedDict()

                    self.connection = Tty.VtyLines.VtyLine.VtyStatistics.Connection()
                    self.connection.parent = self
                    self._children_name_map["connection"] = "connection"

                    self.general_statistics = Tty.VtyLines.VtyLine.VtyStatistics.GeneralStatistics()
                    self.general_statistics.parent = self
                    self._children_name_map["general_statistics"] = "general-statistics"

                    self.exec_ = Tty.VtyLines.VtyLine.VtyStatistics.Exec()
                    self.exec_.parent = self
                    self._children_name_map["exec_"] = "exec"

                    self.aaa = Tty.VtyLines.VtyLine.VtyStatistics.Aaa()
                    self.aaa.parent = self
                    self._children_name_map["aaa"] = "aaa"
                    self._segment_path = lambda: "vty-statistics"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Tty.VtyLines.VtyLine.VtyStatistics, [], name, value)


                class Connection(Entity):
                    """
                    Connection related statistics
                    
                    .. attribute:: incoming_host_address
                    
                    	Incoming host address(max)
                    	**type**\: str
                    
                    	**length:** 0..46
                    
                    .. attribute:: host_address_family
                    
                    	Incoming host address family
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: service
                    
                    	Input transport
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'tty-server-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Tty.VtyLines.VtyLine.VtyStatistics.Connection, self).__init__()

                        self.yang_name = "connection"
                        self.yang_parent_name = "vty-statistics"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('incoming_host_address', (YLeaf(YType.str, 'incoming-host-address'), ['str'])),
                            ('host_address_family', (YLeaf(YType.uint32, 'host-address-family'), ['int'])),
                            ('service', (YLeaf(YType.uint32, 'service'), ['int'])),
                        ])
                        self.incoming_host_address = None
                        self.host_address_family = None
                        self.service = None
                        self._segment_path = lambda: "connection"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Tty.VtyLines.VtyLine.VtyStatistics.Connection, [u'incoming_host_address', u'host_address_family', u'service'], name, value)


                class GeneralStatistics(Entity):
                    """
                    General statistics of line
                    
                    .. attribute:: terminal_length
                    
                    	Terminal length
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: terminal_width
                    
                    	Line width
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: async_interface
                    
                    	Usable as async interface
                    	**type**\: bool
                    
                    .. attribute:: flow_control_start_character
                    
                    	Software flow control start char
                    	**type**\: int
                    
                    	**range:** \-128..127
                    
                    .. attribute:: flow_control_stop_character
                    
                    	Software flow control stop char
                    	**type**\: int
                    
                    	**range:** \-128..127
                    
                    .. attribute:: domain_lookup_enabled
                    
                    	DNS resolution enabled
                    	**type**\: bool
                    
                    .. attribute:: motd_banner_enabled
                    
                    	MOTD banner enabled
                    	**type**\: bool
                    
                    .. attribute:: private_flag
                    
                    	TTY private flag
                    	**type**\: bool
                    
                    .. attribute:: terminal_type
                    
                    	Terminal type
                    	**type**\: str
                    
                    .. attribute:: absolute_timeout
                    
                    	Absolute timeout period
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: idle_time
                    
                    	TTY idle time
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'tty-server-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Tty.VtyLines.VtyLine.VtyStatistics.GeneralStatistics, self).__init__()

                        self.yang_name = "general-statistics"
                        self.yang_parent_name = "vty-statistics"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('terminal_length', (YLeaf(YType.uint32, 'terminal-length'), ['int'])),
                            ('terminal_width', (YLeaf(YType.uint32, 'terminal-width'), ['int'])),
                            ('async_interface', (YLeaf(YType.boolean, 'async-interface'), ['bool'])),
                            ('flow_control_start_character', (YLeaf(YType.int8, 'flow-control-start-character'), ['int'])),
                            ('flow_control_stop_character', (YLeaf(YType.int8, 'flow-control-stop-character'), ['int'])),
                            ('domain_lookup_enabled', (YLeaf(YType.boolean, 'domain-lookup-enabled'), ['bool'])),
                            ('motd_banner_enabled', (YLeaf(YType.boolean, 'motd-banner-enabled'), ['bool'])),
                            ('private_flag', (YLeaf(YType.boolean, 'private-flag'), ['bool'])),
                            ('terminal_type', (YLeaf(YType.str, 'terminal-type'), ['str'])),
                            ('absolute_timeout', (YLeaf(YType.uint32, 'absolute-timeout'), ['int'])),
                            ('idle_time', (YLeaf(YType.uint32, 'idle-time'), ['int'])),
                        ])
                        self.terminal_length = None
                        self.terminal_width = None
                        self.async_interface = None
                        self.flow_control_start_character = None
                        self.flow_control_stop_character = None
                        self.domain_lookup_enabled = None
                        self.motd_banner_enabled = None
                        self.private_flag = None
                        self.terminal_type = None
                        self.absolute_timeout = None
                        self.idle_time = None
                        self._segment_path = lambda: "general-statistics"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Tty.VtyLines.VtyLine.VtyStatistics.GeneralStatistics, ['terminal_length', 'terminal_width', 'async_interface', 'flow_control_start_character', 'flow_control_stop_character', 'domain_lookup_enabled', 'motd_banner_enabled', 'private_flag', 'terminal_type', 'absolute_timeout', 'idle_time'], name, value)


                class Exec(Entity):
                    """
                    Exec related statistics
                    
                    .. attribute:: time_stamp_enabled
                    
                    	Specifies whether timestamp is enabled or not
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'tty-server-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Tty.VtyLines.VtyLine.VtyStatistics.Exec, self).__init__()

                        self.yang_name = "exec"
                        self.yang_parent_name = "vty-statistics"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('time_stamp_enabled', (YLeaf(YType.boolean, 'time-stamp-enabled'), ['bool'])),
                        ])
                        self.time_stamp_enabled = None
                        self._segment_path = lambda: "exec"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Tty.VtyLines.VtyLine.VtyStatistics.Exec, [u'time_stamp_enabled'], name, value)


                class Aaa(Entity):
                    """
                    AAA related statistics
                    
                    .. attribute:: user_name
                    
                    	The authenticated username
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'tty-server-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Tty.VtyLines.VtyLine.VtyStatistics.Aaa, self).__init__()

                        self.yang_name = "aaa"
                        self.yang_parent_name = "vty-statistics"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('user_name', (YLeaf(YType.str, 'user-name'), ['str'])),
                        ])
                        self.user_name = None
                        self._segment_path = lambda: "aaa"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Tty.VtyLines.VtyLine.VtyStatistics.Aaa, [u'user_name'], name, value)


            class State(Entity):
                """
                Line state information
                
                .. attribute:: template
                
                	Information related to template applied to the line
                	**type**\:  :py:class:`Template <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.VtyLines.VtyLine.State.Template>`
                
                .. attribute:: general
                
                	General information
                	**type**\:  :py:class:`General <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.VtyLines.VtyLine.State.General>`
                
                

                """

                _prefix = 'tty-server-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Tty.VtyLines.VtyLine.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "vty-line"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("template", ("template", Tty.VtyLines.VtyLine.State.Template)), ("general", ("general", Tty.VtyLines.VtyLine.State.General))])
                    self._leafs = OrderedDict()

                    self.template = Tty.VtyLines.VtyLine.State.Template()
                    self.template.parent = self
                    self._children_name_map["template"] = "template"

                    self.general = Tty.VtyLines.VtyLine.State.General()
                    self.general.parent = self
                    self._children_name_map["general"] = "general"
                    self._segment_path = lambda: "state"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Tty.VtyLines.VtyLine.State, [], name, value)


                class Template(Entity):
                    """
                    Information related to template applied to the
                    line
                    
                    .. attribute:: name
                    
                    	Name of the template
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'tty-server-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Tty.VtyLines.VtyLine.State.Template, self).__init__()

                        self.yang_name = "template"
                        self.yang_parent_name = "state"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                        ])
                        self.name = None
                        self._segment_path = lambda: "template"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Tty.VtyLines.VtyLine.State.Template, ['name'], name, value)


                class General(Entity):
                    """
                    General information
                    
                    .. attribute:: operation_
                    
                    	application running of on the tty line
                    	**type**\:  :py:class:`SessionOperation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.SessionOperation>`
                    
                    .. attribute:: general_state
                    
                    	State of the line
                    	**type**\:  :py:class:`LineState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.LineState>`
                    
                    

                    """

                    _prefix = 'tty-server-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Tty.VtyLines.VtyLine.State.General, self).__init__()

                        self.yang_name = "general"
                        self.yang_parent_name = "state"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('operation_', (YLeaf(YType.enumeration, 'operation'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper', 'SessionOperation', '')])),
                            ('general_state', (YLeaf(YType.enumeration, 'general-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper', 'LineState', '')])),
                        ])
                        self.operation_ = None
                        self.general_state = None
                        self._segment_path = lambda: "general"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Tty.VtyLines.VtyLine.State.General, ['operation_', 'general_state'], name, value)


            class Configuration(Entity):
                """
                Configuration information of the line
                
                .. attribute:: connection_configuration
                
                	Conection configuration information
                	**type**\:  :py:class:`ConnectionConfiguration <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.VtyLines.VtyLine.Configuration.ConnectionConfiguration>`
                
                

                """

                _prefix = 'tty-server-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Tty.VtyLines.VtyLine.Configuration, self).__init__()

                    self.yang_name = "configuration"
                    self.yang_parent_name = "vty-line"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("connection-configuration", ("connection_configuration", Tty.VtyLines.VtyLine.Configuration.ConnectionConfiguration))])
                    self._leafs = OrderedDict()

                    self.connection_configuration = Tty.VtyLines.VtyLine.Configuration.ConnectionConfiguration()
                    self.connection_configuration.parent = self
                    self._children_name_map["connection_configuration"] = "connection-configuration"
                    self._segment_path = lambda: "configuration"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Tty.VtyLines.VtyLine.Configuration, [], name, value)


                class ConnectionConfiguration(Entity):
                    """
                    Conection configuration information
                    
                    .. attribute:: transport_input
                    
                    	Protocols to use when connecting to the terminal server
                    	**type**\:  :py:class:`TransportInput <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.VtyLines.VtyLine.Configuration.ConnectionConfiguration.TransportInput>`
                    
                    .. attribute:: acl_out
                    
                    	ACL for outbound traffic
                    	**type**\: str
                    
                    .. attribute:: acl_in
                    
                    	ACL for inbound traffic
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'tty-server-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Tty.VtyLines.VtyLine.Configuration.ConnectionConfiguration, self).__init__()

                        self.yang_name = "connection-configuration"
                        self.yang_parent_name = "configuration"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("transport-input", ("transport_input", Tty.VtyLines.VtyLine.Configuration.ConnectionConfiguration.TransportInput))])
                        self._leafs = OrderedDict([
                            ('acl_out', (YLeaf(YType.str, 'acl-out'), ['str'])),
                            ('acl_in', (YLeaf(YType.str, 'acl-in'), ['str'])),
                        ])
                        self.acl_out = None
                        self.acl_in = None

                        self.transport_input = Tty.VtyLines.VtyLine.Configuration.ConnectionConfiguration.TransportInput()
                        self.transport_input.parent = self
                        self._children_name_map["transport_input"] = "transport-input"
                        self._segment_path = lambda: "connection-configuration"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Tty.VtyLines.VtyLine.Configuration.ConnectionConfiguration, ['acl_out', 'acl_in'], name, value)


                    class TransportInput(Entity):
                        """
                        Protocols to use when connecting to the
                        terminal server
                        
                        .. attribute:: select
                        
                        	Choose transport protocols
                        	**type**\:  :py:class:`TtyTransportProtocolSelect <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes.TtyTransportProtocolSelect>`
                        
                        	**default value**\: all
                        
                        .. attribute:: protocol1
                        
                        	Transport protocol1
                        	**type**\:  :py:class:`TtyTransportProtocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes.TtyTransportProtocol>`
                        
                        .. attribute:: protocol2
                        
                        	Transport protocol2
                        	**type**\:  :py:class:`TtyTransportProtocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes.TtyTransportProtocol>`
                        
                        .. attribute:: none
                        
                        	Not used
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'tty-server-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(Tty.VtyLines.VtyLine.Configuration.ConnectionConfiguration.TransportInput, self).__init__()

                            self.yang_name = "transport-input"
                            self.yang_parent_name = "connection-configuration"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('select', (YLeaf(YType.enumeration, 'select'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes', 'TtyTransportProtocolSelect', '')])),
                                ('protocol1', (YLeaf(YType.enumeration, 'protocol1'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes', 'TtyTransportProtocol', '')])),
                                ('protocol2', (YLeaf(YType.enumeration, 'protocol2'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes', 'TtyTransportProtocol', '')])),
                                ('none', (YLeaf(YType.uint32, 'none'), ['int'])),
                            ])
                            self.select = None
                            self.protocol1 = None
                            self.protocol2 = None
                            self.none = None
                            self._segment_path = lambda: "transport-input"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Tty.VtyLines.VtyLine.Configuration.ConnectionConfiguration.TransportInput, ['select', 'protocol1', 'protocol2', 'none'], name, value)


            class Sessions(Entity):
                """
                Outgoing sessions
                
                .. attribute:: outgoing_connection
                
                	List of outgoing sessions
                	**type**\: list of  		 :py:class:`OutgoingConnection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.VtyLines.VtyLine.Sessions.OutgoingConnection>`
                
                

                """

                _prefix = 'tty-management-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Tty.VtyLines.VtyLine.Sessions, self).__init__()

                    self.yang_name = "sessions"
                    self.yang_parent_name = "vty-line"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("outgoing-connection", ("outgoing_connection", Tty.VtyLines.VtyLine.Sessions.OutgoingConnection))])
                    self._leafs = OrderedDict()

                    self.outgoing_connection = YList(self)
                    self._segment_path = lambda: "Cisco-IOS-XR-tty-management-oper:sessions"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Tty.VtyLines.VtyLine.Sessions, [], name, value)


                class OutgoingConnection(Entity):
                    """
                    List of outgoing sessions
                    
                    .. attribute:: host_address
                    
                    	Host address
                    	**type**\:  :py:class:`HostAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.VtyLines.VtyLine.Sessions.OutgoingConnection.HostAddress>`
                    
                    .. attribute:: connection_id
                    
                    	Connection ID [1\-20]
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: host_name
                    
                    	Host name
                    	**type**\: str
                    
                    .. attribute:: transport_protocol
                    
                    	Session transport protocol
                    	**type**\:  :py:class:`TransportService <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_oper.TransportService>`
                    
                    .. attribute:: is_last_active_session
                    
                    	True indicates last active session
                    	**type**\: bool
                    
                    .. attribute:: idle_time
                    
                    	Elapsed time since session was suspended (in seconds)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    

                    """

                    _prefix = 'tty-management-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Tty.VtyLines.VtyLine.Sessions.OutgoingConnection, self).__init__()

                        self.yang_name = "outgoing-connection"
                        self.yang_parent_name = "sessions"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("host-address", ("host_address", Tty.VtyLines.VtyLine.Sessions.OutgoingConnection.HostAddress))])
                        self._leafs = OrderedDict([
                            ('connection_id', (YLeaf(YType.uint8, 'connection-id'), ['int'])),
                            ('host_name', (YLeaf(YType.str, 'host-name'), ['str'])),
                            ('transport_protocol', (YLeaf(YType.enumeration, 'transport-protocol'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_oper', 'TransportService', '')])),
                            ('is_last_active_session', (YLeaf(YType.boolean, 'is-last-active-session'), ['bool'])),
                            ('idle_time', (YLeaf(YType.uint32, 'idle-time'), ['int'])),
                        ])
                        self.connection_id = None
                        self.host_name = None
                        self.transport_protocol = None
                        self.is_last_active_session = None
                        self.idle_time = None

                        self.host_address = Tty.VtyLines.VtyLine.Sessions.OutgoingConnection.HostAddress()
                        self.host_address.parent = self
                        self._children_name_map["host_address"] = "host-address"
                        self._segment_path = lambda: "outgoing-connection"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Tty.VtyLines.VtyLine.Sessions.OutgoingConnection, ['connection_id', 'host_name', 'transport_protocol', 'is_last_active_session', 'idle_time'], name, value)


                    class HostAddress(Entity):
                        """
                        Host address
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\:  :py:class:`HostAfIdBase <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_oper.HostAfIdBase>`
                        
                        .. attribute:: ipv4_address
                        
                        	IPv4 address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6_address
                        
                        	IPv6 address
                        	**type**\: str
                        
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
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('af_name', (YLeaf(YType.identityref, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_oper', 'HostAfIdBase')])),
                                ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                            ])
                            self.af_name = None
                            self.ipv4_address = None
                            self.ipv6_address = None
                            self._segment_path = lambda: "host-address"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Tty.VtyLines.VtyLine.Sessions.OutgoingConnection.HostAddress, ['af_name', 'ipv4_address', 'ipv6_address'], name, value)


    class AuxiliaryNodes(Entity):
        """
        List of Nodes attached with an auxiliary line
        
        .. attribute:: auxiliary_node
        
        	Line configuration on a node
        	**type**\: list of  		 :py:class:`AuxiliaryNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.AuxiliaryNodes.AuxiliaryNode>`
        
        

        """

        _prefix = 'tty-server-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(Tty.AuxiliaryNodes, self).__init__()

            self.yang_name = "auxiliary-nodes"
            self.yang_parent_name = "tty"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("auxiliary-node", ("auxiliary_node", Tty.AuxiliaryNodes.AuxiliaryNode))])
            self._leafs = OrderedDict()

            self.auxiliary_node = YList(self)
            self._segment_path = lambda: "auxiliary-nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-tty-server-oper:tty/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Tty.AuxiliaryNodes, [], name, value)


        class AuxiliaryNode(Entity):
            """
            Line configuration on a node
            
            .. attribute:: id  (key)
            
            	Node ID
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: auxiliary_line
            
            	Auxiliary line
            	**type**\:  :py:class:`AuxiliaryLine <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine>`
            
            

            """

            _prefix = 'tty-server-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(Tty.AuxiliaryNodes.AuxiliaryNode, self).__init__()

                self.yang_name = "auxiliary-node"
                self.yang_parent_name = "auxiliary-nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['id']
                self._child_classes = OrderedDict([("auxiliary-line", ("auxiliary_line", Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine))])
                self._leafs = OrderedDict([
                    ('id', (YLeaf(YType.str, 'id'), ['str'])),
                ])
                self.id = None

                self.auxiliary_line = Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine()
                self.auxiliary_line.parent = self
                self._children_name_map["auxiliary_line"] = "auxiliary-line"
                self._segment_path = lambda: "auxiliary-node" + "[id='" + str(self.id) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-tty-server-oper:tty/auxiliary-nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Tty.AuxiliaryNodes.AuxiliaryNode, ['id'], name, value)


            class AuxiliaryLine(Entity):
                """
                Auxiliary line
                
                .. attribute:: auxiliary_statistics
                
                	Statistics of the auxiliary line
                	**type**\:  :py:class:`AuxiliaryStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics>`
                
                .. attribute:: state
                
                	Line state information
                	**type**\:  :py:class:`State <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.State>`
                
                .. attribute:: configuration
                
                	Configuration information of the line
                	**type**\:  :py:class:`Configuration <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.Configuration>`
                
                

                """

                _prefix = 'tty-server-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine, self).__init__()

                    self.yang_name = "auxiliary-line"
                    self.yang_parent_name = "auxiliary-node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("auxiliary-statistics", ("auxiliary_statistics", Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics)), ("state", ("state", Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.State)), ("configuration", ("configuration", Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.Configuration))])
                    self._leafs = OrderedDict()

                    self.auxiliary_statistics = Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics()
                    self.auxiliary_statistics.parent = self
                    self._children_name_map["auxiliary_statistics"] = "auxiliary-statistics"

                    self.state = Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"

                    self.configuration = Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.Configuration()
                    self.configuration.parent = self
                    self._children_name_map["configuration"] = "configuration"
                    self._segment_path = lambda: "auxiliary-line"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine, [], name, value)


                class AuxiliaryStatistics(Entity):
                    """
                    Statistics of the auxiliary line
                    
                    .. attribute:: rs232
                    
                    	RS232 statistics of console line
                    	**type**\:  :py:class:`Rs232 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.Rs232>`
                    
                    .. attribute:: general_statistics
                    
                    	General statistics of line
                    	**type**\:  :py:class:`GeneralStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.GeneralStatistics>`
                    
                    .. attribute:: exec_
                    
                    	Exec related statistics
                    	**type**\:  :py:class:`Exec <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.Exec>`
                    
                    .. attribute:: aaa
                    
                    	AAA related statistics
                    	**type**\:  :py:class:`Aaa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.Aaa>`
                    
                    

                    """

                    _prefix = 'tty-server-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics, self).__init__()

                        self.yang_name = "auxiliary-statistics"
                        self.yang_parent_name = "auxiliary-line"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("rs232", ("rs232", Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.Rs232)), ("general-statistics", ("general_statistics", Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.GeneralStatistics)), ("exec", ("exec_", Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.Exec)), ("aaa", ("aaa", Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.Aaa))])
                        self._leafs = OrderedDict()

                        self.rs232 = Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.Rs232()
                        self.rs232.parent = self
                        self._children_name_map["rs232"] = "rs232"

                        self.general_statistics = Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.GeneralStatistics()
                        self.general_statistics.parent = self
                        self._children_name_map["general_statistics"] = "general-statistics"

                        self.exec_ = Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.Exec()
                        self.exec_.parent = self
                        self._children_name_map["exec_"] = "exec"

                        self.aaa = Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.Aaa()
                        self.aaa.parent = self
                        self._children_name_map["aaa"] = "aaa"
                        self._segment_path = lambda: "auxiliary-statistics"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics, [], name, value)


                    class Rs232(Entity):
                        """
                        RS232 statistics of console line
                        
                        .. attribute:: data_bits
                        
                        	Number of databits
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: bit
                        
                        .. attribute:: exec_disabled
                        
                        	Exec disabled on TTY
                        	**type**\: bool
                        
                        .. attribute:: hardware_flow_control_status
                        
                        	Hardware flow control status
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: parity_status
                        
                        	Parity status
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: baud_rate
                        
                        	Inbound/Outbound baud rate in bps
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: bit/s
                        
                        .. attribute:: stop_bits
                        
                        	Number of stopbits
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: bit
                        
                        .. attribute:: overrun_error_count
                        
                        	Overrun error count
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: framing_error_count
                        
                        	Framing error count
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: parity_error_count
                        
                        	Parity error count
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'tty-server-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.Rs232, self).__init__()

                            self.yang_name = "rs232"
                            self.yang_parent_name = "auxiliary-statistics"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('data_bits', (YLeaf(YType.uint32, 'data-bits'), ['int'])),
                                ('exec_disabled', (YLeaf(YType.boolean, 'exec-disabled'), ['bool'])),
                                ('hardware_flow_control_status', (YLeaf(YType.uint32, 'hardware-flow-control-status'), ['int'])),
                                ('parity_status', (YLeaf(YType.uint32, 'parity-status'), ['int'])),
                                ('baud_rate', (YLeaf(YType.uint32, 'baud-rate'), ['int'])),
                                ('stop_bits', (YLeaf(YType.uint32, 'stop-bits'), ['int'])),
                                ('overrun_error_count', (YLeaf(YType.uint32, 'overrun-error-count'), ['int'])),
                                ('framing_error_count', (YLeaf(YType.uint32, 'framing-error-count'), ['int'])),
                                ('parity_error_count', (YLeaf(YType.uint32, 'parity-error-count'), ['int'])),
                            ])
                            self.data_bits = None
                            self.exec_disabled = None
                            self.hardware_flow_control_status = None
                            self.parity_status = None
                            self.baud_rate = None
                            self.stop_bits = None
                            self.overrun_error_count = None
                            self.framing_error_count = None
                            self.parity_error_count = None
                            self._segment_path = lambda: "rs232"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.Rs232, [u'data_bits', u'exec_disabled', u'hardware_flow_control_status', u'parity_status', u'baud_rate', u'stop_bits', u'overrun_error_count', u'framing_error_count', u'parity_error_count'], name, value)


                    class GeneralStatistics(Entity):
                        """
                        General statistics of line
                        
                        .. attribute:: terminal_length
                        
                        	Terminal length
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: terminal_width
                        
                        	Line width
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: async_interface
                        
                        	Usable as async interface
                        	**type**\: bool
                        
                        .. attribute:: flow_control_start_character
                        
                        	Software flow control start char
                        	**type**\: int
                        
                        	**range:** \-128..127
                        
                        .. attribute:: flow_control_stop_character
                        
                        	Software flow control stop char
                        	**type**\: int
                        
                        	**range:** \-128..127
                        
                        .. attribute:: domain_lookup_enabled
                        
                        	DNS resolution enabled
                        	**type**\: bool
                        
                        .. attribute:: motd_banner_enabled
                        
                        	MOTD banner enabled
                        	**type**\: bool
                        
                        .. attribute:: private_flag
                        
                        	TTY private flag
                        	**type**\: bool
                        
                        .. attribute:: terminal_type
                        
                        	Terminal type
                        	**type**\: str
                        
                        .. attribute:: absolute_timeout
                        
                        	Absolute timeout period
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: idle_time
                        
                        	TTY idle time
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'tty-server-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.GeneralStatistics, self).__init__()

                            self.yang_name = "general-statistics"
                            self.yang_parent_name = "auxiliary-statistics"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('terminal_length', (YLeaf(YType.uint32, 'terminal-length'), ['int'])),
                                ('terminal_width', (YLeaf(YType.uint32, 'terminal-width'), ['int'])),
                                ('async_interface', (YLeaf(YType.boolean, 'async-interface'), ['bool'])),
                                ('flow_control_start_character', (YLeaf(YType.int8, 'flow-control-start-character'), ['int'])),
                                ('flow_control_stop_character', (YLeaf(YType.int8, 'flow-control-stop-character'), ['int'])),
                                ('domain_lookup_enabled', (YLeaf(YType.boolean, 'domain-lookup-enabled'), ['bool'])),
                                ('motd_banner_enabled', (YLeaf(YType.boolean, 'motd-banner-enabled'), ['bool'])),
                                ('private_flag', (YLeaf(YType.boolean, 'private-flag'), ['bool'])),
                                ('terminal_type', (YLeaf(YType.str, 'terminal-type'), ['str'])),
                                ('absolute_timeout', (YLeaf(YType.uint32, 'absolute-timeout'), ['int'])),
                                ('idle_time', (YLeaf(YType.uint32, 'idle-time'), ['int'])),
                            ])
                            self.terminal_length = None
                            self.terminal_width = None
                            self.async_interface = None
                            self.flow_control_start_character = None
                            self.flow_control_stop_character = None
                            self.domain_lookup_enabled = None
                            self.motd_banner_enabled = None
                            self.private_flag = None
                            self.terminal_type = None
                            self.absolute_timeout = None
                            self.idle_time = None
                            self._segment_path = lambda: "general-statistics"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.GeneralStatistics, ['terminal_length', 'terminal_width', 'async_interface', 'flow_control_start_character', 'flow_control_stop_character', 'domain_lookup_enabled', 'motd_banner_enabled', 'private_flag', 'terminal_type', 'absolute_timeout', 'idle_time'], name, value)


                    class Exec(Entity):
                        """
                        Exec related statistics
                        
                        .. attribute:: time_stamp_enabled
                        
                        	Specifies whether timestamp is enabled or not
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'tty-server-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.Exec, self).__init__()

                            self.yang_name = "exec"
                            self.yang_parent_name = "auxiliary-statistics"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('time_stamp_enabled', (YLeaf(YType.boolean, 'time-stamp-enabled'), ['bool'])),
                            ])
                            self.time_stamp_enabled = None
                            self._segment_path = lambda: "exec"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.Exec, [u'time_stamp_enabled'], name, value)


                    class Aaa(Entity):
                        """
                        AAA related statistics
                        
                        .. attribute:: user_name
                        
                        	The authenticated username
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'tty-server-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.Aaa, self).__init__()

                            self.yang_name = "aaa"
                            self.yang_parent_name = "auxiliary-statistics"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('user_name', (YLeaf(YType.str, 'user-name'), ['str'])),
                            ])
                            self.user_name = None
                            self._segment_path = lambda: "aaa"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.Aaa, [u'user_name'], name, value)


                class State(Entity):
                    """
                    Line state information
                    
                    .. attribute:: template
                    
                    	Information related to template applied to the line
                    	**type**\:  :py:class:`Template <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.State.Template>`
                    
                    .. attribute:: general
                    
                    	General information
                    	**type**\:  :py:class:`General <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.State.General>`
                    
                    

                    """

                    _prefix = 'tty-server-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "auxiliary-line"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("template", ("template", Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.State.Template)), ("general", ("general", Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.State.General))])
                        self._leafs = OrderedDict()

                        self.template = Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.State.Template()
                        self.template.parent = self
                        self._children_name_map["template"] = "template"

                        self.general = Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.State.General()
                        self.general.parent = self
                        self._children_name_map["general"] = "general"
                        self._segment_path = lambda: "state"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.State, [], name, value)


                    class Template(Entity):
                        """
                        Information related to template applied to the
                        line
                        
                        .. attribute:: name
                        
                        	Name of the template
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'tty-server-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.State.Template, self).__init__()

                            self.yang_name = "template"
                            self.yang_parent_name = "state"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                            ])
                            self.name = None
                            self._segment_path = lambda: "template"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.State.Template, ['name'], name, value)


                    class General(Entity):
                        """
                        General information
                        
                        .. attribute:: operation_
                        
                        	application running of on the tty line
                        	**type**\:  :py:class:`SessionOperation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.SessionOperation>`
                        
                        .. attribute:: general_state
                        
                        	State of the line
                        	**type**\:  :py:class:`LineState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.LineState>`
                        
                        

                        """

                        _prefix = 'tty-server-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.State.General, self).__init__()

                            self.yang_name = "general"
                            self.yang_parent_name = "state"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('operation_', (YLeaf(YType.enumeration, 'operation'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper', 'SessionOperation', '')])),
                                ('general_state', (YLeaf(YType.enumeration, 'general-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper', 'LineState', '')])),
                            ])
                            self.operation_ = None
                            self.general_state = None
                            self._segment_path = lambda: "general"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.State.General, ['operation_', 'general_state'], name, value)


                class Configuration(Entity):
                    """
                    Configuration information of the line
                    
                    .. attribute:: connection_configuration
                    
                    	Conection configuration information
                    	**type**\:  :py:class:`ConnectionConfiguration <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.Configuration.ConnectionConfiguration>`
                    
                    

                    """

                    _prefix = 'tty-server-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.Configuration, self).__init__()

                        self.yang_name = "configuration"
                        self.yang_parent_name = "auxiliary-line"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("connection-configuration", ("connection_configuration", Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.Configuration.ConnectionConfiguration))])
                        self._leafs = OrderedDict()

                        self.connection_configuration = Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.Configuration.ConnectionConfiguration()
                        self.connection_configuration.parent = self
                        self._children_name_map["connection_configuration"] = "connection-configuration"
                        self._segment_path = lambda: "configuration"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.Configuration, [], name, value)


                    class ConnectionConfiguration(Entity):
                        """
                        Conection configuration information
                        
                        .. attribute:: transport_input
                        
                        	Protocols to use when connecting to the terminal server
                        	**type**\:  :py:class:`TransportInput <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.Configuration.ConnectionConfiguration.TransportInput>`
                        
                        .. attribute:: acl_out
                        
                        	ACL for outbound traffic
                        	**type**\: str
                        
                        .. attribute:: acl_in
                        
                        	ACL for inbound traffic
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'tty-server-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.Configuration.ConnectionConfiguration, self).__init__()

                            self.yang_name = "connection-configuration"
                            self.yang_parent_name = "configuration"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("transport-input", ("transport_input", Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.Configuration.ConnectionConfiguration.TransportInput))])
                            self._leafs = OrderedDict([
                                ('acl_out', (YLeaf(YType.str, 'acl-out'), ['str'])),
                                ('acl_in', (YLeaf(YType.str, 'acl-in'), ['str'])),
                            ])
                            self.acl_out = None
                            self.acl_in = None

                            self.transport_input = Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.Configuration.ConnectionConfiguration.TransportInput()
                            self.transport_input.parent = self
                            self._children_name_map["transport_input"] = "transport-input"
                            self._segment_path = lambda: "connection-configuration"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.Configuration.ConnectionConfiguration, ['acl_out', 'acl_in'], name, value)


                        class TransportInput(Entity):
                            """
                            Protocols to use when connecting to the
                            terminal server
                            
                            .. attribute:: select
                            
                            	Choose transport protocols
                            	**type**\:  :py:class:`TtyTransportProtocolSelect <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes.TtyTransportProtocolSelect>`
                            
                            	**default value**\: all
                            
                            .. attribute:: protocol1
                            
                            	Transport protocol1
                            	**type**\:  :py:class:`TtyTransportProtocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes.TtyTransportProtocol>`
                            
                            .. attribute:: protocol2
                            
                            	Transport protocol2
                            	**type**\:  :py:class:`TtyTransportProtocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes.TtyTransportProtocol>`
                            
                            .. attribute:: none
                            
                            	Not used
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'tty-server-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.Configuration.ConnectionConfiguration.TransportInput, self).__init__()

                                self.yang_name = "transport-input"
                                self.yang_parent_name = "connection-configuration"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('select', (YLeaf(YType.enumeration, 'select'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes', 'TtyTransportProtocolSelect', '')])),
                                    ('protocol1', (YLeaf(YType.enumeration, 'protocol1'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes', 'TtyTransportProtocol', '')])),
                                    ('protocol2', (YLeaf(YType.enumeration, 'protocol2'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes', 'TtyTransportProtocol', '')])),
                                    ('none', (YLeaf(YType.uint32, 'none'), ['int'])),
                                ])
                                self.select = None
                                self.protocol1 = None
                                self.protocol2 = None
                                self.none = None
                                self._segment_path = lambda: "transport-input"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.Configuration.ConnectionConfiguration.TransportInput, ['select', 'protocol1', 'protocol2', 'none'], name, value)

    def clone_ptr(self):
        self._top_entity = Tty()
        return self._top_entity

