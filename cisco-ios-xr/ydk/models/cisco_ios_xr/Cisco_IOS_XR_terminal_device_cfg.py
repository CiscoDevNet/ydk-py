""" Cisco_IOS_XR_terminal_device_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR terminal\-device package configuration.

This module contains definitions
for the following management objects\:
  logical\-channels\: Logical channel in mxp
  optical\-channels\: optical channels

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class LogicalAdminState(Enum):
    """
    LogicalAdminState

    Logical admin state

    .. data:: enable = 1

    	Enable

    .. data:: disable = 2

    	Disable

    .. data:: maintenance = 3

    	Maintenance

    """

    enable = Enum.YLeaf(1, "enable")

    disable = Enum.YLeaf(2, "disable")

    maintenance = Enum.YLeaf(3, "maintenance")


class LogicalChannelAssignment(Enum):
    """
    LogicalChannelAssignment

    Logical channel assignment

    .. data:: type_logical_channel = 1

    	Type Logical channel

    .. data:: type_optical_channel = 2

    	Type Optical channel

    """

    type_logical_channel = Enum.YLeaf(1, "type-logical-channel")

    type_optical_channel = Enum.YLeaf(2, "type-optical-channel")


class LogicalChannelOtnTtiAuto(Enum):
    """
    LogicalChannelOtnTtiAuto

    Logical channel otn tti auto

    .. data:: false = 0

    	Otn tti auto mode false

    .. data:: true = 1

    	Otn tti auto mode true

    """

    false = Enum.YLeaf(0, "false")

    true = Enum.YLeaf(1, "true")


class LogicalLoopbackMode(Enum):
    """
    LogicalLoopbackMode

    Logical loopback mode

    .. data:: none = 0

    	None

    .. data:: facility = 1

    	Facility

    .. data:: terminal = 2

    	Terminal

    """

    none = Enum.YLeaf(0, "none")

    facility = Enum.YLeaf(1, "facility")

    terminal = Enum.YLeaf(2, "terminal")


class LogicalProtocol(Enum):
    """
    LogicalProtocol

    Logical protocol

    .. data:: type_ethernet = 1

    	Type Ethernet

    .. data:: type_otn = 2

    	Type OTN

    """

    type_ethernet = Enum.YLeaf(1, "type-ethernet")

    type_otn = Enum.YLeaf(2, "type-otn")


class LogicalTribProtocol(Enum):
    """
    LogicalTribProtocol

    Logical trib protocol

    .. data:: trib_proto_type1ge = 1

    	1G Ethernet protocol

    .. data:: trib_proto_type_oc48 = 2

    	OC48 protocol

    .. data:: trib_proto_type_stm16 = 3

    	STM 16 protocol

    .. data:: trib_proto_type10gelan = 4

    	10G Ethernet LAN protocol

    .. data:: trib_proto_type10gewan = 5

    	10G Ethernet WAN protocol

    .. data:: trib_proto_type_oc192 = 6

    	OC 192 (9.6GB) port protocol

    .. data:: trib_proto_type_stm64 = 7

    	STM 64 protocol

    .. data:: trib_proto_type_otu2 = 8

    	OTU 2 protocol

    .. data:: trib_proto_type_otu2e = 9

    	OTU 2e protocol

    .. data:: trib_proto_type_otu1e = 10

    	OTU 1e protocol

    .. data:: trib_proto_type_odu2 = 11

    	ODU 2 protocol

    .. data:: trib_proto_type_odu2e = 12

    	ODU 2e protocol

    .. data:: trib_proto_type40ge = 13

    	40G Ethernet port protocol

    .. data:: trib_proto_type_oc768 = 14

    	OC 768 protocol

    .. data:: trib_proto_type_stm256 = 15

    	STM 256 protocol

    .. data:: trib_proto_type_otu3 = 16

    	OTU 3 protocol

    .. data:: trib_proto_type_odu3 = 17

    	ODU 3 protocol

    .. data:: trib_proto_type100ge = 18

    	100G Ethernet protocol

    .. data:: trib_proto_type100g_mlg = 19

    	100G MLG protocol

    .. data:: trib_proto_type_otu4 = 20

    	OTU4 signal protocol (112G) for transporting

    	100GE signal

    .. data:: trib_proto_type_otu_cn = 21

    	OTU Cn protocol

    .. data:: trib_proto_type_odu4 = 22

    	ODU 4 protocol

    """

    trib_proto_type1ge = Enum.YLeaf(1, "trib-proto-type1ge")

    trib_proto_type_oc48 = Enum.YLeaf(2, "trib-proto-type-oc48")

    trib_proto_type_stm16 = Enum.YLeaf(3, "trib-proto-type-stm16")

    trib_proto_type10gelan = Enum.YLeaf(4, "trib-proto-type10gelan")

    trib_proto_type10gewan = Enum.YLeaf(5, "trib-proto-type10gewan")

    trib_proto_type_oc192 = Enum.YLeaf(6, "trib-proto-type-oc192")

    trib_proto_type_stm64 = Enum.YLeaf(7, "trib-proto-type-stm64")

    trib_proto_type_otu2 = Enum.YLeaf(8, "trib-proto-type-otu2")

    trib_proto_type_otu2e = Enum.YLeaf(9, "trib-proto-type-otu2e")

    trib_proto_type_otu1e = Enum.YLeaf(10, "trib-proto-type-otu1e")

    trib_proto_type_odu2 = Enum.YLeaf(11, "trib-proto-type-odu2")

    trib_proto_type_odu2e = Enum.YLeaf(12, "trib-proto-type-odu2e")

    trib_proto_type40ge = Enum.YLeaf(13, "trib-proto-type40ge")

    trib_proto_type_oc768 = Enum.YLeaf(14, "trib-proto-type-oc768")

    trib_proto_type_stm256 = Enum.YLeaf(15, "trib-proto-type-stm256")

    trib_proto_type_otu3 = Enum.YLeaf(16, "trib-proto-type-otu3")

    trib_proto_type_odu3 = Enum.YLeaf(17, "trib-proto-type-odu3")

    trib_proto_type100ge = Enum.YLeaf(18, "trib-proto-type100ge")

    trib_proto_type100g_mlg = Enum.YLeaf(19, "trib-proto-type100g-mlg")

    trib_proto_type_otu4 = Enum.YLeaf(20, "trib-proto-type-otu4")

    trib_proto_type_otu_cn = Enum.YLeaf(21, "trib-proto-type-otu-cn")

    trib_proto_type_odu4 = Enum.YLeaf(22, "trib-proto-type-odu4")


class LogicalTribRate(Enum):
    """
    LogicalTribRate

    Logical trib rate

    .. data:: trib_rate1g = 1

    	TribRate1G

    .. data:: trib_rate2_5g = 2

    	TribRate25G

    .. data:: trib_rate10g = 3

    	TribRate10G

    .. data:: trib_rate40g = 4

    	TribRate40G

    .. data:: trib_rate100g = 5

    	TribRate100G

    """

    trib_rate1g = Enum.YLeaf(1, "trib-rate1g")

    trib_rate2_5g = Enum.YLeaf(2, "trib-rate2-5g")

    trib_rate10g = Enum.YLeaf(3, "trib-rate10g")

    trib_rate40g = Enum.YLeaf(4, "trib-rate40g")

    trib_rate100g = Enum.YLeaf(5, "trib-rate100g")



class LogicalChannels(Entity):
    """
    Logical channel in mxp
    
    .. attribute:: channel
    
    	Logical channel index
    	**type**\: list of    :py:class:`Channel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_cfg.LogicalChannels.Channel>`
    
    

    """

    _prefix = 'terminal-device-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(LogicalChannels, self).__init__()
        self._top_entity = None

        self.yang_name = "logical-channels"
        self.yang_parent_name = "Cisco-IOS-XR-terminal-device-cfg"

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
                    super(LogicalChannels, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(LogicalChannels, self).__setattr__(name, value)


    class Channel(Entity):
        """
        Logical channel index
        
        .. attribute:: channel_index  <key>
        
        	Logical Channel Index
        	**type**\:  int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: admin_state
        
        	Configure the admin\-state 
        	**type**\:   :py:class:`LogicalAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_cfg.LogicalAdminState>`
        
        .. attribute:: description
        
        	Description (Max 255 characters)
        	**type**\:  str
        
        	**length:** 1..255
        
        .. attribute:: ingress_client_port
        
        	Configure ingress client port for this logical channel
        	**type**\:  str
        
        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
        
        .. attribute:: ingress_physical_channel
        
        	Configure ingress physical channel for this logical channel
        	**type**\:  int
        
        	**range:** 1..4
        
        .. attribute:: logical_channel_assignments
        
        	Logical channel assignment for logical channel
        	**type**\:   :py:class:`LogicalChannelAssignments <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_cfg.LogicalChannels.Channel.LogicalChannelAssignments>`
        
        .. attribute:: logical_channel_type
        
        	Configure the logical\-channel\-type 
        	**type**\:   :py:class:`LogicalProtocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_cfg.LogicalProtocol>`
        
        .. attribute:: loopback_mode
        
        	Configure the loopback mode 
        	**type**\:   :py:class:`LogicalLoopbackMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_cfg.LogicalLoopbackMode>`
        
        .. attribute:: otn
        
        	Otn Related configs for Logical channel
        	**type**\:   :py:class:`Otn <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_cfg.LogicalChannels.Channel.Otn>`
        
        .. attribute:: rate_class
        
        	Rounded bit rate of the tributary signal
        	**type**\:   :py:class:`LogicalTribRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_cfg.LogicalTribRate>`
        
        .. attribute:: trib_protocol
        
        	Protocol framing of the tributary signal
        	**type**\:   :py:class:`LogicalTribProtocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_cfg.LogicalTribProtocol>`
        
        

        """

        _prefix = 'terminal-device-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(LogicalChannels.Channel, self).__init__()

            self.yang_name = "channel"
            self.yang_parent_name = "logical-channels"

            self.channel_index = YLeaf(YType.int32, "channel-index")

            self.admin_state = YLeaf(YType.enumeration, "admin-state")

            self.description = YLeaf(YType.str, "description")

            self.ingress_client_port = YLeaf(YType.str, "ingress-client-port")

            self.ingress_physical_channel = YLeaf(YType.uint32, "ingress-physical-channel")

            self.logical_channel_type = YLeaf(YType.enumeration, "logical-channel-type")

            self.loopback_mode = YLeaf(YType.enumeration, "loopback-mode")

            self.rate_class = YLeaf(YType.enumeration, "rate-class")

            self.trib_protocol = YLeaf(YType.enumeration, "trib-protocol")

            self.logical_channel_assignments = LogicalChannels.Channel.LogicalChannelAssignments()
            self.logical_channel_assignments.parent = self
            self._children_name_map["logical_channel_assignments"] = "logical-channel-assignments"
            self._children_yang_names.add("logical-channel-assignments")

            self.otn = LogicalChannels.Channel.Otn()
            self.otn.parent = self
            self._children_name_map["otn"] = "otn"
            self._children_yang_names.add("otn")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("channel_index",
                            "admin_state",
                            "description",
                            "ingress_client_port",
                            "ingress_physical_channel",
                            "logical_channel_type",
                            "loopback_mode",
                            "rate_class",
                            "trib_protocol") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(LogicalChannels.Channel, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(LogicalChannels.Channel, self).__setattr__(name, value)


        class LogicalChannelAssignments(Entity):
            """
            Logical channel assignment for logical channel
            
            .. attribute:: logical_channel_assignment
            
            	Logical Channel Assignment id
            	**type**\: list of    :py:class:`LogicalChannelAssignment <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_cfg.LogicalChannels.Channel.LogicalChannelAssignments.LogicalChannelAssignment>`
            
            

            """

            _prefix = 'terminal-device-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(LogicalChannels.Channel.LogicalChannelAssignments, self).__init__()

                self.yang_name = "logical-channel-assignments"
                self.yang_parent_name = "channel"

                self.logical_channel_assignment = YList(self)

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
                            super(LogicalChannels.Channel.LogicalChannelAssignments, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(LogicalChannels.Channel.LogicalChannelAssignments, self).__setattr__(name, value)


            class LogicalChannelAssignment(Entity):
                """
                Logical Channel Assignment id
                
                .. attribute:: assignment_index  <key>
                
                	Logical channel assignment index
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: allocation
                
                	Configure Allocation for this assignment(10, 40 or 100G)
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: assignment_type
                
                	Type of assignment for logical channel
                	**type**\:   :py:class:`LogicalChannelAssignment <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_cfg.LogicalChannelAssignment>`
                
                .. attribute:: description
                
                	Configure description for this assignment
                	**type**\:  str
                
                	**length:** 1..255
                
                .. attribute:: logical_channel_id
                
                	Configure logical channel for this assignment
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: optical_channel_id
                
                	Configure optical channel for this assignment
                	**type**\:  str
                
                

                """

                _prefix = 'terminal-device-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(LogicalChannels.Channel.LogicalChannelAssignments.LogicalChannelAssignment, self).__init__()

                    self.yang_name = "logical-channel-assignment"
                    self.yang_parent_name = "logical-channel-assignments"

                    self.assignment_index = YLeaf(YType.int32, "assignment-index")

                    self.allocation = YLeaf(YType.int32, "allocation")

                    self.assignment_type = YLeaf(YType.enumeration, "assignment-type")

                    self.description = YLeaf(YType.str, "description")

                    self.logical_channel_id = YLeaf(YType.int32, "logical-channel-id")

                    self.optical_channel_id = YLeaf(YType.str, "optical-channel-id")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("assignment_index",
                                    "allocation",
                                    "assignment_type",
                                    "description",
                                    "logical_channel_id",
                                    "optical_channel_id") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(LogicalChannels.Channel.LogicalChannelAssignments.LogicalChannelAssignment, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(LogicalChannels.Channel.LogicalChannelAssignments.LogicalChannelAssignment, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.assignment_index.is_set or
                        self.allocation.is_set or
                        self.assignment_type.is_set or
                        self.description.is_set or
                        self.logical_channel_id.is_set or
                        self.optical_channel_id.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.assignment_index.yfilter != YFilter.not_set or
                        self.allocation.yfilter != YFilter.not_set or
                        self.assignment_type.yfilter != YFilter.not_set or
                        self.description.yfilter != YFilter.not_set or
                        self.logical_channel_id.yfilter != YFilter.not_set or
                        self.optical_channel_id.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "logical-channel-assignment" + "[assignment-index='" + self.assignment_index.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.assignment_index.is_set or self.assignment_index.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.assignment_index.get_name_leafdata())
                    if (self.allocation.is_set or self.allocation.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.allocation.get_name_leafdata())
                    if (self.assignment_type.is_set or self.assignment_type.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.assignment_type.get_name_leafdata())
                    if (self.description.is_set or self.description.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.description.get_name_leafdata())
                    if (self.logical_channel_id.is_set or self.logical_channel_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.logical_channel_id.get_name_leafdata())
                    if (self.optical_channel_id.is_set or self.optical_channel_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.optical_channel_id.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "assignment-index" or name == "allocation" or name == "assignment-type" or name == "description" or name == "logical-channel-id" or name == "optical-channel-id"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "assignment-index"):
                        self.assignment_index = value
                        self.assignment_index.value_namespace = name_space
                        self.assignment_index.value_namespace_prefix = name_space_prefix
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
                    if(value_path == "logical-channel-id"):
                        self.logical_channel_id = value
                        self.logical_channel_id.value_namespace = name_space
                        self.logical_channel_id.value_namespace_prefix = name_space_prefix
                    if(value_path == "optical-channel-id"):
                        self.optical_channel_id = value
                        self.optical_channel_id.value_namespace = name_space
                        self.optical_channel_id.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.logical_channel_assignment:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.logical_channel_assignment:
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

                if (child_yang_name == "logical-channel-assignment"):
                    for c in self.logical_channel_assignment:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = LogicalChannels.Channel.LogicalChannelAssignments.LogicalChannelAssignment()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.logical_channel_assignment.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "logical-channel-assignment"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class Otn(Entity):
            """
            Otn Related configs for Logical channel
            
            .. attribute:: tti_msg_auto
            
            	Trail trace identifier (TTI) transmit message automatically created. If True, then setting a custom transmit message would be invalid. Trail trace identifier (TTI) transmit message automatically created
            	**type**\:   :py:class:`LogicalChannelOtnTtiAuto <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_cfg.LogicalChannelOtnTtiAuto>`
            
            .. attribute:: tti_msg_expected
            
            	Trail trace identifier (TTI) message expectedTrail trace identifier (TTI) message expected
            	**type**\:  str
            
            	**length:** 1..255
            
            .. attribute:: tti_msg_transmit
            
            	Trail trace identifier (TTI) message transmittedTrail trace identifier (TTI) message transmitted
            	**type**\:  str
            
            	**length:** 1..255
            
            

            """

            _prefix = 'terminal-device-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(LogicalChannels.Channel.Otn, self).__init__()

                self.yang_name = "otn"
                self.yang_parent_name = "channel"

                self.tti_msg_auto = YLeaf(YType.enumeration, "tti-msg-auto")

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
                            super(LogicalChannels.Channel.Otn, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(LogicalChannels.Channel.Otn, self).__setattr__(name, value)

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
                path_buffer = "otn" + path_buffer

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

        def has_data(self):
            return (
                self.channel_index.is_set or
                self.admin_state.is_set or
                self.description.is_set or
                self.ingress_client_port.is_set or
                self.ingress_physical_channel.is_set or
                self.logical_channel_type.is_set or
                self.loopback_mode.is_set or
                self.rate_class.is_set or
                self.trib_protocol.is_set or
                (self.logical_channel_assignments is not None and self.logical_channel_assignments.has_data()) or
                (self.otn is not None and self.otn.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.channel_index.yfilter != YFilter.not_set or
                self.admin_state.yfilter != YFilter.not_set or
                self.description.yfilter != YFilter.not_set or
                self.ingress_client_port.yfilter != YFilter.not_set or
                self.ingress_physical_channel.yfilter != YFilter.not_set or
                self.logical_channel_type.yfilter != YFilter.not_set or
                self.loopback_mode.yfilter != YFilter.not_set or
                self.rate_class.yfilter != YFilter.not_set or
                self.trib_protocol.yfilter != YFilter.not_set or
                (self.logical_channel_assignments is not None and self.logical_channel_assignments.has_operation()) or
                (self.otn is not None and self.otn.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "channel" + "[channel-index='" + self.channel_index.get() + "']" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-terminal-device-cfg:logical-channels/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.channel_index.is_set or self.channel_index.yfilter != YFilter.not_set):
                leaf_name_data.append(self.channel_index.get_name_leafdata())
            if (self.admin_state.is_set or self.admin_state.yfilter != YFilter.not_set):
                leaf_name_data.append(self.admin_state.get_name_leafdata())
            if (self.description.is_set or self.description.yfilter != YFilter.not_set):
                leaf_name_data.append(self.description.get_name_leafdata())
            if (self.ingress_client_port.is_set or self.ingress_client_port.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ingress_client_port.get_name_leafdata())
            if (self.ingress_physical_channel.is_set or self.ingress_physical_channel.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ingress_physical_channel.get_name_leafdata())
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

            if (child_yang_name == "logical-channel-assignments"):
                if (self.logical_channel_assignments is None):
                    self.logical_channel_assignments = LogicalChannels.Channel.LogicalChannelAssignments()
                    self.logical_channel_assignments.parent = self
                    self._children_name_map["logical_channel_assignments"] = "logical-channel-assignments"
                return self.logical_channel_assignments

            if (child_yang_name == "otn"):
                if (self.otn is None):
                    self.otn = LogicalChannels.Channel.Otn()
                    self.otn.parent = self
                    self._children_name_map["otn"] = "otn"
                return self.otn

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "logical-channel-assignments" or name == "otn" or name == "channel-index" or name == "admin-state" or name == "description" or name == "ingress-client-port" or name == "ingress-physical-channel" or name == "logical-channel-type" or name == "loopback-mode" or name == "rate-class" or name == "trib-protocol"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "channel-index"):
                self.channel_index = value
                self.channel_index.value_namespace = name_space
                self.channel_index.value_namespace_prefix = name_space_prefix
            if(value_path == "admin-state"):
                self.admin_state = value
                self.admin_state.value_namespace = name_space
                self.admin_state.value_namespace_prefix = name_space_prefix
            if(value_path == "description"):
                self.description = value
                self.description.value_namespace = name_space
                self.description.value_namespace_prefix = name_space_prefix
            if(value_path == "ingress-client-port"):
                self.ingress_client_port = value
                self.ingress_client_port.value_namespace = name_space
                self.ingress_client_port.value_namespace_prefix = name_space_prefix
            if(value_path == "ingress-physical-channel"):
                self.ingress_physical_channel = value
                self.ingress_physical_channel.value_namespace = name_space
                self.ingress_physical_channel.value_namespace_prefix = name_space_prefix
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
        path_buffer = "Cisco-IOS-XR-terminal-device-cfg:logical-channels" + path_buffer

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

        if (child_yang_name == "channel"):
            for c in self.channel:
                segment = c.get_segment_path()
                if (segment_path == segment):
                    return c
            c = LogicalChannels.Channel()
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

    def clone_ptr(self):
        self._top_entity = LogicalChannels()
        return self._top_entity

class OpticalChannels(Entity):
    """
    optical channels
    
    .. attribute:: optical_channel
    
    	Optical Channel index
    	**type**\: list of    :py:class:`OpticalChannel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_cfg.OpticalChannels.OpticalChannel>`
    
    

    """

    _prefix = 'terminal-device-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(OpticalChannels, self).__init__()
        self._top_entity = None

        self.yang_name = "optical-channels"
        self.yang_parent_name = "Cisco-IOS-XR-terminal-device-cfg"

        self.optical_channel = YList(self)

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
                    super(OpticalChannels, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(OpticalChannels, self).__setattr__(name, value)


    class OpticalChannel(Entity):
        """
        Optical Channel index
        
        .. attribute:: ifname  <key>
        
        	Optical Channel Name
        	**type**\:  str
        
        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
        
        .. attribute:: line_port
        
        	Specify R/S/I/P
        	**type**\:  str
        
        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
        
        .. attribute:: operational_mode
        
        	Configure operational mode
        	**type**\:  int
        
        	**range:** 1..100000
        
        

        """

        _prefix = 'terminal-device-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(OpticalChannels.OpticalChannel, self).__init__()

            self.yang_name = "optical-channel"
            self.yang_parent_name = "optical-channels"

            self.ifname = YLeaf(YType.str, "ifname")

            self.line_port = YLeaf(YType.str, "line-port")

            self.operational_mode = YLeaf(YType.uint32, "operational-mode")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("ifname",
                            "line_port",
                            "operational_mode") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(OpticalChannels.OpticalChannel, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(OpticalChannels.OpticalChannel, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.ifname.is_set or
                self.line_port.is_set or
                self.operational_mode.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.ifname.yfilter != YFilter.not_set or
                self.line_port.yfilter != YFilter.not_set or
                self.operational_mode.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "optical-channel" + "[ifname='" + self.ifname.get() + "']" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-terminal-device-cfg:optical-channels/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.ifname.is_set or self.ifname.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ifname.get_name_leafdata())
            if (self.line_port.is_set or self.line_port.yfilter != YFilter.not_set):
                leaf_name_data.append(self.line_port.get_name_leafdata())
            if (self.operational_mode.is_set or self.operational_mode.yfilter != YFilter.not_set):
                leaf_name_data.append(self.operational_mode.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ifname" or name == "line-port" or name == "operational-mode"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "ifname"):
                self.ifname = value
                self.ifname.value_namespace = name_space
                self.ifname.value_namespace_prefix = name_space_prefix
            if(value_path == "line-port"):
                self.line_port = value
                self.line_port.value_namespace = name_space
                self.line_port.value_namespace_prefix = name_space_prefix
            if(value_path == "operational-mode"):
                self.operational_mode = value
                self.operational_mode.value_namespace = name_space
                self.operational_mode.value_namespace_prefix = name_space_prefix

    def has_data(self):
        for c in self.optical_channel:
            if (c.has_data()):
                return True
        return False

    def has_operation(self):
        for c in self.optical_channel:
            if (c.has_operation()):
                return True
        return self.yfilter != YFilter.not_set

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-terminal-device-cfg:optical-channels" + path_buffer

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

        if (child_yang_name == "optical-channel"):
            for c in self.optical_channel:
                segment = c.get_segment_path()
                if (segment_path == segment):
                    return c
            c = OpticalChannels.OpticalChannel()
            c.parent = self
            local_reference_key = "ydk::seg::%s" % segment_path
            self._local_refs[local_reference_key] = c
            self.optical_channel.append(c)
            return c

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "optical-channel"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = OpticalChannels()
        return self._top_entity

