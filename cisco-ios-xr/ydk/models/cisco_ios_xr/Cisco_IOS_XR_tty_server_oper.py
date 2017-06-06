""" Cisco_IOS_XR_tty_server_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR tty\-server package operational data.

This module contains definitions
for the following management objects\:
  tty\: TTY Line Configuration

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class LineStateEnum(Enum):
    """
    LineStateEnum

    Line state

    .. data:: none = 0

    	Line not connected

    .. data:: registered = 1

    	Line registered

    .. data:: in_use = 2

    	Line active and in use

    """

    none = 0

    registered = 1

    in_use = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tty_server_oper as meta
        return meta._meta_table['LineStateEnum']


class SessionOperationEnum(Enum):
    """
    SessionOperationEnum

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

    none = 0

    setup = 1

    shell = 2

    transitioning = 3

    packet = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tty_server_oper as meta
        return meta._meta_table['SessionOperationEnum']



class Tty(object):
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
        self.auxiliary_nodes = Tty.AuxiliaryNodes()
        self.auxiliary_nodes.parent = self
        self.console_nodes = Tty.ConsoleNodes()
        self.console_nodes.parent = self
        self.vty_lines = Tty.VtyLines()
        self.vty_lines.parent = self


    class ConsoleNodes(object):
        """
        List of Nodes for console
        
        .. attribute:: console_node
        
        	Console line configuration on a node
        	**type**\: list of    :py:class:`ConsoleNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.ConsoleNodes.ConsoleNode>`
        
        

        """

        _prefix = 'tty-server-oper'
        _revision = '2015-07-30'

        def __init__(self):
            self.parent = None
            self.console_node = YList()
            self.console_node.parent = self
            self.console_node.name = 'console_node'


        class ConsoleNode(object):
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
                self.parent = None
                self.id = None
                self.console_line = Tty.ConsoleNodes.ConsoleNode.ConsoleLine()
                self.console_line.parent = self


            class ConsoleLine(object):
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
                    self.parent = None
                    self.configuration = Tty.ConsoleNodes.ConsoleNode.ConsoleLine.Configuration()
                    self.configuration.parent = self
                    self.console_statistics = Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics()
                    self.console_statistics.parent = self
                    self.state = Tty.ConsoleNodes.ConsoleNode.ConsoleLine.State()
                    self.state.parent = self


                class ConsoleStatistics(object):
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
                        self.parent = None
                        self.aaa = Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.Aaa()
                        self.aaa.parent = self
                        self.exec_ = Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.Exec_()
                        self.exec_.parent = self
                        self.general_statistics = Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.GeneralStatistics()
                        self.general_statistics.parent = self
                        self.rs232 = Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.Rs232()
                        self.rs232.parent = self


                    class Rs232(object):
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
                            self.parent = None
                            self.baud_rate = None
                            self.data_bits = None
                            self.exec_disabled = None
                            self.framing_error_count = None
                            self.hardware_flow_control_status = None
                            self.overrun_error_count = None
                            self.parity_error_count = None
                            self.parity_status = None
                            self.stop_bits = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-tty-server-oper:rs232'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.baud_rate is not None:
                                return True

                            if self.data_bits is not None:
                                return True

                            if self.exec_disabled is not None:
                                return True

                            if self.framing_error_count is not None:
                                return True

                            if self.hardware_flow_control_status is not None:
                                return True

                            if self.overrun_error_count is not None:
                                return True

                            if self.parity_error_count is not None:
                                return True

                            if self.parity_status is not None:
                                return True

                            if self.stop_bits is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tty_server_oper as meta
                            return meta._meta_table['Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.Rs232']['meta_info']


                    class GeneralStatistics(object):
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
                            self.parent = None
                            self.absolute_timeout = None
                            self.async_interface = None
                            self.domain_lookup_enabled = None
                            self.flow_control_start_character = None
                            self.flow_control_stop_character = None
                            self.idle_time = None
                            self.motd_banner_enabled = None
                            self.private_flag = None
                            self.terminal_length = None
                            self.terminal_type = None
                            self.terminal_width = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-tty-server-oper:general-statistics'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.absolute_timeout is not None:
                                return True

                            if self.async_interface is not None:
                                return True

                            if self.domain_lookup_enabled is not None:
                                return True

                            if self.flow_control_start_character is not None:
                                return True

                            if self.flow_control_stop_character is not None:
                                return True

                            if self.idle_time is not None:
                                return True

                            if self.motd_banner_enabled is not None:
                                return True

                            if self.private_flag is not None:
                                return True

                            if self.terminal_length is not None:
                                return True

                            if self.terminal_type is not None:
                                return True

                            if self.terminal_width is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tty_server_oper as meta
                            return meta._meta_table['Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.GeneralStatistics']['meta_info']


                    class Exec_(object):
                        """
                        Exec related statistics
                        
                        .. attribute:: time_stamp_enabled
                        
                        	Specifies whether timestamp is enabled or not
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'tty-server-oper'
                        _revision = '2015-07-30'

                        def __init__(self):
                            self.parent = None
                            self.time_stamp_enabled = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-tty-server-oper:exec'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.time_stamp_enabled is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tty_server_oper as meta
                            return meta._meta_table['Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.Exec_']['meta_info']


                    class Aaa(object):
                        """
                        AAA related statistics
                        
                        .. attribute:: user_name
                        
                        	The authenticated username
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'tty-server-oper'
                        _revision = '2015-07-30'

                        def __init__(self):
                            self.parent = None
                            self.user_name = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-tty-server-oper:aaa'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.user_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tty_server_oper as meta
                            return meta._meta_table['Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.Aaa']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-tty-server-oper:console-statistics'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.aaa is not None and self.aaa._has_data():
                            return True

                        if self.exec_ is not None and self.exec_._has_data():
                            return True

                        if self.general_statistics is not None and self.general_statistics._has_data():
                            return True

                        if self.rs232 is not None and self.rs232._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tty_server_oper as meta
                        return meta._meta_table['Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics']['meta_info']


                class State(object):
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
                        self.parent = None
                        self.general = Tty.ConsoleNodes.ConsoleNode.ConsoleLine.State.General()
                        self.general.parent = self
                        self.template = Tty.ConsoleNodes.ConsoleNode.ConsoleLine.State.Template()
                        self.template.parent = self


                    class Template(object):
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
                            self.parent = None
                            self.name = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-tty-server-oper:template'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tty_server_oper as meta
                            return meta._meta_table['Tty.ConsoleNodes.ConsoleNode.ConsoleLine.State.Template']['meta_info']


                    class General(object):
                        """
                        General information
                        
                        .. attribute:: general_state
                        
                        	State of the line
                        	**type**\:   :py:class:`LineStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.LineStateEnum>`
                        
                        .. attribute:: operation
                        
                        	application running of on the tty line
                        	**type**\:   :py:class:`SessionOperationEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.SessionOperationEnum>`
                        
                        

                        """

                        _prefix = 'tty-server-oper'
                        _revision = '2015-07-30'

                        def __init__(self):
                            self.parent = None
                            self.general_state = None
                            self.operation = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-tty-server-oper:general'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.general_state is not None:
                                return True

                            if self.operation is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tty_server_oper as meta
                            return meta._meta_table['Tty.ConsoleNodes.ConsoleNode.ConsoleLine.State.General']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-tty-server-oper:state'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.general is not None and self.general._has_data():
                            return True

                        if self.template is not None and self.template._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tty_server_oper as meta
                        return meta._meta_table['Tty.ConsoleNodes.ConsoleNode.ConsoleLine.State']['meta_info']


                class Configuration(object):
                    """
                    Configuration information of the line
                    
                    .. attribute:: connection_configuration
                    
                    	Conection configuration information
                    	**type**\:   :py:class:`ConnectionConfiguration <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.ConsoleNodes.ConsoleNode.ConsoleLine.Configuration.ConnectionConfiguration>`
                    
                    

                    """

                    _prefix = 'tty-server-oper'
                    _revision = '2015-07-30'

                    def __init__(self):
                        self.parent = None
                        self.connection_configuration = Tty.ConsoleNodes.ConsoleNode.ConsoleLine.Configuration.ConnectionConfiguration()
                        self.connection_configuration.parent = self


                    class ConnectionConfiguration(object):
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
                            self.parent = None
                            self.acl_in = None
                            self.acl_out = None
                            self.transport_input = Tty.ConsoleNodes.ConsoleNode.ConsoleLine.Configuration.ConnectionConfiguration.TransportInput()
                            self.transport_input.parent = self


                        class TransportInput(object):
                            """
                            Protocols to use when connecting to the
                            terminal server
                            
                            .. attribute:: none
                            
                            	Not used
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: protocol1
                            
                            	Transport protocol1
                            	**type**\:   :py:class:`TtyTransportProtocolEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes.TtyTransportProtocolEnum>`
                            
                            .. attribute:: protocol2
                            
                            	Transport protocol2
                            	**type**\:   :py:class:`TtyTransportProtocolEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes.TtyTransportProtocolEnum>`
                            
                            .. attribute:: select
                            
                            	Choose transport protocols
                            	**type**\:   :py:class:`TtyTransportProtocolSelectEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes.TtyTransportProtocolSelectEnum>`
                            
                            	**default value**\: all
                            
                            

                            """

                            _prefix = 'tty-server-oper'
                            _revision = '2015-07-30'

                            def __init__(self):
                                self.parent = None
                                self.none = None
                                self.protocol1 = None
                                self.protocol2 = None
                                self.select = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-tty-server-oper:transport-input'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.none is not None:
                                    return True

                                if self.protocol1 is not None:
                                    return True

                                if self.protocol2 is not None:
                                    return True

                                if self.select is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tty_server_oper as meta
                                return meta._meta_table['Tty.ConsoleNodes.ConsoleNode.ConsoleLine.Configuration.ConnectionConfiguration.TransportInput']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-tty-server-oper:connection-configuration'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.acl_in is not None:
                                return True

                            if self.acl_out is not None:
                                return True

                            if self.transport_input is not None and self.transport_input._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tty_server_oper as meta
                            return meta._meta_table['Tty.ConsoleNodes.ConsoleNode.ConsoleLine.Configuration.ConnectionConfiguration']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-tty-server-oper:configuration'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.connection_configuration is not None and self.connection_configuration._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tty_server_oper as meta
                        return meta._meta_table['Tty.ConsoleNodes.ConsoleNode.ConsoleLine.Configuration']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-tty-server-oper:console-line'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.configuration is not None and self.configuration._has_data():
                        return True

                    if self.console_statistics is not None and self.console_statistics._has_data():
                        return True

                    if self.state is not None and self.state._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tty_server_oper as meta
                    return meta._meta_table['Tty.ConsoleNodes.ConsoleNode.ConsoleLine']['meta_info']

            @property
            def _common_path(self):
                if self.id is None:
                    raise YPYModelError('Key property id is None')

                return '/Cisco-IOS-XR-tty-server-oper:tty/Cisco-IOS-XR-tty-server-oper:console-nodes/Cisco-IOS-XR-tty-server-oper:console-node[Cisco-IOS-XR-tty-server-oper:id = ' + str(self.id) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.id is not None:
                    return True

                if self.console_line is not None and self.console_line._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tty_server_oper as meta
                return meta._meta_table['Tty.ConsoleNodes.ConsoleNode']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-tty-server-oper:tty/Cisco-IOS-XR-tty-server-oper:console-nodes'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.console_node is not None:
                for child_ref in self.console_node:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tty_server_oper as meta
            return meta._meta_table['Tty.ConsoleNodes']['meta_info']


    class VtyLines(object):
        """
        List of VTY lines
        
        .. attribute:: vty_line
        
        	VTY Line
        	**type**\: list of    :py:class:`VtyLine <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.VtyLines.VtyLine>`
        
        

        """

        _prefix = 'tty-server-oper'
        _revision = '2015-07-30'

        def __init__(self):
            self.parent = None
            self.vty_line = YList()
            self.vty_line.parent = self
            self.vty_line.name = 'vty_line'


        class VtyLine(object):
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
                self.parent = None
                self.line_number = None
                self.configuration = Tty.VtyLines.VtyLine.Configuration()
                self.configuration.parent = self
                self.sessions = Tty.VtyLines.VtyLine.Sessions()
                self.sessions.parent = self
                self.state = Tty.VtyLines.VtyLine.State()
                self.state.parent = self
                self.vty_statistics = Tty.VtyLines.VtyLine.VtyStatistics()
                self.vty_statistics.parent = self


            class VtyStatistics(object):
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
                    self.parent = None
                    self.aaa = Tty.VtyLines.VtyLine.VtyStatistics.Aaa()
                    self.aaa.parent = self
                    self.connection = Tty.VtyLines.VtyLine.VtyStatistics.Connection()
                    self.connection.parent = self
                    self.exec_ = Tty.VtyLines.VtyLine.VtyStatistics.Exec_()
                    self.exec_.parent = self
                    self.general_statistics = Tty.VtyLines.VtyLine.VtyStatistics.GeneralStatistics()
                    self.general_statistics.parent = self


                class Connection(object):
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
                        self.parent = None
                        self.host_address_family = None
                        self.incoming_host_address = None
                        self.service = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-tty-server-oper:connection'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.host_address_family is not None:
                            return True

                        if self.incoming_host_address is not None:
                            return True

                        if self.service is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tty_server_oper as meta
                        return meta._meta_table['Tty.VtyLines.VtyLine.VtyStatistics.Connection']['meta_info']


                class GeneralStatistics(object):
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
                        self.parent = None
                        self.absolute_timeout = None
                        self.async_interface = None
                        self.domain_lookup_enabled = None
                        self.flow_control_start_character = None
                        self.flow_control_stop_character = None
                        self.idle_time = None
                        self.motd_banner_enabled = None
                        self.private_flag = None
                        self.terminal_length = None
                        self.terminal_type = None
                        self.terminal_width = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-tty-server-oper:general-statistics'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.absolute_timeout is not None:
                            return True

                        if self.async_interface is not None:
                            return True

                        if self.domain_lookup_enabled is not None:
                            return True

                        if self.flow_control_start_character is not None:
                            return True

                        if self.flow_control_stop_character is not None:
                            return True

                        if self.idle_time is not None:
                            return True

                        if self.motd_banner_enabled is not None:
                            return True

                        if self.private_flag is not None:
                            return True

                        if self.terminal_length is not None:
                            return True

                        if self.terminal_type is not None:
                            return True

                        if self.terminal_width is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tty_server_oper as meta
                        return meta._meta_table['Tty.VtyLines.VtyLine.VtyStatistics.GeneralStatistics']['meta_info']


                class Exec_(object):
                    """
                    Exec related statistics
                    
                    .. attribute:: time_stamp_enabled
                    
                    	Specifies whether timestamp is enabled or not
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'tty-server-oper'
                    _revision = '2015-07-30'

                    def __init__(self):
                        self.parent = None
                        self.time_stamp_enabled = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-tty-server-oper:exec'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.time_stamp_enabled is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tty_server_oper as meta
                        return meta._meta_table['Tty.VtyLines.VtyLine.VtyStatistics.Exec_']['meta_info']


                class Aaa(object):
                    """
                    AAA related statistics
                    
                    .. attribute:: user_name
                    
                    	The authenticated username
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'tty-server-oper'
                    _revision = '2015-07-30'

                    def __init__(self):
                        self.parent = None
                        self.user_name = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-tty-server-oper:aaa'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.user_name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tty_server_oper as meta
                        return meta._meta_table['Tty.VtyLines.VtyLine.VtyStatistics.Aaa']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-tty-server-oper:vty-statistics'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.aaa is not None and self.aaa._has_data():
                        return True

                    if self.connection is not None and self.connection._has_data():
                        return True

                    if self.exec_ is not None and self.exec_._has_data():
                        return True

                    if self.general_statistics is not None and self.general_statistics._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tty_server_oper as meta
                    return meta._meta_table['Tty.VtyLines.VtyLine.VtyStatistics']['meta_info']


            class State(object):
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
                    self.parent = None
                    self.general = Tty.VtyLines.VtyLine.State.General()
                    self.general.parent = self
                    self.template = Tty.VtyLines.VtyLine.State.Template()
                    self.template.parent = self


                class Template(object):
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
                        self.parent = None
                        self.name = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-tty-server-oper:template'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tty_server_oper as meta
                        return meta._meta_table['Tty.VtyLines.VtyLine.State.Template']['meta_info']


                class General(object):
                    """
                    General information
                    
                    .. attribute:: general_state
                    
                    	State of the line
                    	**type**\:   :py:class:`LineStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.LineStateEnum>`
                    
                    .. attribute:: operation
                    
                    	application running of on the tty line
                    	**type**\:   :py:class:`SessionOperationEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.SessionOperationEnum>`
                    
                    

                    """

                    _prefix = 'tty-server-oper'
                    _revision = '2015-07-30'

                    def __init__(self):
                        self.parent = None
                        self.general_state = None
                        self.operation = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-tty-server-oper:general'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.general_state is not None:
                            return True

                        if self.operation is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tty_server_oper as meta
                        return meta._meta_table['Tty.VtyLines.VtyLine.State.General']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-tty-server-oper:state'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.general is not None and self.general._has_data():
                        return True

                    if self.template is not None and self.template._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tty_server_oper as meta
                    return meta._meta_table['Tty.VtyLines.VtyLine.State']['meta_info']


            class Configuration(object):
                """
                Configuration information of the line
                
                .. attribute:: connection_configuration
                
                	Conection configuration information
                	**type**\:   :py:class:`ConnectionConfiguration <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.VtyLines.VtyLine.Configuration.ConnectionConfiguration>`
                
                

                """

                _prefix = 'tty-server-oper'
                _revision = '2015-07-30'

                def __init__(self):
                    self.parent = None
                    self.connection_configuration = Tty.VtyLines.VtyLine.Configuration.ConnectionConfiguration()
                    self.connection_configuration.parent = self


                class ConnectionConfiguration(object):
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
                        self.parent = None
                        self.acl_in = None
                        self.acl_out = None
                        self.transport_input = Tty.VtyLines.VtyLine.Configuration.ConnectionConfiguration.TransportInput()
                        self.transport_input.parent = self


                    class TransportInput(object):
                        """
                        Protocols to use when connecting to the
                        terminal server
                        
                        .. attribute:: none
                        
                        	Not used
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: protocol1
                        
                        	Transport protocol1
                        	**type**\:   :py:class:`TtyTransportProtocolEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes.TtyTransportProtocolEnum>`
                        
                        .. attribute:: protocol2
                        
                        	Transport protocol2
                        	**type**\:   :py:class:`TtyTransportProtocolEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes.TtyTransportProtocolEnum>`
                        
                        .. attribute:: select
                        
                        	Choose transport protocols
                        	**type**\:   :py:class:`TtyTransportProtocolSelectEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes.TtyTransportProtocolSelectEnum>`
                        
                        	**default value**\: all
                        
                        

                        """

                        _prefix = 'tty-server-oper'
                        _revision = '2015-07-30'

                        def __init__(self):
                            self.parent = None
                            self.none = None
                            self.protocol1 = None
                            self.protocol2 = None
                            self.select = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-tty-server-oper:transport-input'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.none is not None:
                                return True

                            if self.protocol1 is not None:
                                return True

                            if self.protocol2 is not None:
                                return True

                            if self.select is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tty_server_oper as meta
                            return meta._meta_table['Tty.VtyLines.VtyLine.Configuration.ConnectionConfiguration.TransportInput']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-tty-server-oper:connection-configuration'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.acl_in is not None:
                            return True

                        if self.acl_out is not None:
                            return True

                        if self.transport_input is not None and self.transport_input._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tty_server_oper as meta
                        return meta._meta_table['Tty.VtyLines.VtyLine.Configuration.ConnectionConfiguration']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-tty-server-oper:configuration'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.connection_configuration is not None and self.connection_configuration._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tty_server_oper as meta
                    return meta._meta_table['Tty.VtyLines.VtyLine.Configuration']['meta_info']


            class Sessions(object):
                """
                Outgoing sessions
                
                .. attribute:: outgoing_connection
                
                	List of outgoing sessions
                	**type**\: list of    :py:class:`OutgoingConnection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.VtyLines.VtyLine.Sessions.OutgoingConnection>`
                
                

                """

                _prefix = 'tty-management-oper'
                _revision = '2015-01-07'

                def __init__(self):
                    self.parent = None
                    self.outgoing_connection = YList()
                    self.outgoing_connection.parent = self
                    self.outgoing_connection.name = 'outgoing_connection'


                class OutgoingConnection(object):
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
                    	**type**\:   :py:class:`TransportServiceEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_oper.TransportServiceEnum>`
                    
                    

                    """

                    _prefix = 'tty-management-oper'
                    _revision = '2015-01-07'

                    def __init__(self):
                        self.parent = None
                        self.connection_id = None
                        self.host_address = Tty.VtyLines.VtyLine.Sessions.OutgoingConnection.HostAddress()
                        self.host_address.parent = self
                        self.host_name = None
                        self.idle_time = None
                        self.is_last_active_session = None
                        self.transport_protocol = None


                    class HostAddress(object):
                        """
                        Host address
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\:   :py:class:`HostAfIdBaseIdentity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_oper.HostAfIdBaseIdentity>`
                        
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
                            self.parent = None
                            self.af_name = None
                            self.ipv4_address = None
                            self.ipv6_address = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-tty-management-oper:host-address'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.af_name is not None:
                                return True

                            if self.ipv4_address is not None:
                                return True

                            if self.ipv6_address is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tty_server_oper as meta
                            return meta._meta_table['Tty.VtyLines.VtyLine.Sessions.OutgoingConnection.HostAddress']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-tty-management-oper:outgoing-connection'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.connection_id is not None:
                            return True

                        if self.host_address is not None and self.host_address._has_data():
                            return True

                        if self.host_name is not None:
                            return True

                        if self.idle_time is not None:
                            return True

                        if self.is_last_active_session is not None:
                            return True

                        if self.transport_protocol is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tty_server_oper as meta
                        return meta._meta_table['Tty.VtyLines.VtyLine.Sessions.OutgoingConnection']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-tty-management-oper:sessions'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.outgoing_connection is not None:
                        for child_ref in self.outgoing_connection:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tty_server_oper as meta
                    return meta._meta_table['Tty.VtyLines.VtyLine.Sessions']['meta_info']

            @property
            def _common_path(self):
                if self.line_number is None:
                    raise YPYModelError('Key property line_number is None')

                return '/Cisco-IOS-XR-tty-server-oper:tty/Cisco-IOS-XR-tty-server-oper:vty-lines/Cisco-IOS-XR-tty-server-oper:vty-line[Cisco-IOS-XR-tty-server-oper:line-number = ' + str(self.line_number) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.line_number is not None:
                    return True

                if self.configuration is not None and self.configuration._has_data():
                    return True

                if self.sessions is not None and self.sessions._has_data():
                    return True

                if self.state is not None and self.state._has_data():
                    return True

                if self.vty_statistics is not None and self.vty_statistics._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tty_server_oper as meta
                return meta._meta_table['Tty.VtyLines.VtyLine']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-tty-server-oper:tty/Cisco-IOS-XR-tty-server-oper:vty-lines'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.vty_line is not None:
                for child_ref in self.vty_line:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tty_server_oper as meta
            return meta._meta_table['Tty.VtyLines']['meta_info']


    class AuxiliaryNodes(object):
        """
        List of Nodes attached with an auxiliary line
        
        .. attribute:: auxiliary_node
        
        	Line configuration on a node
        	**type**\: list of    :py:class:`AuxiliaryNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.AuxiliaryNodes.AuxiliaryNode>`
        
        

        """

        _prefix = 'tty-server-oper'
        _revision = '2015-07-30'

        def __init__(self):
            self.parent = None
            self.auxiliary_node = YList()
            self.auxiliary_node.parent = self
            self.auxiliary_node.name = 'auxiliary_node'


        class AuxiliaryNode(object):
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
                self.parent = None
                self.id = None
                self.auxiliary_line = Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine()
                self.auxiliary_line.parent = self


            class AuxiliaryLine(object):
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
                    self.parent = None
                    self.auxiliary_statistics = Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics()
                    self.auxiliary_statistics.parent = self
                    self.configuration = Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.Configuration()
                    self.configuration.parent = self
                    self.state = Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.State()
                    self.state.parent = self


                class AuxiliaryStatistics(object):
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
                        self.parent = None
                        self.aaa = Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.Aaa()
                        self.aaa.parent = self
                        self.exec_ = Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.Exec_()
                        self.exec_.parent = self
                        self.general_statistics = Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.GeneralStatistics()
                        self.general_statistics.parent = self
                        self.rs232 = Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.Rs232()
                        self.rs232.parent = self


                    class Rs232(object):
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
                            self.parent = None
                            self.baud_rate = None
                            self.data_bits = None
                            self.exec_disabled = None
                            self.framing_error_count = None
                            self.hardware_flow_control_status = None
                            self.overrun_error_count = None
                            self.parity_error_count = None
                            self.parity_status = None
                            self.stop_bits = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-tty-server-oper:rs232'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.baud_rate is not None:
                                return True

                            if self.data_bits is not None:
                                return True

                            if self.exec_disabled is not None:
                                return True

                            if self.framing_error_count is not None:
                                return True

                            if self.hardware_flow_control_status is not None:
                                return True

                            if self.overrun_error_count is not None:
                                return True

                            if self.parity_error_count is not None:
                                return True

                            if self.parity_status is not None:
                                return True

                            if self.stop_bits is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tty_server_oper as meta
                            return meta._meta_table['Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.Rs232']['meta_info']


                    class GeneralStatistics(object):
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
                            self.parent = None
                            self.absolute_timeout = None
                            self.async_interface = None
                            self.domain_lookup_enabled = None
                            self.flow_control_start_character = None
                            self.flow_control_stop_character = None
                            self.idle_time = None
                            self.motd_banner_enabled = None
                            self.private_flag = None
                            self.terminal_length = None
                            self.terminal_type = None
                            self.terminal_width = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-tty-server-oper:general-statistics'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.absolute_timeout is not None:
                                return True

                            if self.async_interface is not None:
                                return True

                            if self.domain_lookup_enabled is not None:
                                return True

                            if self.flow_control_start_character is not None:
                                return True

                            if self.flow_control_stop_character is not None:
                                return True

                            if self.idle_time is not None:
                                return True

                            if self.motd_banner_enabled is not None:
                                return True

                            if self.private_flag is not None:
                                return True

                            if self.terminal_length is not None:
                                return True

                            if self.terminal_type is not None:
                                return True

                            if self.terminal_width is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tty_server_oper as meta
                            return meta._meta_table['Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.GeneralStatistics']['meta_info']


                    class Exec_(object):
                        """
                        Exec related statistics
                        
                        .. attribute:: time_stamp_enabled
                        
                        	Specifies whether timestamp is enabled or not
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'tty-server-oper'
                        _revision = '2015-07-30'

                        def __init__(self):
                            self.parent = None
                            self.time_stamp_enabled = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-tty-server-oper:exec'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.time_stamp_enabled is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tty_server_oper as meta
                            return meta._meta_table['Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.Exec_']['meta_info']


                    class Aaa(object):
                        """
                        AAA related statistics
                        
                        .. attribute:: user_name
                        
                        	The authenticated username
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'tty-server-oper'
                        _revision = '2015-07-30'

                        def __init__(self):
                            self.parent = None
                            self.user_name = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-tty-server-oper:aaa'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.user_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tty_server_oper as meta
                            return meta._meta_table['Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.Aaa']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-tty-server-oper:auxiliary-statistics'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.aaa is not None and self.aaa._has_data():
                            return True

                        if self.exec_ is not None and self.exec_._has_data():
                            return True

                        if self.general_statistics is not None and self.general_statistics._has_data():
                            return True

                        if self.rs232 is not None and self.rs232._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tty_server_oper as meta
                        return meta._meta_table['Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics']['meta_info']


                class State(object):
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
                        self.parent = None
                        self.general = Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.State.General()
                        self.general.parent = self
                        self.template = Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.State.Template()
                        self.template.parent = self


                    class Template(object):
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
                            self.parent = None
                            self.name = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-tty-server-oper:template'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tty_server_oper as meta
                            return meta._meta_table['Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.State.Template']['meta_info']


                    class General(object):
                        """
                        General information
                        
                        .. attribute:: general_state
                        
                        	State of the line
                        	**type**\:   :py:class:`LineStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.LineStateEnum>`
                        
                        .. attribute:: operation
                        
                        	application running of on the tty line
                        	**type**\:   :py:class:`SessionOperationEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.SessionOperationEnum>`
                        
                        

                        """

                        _prefix = 'tty-server-oper'
                        _revision = '2015-07-30'

                        def __init__(self):
                            self.parent = None
                            self.general_state = None
                            self.operation = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-tty-server-oper:general'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.general_state is not None:
                                return True

                            if self.operation is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tty_server_oper as meta
                            return meta._meta_table['Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.State.General']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-tty-server-oper:state'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.general is not None and self.general._has_data():
                            return True

                        if self.template is not None and self.template._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tty_server_oper as meta
                        return meta._meta_table['Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.State']['meta_info']


                class Configuration(object):
                    """
                    Configuration information of the line
                    
                    .. attribute:: connection_configuration
                    
                    	Conection configuration information
                    	**type**\:   :py:class:`ConnectionConfiguration <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper.Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.Configuration.ConnectionConfiguration>`
                    
                    

                    """

                    _prefix = 'tty-server-oper'
                    _revision = '2015-07-30'

                    def __init__(self):
                        self.parent = None
                        self.connection_configuration = Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.Configuration.ConnectionConfiguration()
                        self.connection_configuration.parent = self


                    class ConnectionConfiguration(object):
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
                            self.parent = None
                            self.acl_in = None
                            self.acl_out = None
                            self.transport_input = Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.Configuration.ConnectionConfiguration.TransportInput()
                            self.transport_input.parent = self


                        class TransportInput(object):
                            """
                            Protocols to use when connecting to the
                            terminal server
                            
                            .. attribute:: none
                            
                            	Not used
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: protocol1
                            
                            	Transport protocol1
                            	**type**\:   :py:class:`TtyTransportProtocolEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes.TtyTransportProtocolEnum>`
                            
                            .. attribute:: protocol2
                            
                            	Transport protocol2
                            	**type**\:   :py:class:`TtyTransportProtocolEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes.TtyTransportProtocolEnum>`
                            
                            .. attribute:: select
                            
                            	Choose transport protocols
                            	**type**\:   :py:class:`TtyTransportProtocolSelectEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes.TtyTransportProtocolSelectEnum>`
                            
                            	**default value**\: all
                            
                            

                            """

                            _prefix = 'tty-server-oper'
                            _revision = '2015-07-30'

                            def __init__(self):
                                self.parent = None
                                self.none = None
                                self.protocol1 = None
                                self.protocol2 = None
                                self.select = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-tty-server-oper:transport-input'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.none is not None:
                                    return True

                                if self.protocol1 is not None:
                                    return True

                                if self.protocol2 is not None:
                                    return True

                                if self.select is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tty_server_oper as meta
                                return meta._meta_table['Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.Configuration.ConnectionConfiguration.TransportInput']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-tty-server-oper:connection-configuration'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.acl_in is not None:
                                return True

                            if self.acl_out is not None:
                                return True

                            if self.transport_input is not None and self.transport_input._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tty_server_oper as meta
                            return meta._meta_table['Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.Configuration.ConnectionConfiguration']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-tty-server-oper:configuration'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.connection_configuration is not None and self.connection_configuration._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tty_server_oper as meta
                        return meta._meta_table['Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.Configuration']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-tty-server-oper:auxiliary-line'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.auxiliary_statistics is not None and self.auxiliary_statistics._has_data():
                        return True

                    if self.configuration is not None and self.configuration._has_data():
                        return True

                    if self.state is not None and self.state._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tty_server_oper as meta
                    return meta._meta_table['Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine']['meta_info']

            @property
            def _common_path(self):
                if self.id is None:
                    raise YPYModelError('Key property id is None')

                return '/Cisco-IOS-XR-tty-server-oper:tty/Cisco-IOS-XR-tty-server-oper:auxiliary-nodes/Cisco-IOS-XR-tty-server-oper:auxiliary-node[Cisco-IOS-XR-tty-server-oper:id = ' + str(self.id) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.id is not None:
                    return True

                if self.auxiliary_line is not None and self.auxiliary_line._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tty_server_oper as meta
                return meta._meta_table['Tty.AuxiliaryNodes.AuxiliaryNode']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-tty-server-oper:tty/Cisco-IOS-XR-tty-server-oper:auxiliary-nodes'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.auxiliary_node is not None:
                for child_ref in self.auxiliary_node:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tty_server_oper as meta
            return meta._meta_table['Tty.AuxiliaryNodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-tty-server-oper:tty'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.auxiliary_nodes is not None and self.auxiliary_nodes._has_data():
            return True

        if self.console_nodes is not None and self.console_nodes._has_data():
            return True

        if self.vty_lines is not None and self.vty_lines._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tty_server_oper as meta
        return meta._meta_table['Tty']['meta_info']


