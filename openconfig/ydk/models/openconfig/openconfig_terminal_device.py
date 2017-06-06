""" openconfig_terminal_device 

This module describes a terminal optics device model for
managing the terminal systems (client and line side) in a
DWDM transport network.

Elements of the model\:

physical port\: corresponds to a physical, pluggable client
port on the terminal device. Examples includes 10G, 40G, 100G
(e.g., 10x10G, 4x25G or 1x100G) and 400G/1T in the future.
Physical client ports will have associated operational state or
PMs.

physical channel\: a physical lane or channel in the
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

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class TerminalDevice(object):
    """
    Top\-level container for the terminal device
    
    .. attribute:: config
    
    	Configuration data for global terminal\-device
    	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.Config>`
    
    .. attribute:: logical_channels
    
    	Enclosing container the list of logical channels
    	**type**\:   :py:class:`LogicalChannels <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels>`
    
    .. attribute:: operational_modes
    
    	Enclosing container for list of operational modes
    	**type**\:   :py:class:`OperationalModes <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.OperationalModes>`
    
    .. attribute:: state
    
    	Operational state data for global terminal device
    	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.State>`
    
    

    """

    _prefix = 'oc-opt-term'
    _revision = '2016-06-17'

    def __init__(self):
        self.config = TerminalDevice.Config()
        self.config.parent = self
        self.logical_channels = TerminalDevice.LogicalChannels()
        self.logical_channels.parent = self
        self.operational_modes = TerminalDevice.OperationalModes()
        self.operational_modes.parent = self
        self.state = TerminalDevice.State()
        self.state.parent = self


    class Config(object):
        """
        Configuration data for global terminal\-device
        
        

        """

        _prefix = 'oc-opt-term'
        _revision = '2016-06-17'

        def __init__(self):
            self.parent = None

        @property
        def _common_path(self):

            return '/openconfig-terminal-device:terminal-device/openconfig-terminal-device:config'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.openconfig._meta import _openconfig_terminal_device as meta
            return meta._meta_table['TerminalDevice.Config']['meta_info']


    class State(object):
        """
        Operational state data for global terminal device
        
        

        """

        _prefix = 'oc-opt-term'
        _revision = '2016-06-17'

        def __init__(self):
            self.parent = None

        @property
        def _common_path(self):

            return '/openconfig-terminal-device:terminal-device/openconfig-terminal-device:state'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.openconfig._meta import _openconfig_terminal_device as meta
            return meta._meta_table['TerminalDevice.State']['meta_info']


    class LogicalChannels(object):
        """
        Enclosing container the list of logical channels
        
        .. attribute:: channel
        
        	List of logical channels
        	**type**\: list of    :py:class:`Channel <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel>`
        
        

        """

        _prefix = 'oc-opt-term'
        _revision = '2016-06-17'

        def __init__(self):
            self.parent = None
            self.channel = YList()
            self.channel.parent = self
            self.channel.name = 'channel'


        class Channel(object):
            """
            List of logical channels
            
            .. attribute:: index  <key>
            
            	Reference to the index of the logical channel
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`index <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel.Config>`
            
            .. attribute:: config
            
            	Configuration data for logical channels
            	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel.Config>`
            
            .. attribute:: ethernet
            
            	Top level container for data related to Ethernet framing for the logical channel
            	**type**\:   :py:class:`Ethernet <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel.Ethernet>`
            
            .. attribute:: ingress
            
            	Top\-level container for specifying references to the source of signal for the logical channel, either a transceiver or individual physical channels
            	**type**\:   :py:class:`Ingress <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel.Ingress>`
            
            .. attribute:: logical_channel_assignments
            
            	Enclosing container for tributary assignments
            	**type**\:   :py:class:`LogicalChannelAssignments <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments>`
            
            .. attribute:: otn
            
            	Top level container for OTU configuration when logical channel framing is using an OTU protocol, e.g., OTU1, OTU3, etc
            	**type**\:   :py:class:`Otn <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel.Otn>`
            
            .. attribute:: state
            
            	Operational state data for logical channels
            	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel.State>`
            
            

            """

            _prefix = 'oc-opt-term'
            _revision = '2016-06-17'

            def __init__(self):
                self.parent = None
                self.index = None
                self.config = TerminalDevice.LogicalChannels.Channel.Config()
                self.config.parent = self
                self.ethernet = TerminalDevice.LogicalChannels.Channel.Ethernet()
                self.ethernet.parent = self
                self.ingress = TerminalDevice.LogicalChannels.Channel.Ingress()
                self.ingress.parent = self
                self.logical_channel_assignments = TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments()
                self.logical_channel_assignments.parent = self
                self.otn = TerminalDevice.LogicalChannels.Channel.Otn()
                self.otn.parent = self
                self.state = TerminalDevice.LogicalChannels.Channel.State()
                self.state.parent = self


            class Config(object):
                """
                Configuration data for logical channels
                
                .. attribute:: admin_state
                
                	Sets the admin state of the logical channel
                	**type**\:   :py:class:`AdminStateTypeEnum <ydk.models.openconfig.openconfig_transport_types.AdminStateTypeEnum>`
                
                .. attribute:: description
                
                	Description of the logical channel
                	**type**\:  str
                
                .. attribute:: index
                
                	Index of the current logical channel
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: logical_channel_type
                
                	The type / stage of the logical element determines the configuration and operational state parameters (PMs) available for the logical element
                	**type**\:   :py:class:`Logical_Element_Protocol_TypeIdentity <ydk.models.openconfig.openconfig_transport_types.Logical_Element_Protocol_TypeIdentity>`
                
                .. attribute:: loopback_mode
                
                	Sets the loopback type on the logical channel. Setting the mode to something besides NONE activates the loopback in the specified mode
                	**type**\:   :py:class:`LoopbackModeTypeEnum <ydk.models.openconfig.openconfig_transport_types.LoopbackModeTypeEnum>`
                
                .. attribute:: rate_class
                
                	Rounded bit rate of the tributary signal. Exact bit rate will be refined by protocol selection
                	**type**\:   :py:class:`Tributary_Rate_Class_TypeIdentity <ydk.models.openconfig.openconfig_transport_types.Tributary_Rate_Class_TypeIdentity>`
                
                .. attribute:: trib_protocol
                
                	Protocol framing of the tributary signal. If this LogicalChannel is directly connected to a Client\-Port or Optical\-Channel, this is the protocol of the associated port. If the LogicalChannel is connected to other LogicalChannels, the TributaryProtocol of the LogicalChannels will define a specific mapping/demapping or multiplexing/demultiplexing function.  Not all protocols are valid, depending on the value of trib\-rate\-class.  The expectation is that the NMS will validate that a correct combination of rate class and protocol are specfied.  Basic combinations are\:  rate class\: 1G protocols\: 1GE  rate class\: 2.5G protocols\: OC48, STM16  rate class\: 10G protocols\:  10GE LAN, 10GE WAN, OC192, STM64, OTU2, OTU2e,            OTU1e, ODU2, ODU2e, ODU1e  rate class\: 40G protocols\:  40GE, OC768, STM256, OTU3, ODU3  rate class\: 100G protocols\:  100GE, 100G MLG, OTU4, OTUCn, ODU4
                	**type**\:   :py:class:`Tributary_Protocol_TypeIdentity <ydk.models.openconfig.openconfig_transport_types.Tributary_Protocol_TypeIdentity>`
                
                

                """

                _prefix = 'oc-opt-term'
                _revision = '2016-06-17'

                def __init__(self):
                    self.parent = None
                    self.admin_state = None
                    self.description = None
                    self.index = None
                    self.logical_channel_type = None
                    self.loopback_mode = None
                    self.rate_class = None
                    self.trib_protocol = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/openconfig-terminal-device:config'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.admin_state is not None:
                        return True

                    if self.description is not None:
                        return True

                    if self.index is not None:
                        return True

                    if self.logical_channel_type is not None:
                        return True

                    if self.loopback_mode is not None:
                        return True

                    if self.rate_class is not None:
                        return True

                    if self.trib_protocol is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_terminal_device as meta
                    return meta._meta_table['TerminalDevice.LogicalChannels.Channel.Config']['meta_info']


            class State(object):
                """
                Operational state data for logical channels
                
                .. attribute:: admin_state
                
                	Sets the admin state of the logical channel
                	**type**\:   :py:class:`AdminStateTypeEnum <ydk.models.openconfig.openconfig_transport_types.AdminStateTypeEnum>`
                
                .. attribute:: description
                
                	Description of the logical channel
                	**type**\:  str
                
                .. attribute:: index
                
                	Index of the current logical channel
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: link_state
                
                	Link\-state of the Ethernet protocol on the logical channel, SONET / SDH framed signal, etc
                	**type**\:   :py:class:`LinkStateEnum <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel.State.LinkStateEnum>`
                
                .. attribute:: logical_channel_type
                
                	The type / stage of the logical element determines the configuration and operational state parameters (PMs) available for the logical element
                	**type**\:   :py:class:`Logical_Element_Protocol_TypeIdentity <ydk.models.openconfig.openconfig_transport_types.Logical_Element_Protocol_TypeIdentity>`
                
                .. attribute:: loopback_mode
                
                	Sets the loopback type on the logical channel. Setting the mode to something besides NONE activates the loopback in the specified mode
                	**type**\:   :py:class:`LoopbackModeTypeEnum <ydk.models.openconfig.openconfig_transport_types.LoopbackModeTypeEnum>`
                
                .. attribute:: rate_class
                
                	Rounded bit rate of the tributary signal. Exact bit rate will be refined by protocol selection
                	**type**\:   :py:class:`Tributary_Rate_Class_TypeIdentity <ydk.models.openconfig.openconfig_transport_types.Tributary_Rate_Class_TypeIdentity>`
                
                .. attribute:: trib_protocol
                
                	Protocol framing of the tributary signal. If this LogicalChannel is directly connected to a Client\-Port or Optical\-Channel, this is the protocol of the associated port. If the LogicalChannel is connected to other LogicalChannels, the TributaryProtocol of the LogicalChannels will define a specific mapping/demapping or multiplexing/demultiplexing function.  Not all protocols are valid, depending on the value of trib\-rate\-class.  The expectation is that the NMS will validate that a correct combination of rate class and protocol are specfied.  Basic combinations are\:  rate class\: 1G protocols\: 1GE  rate class\: 2.5G protocols\: OC48, STM16  rate class\: 10G protocols\:  10GE LAN, 10GE WAN, OC192, STM64, OTU2, OTU2e,            OTU1e, ODU2, ODU2e, ODU1e  rate class\: 40G protocols\:  40GE, OC768, STM256, OTU3, ODU3  rate class\: 100G protocols\:  100GE, 100G MLG, OTU4, OTUCn, ODU4
                	**type**\:   :py:class:`Tributary_Protocol_TypeIdentity <ydk.models.openconfig.openconfig_transport_types.Tributary_Protocol_TypeIdentity>`
                
                

                """

                _prefix = 'oc-opt-term'
                _revision = '2016-06-17'

                def __init__(self):
                    self.parent = None
                    self.admin_state = None
                    self.description = None
                    self.index = None
                    self.link_state = None
                    self.logical_channel_type = None
                    self.loopback_mode = None
                    self.rate_class = None
                    self.trib_protocol = None

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


                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/openconfig-terminal-device:state'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.admin_state is not None:
                        return True

                    if self.description is not None:
                        return True

                    if self.index is not None:
                        return True

                    if self.link_state is not None:
                        return True

                    if self.logical_channel_type is not None:
                        return True

                    if self.loopback_mode is not None:
                        return True

                    if self.rate_class is not None:
                        return True

                    if self.trib_protocol is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_terminal_device as meta
                    return meta._meta_table['TerminalDevice.LogicalChannels.Channel.State']['meta_info']


            class Otn(object):
                """
                Top level container for OTU configuration when logical
                channel framing is using an OTU protocol, e.g., OTU1, OTU3,
                etc.
                
                .. attribute:: config
                
                	Configuration data for OTN protocol framing
                	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel.Otn.Config>`
                
                .. attribute:: state
                
                	Operational state data for OTN protocol PMs, statistics, etc
                	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel.Otn.State>`
                
                

                """

                _prefix = 'oc-opt-term'
                _revision = '2016-06-17'

                def __init__(self):
                    self.parent = None
                    self.config = TerminalDevice.LogicalChannels.Channel.Otn.Config()
                    self.config.parent = self
                    self.state = TerminalDevice.LogicalChannels.Channel.Otn.State()
                    self.state.parent = self


                class Config(object):
                    """
                    Configuration data for OTN protocol framing
                    
                    .. attribute:: tti_msg_auto
                    
                    	Trail trace identifier (TTI) transmit message automatically created. If True, then setting a custom transmit message would be invalid
                    	**type**\:  bool
                    
                    .. attribute:: tti_msg_expected
                    
                    	Trail trace identifier (TTI) message expected
                    	**type**\:  str
                    
                    .. attribute:: tti_msg_transmit
                    
                    	Trail trace identifier (TTI) message transmitted
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'oc-opt-term'
                    _revision = '2016-06-17'

                    def __init__(self):
                        self.parent = None
                        self.tti_msg_auto = None
                        self.tti_msg_expected = None
                        self.tti_msg_transmit = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-terminal-device:config'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.tti_msg_auto is not None:
                            return True

                        if self.tti_msg_expected is not None:
                            return True

                        if self.tti_msg_transmit is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_terminal_device as meta
                        return meta._meta_table['TerminalDevice.LogicalChannels.Channel.Otn.Config']['meta_info']


                class State(object):
                    """
                    Operational state data for OTN protocol PMs, statistics,
                    etc.
                    
                    .. attribute:: background_block_errors
                    
                    	The number of background block errors
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: code_violations
                    
                    	For ethernet or fiberchannel links, the number of 8b/10b coding violations. For SONET/SDH, the number of BIP (bit interleaved parity) errors
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: errored_seconds
                    
                    	The number of seconds that at least one errored blocks occurs, at least one code violation occurs, loss of sync is detected or loss of signal is detected
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: esnr
                    
                    	Electrical signal to noise ratio. Baud rate normalized signal to noise ratio based on error vector magnitude
                    	**type**\:   :py:class:`Esnr <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel.Otn.State.Esnr>`
                    
                    .. attribute:: fec_corrected_bits
                    
                    	The number of bits that were corrected by the FEC
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: fec_corrected_bytes
                    
                    	The number of bytes that were corrected by the FEC
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: fec_uncorrectable_words
                    
                    	The number words that were uncorrectable by the FEC
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: post_fec_ber
                    
                    	Bit error rate after forward error correction \-\- computed value
                    	**type**\:   :py:class:`PostFecBer <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel.Otn.State.PostFecBer>`
                    
                    .. attribute:: pre_fec_ber
                    
                    	Bit error rate before forward error correction \-\- computed value
                    	**type**\:   :py:class:`PreFecBer <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel.Otn.State.PreFecBer>`
                    
                    .. attribute:: q_value
                    
                    	Quality value (factor) of a channel
                    	**type**\:   :py:class:`QValue <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel.Otn.State.QValue>`
                    
                    .. attribute:: rdi_msg
                    
                    	Remote defect indication (RDI) message received
                    	**type**\:  str
                    
                    .. attribute:: severely_errored_seconds
                    
                    	The number of seconds that loss of frame is detected OR the number of errored blocks, code violations, loss of sync or loss of signal is detected exceeds a predefined threshold
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: tti_msg_auto
                    
                    	Trail trace identifier (TTI) transmit message automatically created. If True, then setting a custom transmit message would be invalid
                    	**type**\:  bool
                    
                    .. attribute:: tti_msg_expected
                    
                    	Trail trace identifier (TTI) message expected
                    	**type**\:  str
                    
                    .. attribute:: tti_msg_recv
                    
                    	Trail trace identifier (TTI) message received
                    	**type**\:  str
                    
                    .. attribute:: tti_msg_transmit
                    
                    	Trail trace identifier (TTI) message transmitted
                    	**type**\:  str
                    
                    .. attribute:: unavailable_seconds
                    
                    	The number of seconds during which the link is unavailable
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'oc-opt-term'
                    _revision = '2016-06-17'

                    def __init__(self):
                        self.parent = None
                        self.background_block_errors = None
                        self.code_violations = None
                        self.errored_seconds = None
                        self.esnr = TerminalDevice.LogicalChannels.Channel.Otn.State.Esnr()
                        self.esnr.parent = self
                        self.fec_corrected_bits = None
                        self.fec_corrected_bytes = None
                        self.fec_uncorrectable_words = None
                        self.post_fec_ber = TerminalDevice.LogicalChannels.Channel.Otn.State.PostFecBer()
                        self.post_fec_ber.parent = self
                        self.pre_fec_ber = TerminalDevice.LogicalChannels.Channel.Otn.State.PreFecBer()
                        self.pre_fec_ber.parent = self
                        self.q_value = TerminalDevice.LogicalChannels.Channel.Otn.State.QValue()
                        self.q_value.parent = self
                        self.rdi_msg = None
                        self.severely_errored_seconds = None
                        self.tti_msg_auto = None
                        self.tti_msg_expected = None
                        self.tti_msg_recv = None
                        self.tti_msg_transmit = None
                        self.unavailable_seconds = None


                    class PreFecBer(object):
                        """
                        Bit error rate before forward error correction \-\- computed
                        value
                        
                        .. attribute:: avg
                        
                        	The arithmetic mean value of the statistic over the sampling period
                        	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-922337203685477580.8..922337203685477580.7
                        
                        .. attribute:: instant
                        
                        	The instantaneous value of the statistic
                        	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-922337203685477580.8..922337203685477580.7
                        
                        .. attribute:: max
                        
                        	The maximum value of the statitic over the sampling period
                        	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-922337203685477580.8..922337203685477580.7
                        
                        .. attribute:: min
                        
                        	The minimum value of the statistic over the sampling period
                        	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-922337203685477580.8..922337203685477580.7
                        
                        

                        """

                        _prefix = 'oc-opt-term'
                        _revision = '2016-06-17'

                        def __init__(self):
                            self.parent = None
                            self.avg = None
                            self.instant = None
                            self.max = None
                            self.min = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/openconfig-terminal-device:pre-fec-ber'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.avg is not None:
                                return True

                            if self.instant is not None:
                                return True

                            if self.max is not None:
                                return True

                            if self.min is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_terminal_device as meta
                            return meta._meta_table['TerminalDevice.LogicalChannels.Channel.Otn.State.PreFecBer']['meta_info']


                    class PostFecBer(object):
                        """
                        Bit error rate after forward error correction \-\- computed
                        value
                        
                        .. attribute:: avg
                        
                        	The arithmetic mean value of the statistic over the sampling period
                        	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-922337203685477580.8..922337203685477580.7
                        
                        .. attribute:: instant
                        
                        	The instantaneous value of the statistic
                        	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-922337203685477580.8..922337203685477580.7
                        
                        .. attribute:: max
                        
                        	The maximum value of the statitic over the sampling period
                        	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-922337203685477580.8..922337203685477580.7
                        
                        .. attribute:: min
                        
                        	The minimum value of the statistic over the sampling period
                        	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-922337203685477580.8..922337203685477580.7
                        
                        

                        """

                        _prefix = 'oc-opt-term'
                        _revision = '2016-06-17'

                        def __init__(self):
                            self.parent = None
                            self.avg = None
                            self.instant = None
                            self.max = None
                            self.min = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/openconfig-terminal-device:post-fec-ber'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.avg is not None:
                                return True

                            if self.instant is not None:
                                return True

                            if self.max is not None:
                                return True

                            if self.min is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_terminal_device as meta
                            return meta._meta_table['TerminalDevice.LogicalChannels.Channel.Otn.State.PostFecBer']['meta_info']


                    class QValue(object):
                        """
                        Quality value (factor) of a channel
                        
                        .. attribute:: avg
                        
                        	The arithmetic mean value of the statistic over the sampling period
                        	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-922337203685477580.8..922337203685477580.7
                        
                        .. attribute:: instant
                        
                        	The instantaneous value of the statistic
                        	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-922337203685477580.8..922337203685477580.7
                        
                        .. attribute:: max
                        
                        	The maximum value of the statitic over the sampling period
                        	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-922337203685477580.8..922337203685477580.7
                        
                        .. attribute:: min
                        
                        	The minimum value of the statistic over the sampling period
                        	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-922337203685477580.8..922337203685477580.7
                        
                        

                        """

                        _prefix = 'oc-opt-term'
                        _revision = '2016-06-17'

                        def __init__(self):
                            self.parent = None
                            self.avg = None
                            self.instant = None
                            self.max = None
                            self.min = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/openconfig-terminal-device:q-value'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.avg is not None:
                                return True

                            if self.instant is not None:
                                return True

                            if self.max is not None:
                                return True

                            if self.min is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_terminal_device as meta
                            return meta._meta_table['TerminalDevice.LogicalChannels.Channel.Otn.State.QValue']['meta_info']


                    class Esnr(object):
                        """
                        Electrical signal to noise ratio. Baud rate
                        normalized signal to noise ratio based on
                        error vector magnitude
                        
                        .. attribute:: avg
                        
                        	The arithmetic mean value of the statistic over the sampling period
                        	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-922337203685477580.8..922337203685477580.7
                        
                        .. attribute:: instant
                        
                        	The instantaneous value of the statistic
                        	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-922337203685477580.8..922337203685477580.7
                        
                        .. attribute:: max
                        
                        	The maximum value of the statitic over the sampling period
                        	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-922337203685477580.8..922337203685477580.7
                        
                        .. attribute:: min
                        
                        	The minimum value of the statistic over the sampling period
                        	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-922337203685477580.8..922337203685477580.7
                        
                        

                        """

                        _prefix = 'oc-opt-term'
                        _revision = '2016-06-17'

                        def __init__(self):
                            self.parent = None
                            self.avg = None
                            self.instant = None
                            self.max = None
                            self.min = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/openconfig-terminal-device:esnr'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.avg is not None:
                                return True

                            if self.instant is not None:
                                return True

                            if self.max is not None:
                                return True

                            if self.min is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_terminal_device as meta
                            return meta._meta_table['TerminalDevice.LogicalChannels.Channel.Otn.State.Esnr']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-terminal-device:state'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.background_block_errors is not None:
                            return True

                        if self.code_violations is not None:
                            return True

                        if self.errored_seconds is not None:
                            return True

                        if self.esnr is not None and self.esnr._has_data():
                            return True

                        if self.fec_corrected_bits is not None:
                            return True

                        if self.fec_corrected_bytes is not None:
                            return True

                        if self.fec_uncorrectable_words is not None:
                            return True

                        if self.post_fec_ber is not None and self.post_fec_ber._has_data():
                            return True

                        if self.pre_fec_ber is not None and self.pre_fec_ber._has_data():
                            return True

                        if self.q_value is not None and self.q_value._has_data():
                            return True

                        if self.rdi_msg is not None:
                            return True

                        if self.severely_errored_seconds is not None:
                            return True

                        if self.tti_msg_auto is not None:
                            return True

                        if self.tti_msg_expected is not None:
                            return True

                        if self.tti_msg_recv is not None:
                            return True

                        if self.tti_msg_transmit is not None:
                            return True

                        if self.unavailable_seconds is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_terminal_device as meta
                        return meta._meta_table['TerminalDevice.LogicalChannels.Channel.Otn.State']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/openconfig-terminal-device:otn'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.config is not None and self.config._has_data():
                        return True

                    if self.state is not None and self.state._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_terminal_device as meta
                    return meta._meta_table['TerminalDevice.LogicalChannels.Channel.Otn']['meta_info']


            class Ethernet(object):
                """
                Top level container for data related to Ethernet framing
                for the logical channel
                
                .. attribute:: config
                
                	Configuration data for Ethernet protocol framing on logical channels
                	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel.Ethernet.Config>`
                
                .. attribute:: state
                
                	Operational state data for Ethernet protocol framing on logical channels
                	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel.Ethernet.State>`
                
                

                """

                _prefix = 'oc-opt-term'
                _revision = '2016-06-17'

                def __init__(self):
                    self.parent = None
                    self.config = TerminalDevice.LogicalChannels.Channel.Ethernet.Config()
                    self.config.parent = self
                    self.state = TerminalDevice.LogicalChannels.Channel.Ethernet.State()
                    self.state.parent = self


                class Config(object):
                    """
                    Configuration data for Ethernet protocol framing on logical
                    channels
                    
                    

                    """

                    _prefix = 'oc-opt-term'
                    _revision = '2016-06-17'

                    def __init__(self):
                        self.parent = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-terminal-device:config'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_terminal_device as meta
                        return meta._meta_table['TerminalDevice.LogicalChannels.Channel.Ethernet.Config']['meta_info']


                class State(object):
                    """
                    Operational state data for Ethernet protocol framing on logical
                    channels
                    
                    .. attribute:: in_8021q_frames
                    
                    	Number of 802.1q tagged frames received on the interface
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: in_crc_errors
                    
                    	Number of receive error events due to FCS/CRC check failure
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: in_fragment_frames
                    
                    	Number of fragment frames received on the interface
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: in_jabber_frames
                    
                    	Number of jabber frames received on the interface.  Jabber frames are typically defined as oversize frames which also have a bad CRC.  Implementations may use slightly different definitions of what constitutes a jabber frame.  Often indicative of a NIC hardware problem
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: in_mac_control_frames
                    
                    	MAC layer control frames received on the interface
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: in_mac_pause_frames
                    
                    	MAC layer PAUSE frames received on the interface
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: in_oversize_frames
                    
                    	Number of oversize frames received on the interface
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: out_8021q_frames
                    
                    	Number of 802.1q tagged frames sent on the interface
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: out_mac_control_frames
                    
                    	MAC layer control frames sent on the interface
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: out_mac_pause_frames
                    
                    	MAC layer PAUSE frames sent on the interface
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'oc-opt-term'
                    _revision = '2016-06-17'

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
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-terminal-device:state'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
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
                        return meta._meta_table['TerminalDevice.LogicalChannels.Channel.Ethernet.State']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/openconfig-terminal-device:ethernet'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.config is not None and self.config._has_data():
                        return True

                    if self.state is not None and self.state._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_terminal_device as meta
                    return meta._meta_table['TerminalDevice.LogicalChannels.Channel.Ethernet']['meta_info']


            class Ingress(object):
                """
                Top\-level container for specifying references to the
                source of signal for the logical channel, either a
                transceiver or individual physical channels
                
                .. attribute:: config
                
                	Configuration data for the signal source for the logical channel
                	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel.Ingress.Config>`
                
                .. attribute:: state
                
                	Operational state data for the signal source for the logical channel
                	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel.Ingress.State>`
                
                

                """

                _prefix = 'oc-opt-term'
                _revision = '2016-06-17'

                def __init__(self):
                    self.parent = None
                    self.config = TerminalDevice.LogicalChannels.Channel.Ingress.Config()
                    self.config.parent = self
                    self.state = TerminalDevice.LogicalChannels.Channel.Ingress.State()
                    self.state.parent = self


                class Config(object):
                    """
                    Configuration data for the signal source for the
                    logical channel
                    
                    .. attribute:: physical_channel
                    
                    	This list should be populated with references to the client physical channels that feed this logical channel from the transceiver specified in the 'transceiver' leaf, which must be specified.  If this leaf\-list is empty, all physical channels in the transceiver are assumed to be mapped to the logical channel
                    	**type**\:  list of int
                    
                    	**range:** 0..65535
                    
                    	**refers to**\:  :py:class:`index <ydk.models.openconfig.openconfig_platform.Components.Component.Transceiver.PhysicalChannels.Channel>`
                    
                    .. attribute:: transceiver
                    
                    	Reference to the transceiver carrying the input signal for the logical channel.  If specific physical channels are mapped to the logical channel (as opposed to all physical channels carried by the transceiver), they can be specified in the list of physical channel references
                    	**type**\:  str
                    
                    	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_platform.Components.Component>`
                    
                    

                    """

                    _prefix = 'oc-opt-term'
                    _revision = '2016-06-17'

                    def __init__(self):
                        self.parent = None
                        self.physical_channel = YLeafList()
                        self.physical_channel.parent = self
                        self.physical_channel.name = 'physical_channel'
                        self.transceiver = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-terminal-device:config'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.physical_channel is not None:
                            for child in self.physical_channel:
                                if child is not None:
                                    return True

                        if self.transceiver is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_terminal_device as meta
                        return meta._meta_table['TerminalDevice.LogicalChannels.Channel.Ingress.Config']['meta_info']


                class State(object):
                    """
                    Operational state data for the signal source for the
                    logical channel
                    
                    .. attribute:: physical_channel
                    
                    	This list should be populated with references to the client physical channels that feed this logical channel from the transceiver specified in the 'transceiver' leaf, which must be specified.  If this leaf\-list is empty, all physical channels in the transceiver are assumed to be mapped to the logical channel
                    	**type**\:  list of int
                    
                    	**range:** 0..65535
                    
                    	**refers to**\:  :py:class:`index <ydk.models.openconfig.openconfig_platform.Components.Component.Transceiver.PhysicalChannels.Channel>`
                    
                    .. attribute:: transceiver
                    
                    	Reference to the transceiver carrying the input signal for the logical channel.  If specific physical channels are mapped to the logical channel (as opposed to all physical channels carried by the transceiver), they can be specified in the list of physical channel references
                    	**type**\:  str
                    
                    	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_platform.Components.Component>`
                    
                    

                    """

                    _prefix = 'oc-opt-term'
                    _revision = '2016-06-17'

                    def __init__(self):
                        self.parent = None
                        self.physical_channel = YLeafList()
                        self.physical_channel.parent = self
                        self.physical_channel.name = 'physical_channel'
                        self.transceiver = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-terminal-device:state'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.physical_channel is not None:
                            for child in self.physical_channel:
                                if child is not None:
                                    return True

                        if self.transceiver is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_terminal_device as meta
                        return meta._meta_table['TerminalDevice.LogicalChannels.Channel.Ingress.State']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/openconfig-terminal-device:ingress'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.config is not None and self.config._has_data():
                        return True

                    if self.state is not None and self.state._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_terminal_device as meta
                    return meta._meta_table['TerminalDevice.LogicalChannels.Channel.Ingress']['meta_info']


            class LogicalChannelAssignments(object):
                """
                Enclosing container for tributary assignments
                
                .. attribute:: assignment
                
                	Logical channel elements may be assigned directly to optical channels for line\-side transmission, or can be further groomed into additional stages of logical channel elements.  The grooming can multiplex (i.e., split the current element into multiple elements in the subsequent stage) or de\-multiplex (i.e., combine the current element with other elements into the same element in the subsequent stage) logical elements in each stage.  Note that to support the ability to groom the logical elements, the list of logical channel elements should be populated with an entry for the logical elements at each stage, starting with the initial assignment from the respective client physical port.  Each logical element assignment consists of a pointer to an element in the next stage, or to an optical channel, along with a bandwidth allocation for the corresponding assignment (e.g., to split or combine signal)
                	**type**\: list of    :py:class:`Assignment <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment>`
                
                

                """

                _prefix = 'oc-opt-term'
                _revision = '2016-06-17'

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
                    
                    .. attribute:: index  <key>
                    
                    	Reference to the index for the current tributary assignment
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**refers to**\:  :py:class:`index <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment.Config>`
                    
                    .. attribute:: config
                    
                    	Configuration data for tributary assignments
                    	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment.Config>`
                    
                    .. attribute:: state
                    
                    	Operational state data for tributary assignments
                    	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment.State>`
                    
                    

                    """

                    _prefix = 'oc-opt-term'
                    _revision = '2016-06-17'

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
                        	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-9223372036854775.808..9223372036854775.807
                        
                        	**units**\: Gbps
                        
                        .. attribute:: assignment_type
                        
                        	Each logical channel element may be assigned to subsequent stages of logical elements to implement further grooming, or can be assigned to a line\-side optical channel for transmission.  Each assignment also has an associated bandwidth allocation
                        	**type**\:   :py:class:`AssignmentTypeEnum <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment.Config.AssignmentTypeEnum>`
                        
                        .. attribute:: description
                        
                        	Name assigned to the logical client channel
                        	**type**\:  str
                        
                        .. attribute:: index
                        
                        	Index of the current logical client channel to tributary mapping
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: logical_channel
                        
                        	Reference to another stage of logical channel elements
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**refers to**\:  :py:class:`index <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel>`
                        
                        .. attribute:: optical_channel
                        
                        	Reference to the line\-side optical channel that should carry the current logical channel element.  Use this reference to exit the logical element stage
                        	**type**\:  str
                        
                        	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_platform.Components.Component>`
                        
                        

                        """

                        _prefix = 'oc-opt-term'
                        _revision = '2016-06-17'

                        def __init__(self):
                            self.parent = None
                            self.allocation = None
                            self.assignment_type = None
                            self.description = None
                            self.index = None
                            self.logical_channel = None
                            self.optical_channel = None

                        class AssignmentTypeEnum(Enum):
                            """
                            AssignmentTypeEnum

                            Each logical channel element may be assigned to subsequent

                            stages of logical elements to implement further grooming, or

                            can be assigned to a line\-side optical channel for

                            transmission.  Each assignment also has an associated

                            bandwidth allocation.

                            .. data:: LOGICAL_CHANNEL = 0

                            	Subsequent channel is a logical channel

                            .. data:: OPTICAL_CHANNEL = 1

                            	Subsequent channel is a optical channel / carrier

                            """

                            LOGICAL_CHANNEL = 0

                            OPTICAL_CHANNEL = 1


                            @staticmethod
                            def _meta_info():
                                from ydk.models.openconfig._meta import _openconfig_terminal_device as meta
                                return meta._meta_table['TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment.Config.AssignmentTypeEnum']


                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/openconfig-terminal-device:config'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.allocation is not None:
                                return True

                            if self.assignment_type is not None:
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
                        	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-9223372036854775.808..9223372036854775.807
                        
                        	**units**\: Gbps
                        
                        .. attribute:: assignment_type
                        
                        	Each logical channel element may be assigned to subsequent stages of logical elements to implement further grooming, or can be assigned to a line\-side optical channel for transmission.  Each assignment also has an associated bandwidth allocation
                        	**type**\:   :py:class:`AssignmentTypeEnum <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment.State.AssignmentTypeEnum>`
                        
                        .. attribute:: description
                        
                        	Name assigned to the logical client channel
                        	**type**\:  str
                        
                        .. attribute:: index
                        
                        	Index of the current logical client channel to tributary mapping
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: logical_channel
                        
                        	Reference to another stage of logical channel elements
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**refers to**\:  :py:class:`index <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel>`
                        
                        .. attribute:: optical_channel
                        
                        	Reference to the line\-side optical channel that should carry the current logical channel element.  Use this reference to exit the logical element stage
                        	**type**\:  str
                        
                        	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_platform.Components.Component>`
                        
                        

                        """

                        _prefix = 'oc-opt-term'
                        _revision = '2016-06-17'

                        def __init__(self):
                            self.parent = None
                            self.allocation = None
                            self.assignment_type = None
                            self.description = None
                            self.index = None
                            self.logical_channel = None
                            self.optical_channel = None

                        class AssignmentTypeEnum(Enum):
                            """
                            AssignmentTypeEnum

                            Each logical channel element may be assigned to subsequent

                            stages of logical elements to implement further grooming, or

                            can be assigned to a line\-side optical channel for

                            transmission.  Each assignment also has an associated

                            bandwidth allocation.

                            .. data:: LOGICAL_CHANNEL = 0

                            	Subsequent channel is a logical channel

                            .. data:: OPTICAL_CHANNEL = 1

                            	Subsequent channel is a optical channel / carrier

                            """

                            LOGICAL_CHANNEL = 0

                            OPTICAL_CHANNEL = 1


                            @staticmethod
                            def _meta_info():
                                from ydk.models.openconfig._meta import _openconfig_terminal_device as meta
                                return meta._meta_table['TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment.State.AssignmentTypeEnum']


                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/openconfig-terminal-device:state'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.allocation is not None:
                                return True

                            if self.assignment_type is not None:
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
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.index is None:
                            raise YPYModelError('Key property index is None')

                        return self.parent._common_path +'/openconfig-terminal-device:assignment[openconfig-terminal-device:index = ' + str(self.index) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
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
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/openconfig-terminal-device:logical-channel-assignments'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.assignment is not None:
                        for child_ref in self.assignment:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_terminal_device as meta
                    return meta._meta_table['TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments']['meta_info']

            @property
            def _common_path(self):
                if self.index is None:
                    raise YPYModelError('Key property index is None')

                return '/openconfig-terminal-device:terminal-device/openconfig-terminal-device:logical-channels/openconfig-terminal-device:channel[openconfig-terminal-device:index = ' + str(self.index) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.index is not None:
                    return True

                if self.config is not None and self.config._has_data():
                    return True

                if self.ethernet is not None and self.ethernet._has_data():
                    return True

                if self.ingress is not None and self.ingress._has_data():
                    return True

                if self.logical_channel_assignments is not None and self.logical_channel_assignments._has_data():
                    return True

                if self.otn is not None and self.otn._has_data():
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
        Enclosing container for list of operational modes
        
        .. attribute:: mode
        
        	List of operational modes supported by the platform. The operational mode provides a platform\-defined summary of information such as symbol rate, modulation, pulse shaping, etc
        	**type**\: list of    :py:class:`Mode <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.OperationalModes.Mode>`
        
        

        """

        _prefix = 'oc-opt-term'
        _revision = '2016-06-17'

        def __init__(self):
            self.parent = None
            self.mode = YList()
            self.mode.parent = self
            self.mode.name = 'mode'


        class Mode(object):
            """
            List of operational modes supported by the platform.
            The operational mode provides a platform\-defined summary
            of information such as symbol rate, modulation, pulse
            shaping, etc.
            
            .. attribute:: mode_id  <key>
            
            	Reference to mode\-id
            	**type**\:  int
            
            	**range:** 0..65535
            
            	**refers to**\:  :py:class:`mode_id <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.OperationalModes.Mode.State>`
            
            .. attribute:: config
            
            	Configuration data for operational mode
            	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.OperationalModes.Mode.Config>`
            
            .. attribute:: state
            
            	Operational state data for the platform\-defined operational mode
            	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.OperationalModes.Mode.State>`
            
            

            """

            _prefix = 'oc-opt-term'
            _revision = '2016-06-17'

            def __init__(self):
                self.parent = None
                self.mode_id = None
                self.config = TerminalDevice.OperationalModes.Mode.Config()
                self.config.parent = self
                self.state = TerminalDevice.OperationalModes.Mode.State()
                self.state.parent = self


            class Config(object):
                """
                Configuration data for operational mode
                
                

                """

                _prefix = 'oc-opt-term'
                _revision = '2016-06-17'

                def __init__(self):
                    self.parent = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/openconfig-terminal-device:config'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_terminal_device as meta
                    return meta._meta_table['TerminalDevice.OperationalModes.Mode.Config']['meta_info']


            class State(object):
                """
                Operational state data for the platform\-defined
                operational mode
                
                .. attribute:: description
                
                	Vendor\-supplied textual description of the characteristics of this operational mode to enable operators to select the appropriate mode for the application
                	**type**\:  str
                
                .. attribute:: mode_id
                
                	Two\-octet encoding of the vendor\-defined operational mode
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: vendor_id
                
                	Identifier to represent the vendor / supplier of the platform and the associated operational mode information
                	**type**\:  str
                
                

                """

                _prefix = 'oc-opt-term'
                _revision = '2016-06-17'

                def __init__(self):
                    self.parent = None
                    self.description = None
                    self.mode_id = None
                    self.vendor_id = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/openconfig-terminal-device:state'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.description is not None:
                        return True

                    if self.mode_id is not None:
                        return True

                    if self.vendor_id is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_terminal_device as meta
                    return meta._meta_table['TerminalDevice.OperationalModes.Mode.State']['meta_info']

            @property
            def _common_path(self):
                if self.mode_id is None:
                    raise YPYModelError('Key property mode_id is None')

                return '/openconfig-terminal-device:terminal-device/openconfig-terminal-device:operational-modes/openconfig-terminal-device:mode[openconfig-terminal-device:mode-id = ' + str(self.mode_id) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.mode_id is not None:
                    return True

                if self.config is not None and self.config._has_data():
                    return True

                if self.state is not None and self.state._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.openconfig._meta import _openconfig_terminal_device as meta
                return meta._meta_table['TerminalDevice.OperationalModes.Mode']['meta_info']

        @property
        def _common_path(self):

            return '/openconfig-terminal-device:terminal-device/openconfig-terminal-device:operational-modes'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.mode is not None:
                for child_ref in self.mode:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.openconfig._meta import _openconfig_terminal_device as meta
            return meta._meta_table['TerminalDevice.OperationalModes']['meta_info']

    @property
    def _common_path(self):

        return '/openconfig-terminal-device:terminal-device'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.config is not None and self.config._has_data():
            return True

        if self.logical_channels is not None and self.logical_channels._has_data():
            return True

        if self.operational_modes is not None and self.operational_modes._has_data():
            return True

        if self.state is not None and self.state._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_terminal_device as meta
        return meta._meta_table['TerminalDevice']['meta_info']


