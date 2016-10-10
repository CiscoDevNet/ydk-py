""" Cisco_IOS_XR_openconfig_terminal_device_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR openconfig\-terminal\-device package configuration.

This module contains definitions
for the following management objects\:
  logical\-channels\: Logical channel in mxp
  optical\-channels\: optical channels

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class LogicalAdminStateEnum(Enum):
    """
    LogicalAdminStateEnum

    Logical admin state

    .. data:: ENABLE = 1

    	Enable

    .. data:: DISABLE = 2

    	Disable

    .. data:: MAINTENANCE = 3

    	Maintenance

    """

    ENABLE = 1

    DISABLE = 2

    MAINTENANCE = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_openconfig_terminal_device_cfg as meta
        return meta._meta_table['LogicalAdminStateEnum']


class LogicalChannelAssignmentEnum(Enum):
    """
    LogicalChannelAssignmentEnum

    Logical channel assignment

    .. data:: TYPE_LOGICAL_CHANNEL = 1

    	Type Logical channel

    .. data:: TYPE_OPTICAL_CHANNEL = 2

    	Type Optical channel

    """

    TYPE_LOGICAL_CHANNEL = 1

    TYPE_OPTICAL_CHANNEL = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_openconfig_terminal_device_cfg as meta
        return meta._meta_table['LogicalChannelAssignmentEnum']


class LogicalChannelOtnTtiAutoEnum(Enum):
    """
    LogicalChannelOtnTtiAutoEnum

    Logical channel otn tti auto

    .. data:: FALSE = 0

    	Otn tti auto mode false

    .. data:: TRUE = 1

    	Otn tti auto mode true

    """

    FALSE = 0

    TRUE = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_openconfig_terminal_device_cfg as meta
        return meta._meta_table['LogicalChannelOtnTtiAutoEnum']


class LogicalLoopbackModeEnum(Enum):
    """
    LogicalLoopbackModeEnum

    Logical loopback mode

    .. data:: NONE = 1

    	None

    .. data:: FACILITY = 2

    	Facility

    .. data:: TERMINAL = 3

    	Terminal

    """

    NONE = 1

    FACILITY = 2

    TERMINAL = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_openconfig_terminal_device_cfg as meta
        return meta._meta_table['LogicalLoopbackModeEnum']


class LogicalProtocolEnum(Enum):
    """
    LogicalProtocolEnum

    Logical protocol

    .. data:: TYPE_ETHERNET = 1

    	Type Ethernet

    .. data:: TYPE_OTN = 2

    	Type OTN

    """

    TYPE_ETHERNET = 1

    TYPE_OTN = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_openconfig_terminal_device_cfg as meta
        return meta._meta_table['LogicalProtocolEnum']


class LogicalTribProtocolEnum(Enum):
    """
    LogicalTribProtocolEnum

    Logical trib protocol

    .. data:: TRIB_PROTO_TYPE1GE = 1

    	1G Ethernet protocol

    .. data:: TRIB_PROTO_TYPE_OC48 = 2

    	OC48 protocol

    .. data:: TRIB_PROTO_TYPE_STM16 = 3

    	STM 16 protocol

    .. data:: TRIB_PROTO_TYPE10GELAN = 4

    	10G Ethernet LAN protocol

    .. data:: TRIB_PROTO_TYPE10GEWAN = 5

    	10G Ethernet WAN protocol

    .. data:: TRIB_PROTO_TYPE_OC192 = 6

    	OC 192 (9.6GB) port protocol

    .. data:: TRIB_PROTO_TYPE_STM64 = 7

    	STM 64 protocol

    .. data:: TRIB_PROTO_TYPE_OTU2 = 8

    	OTU 2 protocol

    .. data:: TRIB_PROTO_TYPE_OTU2E = 9

    	OTU 2e protocol

    .. data:: TRIB_PROTO_TYPE_OTU1E = 10

    	OTU 1e protocol

    .. data:: TRIB_PROTO_TYPE_ODU2 = 11

    	ODU 2 protocol

    .. data:: TRIB_PROTO_TYPE_ODU2E = 12

    	ODU 2e protocol

    .. data:: TRIB_PROTO_TYPE40GE = 13

    	40G Ethernet port protocol

    .. data:: TRIB_PROTO_TYPE_OC768 = 14

    	OC 768 protocol

    .. data:: TRIB_PROTO_TYPE_STM256 = 15

    	STM 256 protocol

    .. data:: TRIB_PROTO_TYPE_OTU3 = 16

    	OTU 3 protocol

    .. data:: TRIB_PROTO_TYPE_ODU3 = 17

    	ODU 3 protocol

    .. data:: TRIB_PROTO_TYPE100GE = 18

    	100G Ethernet protocol

    .. data:: TRIB_PROTO_TYPE100G_MLG = 19

    	100G MLG protocol

    .. data:: TRIB_PROTO_TYPE_OTU4 = 20

    	OTU4 signal protocol (112G) for transporting

    	100GE signal

    .. data:: TRIB_PROTO_TYPE_OTU_CN = 21

    	OTU Cn protocol

    .. data:: TRIB_PROTO_TYPE_ODU4 = 22

    	ODU 4 protocol

    """

    TRIB_PROTO_TYPE1GE = 1

    TRIB_PROTO_TYPE_OC48 = 2

    TRIB_PROTO_TYPE_STM16 = 3

    TRIB_PROTO_TYPE10GELAN = 4

    TRIB_PROTO_TYPE10GEWAN = 5

    TRIB_PROTO_TYPE_OC192 = 6

    TRIB_PROTO_TYPE_STM64 = 7

    TRIB_PROTO_TYPE_OTU2 = 8

    TRIB_PROTO_TYPE_OTU2E = 9

    TRIB_PROTO_TYPE_OTU1E = 10

    TRIB_PROTO_TYPE_ODU2 = 11

    TRIB_PROTO_TYPE_ODU2E = 12

    TRIB_PROTO_TYPE40GE = 13

    TRIB_PROTO_TYPE_OC768 = 14

    TRIB_PROTO_TYPE_STM256 = 15

    TRIB_PROTO_TYPE_OTU3 = 16

    TRIB_PROTO_TYPE_ODU3 = 17

    TRIB_PROTO_TYPE100GE = 18

    TRIB_PROTO_TYPE100G_MLG = 19

    TRIB_PROTO_TYPE_OTU4 = 20

    TRIB_PROTO_TYPE_OTU_CN = 21

    TRIB_PROTO_TYPE_ODU4 = 22


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_openconfig_terminal_device_cfg as meta
        return meta._meta_table['LogicalTribProtocolEnum']


class LogicalTribRateEnum(Enum):
    """
    LogicalTribRateEnum

    Logical trib rate

    .. data:: TRIB_RATE1G = 0

    	TribRate1G

    .. data:: TRIB_RATE2_5G = 1

    	TribRate25G

    .. data:: TRIB_RATE10G = 2

    	TribRate10G

    .. data:: TRIB_RATE40G = 3

    	TribRate40G

    .. data:: TRIB_RATE100G = 4

    	TribRate100G

    """

    TRIB_RATE1G = 0

    TRIB_RATE2_5G = 1

    TRIB_RATE10G = 2

    TRIB_RATE40G = 3

    TRIB_RATE100G = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_openconfig_terminal_device_cfg as meta
        return meta._meta_table['LogicalTribRateEnum']



class LogicalChannels(object):
    """
    Logical channel in mxp
    
    .. attribute:: channel
    
    	Logical channel index
    	**type**\: list of  :py:class:`Channel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_cfg.LogicalChannels.Channel>`
    
    

    """

    _prefix = 'openconfig-terminal-device-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.channel = YList()
        self.channel.parent = self
        self.channel.name = 'channel'


    class Channel(object):
        """
        Logical channel index
        
        .. attribute:: channel_index  <key>
        
        	Logical Channel Index
        	**type**\:  int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: admin_state
        
        	Configure the admin\-state 
        	**type**\:  :py:class:`LogicalAdminStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_cfg.LogicalAdminStateEnum>`
        
        .. attribute:: description
        
        	Description (Max 255 characters)
        	**type**\:  str
        
        	**range:** 0..255
        
        .. attribute:: ingress_client_port
        
        	Configure ingress client port for this logical channel
        	**type**\:  str
        
        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
        
        .. attribute:: ingress_physical_channel
        
        	Configure ingress physical channel for this logical channel
        	**type**\:  int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: logical_channel_assignments
        
        	Logical channel assignment for logical channel
        	**type**\:  :py:class:`LogicalChannelAssignments <ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_cfg.LogicalChannels.Channel.LogicalChannelAssignments>`
        
        .. attribute:: logical_channel_type
        
        	Configure the logical\-channel\-type 
        	**type**\:  :py:class:`LogicalProtocolEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_cfg.LogicalProtocolEnum>`
        
        .. attribute:: loopback_mode
        
        	Configure the loopback mode 
        	**type**\:  :py:class:`LogicalLoopbackModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_cfg.LogicalLoopbackModeEnum>`
        
        .. attribute:: otn
        
        	Otn Related configs for Logical channel
        	**type**\:  :py:class:`Otn <ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_cfg.LogicalChannels.Channel.Otn>`
        
        .. attribute:: rate_class
        
        	Rounded bit rate of the tributary signal
        	**type**\:  :py:class:`LogicalTribRateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_cfg.LogicalTribRateEnum>`
        
        .. attribute:: trib_protocol
        
        	Protocol framing of the tributary signal
        	**type**\:  :py:class:`LogicalTribProtocolEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_cfg.LogicalTribProtocolEnum>`
        
        

        """

        _prefix = 'openconfig-terminal-device-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.channel_index = None
            self.admin_state = None
            self.description = None
            self.ingress_client_port = None
            self.ingress_physical_channel = None
            self.logical_channel_assignments = LogicalChannels.Channel.LogicalChannelAssignments()
            self.logical_channel_assignments.parent = self
            self.logical_channel_type = None
            self.loopback_mode = None
            self.otn = LogicalChannels.Channel.Otn()
            self.otn.parent = self
            self.rate_class = None
            self.trib_protocol = None


        class LogicalChannelAssignments(object):
            """
            Logical channel assignment for logical channel
            
            .. attribute:: logical_channel_assignment
            
            	Logical Channel Assignment id
            	**type**\: list of  :py:class:`LogicalChannelAssignment <ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_cfg.LogicalChannels.Channel.LogicalChannelAssignments.LogicalChannelAssignment>`
            
            

            """

            _prefix = 'openconfig-terminal-device-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.logical_channel_assignment = YList()
                self.logical_channel_assignment.parent = self
                self.logical_channel_assignment.name = 'logical_channel_assignment'


            class LogicalChannelAssignment(object):
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
                	**type**\:  :py:class:`LogicalChannelAssignmentEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_cfg.LogicalChannelAssignmentEnum>`
                
                .. attribute:: description
                
                	Configure description for this assignment
                	**type**\:  str
                
                	**range:** 0..255
                
                .. attribute:: logical_channel_id
                
                	Configure logical channel for this assignment
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: optical_channel_id
                
                	Configure optical channel for this assignment
                	**type**\:  str
                
                

                """

                _prefix = 'openconfig-terminal-device-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.assignment_index = None
                    self.allocation = None
                    self.assignment_type = None
                    self.description = None
                    self.logical_channel_id = None
                    self.optical_channel_id = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.assignment_index is None:
                        raise YPYModelError('Key property assignment_index is None')

                    return self.parent._common_path +'/Cisco-IOS-XR-openconfig-terminal-device-cfg:logical-channel-assignment[Cisco-IOS-XR-openconfig-terminal-device-cfg:assignment-index = ' + str(self.assignment_index) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.assignment_index is not None:
                        return True

                    if self.allocation is not None:
                        return True

                    if self.assignment_type is not None:
                        return True

                    if self.description is not None:
                        return True

                    if self.logical_channel_id is not None:
                        return True

                    if self.optical_channel_id is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_openconfig_terminal_device_cfg as meta
                    return meta._meta_table['LogicalChannels.Channel.LogicalChannelAssignments.LogicalChannelAssignment']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/Cisco-IOS-XR-openconfig-terminal-device-cfg:logical-channel-assignments'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.logical_channel_assignment is not None:
                    for child_ref in self.logical_channel_assignment:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_openconfig_terminal_device_cfg as meta
                return meta._meta_table['LogicalChannels.Channel.LogicalChannelAssignments']['meta_info']


        class Otn(object):
            """
            Otn Related configs for Logical channel
            
            .. attribute:: tti_msg_auto
            
            	Trail trace identifier (TTI) transmit message automatically created. If True, then setting a custom transmit message would be invalid. Trail trace identifier (TTI) transmit message automatically created
            	**type**\:  :py:class:`LogicalChannelOtnTtiAutoEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_cfg.LogicalChannelOtnTtiAutoEnum>`
            
            .. attribute:: tti_msg_expected
            
            	Trail trace identifier (TTI) message expectedTrail trace identifier (TTI) message expected
            	**type**\:  str
            
            	**range:** 0..255
            
            .. attribute:: tti_msg_transmit
            
            	Trail trace identifier (TTI) message transmittedTrail trace identifier (TTI) message transmitted
            	**type**\:  str
            
            	**range:** 0..255
            
            

            """

            _prefix = 'openconfig-terminal-device-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.tti_msg_auto = None
                self.tti_msg_expected = None
                self.tti_msg_transmit = None

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/Cisco-IOS-XR-openconfig-terminal-device-cfg:otn'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.tti_msg_auto is not None:
                    return True

                if self.tti_msg_expected is not None:
                    return True

                if self.tti_msg_transmit is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_openconfig_terminal_device_cfg as meta
                return meta._meta_table['LogicalChannels.Channel.Otn']['meta_info']

        @property
        def _common_path(self):
            if self.channel_index is None:
                raise YPYModelError('Key property channel_index is None')

            return '/Cisco-IOS-XR-openconfig-terminal-device-cfg:logical-channels/Cisco-IOS-XR-openconfig-terminal-device-cfg:channel[Cisco-IOS-XR-openconfig-terminal-device-cfg:channel-index = ' + str(self.channel_index) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.channel_index is not None:
                return True

            if self.admin_state is not None:
                return True

            if self.description is not None:
                return True

            if self.ingress_client_port is not None:
                return True

            if self.ingress_physical_channel is not None:
                return True

            if self.logical_channel_assignments is not None and self.logical_channel_assignments._has_data():
                return True

            if self.logical_channel_type is not None:
                return True

            if self.loopback_mode is not None:
                return True

            if self.otn is not None and self.otn._has_data():
                return True

            if self.rate_class is not None:
                return True

            if self.trib_protocol is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_openconfig_terminal_device_cfg as meta
            return meta._meta_table['LogicalChannels.Channel']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-openconfig-terminal-device-cfg:logical-channels'

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
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_openconfig_terminal_device_cfg as meta
        return meta._meta_table['LogicalChannels']['meta_info']


