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
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class TerminalDevice(Entity):
    """
    Top\-level container for the terminal device
    
    .. attribute:: config
    
    	Configuration data for global terminal\-device
    	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.Config>`
    
    .. attribute:: state
    
    	Operational state data for global terminal device
    	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.State>`
    
    .. attribute:: logical_channels
    
    	Enclosing container the list of logical channels
    	**type**\:  :py:class:`LogicalChannels <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels>`
    
    .. attribute:: operational_modes
    
    	Enclosing container for list of operational modes
    	**type**\:  :py:class:`OperationalModes <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.OperationalModes>`
    
    

    """

    _prefix = 'oc-opt-term'
    _revision = '2016-06-17'

    def __init__(self):
        super(TerminalDevice, self).__init__()
        self._top_entity = None

        self.yang_name = "terminal-device"
        self.yang_parent_name = "openconfig-terminal-device"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("config", ("config", TerminalDevice.Config)), ("state", ("state", TerminalDevice.State)), ("logical-channels", ("logical_channels", TerminalDevice.LogicalChannels)), ("operational-modes", ("operational_modes", TerminalDevice.OperationalModes))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.config = TerminalDevice.Config()
        self.config.parent = self
        self._children_name_map["config"] = "config"
        self._children_yang_names.add("config")

        self.state = TerminalDevice.State()
        self.state.parent = self
        self._children_name_map["state"] = "state"
        self._children_yang_names.add("state")

        self.logical_channels = TerminalDevice.LogicalChannels()
        self.logical_channels.parent = self
        self._children_name_map["logical_channels"] = "logical-channels"
        self._children_yang_names.add("logical-channels")

        self.operational_modes = TerminalDevice.OperationalModes()
        self.operational_modes.parent = self
        self._children_name_map["operational_modes"] = "operational-modes"
        self._children_yang_names.add("operational-modes")
        self._segment_path = lambda: "openconfig-terminal-device:terminal-device"


    class Config(Entity):
        """
        Configuration data for global terminal\-device
        
        

        """

        _prefix = 'oc-opt-term'
        _revision = '2016-06-17'

        def __init__(self):
            super(TerminalDevice.Config, self).__init__()

            self.yang_name = "config"
            self.yang_parent_name = "terminal-device"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict()
            self._segment_path = lambda: "config"
            self._absolute_path = lambda: "openconfig-terminal-device:terminal-device/%s" % self._segment_path()


    class State(Entity):
        """
        Operational state data for global terminal device
        
        

        """

        _prefix = 'oc-opt-term'
        _revision = '2016-06-17'

        def __init__(self):
            super(TerminalDevice.State, self).__init__()

            self.yang_name = "state"
            self.yang_parent_name = "terminal-device"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict()
            self._segment_path = lambda: "state"
            self._absolute_path = lambda: "openconfig-terminal-device:terminal-device/%s" % self._segment_path()


    class LogicalChannels(Entity):
        """
        Enclosing container the list of logical channels
        
        .. attribute:: channel
        
        	List of logical channels
        	**type**\: list of  		 :py:class:`Channel <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel>`
        
        

        """

        _prefix = 'oc-opt-term'
        _revision = '2016-06-17'

        def __init__(self):
            super(TerminalDevice.LogicalChannels, self).__init__()

            self.yang_name = "logical-channels"
            self.yang_parent_name = "terminal-device"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("channel", ("channel", TerminalDevice.LogicalChannels.Channel))])
            self._leafs = OrderedDict()

            self.channel = YList(self)
            self._segment_path = lambda: "logical-channels"
            self._absolute_path = lambda: "openconfig-terminal-device:terminal-device/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(TerminalDevice.LogicalChannels, [], name, value)


        class Channel(Entity):
            """
            List of logical channels
            
            .. attribute:: index  (key)
            
            	Reference to the index of the logical channel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`index <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel.Config>`
            
            .. attribute:: config
            
            	Configuration data for logical channels
            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel.Config>`
            
            .. attribute:: state
            
            	Operational state data for logical channels
            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel.State>`
            
            .. attribute:: otn
            
            	Top level container for OTU configuration when logical channel framing is using an OTU protocol, e.g., OTU1, OTU3, etc
            	**type**\:  :py:class:`Otn <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel.Otn>`
            
            .. attribute:: ethernet
            
            	Top level container for data related to Ethernet framing for the logical channel
            	**type**\:  :py:class:`Ethernet <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel.Ethernet>`
            
            .. attribute:: ingress
            
            	Top\-level container for specifying references to the source of signal for the logical channel, either a transceiver or individual physical channels
            	**type**\:  :py:class:`Ingress <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel.Ingress>`
            
            .. attribute:: logical_channel_assignments
            
            	Enclosing container for tributary assignments
            	**type**\:  :py:class:`LogicalChannelAssignments <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments>`
            
            

            """

            _prefix = 'oc-opt-term'
            _revision = '2016-06-17'

            def __init__(self):
                super(TerminalDevice.LogicalChannels.Channel, self).__init__()

                self.yang_name = "channel"
                self.yang_parent_name = "logical-channels"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['index']
                self._child_container_classes = OrderedDict([("config", ("config", TerminalDevice.LogicalChannels.Channel.Config)), ("state", ("state", TerminalDevice.LogicalChannels.Channel.State)), ("otn", ("otn", TerminalDevice.LogicalChannels.Channel.Otn)), ("ethernet", ("ethernet", TerminalDevice.LogicalChannels.Channel.Ethernet)), ("ingress", ("ingress", TerminalDevice.LogicalChannels.Channel.Ingress)), ("logical-channel-assignments", ("logical_channel_assignments", TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('index', YLeaf(YType.str, 'index')),
                ])
                self.index = None

                self.config = TerminalDevice.LogicalChannels.Channel.Config()
                self.config.parent = self
                self._children_name_map["config"] = "config"
                self._children_yang_names.add("config")

                self.state = TerminalDevice.LogicalChannels.Channel.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"
                self._children_yang_names.add("state")

                self.otn = TerminalDevice.LogicalChannels.Channel.Otn()
                self.otn.parent = self
                self._children_name_map["otn"] = "otn"
                self._children_yang_names.add("otn")

                self.ethernet = TerminalDevice.LogicalChannels.Channel.Ethernet()
                self.ethernet.parent = self
                self._children_name_map["ethernet"] = "ethernet"
                self._children_yang_names.add("ethernet")

                self.ingress = TerminalDevice.LogicalChannels.Channel.Ingress()
                self.ingress.parent = self
                self._children_name_map["ingress"] = "ingress"
                self._children_yang_names.add("ingress")

                self.logical_channel_assignments = TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments()
                self.logical_channel_assignments.parent = self
                self._children_name_map["logical_channel_assignments"] = "logical-channel-assignments"
                self._children_yang_names.add("logical-channel-assignments")
                self._segment_path = lambda: "channel" + "[index='" + str(self.index) + "']"
                self._absolute_path = lambda: "openconfig-terminal-device:terminal-device/logical-channels/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(TerminalDevice.LogicalChannels.Channel, ['index'], name, value)


            class Config(Entity):
                """
                Configuration data for logical channels
                
                .. attribute:: index
                
                	Index of the current logical channel
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: description
                
                	Description of the logical channel
                	**type**\: str
                
                .. attribute:: admin_state
                
                	Sets the admin state of the logical channel
                	**type**\:  :py:class:`AdminStateType <ydk.models.openconfig.openconfig_transport_types.AdminStateType>`
                
                .. attribute:: rate_class
                
                	Rounded bit rate of the tributary signal. Exact bit rate will be refined by protocol selection
                	**type**\:  :py:class:`TRIBUTARYRATECLASSTYPE <ydk.models.openconfig.openconfig_transport_types.TRIBUTARYRATECLASSTYPE>`
                
                .. attribute:: trib_protocol
                
                	Protocol framing of the tributary signal. If this LogicalChannel is directly connected to a Client\-Port or Optical\-Channel, this is the protocol of the associated port. If the LogicalChannel is connected to other LogicalChannels, the TributaryProtocol of the LogicalChannels will define a specific mapping/demapping or multiplexing/demultiplexing function.  Not all protocols are valid, depending on the value of trib\-rate\-class.  The expectation is that the NMS will validate that a correct combination of rate class and protocol are specfied.  Basic combinations are\:  rate class\: 1G protocols\: 1GE  rate class\: 2.5G protocols\: OC48, STM16  rate class\: 10G protocols\:  10GE LAN, 10GE WAN, OC192, STM64, OTU2, OTU2e,            OTU1e, ODU2, ODU2e, ODU1e  rate class\: 40G protocols\:  40GE, OC768, STM256, OTU3, ODU3  rate class\: 100G protocols\:  100GE, 100G MLG, OTU4, OTUCn, ODU4
                	**type**\:  :py:class:`TRIBUTARYPROTOCOLTYPE <ydk.models.openconfig.openconfig_transport_types.TRIBUTARYPROTOCOLTYPE>`
                
                .. attribute:: logical_channel_type
                
                	The type / stage of the logical element determines the configuration and operational state parameters (PMs) available for the logical element
                	**type**\:  :py:class:`LOGICALELEMENTPROTOCOLTYPE <ydk.models.openconfig.openconfig_transport_types.LOGICALELEMENTPROTOCOLTYPE>`
                
                .. attribute:: loopback_mode
                
                	Sets the loopback type on the logical channel. Setting the mode to something besides NONE activates the loopback in the specified mode
                	**type**\:  :py:class:`LoopbackModeType <ydk.models.openconfig.openconfig_transport_types.LoopbackModeType>`
                
                

                """

                _prefix = 'oc-opt-term'
                _revision = '2016-06-17'

                def __init__(self):
                    super(TerminalDevice.LogicalChannels.Channel.Config, self).__init__()

                    self.yang_name = "config"
                    self.yang_parent_name = "channel"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('index', YLeaf(YType.uint32, 'index')),
                        ('description', YLeaf(YType.str, 'description')),
                        ('admin_state', YLeaf(YType.enumeration, 'admin-state')),
                        ('rate_class', YLeaf(YType.identityref, 'rate-class')),
                        ('trib_protocol', YLeaf(YType.identityref, 'trib-protocol')),
                        ('logical_channel_type', YLeaf(YType.identityref, 'logical-channel-type')),
                        ('loopback_mode', YLeaf(YType.enumeration, 'loopback-mode')),
                    ])
                    self.index = None
                    self.description = None
                    self.admin_state = None
                    self.rate_class = None
                    self.trib_protocol = None
                    self.logical_channel_type = None
                    self.loopback_mode = None
                    self._segment_path = lambda: "config"

                def __setattr__(self, name, value):
                    self._perform_setattr(TerminalDevice.LogicalChannels.Channel.Config, ['index', 'description', 'admin_state', 'rate_class', 'trib_protocol', 'logical_channel_type', 'loopback_mode'], name, value)


            class State(Entity):
                """
                Operational state data for logical channels
                
                .. attribute:: index
                
                	Index of the current logical channel
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: description
                
                	Description of the logical channel
                	**type**\: str
                
                .. attribute:: admin_state
                
                	Sets the admin state of the logical channel
                	**type**\:  :py:class:`AdminStateType <ydk.models.openconfig.openconfig_transport_types.AdminStateType>`
                
                .. attribute:: rate_class
                
                	Rounded bit rate of the tributary signal. Exact bit rate will be refined by protocol selection
                	**type**\:  :py:class:`TRIBUTARYRATECLASSTYPE <ydk.models.openconfig.openconfig_transport_types.TRIBUTARYRATECLASSTYPE>`
                
                .. attribute:: trib_protocol
                
                	Protocol framing of the tributary signal. If this LogicalChannel is directly connected to a Client\-Port or Optical\-Channel, this is the protocol of the associated port. If the LogicalChannel is connected to other LogicalChannels, the TributaryProtocol of the LogicalChannels will define a specific mapping/demapping or multiplexing/demultiplexing function.  Not all protocols are valid, depending on the value of trib\-rate\-class.  The expectation is that the NMS will validate that a correct combination of rate class and protocol are specfied.  Basic combinations are\:  rate class\: 1G protocols\: 1GE  rate class\: 2.5G protocols\: OC48, STM16  rate class\: 10G protocols\:  10GE LAN, 10GE WAN, OC192, STM64, OTU2, OTU2e,            OTU1e, ODU2, ODU2e, ODU1e  rate class\: 40G protocols\:  40GE, OC768, STM256, OTU3, ODU3  rate class\: 100G protocols\:  100GE, 100G MLG, OTU4, OTUCn, ODU4
                	**type**\:  :py:class:`TRIBUTARYPROTOCOLTYPE <ydk.models.openconfig.openconfig_transport_types.TRIBUTARYPROTOCOLTYPE>`
                
                .. attribute:: logical_channel_type
                
                	The type / stage of the logical element determines the configuration and operational state parameters (PMs) available for the logical element
                	**type**\:  :py:class:`LOGICALELEMENTPROTOCOLTYPE <ydk.models.openconfig.openconfig_transport_types.LOGICALELEMENTPROTOCOLTYPE>`
                
                .. attribute:: loopback_mode
                
                	Sets the loopback type on the logical channel. Setting the mode to something besides NONE activates the loopback in the specified mode
                	**type**\:  :py:class:`LoopbackModeType <ydk.models.openconfig.openconfig_transport_types.LoopbackModeType>`
                
                .. attribute:: link_state
                
                	Link\-state of the Ethernet protocol on the logical channel, SONET / SDH framed signal, etc
                	**type**\:  :py:class:`LinkState <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel.State.LinkState>`
                
                

                """

                _prefix = 'oc-opt-term'
                _revision = '2016-06-17'

                def __init__(self):
                    super(TerminalDevice.LogicalChannels.Channel.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "channel"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('index', YLeaf(YType.uint32, 'index')),
                        ('description', YLeaf(YType.str, 'description')),
                        ('admin_state', YLeaf(YType.enumeration, 'admin-state')),
                        ('rate_class', YLeaf(YType.identityref, 'rate-class')),
                        ('trib_protocol', YLeaf(YType.identityref, 'trib-protocol')),
                        ('logical_channel_type', YLeaf(YType.identityref, 'logical-channel-type')),
                        ('loopback_mode', YLeaf(YType.enumeration, 'loopback-mode')),
                        ('link_state', YLeaf(YType.enumeration, 'link-state')),
                    ])
                    self.index = None
                    self.description = None
                    self.admin_state = None
                    self.rate_class = None
                    self.trib_protocol = None
                    self.logical_channel_type = None
                    self.loopback_mode = None
                    self.link_state = None
                    self._segment_path = lambda: "state"

                def __setattr__(self, name, value):
                    self._perform_setattr(TerminalDevice.LogicalChannels.Channel.State, ['index', 'description', 'admin_state', 'rate_class', 'trib_protocol', 'logical_channel_type', 'loopback_mode', 'link_state'], name, value)

                class LinkState(Enum):
                    """
                    LinkState (Enum Class)

                    Link\-state of the Ethernet protocol on the logical channel,

                    SONET / SDH framed signal, etc.

                    .. data:: UP = 0

                    	Logical channel is operationally up

                    .. data:: DOWN = 1

                    	Logical channel is operationally down

                    """

                    UP = Enum.YLeaf(0, "UP")

                    DOWN = Enum.YLeaf(1, "DOWN")



            class Otn(Entity):
                """
                Top level container for OTU configuration when logical
                channel framing is using an OTU protocol, e.g., OTU1, OTU3,
                etc.
                
                .. attribute:: config
                
                	Configuration data for OTN protocol framing
                	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel.Otn.Config>`
                
                .. attribute:: state
                
                	Operational state data for OTN protocol PMs, statistics, etc
                	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel.Otn.State>`
                
                

                """

                _prefix = 'oc-opt-term'
                _revision = '2016-06-17'

                def __init__(self):
                    super(TerminalDevice.LogicalChannels.Channel.Otn, self).__init__()

                    self.yang_name = "otn"
                    self.yang_parent_name = "channel"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("config", ("config", TerminalDevice.LogicalChannels.Channel.Otn.Config)), ("state", ("state", TerminalDevice.LogicalChannels.Channel.Otn.State))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict()

                    self.config = TerminalDevice.LogicalChannels.Channel.Otn.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"
                    self._children_yang_names.add("config")

                    self.state = TerminalDevice.LogicalChannels.Channel.Otn.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._children_yang_names.add("state")
                    self._segment_path = lambda: "otn"


                class Config(Entity):
                    """
                    Configuration data for OTN protocol framing
                    
                    .. attribute:: tti_msg_transmit
                    
                    	Trail trace identifier (TTI) message transmitted
                    	**type**\: str
                    
                    .. attribute:: tti_msg_expected
                    
                    	Trail trace identifier (TTI) message expected
                    	**type**\: str
                    
                    .. attribute:: tti_msg_auto
                    
                    	Trail trace identifier (TTI) transmit message automatically created. If True, then setting a custom transmit message would be invalid
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'oc-opt-term'
                    _revision = '2016-06-17'

                    def __init__(self):
                        super(TerminalDevice.LogicalChannels.Channel.Otn.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "otn"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('tti_msg_transmit', YLeaf(YType.str, 'tti-msg-transmit')),
                            ('tti_msg_expected', YLeaf(YType.str, 'tti-msg-expected')),
                            ('tti_msg_auto', YLeaf(YType.boolean, 'tti-msg-auto')),
                        ])
                        self.tti_msg_transmit = None
                        self.tti_msg_expected = None
                        self.tti_msg_auto = None
                        self._segment_path = lambda: "config"

                    def __setattr__(self, name, value):
                        self._perform_setattr(TerminalDevice.LogicalChannels.Channel.Otn.Config, ['tti_msg_transmit', 'tti_msg_expected', 'tti_msg_auto'], name, value)


                class State(Entity):
                    """
                    Operational state data for OTN protocol PMs, statistics,
                    etc.
                    
                    .. attribute:: tti_msg_transmit
                    
                    	Trail trace identifier (TTI) message transmitted
                    	**type**\: str
                    
                    .. attribute:: tti_msg_expected
                    
                    	Trail trace identifier (TTI) message expected
                    	**type**\: str
                    
                    .. attribute:: tti_msg_auto
                    
                    	Trail trace identifier (TTI) transmit message automatically created. If True, then setting a custom transmit message would be invalid
                    	**type**\: bool
                    
                    .. attribute:: tti_msg_recv
                    
                    	Trail trace identifier (TTI) message received
                    	**type**\: str
                    
                    .. attribute:: rdi_msg
                    
                    	Remote defect indication (RDI) message received
                    	**type**\: str
                    
                    .. attribute:: errored_seconds
                    
                    	The number of seconds that at least one errored blocks occurs, at least one code violation occurs, loss of sync is detected or loss of signal is detected
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: severely_errored_seconds
                    
                    	The number of seconds that loss of frame is detected OR the number of errored blocks, code violations, loss of sync or loss of signal is detected exceeds a predefined threshold
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: unavailable_seconds
                    
                    	The number of seconds during which the link is unavailable
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: code_violations
                    
                    	For ethernet or fiberchannel links, the number of 8b/10b coding violations. For SONET/SDH, the number of BIP (bit interleaved parity) errors
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: fec_uncorrectable_words
                    
                    	The number words that were uncorrectable by the FEC
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: fec_corrected_bytes
                    
                    	The number of bytes that were corrected by the FEC
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: fec_corrected_bits
                    
                    	The number of bits that were corrected by the FEC
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: background_block_errors
                    
                    	The number of background block errors
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: pre_fec_ber
                    
                    	Bit error rate before forward error correction \-\- computed value
                    	**type**\:  :py:class:`PreFecBer <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel.Otn.State.PreFecBer>`
                    
                    .. attribute:: post_fec_ber
                    
                    	Bit error rate after forward error correction \-\- computed value
                    	**type**\:  :py:class:`PostFecBer <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel.Otn.State.PostFecBer>`
                    
                    .. attribute:: q_value
                    
                    	Quality value (factor) of a channel
                    	**type**\:  :py:class:`QValue <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel.Otn.State.QValue>`
                    
                    .. attribute:: esnr
                    
                    	Electrical signal to noise ratio. Baud rate normalized signal to noise ratio based on error vector magnitude
                    	**type**\:  :py:class:`Esnr <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel.Otn.State.Esnr>`
                    
                    

                    """

                    _prefix = 'oc-opt-term'
                    _revision = '2016-06-17'

                    def __init__(self):
                        super(TerminalDevice.LogicalChannels.Channel.Otn.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "otn"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("pre-fec-ber", ("pre_fec_ber", TerminalDevice.LogicalChannels.Channel.Otn.State.PreFecBer)), ("post-fec-ber", ("post_fec_ber", TerminalDevice.LogicalChannels.Channel.Otn.State.PostFecBer)), ("q-value", ("q_value", TerminalDevice.LogicalChannels.Channel.Otn.State.QValue)), ("esnr", ("esnr", TerminalDevice.LogicalChannels.Channel.Otn.State.Esnr))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('tti_msg_transmit', YLeaf(YType.str, 'tti-msg-transmit')),
                            ('tti_msg_expected', YLeaf(YType.str, 'tti-msg-expected')),
                            ('tti_msg_auto', YLeaf(YType.boolean, 'tti-msg-auto')),
                            ('tti_msg_recv', YLeaf(YType.str, 'tti-msg-recv')),
                            ('rdi_msg', YLeaf(YType.str, 'rdi-msg')),
                            ('errored_seconds', YLeaf(YType.uint64, 'errored-seconds')),
                            ('severely_errored_seconds', YLeaf(YType.uint64, 'severely-errored-seconds')),
                            ('unavailable_seconds', YLeaf(YType.uint64, 'unavailable-seconds')),
                            ('code_violations', YLeaf(YType.uint64, 'code-violations')),
                            ('fec_uncorrectable_words', YLeaf(YType.uint64, 'fec-uncorrectable-words')),
                            ('fec_corrected_bytes', YLeaf(YType.uint64, 'fec-corrected-bytes')),
                            ('fec_corrected_bits', YLeaf(YType.uint64, 'fec-corrected-bits')),
                            ('background_block_errors', YLeaf(YType.uint64, 'background-block-errors')),
                        ])
                        self.tti_msg_transmit = None
                        self.tti_msg_expected = None
                        self.tti_msg_auto = None
                        self.tti_msg_recv = None
                        self.rdi_msg = None
                        self.errored_seconds = None
                        self.severely_errored_seconds = None
                        self.unavailable_seconds = None
                        self.code_violations = None
                        self.fec_uncorrectable_words = None
                        self.fec_corrected_bytes = None
                        self.fec_corrected_bits = None
                        self.background_block_errors = None

                        self.pre_fec_ber = TerminalDevice.LogicalChannels.Channel.Otn.State.PreFecBer()
                        self.pre_fec_ber.parent = self
                        self._children_name_map["pre_fec_ber"] = "pre-fec-ber"
                        self._children_yang_names.add("pre-fec-ber")

                        self.post_fec_ber = TerminalDevice.LogicalChannels.Channel.Otn.State.PostFecBer()
                        self.post_fec_ber.parent = self
                        self._children_name_map["post_fec_ber"] = "post-fec-ber"
                        self._children_yang_names.add("post-fec-ber")

                        self.q_value = TerminalDevice.LogicalChannels.Channel.Otn.State.QValue()
                        self.q_value.parent = self
                        self._children_name_map["q_value"] = "q-value"
                        self._children_yang_names.add("q-value")

                        self.esnr = TerminalDevice.LogicalChannels.Channel.Otn.State.Esnr()
                        self.esnr.parent = self
                        self._children_name_map["esnr"] = "esnr"
                        self._children_yang_names.add("esnr")
                        self._segment_path = lambda: "state"

                    def __setattr__(self, name, value):
                        self._perform_setattr(TerminalDevice.LogicalChannels.Channel.Otn.State, ['tti_msg_transmit', 'tti_msg_expected', 'tti_msg_auto', 'tti_msg_recv', 'rdi_msg', 'errored_seconds', 'severely_errored_seconds', 'unavailable_seconds', 'code_violations', 'fec_uncorrectable_words', 'fec_corrected_bytes', 'fec_corrected_bits', 'background_block_errors'], name, value)


                    class PreFecBer(Entity):
                        """
                        Bit error rate before forward error correction \-\- computed
                        value
                        
                        .. attribute:: instant
                        
                        	The instantaneous value of the statistic
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-922337203685477580.8..922337203685477580.7
                        
                        .. attribute:: avg
                        
                        	The arithmetic mean value of the statistic over the sampling period
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-922337203685477580.8..922337203685477580.7
                        
                        .. attribute:: min
                        
                        	The minimum value of the statistic over the sampling period
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-922337203685477580.8..922337203685477580.7
                        
                        .. attribute:: max
                        
                        	The maximum value of the statitic over the sampling period
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-922337203685477580.8..922337203685477580.7
                        
                        

                        """

                        _prefix = 'oc-opt-term'
                        _revision = '2016-06-17'

                        def __init__(self):
                            super(TerminalDevice.LogicalChannels.Channel.Otn.State.PreFecBer, self).__init__()

                            self.yang_name = "pre-fec-ber"
                            self.yang_parent_name = "state"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('instant', YLeaf(YType.str, 'instant')),
                                ('avg', YLeaf(YType.str, 'avg')),
                                ('min', YLeaf(YType.str, 'min')),
                                ('max', YLeaf(YType.str, 'max')),
                            ])
                            self.instant = None
                            self.avg = None
                            self.min = None
                            self.max = None
                            self._segment_path = lambda: "pre-fec-ber"

                        def __setattr__(self, name, value):
                            self._perform_setattr(TerminalDevice.LogicalChannels.Channel.Otn.State.PreFecBer, ['instant', 'avg', 'min', 'max'], name, value)


                    class PostFecBer(Entity):
                        """
                        Bit error rate after forward error correction \-\- computed
                        value
                        
                        .. attribute:: instant
                        
                        	The instantaneous value of the statistic
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-922337203685477580.8..922337203685477580.7
                        
                        .. attribute:: avg
                        
                        	The arithmetic mean value of the statistic over the sampling period
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-922337203685477580.8..922337203685477580.7
                        
                        .. attribute:: min
                        
                        	The minimum value of the statistic over the sampling period
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-922337203685477580.8..922337203685477580.7
                        
                        .. attribute:: max
                        
                        	The maximum value of the statitic over the sampling period
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-922337203685477580.8..922337203685477580.7
                        
                        

                        """

                        _prefix = 'oc-opt-term'
                        _revision = '2016-06-17'

                        def __init__(self):
                            super(TerminalDevice.LogicalChannels.Channel.Otn.State.PostFecBer, self).__init__()

                            self.yang_name = "post-fec-ber"
                            self.yang_parent_name = "state"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('instant', YLeaf(YType.str, 'instant')),
                                ('avg', YLeaf(YType.str, 'avg')),
                                ('min', YLeaf(YType.str, 'min')),
                                ('max', YLeaf(YType.str, 'max')),
                            ])
                            self.instant = None
                            self.avg = None
                            self.min = None
                            self.max = None
                            self._segment_path = lambda: "post-fec-ber"

                        def __setattr__(self, name, value):
                            self._perform_setattr(TerminalDevice.LogicalChannels.Channel.Otn.State.PostFecBer, ['instant', 'avg', 'min', 'max'], name, value)


                    class QValue(Entity):
                        """
                        Quality value (factor) of a channel
                        
                        .. attribute:: instant
                        
                        	The instantaneous value of the statistic
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-922337203685477580.8..922337203685477580.7
                        
                        .. attribute:: avg
                        
                        	The arithmetic mean value of the statistic over the sampling period
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-922337203685477580.8..922337203685477580.7
                        
                        .. attribute:: min
                        
                        	The minimum value of the statistic over the sampling period
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-922337203685477580.8..922337203685477580.7
                        
                        .. attribute:: max
                        
                        	The maximum value of the statitic over the sampling period
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-922337203685477580.8..922337203685477580.7
                        
                        

                        """

                        _prefix = 'oc-opt-term'
                        _revision = '2016-06-17'

                        def __init__(self):
                            super(TerminalDevice.LogicalChannels.Channel.Otn.State.QValue, self).__init__()

                            self.yang_name = "q-value"
                            self.yang_parent_name = "state"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('instant', YLeaf(YType.str, 'instant')),
                                ('avg', YLeaf(YType.str, 'avg')),
                                ('min', YLeaf(YType.str, 'min')),
                                ('max', YLeaf(YType.str, 'max')),
                            ])
                            self.instant = None
                            self.avg = None
                            self.min = None
                            self.max = None
                            self._segment_path = lambda: "q-value"

                        def __setattr__(self, name, value):
                            self._perform_setattr(TerminalDevice.LogicalChannels.Channel.Otn.State.QValue, ['instant', 'avg', 'min', 'max'], name, value)


                    class Esnr(Entity):
                        """
                        Electrical signal to noise ratio. Baud rate
                        normalized signal to noise ratio based on
                        error vector magnitude
                        
                        .. attribute:: instant
                        
                        	The instantaneous value of the statistic
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-922337203685477580.8..922337203685477580.7
                        
                        .. attribute:: avg
                        
                        	The arithmetic mean value of the statistic over the sampling period
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-922337203685477580.8..922337203685477580.7
                        
                        .. attribute:: min
                        
                        	The minimum value of the statistic over the sampling period
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-922337203685477580.8..922337203685477580.7
                        
                        .. attribute:: max
                        
                        	The maximum value of the statitic over the sampling period
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-922337203685477580.8..922337203685477580.7
                        
                        

                        """

                        _prefix = 'oc-opt-term'
                        _revision = '2016-06-17'

                        def __init__(self):
                            super(TerminalDevice.LogicalChannels.Channel.Otn.State.Esnr, self).__init__()

                            self.yang_name = "esnr"
                            self.yang_parent_name = "state"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('instant', YLeaf(YType.str, 'instant')),
                                ('avg', YLeaf(YType.str, 'avg')),
                                ('min', YLeaf(YType.str, 'min')),
                                ('max', YLeaf(YType.str, 'max')),
                            ])
                            self.instant = None
                            self.avg = None
                            self.min = None
                            self.max = None
                            self._segment_path = lambda: "esnr"

                        def __setattr__(self, name, value):
                            self._perform_setattr(TerminalDevice.LogicalChannels.Channel.Otn.State.Esnr, ['instant', 'avg', 'min', 'max'], name, value)


            class Ethernet(Entity):
                """
                Top level container for data related to Ethernet framing
                for the logical channel
                
                .. attribute:: config
                
                	Configuration data for Ethernet protocol framing on logical channels
                	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel.Ethernet.Config>`
                
                .. attribute:: state
                
                	Operational state data for Ethernet protocol framing on logical channels
                	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel.Ethernet.State>`
                
                

                """

                _prefix = 'oc-opt-term'
                _revision = '2016-06-17'

                def __init__(self):
                    super(TerminalDevice.LogicalChannels.Channel.Ethernet, self).__init__()

                    self.yang_name = "ethernet"
                    self.yang_parent_name = "channel"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("config", ("config", TerminalDevice.LogicalChannels.Channel.Ethernet.Config)), ("state", ("state", TerminalDevice.LogicalChannels.Channel.Ethernet.State))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict()

                    self.config = TerminalDevice.LogicalChannels.Channel.Ethernet.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"
                    self._children_yang_names.add("config")

                    self.state = TerminalDevice.LogicalChannels.Channel.Ethernet.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._children_yang_names.add("state")
                    self._segment_path = lambda: "ethernet"


                class Config(Entity):
                    """
                    Configuration data for Ethernet protocol framing on logical
                    channels
                    
                    

                    """

                    _prefix = 'oc-opt-term'
                    _revision = '2016-06-17'

                    def __init__(self):
                        super(TerminalDevice.LogicalChannels.Channel.Ethernet.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "ethernet"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict()
                        self._segment_path = lambda: "config"


                class State(Entity):
                    """
                    Operational state data for Ethernet protocol framing on logical
                    channels
                    
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
                    
                    .. attribute:: in_jabber_frames
                    
                    	Number of jabber frames received on the interface.  Jabber frames are typically defined as oversize frames which also have a bad CRC.  Implementations may use slightly different definitions of what constitutes a jabber frame.  Often indicative of a NIC hardware problem
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: in_fragment_frames
                    
                    	Number of fragment frames received on the interface
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: in_8021q_frames
                    
                    	Number of 802.1q tagged frames received on the interface
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: in_crc_errors
                    
                    	Number of receive error events due to FCS/CRC check failure
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
                    
                    .. attribute:: out_8021q_frames
                    
                    	Number of 802.1q tagged frames sent on the interface
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'oc-opt-term'
                    _revision = '2016-06-17'

                    def __init__(self):
                        super(TerminalDevice.LogicalChannels.Channel.Ethernet.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "ethernet"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('in_mac_control_frames', YLeaf(YType.uint64, 'in-mac-control-frames')),
                            ('in_mac_pause_frames', YLeaf(YType.uint64, 'in-mac-pause-frames')),
                            ('in_oversize_frames', YLeaf(YType.uint64, 'in-oversize-frames')),
                            ('in_jabber_frames', YLeaf(YType.uint64, 'in-jabber-frames')),
                            ('in_fragment_frames', YLeaf(YType.uint64, 'in-fragment-frames')),
                            ('in_8021q_frames', YLeaf(YType.uint64, 'in-8021q-frames')),
                            ('in_crc_errors', YLeaf(YType.uint64, 'in-crc-errors')),
                            ('out_mac_control_frames', YLeaf(YType.uint64, 'out-mac-control-frames')),
                            ('out_mac_pause_frames', YLeaf(YType.uint64, 'out-mac-pause-frames')),
                            ('out_8021q_frames', YLeaf(YType.uint64, 'out-8021q-frames')),
                        ])
                        self.in_mac_control_frames = None
                        self.in_mac_pause_frames = None
                        self.in_oversize_frames = None
                        self.in_jabber_frames = None
                        self.in_fragment_frames = None
                        self.in_8021q_frames = None
                        self.in_crc_errors = None
                        self.out_mac_control_frames = None
                        self.out_mac_pause_frames = None
                        self.out_8021q_frames = None
                        self._segment_path = lambda: "state"

                    def __setattr__(self, name, value):
                        self._perform_setattr(TerminalDevice.LogicalChannels.Channel.Ethernet.State, ['in_mac_control_frames', 'in_mac_pause_frames', 'in_oversize_frames', 'in_jabber_frames', 'in_fragment_frames', 'in_8021q_frames', 'in_crc_errors', 'out_mac_control_frames', 'out_mac_pause_frames', 'out_8021q_frames'], name, value)


            class Ingress(Entity):
                """
                Top\-level container for specifying references to the
                source of signal for the logical channel, either a
                transceiver or individual physical channels
                
                .. attribute:: config
                
                	Configuration data for the signal source for the logical channel
                	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel.Ingress.Config>`
                
                .. attribute:: state
                
                	Operational state data for the signal source for the logical channel
                	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel.Ingress.State>`
                
                

                """

                _prefix = 'oc-opt-term'
                _revision = '2016-06-17'

                def __init__(self):
                    super(TerminalDevice.LogicalChannels.Channel.Ingress, self).__init__()

                    self.yang_name = "ingress"
                    self.yang_parent_name = "channel"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("config", ("config", TerminalDevice.LogicalChannels.Channel.Ingress.Config)), ("state", ("state", TerminalDevice.LogicalChannels.Channel.Ingress.State))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict()

                    self.config = TerminalDevice.LogicalChannels.Channel.Ingress.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"
                    self._children_yang_names.add("config")

                    self.state = TerminalDevice.LogicalChannels.Channel.Ingress.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._children_yang_names.add("state")
                    self._segment_path = lambda: "ingress"


                class Config(Entity):
                    """
                    Configuration data for the signal source for the
                    logical channel
                    
                    .. attribute:: transceiver
                    
                    	Reference to the transceiver carrying the input signal for the logical channel.  If specific physical channels are mapped to the logical channel (as opposed to all physical channels carried by the transceiver), they can be specified in the list of physical channel references
                    	**type**\: str
                    
                    	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_platform.Components.Component>`
                    
                    .. attribute:: physical_channel
                    
                    	This list should be populated with references to the client physical channels that feed this logical channel from the transceiver specified in the 'transceiver' leaf, which must be specified.  If this leaf\-list is empty, all physical channels in the transceiver are assumed to be mapped to the logical channel
                    	**type**\: list of int
                    
                    	**range:** 0..65535
                    
                    	**refers to**\:  :py:class:`index <ydk.models.openconfig.openconfig_platform.Components.Component.Transceiver.PhysicalChannels.Channel>`
                    
                    

                    """

                    _prefix = 'oc-opt-term'
                    _revision = '2016-06-17'

                    def __init__(self):
                        super(TerminalDevice.LogicalChannels.Channel.Ingress.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "ingress"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('transceiver', YLeaf(YType.str, 'transceiver')),
                            ('physical_channel', YLeafList(YType.str, 'physical-channel')),
                        ])
                        self.transceiver = None
                        self.physical_channel = []
                        self._segment_path = lambda: "config"

                    def __setattr__(self, name, value):
                        self._perform_setattr(TerminalDevice.LogicalChannels.Channel.Ingress.Config, ['transceiver', 'physical_channel'], name, value)


                class State(Entity):
                    """
                    Operational state data for the signal source for the
                    logical channel
                    
                    .. attribute:: transceiver
                    
                    	Reference to the transceiver carrying the input signal for the logical channel.  If specific physical channels are mapped to the logical channel (as opposed to all physical channels carried by the transceiver), they can be specified in the list of physical channel references
                    	**type**\: str
                    
                    	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_platform.Components.Component>`
                    
                    .. attribute:: physical_channel
                    
                    	This list should be populated with references to the client physical channels that feed this logical channel from the transceiver specified in the 'transceiver' leaf, which must be specified.  If this leaf\-list is empty, all physical channels in the transceiver are assumed to be mapped to the logical channel
                    	**type**\: list of int
                    
                    	**range:** 0..65535
                    
                    	**refers to**\:  :py:class:`index <ydk.models.openconfig.openconfig_platform.Components.Component.Transceiver.PhysicalChannels.Channel>`
                    
                    

                    """

                    _prefix = 'oc-opt-term'
                    _revision = '2016-06-17'

                    def __init__(self):
                        super(TerminalDevice.LogicalChannels.Channel.Ingress.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "ingress"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('transceiver', YLeaf(YType.str, 'transceiver')),
                            ('physical_channel', YLeafList(YType.str, 'physical-channel')),
                        ])
                        self.transceiver = None
                        self.physical_channel = []
                        self._segment_path = lambda: "state"

                    def __setattr__(self, name, value):
                        self._perform_setattr(TerminalDevice.LogicalChannels.Channel.Ingress.State, ['transceiver', 'physical_channel'], name, value)


            class LogicalChannelAssignments(Entity):
                """
                Enclosing container for tributary assignments
                
                .. attribute:: assignment
                
                	Logical channel elements may be assigned directly to optical channels for line\-side transmission, or can be further groomed into additional stages of logical channel elements.  The grooming can multiplex (i.e., split the current element into multiple elements in the subsequent stage) or de\-multiplex (i.e., combine the current element with other elements into the same element in the subsequent stage) logical elements in each stage.  Note that to support the ability to groom the logical elements, the list of logical channel elements should be populated with an entry for the logical elements at each stage, starting with the initial assignment from the respective client physical port.  Each logical element assignment consists of a pointer to an element in the next stage, or to an optical channel, along with a bandwidth allocation for the corresponding assignment (e.g., to split or combine signal)
                	**type**\: list of  		 :py:class:`Assignment <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment>`
                
                

                """

                _prefix = 'oc-opt-term'
                _revision = '2016-06-17'

                def __init__(self):
                    super(TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments, self).__init__()

                    self.yang_name = "logical-channel-assignments"
                    self.yang_parent_name = "channel"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("assignment", ("assignment", TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment))])
                    self._leafs = OrderedDict()

                    self.assignment = YList(self)
                    self._segment_path = lambda: "logical-channel-assignments"

                def __setattr__(self, name, value):
                    self._perform_setattr(TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments, [], name, value)


                class Assignment(Entity):
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
                    
                    .. attribute:: index  (key)
                    
                    	Reference to the index for the current tributary assignment
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**refers to**\:  :py:class:`index <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment.Config>`
                    
                    .. attribute:: config
                    
                    	Configuration data for tributary assignments
                    	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment.Config>`
                    
                    .. attribute:: state
                    
                    	Operational state data for tributary assignments
                    	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment.State>`
                    
                    

                    """

                    _prefix = 'oc-opt-term'
                    _revision = '2016-06-17'

                    def __init__(self):
                        super(TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment, self).__init__()

                        self.yang_name = "assignment"
                        self.yang_parent_name = "logical-channel-assignments"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['index']
                        self._child_container_classes = OrderedDict([("config", ("config", TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment.Config)), ("state", ("state", TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment.State))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('index', YLeaf(YType.str, 'index')),
                        ])
                        self.index = None

                        self.config = TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"
                        self._children_yang_names.add("config")

                        self.state = TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._children_yang_names.add("state")
                        self._segment_path = lambda: "assignment" + "[index='" + str(self.index) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment, ['index'], name, value)


                    class Config(Entity):
                        """
                        Configuration data for tributary assignments
                        
                        .. attribute:: index
                        
                        	Index of the current logical client channel to tributary mapping
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: description
                        
                        	Name assigned to the logical client channel
                        	**type**\: str
                        
                        .. attribute:: assignment_type
                        
                        	Each logical channel element may be assigned to subsequent stages of logical elements to implement further grooming, or can be assigned to a line\-side optical channel for transmission.  Each assignment also has an associated bandwidth allocation
                        	**type**\:  :py:class:`AssignmentType <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment.Config.AssignmentType>`
                        
                        .. attribute:: logical_channel
                        
                        	Reference to another stage of logical channel elements
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**refers to**\:  :py:class:`index <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel>`
                        
                        .. attribute:: optical_channel
                        
                        	Reference to the line\-side optical channel that should carry the current logical channel element.  Use this reference to exit the logical element stage
                        	**type**\: str
                        
                        	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_platform.Components.Component>`
                        
                        .. attribute:: allocation
                        
                        	Allocation of the logical client channel to the tributary or sub\-channel, expressed in Gbps
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-9223372036854775.808..9223372036854775.807
                        
                        	**units**\: Gbps
                        
                        

                        """

                        _prefix = 'oc-opt-term'
                        _revision = '2016-06-17'

                        def __init__(self):
                            super(TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "assignment"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('index', YLeaf(YType.uint32, 'index')),
                                ('description', YLeaf(YType.str, 'description')),
                                ('assignment_type', YLeaf(YType.enumeration, 'assignment-type')),
                                ('logical_channel', YLeaf(YType.str, 'logical-channel')),
                                ('optical_channel', YLeaf(YType.str, 'optical-channel')),
                                ('allocation', YLeaf(YType.str, 'allocation')),
                            ])
                            self.index = None
                            self.description = None
                            self.assignment_type = None
                            self.logical_channel = None
                            self.optical_channel = None
                            self.allocation = None
                            self._segment_path = lambda: "config"

                        def __setattr__(self, name, value):
                            self._perform_setattr(TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment.Config, ['index', 'description', 'assignment_type', 'logical_channel', 'optical_channel', 'allocation'], name, value)

                        class AssignmentType(Enum):
                            """
                            AssignmentType (Enum Class)

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

                            LOGICAL_CHANNEL = Enum.YLeaf(0, "LOGICAL_CHANNEL")

                            OPTICAL_CHANNEL = Enum.YLeaf(1, "OPTICAL_CHANNEL")



                    class State(Entity):
                        """
                        Operational state data for tributary assignments
                        
                        .. attribute:: index
                        
                        	Index of the current logical client channel to tributary mapping
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: description
                        
                        	Name assigned to the logical client channel
                        	**type**\: str
                        
                        .. attribute:: assignment_type
                        
                        	Each logical channel element may be assigned to subsequent stages of logical elements to implement further grooming, or can be assigned to a line\-side optical channel for transmission.  Each assignment also has an associated bandwidth allocation
                        	**type**\:  :py:class:`AssignmentType <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment.State.AssignmentType>`
                        
                        .. attribute:: logical_channel
                        
                        	Reference to another stage of logical channel elements
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**refers to**\:  :py:class:`index <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel>`
                        
                        .. attribute:: optical_channel
                        
                        	Reference to the line\-side optical channel that should carry the current logical channel element.  Use this reference to exit the logical element stage
                        	**type**\: str
                        
                        	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_platform.Components.Component>`
                        
                        .. attribute:: allocation
                        
                        	Allocation of the logical client channel to the tributary or sub\-channel, expressed in Gbps
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-9223372036854775.808..9223372036854775.807
                        
                        	**units**\: Gbps
                        
                        

                        """

                        _prefix = 'oc-opt-term'
                        _revision = '2016-06-17'

                        def __init__(self):
                            super(TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "assignment"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('index', YLeaf(YType.uint32, 'index')),
                                ('description', YLeaf(YType.str, 'description')),
                                ('assignment_type', YLeaf(YType.enumeration, 'assignment-type')),
                                ('logical_channel', YLeaf(YType.str, 'logical-channel')),
                                ('optical_channel', YLeaf(YType.str, 'optical-channel')),
                                ('allocation', YLeaf(YType.str, 'allocation')),
                            ])
                            self.index = None
                            self.description = None
                            self.assignment_type = None
                            self.logical_channel = None
                            self.optical_channel = None
                            self.allocation = None
                            self._segment_path = lambda: "state"

                        def __setattr__(self, name, value):
                            self._perform_setattr(TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment.State, ['index', 'description', 'assignment_type', 'logical_channel', 'optical_channel', 'allocation'], name, value)

                        class AssignmentType(Enum):
                            """
                            AssignmentType (Enum Class)

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

                            LOGICAL_CHANNEL = Enum.YLeaf(0, "LOGICAL_CHANNEL")

                            OPTICAL_CHANNEL = Enum.YLeaf(1, "OPTICAL_CHANNEL")



    class OperationalModes(Entity):
        """
        Enclosing container for list of operational modes
        
        .. attribute:: mode
        
        	List of operational modes supported by the platform. The operational mode provides a platform\-defined summary of information such as symbol rate, modulation, pulse shaping, etc
        	**type**\: list of  		 :py:class:`Mode <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.OperationalModes.Mode>`
        
        

        """

        _prefix = 'oc-opt-term'
        _revision = '2016-06-17'

        def __init__(self):
            super(TerminalDevice.OperationalModes, self).__init__()

            self.yang_name = "operational-modes"
            self.yang_parent_name = "terminal-device"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("mode", ("mode", TerminalDevice.OperationalModes.Mode))])
            self._leafs = OrderedDict()

            self.mode = YList(self)
            self._segment_path = lambda: "operational-modes"
            self._absolute_path = lambda: "openconfig-terminal-device:terminal-device/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(TerminalDevice.OperationalModes, [], name, value)


        class Mode(Entity):
            """
            List of operational modes supported by the platform.
            The operational mode provides a platform\-defined summary
            of information such as symbol rate, modulation, pulse
            shaping, etc.
            
            .. attribute:: mode_id  (key)
            
            	Reference to mode\-id
            	**type**\: int
            
            	**range:** 0..65535
            
            	**refers to**\:  :py:class:`mode_id <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.OperationalModes.Mode.State>`
            
            .. attribute:: config
            
            	Configuration data for operational mode
            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.OperationalModes.Mode.Config>`
            
            .. attribute:: state
            
            	Operational state data for the platform\-defined operational mode
            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.OperationalModes.Mode.State>`
            
            

            """

            _prefix = 'oc-opt-term'
            _revision = '2016-06-17'

            def __init__(self):
                super(TerminalDevice.OperationalModes.Mode, self).__init__()

                self.yang_name = "mode"
                self.yang_parent_name = "operational-modes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['mode_id']
                self._child_container_classes = OrderedDict([("config", ("config", TerminalDevice.OperationalModes.Mode.Config)), ("state", ("state", TerminalDevice.OperationalModes.Mode.State))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('mode_id', YLeaf(YType.str, 'mode-id')),
                ])
                self.mode_id = None

                self.config = TerminalDevice.OperationalModes.Mode.Config()
                self.config.parent = self
                self._children_name_map["config"] = "config"
                self._children_yang_names.add("config")

                self.state = TerminalDevice.OperationalModes.Mode.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"
                self._children_yang_names.add("state")
                self._segment_path = lambda: "mode" + "[mode-id='" + str(self.mode_id) + "']"
                self._absolute_path = lambda: "openconfig-terminal-device:terminal-device/operational-modes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(TerminalDevice.OperationalModes.Mode, ['mode_id'], name, value)


            class Config(Entity):
                """
                Configuration data for operational mode
                
                

                """

                _prefix = 'oc-opt-term'
                _revision = '2016-06-17'

                def __init__(self):
                    super(TerminalDevice.OperationalModes.Mode.Config, self).__init__()

                    self.yang_name = "config"
                    self.yang_parent_name = "mode"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict()
                    self._segment_path = lambda: "config"


            class State(Entity):
                """
                Operational state data for the platform\-defined
                operational mode
                
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

                _prefix = 'oc-opt-term'
                _revision = '2016-06-17'

                def __init__(self):
                    super(TerminalDevice.OperationalModes.Mode.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "mode"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('mode_id', YLeaf(YType.uint16, 'mode-id')),
                        ('description', YLeaf(YType.str, 'description')),
                        ('vendor_id', YLeaf(YType.str, 'vendor-id')),
                    ])
                    self.mode_id = None
                    self.description = None
                    self.vendor_id = None
                    self._segment_path = lambda: "state"

                def __setattr__(self, name, value):
                    self._perform_setattr(TerminalDevice.OperationalModes.Mode.State, ['mode_id', 'description', 'vendor_id'], name, value)

    def clone_ptr(self):
        self._top_entity = TerminalDevice()
        return self._top_entity

