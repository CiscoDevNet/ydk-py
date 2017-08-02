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
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class TerminalDevice(Entity):
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
        super(TerminalDevice, self).__init__()
        self._top_entity = None

        self.yang_name = "terminal-device"
        self.yang_parent_name = "openconfig-terminal-device"

        self.config = TerminalDevice.Config()
        self.config.parent = self
        self._children_name_map["config"] = "config"
        self._children_yang_names.add("config")

        self.logical_channels = TerminalDevice.LogicalChannels()
        self.logical_channels.parent = self
        self._children_name_map["logical_channels"] = "logical-channels"
        self._children_yang_names.add("logical-channels")

        self.operational_modes = TerminalDevice.OperationalModes()
        self.operational_modes.parent = self
        self._children_name_map["operational_modes"] = "operational-modes"
        self._children_yang_names.add("operational-modes")

        self.state = TerminalDevice.State()
        self.state.parent = self
        self._children_name_map["state"] = "state"
        self._children_yang_names.add("state")


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

        def has_data(self):
            return False

        def has_operation(self):
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "config" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "openconfig-terminal-device:terminal-device/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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

        def has_data(self):
            return False

        def has_operation(self):
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "state" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "openconfig-terminal-device:terminal-device/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class LogicalChannels(Entity):
        """
        Enclosing container the list of logical channels
        
        .. attribute:: channel
        
        	List of logical channels
        	**type**\: list of    :py:class:`Channel <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel>`
        
        

        """

        _prefix = 'oc-opt-term'
        _revision = '2016-06-17'

        def __init__(self):
            super(TerminalDevice.LogicalChannels, self).__init__()

            self.yang_name = "logical-channels"
            self.yang_parent_name = "terminal-device"

            self.channel = YList(self)

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
                        super(TerminalDevice.LogicalChannels, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(TerminalDevice.LogicalChannels, self).__setattr__(name, value)


        class Channel(Entity):
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
                super(TerminalDevice.LogicalChannels.Channel, self).__init__()

                self.yang_name = "channel"
                self.yang_parent_name = "logical-channels"

                self.index = YLeaf(YType.str, "index")

                self.config = TerminalDevice.LogicalChannels.Channel.Config()
                self.config.parent = self
                self._children_name_map["config"] = "config"
                self._children_yang_names.add("config")

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

                self.otn = TerminalDevice.LogicalChannels.Channel.Otn()
                self.otn.parent = self
                self._children_name_map["otn"] = "otn"
                self._children_yang_names.add("otn")

                self.state = TerminalDevice.LogicalChannels.Channel.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"
                self._children_yang_names.add("state")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("index") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(TerminalDevice.LogicalChannels.Channel, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(TerminalDevice.LogicalChannels.Channel, self).__setattr__(name, value)


            class Config(Entity):
                """
                Configuration data for logical channels
                
                .. attribute:: admin_state
                
                	Sets the admin state of the logical channel
                	**type**\:   :py:class:`AdminStateType <ydk.models.openconfig.openconfig_transport_types.AdminStateType>`
                
                .. attribute:: description
                
                	Description of the logical channel
                	**type**\:  str
                
                .. attribute:: index
                
                	Index of the current logical channel
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: logical_channel_type
                
                	The type / stage of the logical element determines the configuration and operational state parameters (PMs) available for the logical element
                	**type**\:   :py:class:`Logical_Element_Protocol_Type <ydk.models.openconfig.openconfig_transport_types.Logical_Element_Protocol_Type>`
                
                .. attribute:: loopback_mode
                
                	Sets the loopback type on the logical channel. Setting the mode to something besides NONE activates the loopback in the specified mode
                	**type**\:   :py:class:`LoopbackModeType <ydk.models.openconfig.openconfig_transport_types.LoopbackModeType>`
                
                .. attribute:: rate_class
                
                	Rounded bit rate of the tributary signal. Exact bit rate will be refined by protocol selection
                	**type**\:   :py:class:`Tributary_Rate_Class_Type <ydk.models.openconfig.openconfig_transport_types.Tributary_Rate_Class_Type>`
                
                .. attribute:: trib_protocol
                
                	Protocol framing of the tributary signal. If this LogicalChannel is directly connected to a Client\-Port or Optical\-Channel, this is the protocol of the associated port. If the LogicalChannel is connected to other LogicalChannels, the TributaryProtocol of the LogicalChannels will define a specific mapping/demapping or multiplexing/demultiplexing function.  Not all protocols are valid, depending on the value of trib\-rate\-class.  The expectation is that the NMS will validate that a correct combination of rate class and protocol are specfied.  Basic combinations are\:  rate class\: 1G protocols\: 1GE  rate class\: 2.5G protocols\: OC48, STM16  rate class\: 10G protocols\:  10GE LAN, 10GE WAN, OC192, STM64, OTU2, OTU2e,            OTU1e, ODU2, ODU2e, ODU1e  rate class\: 40G protocols\:  40GE, OC768, STM256, OTU3, ODU3  rate class\: 100G protocols\:  100GE, 100G MLG, OTU4, OTUCn, ODU4
                	**type**\:   :py:class:`Tributary_Protocol_Type <ydk.models.openconfig.openconfig_transport_types.Tributary_Protocol_Type>`
                
                

                """

                _prefix = 'oc-opt-term'
                _revision = '2016-06-17'

                def __init__(self):
                    super(TerminalDevice.LogicalChannels.Channel.Config, self).__init__()

                    self.yang_name = "config"
                    self.yang_parent_name = "channel"

                    self.admin_state = YLeaf(YType.enumeration, "admin-state")

                    self.description = YLeaf(YType.str, "description")

                    self.index = YLeaf(YType.uint32, "index")

                    self.logical_channel_type = YLeaf(YType.identityref, "logical-channel-type")

                    self.loopback_mode = YLeaf(YType.enumeration, "loopback-mode")

                    self.rate_class = YLeaf(YType.identityref, "rate-class")

                    self.trib_protocol = YLeaf(YType.identityref, "trib-protocol")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("admin_state",
                                    "description",
                                    "index",
                                    "logical_channel_type",
                                    "loopback_mode",
                                    "rate_class",
                                    "trib_protocol") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(TerminalDevice.LogicalChannels.Channel.Config, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(TerminalDevice.LogicalChannels.Channel.Config, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.admin_state.is_set or
                        self.description.is_set or
                        self.index.is_set or
                        self.logical_channel_type.is_set or
                        self.loopback_mode.is_set or
                        self.rate_class.is_set or
                        self.trib_protocol.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.admin_state.yfilter != YFilter.not_set or
                        self.description.yfilter != YFilter.not_set or
                        self.index.yfilter != YFilter.not_set or
                        self.logical_channel_type.yfilter != YFilter.not_set or
                        self.loopback_mode.yfilter != YFilter.not_set or
                        self.rate_class.yfilter != YFilter.not_set or
                        self.trib_protocol.yfilter != YFilter.not_set)

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
                    if (self.admin_state.is_set or self.admin_state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.admin_state.get_name_leafdata())
                    if (self.description.is_set or self.description.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.description.get_name_leafdata())
                    if (self.index.is_set or self.index.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.index.get_name_leafdata())
                    if (self.logical_channel_type.is_set or self.logical_channel_type.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.logical_channel_type.get_name_leafdata())
                    if (self.loopback_mode.is_set or self.loopback_mode.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.loopback_mode.get_name_leafdata())
                    if (self.rate_class.is_set or self.rate_class.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rate_class.get_name_leafdata())
                    if (self.trib_protocol.is_set or self.trib_protocol.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.trib_protocol.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "admin-state" or name == "description" or name == "index" or name == "logical-channel-type" or name == "loopback-mode" or name == "rate-class" or name == "trib-protocol"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "admin-state"):
                        self.admin_state = value
                        self.admin_state.value_namespace = name_space
                        self.admin_state.value_namespace_prefix = name_space_prefix
                    if(value_path == "description"):
                        self.description = value
                        self.description.value_namespace = name_space
                        self.description.value_namespace_prefix = name_space_prefix
                    if(value_path == "index"):
                        self.index = value
                        self.index.value_namespace = name_space
                        self.index.value_namespace_prefix = name_space_prefix
                    if(value_path == "logical-channel-type"):
                        self.logical_channel_type = value
                        self.logical_channel_type.value_namespace = name_space
                        self.logical_channel_type.value_namespace_prefix = name_space_prefix
                    if(value_path == "loopback-mode"):
                        self.loopback_mode = value
                        self.loopback_mode.value_namespace = name_space
                        self.loopback_mode.value_namespace_prefix = name_space_prefix
                    if(value_path == "rate-class"):
                        self.rate_class = value
                        self.rate_class.value_namespace = name_space
                        self.rate_class.value_namespace_prefix = name_space_prefix
                    if(value_path == "trib-protocol"):
                        self.trib_protocol = value
                        self.trib_protocol.value_namespace = name_space
                        self.trib_protocol.value_namespace_prefix = name_space_prefix


            class State(Entity):
                """
                Operational state data for logical channels
                
                .. attribute:: admin_state
                
                	Sets the admin state of the logical channel
                	**type**\:   :py:class:`AdminStateType <ydk.models.openconfig.openconfig_transport_types.AdminStateType>`
                
                .. attribute:: description
                
                	Description of the logical channel
                	**type**\:  str
                
                .. attribute:: index
                
                	Index of the current logical channel
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: link_state
                
                	Link\-state of the Ethernet protocol on the logical channel, SONET / SDH framed signal, etc
                	**type**\:   :py:class:`LinkState <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel.State.LinkState>`
                
                .. attribute:: logical_channel_type
                
                	The type / stage of the logical element determines the configuration and operational state parameters (PMs) available for the logical element
                	**type**\:   :py:class:`Logical_Element_Protocol_Type <ydk.models.openconfig.openconfig_transport_types.Logical_Element_Protocol_Type>`
                
                .. attribute:: loopback_mode
                
                	Sets the loopback type on the logical channel. Setting the mode to something besides NONE activates the loopback in the specified mode
                	**type**\:   :py:class:`LoopbackModeType <ydk.models.openconfig.openconfig_transport_types.LoopbackModeType>`
                
                .. attribute:: rate_class
                
                	Rounded bit rate of the tributary signal. Exact bit rate will be refined by protocol selection
                	**type**\:   :py:class:`Tributary_Rate_Class_Type <ydk.models.openconfig.openconfig_transport_types.Tributary_Rate_Class_Type>`
                
                .. attribute:: trib_protocol
                
                	Protocol framing of the tributary signal. If this LogicalChannel is directly connected to a Client\-Port or Optical\-Channel, this is the protocol of the associated port. If the LogicalChannel is connected to other LogicalChannels, the TributaryProtocol of the LogicalChannels will define a specific mapping/demapping or multiplexing/demultiplexing function.  Not all protocols are valid, depending on the value of trib\-rate\-class.  The expectation is that the NMS will validate that a correct combination of rate class and protocol are specfied.  Basic combinations are\:  rate class\: 1G protocols\: 1GE  rate class\: 2.5G protocols\: OC48, STM16  rate class\: 10G protocols\:  10GE LAN, 10GE WAN, OC192, STM64, OTU2, OTU2e,            OTU1e, ODU2, ODU2e, ODU1e  rate class\: 40G protocols\:  40GE, OC768, STM256, OTU3, ODU3  rate class\: 100G protocols\:  100GE, 100G MLG, OTU4, OTUCn, ODU4
                	**type**\:   :py:class:`Tributary_Protocol_Type <ydk.models.openconfig.openconfig_transport_types.Tributary_Protocol_Type>`
                
                

                """

                _prefix = 'oc-opt-term'
                _revision = '2016-06-17'

                def __init__(self):
                    super(TerminalDevice.LogicalChannels.Channel.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "channel"

                    self.admin_state = YLeaf(YType.enumeration, "admin-state")

                    self.description = YLeaf(YType.str, "description")

                    self.index = YLeaf(YType.uint32, "index")

                    self.link_state = YLeaf(YType.enumeration, "link-state")

                    self.logical_channel_type = YLeaf(YType.identityref, "logical-channel-type")

                    self.loopback_mode = YLeaf(YType.enumeration, "loopback-mode")

                    self.rate_class = YLeaf(YType.identityref, "rate-class")

                    self.trib_protocol = YLeaf(YType.identityref, "trib-protocol")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("admin_state",
                                    "description",
                                    "index",
                                    "link_state",
                                    "logical_channel_type",
                                    "loopback_mode",
                                    "rate_class",
                                    "trib_protocol") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(TerminalDevice.LogicalChannels.Channel.State, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(TerminalDevice.LogicalChannels.Channel.State, self).__setattr__(name, value)

                class LinkState(Enum):
                    """
                    LinkState

                    Link\-state of the Ethernet protocol on the logical channel,

                    SONET / SDH framed signal, etc.

                    .. data:: UP = 0

                    	Logical channel is operationally up

                    .. data:: DOWN = 1

                    	Logical channel is operationally down

                    """

                    UP = Enum.YLeaf(0, "UP")

                    DOWN = Enum.YLeaf(1, "DOWN")


                def has_data(self):
                    return (
                        self.admin_state.is_set or
                        self.description.is_set or
                        self.index.is_set or
                        self.link_state.is_set or
                        self.logical_channel_type.is_set or
                        self.loopback_mode.is_set or
                        self.rate_class.is_set or
                        self.trib_protocol.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.admin_state.yfilter != YFilter.not_set or
                        self.description.yfilter != YFilter.not_set or
                        self.index.yfilter != YFilter.not_set or
                        self.link_state.yfilter != YFilter.not_set or
                        self.logical_channel_type.yfilter != YFilter.not_set or
                        self.loopback_mode.yfilter != YFilter.not_set or
                        self.rate_class.yfilter != YFilter.not_set or
                        self.trib_protocol.yfilter != YFilter.not_set)

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
                    if (self.admin_state.is_set or self.admin_state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.admin_state.get_name_leafdata())
                    if (self.description.is_set or self.description.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.description.get_name_leafdata())
                    if (self.index.is_set or self.index.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.index.get_name_leafdata())
                    if (self.link_state.is_set or self.link_state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.link_state.get_name_leafdata())
                    if (self.logical_channel_type.is_set or self.logical_channel_type.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.logical_channel_type.get_name_leafdata())
                    if (self.loopback_mode.is_set or self.loopback_mode.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.loopback_mode.get_name_leafdata())
                    if (self.rate_class.is_set or self.rate_class.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rate_class.get_name_leafdata())
                    if (self.trib_protocol.is_set or self.trib_protocol.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.trib_protocol.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "admin-state" or name == "description" or name == "index" or name == "link-state" or name == "logical-channel-type" or name == "loopback-mode" or name == "rate-class" or name == "trib-protocol"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "admin-state"):
                        self.admin_state = value
                        self.admin_state.value_namespace = name_space
                        self.admin_state.value_namespace_prefix = name_space_prefix
                    if(value_path == "description"):
                        self.description = value
                        self.description.value_namespace = name_space
                        self.description.value_namespace_prefix = name_space_prefix
                    if(value_path == "index"):
                        self.index = value
                        self.index.value_namespace = name_space
                        self.index.value_namespace_prefix = name_space_prefix
                    if(value_path == "link-state"):
                        self.link_state = value
                        self.link_state.value_namespace = name_space
                        self.link_state.value_namespace_prefix = name_space_prefix
                    if(value_path == "logical-channel-type"):
                        self.logical_channel_type = value
                        self.logical_channel_type.value_namespace = name_space
                        self.logical_channel_type.value_namespace_prefix = name_space_prefix
                    if(value_path == "loopback-mode"):
                        self.loopback_mode = value
                        self.loopback_mode.value_namespace = name_space
                        self.loopback_mode.value_namespace_prefix = name_space_prefix
                    if(value_path == "rate-class"):
                        self.rate_class = value
                        self.rate_class.value_namespace = name_space
                        self.rate_class.value_namespace_prefix = name_space_prefix
                    if(value_path == "trib-protocol"):
                        self.trib_protocol = value
                        self.trib_protocol.value_namespace = name_space
                        self.trib_protocol.value_namespace_prefix = name_space_prefix


            class Otn(Entity):
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
                    super(TerminalDevice.LogicalChannels.Channel.Otn, self).__init__()

                    self.yang_name = "otn"
                    self.yang_parent_name = "channel"

                    self.config = TerminalDevice.LogicalChannels.Channel.Otn.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"
                    self._children_yang_names.add("config")

                    self.state = TerminalDevice.LogicalChannels.Channel.Otn.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._children_yang_names.add("state")


                class Config(Entity):
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
                        super(TerminalDevice.LogicalChannels.Channel.Otn.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "otn"

                        self.tti_msg_auto = YLeaf(YType.boolean, "tti-msg-auto")

                        self.tti_msg_expected = YLeaf(YType.str, "tti-msg-expected")

                        self.tti_msg_transmit = YLeaf(YType.str, "tti-msg-transmit")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("tti_msg_auto",
                                        "tti_msg_expected",
                                        "tti_msg_transmit") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(TerminalDevice.LogicalChannels.Channel.Otn.Config, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(TerminalDevice.LogicalChannels.Channel.Otn.Config, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.tti_msg_auto.is_set or
                            self.tti_msg_expected.is_set or
                            self.tti_msg_transmit.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.tti_msg_auto.yfilter != YFilter.not_set or
                            self.tti_msg_expected.yfilter != YFilter.not_set or
                            self.tti_msg_transmit.yfilter != YFilter.not_set)

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
                        if (self.tti_msg_auto.is_set or self.tti_msg_auto.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tti_msg_auto.get_name_leafdata())
                        if (self.tti_msg_expected.is_set or self.tti_msg_expected.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tti_msg_expected.get_name_leafdata())
                        if (self.tti_msg_transmit.is_set or self.tti_msg_transmit.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tti_msg_transmit.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "tti-msg-auto" or name == "tti-msg-expected" or name == "tti-msg-transmit"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "tti-msg-auto"):
                            self.tti_msg_auto = value
                            self.tti_msg_auto.value_namespace = name_space
                            self.tti_msg_auto.value_namespace_prefix = name_space_prefix
                        if(value_path == "tti-msg-expected"):
                            self.tti_msg_expected = value
                            self.tti_msg_expected.value_namespace = name_space
                            self.tti_msg_expected.value_namespace_prefix = name_space_prefix
                        if(value_path == "tti-msg-transmit"):
                            self.tti_msg_transmit = value
                            self.tti_msg_transmit.value_namespace = name_space
                            self.tti_msg_transmit.value_namespace_prefix = name_space_prefix


                class State(Entity):
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
                        super(TerminalDevice.LogicalChannels.Channel.Otn.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "otn"

                        self.background_block_errors = YLeaf(YType.uint64, "background-block-errors")

                        self.code_violations = YLeaf(YType.uint64, "code-violations")

                        self.errored_seconds = YLeaf(YType.uint64, "errored-seconds")

                        self.fec_corrected_bits = YLeaf(YType.uint64, "fec-corrected-bits")

                        self.fec_corrected_bytes = YLeaf(YType.uint64, "fec-corrected-bytes")

                        self.fec_uncorrectable_words = YLeaf(YType.uint64, "fec-uncorrectable-words")

                        self.rdi_msg = YLeaf(YType.str, "rdi-msg")

                        self.severely_errored_seconds = YLeaf(YType.uint64, "severely-errored-seconds")

                        self.tti_msg_auto = YLeaf(YType.boolean, "tti-msg-auto")

                        self.tti_msg_expected = YLeaf(YType.str, "tti-msg-expected")

                        self.tti_msg_recv = YLeaf(YType.str, "tti-msg-recv")

                        self.tti_msg_transmit = YLeaf(YType.str, "tti-msg-transmit")

                        self.unavailable_seconds = YLeaf(YType.uint64, "unavailable-seconds")

                        self.esnr = TerminalDevice.LogicalChannels.Channel.Otn.State.Esnr()
                        self.esnr.parent = self
                        self._children_name_map["esnr"] = "esnr"
                        self._children_yang_names.add("esnr")

                        self.post_fec_ber = TerminalDevice.LogicalChannels.Channel.Otn.State.PostFecBer()
                        self.post_fec_ber.parent = self
                        self._children_name_map["post_fec_ber"] = "post-fec-ber"
                        self._children_yang_names.add("post-fec-ber")

                        self.pre_fec_ber = TerminalDevice.LogicalChannels.Channel.Otn.State.PreFecBer()
                        self.pre_fec_ber.parent = self
                        self._children_name_map["pre_fec_ber"] = "pre-fec-ber"
                        self._children_yang_names.add("pre-fec-ber")

                        self.q_value = TerminalDevice.LogicalChannels.Channel.Otn.State.QValue()
                        self.q_value.parent = self
                        self._children_name_map["q_value"] = "q-value"
                        self._children_yang_names.add("q-value")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("background_block_errors",
                                        "code_violations",
                                        "errored_seconds",
                                        "fec_corrected_bits",
                                        "fec_corrected_bytes",
                                        "fec_uncorrectable_words",
                                        "rdi_msg",
                                        "severely_errored_seconds",
                                        "tti_msg_auto",
                                        "tti_msg_expected",
                                        "tti_msg_recv",
                                        "tti_msg_transmit",
                                        "unavailable_seconds") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(TerminalDevice.LogicalChannels.Channel.Otn.State, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(TerminalDevice.LogicalChannels.Channel.Otn.State, self).__setattr__(name, value)


                    class PostFecBer(Entity):
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
                            super(TerminalDevice.LogicalChannels.Channel.Otn.State.PostFecBer, self).__init__()

                            self.yang_name = "post-fec-ber"
                            self.yang_parent_name = "state"

                            self.avg = YLeaf(YType.str, "avg")

                            self.instant = YLeaf(YType.str, "instant")

                            self.max = YLeaf(YType.str, "max")

                            self.min = YLeaf(YType.str, "min")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("avg",
                                            "instant",
                                            "max",
                                            "min") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(TerminalDevice.LogicalChannels.Channel.Otn.State.PostFecBer, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(TerminalDevice.LogicalChannels.Channel.Otn.State.PostFecBer, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.avg.is_set or
                                self.instant.is_set or
                                self.max.is_set or
                                self.min.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.avg.yfilter != YFilter.not_set or
                                self.instant.yfilter != YFilter.not_set or
                                self.max.yfilter != YFilter.not_set or
                                self.min.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "post-fec-ber" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.avg.is_set or self.avg.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.avg.get_name_leafdata())
                            if (self.instant.is_set or self.instant.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.instant.get_name_leafdata())
                            if (self.max.is_set or self.max.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.max.get_name_leafdata())
                            if (self.min.is_set or self.min.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.min.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "avg" or name == "instant" or name == "max" or name == "min"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "avg"):
                                self.avg = value
                                self.avg.value_namespace = name_space
                                self.avg.value_namespace_prefix = name_space_prefix
                            if(value_path == "instant"):
                                self.instant = value
                                self.instant.value_namespace = name_space
                                self.instant.value_namespace_prefix = name_space_prefix
                            if(value_path == "max"):
                                self.max = value
                                self.max.value_namespace = name_space
                                self.max.value_namespace_prefix = name_space_prefix
                            if(value_path == "min"):
                                self.min = value
                                self.min.value_namespace = name_space
                                self.min.value_namespace_prefix = name_space_prefix


                    class QValue(Entity):
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
                            super(TerminalDevice.LogicalChannels.Channel.Otn.State.QValue, self).__init__()

                            self.yang_name = "q-value"
                            self.yang_parent_name = "state"

                            self.avg = YLeaf(YType.str, "avg")

                            self.instant = YLeaf(YType.str, "instant")

                            self.max = YLeaf(YType.str, "max")

                            self.min = YLeaf(YType.str, "min")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("avg",
                                            "instant",
                                            "max",
                                            "min") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(TerminalDevice.LogicalChannels.Channel.Otn.State.QValue, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(TerminalDevice.LogicalChannels.Channel.Otn.State.QValue, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.avg.is_set or
                                self.instant.is_set or
                                self.max.is_set or
                                self.min.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.avg.yfilter != YFilter.not_set or
                                self.instant.yfilter != YFilter.not_set or
                                self.max.yfilter != YFilter.not_set or
                                self.min.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "q-value" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.avg.is_set or self.avg.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.avg.get_name_leafdata())
                            if (self.instant.is_set or self.instant.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.instant.get_name_leafdata())
                            if (self.max.is_set or self.max.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.max.get_name_leafdata())
                            if (self.min.is_set or self.min.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.min.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "avg" or name == "instant" or name == "max" or name == "min"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "avg"):
                                self.avg = value
                                self.avg.value_namespace = name_space
                                self.avg.value_namespace_prefix = name_space_prefix
                            if(value_path == "instant"):
                                self.instant = value
                                self.instant.value_namespace = name_space
                                self.instant.value_namespace_prefix = name_space_prefix
                            if(value_path == "max"):
                                self.max = value
                                self.max.value_namespace = name_space
                                self.max.value_namespace_prefix = name_space_prefix
                            if(value_path == "min"):
                                self.min = value
                                self.min.value_namespace = name_space
                                self.min.value_namespace_prefix = name_space_prefix


                    class PreFecBer(Entity):
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
                            super(TerminalDevice.LogicalChannels.Channel.Otn.State.PreFecBer, self).__init__()

                            self.yang_name = "pre-fec-ber"
                            self.yang_parent_name = "state"

                            self.avg = YLeaf(YType.str, "avg")

                            self.instant = YLeaf(YType.str, "instant")

                            self.max = YLeaf(YType.str, "max")

                            self.min = YLeaf(YType.str, "min")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("avg",
                                            "instant",
                                            "max",
                                            "min") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(TerminalDevice.LogicalChannels.Channel.Otn.State.PreFecBer, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(TerminalDevice.LogicalChannels.Channel.Otn.State.PreFecBer, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.avg.is_set or
                                self.instant.is_set or
                                self.max.is_set or
                                self.min.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.avg.yfilter != YFilter.not_set or
                                self.instant.yfilter != YFilter.not_set or
                                self.max.yfilter != YFilter.not_set or
                                self.min.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "pre-fec-ber" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.avg.is_set or self.avg.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.avg.get_name_leafdata())
                            if (self.instant.is_set or self.instant.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.instant.get_name_leafdata())
                            if (self.max.is_set or self.max.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.max.get_name_leafdata())
                            if (self.min.is_set or self.min.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.min.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "avg" or name == "instant" or name == "max" or name == "min"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "avg"):
                                self.avg = value
                                self.avg.value_namespace = name_space
                                self.avg.value_namespace_prefix = name_space_prefix
                            if(value_path == "instant"):
                                self.instant = value
                                self.instant.value_namespace = name_space
                                self.instant.value_namespace_prefix = name_space_prefix
                            if(value_path == "max"):
                                self.max = value
                                self.max.value_namespace = name_space
                                self.max.value_namespace_prefix = name_space_prefix
                            if(value_path == "min"):
                                self.min = value
                                self.min.value_namespace = name_space
                                self.min.value_namespace_prefix = name_space_prefix


                    class Esnr(Entity):
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
                            super(TerminalDevice.LogicalChannels.Channel.Otn.State.Esnr, self).__init__()

                            self.yang_name = "esnr"
                            self.yang_parent_name = "state"

                            self.avg = YLeaf(YType.str, "avg")

                            self.instant = YLeaf(YType.str, "instant")

                            self.max = YLeaf(YType.str, "max")

                            self.min = YLeaf(YType.str, "min")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("avg",
                                            "instant",
                                            "max",
                                            "min") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(TerminalDevice.LogicalChannels.Channel.Otn.State.Esnr, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(TerminalDevice.LogicalChannels.Channel.Otn.State.Esnr, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.avg.is_set or
                                self.instant.is_set or
                                self.max.is_set or
                                self.min.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.avg.yfilter != YFilter.not_set or
                                self.instant.yfilter != YFilter.not_set or
                                self.max.yfilter != YFilter.not_set or
                                self.min.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "esnr" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.avg.is_set or self.avg.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.avg.get_name_leafdata())
                            if (self.instant.is_set or self.instant.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.instant.get_name_leafdata())
                            if (self.max.is_set or self.max.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.max.get_name_leafdata())
                            if (self.min.is_set or self.min.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.min.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "avg" or name == "instant" or name == "max" or name == "min"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "avg"):
                                self.avg = value
                                self.avg.value_namespace = name_space
                                self.avg.value_namespace_prefix = name_space_prefix
                            if(value_path == "instant"):
                                self.instant = value
                                self.instant.value_namespace = name_space
                                self.instant.value_namespace_prefix = name_space_prefix
                            if(value_path == "max"):
                                self.max = value
                                self.max.value_namespace = name_space
                                self.max.value_namespace_prefix = name_space_prefix
                            if(value_path == "min"):
                                self.min = value
                                self.min.value_namespace = name_space
                                self.min.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.background_block_errors.is_set or
                            self.code_violations.is_set or
                            self.errored_seconds.is_set or
                            self.fec_corrected_bits.is_set or
                            self.fec_corrected_bytes.is_set or
                            self.fec_uncorrectable_words.is_set or
                            self.rdi_msg.is_set or
                            self.severely_errored_seconds.is_set or
                            self.tti_msg_auto.is_set or
                            self.tti_msg_expected.is_set or
                            self.tti_msg_recv.is_set or
                            self.tti_msg_transmit.is_set or
                            self.unavailable_seconds.is_set or
                            (self.esnr is not None and self.esnr.has_data()) or
                            (self.post_fec_ber is not None and self.post_fec_ber.has_data()) or
                            (self.pre_fec_ber is not None and self.pre_fec_ber.has_data()) or
                            (self.q_value is not None and self.q_value.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.background_block_errors.yfilter != YFilter.not_set or
                            self.code_violations.yfilter != YFilter.not_set or
                            self.errored_seconds.yfilter != YFilter.not_set or
                            self.fec_corrected_bits.yfilter != YFilter.not_set or
                            self.fec_corrected_bytes.yfilter != YFilter.not_set or
                            self.fec_uncorrectable_words.yfilter != YFilter.not_set or
                            self.rdi_msg.yfilter != YFilter.not_set or
                            self.severely_errored_seconds.yfilter != YFilter.not_set or
                            self.tti_msg_auto.yfilter != YFilter.not_set or
                            self.tti_msg_expected.yfilter != YFilter.not_set or
                            self.tti_msg_recv.yfilter != YFilter.not_set or
                            self.tti_msg_transmit.yfilter != YFilter.not_set or
                            self.unavailable_seconds.yfilter != YFilter.not_set or
                            (self.esnr is not None and self.esnr.has_operation()) or
                            (self.post_fec_ber is not None and self.post_fec_ber.has_operation()) or
                            (self.pre_fec_ber is not None and self.pre_fec_ber.has_operation()) or
                            (self.q_value is not None and self.q_value.has_operation()))

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
                        if (self.background_block_errors.is_set or self.background_block_errors.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.background_block_errors.get_name_leafdata())
                        if (self.code_violations.is_set or self.code_violations.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.code_violations.get_name_leafdata())
                        if (self.errored_seconds.is_set or self.errored_seconds.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.errored_seconds.get_name_leafdata())
                        if (self.fec_corrected_bits.is_set or self.fec_corrected_bits.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.fec_corrected_bits.get_name_leafdata())
                        if (self.fec_corrected_bytes.is_set or self.fec_corrected_bytes.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.fec_corrected_bytes.get_name_leafdata())
                        if (self.fec_uncorrectable_words.is_set or self.fec_uncorrectable_words.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.fec_uncorrectable_words.get_name_leafdata())
                        if (self.rdi_msg.is_set or self.rdi_msg.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.rdi_msg.get_name_leafdata())
                        if (self.severely_errored_seconds.is_set or self.severely_errored_seconds.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.severely_errored_seconds.get_name_leafdata())
                        if (self.tti_msg_auto.is_set or self.tti_msg_auto.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tti_msg_auto.get_name_leafdata())
                        if (self.tti_msg_expected.is_set or self.tti_msg_expected.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tti_msg_expected.get_name_leafdata())
                        if (self.tti_msg_recv.is_set or self.tti_msg_recv.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tti_msg_recv.get_name_leafdata())
                        if (self.tti_msg_transmit.is_set or self.tti_msg_transmit.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tti_msg_transmit.get_name_leafdata())
                        if (self.unavailable_seconds.is_set or self.unavailable_seconds.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.unavailable_seconds.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "esnr"):
                            if (self.esnr is None):
                                self.esnr = TerminalDevice.LogicalChannels.Channel.Otn.State.Esnr()
                                self.esnr.parent = self
                                self._children_name_map["esnr"] = "esnr"
                            return self.esnr

                        if (child_yang_name == "post-fec-ber"):
                            if (self.post_fec_ber is None):
                                self.post_fec_ber = TerminalDevice.LogicalChannels.Channel.Otn.State.PostFecBer()
                                self.post_fec_ber.parent = self
                                self._children_name_map["post_fec_ber"] = "post-fec-ber"
                            return self.post_fec_ber

                        if (child_yang_name == "pre-fec-ber"):
                            if (self.pre_fec_ber is None):
                                self.pre_fec_ber = TerminalDevice.LogicalChannels.Channel.Otn.State.PreFecBer()
                                self.pre_fec_ber.parent = self
                                self._children_name_map["pre_fec_ber"] = "pre-fec-ber"
                            return self.pre_fec_ber

                        if (child_yang_name == "q-value"):
                            if (self.q_value is None):
                                self.q_value = TerminalDevice.LogicalChannels.Channel.Otn.State.QValue()
                                self.q_value.parent = self
                                self._children_name_map["q_value"] = "q-value"
                            return self.q_value

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "esnr" or name == "post-fec-ber" or name == "pre-fec-ber" or name == "q-value" or name == "background-block-errors" or name == "code-violations" or name == "errored-seconds" or name == "fec-corrected-bits" or name == "fec-corrected-bytes" or name == "fec-uncorrectable-words" or name == "rdi-msg" or name == "severely-errored-seconds" or name == "tti-msg-auto" or name == "tti-msg-expected" or name == "tti-msg-recv" or name == "tti-msg-transmit" or name == "unavailable-seconds"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "background-block-errors"):
                            self.background_block_errors = value
                            self.background_block_errors.value_namespace = name_space
                            self.background_block_errors.value_namespace_prefix = name_space_prefix
                        if(value_path == "code-violations"):
                            self.code_violations = value
                            self.code_violations.value_namespace = name_space
                            self.code_violations.value_namespace_prefix = name_space_prefix
                        if(value_path == "errored-seconds"):
                            self.errored_seconds = value
                            self.errored_seconds.value_namespace = name_space
                            self.errored_seconds.value_namespace_prefix = name_space_prefix
                        if(value_path == "fec-corrected-bits"):
                            self.fec_corrected_bits = value
                            self.fec_corrected_bits.value_namespace = name_space
                            self.fec_corrected_bits.value_namespace_prefix = name_space_prefix
                        if(value_path == "fec-corrected-bytes"):
                            self.fec_corrected_bytes = value
                            self.fec_corrected_bytes.value_namespace = name_space
                            self.fec_corrected_bytes.value_namespace_prefix = name_space_prefix
                        if(value_path == "fec-uncorrectable-words"):
                            self.fec_uncorrectable_words = value
                            self.fec_uncorrectable_words.value_namespace = name_space
                            self.fec_uncorrectable_words.value_namespace_prefix = name_space_prefix
                        if(value_path == "rdi-msg"):
                            self.rdi_msg = value
                            self.rdi_msg.value_namespace = name_space
                            self.rdi_msg.value_namespace_prefix = name_space_prefix
                        if(value_path == "severely-errored-seconds"):
                            self.severely_errored_seconds = value
                            self.severely_errored_seconds.value_namespace = name_space
                            self.severely_errored_seconds.value_namespace_prefix = name_space_prefix
                        if(value_path == "tti-msg-auto"):
                            self.tti_msg_auto = value
                            self.tti_msg_auto.value_namespace = name_space
                            self.tti_msg_auto.value_namespace_prefix = name_space_prefix
                        if(value_path == "tti-msg-expected"):
                            self.tti_msg_expected = value
                            self.tti_msg_expected.value_namespace = name_space
                            self.tti_msg_expected.value_namespace_prefix = name_space_prefix
                        if(value_path == "tti-msg-recv"):
                            self.tti_msg_recv = value
                            self.tti_msg_recv.value_namespace = name_space
                            self.tti_msg_recv.value_namespace_prefix = name_space_prefix
                        if(value_path == "tti-msg-transmit"):
                            self.tti_msg_transmit = value
                            self.tti_msg_transmit.value_namespace = name_space
                            self.tti_msg_transmit.value_namespace_prefix = name_space_prefix
                        if(value_path == "unavailable-seconds"):
                            self.unavailable_seconds = value
                            self.unavailable_seconds.value_namespace = name_space
                            self.unavailable_seconds.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        (self.config is not None and self.config.has_data()) or
                        (self.state is not None and self.state.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.config is not None and self.config.has_operation()) or
                        (self.state is not None and self.state.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "otn" + path_buffer

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

                    if (child_yang_name == "config"):
                        if (self.config is None):
                            self.config = TerminalDevice.LogicalChannels.Channel.Otn.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"
                        return self.config

                    if (child_yang_name == "state"):
                        if (self.state is None):
                            self.state = TerminalDevice.LogicalChannels.Channel.Otn.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                        return self.state

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "config" or name == "state"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Ethernet(Entity):
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
                    super(TerminalDevice.LogicalChannels.Channel.Ethernet, self).__init__()

                    self.yang_name = "ethernet"
                    self.yang_parent_name = "channel"

                    self.config = TerminalDevice.LogicalChannels.Channel.Ethernet.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"
                    self._children_yang_names.add("config")

                    self.state = TerminalDevice.LogicalChannels.Channel.Ethernet.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._children_yang_names.add("state")


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

                    def has_data(self):
                        return False

                    def has_operation(self):
                        return self.yfilter != YFilter.not_set

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

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class State(Entity):
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
                        super(TerminalDevice.LogicalChannels.Channel.Ethernet.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "ethernet"

                        self.in_8021q_frames = YLeaf(YType.uint64, "in-8021q-frames")

                        self.in_crc_errors = YLeaf(YType.uint64, "in-crc-errors")

                        self.in_fragment_frames = YLeaf(YType.uint64, "in-fragment-frames")

                        self.in_jabber_frames = YLeaf(YType.uint64, "in-jabber-frames")

                        self.in_mac_control_frames = YLeaf(YType.uint64, "in-mac-control-frames")

                        self.in_mac_pause_frames = YLeaf(YType.uint64, "in-mac-pause-frames")

                        self.in_oversize_frames = YLeaf(YType.uint64, "in-oversize-frames")

                        self.out_8021q_frames = YLeaf(YType.uint64, "out-8021q-frames")

                        self.out_mac_control_frames = YLeaf(YType.uint64, "out-mac-control-frames")

                        self.out_mac_pause_frames = YLeaf(YType.uint64, "out-mac-pause-frames")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("in_8021q_frames",
                                        "in_crc_errors",
                                        "in_fragment_frames",
                                        "in_jabber_frames",
                                        "in_mac_control_frames",
                                        "in_mac_pause_frames",
                                        "in_oversize_frames",
                                        "out_8021q_frames",
                                        "out_mac_control_frames",
                                        "out_mac_pause_frames") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(TerminalDevice.LogicalChannels.Channel.Ethernet.State, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(TerminalDevice.LogicalChannels.Channel.Ethernet.State, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.in_8021q_frames.is_set or
                            self.in_crc_errors.is_set or
                            self.in_fragment_frames.is_set or
                            self.in_jabber_frames.is_set or
                            self.in_mac_control_frames.is_set or
                            self.in_mac_pause_frames.is_set or
                            self.in_oversize_frames.is_set or
                            self.out_8021q_frames.is_set or
                            self.out_mac_control_frames.is_set or
                            self.out_mac_pause_frames.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.in_8021q_frames.yfilter != YFilter.not_set or
                            self.in_crc_errors.yfilter != YFilter.not_set or
                            self.in_fragment_frames.yfilter != YFilter.not_set or
                            self.in_jabber_frames.yfilter != YFilter.not_set or
                            self.in_mac_control_frames.yfilter != YFilter.not_set or
                            self.in_mac_pause_frames.yfilter != YFilter.not_set or
                            self.in_oversize_frames.yfilter != YFilter.not_set or
                            self.out_8021q_frames.yfilter != YFilter.not_set or
                            self.out_mac_control_frames.yfilter != YFilter.not_set or
                            self.out_mac_pause_frames.yfilter != YFilter.not_set)

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
                        if (self.in_8021q_frames.is_set or self.in_8021q_frames.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.in_8021q_frames.get_name_leafdata())
                        if (self.in_crc_errors.is_set or self.in_crc_errors.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.in_crc_errors.get_name_leafdata())
                        if (self.in_fragment_frames.is_set or self.in_fragment_frames.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.in_fragment_frames.get_name_leafdata())
                        if (self.in_jabber_frames.is_set or self.in_jabber_frames.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.in_jabber_frames.get_name_leafdata())
                        if (self.in_mac_control_frames.is_set or self.in_mac_control_frames.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.in_mac_control_frames.get_name_leafdata())
                        if (self.in_mac_pause_frames.is_set or self.in_mac_pause_frames.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.in_mac_pause_frames.get_name_leafdata())
                        if (self.in_oversize_frames.is_set or self.in_oversize_frames.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.in_oversize_frames.get_name_leafdata())
                        if (self.out_8021q_frames.is_set or self.out_8021q_frames.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.out_8021q_frames.get_name_leafdata())
                        if (self.out_mac_control_frames.is_set or self.out_mac_control_frames.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.out_mac_control_frames.get_name_leafdata())
                        if (self.out_mac_pause_frames.is_set or self.out_mac_pause_frames.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.out_mac_pause_frames.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "in-8021q-frames" or name == "in-crc-errors" or name == "in-fragment-frames" or name == "in-jabber-frames" or name == "in-mac-control-frames" or name == "in-mac-pause-frames" or name == "in-oversize-frames" or name == "out-8021q-frames" or name == "out-mac-control-frames" or name == "out-mac-pause-frames"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "in-8021q-frames"):
                            self.in_8021q_frames = value
                            self.in_8021q_frames.value_namespace = name_space
                            self.in_8021q_frames.value_namespace_prefix = name_space_prefix
                        if(value_path == "in-crc-errors"):
                            self.in_crc_errors = value
                            self.in_crc_errors.value_namespace = name_space
                            self.in_crc_errors.value_namespace_prefix = name_space_prefix
                        if(value_path == "in-fragment-frames"):
                            self.in_fragment_frames = value
                            self.in_fragment_frames.value_namespace = name_space
                            self.in_fragment_frames.value_namespace_prefix = name_space_prefix
                        if(value_path == "in-jabber-frames"):
                            self.in_jabber_frames = value
                            self.in_jabber_frames.value_namespace = name_space
                            self.in_jabber_frames.value_namespace_prefix = name_space_prefix
                        if(value_path == "in-mac-control-frames"):
                            self.in_mac_control_frames = value
                            self.in_mac_control_frames.value_namespace = name_space
                            self.in_mac_control_frames.value_namespace_prefix = name_space_prefix
                        if(value_path == "in-mac-pause-frames"):
                            self.in_mac_pause_frames = value
                            self.in_mac_pause_frames.value_namespace = name_space
                            self.in_mac_pause_frames.value_namespace_prefix = name_space_prefix
                        if(value_path == "in-oversize-frames"):
                            self.in_oversize_frames = value
                            self.in_oversize_frames.value_namespace = name_space
                            self.in_oversize_frames.value_namespace_prefix = name_space_prefix
                        if(value_path == "out-8021q-frames"):
                            self.out_8021q_frames = value
                            self.out_8021q_frames.value_namespace = name_space
                            self.out_8021q_frames.value_namespace_prefix = name_space_prefix
                        if(value_path == "out-mac-control-frames"):
                            self.out_mac_control_frames = value
                            self.out_mac_control_frames.value_namespace = name_space
                            self.out_mac_control_frames.value_namespace_prefix = name_space_prefix
                        if(value_path == "out-mac-pause-frames"):
                            self.out_mac_pause_frames = value
                            self.out_mac_pause_frames.value_namespace = name_space
                            self.out_mac_pause_frames.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        (self.config is not None and self.config.has_data()) or
                        (self.state is not None and self.state.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.config is not None and self.config.has_operation()) or
                        (self.state is not None and self.state.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "ethernet" + path_buffer

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

                    if (child_yang_name == "config"):
                        if (self.config is None):
                            self.config = TerminalDevice.LogicalChannels.Channel.Ethernet.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"
                        return self.config

                    if (child_yang_name == "state"):
                        if (self.state is None):
                            self.state = TerminalDevice.LogicalChannels.Channel.Ethernet.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                        return self.state

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "config" or name == "state"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Ingress(Entity):
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
                    super(TerminalDevice.LogicalChannels.Channel.Ingress, self).__init__()

                    self.yang_name = "ingress"
                    self.yang_parent_name = "channel"

                    self.config = TerminalDevice.LogicalChannels.Channel.Ingress.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"
                    self._children_yang_names.add("config")

                    self.state = TerminalDevice.LogicalChannels.Channel.Ingress.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._children_yang_names.add("state")


                class Config(Entity):
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
                        super(TerminalDevice.LogicalChannels.Channel.Ingress.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "ingress"

                        self.physical_channel = YLeafList(YType.str, "physical-channel")

                        self.transceiver = YLeaf(YType.str, "transceiver")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("physical_channel",
                                        "transceiver") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(TerminalDevice.LogicalChannels.Channel.Ingress.Config, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(TerminalDevice.LogicalChannels.Channel.Ingress.Config, self).__setattr__(name, value)

                    def has_data(self):
                        for leaf in self.physical_channel.getYLeafs():
                            if (leaf.yfilter != YFilter.not_set):
                                return True
                        return self.transceiver.is_set

                    def has_operation(self):
                        for leaf in self.physical_channel.getYLeafs():
                            if (leaf.is_set):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.physical_channel.yfilter != YFilter.not_set or
                            self.transceiver.yfilter != YFilter.not_set)

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
                        if (self.transceiver.is_set or self.transceiver.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.transceiver.get_name_leafdata())

                        leaf_name_data.extend(self.physical_channel.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "physical-channel" or name == "transceiver"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "physical-channel"):
                            self.physical_channel.append(value)
                        if(value_path == "transceiver"):
                            self.transceiver = value
                            self.transceiver.value_namespace = name_space
                            self.transceiver.value_namespace_prefix = name_space_prefix


                class State(Entity):
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
                        super(TerminalDevice.LogicalChannels.Channel.Ingress.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "ingress"

                        self.physical_channel = YLeafList(YType.str, "physical-channel")

                        self.transceiver = YLeaf(YType.str, "transceiver")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("physical_channel",
                                        "transceiver") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(TerminalDevice.LogicalChannels.Channel.Ingress.State, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(TerminalDevice.LogicalChannels.Channel.Ingress.State, self).__setattr__(name, value)

                    def has_data(self):
                        for leaf in self.physical_channel.getYLeafs():
                            if (leaf.yfilter != YFilter.not_set):
                                return True
                        return self.transceiver.is_set

                    def has_operation(self):
                        for leaf in self.physical_channel.getYLeafs():
                            if (leaf.is_set):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.physical_channel.yfilter != YFilter.not_set or
                            self.transceiver.yfilter != YFilter.not_set)

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
                        if (self.transceiver.is_set or self.transceiver.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.transceiver.get_name_leafdata())

                        leaf_name_data.extend(self.physical_channel.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "physical-channel" or name == "transceiver"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "physical-channel"):
                            self.physical_channel.append(value)
                        if(value_path == "transceiver"):
                            self.transceiver = value
                            self.transceiver.value_namespace = name_space
                            self.transceiver.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        (self.config is not None and self.config.has_data()) or
                        (self.state is not None and self.state.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.config is not None and self.config.has_operation()) or
                        (self.state is not None and self.state.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "ingress" + path_buffer

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

                    if (child_yang_name == "config"):
                        if (self.config is None):
                            self.config = TerminalDevice.LogicalChannels.Channel.Ingress.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"
                        return self.config

                    if (child_yang_name == "state"):
                        if (self.state is None):
                            self.state = TerminalDevice.LogicalChannels.Channel.Ingress.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                        return self.state

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "config" or name == "state"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class LogicalChannelAssignments(Entity):
                """
                Enclosing container for tributary assignments
                
                .. attribute:: assignment
                
                	Logical channel elements may be assigned directly to optical channels for line\-side transmission, or can be further groomed into additional stages of logical channel elements.  The grooming can multiplex (i.e., split the current element into multiple elements in the subsequent stage) or de\-multiplex (i.e., combine the current element with other elements into the same element in the subsequent stage) logical elements in each stage.  Note that to support the ability to groom the logical elements, the list of logical channel elements should be populated with an entry for the logical elements at each stage, starting with the initial assignment from the respective client physical port.  Each logical element assignment consists of a pointer to an element in the next stage, or to an optical channel, along with a bandwidth allocation for the corresponding assignment (e.g., to split or combine signal)
                	**type**\: list of    :py:class:`Assignment <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment>`
                
                

                """

                _prefix = 'oc-opt-term'
                _revision = '2016-06-17'

                def __init__(self):
                    super(TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments, self).__init__()

                    self.yang_name = "logical-channel-assignments"
                    self.yang_parent_name = "channel"

                    self.assignment = YList(self)

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
                                super(TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments, self).__setattr__(name, value)


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
                        super(TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment, self).__init__()

                        self.yang_name = "assignment"
                        self.yang_parent_name = "logical-channel-assignments"

                        self.index = YLeaf(YType.str, "index")

                        self.config = TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"
                        self._children_yang_names.add("config")

                        self.state = TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._children_yang_names.add("state")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("index") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment, self).__setattr__(name, value)


                    class Config(Entity):
                        """
                        Configuration data for tributary assignments
                        
                        .. attribute:: allocation
                        
                        	Allocation of the logical client channel to the tributary or sub\-channel, expressed in Gbps
                        	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-9223372036854775.808..9223372036854775.807
                        
                        	**units**\: Gbps
                        
                        .. attribute:: assignment_type
                        
                        	Each logical channel element may be assigned to subsequent stages of logical elements to implement further grooming, or can be assigned to a line\-side optical channel for transmission.  Each assignment also has an associated bandwidth allocation
                        	**type**\:   :py:class:`AssignmentType <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment.Config.AssignmentType>`
                        
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
                            super(TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "assignment"

                            self.allocation = YLeaf(YType.str, "allocation")

                            self.assignment_type = YLeaf(YType.enumeration, "assignment-type")

                            self.description = YLeaf(YType.str, "description")

                            self.index = YLeaf(YType.uint32, "index")

                            self.logical_channel = YLeaf(YType.str, "logical-channel")

                            self.optical_channel = YLeaf(YType.str, "optical-channel")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("allocation",
                                            "assignment_type",
                                            "description",
                                            "index",
                                            "logical_channel",
                                            "optical_channel") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment.Config, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment.Config, self).__setattr__(name, value)

                        class AssignmentType(Enum):
                            """
                            AssignmentType

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


                        def has_data(self):
                            return (
                                self.allocation.is_set or
                                self.assignment_type.is_set or
                                self.description.is_set or
                                self.index.is_set or
                                self.logical_channel.is_set or
                                self.optical_channel.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.allocation.yfilter != YFilter.not_set or
                                self.assignment_type.yfilter != YFilter.not_set or
                                self.description.yfilter != YFilter.not_set or
                                self.index.yfilter != YFilter.not_set or
                                self.logical_channel.yfilter != YFilter.not_set or
                                self.optical_channel.yfilter != YFilter.not_set)

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
                            if (self.allocation.is_set or self.allocation.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.allocation.get_name_leafdata())
                            if (self.assignment_type.is_set or self.assignment_type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.assignment_type.get_name_leafdata())
                            if (self.description.is_set or self.description.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.description.get_name_leafdata())
                            if (self.index.is_set or self.index.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.index.get_name_leafdata())
                            if (self.logical_channel.is_set or self.logical_channel.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.logical_channel.get_name_leafdata())
                            if (self.optical_channel.is_set or self.optical_channel.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.optical_channel.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "allocation" or name == "assignment-type" or name == "description" or name == "index" or name == "logical-channel" or name == "optical-channel"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "allocation"):
                                self.allocation = value
                                self.allocation.value_namespace = name_space
                                self.allocation.value_namespace_prefix = name_space_prefix
                            if(value_path == "assignment-type"):
                                self.assignment_type = value
                                self.assignment_type.value_namespace = name_space
                                self.assignment_type.value_namespace_prefix = name_space_prefix
                            if(value_path == "description"):
                                self.description = value
                                self.description.value_namespace = name_space
                                self.description.value_namespace_prefix = name_space_prefix
                            if(value_path == "index"):
                                self.index = value
                                self.index.value_namespace = name_space
                                self.index.value_namespace_prefix = name_space_prefix
                            if(value_path == "logical-channel"):
                                self.logical_channel = value
                                self.logical_channel.value_namespace = name_space
                                self.logical_channel.value_namespace_prefix = name_space_prefix
                            if(value_path == "optical-channel"):
                                self.optical_channel = value
                                self.optical_channel.value_namespace = name_space
                                self.optical_channel.value_namespace_prefix = name_space_prefix


                    class State(Entity):
                        """
                        Operational state data for tributary assignments
                        
                        .. attribute:: allocation
                        
                        	Allocation of the logical client channel to the tributary or sub\-channel, expressed in Gbps
                        	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-9223372036854775.808..9223372036854775.807
                        
                        	**units**\: Gbps
                        
                        .. attribute:: assignment_type
                        
                        	Each logical channel element may be assigned to subsequent stages of logical elements to implement further grooming, or can be assigned to a line\-side optical channel for transmission.  Each assignment also has an associated bandwidth allocation
                        	**type**\:   :py:class:`AssignmentType <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment.State.AssignmentType>`
                        
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
                            super(TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "assignment"

                            self.allocation = YLeaf(YType.str, "allocation")

                            self.assignment_type = YLeaf(YType.enumeration, "assignment-type")

                            self.description = YLeaf(YType.str, "description")

                            self.index = YLeaf(YType.uint32, "index")

                            self.logical_channel = YLeaf(YType.str, "logical-channel")

                            self.optical_channel = YLeaf(YType.str, "optical-channel")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("allocation",
                                            "assignment_type",
                                            "description",
                                            "index",
                                            "logical_channel",
                                            "optical_channel") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment.State, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment.State, self).__setattr__(name, value)

                        class AssignmentType(Enum):
                            """
                            AssignmentType

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


                        def has_data(self):
                            return (
                                self.allocation.is_set or
                                self.assignment_type.is_set or
                                self.description.is_set or
                                self.index.is_set or
                                self.logical_channel.is_set or
                                self.optical_channel.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.allocation.yfilter != YFilter.not_set or
                                self.assignment_type.yfilter != YFilter.not_set or
                                self.description.yfilter != YFilter.not_set or
                                self.index.yfilter != YFilter.not_set or
                                self.logical_channel.yfilter != YFilter.not_set or
                                self.optical_channel.yfilter != YFilter.not_set)

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
                            if (self.allocation.is_set or self.allocation.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.allocation.get_name_leafdata())
                            if (self.assignment_type.is_set or self.assignment_type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.assignment_type.get_name_leafdata())
                            if (self.description.is_set or self.description.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.description.get_name_leafdata())
                            if (self.index.is_set or self.index.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.index.get_name_leafdata())
                            if (self.logical_channel.is_set or self.logical_channel.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.logical_channel.get_name_leafdata())
                            if (self.optical_channel.is_set or self.optical_channel.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.optical_channel.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "allocation" or name == "assignment-type" or name == "description" or name == "index" or name == "logical-channel" or name == "optical-channel"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "allocation"):
                                self.allocation = value
                                self.allocation.value_namespace = name_space
                                self.allocation.value_namespace_prefix = name_space_prefix
                            if(value_path == "assignment-type"):
                                self.assignment_type = value
                                self.assignment_type.value_namespace = name_space
                                self.assignment_type.value_namespace_prefix = name_space_prefix
                            if(value_path == "description"):
                                self.description = value
                                self.description.value_namespace = name_space
                                self.description.value_namespace_prefix = name_space_prefix
                            if(value_path == "index"):
                                self.index = value
                                self.index.value_namespace = name_space
                                self.index.value_namespace_prefix = name_space_prefix
                            if(value_path == "logical-channel"):
                                self.logical_channel = value
                                self.logical_channel.value_namespace = name_space
                                self.logical_channel.value_namespace_prefix = name_space_prefix
                            if(value_path == "optical-channel"):
                                self.optical_channel = value
                                self.optical_channel.value_namespace = name_space
                                self.optical_channel.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.index.is_set or
                            (self.config is not None and self.config.has_data()) or
                            (self.state is not None and self.state.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.index.yfilter != YFilter.not_set or
                            (self.config is not None and self.config.has_operation()) or
                            (self.state is not None and self.state.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "assignment" + "[index='" + self.index.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.index.is_set or self.index.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.index.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "config"):
                            if (self.config is None):
                                self.config = TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment.Config()
                                self.config.parent = self
                                self._children_name_map["config"] = "config"
                            return self.config

                        if (child_yang_name == "state"):
                            if (self.state is None):
                                self.state = TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"
                            return self.state

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "config" or name == "state" or name == "index"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "index"):
                            self.index = value
                            self.index.value_namespace = name_space
                            self.index.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.assignment:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.assignment:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "logical-channel-assignments" + path_buffer

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

                    if (child_yang_name == "assignment"):
                        for c in self.assignment:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.assignment.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "assignment"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.index.is_set or
                    (self.config is not None and self.config.has_data()) or
                    (self.ethernet is not None and self.ethernet.has_data()) or
                    (self.ingress is not None and self.ingress.has_data()) or
                    (self.logical_channel_assignments is not None and self.logical_channel_assignments.has_data()) or
                    (self.otn is not None and self.otn.has_data()) or
                    (self.state is not None and self.state.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.index.yfilter != YFilter.not_set or
                    (self.config is not None and self.config.has_operation()) or
                    (self.ethernet is not None and self.ethernet.has_operation()) or
                    (self.ingress is not None and self.ingress.has_operation()) or
                    (self.logical_channel_assignments is not None and self.logical_channel_assignments.has_operation()) or
                    (self.otn is not None and self.otn.has_operation()) or
                    (self.state is not None and self.state.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "channel" + "[index='" + self.index.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "openconfig-terminal-device:terminal-device/logical-channels/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.index.is_set or self.index.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.index.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "config"):
                    if (self.config is None):
                        self.config = TerminalDevice.LogicalChannels.Channel.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"
                    return self.config

                if (child_yang_name == "ethernet"):
                    if (self.ethernet is None):
                        self.ethernet = TerminalDevice.LogicalChannels.Channel.Ethernet()
                        self.ethernet.parent = self
                        self._children_name_map["ethernet"] = "ethernet"
                    return self.ethernet

                if (child_yang_name == "ingress"):
                    if (self.ingress is None):
                        self.ingress = TerminalDevice.LogicalChannels.Channel.Ingress()
                        self.ingress.parent = self
                        self._children_name_map["ingress"] = "ingress"
                    return self.ingress

                if (child_yang_name == "logical-channel-assignments"):
                    if (self.logical_channel_assignments is None):
                        self.logical_channel_assignments = TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments()
                        self.logical_channel_assignments.parent = self
                        self._children_name_map["logical_channel_assignments"] = "logical-channel-assignments"
                    return self.logical_channel_assignments

                if (child_yang_name == "otn"):
                    if (self.otn is None):
                        self.otn = TerminalDevice.LogicalChannels.Channel.Otn()
                        self.otn.parent = self
                        self._children_name_map["otn"] = "otn"
                    return self.otn

                if (child_yang_name == "state"):
                    if (self.state is None):
                        self.state = TerminalDevice.LogicalChannels.Channel.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                    return self.state

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "config" or name == "ethernet" or name == "ingress" or name == "logical-channel-assignments" or name == "otn" or name == "state" or name == "index"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "index"):
                    self.index = value
                    self.index.value_namespace = name_space
                    self.index.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.channel:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.channel:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "logical-channels" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "openconfig-terminal-device:terminal-device/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "channel"):
                for c in self.channel:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = TerminalDevice.LogicalChannels.Channel()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.channel.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "channel"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class OperationalModes(Entity):
        """
        Enclosing container for list of operational modes
        
        .. attribute:: mode
        
        	List of operational modes supported by the platform. The operational mode provides a platform\-defined summary of information such as symbol rate, modulation, pulse shaping, etc
        	**type**\: list of    :py:class:`Mode <ydk.models.openconfig.openconfig_terminal_device.TerminalDevice.OperationalModes.Mode>`
        
        

        """

        _prefix = 'oc-opt-term'
        _revision = '2016-06-17'

        def __init__(self):
            super(TerminalDevice.OperationalModes, self).__init__()

            self.yang_name = "operational-modes"
            self.yang_parent_name = "terminal-device"

            self.mode = YList(self)

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
                        super(TerminalDevice.OperationalModes, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(TerminalDevice.OperationalModes, self).__setattr__(name, value)


        class Mode(Entity):
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
                super(TerminalDevice.OperationalModes.Mode, self).__init__()

                self.yang_name = "mode"
                self.yang_parent_name = "operational-modes"

                self.mode_id = YLeaf(YType.str, "mode-id")

                self.config = TerminalDevice.OperationalModes.Mode.Config()
                self.config.parent = self
                self._children_name_map["config"] = "config"
                self._children_yang_names.add("config")

                self.state = TerminalDevice.OperationalModes.Mode.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"
                self._children_yang_names.add("state")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("mode_id") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(TerminalDevice.OperationalModes.Mode, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(TerminalDevice.OperationalModes.Mode, self).__setattr__(name, value)


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

                def has_data(self):
                    return False

                def has_operation(self):
                    return self.yfilter != YFilter.not_set

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

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class State(Entity):
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
                    super(TerminalDevice.OperationalModes.Mode.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "mode"

                    self.description = YLeaf(YType.str, "description")

                    self.mode_id = YLeaf(YType.uint16, "mode-id")

                    self.vendor_id = YLeaf(YType.str, "vendor-id")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("description",
                                    "mode_id",
                                    "vendor_id") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(TerminalDevice.OperationalModes.Mode.State, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(TerminalDevice.OperationalModes.Mode.State, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.description.is_set or
                        self.mode_id.is_set or
                        self.vendor_id.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.description.yfilter != YFilter.not_set or
                        self.mode_id.yfilter != YFilter.not_set or
                        self.vendor_id.yfilter != YFilter.not_set)

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
                    if (self.description.is_set or self.description.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.description.get_name_leafdata())
                    if (self.mode_id.is_set or self.mode_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.mode_id.get_name_leafdata())
                    if (self.vendor_id.is_set or self.vendor_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.vendor_id.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "description" or name == "mode-id" or name == "vendor-id"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "description"):
                        self.description = value
                        self.description.value_namespace = name_space
                        self.description.value_namespace_prefix = name_space_prefix
                    if(value_path == "mode-id"):
                        self.mode_id = value
                        self.mode_id.value_namespace = name_space
                        self.mode_id.value_namespace_prefix = name_space_prefix
                    if(value_path == "vendor-id"):
                        self.vendor_id = value
                        self.vendor_id.value_namespace = name_space
                        self.vendor_id.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.mode_id.is_set or
                    (self.config is not None and self.config.has_data()) or
                    (self.state is not None and self.state.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.mode_id.yfilter != YFilter.not_set or
                    (self.config is not None and self.config.has_operation()) or
                    (self.state is not None and self.state.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "mode" + "[mode-id='" + self.mode_id.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "openconfig-terminal-device:terminal-device/operational-modes/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.mode_id.is_set or self.mode_id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mode_id.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "config"):
                    if (self.config is None):
                        self.config = TerminalDevice.OperationalModes.Mode.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"
                    return self.config

                if (child_yang_name == "state"):
                    if (self.state is None):
                        self.state = TerminalDevice.OperationalModes.Mode.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                    return self.state

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "config" or name == "state" or name == "mode-id"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "mode-id"):
                    self.mode_id = value
                    self.mode_id.value_namespace = name_space
                    self.mode_id.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.mode:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.mode:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "operational-modes" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "openconfig-terminal-device:terminal-device/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "mode"):
                for c in self.mode:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = TerminalDevice.OperationalModes.Mode()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.mode.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "mode"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.config is not None and self.config.has_data()) or
            (self.logical_channels is not None and self.logical_channels.has_data()) or
            (self.operational_modes is not None and self.operational_modes.has_data()) or
            (self.state is not None and self.state.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.config is not None and self.config.has_operation()) or
            (self.logical_channels is not None and self.logical_channels.has_operation()) or
            (self.operational_modes is not None and self.operational_modes.has_operation()) or
            (self.state is not None and self.state.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "openconfig-terminal-device:terminal-device" + path_buffer

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

        if (child_yang_name == "config"):
            if (self.config is None):
                self.config = TerminalDevice.Config()
                self.config.parent = self
                self._children_name_map["config"] = "config"
            return self.config

        if (child_yang_name == "logical-channels"):
            if (self.logical_channels is None):
                self.logical_channels = TerminalDevice.LogicalChannels()
                self.logical_channels.parent = self
                self._children_name_map["logical_channels"] = "logical-channels"
            return self.logical_channels

        if (child_yang_name == "operational-modes"):
            if (self.operational_modes is None):
                self.operational_modes = TerminalDevice.OperationalModes()
                self.operational_modes.parent = self
                self._children_name_map["operational_modes"] = "operational-modes"
            return self.operational_modes

        if (child_yang_name == "state"):
            if (self.state is None):
                self.state = TerminalDevice.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"
            return self.state

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "config" or name == "logical-channels" or name == "operational-modes" or name == "state"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = TerminalDevice()
        return self._top_entity