class OpticalChannels(object):
    """
    optical channels
    
    .. attribute:: optical_channel
    
    	Optical Channel index
    	**type**\: list of  :py:class:`OpticalChannel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_cfg.OpticalChannels.OpticalChannel>`
    
    

    """

    _prefix = 'openconfig-terminal-device-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.optical_channel = YList()
        self.optical_channel.parent = self
        self.optical_channel.name = 'optical_channel'


    class OpticalChannel(object):
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

        _prefix = 'openconfig-terminal-device-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.ifname = None
            self.line_port = None
            self.operational_mode = None

        @property
        def _common_path(self):
            if self.ifname is None:
                raise YPYModelError('Key property ifname is None')

            return '/Cisco-IOS-XR-openconfig-terminal-device-cfg:optical-channels/Cisco-IOS-XR-openconfig-terminal-device-cfg:optical-channel[Cisco-IOS-XR-openconfig-terminal-device-cfg:ifname = ' + str(self.ifname) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.ifname is not None:
                return True

            if self.line_port is not None:
                return True

            if self.operational_mode is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_openconfig_terminal_device_cfg as meta
            return meta._meta_table['OpticalChannels.OpticalChannel']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-openconfig-terminal-device-cfg:optical-channels'

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
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_openconfig_terminal_device_cfg as meta
        return meta._meta_table['OpticalChannels']['meta_info']


