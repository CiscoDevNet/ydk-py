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
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class TerminalDevice(_Entity_):
    """
    Top\-level container for the terminal device
    
    .. attribute:: config
    
    	Configuration data for global terminal\-device
    	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.Config>`
    
    .. attribute:: state
    
    	Operational state data for global terminal device
    	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.State>`
    
    	**config**\: False
    
    .. attribute:: logical_channels
    
    	Enclosing container the list of logical channels
    	**type**\:  :py:class:`LogicalChannels <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels>`
    
    .. attribute:: operational_modes
    
    	Enclosing container for list of operational modes
    	**type**\:  :py:class:`OperationalModes <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.OperationalModes>`
    
    

    """

    _prefix = 'oc-opt-term'
    _revision = '2018-11-21'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(TerminalDevice, self).__init__()
        self._top_entity = None

        self.yang_name = "terminal-device"
        self.yang_parent_name = "openconfig-terminal-device"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("config", ("config", TerminalDevice.Config)), ("state", ("state", TerminalDevice.State)), ("logical-channels", ("logical_channels", TerminalDevice.LogicalChannels)), ("operational-modes", ("operational_modes", TerminalDevice.OperationalModes))])
        self._leafs = OrderedDict()

        self.config = TerminalDevice.Config()
        self.config.parent = self
        self._children_name_map["config"] = "config"

        self.state = TerminalDevice.State()
        self.state.parent = self
        self._children_name_map["state"] = "state"

        self.logical_channels = TerminalDevice.LogicalChannels()
        self.logical_channels.parent = self
        self._children_name_map["logical_channels"] = "logical-channels"

        self.operational_modes = TerminalDevice.OperationalModes()
        self.operational_modes.parent = self
        self._children_name_map["operational_modes"] = "operational-modes"
        self._segment_path = lambda: "openconfig-terminal-device:terminal-device"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(TerminalDevice, [], name, value)


    class Config(_Entity_):
        """
        Configuration data for global terminal\-device
        
        

        """

        _prefix = 'oc-opt-term'
        _revision = '2018-11-21'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(TerminalDevice.Config, self).__init__()

            self.yang_name = "config"
            self.yang_parent_name = "terminal-device"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict()
            self._segment_path = lambda: "config"
            self._absolute_path = lambda: "openconfig-terminal-device:terminal-device/%s" % self._segment_path()
            self._is_frozen = True



    class State(_Entity_):
        """
        Operational state data for global terminal device
        
        

        """

        _prefix = 'oc-opt-term'
        _revision = '2018-11-21'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(TerminalDevice.State, self).__init__()

            self.yang_name = "state"
            self.yang_parent_name = "terminal-device"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict()
            self._segment_path = lambda: "state"
            self._absolute_path = lambda: "openconfig-terminal-device:terminal-device/%s" % self._segment_path()
            self._is_frozen = True



    class LogicalChannels(_Entity_):
        """
        Enclosing container the list of logical channels
        
        .. attribute:: channel
        
        	List of logical channels
        	**type**\: list of  		 :py:class:`Channel <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel>`
        
        

        """

        _prefix = 'oc-opt-term'
        _revision = '2018-11-21'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(TerminalDevice.LogicalChannels, self).__init__()

            self.yang_name = "logical-channels"
            self.yang_parent_name = "terminal-device"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("channel", ("channel", TerminalDevice.LogicalChannels.Channel))])
            self._leafs = OrderedDict()

            self.channel = YList(self)
            self._segment_path = lambda: "logical-channels"
            self._absolute_path = lambda: "openconfig-terminal-device:terminal-device/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(TerminalDevice.LogicalChannels, [], name, value)


        class Channel(_Entity_):
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
            
            	**config**\: False
            
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
            _revision = '2018-11-21'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(TerminalDevice.LogicalChannels.Channel, self).__init__()

                self.yang_name = "channel"
                self.yang_parent_name = "logical-channels"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['index']
                self._child_classes = OrderedDict([("config", ("config", TerminalDevice.LogicalChannels.Channel.Config)), ("state", ("state", TerminalDevice.LogicalChannels.Channel.State)), ("otn", ("otn", TerminalDevice.LogicalChannels.Channel.Otn)), ("ethernet", ("ethernet", TerminalDevice.LogicalChannels.Channel.Ethernet)), ("ingress", ("ingress", TerminalDevice.LogicalChannels.Channel.Ingress)), ("logical-channel-assignments", ("logical_channel_assignments", TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments))])
                self._leafs = OrderedDict([
                    ('index', (YLeaf(YType.str, 'index'), ['int'])),
                ])
                self.index = None

                self.config = TerminalDevice.LogicalChannels.Channel.Config()
                self.config.parent = self
                self._children_name_map["config"] = "config"

                self.state = TerminalDevice.LogicalChannels.Channel.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"

                self.otn = TerminalDevice.LogicalChannels.Channel.Otn()
                self.otn.parent = self
                self._children_name_map["otn"] = "otn"

                self.ethernet = TerminalDevice.LogicalChannels.Channel.Ethernet()
                self.ethernet.parent = self
                self._children_name_map["ethernet"] = "ethernet"

                self.ingress = TerminalDevice.LogicalChannels.Channel.Ingress()
                self.ingress.parent = self
                self._children_name_map["ingress"] = "ingress"

                self.logical_channel_assignments = TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments()
                self.logical_channel_assignments.parent = self
                self._children_name_map["logical_channel_assignments"] = "logical-channel-assignments"
                self._segment_path = lambda: "channel" + "[index='" + str(self.index) + "']"
                self._absolute_path = lambda: "openconfig-terminal-device:terminal-device/logical-channels/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(TerminalDevice.LogicalChannels.Channel, ['index'], name, value)


            class Config(_Entity_):
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
                
                .. attribute:: test_signal
                
                	When enabled the logical channel's DSP will generate a pseudo randmon bit stream (PRBS) which can be used during testing
                	**type**\: bool
                
                

                """

                _prefix = 'oc-opt-term'
                _revision = '2018-11-21'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(TerminalDevice.LogicalChannels.Channel.Config, self).__init__()

                    self.yang_name = "config"
                    self.yang_parent_name = "channel"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('index', (YLeaf(YType.uint32, 'index'), ['int'])),
                        ('description', (YLeaf(YType.str, 'description'), ['str'])),
                        ('admin_state', (YLeaf(YType.enumeration, 'admin-state'), [('ydk.models.openconfig.openconfig_transport_types', 'AdminStateType', '')])),
                        ('rate_class', (YLeaf(YType.identityref, 'rate-class'), [('ydk.models.openconfig.openconfig_transport_types', 'TRIBUTARYRATECLASSTYPE')])),
                        ('trib_protocol', (YLeaf(YType.identityref, 'trib-protocol'), [('ydk.models.openconfig.openconfig_transport_types', 'TRIBUTARYPROTOCOLTYPE')])),
                        ('logical_channel_type', (YLeaf(YType.identityref, 'logical-channel-type'), [('ydk.models.openconfig.openconfig_transport_types', 'LOGICALELEMENTPROTOCOLTYPE')])),
                        ('loopback_mode', (YLeaf(YType.enumeration, 'loopback-mode'), [('ydk.models.openconfig.openconfig_transport_types', 'LoopbackModeType', '')])),
                        ('test_signal', (YLeaf(YType.boolean, 'test-signal'), ['bool'])),
                    ])
                    self.index = None
                    self.description = None
                    self.admin_state = None
                    self.rate_class = None
                    self.trib_protocol = None
                    self.logical_channel_type = None
                    self.loopback_mode = None
                    self.test_signal = None
                    self._segment_path = lambda: "config"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(TerminalDevice.LogicalChannels.Channel.Config, ['index', 'description', 'admin_state', 'rate_class', 'trib_protocol', 'logical_channel_type', 'loopback_mode', 'test_signal'], name, value)



            class State(_Entity_):
                """
                Operational state data for logical channels
                
                .. attribute:: index
                
                	Index of the current logical channel
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: description
                
                	Description of the logical channel
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: admin_state
                
                	Sets the admin state of the logical channel
                	**type**\:  :py:class:`AdminStateType <ydk.models.openconfig.openconfig_transport_types.AdminStateType>`
                
                	**config**\: False
                
                .. attribute:: rate_class
                
                	Rounded bit rate of the tributary signal. Exact bit rate will be refined by protocol selection
                	**type**\:  :py:class:`TRIBUTARYRATECLASSTYPE <ydk.models.openconfig.openconfig_transport_types.TRIBUTARYRATECLASSTYPE>`
                
                	**config**\: False
                
                .. attribute:: trib_protocol
                
                	Protocol framing of the tributary signal. If this LogicalChannel is directly connected to a Client\-Port or Optical\-Channel, this is the protocol of the associated port. If the LogicalChannel is connected to other LogicalChannels, the TributaryProtocol of the LogicalChannels will define a specific mapping/demapping or multiplexing/demultiplexing function.  Not all protocols are valid, depending on the value of trib\-rate\-class.  The expectation is that the NMS will validate that a correct combination of rate class and protocol are specfied.  Basic combinations are\:  rate class\: 1G protocols\: 1GE  rate class\: 2.5G protocols\: OC48, STM16  rate class\: 10G protocols\:  10GE LAN, 10GE WAN, OC192, STM64, OTU2, OTU2e,            OTU1e, ODU2, ODU2e, ODU1e  rate class\: 40G protocols\:  40GE, OC768, STM256, OTU3, ODU3  rate class\: 100G protocols\:  100GE, 100G MLG, OTU4, OTUCn, ODU4
                	**type**\:  :py:class:`TRIBUTARYPROTOCOLTYPE <ydk.models.openconfig.openconfig_transport_types.TRIBUTARYPROTOCOLTYPE>`
                
                	**config**\: False
                
                .. attribute:: logical_channel_type
                
                	The type / stage of the logical element determines the configuration and operational state parameters (PMs) available for the logical element
                	**type**\:  :py:class:`LOGICALELEMENTPROTOCOLTYPE <ydk.models.openconfig.openconfig_transport_types.LOGICALELEMENTPROTOCOLTYPE>`
                
                	**config**\: False
                
                .. attribute:: loopback_mode
                
                	Sets the loopback type on the logical channel. Setting the mode to something besides NONE activates the loopback in the specified mode
                	**type**\:  :py:class:`LoopbackModeType <ydk.models.openconfig.openconfig_transport_types.LoopbackModeType>`
                
                	**config**\: False
                
                .. attribute:: test_signal
                
                	When enabled the logical channel's DSP will generate a pseudo randmon bit stream (PRBS) which can be used during testing
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: link_state
                
                	Link\-state of the Ethernet protocol on the logical channel, SONET / SDH framed signal, etc
                	**type**\:  :py:class:`LinkState <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel.State.LinkState>`
                
                	**config**\: False
                
                

                """

                _prefix = 'oc-opt-term'
                _revision = '2018-11-21'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(TerminalDevice.LogicalChannels.Channel.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "channel"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('index', (YLeaf(YType.uint32, 'index'), ['int'])),
                        ('description', (YLeaf(YType.str, 'description'), ['str'])),
                        ('admin_state', (YLeaf(YType.enumeration, 'admin-state'), [('ydk.models.openconfig.openconfig_transport_types', 'AdminStateType', '')])),
                        ('rate_class', (YLeaf(YType.identityref, 'rate-class'), [('ydk.models.openconfig.openconfig_transport_types', 'TRIBUTARYRATECLASSTYPE')])),
                        ('trib_protocol', (YLeaf(YType.identityref, 'trib-protocol'), [('ydk.models.openconfig.openconfig_transport_types', 'TRIBUTARYPROTOCOLTYPE')])),
                        ('logical_channel_type', (YLeaf(YType.identityref, 'logical-channel-type'), [('ydk.models.openconfig.openconfig_transport_types', 'LOGICALELEMENTPROTOCOLTYPE')])),
                        ('loopback_mode', (YLeaf(YType.enumeration, 'loopback-mode'), [('ydk.models.openconfig.openconfig_transport_types', 'LoopbackModeType', '')])),
                        ('test_signal', (YLeaf(YType.boolean, 'test-signal'), ['bool'])),
                        ('link_state', (YLeaf(YType.enumeration, 'link-state'), [('ydk.models.openconfig.openconfig_terminal_device', 'TerminalDevice', 'LogicalChannels.Channel.State.LinkState')])),
                    ])
                    self.index = None
                    self.description = None
                    self.admin_state = None
                    self.rate_class = None
                    self.trib_protocol = None
                    self.logical_channel_type = None
                    self.loopback_mode = None
                    self.test_signal = None
                    self.link_state = None
                    self._segment_path = lambda: "state"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(TerminalDevice.LogicalChannels.Channel.State, ['index', 'description', 'admin_state', 'rate_class', 'trib_protocol', 'logical_channel_type', 'loopback_mode', 'test_signal', 'link_state'], name, value)

                class LinkState(Enum):
                    """
                    LinkState (Enum Class)

                    Link\-state of the Ethernet protocol on the logical channel,

                    SONET / SDH framed signal, etc.

                    .. data:: UP = 0

                    	Logical channel is operationally up

                    .. data:: DOWN = 1

                    	Logical channel is operationally down

                    .. data:: TESTING = 2

                    	Logical channel is under test as a result of

                    	enabling test-signal

                    """

                    UP = Enum.YLeaf(0, "UP")

                    DOWN = Enum.YLeaf(1, "DOWN")

                    TESTING = Enum.YLeaf(2, "TESTING")




            class Otn(_Entity_):
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
                
                	**config**\: False
                
                

                """

                _prefix = 'oc-opt-term'
                _revision = '2018-11-21'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(TerminalDevice.LogicalChannels.Channel.Otn, self).__init__()

                    self.yang_name = "otn"
                    self.yang_parent_name = "channel"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("config", ("config", TerminalDevice.LogicalChannels.Channel.Otn.Config)), ("state", ("state", TerminalDevice.LogicalChannels.Channel.Otn.State))])
                    self._leafs = OrderedDict()

                    self.config = TerminalDevice.LogicalChannels.Channel.Otn.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"

                    self.state = TerminalDevice.LogicalChannels.Channel.Otn.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._segment_path = lambda: "otn"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(TerminalDevice.LogicalChannels.Channel.Otn, [], name, value)


                class Config(_Entity_):
                    """
                    Configuration data for OTN protocol framing
                    
                    .. attribute:: tti_msg_transmit
                    
                    	Trail trace identifier (TTI) message transmitted
                    	**type**\: str
                    
                    .. attribute:: tti_msg_expected
                    
                    	Trail trace identifier (TTI) message expected
                    	**type**\: str
                    
                    .. attribute:: tti_msg_auto
                    
                    	Trail trace identifier (TTI) transmit message automatically created.  If true, then setting a custom transmit message would be invalid
                    	**type**\: bool
                    
                    .. attribute:: tributary_slot_granularity
                    
                    	Granularity value of OPUk or OPUCn tributary slots for OTN signal allocation. The currently defined values follow the existing ITU\-T G.709 standard, which can be extended as needed in future
                    	**type**\:  :py:class:`TRIBUTARYSLOTGRANULARITY <ydk.models.openconfig.openconfig_transport_types.TRIBUTARYSLOTGRANULARITY>`
                    
                    

                    """

                    _prefix = 'oc-opt-term'
                    _revision = '2018-11-21'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(TerminalDevice.LogicalChannels.Channel.Otn.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "otn"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('tti_msg_transmit', (YLeaf(YType.str, 'tti-msg-transmit'), ['str'])),
                            ('tti_msg_expected', (YLeaf(YType.str, 'tti-msg-expected'), ['str'])),
                            ('tti_msg_auto', (YLeaf(YType.boolean, 'tti-msg-auto'), ['bool'])),
                            ('tributary_slot_granularity', (YLeaf(YType.identityref, 'tributary-slot-granularity'), [('ydk.models.openconfig.openconfig_transport_types', 'TRIBUTARYSLOTGRANULARITY')])),
                        ])
                        self.tti_msg_transmit = None
                        self.tti_msg_expected = None
                        self.tti_msg_auto = None
                        self.tributary_slot_granularity = None
                        self._segment_path = lambda: "config"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(TerminalDevice.LogicalChannels.Channel.Otn.Config, ['tti_msg_transmit', 'tti_msg_expected', 'tti_msg_auto', 'tributary_slot_granularity'], name, value)



                class State(_Entity_):
                    """
                    Operational state data for OTN protocol PMs, statistics,
                    etc.
                    
                    .. attribute:: tti_msg_transmit
                    
                    	Trail trace identifier (TTI) message transmitted
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: tti_msg_expected
                    
                    	Trail trace identifier (TTI) message expected
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: tti_msg_auto
                    
                    	Trail trace identifier (TTI) transmit message automatically created.  If true, then setting a custom transmit message would be invalid
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: tributary_slot_granularity
                    
                    	Granularity value of OPUk or OPUCn tributary slots for OTN signal allocation. The currently defined values follow the existing ITU\-T G.709 standard, which can be extended as needed in future
                    	**type**\:  :py:class:`TRIBUTARYSLOTGRANULARITY <ydk.models.openconfig.openconfig_transport_types.TRIBUTARYSLOTGRANULARITY>`
                    
                    	**config**\: False
                    
                    .. attribute:: tti_msg_recv
                    
                    	Trail trace identifier (TTI) message received
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: rdi_msg
                    
                    	Remote defect indication (RDI) message received
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: errored_seconds
                    
                    	The number of seconds that at least one errored blocks occurs, at least one code violation occurs, loss of sync is detected or loss of signal is detected
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: severely_errored_seconds
                    
                    	The number of seconds that loss of frame is detected OR the number of errored blocks, code violations, loss of sync or loss of signal is detected exceeds a predefined threshold
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: unavailable_seconds
                    
                    	The number of seconds during which the link is unavailable
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: code_violations
                    
                    	For ethernet or fiberchannel links, the number of 8b/10b coding violations. For SONET/SDH, the number of BIP (bit interleaved parity) errors
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: errored_blocks
                    
                    	The number of errored blocks. Error detection codes are capable to detect whether one or more errors have occurred possible to determine the exact number of errored bits within the block
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: fec_uncorrectable_blocks
                    
                    	The number of blocks that were uncorrectable by the FEC
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: fec_uncorrectable_words
                    
                    	The number of words that were uncorrectable by the FEC
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: fec_corrected_bytes
                    
                    	The number of bytes that were corrected by the FEC
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: fec_corrected_bits
                    
                    	The number of bits that were corrected by the FEC
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: background_block_errors
                    
                    	The number of background block errors
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: pre_fec_ber
                    
                    	Bit error rate before forward error correction \-\- computed value with 18 decimal precision. Note that decimal64 supports values as small as i x 10^\-18 where i is an integer. Values smaller than this should be reported as 0 to inidicate error free or near error free performance. Values include the instantaneous, average, minimum, and maximum statistics. If avg/min/max statistics are not supported, the target is expected to just supply the instant value
                    	**type**\:  :py:class:`PreFecBer <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel.Otn.State.PreFecBer>`
                    
                    	**config**\: False
                    
                    .. attribute:: post_fec_ber
                    
                    	Bit error rate after forward error correction \-\- computed value with 18 decimal precision. Note that decimal64 supports values as small as i x 10^\-18 where i is an integer. Values smaller than this should be reported as 0 to inidicate error free or near error free performance. Values include the instantaneous, average, minimum, and maximum statistics. If avg/min/max statistics are not supported, the target is expected to just supply the instant value
                    	**type**\:  :py:class:`PostFecBer <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel.Otn.State.PostFecBer>`
                    
                    	**config**\: False
                    
                    .. attribute:: q_value
                    
                    	Quality value (factor) in dB of a channel with two decimal precision. Values include the instantaneous, average, minimum, and maximum statistics. If avg/min/max statistics are not supported, the target is expected to just supply the instant value
                    	**type**\:  :py:class:`QValue <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel.Otn.State.QValue>`
                    
                    	**config**\: False
                    
                    .. attribute:: esnr
                    
                    	Electrical signal to noise ratio. Baud rate normalized signal to noise ratio based on error vector magnitude in dB with two decimal precision. Values include the instantaneous, average, minimum, and maximum statistics. If avg/min/max statistics are not supported, the target is expected to just supply the instant value
                    	**type**\:  :py:class:`Esnr <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel.Otn.State.Esnr>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-opt-term'
                    _revision = '2018-11-21'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(TerminalDevice.LogicalChannels.Channel.Otn.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "otn"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("pre-fec-ber", ("pre_fec_ber", TerminalDevice.LogicalChannels.Channel.Otn.State.PreFecBer)), ("post-fec-ber", ("post_fec_ber", TerminalDevice.LogicalChannels.Channel.Otn.State.PostFecBer)), ("q-value", ("q_value", TerminalDevice.LogicalChannels.Channel.Otn.State.QValue)), ("esnr", ("esnr", TerminalDevice.LogicalChannels.Channel.Otn.State.Esnr))])
                        self._leafs = OrderedDict([
                            ('tti_msg_transmit', (YLeaf(YType.str, 'tti-msg-transmit'), ['str'])),
                            ('tti_msg_expected', (YLeaf(YType.str, 'tti-msg-expected'), ['str'])),
                            ('tti_msg_auto', (YLeaf(YType.boolean, 'tti-msg-auto'), ['bool'])),
                            ('tributary_slot_granularity', (YLeaf(YType.identityref, 'tributary-slot-granularity'), [('ydk.models.openconfig.openconfig_transport_types', 'TRIBUTARYSLOTGRANULARITY')])),
                            ('tti_msg_recv', (YLeaf(YType.str, 'tti-msg-recv'), ['str'])),
                            ('rdi_msg', (YLeaf(YType.str, 'rdi-msg'), ['str'])),
                            ('errored_seconds', (YLeaf(YType.uint64, 'errored-seconds'), ['int'])),
                            ('severely_errored_seconds', (YLeaf(YType.uint64, 'severely-errored-seconds'), ['int'])),
                            ('unavailable_seconds', (YLeaf(YType.uint64, 'unavailable-seconds'), ['int'])),
                            ('code_violations', (YLeaf(YType.uint64, 'code-violations'), ['int'])),
                            ('errored_blocks', (YLeaf(YType.uint64, 'errored-blocks'), ['int'])),
                            ('fec_uncorrectable_blocks', (YLeaf(YType.uint64, 'fec-uncorrectable-blocks'), ['int'])),
                            ('fec_uncorrectable_words', (YLeaf(YType.uint64, 'fec-uncorrectable-words'), ['int'])),
                            ('fec_corrected_bytes', (YLeaf(YType.uint64, 'fec-corrected-bytes'), ['int'])),
                            ('fec_corrected_bits', (YLeaf(YType.uint64, 'fec-corrected-bits'), ['int'])),
                            ('background_block_errors', (YLeaf(YType.uint64, 'background-block-errors'), ['int'])),
                        ])
                        self.tti_msg_transmit = None
                        self.tti_msg_expected = None
                        self.tti_msg_auto = None
                        self.tributary_slot_granularity = None
                        self.tti_msg_recv = None
                        self.rdi_msg = None
                        self.errored_seconds = None
                        self.severely_errored_seconds = None
                        self.unavailable_seconds = None
                        self.code_violations = None
                        self.errored_blocks = None
                        self.fec_uncorrectable_blocks = None
                        self.fec_uncorrectable_words = None
                        self.fec_corrected_bytes = None
                        self.fec_corrected_bits = None
                        self.background_block_errors = None

                        self.pre_fec_ber = TerminalDevice.LogicalChannels.Channel.Otn.State.PreFecBer()
                        self.pre_fec_ber.parent = self
                        self._children_name_map["pre_fec_ber"] = "pre-fec-ber"

                        self.post_fec_ber = TerminalDevice.LogicalChannels.Channel.Otn.State.PostFecBer()
                        self.post_fec_ber.parent = self
                        self._children_name_map["post_fec_ber"] = "post-fec-ber"

                        self.q_value = TerminalDevice.LogicalChannels.Channel.Otn.State.QValue()
                        self.q_value.parent = self
                        self._children_name_map["q_value"] = "q-value"

                        self.esnr = TerminalDevice.LogicalChannels.Channel.Otn.State.Esnr()
                        self.esnr.parent = self
                        self._children_name_map["esnr"] = "esnr"
                        self._segment_path = lambda: "state"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(TerminalDevice.LogicalChannels.Channel.Otn.State, ['tti_msg_transmit', 'tti_msg_expected', 'tti_msg_auto', 'tributary_slot_granularity', 'tti_msg_recv', 'rdi_msg', 'errored_seconds', 'severely_errored_seconds', 'unavailable_seconds', 'code_violations', 'errored_blocks', 'fec_uncorrectable_blocks', 'fec_uncorrectable_words', 'fec_corrected_bytes', 'fec_corrected_bits', 'background_block_errors'], name, value)


                    class PreFecBer(_Entity_):
                        """
                        Bit error rate before forward error correction \-\- computed
                        value with 18 decimal precision. Note that decimal64
                        supports values as small as i x 10^\-18 where i is an
                        integer. Values smaller than this should be reported as 0
                        to inidicate error free or near error free performance.
                        Values include the instantaneous, average, minimum, and
                        maximum statistics. If avg/min/max statistics are not
                        supported, the target is expected to just supply the
                        instant value
                        
                        .. attribute:: instant
                        
                        	The instantaneous value of the statistic
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-9.223372036854775808..9.223372036854775807
                        
                        	**config**\: False
                        
                        	**units**\: bit-errors-per-second
                        
                        .. attribute:: avg
                        
                        	The arithmetic mean value of the statistic over the time interval
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-9.223372036854775808..9.223372036854775807
                        
                        	**config**\: False
                        
                        	**units**\: bit-errors-per-second
                        
                        .. attribute:: min
                        
                        	The minimum value of the statistic over the time interval
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-9.223372036854775808..9.223372036854775807
                        
                        	**config**\: False
                        
                        	**units**\: bit-errors-per-second
                        
                        .. attribute:: max
                        
                        	The maximum value of the statistic over the time interval
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-9.223372036854775808..9.223372036854775807
                        
                        	**config**\: False
                        
                        	**units**\: bit-errors-per-second
                        
                        .. attribute:: interval
                        
                        	If supported by the system, this reports the time interval over which the min/max/average statistics are computed by the system
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: min_time
                        
                        	The absolute time at which the minimum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: max_time
                        
                        	The absolute time at which the maximum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'oc-opt-term'
                        _revision = '2018-11-21'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(TerminalDevice.LogicalChannels.Channel.Otn.State.PreFecBer, self).__init__()

                            self.yang_name = "pre-fec-ber"
                            self.yang_parent_name = "state"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('instant', (YLeaf(YType.str, 'instant'), ['Decimal64'])),
                                ('avg', (YLeaf(YType.str, 'avg'), ['Decimal64'])),
                                ('min', (YLeaf(YType.str, 'min'), ['Decimal64'])),
                                ('max', (YLeaf(YType.str, 'max'), ['Decimal64'])),
                                ('interval', (YLeaf(YType.uint64, 'interval'), ['int'])),
                                ('min_time', (YLeaf(YType.uint64, 'min-time'), ['int'])),
                                ('max_time', (YLeaf(YType.uint64, 'max-time'), ['int'])),
                            ])
                            self.instant = None
                            self.avg = None
                            self.min = None
                            self.max = None
                            self.interval = None
                            self.min_time = None
                            self.max_time = None
                            self._segment_path = lambda: "pre-fec-ber"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(TerminalDevice.LogicalChannels.Channel.Otn.State.PreFecBer, ['instant', 'avg', 'min', 'max', 'interval', 'min_time', 'max_time'], name, value)



                    class PostFecBer(_Entity_):
                        """
                        Bit error rate after forward error correction \-\- computed
                        value with 18 decimal precision. Note that decimal64
                        supports values as small as i x 10^\-18 where i is an
                        integer. Values smaller than this should be reported as 0
                        to inidicate error free or near error free performance.
                        Values include the instantaneous, average, minimum, and
                        maximum statistics. If avg/min/max statistics are not
                        supported, the target is expected to just supply the
                        instant value
                        
                        .. attribute:: instant
                        
                        	The instantaneous value of the statistic
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-9.223372036854775808..9.223372036854775807
                        
                        	**config**\: False
                        
                        	**units**\: bit-errors-per-second
                        
                        .. attribute:: avg
                        
                        	The arithmetic mean value of the statistic over the time interval
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-9.223372036854775808..9.223372036854775807
                        
                        	**config**\: False
                        
                        	**units**\: bit-errors-per-second
                        
                        .. attribute:: min
                        
                        	The minimum value of the statistic over the time interval
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-9.223372036854775808..9.223372036854775807
                        
                        	**config**\: False
                        
                        	**units**\: bit-errors-per-second
                        
                        .. attribute:: max
                        
                        	The maximum value of the statistic over the time interval
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-9.223372036854775808..9.223372036854775807
                        
                        	**config**\: False
                        
                        	**units**\: bit-errors-per-second
                        
                        .. attribute:: interval
                        
                        	If supported by the system, this reports the time interval over which the min/max/average statistics are computed by the system
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: min_time
                        
                        	The absolute time at which the minimum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: max_time
                        
                        	The absolute time at which the maximum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'oc-opt-term'
                        _revision = '2018-11-21'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(TerminalDevice.LogicalChannels.Channel.Otn.State.PostFecBer, self).__init__()

                            self.yang_name = "post-fec-ber"
                            self.yang_parent_name = "state"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('instant', (YLeaf(YType.str, 'instant'), ['Decimal64'])),
                                ('avg', (YLeaf(YType.str, 'avg'), ['Decimal64'])),
                                ('min', (YLeaf(YType.str, 'min'), ['Decimal64'])),
                                ('max', (YLeaf(YType.str, 'max'), ['Decimal64'])),
                                ('interval', (YLeaf(YType.uint64, 'interval'), ['int'])),
                                ('min_time', (YLeaf(YType.uint64, 'min-time'), ['int'])),
                                ('max_time', (YLeaf(YType.uint64, 'max-time'), ['int'])),
                            ])
                            self.instant = None
                            self.avg = None
                            self.min = None
                            self.max = None
                            self.interval = None
                            self.min_time = None
                            self.max_time = None
                            self._segment_path = lambda: "post-fec-ber"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(TerminalDevice.LogicalChannels.Channel.Otn.State.PostFecBer, ['instant', 'avg', 'min', 'max', 'interval', 'min_time', 'max_time'], name, value)



                    class QValue(_Entity_):
                        """
                        Quality value (factor) in dB of a channel with two
                        decimal precision. Values include the instantaneous,
                        average, minimum, and maximum statistics. If avg/min/max
                        statistics are not supported, the target is expected
                        to just supply the instant value
                        
                        .. attribute:: instant
                        
                        	The instantaneous value of the statistic
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-92233720368547758.08..92233720368547758.07
                        
                        	**config**\: False
                        
                        	**units**\: dB
                        
                        .. attribute:: avg
                        
                        	The arithmetic mean value of the statistic over the time interval
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-92233720368547758.08..92233720368547758.07
                        
                        	**config**\: False
                        
                        	**units**\: dB
                        
                        .. attribute:: min
                        
                        	The minimum value of the statistic over the time interval
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-92233720368547758.08..92233720368547758.07
                        
                        	**config**\: False
                        
                        	**units**\: dB
                        
                        .. attribute:: max
                        
                        	The maximum value of the statistic over the time interval
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-92233720368547758.08..92233720368547758.07
                        
                        	**config**\: False
                        
                        	**units**\: dB
                        
                        .. attribute:: interval
                        
                        	If supported by the system, this reports the time interval over which the min/max/average statistics are computed by the system
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: min_time
                        
                        	The absolute time at which the minimum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: max_time
                        
                        	The absolute time at which the maximum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'oc-opt-term'
                        _revision = '2018-11-21'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(TerminalDevice.LogicalChannels.Channel.Otn.State.QValue, self).__init__()

                            self.yang_name = "q-value"
                            self.yang_parent_name = "state"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('instant', (YLeaf(YType.str, 'instant'), ['Decimal64'])),
                                ('avg', (YLeaf(YType.str, 'avg'), ['Decimal64'])),
                                ('min', (YLeaf(YType.str, 'min'), ['Decimal64'])),
                                ('max', (YLeaf(YType.str, 'max'), ['Decimal64'])),
                                ('interval', (YLeaf(YType.uint64, 'interval'), ['int'])),
                                ('min_time', (YLeaf(YType.uint64, 'min-time'), ['int'])),
                                ('max_time', (YLeaf(YType.uint64, 'max-time'), ['int'])),
                            ])
                            self.instant = None
                            self.avg = None
                            self.min = None
                            self.max = None
                            self.interval = None
                            self.min_time = None
                            self.max_time = None
                            self._segment_path = lambda: "q-value"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(TerminalDevice.LogicalChannels.Channel.Otn.State.QValue, ['instant', 'avg', 'min', 'max', 'interval', 'min_time', 'max_time'], name, value)



                    class Esnr(_Entity_):
                        """
                        Electrical signal to noise ratio. Baud rate
                        normalized signal to noise ratio based on
                        error vector magnitude in dB with two decimal
                        precision. Values include the instantaneous, average,
                        minimum, and maximum statistics. If avg/min/max
                        statistics are not supported, the target is expected
                        to just supply the instant value
                        
                        .. attribute:: instant
                        
                        	The instantaneous value of the statistic
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-92233720368547758.08..92233720368547758.07
                        
                        	**config**\: False
                        
                        	**units**\: dB
                        
                        .. attribute:: avg
                        
                        	The arithmetic mean value of the statistic over the time interval
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-92233720368547758.08..92233720368547758.07
                        
                        	**config**\: False
                        
                        	**units**\: dB
                        
                        .. attribute:: min
                        
                        	The minimum value of the statistic over the time interval
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-92233720368547758.08..92233720368547758.07
                        
                        	**config**\: False
                        
                        	**units**\: dB
                        
                        .. attribute:: max
                        
                        	The maximum value of the statistic over the time interval
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-92233720368547758.08..92233720368547758.07
                        
                        	**config**\: False
                        
                        	**units**\: dB
                        
                        .. attribute:: interval
                        
                        	If supported by the system, this reports the time interval over which the min/max/average statistics are computed by the system
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: min_time
                        
                        	The absolute time at which the minimum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: max_time
                        
                        	The absolute time at which the maximum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'oc-opt-term'
                        _revision = '2018-11-21'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(TerminalDevice.LogicalChannels.Channel.Otn.State.Esnr, self).__init__()

                            self.yang_name = "esnr"
                            self.yang_parent_name = "state"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('instant', (YLeaf(YType.str, 'instant'), ['Decimal64'])),
                                ('avg', (YLeaf(YType.str, 'avg'), ['Decimal64'])),
                                ('min', (YLeaf(YType.str, 'min'), ['Decimal64'])),
                                ('max', (YLeaf(YType.str, 'max'), ['Decimal64'])),
                                ('interval', (YLeaf(YType.uint64, 'interval'), ['int'])),
                                ('min_time', (YLeaf(YType.uint64, 'min-time'), ['int'])),
                                ('max_time', (YLeaf(YType.uint64, 'max-time'), ['int'])),
                            ])
                            self.instant = None
                            self.avg = None
                            self.min = None
                            self.max = None
                            self.interval = None
                            self.min_time = None
                            self.max_time = None
                            self._segment_path = lambda: "esnr"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(TerminalDevice.LogicalChannels.Channel.Otn.State.Esnr, ['instant', 'avg', 'min', 'max', 'interval', 'min_time', 'max_time'], name, value)





            class Ethernet(_Entity_):
                """
                Top level container for data related to Ethernet framing
                for the logical channel
                
                .. attribute:: config
                
                	Configuration data for Ethernet protocol framing on logical channels
                	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel.Ethernet.Config>`
                
                .. attribute:: state
                
                	Operational state data for Ethernet protocol framing on logical channels
                	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel.Ethernet.State>`
                
                	**config**\: False
                
                

                """

                _prefix = 'oc-opt-term'
                _revision = '2018-11-21'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(TerminalDevice.LogicalChannels.Channel.Ethernet, self).__init__()

                    self.yang_name = "ethernet"
                    self.yang_parent_name = "channel"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("config", ("config", TerminalDevice.LogicalChannels.Channel.Ethernet.Config)), ("state", ("state", TerminalDevice.LogicalChannels.Channel.Ethernet.State))])
                    self._leafs = OrderedDict()

                    self.config = TerminalDevice.LogicalChannels.Channel.Ethernet.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"

                    self.state = TerminalDevice.LogicalChannels.Channel.Ethernet.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._segment_path = lambda: "ethernet"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(TerminalDevice.LogicalChannels.Channel.Ethernet, [], name, value)


                class Config(_Entity_):
                    """
                    Configuration data for Ethernet protocol framing on
                    logical channels
                    
                    

                    """

                    _prefix = 'oc-opt-term'
                    _revision = '2018-11-21'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(TerminalDevice.LogicalChannels.Channel.Ethernet.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "ethernet"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict()
                        self._segment_path = lambda: "config"
                        self._is_frozen = True



                class State(_Entity_):
                    """
                    Operational state data for Ethernet protocol framing
                    on logical channels
                    
                    .. attribute:: in_mac_control_frames
                    
                    	MAC layer control frames received on the interface
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: in_mac_pause_frames
                    
                    	MAC layer PAUSE frames received on the interface
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: in_oversize_frames
                    
                    	Number of oversize frames received on the interface
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: in_jabber_frames
                    
                    	Number of jabber frames received on the interface.  Jabber frames are typically defined as oversize frames which also have a bad CRC.  Implementations may use slightly different definitions of what constitutes a jabber frame.  Often indicative of a NIC hardware problem
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: in_fragment_frames
                    
                    	Number of fragment frames received on the interface
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: in_8021q_frames
                    
                    	Number of 802.1q tagged frames received on the interface
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: in_crc_errors
                    
                    	Number of receive error events due to FCS/CRC check failure
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: out_mac_control_frames
                    
                    	MAC layer control frames sent on the interface
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: out_mac_pause_frames
                    
                    	MAC layer PAUSE frames sent on the interface
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: out_8021q_frames
                    
                    	Number of 802.1q tagged frames sent on the interface
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: in_pcs_bip_errors
                    
                    	The number of received bit interleaved parity (BIP) errors at the physical coding sublayer (PCS). If the interface consists of multiple lanes, this will be the sum of all errors on the lane
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: in_pcs_errored_seconds
                    
                    	The number of seconds that physical coding sublayer (PCS) errors have crossed a sytem defined threshold indicating the link is erroring
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: in_pcs_severely_errored_seconds
                    
                    	The number of seconds that physical coding sublayer (PCS) errors have crossed a system defined threshold indicating the link is severely erroring
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: in_pcs_unavailable_seconds
                    
                    	The number of seconds that physical coding sublayer (PCS) errors have crossed a system defined threshold indicating the link is unavailable
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: out_pcs_bip_errors
                    
                    	The number of transmitted bit interleaved parity (BIP) errors at the physical coding sublayer (PCS). If the interface consists of multiple lanes, this will be the sum of all errors on the lane
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: out_crc_errors
                    
                    	Number of FCS/CRC error check failures sent on the interface
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: out_block_errors
                    
                    	The number of transmitted errored blocks. Error detection codes are capable of detecting whether one or more errors have normally not possible to determine the exact number of errored bits within the block
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-opt-term'
                    _revision = '2018-11-21'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(TerminalDevice.LogicalChannels.Channel.Ethernet.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "ethernet"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('in_mac_control_frames', (YLeaf(YType.uint64, 'in-mac-control-frames'), ['int'])),
                            ('in_mac_pause_frames', (YLeaf(YType.uint64, 'in-mac-pause-frames'), ['int'])),
                            ('in_oversize_frames', (YLeaf(YType.uint64, 'in-oversize-frames'), ['int'])),
                            ('in_jabber_frames', (YLeaf(YType.uint64, 'in-jabber-frames'), ['int'])),
                            ('in_fragment_frames', (YLeaf(YType.uint64, 'in-fragment-frames'), ['int'])),
                            ('in_8021q_frames', (YLeaf(YType.uint64, 'in-8021q-frames'), ['int'])),
                            ('in_crc_errors', (YLeaf(YType.uint64, 'in-crc-errors'), ['int'])),
                            ('out_mac_control_frames', (YLeaf(YType.uint64, 'out-mac-control-frames'), ['int'])),
                            ('out_mac_pause_frames', (YLeaf(YType.uint64, 'out-mac-pause-frames'), ['int'])),
                            ('out_8021q_frames', (YLeaf(YType.uint64, 'out-8021q-frames'), ['int'])),
                            ('in_pcs_bip_errors', (YLeaf(YType.uint64, 'in-pcs-bip-errors'), ['int'])),
                            ('in_pcs_errored_seconds', (YLeaf(YType.uint64, 'in-pcs-errored-seconds'), ['int'])),
                            ('in_pcs_severely_errored_seconds', (YLeaf(YType.uint64, 'in-pcs-severely-errored-seconds'), ['int'])),
                            ('in_pcs_unavailable_seconds', (YLeaf(YType.uint64, 'in-pcs-unavailable-seconds'), ['int'])),
                            ('out_pcs_bip_errors', (YLeaf(YType.uint64, 'out-pcs-bip-errors'), ['int'])),
                            ('out_crc_errors', (YLeaf(YType.uint64, 'out-crc-errors'), ['int'])),
                            ('out_block_errors', (YLeaf(YType.uint64, 'out-block-errors'), ['int'])),
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
                        self.in_pcs_bip_errors = None
                        self.in_pcs_errored_seconds = None
                        self.in_pcs_severely_errored_seconds = None
                        self.in_pcs_unavailable_seconds = None
                        self.out_pcs_bip_errors = None
                        self.out_crc_errors = None
                        self.out_block_errors = None
                        self._segment_path = lambda: "state"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(TerminalDevice.LogicalChannels.Channel.Ethernet.State, ['in_mac_control_frames', 'in_mac_pause_frames', 'in_oversize_frames', 'in_jabber_frames', 'in_fragment_frames', 'in_8021q_frames', 'in_crc_errors', 'out_mac_control_frames', 'out_mac_pause_frames', 'out_8021q_frames', 'in_pcs_bip_errors', 'in_pcs_errored_seconds', 'in_pcs_severely_errored_seconds', 'in_pcs_unavailable_seconds', 'out_pcs_bip_errors', 'out_crc_errors', 'out_block_errors'], name, value)




            class Ingress(_Entity_):
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
                
                	**config**\: False
                
                

                """

                _prefix = 'oc-opt-term'
                _revision = '2018-11-21'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(TerminalDevice.LogicalChannels.Channel.Ingress, self).__init__()

                    self.yang_name = "ingress"
                    self.yang_parent_name = "channel"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("config", ("config", TerminalDevice.LogicalChannels.Channel.Ingress.Config)), ("state", ("state", TerminalDevice.LogicalChannels.Channel.Ingress.State))])
                    self._leafs = OrderedDict()

                    self.config = TerminalDevice.LogicalChannels.Channel.Ingress.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"

                    self.state = TerminalDevice.LogicalChannels.Channel.Ingress.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._segment_path = lambda: "ingress"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(TerminalDevice.LogicalChannels.Channel.Ingress, [], name, value)


                class Config(_Entity_):
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
                    _revision = '2018-11-21'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(TerminalDevice.LogicalChannels.Channel.Ingress.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "ingress"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('transceiver', (YLeaf(YType.str, 'transceiver'), ['str'])),
                            ('physical_channel', (YLeafList(YType.str, 'physical-channel'), ['int'])),
                        ])
                        self.transceiver = None
                        self.physical_channel = []
                        self._segment_path = lambda: "config"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(TerminalDevice.LogicalChannels.Channel.Ingress.Config, ['transceiver', 'physical_channel'], name, value)



                class State(_Entity_):
                    """
                    Operational state data for the signal source for the
                    logical channel
                    
                    .. attribute:: transceiver
                    
                    	Reference to the transceiver carrying the input signal for the logical channel.  If specific physical channels are mapped to the logical channel (as opposed to all physical channels carried by the transceiver), they can be specified in the list of physical channel references
                    	**type**\: str
                    
                    	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_platform.Components.Component>`
                    
                    	**config**\: False
                    
                    .. attribute:: physical_channel
                    
                    	This list should be populated with references to the client physical channels that feed this logical channel from the transceiver specified in the 'transceiver' leaf, which must be specified.  If this leaf\-list is empty, all physical channels in the transceiver are assumed to be mapped to the logical channel
                    	**type**\: list of int
                    
                    	**range:** 0..65535
                    
                    	**refers to**\:  :py:class:`index <ydk.models.openconfig.openconfig_platform.Components.Component.Transceiver.PhysicalChannels.Channel>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-opt-term'
                    _revision = '2018-11-21'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(TerminalDevice.LogicalChannels.Channel.Ingress.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "ingress"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('transceiver', (YLeaf(YType.str, 'transceiver'), ['str'])),
                            ('physical_channel', (YLeafList(YType.str, 'physical-channel'), ['int'])),
                        ])
                        self.transceiver = None
                        self.physical_channel = []
                        self._segment_path = lambda: "state"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(TerminalDevice.LogicalChannels.Channel.Ingress.State, ['transceiver', 'physical_channel'], name, value)




            class LogicalChannelAssignments(_Entity_):
                """
                Enclosing container for tributary assignments
                
                .. attribute:: assignment
                
                	Logical channel elements may be assigned directly to optical channels for line\-side transmission, or can be further groomed into additional stages of logical channel elements.  The grooming can multiplex (i.e., split the current element into multiple elements in the subsequent stage) or de\-multiplex (i.e., combine the current element with other elements into the same element in the subsequent stage) logical elements in each stage.  Note that to support the ability to groom the logical elements, the list of logical channel elements should be populated with an entry for the logical elements at each stage, starting with the initial assignment from the respective client physical port.  Each logical element assignment consists of a pointer to an element in the next stage, or to an optical channel, along with a bandwidth allocation for the corresponding assignment (e.g., to split or combine signal)
                	**type**\: list of  		 :py:class:`Assignment <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment>`
                
                

                """

                _prefix = 'oc-opt-term'
                _revision = '2018-11-21'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments, self).__init__()

                    self.yang_name = "logical-channel-assignments"
                    self.yang_parent_name = "channel"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("assignment", ("assignment", TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment))])
                    self._leafs = OrderedDict()

                    self.assignment = YList(self)
                    self._segment_path = lambda: "logical-channel-assignments"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments, [], name, value)


                class Assignment(_Entity_):
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
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-opt-term'
                    _revision = '2018-11-21'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment, self).__init__()

                        self.yang_name = "assignment"
                        self.yang_parent_name = "logical-channel-assignments"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['index']
                        self._child_classes = OrderedDict([("config", ("config", TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment.Config)), ("state", ("state", TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment.State))])
                        self._leafs = OrderedDict([
                            ('index', (YLeaf(YType.str, 'index'), ['int'])),
                        ])
                        self.index = None

                        self.config = TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"

                        self.state = TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._segment_path = lambda: "assignment" + "[index='" + str(self.index) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment, ['index'], name, value)


                    class Config(_Entity_):
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
                        
                        	Allocation of the logical client channel to the tributary or sub\-channel, expressed in Gbps. Please note that if the assignment is to an OTN logical channel, the allocation must be an integer multiplication to tributary\-slot\-granularity of the OTN logical channel
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-9223372036854775.808..9223372036854775.807
                        
                        	**units**\: Gbps
                        
                        .. attribute:: tributary_slot_index
                        
                        	Indicates the first tributary slot index allocated to the client signal or logical channel in the assignment. Valid only when the assignment is to an OTN logical channel
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: mapping
                        
                        	Logical channel mapping procedure. Valid only when the assignment is to an OTN logical channel
                        	**type**\:  :py:class:`FRAMEMAPPINGPROTOCOL <ydk.models.openconfig.openconfig_transport_types.FRAMEMAPPINGPROTOCOL>`
                        
                        

                        """

                        _prefix = 'oc-opt-term'
                        _revision = '2018-11-21'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "assignment"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('index', (YLeaf(YType.uint32, 'index'), ['int'])),
                                ('description', (YLeaf(YType.str, 'description'), ['str'])),
                                ('assignment_type', (YLeaf(YType.enumeration, 'assignment-type'), [('ydk.models.openconfig.openconfig_terminal_device', 'TerminalDevice', 'LogicalChannels.Channel.LogicalChannelAssignments.Assignment.Config.AssignmentType')])),
                                ('logical_channel', (YLeaf(YType.str, 'logical-channel'), ['int'])),
                                ('optical_channel', (YLeaf(YType.str, 'optical-channel'), ['str'])),
                                ('allocation', (YLeaf(YType.str, 'allocation'), ['Decimal64'])),
                                ('tributary_slot_index', (YLeaf(YType.int32, 'tributary-slot-index'), ['int'])),
                                ('mapping', (YLeaf(YType.identityref, 'mapping'), [('ydk.models.openconfig.openconfig_transport_types', 'FRAMEMAPPINGPROTOCOL')])),
                            ])
                            self.index = None
                            self.description = None
                            self.assignment_type = None
                            self.logical_channel = None
                            self.optical_channel = None
                            self.allocation = None
                            self.tributary_slot_index = None
                            self.mapping = None
                            self._segment_path = lambda: "config"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment.Config, ['index', 'description', 'assignment_type', 'logical_channel', 'optical_channel', 'allocation', 'tributary_slot_index', 'mapping'], name, value)

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




                    class State(_Entity_):
                        """
                        Operational state data for tributary assignments
                        
                        .. attribute:: index
                        
                        	Index of the current logical client channel to tributary mapping
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: description
                        
                        	Name assigned to the logical client channel
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: assignment_type
                        
                        	Each logical channel element may be assigned to subsequent stages of logical elements to implement further grooming, or can be assigned to a line\-side optical channel for transmission.  Each assignment also has an associated bandwidth allocation
                        	**type**\:  :py:class:`AssignmentType <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment.State.AssignmentType>`
                        
                        	**config**\: False
                        
                        .. attribute:: logical_channel
                        
                        	Reference to another stage of logical channel elements
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**refers to**\:  :py:class:`index <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel>`
                        
                        	**config**\: False
                        
                        .. attribute:: optical_channel
                        
                        	Reference to the line\-side optical channel that should carry the current logical channel element.  Use this reference to exit the logical element stage
                        	**type**\: str
                        
                        	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_platform.Components.Component>`
                        
                        	**config**\: False
                        
                        .. attribute:: allocation
                        
                        	Allocation of the logical client channel to the tributary or sub\-channel, expressed in Gbps. Please note that if the assignment is to an OTN logical channel, the allocation must be an integer multiplication to tributary\-slot\-granularity of the OTN logical channel
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-9223372036854775.808..9223372036854775.807
                        
                        	**config**\: False
                        
                        	**units**\: Gbps
                        
                        .. attribute:: tributary_slot_index
                        
                        	Indicates the first tributary slot index allocated to the client signal or logical channel in the assignment. Valid only when the assignment is to an OTN logical channel
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        .. attribute:: mapping
                        
                        	Logical channel mapping procedure. Valid only when the assignment is to an OTN logical channel
                        	**type**\:  :py:class:`FRAMEMAPPINGPROTOCOL <ydk.models.openconfig.openconfig_transport_types.FRAMEMAPPINGPROTOCOL>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'oc-opt-term'
                        _revision = '2018-11-21'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "assignment"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('index', (YLeaf(YType.uint32, 'index'), ['int'])),
                                ('description', (YLeaf(YType.str, 'description'), ['str'])),
                                ('assignment_type', (YLeaf(YType.enumeration, 'assignment-type'), [('ydk.models.openconfig.openconfig_terminal_device', 'TerminalDevice', 'LogicalChannels.Channel.LogicalChannelAssignments.Assignment.State.AssignmentType')])),
                                ('logical_channel', (YLeaf(YType.str, 'logical-channel'), ['int'])),
                                ('optical_channel', (YLeaf(YType.str, 'optical-channel'), ['str'])),
                                ('allocation', (YLeaf(YType.str, 'allocation'), ['Decimal64'])),
                                ('tributary_slot_index', (YLeaf(YType.int32, 'tributary-slot-index'), ['int'])),
                                ('mapping', (YLeaf(YType.identityref, 'mapping'), [('ydk.models.openconfig.openconfig_transport_types', 'FRAMEMAPPINGPROTOCOL')])),
                            ])
                            self.index = None
                            self.description = None
                            self.assignment_type = None
                            self.logical_channel = None
                            self.optical_channel = None
                            self.allocation = None
                            self.tributary_slot_index = None
                            self.mapping = None
                            self._segment_path = lambda: "state"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment.State, ['index', 'description', 'assignment_type', 'logical_channel', 'optical_channel', 'allocation', 'tributary_slot_index', 'mapping'], name, value)

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








    class OperationalModes(_Entity_):
        """
        Enclosing container for list of operational modes
        
        .. attribute:: mode
        
        	List of operational modes supported by the platform. The operational mode provides a platform\-defined summary of information such as symbol rate, modulation, pulse shaping, etc
        	**type**\: list of  		 :py:class:`Mode <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.OperationalModes.Mode>`
        
        	**config**\: False
        
        

        """

        _prefix = 'oc-opt-term'
        _revision = '2018-11-21'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(TerminalDevice.OperationalModes, self).__init__()

            self.yang_name = "operational-modes"
            self.yang_parent_name = "terminal-device"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("mode", ("mode", TerminalDevice.OperationalModes.Mode))])
            self._leafs = OrderedDict()

            self.mode = YList(self)
            self._segment_path = lambda: "operational-modes"
            self._absolute_path = lambda: "openconfig-terminal-device:terminal-device/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(TerminalDevice.OperationalModes, [], name, value)


        class Mode(_Entity_):
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
            
            	**config**\: False
            
            .. attribute:: config
            
            	Configuration data for operational mode
            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.OperationalModes.Mode.Config>`
            
            	**config**\: False
            
            .. attribute:: state
            
            	Operational state data for the platform\-defined operational mode
            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.OperationalModes.Mode.State>`
            
            	**config**\: False
            
            

            """

            _prefix = 'oc-opt-term'
            _revision = '2018-11-21'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(TerminalDevice.OperationalModes.Mode, self).__init__()

                self.yang_name = "mode"
                self.yang_parent_name = "operational-modes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['mode_id']
                self._child_classes = OrderedDict([("config", ("config", TerminalDevice.OperationalModes.Mode.Config)), ("state", ("state", TerminalDevice.OperationalModes.Mode.State))])
                self._leafs = OrderedDict([
                    ('mode_id', (YLeaf(YType.str, 'mode-id'), ['int'])),
                ])
                self.mode_id = None

                self.config = TerminalDevice.OperationalModes.Mode.Config()
                self.config.parent = self
                self._children_name_map["config"] = "config"

                self.state = TerminalDevice.OperationalModes.Mode.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"
                self._segment_path = lambda: "mode" + "[mode-id='" + str(self.mode_id) + "']"
                self._absolute_path = lambda: "openconfig-terminal-device:terminal-device/operational-modes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(TerminalDevice.OperationalModes.Mode, ['mode_id'], name, value)


            class Config(_Entity_):
                """
                Configuration data for operational mode
                
                

                """

                _prefix = 'oc-opt-term'
                _revision = '2018-11-21'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(TerminalDevice.OperationalModes.Mode.Config, self).__init__()

                    self.yang_name = "config"
                    self.yang_parent_name = "mode"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict()
                    self._segment_path = lambda: "config"
                    self._is_frozen = True



            class State(_Entity_):
                """
                Operational state data for the platform\-defined
                operational mode
                
                .. attribute:: mode_id
                
                	Two\-octet encoding of the vendor\-defined operational mode
                	**type**\: int
                
                	**range:** 0..65535
                
                	**config**\: False
                
                .. attribute:: description
                
                	Vendor\-supplied textual description of the characteristics of this operational mode to enable operators to select the appropriate mode for the application
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: vendor_id
                
                	Identifier to represent the vendor / supplier of the platform and the associated operational mode information
                	**type**\: str
                
                	**config**\: False
                
                

                """

                _prefix = 'oc-opt-term'
                _revision = '2018-11-21'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(TerminalDevice.OperationalModes.Mode.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "mode"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('mode_id', (YLeaf(YType.uint16, 'mode-id'), ['int'])),
                        ('description', (YLeaf(YType.str, 'description'), ['str'])),
                        ('vendor_id', (YLeaf(YType.str, 'vendor-id'), ['str'])),
                    ])
                    self.mode_id = None
                    self.description = None
                    self.vendor_id = None
                    self._segment_path = lambda: "state"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(TerminalDevice.OperationalModes.Mode.State, ['mode_id', 'description', 'vendor_id'], name, value)




    def clone_ptr(self):
        self._top_entity = TerminalDevice()
        return self._top_entity



