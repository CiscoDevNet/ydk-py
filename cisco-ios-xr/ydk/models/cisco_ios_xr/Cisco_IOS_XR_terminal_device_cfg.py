""" Cisco_IOS_XR_terminal_device_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR terminal\-device package configuration.

This module contains definitions
for the following management objects\:
  logical\-channels\: Logical channel in mxp
  optical\-channels\: optical channels

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class LogicalAdminState(Enum):
    """
    LogicalAdminState (Enum Class)

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
    LogicalChannelAssignment (Enum Class)

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
    LogicalChannelOtnTtiAuto (Enum Class)

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
    LogicalLoopbackMode (Enum Class)

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
    LogicalProtocol (Enum Class)

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
    LogicalTribProtocol (Enum Class)

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
    LogicalTribRate (Enum Class)

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
    	**type**\: list of  		 :py:class:`Channel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_cfg.LogicalChannels.Channel>`
    
    

    """

    _prefix = 'terminal-device-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(LogicalChannels, self).__init__()
        self._top_entity = None

        self.yang_name = "logical-channels"
        self.yang_parent_name = "Cisco-IOS-XR-terminal-device-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("channel", ("channel", LogicalChannels.Channel))])
        self._leafs = OrderedDict()

        self.channel = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-terminal-device-cfg:logical-channels"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(LogicalChannels, [], name, value)


    class Channel(Entity):
        """
        Logical channel index
        
        .. attribute:: channel_index  (key)
        
        	Logical Channel Index
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: logical_channel_assignments
        
        	Logical channel assignment for logical channel
        	**type**\:  :py:class:`LogicalChannelAssignments <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_cfg.LogicalChannels.Channel.LogicalChannelAssignments>`
        
        .. attribute:: otn
        
        	Otn Related configs for Logical channel
        	**type**\:  :py:class:`Otn <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_cfg.LogicalChannels.Channel.Otn>`
        
        .. attribute:: trib_protocol
        
        	Protocol framing of the tributary signal
        	**type**\:  :py:class:`LogicalTribProtocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_cfg.LogicalTribProtocol>`
        
        .. attribute:: description
        
        	Description (Max 255 characters)
        	**type**\: str
        
        	**length:** 1..255
        
        .. attribute:: ingress_client_port
        
        	Configure ingress client port for this logical channel
        	**type**\: str
        
        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
        
        .. attribute:: ingress_physical_channel
        
        	Configure ingress physical channel for this logical channel
        	**type**\: int
        
        	**range:** 1..4
        
        .. attribute:: admin_state
        
        	Configure the admin\-state 
        	**type**\:  :py:class:`LogicalAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_cfg.LogicalAdminState>`
        
        .. attribute:: loopback_mode
        
        	Configure the loopback mode 
        	**type**\:  :py:class:`LogicalLoopbackMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_cfg.LogicalLoopbackMode>`
        
        .. attribute:: logical_channel_type
        
        	Configure the logical\-channel\-type 
        	**type**\:  :py:class:`LogicalProtocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_cfg.LogicalProtocol>`
        
        .. attribute:: rate_class
        
        	Rounded bit rate of the tributary signal
        	**type**\:  :py:class:`LogicalTribRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_cfg.LogicalTribRate>`
        
        

        """

        _prefix = 'terminal-device-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(LogicalChannels.Channel, self).__init__()

            self.yang_name = "channel"
            self.yang_parent_name = "logical-channels"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['channel_index']
            self._child_classes = OrderedDict([("logical-channel-assignments", ("logical_channel_assignments", LogicalChannels.Channel.LogicalChannelAssignments)), ("otn", ("otn", LogicalChannels.Channel.Otn))])
            self._leafs = OrderedDict([
                ('channel_index', (YLeaf(YType.uint32, 'channel-index'), ['int'])),
                ('trib_protocol', (YLeaf(YType.enumeration, 'trib-protocol'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_cfg', 'LogicalTribProtocol', '')])),
                ('description', (YLeaf(YType.str, 'description'), ['str'])),
                ('ingress_client_port', (YLeaf(YType.str, 'ingress-client-port'), ['str'])),
                ('ingress_physical_channel', (YLeaf(YType.uint32, 'ingress-physical-channel'), ['int'])),
                ('admin_state', (YLeaf(YType.enumeration, 'admin-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_cfg', 'LogicalAdminState', '')])),
                ('loopback_mode', (YLeaf(YType.enumeration, 'loopback-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_cfg', 'LogicalLoopbackMode', '')])),
                ('logical_channel_type', (YLeaf(YType.enumeration, 'logical-channel-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_cfg', 'LogicalProtocol', '')])),
                ('rate_class', (YLeaf(YType.enumeration, 'rate-class'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_cfg', 'LogicalTribRate', '')])),
            ])
            self.channel_index = None
            self.trib_protocol = None
            self.description = None
            self.ingress_client_port = None
            self.ingress_physical_channel = None
            self.admin_state = None
            self.loopback_mode = None
            self.logical_channel_type = None
            self.rate_class = None

            self.logical_channel_assignments = LogicalChannels.Channel.LogicalChannelAssignments()
            self.logical_channel_assignments.parent = self
            self._children_name_map["logical_channel_assignments"] = "logical-channel-assignments"

            self.otn = LogicalChannels.Channel.Otn()
            self.otn.parent = self
            self._children_name_map["otn"] = "otn"
            self._segment_path = lambda: "channel" + "[channel-index='" + str(self.channel_index) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-terminal-device-cfg:logical-channels/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(LogicalChannels.Channel, ['channel_index', 'trib_protocol', 'description', 'ingress_client_port', 'ingress_physical_channel', 'admin_state', 'loopback_mode', 'logical_channel_type', 'rate_class'], name, value)


        class LogicalChannelAssignments(Entity):
            """
            Logical channel assignment for logical channel
            
            .. attribute:: logical_channel_assignment
            
            	Logical Channel Assignment id
            	**type**\: list of  		 :py:class:`LogicalChannelAssignment <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_cfg.LogicalChannels.Channel.LogicalChannelAssignments.LogicalChannelAssignment>`
            
            

            """

            _prefix = 'terminal-device-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(LogicalChannels.Channel.LogicalChannelAssignments, self).__init__()

                self.yang_name = "logical-channel-assignments"
                self.yang_parent_name = "channel"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("logical-channel-assignment", ("logical_channel_assignment", LogicalChannels.Channel.LogicalChannelAssignments.LogicalChannelAssignment))])
                self._leafs = OrderedDict()

                self.logical_channel_assignment = YList(self)
                self._segment_path = lambda: "logical-channel-assignments"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(LogicalChannels.Channel.LogicalChannelAssignments, [], name, value)


            class LogicalChannelAssignment(Entity):
                """
                Logical Channel Assignment id
                
                .. attribute:: assignment_index  (key)
                
                	Logical channel assignment index
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: description
                
                	Configure description for this assignment
                	**type**\: str
                
                	**length:** 1..255
                
                .. attribute:: logical_channel_id
                
                	Configure logical channel for this assignment
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: assignment_type
                
                	Type of assignment for logical channel
                	**type**\:  :py:class:`LogicalChannelAssignment <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_cfg.LogicalChannelAssignment>`
                
                .. attribute:: allocation
                
                	Configure Allocation for this assignment(10, 40 or 100G)
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: optical_channel_id
                
                	Configure optical channel for this assignment
                	**type**\: str
                
                

                """

                _prefix = 'terminal-device-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(LogicalChannels.Channel.LogicalChannelAssignments.LogicalChannelAssignment, self).__init__()

                    self.yang_name = "logical-channel-assignment"
                    self.yang_parent_name = "logical-channel-assignments"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['assignment_index']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('assignment_index', (YLeaf(YType.uint32, 'assignment-index'), ['int'])),
                        ('description', (YLeaf(YType.str, 'description'), ['str'])),
                        ('logical_channel_id', (YLeaf(YType.uint32, 'logical-channel-id'), ['int'])),
                        ('assignment_type', (YLeaf(YType.enumeration, 'assignment-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_cfg', 'LogicalChannelAssignment', '')])),
                        ('allocation', (YLeaf(YType.uint32, 'allocation'), ['int'])),
                        ('optical_channel_id', (YLeaf(YType.str, 'optical-channel-id'), ['str'])),
                    ])
                    self.assignment_index = None
                    self.description = None
                    self.logical_channel_id = None
                    self.assignment_type = None
                    self.allocation = None
                    self.optical_channel_id = None
                    self._segment_path = lambda: "logical-channel-assignment" + "[assignment-index='" + str(self.assignment_index) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(LogicalChannels.Channel.LogicalChannelAssignments.LogicalChannelAssignment, ['assignment_index', 'description', 'logical_channel_id', 'assignment_type', 'allocation', 'optical_channel_id'], name, value)


        class Otn(Entity):
            """
            Otn Related configs for Logical channel
            
            .. attribute:: tti_msg_auto
            
            	Trail trace identifier (TTI) transmit message automatically created. If True, then setting a custom transmit message would be invalid. Trail trace identifier (TTI) transmit message automatically created
            	**type**\:  :py:class:`LogicalChannelOtnTtiAuto <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_cfg.LogicalChannelOtnTtiAuto>`
            
            .. attribute:: tti_msg_expected
            
            	Trail trace identifier (TTI) message expectedTrail trace identifier (TTI) message expected
            	**type**\: str
            
            	**length:** 1..255
            
            .. attribute:: tti_msg_transmit
            
            	Trail trace identifier (TTI) message transmittedTrail trace identifier (TTI) message transmitted
            	**type**\: str
            
            	**length:** 1..255
            
            

            """

            _prefix = 'terminal-device-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(LogicalChannels.Channel.Otn, self).__init__()

                self.yang_name = "otn"
                self.yang_parent_name = "channel"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('tti_msg_auto', (YLeaf(YType.enumeration, 'tti-msg-auto'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_cfg', 'LogicalChannelOtnTtiAuto', '')])),
                    ('tti_msg_expected', (YLeaf(YType.str, 'tti-msg-expected'), ['str'])),
                    ('tti_msg_transmit', (YLeaf(YType.str, 'tti-msg-transmit'), ['str'])),
                ])
                self.tti_msg_auto = None
                self.tti_msg_expected = None
                self.tti_msg_transmit = None
                self._segment_path = lambda: "otn"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(LogicalChannels.Channel.Otn, ['tti_msg_auto', 'tti_msg_expected', 'tti_msg_transmit'], name, value)

    def clone_ptr(self):
        self._top_entity = LogicalChannels()
        return self._top_entity

class OpticalChannels(Entity):
    """
    optical channels
    
    .. attribute:: optical_channel
    
    	Optical Channel index
    	**type**\: list of  		 :py:class:`OpticalChannel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_cfg.OpticalChannels.OpticalChannel>`
    
    

    """

    _prefix = 'terminal-device-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(OpticalChannels, self).__init__()
        self._top_entity = None

        self.yang_name = "optical-channels"
        self.yang_parent_name = "Cisco-IOS-XR-terminal-device-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("optical-channel", ("optical_channel", OpticalChannels.OpticalChannel))])
        self._leafs = OrderedDict()

        self.optical_channel = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-terminal-device-cfg:optical-channels"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(OpticalChannels, [], name, value)


    class OpticalChannel(Entity):
        """
        Optical Channel index
        
        .. attribute:: ifname  (key)
        
        	Optical Channel Name
        	**type**\: str
        
        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
        
        .. attribute:: operational_mode
        
        	Configure operational mode
        	**type**\: int
        
        	**range:** 1..100000
        
        .. attribute:: line_port
        
        	Specify R/S/I/P
        	**type**\: str
        
        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
        
        

        """

        _prefix = 'terminal-device-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(OpticalChannels.OpticalChannel, self).__init__()

            self.yang_name = "optical-channel"
            self.yang_parent_name = "optical-channels"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['ifname']
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('ifname', (YLeaf(YType.str, 'ifname'), ['str'])),
                ('operational_mode', (YLeaf(YType.uint32, 'operational-mode'), ['int'])),
                ('line_port', (YLeaf(YType.str, 'line-port'), ['str'])),
            ])
            self.ifname = None
            self.operational_mode = None
            self.line_port = None
            self._segment_path = lambda: "optical-channel" + "[ifname='" + str(self.ifname) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-terminal-device-cfg:optical-channels/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(OpticalChannels.OpticalChannel, ['ifname', 'operational_mode', 'line_port'], name, value)

    def clone_ptr(self):
        self._top_entity = OpticalChannels()
        return self._top_entity

