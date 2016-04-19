""" openconfig_terminal_device 

This module describes a terminal optics device model for
managing the terminal systems (client and line side) in a
DWDM transport network.

Elements of the model\:

physical client port\: corresponds to a physical, pluggable client
port on the terminal device. Examples includes 10G, 40G, 100G
(e.g., 10x10G, 4x25G or 1x100G) and 400G/1T in the future.
Physical client ports will have associated operational state or
PMs.

physical client channel\: a physical lane or channel in the
physical client port.  Each physical client port has 1 or more
channels. An example is 100GBASE\-LR4 client physical port having
4x25G channels. Channels have their own optical PMs and can be
monitored independently within a client physical port (e.g.,
channel power).  Physical client channels are defined in the
model as part of a physical client port, and are modeled
primarily for reading their PMs.

logical channel\: a logical grouping of logical grooming elements
that may be assigned to subsequent grooming stages for
multiplexing / de\-multiplexing, or to an optical channel for
line side transmission.  The logical channels can represent, for
example, an ODU/OTU logical packing of the client
data onto the line side.  Tributaries are similarly logical
groupings of demand that can be represented in this structure and
assigned to an optical channel.  Note that different types of
logical channels may be present, each with their corresponding
PMs.

optical channel\:  corresponds to an optical carrier and is
assigned a wavelength/frequency.  Optical channels have PMs
such as power, BER, and operational mode.

physical line port\: represent the physical line\-side ports on
the terminal device.  Line ports act as containers for optical
channels.

Directionality\:

To maintain simplicity in the model, the configuration is
described from client\-to\-line direction.  The assumption is that
equivalent reverse configuration is implicit, resulting in
the same line\-to\-client configuration.

Physical layout\:

The model does not assume a particular physical layout of client
and line ports on the terminal device (e.g., such as number of
ports per linecard, separate linecards for client and line ports,
etc.).

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError


from ydk.models.openconfig.openconfig_transport_types import EthernetPmdType_Identity
from ydk.models.openconfig.openconfig_transport_types import FiberConnectorType_Identity
from ydk.models.openconfig.openconfig_transport_types import LogicalElementProtocolType_Identity
from ydk.models.openconfig.openconfig_transport_types import OtnApplicationCode_Identity
from ydk.models.openconfig.openconfig_transport_types import SonetApplicationCode_Identity
from ydk.models.openconfig.openconfig_transport_types import TransceiverFormFactorType_Identity
from ydk.models.openconfig.openconfig_transport_types import TributaryProtocolType_Identity
from ydk.models.openconfig.openconfig_transport_types import TributaryRateClassType_Identity


class TerminalDevice(object):
    """
    Top\-level container for the terminal device
    
    .. attribute:: client_ports
    
    	Enclosing container for the list of client ports
    	**type**\: :py:class:`ClientPorts <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.ClientPorts>`
    
    .. attribute:: config
    
    	Configuration data for global terminal\-device
    	**type**\: :py:class:`Config <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.Config>`
    
    .. attribute:: line_ports
    
    	Enclosing container for line ports
    	**type**\: :py:class:`LinePorts <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LinePorts>`
    
    .. attribute:: logical_channels
    
    	Enclosing container the list of logical channels
    	**type**\: :py:class:`LogicalChannels <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels>`
    
    .. attribute:: operational_modes
    
    	Top\-level container for vendor\-specific operational mode information
    	**type**\: :py:class:`OperationalModes <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.OperationalModes>`
    
    .. attribute:: optical_channels
    
    	Enclosing container 
    	**type**\: :py:class:`OpticalChannels <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.OpticalChannels>`
    
    .. attribute:: state
    
    	Operational state data for global terminal device
    	**type**\: :py:class:`State <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.State>`
    
    

    """

    _prefix = 'opt-term'
    _revision = '2015-11-25'

    def __init__(self):
        self.client_ports = TerminalDevice.ClientPorts()
        self.client_ports.parent = self
        self.config = TerminalDevice.Config()
        self.config.parent = self
        self.line_ports = TerminalDevice.LinePorts()
        self.line_ports.parent = self
        self.logical_channels = TerminalDevice.LogicalChannels()
        self.logical_channels.parent = self
        self.operational_modes = TerminalDevice.OperationalModes()
        self.operational_modes.parent = self
        self.optical_channels = TerminalDevice.OpticalChannels()
        self.optical_channels.parent = self
        self.state = TerminalDevice.State()
        self.state.parent = self


    class ClientPorts(object):
        """
        Enclosing container for the list of client ports
        
        .. attribute:: port
        
        	List of client physical ports on the terminal device
        	**type**\: list of :py:class:`Port <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.ClientPorts.Port>`
        
        

        """

        _prefix = 'opt-term'
        _revision = '2015-11-25'

        def __init__(self):
            self.parent = None
            self.port = YList()
            self.port.parent = self
            self.port.name = 'port'


        class Port(object):
            """
            List of client physical ports on the terminal device
            
            .. attribute:: name
            
            	Reference to the name of the client port
            	**type**\: str
            
            .. attribute:: config
            
            	Configuration data for client physical ports
            	**type**\: :py:class:`Config <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.ClientPorts.Port.Config>`
            
            .. attribute:: logical_channel_assignments
            
            	Enclosing container for client port to logical client mappings
            	**type**\: :py:class:`LogicalChannelAssignments <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.ClientPorts.Port.LogicalChannelAssignments>`
            
            .. attribute:: physical_channels
            
            	Enclosing container for client channels
            	**type**\: :py:class:`PhysicalChannels <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.ClientPorts.Port.PhysicalChannels>`
            
            .. attribute:: state
            
            	Operational state data for client physical ports
            	**type**\: :py:class:`State <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.ClientPorts.Port.State>`
            
            .. attribute:: transceiver
            
            	Top\-level container for client port transceiver data
            	**type**\: :py:class:`Transceiver <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.ClientPorts.Port.Transceiver>`
            
            

            """

            _prefix = 'opt-term'
            _revision = '2015-11-25'

            def __init__(self):
                self.parent = None
                self.name = None
                self.config = TerminalDevice.ClientPorts.Port.Config()
                self.config.parent = self
                self.logical_channel_assignments = TerminalDevice.ClientPorts.Port.LogicalChannelAssignments()
                self.logical_channel_assignments.parent = self
                self.physical_channels = TerminalDevice.ClientPorts.Port.PhysicalChannels()
                self.physical_channels.parent = self
                self.state = TerminalDevice.ClientPorts.Port.State()
                self.state.parent = self
                self.transceiver = TerminalDevice.ClientPorts.Port.Transceiver()
                self.transceiver.parent = self


            class Config(object):
                """
                Configuration data for client physical ports
                
                .. attribute:: description
                
                	Text description for the physical client port
                	**type**\: str
                
                .. attribute:: name
                
                	Name of the physical client port
                	**type**\: str
                
                

                """

                _prefix = 'opt-term'
                _revision = '2015-11-25'

                def __init__(self):
                    self.parent = None
                    self.description = None
                    self.name = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/openconfig-terminal-device:config'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.description is not None:
                        return True

                    if self.name is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_terminal_device as meta
                    return meta._meta_table['TerminalDevice.ClientPorts.Port.Config']['meta_info']


            class LogicalChannelAssignments(object):
                """
                Enclosing container for client port to logical client
                mappings
                
                .. attribute:: assignment
                
                	List of assignments to logical clients
                	**type**\: list of :py:class:`Assignment <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.ClientPorts.Port.LogicalChannelAssignments.Assignment>`
                
                

                """

                _prefix = 'opt-term'
                _revision = '2015-11-25'

                def __init__(self):
                    self.parent = None
                    self.assignment = YList()
                    self.assignment.parent = self
                    self.assignment.name = 'assignment'


                class Assignment(object):
                    """
                    List of assignments to logical clients
                    
                    .. attribute:: index
                    
                    	Reference to the index of this logical client assignment
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: config
                    
                    	Configuration data for the logical client assignment
                    	**type**\: :py:class:`Config <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.ClientPorts.Port.LogicalChannelAssignments.Assignment.Config>`
                    
                    .. attribute:: state
                    
                    	Operational state data for the logical client assignment
                    	**type**\: :py:class:`State <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.ClientPorts.Port.LogicalChannelAssignments.Assignment.State>`
                    
                    

                    """

                    _prefix = 'opt-term'
                    _revision = '2015-11-25'

                    def __init__(self):
                        self.parent = None
                        self.index = None
                        self.config = TerminalDevice.ClientPorts.Port.LogicalChannelAssignments.Assignment.Config()
                        self.config.parent = self
                        self.state = TerminalDevice.ClientPorts.Port.LogicalChannelAssignments.Assignment.State()
                        self.state.parent = self


                    class Config(object):
                        """
                        Configuration data for the logical client assignment
                        
                        .. attribute:: allocation
                        
                        	Allocation of the client physical port to the assigned logical channel expressed in Gbps.  In most cases, the full client physical port rate is assigned to a single logical channel
                        	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                        
                        	**range:** \-9223372036854775.808..9223372036854775.807
                        
                        .. attribute:: description
                        
                        	Descriptive name for the client port\-to\-logical channel mapping
                        	**type**\: str
                        
                        .. attribute:: index
                        
                        	Index of the client port assignment
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: logical_channel
                        
                        	Reference to the logical channel for this assignment
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'opt-term'
                        _revision = '2015-11-25'

                        def __init__(self):
                            self.parent = None
                            self.allocation = None
                            self.description = None
                            self.index = None
                            self.logical_channel = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/openconfig-terminal-device:config'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.allocation is not None:
                                return True

                            if self.description is not None:
                                return True

                            if self.index is not None:
                                return True

                            if self.logical_channel is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_terminal_device as meta
                            return meta._meta_table['TerminalDevice.ClientPorts.Port.LogicalChannelAssignments.Assignment.Config']['meta_info']


                    class State(object):
                        """
                        Operational state data for the logical client
                        assignment
                        
                        .. attribute:: allocation
                        
                        	Allocation of the client physical port to the assigned logical channel expressed in Gbps.  In most cases, the full client physical port rate is assigned to a single logical channel
                        	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                        
                        	**range:** \-9223372036854775.808..9223372036854775.807
                        
                        .. attribute:: description
                        
                        	Descriptive name for the client port\-to\-logical channel mapping
                        	**type**\: str
                        
                        .. attribute:: index
                        
                        	Index of the client port assignment
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: logical_channel
                        
                        	Reference to the logical channel for this assignment
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'opt-term'
                        _revision = '2015-11-25'

                        def __init__(self):
                            self.parent = None
                            self.allocation = None
                            self.description = None
                            self.index = None
                            self.logical_channel = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/openconfig-terminal-device:state'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.allocation is not None:
                                return True

                            if self.description is not None:
                                return True

                            if self.index is not None:
                                return True

                            if self.logical_channel is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_terminal_device as meta
                            return meta._meta_table['TerminalDevice.ClientPorts.Port.LogicalChannelAssignments.Assignment.State']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')
                        if self.index is None:
                            raise YPYDataValidationError('Key property index is None')

                        return self.parent._common_path +'/openconfig-terminal-device:assignment[openconfig-terminal-device:index = ' + str(self.index) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.index is not None:
                            return True

                        if self.config is not None and self.config._has_data():
                            return True

                        if self.state is not None and self.state._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_terminal_device as meta
                        return meta._meta_table['TerminalDevice.ClientPorts.Port.LogicalChannelAssignments.Assignment']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/openconfig-terminal-device:logical-channel-assignments'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.assignment is not None:
                        for child_ref in self.assignment:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_terminal_device as meta
                    return meta._meta_table['TerminalDevice.ClientPorts.Port.LogicalChannelAssignments']['meta_info']


            class PhysicalChannels(object):
                """
                Enclosing container for client channels
                
                .. attribute:: channel
                
                	List of client channels, keyed by index within a physical client port.  A physical port with a single channel would have a single zero\-indexed element
                	**type**\: list of :py:class:`Channel <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.ClientPorts.Port.PhysicalChannels.Channel>`
                
                

                """

                _prefix = 'opt-term'
                _revision = '2015-11-25'

                def __init__(self):
                    self.parent = None
                    self.channel = YList()
                    self.channel.parent = self
                    self.channel.name = 'channel'


                class Channel(object):
                    """
                    List of client channels, keyed by index within a physical
                    client port.  A physical port with a single channel would
                    have a single zero\-indexed element
                    
                    .. attribute:: index
                    
                    	Reference to the index number of the client channel
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: config
                    
                    	Configuration data 
                    	**type**\: :py:class:`Config <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.ClientPorts.Port.PhysicalChannels.Channel.Config>`
                    
                    .. attribute:: state
                    
                    	Operational state data for client channels
                    	**type**\: :py:class:`State <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.ClientPorts.Port.PhysicalChannels.Channel.State>`
                    
                    

                    """

                    _prefix = 'opt-term'
                    _revision = '2015-11-25'

                    def __init__(self):
                        self.parent = None
                        self.index = None
                        self.config = TerminalDevice.ClientPorts.Port.PhysicalChannels.Channel.Config()
                        self.config.parent = self
                        self.state = TerminalDevice.ClientPorts.Port.PhysicalChannels.Channel.State()
                        self.state.parent = self


                    class Config(object):
                        """
                        Configuration data 
                        
                        .. attribute:: description
                        
                        	Text description for the client physical channel
                        	**type**\: str
                        
                        .. attribute:: index
                        
                        	Index of the physical channnel or lane within a physical client port
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: tx_laser
                        
                        	Enable (true) or disable (false) the transmit label for the channel
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'opt-term'
                        _revision = '2015-11-25'

                        def __init__(self):
                            self.parent = None
                            self.description = None
                            self.index = None
                            self.tx_laser = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/openconfig-terminal-device:config'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.description is not None:
                                return True

                            if self.index is not None:
                                return True

                            if self.tx_laser is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_terminal_device as meta
                            return meta._meta_table['TerminalDevice.ClientPorts.Port.PhysicalChannels.Channel.Config']['meta_info']


                    class State(object):
                        """
                        Operational state data for client channels
                        
                        .. attribute:: description
                        
                        	Text description for the client physical channel
                        	**type**\: str
                        
                        .. attribute:: index
                        
                        	Index of the physical channnel or lane within a physical client port
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: output_frequency
                        
                        	The frequency in MHz of the individual physical channel (e.g. ITU C50 \- 195.0THz and would be reported as 195,000,000 MHz in this model). This attribute is not configurable on most client ports
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: output_power
                        
                        	The output optical power of this port in units of 0.01dBm. If the port is an aggregate of multiple physical channels, this attribute is the total power or sum of all channels
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: tx_laser
                        
                        	Enable (true) or disable (false) the transmit label for the channel
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'opt-term'
                        _revision = '2015-11-25'

                        def __init__(self):
                            self.parent = None
                            self.description = None
                            self.index = None
                            self.output_frequency = None
                            self.output_power = None
                            self.tx_laser = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/openconfig-terminal-device:state'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.description is not None:
                                return True

                            if self.index is not None:
                                return True

                            if self.output_frequency is not None:
                                return True

                            if self.output_power is not None:
                                return True

                            if self.tx_laser is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_terminal_device as meta
                            return meta._meta_table['TerminalDevice.ClientPorts.Port.PhysicalChannels.Channel.State']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')
                        if self.index is None:
                            raise YPYDataValidationError('Key property index is None')

                        return self.parent._common_path +'/openconfig-terminal-device:channel[openconfig-terminal-device:index = ' + str(self.index) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.index is not None:
                            return True

                        if self.config is not None and self.config._has_data():
                            return True

                        if self.state is not None and self.state._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_terminal_device as meta
                        return meta._meta_table['TerminalDevice.ClientPorts.Port.PhysicalChannels.Channel']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/openconfig-terminal-device:physical-channels'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.channel is not None:
                        for child_ref in self.channel:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_terminal_device as meta
                    return meta._meta_table['TerminalDevice.ClientPorts.Port.PhysicalChannels']['meta_info']


            class State(object):
                """
                Operational state data for client physical ports
                
                .. attribute:: description
                
                	Text description for the physical client port
                	**type**\: str
                
                .. attribute:: ethernet_compliance_code
                
                	Ethernet PMD that the transceiver supports. The SFF/QSFP MSAs have registers for this and CFP MSA has similar
                	**type**\: :py:class:`EthernetPmdType_Identity <ydk.models.openconfig.openconfig_transport_types.EthernetPmdType_Identity>`
                
                .. attribute:: input_power
                
                	The input optical power of this port in units of 0.01dBm. If the port is an aggregate of multiple physical channels, this attribute is the total power or sum of all channels
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: name
                
                	Name of the physical client port
                	**type**\: str
                
                .. attribute:: otn_compliance_code
                
                	OTN application code supported by the port
                	**type**\: :py:class:`OtnApplicationCode_Identity <ydk.models.openconfig.openconfig_transport_types.OtnApplicationCode_Identity>`
                
                .. attribute:: output_power
                
                	The output optical power of this port in units of 0.01dBm. If the port is an aggregate of multiple physical channels, this attribute is the total power or sum of all channels
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: sonet_sdh_compliance_code
                
                	SONET/SDH application code supported by the port
                	**type**\: :py:class:`SonetApplicationCode_Identity <ydk.models.openconfig.openconfig_transport_types.SonetApplicationCode_Identity>`
                
                

                """

                _prefix = 'opt-term'
                _revision = '2015-11-25'

                def __init__(self):
                    self.parent = None
                    self.description = None
                    self.ethernet_compliance_code = None
                    self.input_power = None
                    self.name = None
                    self.otn_compliance_code = None
                    self.output_power = None
                    self.sonet_sdh_compliance_code = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/openconfig-terminal-device:state'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.description is not None:
                        return True

                    if self.ethernet_compliance_code is not None:
                        return True

                    if self.input_power is not None:
                        return True

                    if self.name is not None:
                        return True

                    if self.otn_compliance_code is not None:
                        return True

                    if self.output_power is not None:
                        return True

                    if self.sonet_sdh_compliance_code is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_terminal_device as meta
                    return meta._meta_table['TerminalDevice.ClientPorts.Port.State']['meta_info']


            class Transceiver(object):
                """
                Top\-level container for client port transceiver data
                
                .. attribute:: config
                
                	Configuration data for client port transceivers
                	**type**\: :py:class:`Config <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.ClientPorts.Port.Transceiver.Config>`
                
                .. attribute:: state
                
                	Operational state data for client port transceivers
                	**type**\: :py:class:`State <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.ClientPorts.Port.Transceiver.State>`
                
                

                """

                _prefix = 'opt-term'
                _revision = '2015-11-25'

                def __init__(self):
                    self.parent = None
                    self.config = TerminalDevice.ClientPorts.Port.Transceiver.Config()
                    self.config.parent = self
                    self.state = TerminalDevice.ClientPorts.Port.Transceiver.State()
                    self.state.parent = self


                class Config(object):
                    """
                    Configuration data for client port transceivers
                    
                    .. attribute:: enabled
                    
                    	Turns power on / off to the transceiver \-\- provides a means to power on/off the transceiver (in the case of SFP, SFP+, QSFP,...) or enable high\-power mode (in the case of CFP, CFP2, CFP4) and is optionally supported (device can choose to always enable).  True = power on / high power, False = powered off
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'opt-term'
                    _revision = '2015-11-25'

                    def __init__(self):
                        self.parent = None
                        self.enabled = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-terminal-device:config'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.enabled is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_terminal_device as meta
                        return meta._meta_table['TerminalDevice.ClientPorts.Port.Transceiver.Config']['meta_info']


                class State(object):
                    """
                    Operational state data for client port transceivers
                    
                    .. attribute:: connector_type
                    
                    	Connector type used on this port
                    	**type**\: :py:class:`FiberConnectorType_Identity <ydk.models.openconfig.openconfig_transport_types.FiberConnectorType_Identity>`
                    
                    .. attribute:: date_code
                    
                    	Representation of the transceiver date code, typically stored as YYMMDD.  The time portion of the value is undefined and not intended to be read
                    	**type**\: str
                    
                    	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                    
                    .. attribute:: enabled
                    
                    	Turns power on / off to the transceiver \-\- provides a means to power on/off the transceiver (in the case of SFP, SFP+, QSFP,...) or enable high\-power mode (in the case of CFP, CFP2, CFP4) and is optionally supported (device can choose to always enable).  True = power on / high power, False = powered off
                    	**type**\: bool
                    
                    .. attribute:: fault_condition
                    
                    	Indicates if a fault condition exists in the transceiver
                    	**type**\: bool
                    
                    .. attribute:: form_factor
                    
                    	Indicates the type of optical transceiver used on this port.  If the client port is built into the device and not plugable, then non\-pluggable is the corresponding state. If a device port supports multiple form factors (e.g. QSFP28 and QSFP+, then the value of the transceiver installed shall be reported. If no transceiver is present, then the value of the highest rate form factor shall be reported (QSFP28, for example)
                    	**type**\: :py:class:`TransceiverFormFactorType_Identity <ydk.models.openconfig.openconfig_transport_types.TransceiverFormFactorType_Identity>`
                    
                    .. attribute:: internal_temp
                    
                    	Internally measured temperature in degrees Celsius. MSA valid range is between \-40 and +125C. Accuracy shall be better than +/\- 3 degC over the whole temperature range
                    	**type**\: int
                    
                    	**range:** \-40..125
                    
                    .. attribute:: present
                    
                    	Indicates whether a transceiver is present in the specified client port
                    	**type**\: :py:class:`PresentEnum <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.ClientPorts.Port.Transceiver.State.PresentEnum>`
                    
                    .. attribute:: serial_no
                    
                    	Transceiver serial number. 16\-octet field that contains ASCII characters, left\-aligned and padded on the right with ASCII spaces (20h). If part serial number is undefined, all 16 octets = 0h
                    	**type**\: str
                    
                    	**range:** 1..16
                    
                    .. attribute:: vendor
                    
                    	Full name of transceiver vendor. 16\-octet field that contains ASCII characters, left\-aligned and padded on the right with ASCII spaces (20h)
                    	**type**\: str
                    
                    	**range:** 1..16
                    
                    .. attribute:: vendor_part
                    
                    	Transceiver vendor's part number. 16\-octet field that contains ASCII characters, left\-aligned and padded on the right with ASCII spaces (20h). If part number is undefined, all 16 octets = 0h
                    	**type**\: str
                    
                    	**range:** 1..16
                    
                    .. attribute:: vendor_rev
                    
                    	Transceiver vendor's revision number. 2\-octet field that contains ASCII characters, left\-aligned and padded on the right with ASCII spaces (20h)
                    	**type**\: str
                    
                    	**range:** 1..2
                    
                    

                    """

                    _prefix = 'opt-term'
                    _revision = '2015-11-25'

                    def __init__(self):
                        self.parent = None
                        self.connector_type = None
                        self.date_code = None
                        self.enabled = None
                        self.fault_condition = None
                        self.form_factor = None
                        self.internal_temp = None
                        self.present = None
                        self.serial_no = None
                        self.vendor = None
                        self.vendor_part = None
                        self.vendor_rev = None

                    class PresentEnum(Enum):
                        """
                        PresentEnum

                        Indicates whether a transceiver is present in

                        the specified client port.

                        .. data:: PRESENT = 0

                        	Transceiver is present on the port

                        .. data:: NOT_PRESENT = 1

                        	Transceiver is not present on the port

                        """

                        PRESENT = 0

                        NOT_PRESENT = 1


                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_terminal_device as meta
                            return meta._meta_table['TerminalDevice.ClientPorts.Port.Transceiver.State.PresentEnum']


                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-terminal-device:state'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.connector_type is not None:
                            return True

                        if self.date_code is not None:
                            return True

                        if self.enabled is not None:
                            return True

                        if self.fault_condition is not None:
                            return True

                        if self.form_factor is not None:
                            return True

                        if self.internal_temp is not None:
                            return True

                        if self.present is not None:
                            return True

                        if self.serial_no is not None:
                            return True

                        if self.vendor is not None:
                            return True

                        if self.vendor_part is not None:
                            return True

                        if self.vendor_rev is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_terminal_device as meta
                        return meta._meta_table['TerminalDevice.ClientPorts.Port.Transceiver.State']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/openconfig-terminal-device:transceiver'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.config is not None and self.config._has_data():
                        return True

                    if self.state is not None and self.state._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_terminal_device as meta
                    return meta._meta_table['TerminalDevice.ClientPorts.Port.Transceiver']['meta_info']

            @property
            def _common_path(self):
                if self.name is None:
                    raise YPYDataValidationError('Key property name is None')

                return '/openconfig-terminal-device:terminal-device/openconfig-terminal-device:client-ports/openconfig-terminal-device:port[openconfig-terminal-device:name = ' + str(self.name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.name is not None:
                    return True

                if self.config is not None and self.config._has_data():
                    return True

                if self.logical_channel_assignments is not None and self.logical_channel_assignments._has_data():
                    return True

                if self.physical_channels is not None and self.physical_channels._has_data():
                    return True

                if self.state is not None and self.state._has_data():
                    return True

                if self.transceiver is not None and self.transceiver._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.openconfig._meta import _openconfig_terminal_device as meta
                return meta._meta_table['TerminalDevice.ClientPorts.Port']['meta_info']

        @property
        def _common_path(self):

            return '/openconfig-terminal-device:terminal-device/openconfig-terminal-device:client-ports'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.port is not None:
                for child_ref in self.port:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.openconfig._meta import _openconfig_terminal_device as meta
            return meta._meta_table['TerminalDevice.ClientPorts']['meta_info']


    class Config(object):
        """
        Configuration data for global terminal\-device
        
        

        """

        _prefix = 'opt-term'
        _revision = '2015-11-25'

        def __init__(self):
            self.parent = None

        @property
        def _common_path(self):

            return '/openconfig-terminal-device:terminal-device/openconfig-terminal-device:config'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.openconfig._meta import _openconfig_terminal_device as meta
            return meta._meta_table['TerminalDevice.Config']['meta_info']


    class LinePorts(object):
        """
        Enclosing container for line ports
        
        .. attribute:: port
        
        	List of line ports
        	**type**\: list of :py:class:`Port <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LinePorts.Port>`
        
        

        """

        _prefix = 'opt-term'
        _revision = '2015-11-25'

        def __init__(self):
            self.parent = None
            self.port = YList()
            self.port.parent = self
            self.port.name = 'port'


        class Port(object):
            """
            List of line ports
            
            .. attribute:: name
            
            	Reference to the name of the line port
            	**type**\: str
            
            .. attribute:: config
            
            	Configuration data for each physical line port
            	**type**\: :py:class:`Config <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LinePorts.Port.Config>`
            
            .. attribute:: state
            
            	Operational state data for each physical line port
            	**type**\: :py:class:`State <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LinePorts.Port.State>`
            
            

            """

            _prefix = 'opt-term'
            _revision = '2015-11-25'

            def __init__(self):
                self.parent = None
                self.name = None
                self.config = TerminalDevice.LinePorts.Port.Config()
                self.config.parent = self
                self.state = TerminalDevice.LinePorts.Port.State()
                self.state.parent = self


            class Config(object):
                """
                Configuration data for each physical line port
                
                .. attribute:: name
                
                	Name of the line port
                	**type**\: str
                
                .. attribute:: output_power
                
                	The output optical power of this port in units of 0.01dBm. If the port is an aggregate of multiple physical channels, this attribute is the total power or sum of all channels
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'opt-term'
                _revision = '2015-11-25'

                def __init__(self):
                    self.parent = None
                    self.name = None
                    self.output_power = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/openconfig-terminal-device:config'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.name is not None:
                        return True

                    if self.output_power is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_terminal_device as meta
                    return meta._meta_table['TerminalDevice.LinePorts.Port.Config']['meta_info']


            class State(object):
                """
                Operational state data for each physical line port
                
                .. attribute:: name
                
                	Name of the line port
                	**type**\: str
                
                .. attribute:: output_power
                
                	The output optical power of this port in units of 0.01dBm. If the port is an aggregate of multiple physical channels, this attribute is the total power or sum of all channels
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'opt-term'
                _revision = '2015-11-25'

                def __init__(self):
                    self.parent = None
                    self.name = None
                    self.output_power = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/openconfig-terminal-device:state'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.name is not None:
                        return True

                    if self.output_power is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_terminal_device as meta
                    return meta._meta_table['TerminalDevice.LinePorts.Port.State']['meta_info']

            @property
            def _common_path(self):
                if self.name is None:
                    raise YPYDataValidationError('Key property name is None')

                return '/openconfig-terminal-device:terminal-device/openconfig-terminal-device:line-ports/openconfig-terminal-device:port[openconfig-terminal-device:name = ' + str(self.name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.name is not None:
                    return True

                if self.config is not None and self.config._has_data():
                    return True

                if self.state is not None and self.state._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.openconfig._meta import _openconfig_terminal_device as meta
                return meta._meta_table['TerminalDevice.LinePorts.Port']['meta_info']

        @property
        def _common_path(self):

            return '/openconfig-terminal-device:terminal-device/openconfig-terminal-device:line-ports'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.port is not None:
                for child_ref in self.port:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.openconfig._meta import _openconfig_terminal_device as meta
            return meta._meta_table['TerminalDevice.LinePorts']['meta_info']


    class LogicalChannels(object):
        """
        Enclosing container the list of logical channels
        
        .. attribute:: channel
        
        	List of logical channels
        	**type**\: list of :py:class:`Channel <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel>`
        
        

        """

        _prefix = 'opt-term'
        _revision = '2015-11-25'

        def __init__(self):
            self.parent = None
            self.channel = YList()
            self.channel.parent = self
            self.channel.name = 'channel'


        class Channel(object):
            """
            List of logical channels
            
            .. attribute:: index
            
            	Reference to the index of the logical client channel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: config
            
            	Configuration data for logical client channels
            	**type**\: :py:class:`Config <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel.Config>`
            
            .. attribute:: logical_channel_assignments
            
            	Enclosing container for tributary assignments
            	**type**\: :py:class:`LogicalChannelAssignments <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments>`
            
            .. attribute:: state
            
            	Operational state data for logical client channels
            	**type**\: :py:class:`State <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel.State>`
            
            

            """

            _prefix = 'opt-term'
            _revision = '2015-11-25'

            def __init__(self):
                self.parent = None
                self.index = None
                self.config = TerminalDevice.LogicalChannels.Channel.Config()
                self.config.parent = self
                self.logical_channel_assignments = TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments()
                self.logical_channel_assignments.parent = self
                self.state = TerminalDevice.LogicalChannels.Channel.State()
                self.state.parent = self


            class Config(object):
                """
                Configuration data for logical client channels
                
                .. attribute:: description
                
                	Description of the client logical channel
                	**type**\: str
                
                .. attribute:: index
                
                	Index of the current logical client channel
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: protocol_type
                
                	The type / stage of the logical element determines the configuration and operational state parameters (PMs) available for the logical element
                	**type**\: :py:class:`LogicalElementProtocolType_Identity <ydk.models.openconfig.openconfig_transport_types.LogicalElementProtocolType_Identity>`
                
                .. attribute:: trib_protocol
                
                	Protocol framing of the tributary signal. If this LogicalChannel is directly connected to a Client\-Port or Optical\-Channel, this is the protocol of the associated port. If the LogicalChannel is connected to other LogicalChannels, the TributaryProtocol of the LogicalChannels will define a specific mapping/demapping or multiplexing/demultiplexing function.  Not all protocols are valid, depending on the value of trib\-rate\-class.  The expectation is that the NMS will validate that a correct combination of rate class and protocol are specfied.  Basic combinations are\:  rate class\: 1G protocols\: 1GE  rate class\: 2.5G protocols\: OC48, STM16  rate class\: 10G protocols\:  10GE LAN, 10GE WAN, OC192, STM64, OTU2, OTU2e,            OTU1e, ODU2, ODU2e, ODU1e  rate class\: 40G protocols\:  40GE, OC768, STM256, OTU3, ODU3  rate class\: 100G protocols\:  100GE, 100G MLG, OTU4, OTUCn, ODU4
                	**type**\: :py:class:`TributaryProtocolType_Identity <ydk.models.openconfig.openconfig_transport_types.TributaryProtocolType_Identity>`
                
                .. attribute:: trib_rate_class
                
                	Rounded bit rate of the tributary signal. Exact bit rate will be refined by protocol selection
                	**type**\: :py:class:`TributaryRateClassType_Identity <ydk.models.openconfig.openconfig_transport_types.TributaryRateClassType_Identity>`
                
                

                """

                _prefix = 'opt-term'
                _revision = '2015-11-25'

                def __init__(self):
                    self.parent = None
                    self.description = None
                    self.index = None
                    self.protocol_type = None
                    self.trib_protocol = None
                    self.trib_rate_class = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/openconfig-terminal-device:config'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.description is not None:
                        return True

                    if self.index is not None:
                        return True

                    if self.protocol_type is not None:
                        return True

                    if self.trib_protocol is not None:
                        return True

                    if self.trib_rate_class is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_terminal_device as meta
                    return meta._meta_table['TerminalDevice.LogicalChannels.Channel.Config']['meta_info']


            class LogicalChannelAssignments(object):
                """
                Enclosing container for tributary assignments
                
                .. attribute:: assignment
                
                	Logical channel elements may be assigned directly to optical channels for line\-side transmission, or can be further groomed into additional stages of logical channel elements.  The grooming can multiplex (i.e., split the current element into multiple elements in the subsequent stage) or de\-multiplex (i.e., combine the current element with other elements into the same element in the subsequent stage) logical elements in each stage.  Note that to support the ability to groom the logical elements, the list of logical channel elements should be populated with an entry for the logical elements at each stage, starting with the initial assignment from the respective client physical port.  Each logical element assignment consists of a pointer to an element in the next stage, or to an optical channel, along with a bandwidth allocation for the corresponding assignment (e.g., to split or combine signal)
                	**type**\: list of :py:class:`Assignment <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment>`
                
                

                """

                _prefix = 'opt-term'
                _revision = '2015-11-25'

                def __init__(self):
                    self.parent = None
                    self.assignment = YList()
                    self.assignment.parent = self
                    self.assignment.name = 'assignment'


                class Assignment(object):
                    """
                    Logical channel elements may be assigned directly to
                    optical channels for line\-side transmission, or can be
                    further groomed into additional stages of logical channel
                    elements.  The grooming can multiplex (i.e., split the
                    current element into multiple elements in the subsequent
                    stage) or de\-multiplex (i.e., combine the current element
                    with other elements into the same element in the subsequent
                    stage) logical elements in each stage.
                    
                    Note that to support the ability to groom the logical
                    elements, the list of logical channel elements should be
                    populated with an entry for the logical elements at
                    each stage, starting with the initial assignment from the
                    respective client physical port.
                    
                    Each logical element assignment consists of a pointer to
                    an element in the next stage, or to an optical channel,
                    along with a bandwidth allocation for the corresponding
                    assignment (e.g., to split or combine signal).
                    
                    .. attribute:: index
                    
                    	Reference to the index for the current tributary assignment
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: config
                    
                    	Configuration data for tributary assignments
                    	**type**\: :py:class:`Config <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment.Config>`
                    
                    .. attribute:: state
                    
                    	Operational state data for tributary assignments
                    	**type**\: :py:class:`State <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment.State>`
                    
                    

                    """

                    _prefix = 'opt-term'
                    _revision = '2015-11-25'

                    def __init__(self):
                        self.parent = None
                        self.index = None
                        self.config = TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment.Config()
                        self.config.parent = self
                        self.state = TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment.State()
                        self.state.parent = self


                    class Config(object):
                        """
                        Configuration data for tributary assignments
                        
                        .. attribute:: allocation
                        
                        	Allocation of the logical client channel to the tributary or sub\-channel, expressed in Gbps
                        	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                        
                        	**range:** \-9223372036854775.808..9223372036854775.807
                        
                        .. attribute:: description
                        
                        	Name assigned to the logical client channel
                        	**type**\: str
                        
                        .. attribute:: index
                        
                        	Index of the current logical client channel to tributary mapping
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: logical_channel
                        
                        	Reference to another stage of logical channel elements
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: optical_channel
                        
                        	Reference to the line\-side optical channel that should carry the current logical channel element.  Use this reference to exit the logical element stage
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'opt-term'
                        _revision = '2015-11-25'

                        def __init__(self):
                            self.parent = None
                            self.allocation = None
                            self.description = None
                            self.index = None
                            self.logical_channel = None
                            self.optical_channel = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/openconfig-terminal-device:config'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.allocation is not None:
                                return True

                            if self.description is not None:
                                return True

                            if self.index is not None:
                                return True

                            if self.logical_channel is not None:
                                return True

                            if self.optical_channel is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_terminal_device as meta
                            return meta._meta_table['TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment.Config']['meta_info']


                    class State(object):
                        """
                        Operational state data for tributary assignments
                        
                        .. attribute:: allocation
                        
                        	Allocation of the logical client channel to the tributary or sub\-channel, expressed in Gbps
                        	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                        
                        	**range:** \-9223372036854775.808..9223372036854775.807
                        
                        .. attribute:: description
                        
                        	Name assigned to the logical client channel
                        	**type**\: str
                        
                        .. attribute:: index
                        
                        	Index of the current logical client channel to tributary mapping
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: logical_channel
                        
                        	Reference to another stage of logical channel elements
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: optical_channel
                        
                        	Reference to the line\-side optical channel that should carry the current logical channel element.  Use this reference to exit the logical element stage
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'opt-term'
                        _revision = '2015-11-25'

                        def __init__(self):
                            self.parent = None
                            self.allocation = None
                            self.description = None
                            self.index = None
                            self.logical_channel = None
                            self.optical_channel = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/openconfig-terminal-device:state'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.allocation is not None:
                                return True

                            if self.description is not None:
                                return True

                            if self.index is not None:
                                return True

                            if self.logical_channel is not None:
                                return True

                            if self.optical_channel is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_terminal_device as meta
                            return meta._meta_table['TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment.State']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')
                        if self.index is None:
                            raise YPYDataValidationError('Key property index is None')

                        return self.parent._common_path +'/openconfig-terminal-device:assignment[openconfig-terminal-device:index = ' + str(self.index) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.index is not None:
                            return True

                        if self.config is not None and self.config._has_data():
                            return True

                        if self.state is not None and self.state._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_terminal_device as meta
                        return meta._meta_table['TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/openconfig-terminal-device:logical-channel-assignments'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.assignment is not None:
                        for child_ref in self.assignment:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_terminal_device as meta
                    return meta._meta_table['TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments']['meta_info']


            class State(object):
                """
                Operational state data for logical client channels
                
                .. attribute:: description
                
                	Description of the client logical channel
                	**type**\: str
                
                .. attribute:: ethernet
                
                	PMs and counters for Ethernet protocol channels
                	**type**\: :py:class:`Ethernet <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel.State.Ethernet>`
                
                .. attribute:: index
                
                	Index of the current logical client channel
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: link_state
                
                	Link\-state of the Ethernet protocol on the logical channel, SONET / SDH framed signal, etc
                	**type**\: :py:class:`LinkStateEnum <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel.State.LinkStateEnum>`
                
                .. attribute:: otn
                
                	PMs and statistics for OTN protocol channels
                	**type**\: :py:class:`Otn <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel.State.Otn>`
                
                .. attribute:: protocol_type
                
                	The type / stage of the logical element determines the configuration and operational state parameters (PMs) available for the logical element
                	**type**\: :py:class:`LogicalElementProtocolType_Identity <ydk.models.openconfig.openconfig_transport_types.LogicalElementProtocolType_Identity>`
                
                .. attribute:: trib_protocol
                
                	Protocol framing of the tributary signal. If this LogicalChannel is directly connected to a Client\-Port or Optical\-Channel, this is the protocol of the associated port. If the LogicalChannel is connected to other LogicalChannels, the TributaryProtocol of the LogicalChannels will define a specific mapping/demapping or multiplexing/demultiplexing function.  Not all protocols are valid, depending on the value of trib\-rate\-class.  The expectation is that the NMS will validate that a correct combination of rate class and protocol are specfied.  Basic combinations are\:  rate class\: 1G protocols\: 1GE  rate class\: 2.5G protocols\: OC48, STM16  rate class\: 10G protocols\:  10GE LAN, 10GE WAN, OC192, STM64, OTU2, OTU2e,            OTU1e, ODU2, ODU2e, ODU1e  rate class\: 40G protocols\:  40GE, OC768, STM256, OTU3, ODU3  rate class\: 100G protocols\:  100GE, 100G MLG, OTU4, OTUCn, ODU4
                	**type**\: :py:class:`TributaryProtocolType_Identity <ydk.models.openconfig.openconfig_transport_types.TributaryProtocolType_Identity>`
                
                .. attribute:: trib_rate_class
                
                	Rounded bit rate of the tributary signal. Exact bit rate will be refined by protocol selection
                	**type**\: :py:class:`TributaryRateClassType_Identity <ydk.models.openconfig.openconfig_transport_types.TributaryRateClassType_Identity>`
                
                

                """

                _prefix = 'opt-term'
                _revision = '2015-11-25'

                def __init__(self):
                    self.parent = None
                    self.description = None
                    self.ethernet = TerminalDevice.LogicalChannels.Channel.State.Ethernet()
                    self.ethernet.parent = self
                    self.index = None
                    self.link_state = None
                    self.otn = TerminalDevice.LogicalChannels.Channel.State.Otn()
                    self.otn.parent = self
                    self.protocol_type = None
                    self.trib_protocol = None
                    self.trib_rate_class = None

                class LinkStateEnum(Enum):
                    """
                    LinkStateEnum

                    Link\-state of the Ethernet protocol on the logical channel,

                    SONET / SDH framed signal, etc.

                    .. data:: UP = 0

                    	Logical channel is operationally up

                    .. data:: DOWN = 1

                    	Logical channel is operationally down

                    """

                    UP = 0

                    DOWN = 1


                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_terminal_device as meta
                        return meta._meta_table['TerminalDevice.LogicalChannels.Channel.State.LinkStateEnum']



                class Ethernet(object):
                    """
                    PMs and counters for Ethernet protocol channels
                    
                    .. attribute:: in_8021q_frames
                    
                    	Number of 802.1q tagged frames received on the interface
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: in_crc_errors
                    
                    	Number of receive error events due to FCS/CRC check failure
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: in_fragment_frames
                    
                    	Number of fragment frames received on the interface
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: in_jabber_frames
                    
                    	Number of jabber frames received on the interface.  Jabber frames are typically defined as oversize frames which also have a bad CRC.  Implementations may use slightly different definitions of what constitutes a jabber frame.  Often indicative of a NIC hardware problem
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: in_mac_control_frames
                    
                    	MAC layer control frames received on the interface
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: in_mac_pause_frames
                    
                    	MAC layer PAUSE frames received on the interface
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: in_oversize_frames
                    
                    	Number of oversize frames received on the interface
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: out_8021q_frames
                    
                    	Number of 802.1q tagged frames sent on the interface
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: out_mac_control_frames
                    
                    	MAC layer control frames sent on the interface
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: out_mac_pause_frames
                    
                    	MAC layer PAUSE frames sent on the interface
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'opt-term'
                    _revision = '2015-11-25'

                    def __init__(self):
                        self.parent = None
                        self.in_8021q_frames = None
                        self.in_crc_errors = None
                        self.in_fragment_frames = None
                        self.in_jabber_frames = None
                        self.in_mac_control_frames = None
                        self.in_mac_pause_frames = None
                        self.in_oversize_frames = None
                        self.out_8021q_frames = None
                        self.out_mac_control_frames = None
                        self.out_mac_pause_frames = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-terminal-device:ethernet'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.in_8021q_frames is not None:
                            return True

                        if self.in_crc_errors is not None:
                            return True

                        if self.in_fragment_frames is not None:
                            return True

                        if self.in_jabber_frames is not None:
                            return True

                        if self.in_mac_control_frames is not None:
                            return True

                        if self.in_mac_pause_frames is not None:
                            return True

                        if self.in_oversize_frames is not None:
                            return True

                        if self.out_8021q_frames is not None:
                            return True

                        if self.out_mac_control_frames is not None:
                            return True

                        if self.out_mac_pause_frames is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_terminal_device as meta
                        return meta._meta_table['TerminalDevice.LogicalChannels.Channel.State.Ethernet']['meta_info']


                class Otn(object):
                    """
                    PMs and statistics for OTN protocol channels
                    
                    .. attribute:: post_fec_ber
                    
                    	Bit error rate after forward error correction \-\- computed value
                    	**type**\: :py:class:`PostFecBer <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel.State.Otn.PostFecBer>`
                    
                    .. attribute:: pre_fec_ber
                    
                    	Bit error rate before forward error correction \-\- computed value
                    	**type**\: :py:class:`PreFecBer <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel.State.Otn.PreFecBer>`
                    
                    .. attribute:: rdi_msg
                    
                    	Remote defect indication (RDI) message received
                    	**type**\: str
                    
                    .. attribute:: tti_msg
                    
                    	Trail trace identifier (TTI) message received
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'opt-term'
                    _revision = '2015-11-25'

                    def __init__(self):
                        self.parent = None
                        self.post_fec_ber = TerminalDevice.LogicalChannels.Channel.State.Otn.PostFecBer()
                        self.post_fec_ber.parent = self
                        self.pre_fec_ber = TerminalDevice.LogicalChannels.Channel.State.Otn.PreFecBer()
                        self.pre_fec_ber.parent = self
                        self.rdi_msg = None
                        self.tti_msg = None


                    class PostFecBer(object):
                        """
                        Bit error rate after forward error correction \-\- computed
                        value
                        
                        .. attribute:: avg
                        
                        	The arithmetic mean value of the statistic over the sampling period
                        	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                        
                        	**range:** \-922337203685477580.8..922337203685477580.7
                        
                        .. attribute:: max
                        
                        	The maximum value of the statitic over the sampling period
                        	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                        
                        	**range:** \-922337203685477580.8..922337203685477580.7
                        
                        .. attribute:: min
                        
                        	The minimum value of the statistic over the sampling period
                        	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                        
                        	**range:** \-922337203685477580.8..922337203685477580.7
                        
                        

                        """

                        _prefix = 'opt-term'
                        _revision = '2015-11-25'

                        def __init__(self):
                            self.parent = None
                            self.avg = None
                            self.max = None
                            self.min = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/openconfig-terminal-device:post-fec-ber'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.avg is not None:
                                return True

                            if self.max is not None:
                                return True

                            if self.min is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_terminal_device as meta
                            return meta._meta_table['TerminalDevice.LogicalChannels.Channel.State.Otn.PostFecBer']['meta_info']


                    class PreFecBer(object):
                        """
                        Bit error rate before forward error correction \-\- computed
                        value
                        
                        .. attribute:: avg
                        
                        	The arithmetic mean value of the statistic over the sampling period
                        	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                        
                        	**range:** \-922337203685477580.8..922337203685477580.7
                        
                        .. attribute:: max
                        
                        	The maximum value of the statitic over the sampling period
                        	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                        
                        	**range:** \-922337203685477580.8..922337203685477580.7
                        
                        .. attribute:: min
                        
                        	The minimum value of the statistic over the sampling period
                        	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                        
                        	**range:** \-922337203685477580.8..922337203685477580.7
                        
                        

                        """

                        _prefix = 'opt-term'
                        _revision = '2015-11-25'

                        def __init__(self):
                            self.parent = None
                            self.avg = None
                            self.max = None
                            self.min = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/openconfig-terminal-device:pre-fec-ber'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.avg is not None:
                                return True

                            if self.max is not None:
                                return True

                            if self.min is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_terminal_device as meta
                            return meta._meta_table['TerminalDevice.LogicalChannels.Channel.State.Otn.PreFecBer']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-terminal-device:otn'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.post_fec_ber is not None and self.post_fec_ber._has_data():
                            return True

                        if self.pre_fec_ber is not None and self.pre_fec_ber._has_data():
                            return True

                        if self.rdi_msg is not None:
                            return True

                        if self.tti_msg is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_terminal_device as meta
                        return meta._meta_table['TerminalDevice.LogicalChannels.Channel.State.Otn']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/openconfig-terminal-device:state'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.description is not None:
                        return True

                    if self.ethernet is not None and self.ethernet._has_data():
                        return True

                    if self.index is not None:
                        return True

                    if self.link_state is not None:
                        return True

                    if self.otn is not None and self.otn._has_data():
                        return True

                    if self.protocol_type is not None:
                        return True

                    if self.trib_protocol is not None:
                        return True

                    if self.trib_rate_class is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_terminal_device as meta
                    return meta._meta_table['TerminalDevice.LogicalChannels.Channel.State']['meta_info']

            @property
            def _common_path(self):
                if self.index is None:
                    raise YPYDataValidationError('Key property index is None')

                return '/openconfig-terminal-device:terminal-device/openconfig-terminal-device:logical-channels/openconfig-terminal-device:channel[openconfig-terminal-device:index = ' + str(self.index) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.index is not None:
                    return True

                if self.config is not None and self.config._has_data():
                    return True

                if self.logical_channel_assignments is not None and self.logical_channel_assignments._has_data():
                    return True

                if self.state is not None and self.state._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.openconfig._meta import _openconfig_terminal_device as meta
                return meta._meta_table['TerminalDevice.LogicalChannels.Channel']['meta_info']

        @property
        def _common_path(self):

            return '/openconfig-terminal-device:terminal-device/openconfig-terminal-device:logical-channels'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.channel is not None:
                for child_ref in self.channel:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.openconfig._meta import _openconfig_terminal_device as meta
            return meta._meta_table['TerminalDevice.LogicalChannels']['meta_info']


    class OperationalModes(object):
        """
        Top\-level container for vendor\-specific operational mode
        information
        
        .. attribute:: config
        
        	Configuration data for operational modes.  This should generally be empty, i.e., operational mode information is supplied by the platform vendor and is expected to be read\-only
        	**type**\: :py:class:`Config <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.OperationalModes.Config>`
        
        .. attribute:: state
        
        	Operational state data for vendor\-specific operational modes
        	**type**\: :py:class:`State <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.OperationalModes.State>`
        
        

        """

        _prefix = 'opt-term'
        _revision = '2015-11-25'

        def __init__(self):
            self.parent = None
            self.config = TerminalDevice.OperationalModes.Config()
            self.config.parent = self
            self.state = TerminalDevice.OperationalModes.State()
            self.state.parent = self


        class Config(object):
            """
            Configuration data for operational modes.  This should
            generally be empty, i.e., operational mode information
            is supplied by the platform vendor and is expected to be
            read\-only
            
            

            """

            _prefix = 'opt-term'
            _revision = '2015-11-25'

            def __init__(self):
                self.parent = None

            @property
            def _common_path(self):

                return '/openconfig-terminal-device:terminal-device/openconfig-terminal-device:operational-modes/openconfig-terminal-device:config'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.openconfig._meta import _openconfig_terminal_device as meta
                return meta._meta_table['TerminalDevice.OperationalModes.Config']['meta_info']


        class State(object):
            """
            Operational state data for vendor\-specific operational
            modes
            
            .. attribute:: supported_modes
            
            	List of supported modes and their associated metadata
            	**type**\: list of :py:class:`SupportedModes <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.OperationalModes.State.SupportedModes>`
            
            

            """

            _prefix = 'opt-term'
            _revision = '2015-11-25'

            def __init__(self):
                self.parent = None
                self.supported_modes = YList()
                self.supported_modes.parent = self
                self.supported_modes.name = 'supported_modes'


            class SupportedModes(object):
                """
                List of supported modes and their associated metadata
                
                .. attribute:: mode_id
                
                	Two\-octet encoding of the vendor\-defined operational mode
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: description
                
                	Vendor\-supplied textual description of the characteristics of this operational mode to enable operators to select the appropriate mode for the application
                	**type**\: str
                
                .. attribute:: vendor_id
                
                	Identifier to represent the vendor / supplier of the platform and the associated operational mode information
                	**type**\: str
                
                

                """

                _prefix = 'opt-term'
                _revision = '2015-11-25'

                def __init__(self):
                    self.parent = None
                    self.mode_id = None
                    self.description = None
                    self.vendor_id = None

                @property
                def _common_path(self):
                    if self.mode_id is None:
                        raise YPYDataValidationError('Key property mode_id is None')

                    return '/openconfig-terminal-device:terminal-device/openconfig-terminal-device:operational-modes/openconfig-terminal-device:state/openconfig-terminal-device:supported-modes[openconfig-terminal-device:mode-id = ' + str(self.mode_id) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.mode_id is not None:
                        return True

                    if self.description is not None:
                        return True

                    if self.vendor_id is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_terminal_device as meta
                    return meta._meta_table['TerminalDevice.OperationalModes.State.SupportedModes']['meta_info']

            @property
            def _common_path(self):

                return '/openconfig-terminal-device:terminal-device/openconfig-terminal-device:operational-modes/openconfig-terminal-device:state'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.supported_modes is not None:
                    for child_ref in self.supported_modes:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.openconfig._meta import _openconfig_terminal_device as meta
                return meta._meta_table['TerminalDevice.OperationalModes.State']['meta_info']

        @property
        def _common_path(self):

            return '/openconfig-terminal-device:terminal-device/openconfig-terminal-device:operational-modes'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.config is not None and self.config._has_data():
                return True

            if self.state is not None and self.state._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.openconfig._meta import _openconfig_terminal_device as meta
            return meta._meta_table['TerminalDevice.OperationalModes']['meta_info']


    class OpticalChannels(object):
        """
        Enclosing container 
        
        .. attribute:: optical_channel
        
        	List of 
        	**type**\: list of :py:class:`OpticalChannel <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.OpticalChannels.OpticalChannel>`
        
        

        """

        _prefix = 'opt-term'
        _revision = '2015-11-25'

        def __init__(self):
            self.parent = None
            self.optical_channel = YList()
            self.optical_channel.parent = self
            self.optical_channel.name = 'optical_channel'


        class OpticalChannel(object):
            """
            List of 
            
            .. attribute:: index
            
            	 
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: config
            
            	Configuration data 
            	**type**\: :py:class:`Config <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.OpticalChannels.OpticalChannel.Config>`
            
            .. attribute:: state
            
            	Operational state data 
            	**type**\: :py:class:`State <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.OpticalChannels.OpticalChannel.State>`
            
            

            """

            _prefix = 'opt-term'
            _revision = '2015-11-25'

            def __init__(self):
                self.parent = None
                self.index = None
                self.config = TerminalDevice.OpticalChannels.OpticalChannel.Config()
                self.config.parent = self
                self.state = TerminalDevice.OpticalChannels.OpticalChannel.State()
                self.state.parent = self


            class Config(object):
                """
                Configuration data 
                
                .. attribute:: frequency
                
                	Frequency of the optical channel
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: index
                
                	Index number assigned to the optical channel.  The index must be unique on the local system
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: line_port
                
                	Reference to the line\-side physical port that carries this optical channel
                	**type**\: str
                
                .. attribute:: operational_mode
                
                	Vendor\-specific mode identifier \-\- sets the operational mode for the channel
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: power
                
                	Power level of the optical channel
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'opt-term'
                _revision = '2015-11-25'

                def __init__(self):
                    self.parent = None
                    self.frequency = None
                    self.index = None
                    self.line_port = None
                    self.operational_mode = None
                    self.power = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/openconfig-terminal-device:config'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.frequency is not None:
                        return True

                    if self.index is not None:
                        return True

                    if self.line_port is not None:
                        return True

                    if self.operational_mode is not None:
                        return True

                    if self.power is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_terminal_device as meta
                    return meta._meta_table['TerminalDevice.OpticalChannels.OpticalChannel.Config']['meta_info']


            class State(object):
                """
                Operational state data 
                
                .. attribute:: frequency
                
                	Frequency of the optical channel
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: index
                
                	Index number assigned to the optical channel.  The index must be unique on the local system
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: line_port
                
                	Reference to the line\-side physical port that carries this optical channel
                	**type**\: str
                
                .. attribute:: operational_mode
                
                	Vendor\-specific mode identifier \-\- sets the operational mode for the channel
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: power
                
                	Power level of the optical channel
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'opt-term'
                _revision = '2015-11-25'

                def __init__(self):
                    self.parent = None
                    self.frequency = None
                    self.index = None
                    self.line_port = None
                    self.operational_mode = None
                    self.power = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/openconfig-terminal-device:state'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.frequency is not None:
                        return True

                    if self.index is not None:
                        return True

                    if self.line_port is not None:
                        return True

                    if self.operational_mode is not None:
                        return True

                    if self.power is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_terminal_device as meta
                    return meta._meta_table['TerminalDevice.OpticalChannels.OpticalChannel.State']['meta_info']

            @property
            def _common_path(self):
                if self.index is None:
                    raise YPYDataValidationError('Key property index is None')

                return '/openconfig-terminal-device:terminal-device/openconfig-terminal-device:optical-channels/openconfig-terminal-device:optical-channel[openconfig-terminal-device:index = ' + str(self.index) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.index is not None:
                    return True

                if self.config is not None and self.config._has_data():
                    return True

                if self.state is not None and self.state._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.openconfig._meta import _openconfig_terminal_device as meta
                return meta._meta_table['TerminalDevice.OpticalChannels.OpticalChannel']['meta_info']

        @property
        def _common_path(self):

            return '/openconfig-terminal-device:terminal-device/openconfig-terminal-device:optical-channels'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.optical_channel is not None:
                for child_ref in self.optical_channel:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.openconfig._meta import _openconfig_terminal_device as meta
            return meta._meta_table['TerminalDevice.OpticalChannels']['meta_info']


    class State(object):
        """
        Operational state data for global terminal device
        
        

        """

        _prefix = 'opt-term'
        _revision = '2015-11-25'

        def __init__(self):
            self.parent = None

        @property
        def _common_path(self):

            return '/openconfig-terminal-device:terminal-device/openconfig-terminal-device:state'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.openconfig._meta import _openconfig_terminal_device as meta
            return meta._meta_table['TerminalDevice.State']['meta_info']

    @property
    def _common_path(self):

        return '/openconfig-terminal-device:terminal-device'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.client_ports is not None and self.client_ports._has_data():
            return True

        if self.config is not None and self.config._has_data():
            return True

        if self.line_ports is not None and self.line_ports._has_data():
            return True

        if self.logical_channels is not None and self.logical_channels._has_data():
            return True

        if self.operational_modes is not None and self.operational_modes._has_data():
            return True

        if self.optical_channels is not None and self.optical_channels._has_data():
            return True

        if self.state is not None and self.state._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_terminal_device as meta
        return meta._meta_table['TerminalDevice']['meta_info']


