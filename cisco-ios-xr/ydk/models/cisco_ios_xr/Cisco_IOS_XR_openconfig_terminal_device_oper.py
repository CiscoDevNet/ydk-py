""" Cisco_IOS_XR_openconfig_terminal_device_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR openconfig\-terminal\-device package operational data.

This module contains definitions
for the following management objects\:
  optical\-interface\: System\-wide view of interface operational
    data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class LogicalProtocolEnum(Enum):
    """
    LogicalProtocolEnum

    Logical protocol

    .. data:: proto_type_unknown = 0

    	Unknown protocol framing

    .. data:: proto_type_ethernet = 1

    	Ethernet protocol framing

    .. data:: proto_type_otn = 2

    	OTN protocol framing

    """

    proto_type_unknown = 0

    proto_type_ethernet = 1

    proto_type_otn = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_openconfig_terminal_device_oper as meta
        return meta._meta_table['LogicalProtocolEnum']


class TribProtocolEnum(Enum):
    """
    TribProtocolEnum

    Trib protocol

    .. data:: trib_proto_type_unknown = 0

    	Unknown protocol

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

    trib_proto_type_unknown = 0

    trib_proto_type1ge = 1

    trib_proto_type_oc48 = 2

    trib_proto_type_stm16 = 3

    trib_proto_type10gelan = 4

    trib_proto_type10gewan = 5

    trib_proto_type_oc192 = 6

    trib_proto_type_stm64 = 7

    trib_proto_type_otu2 = 8

    trib_proto_type_otu2e = 9

    trib_proto_type_otu1e = 10

    trib_proto_type_odu2 = 11

    trib_proto_type_odu2e = 12

    trib_proto_type40ge = 13

    trib_proto_type_oc768 = 14

    trib_proto_type_stm256 = 15

    trib_proto_type_otu3 = 16

    trib_proto_type_odu3 = 17

    trib_proto_type100ge = 18

    trib_proto_type100g_mlg = 19

    trib_proto_type_otu4 = 20

    trib_proto_type_otu_cn = 21

    trib_proto_type_odu4 = 22


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_openconfig_terminal_device_oper as meta
        return meta._meta_table['TribProtocolEnum']


class TribRateClassEnum(Enum):
    """
    TribRateClassEnum

    Trib rate class

    .. data:: trib_rate1g = 0

    	1G tributary signal rate

    .. data:: trib_rate25g = 1

    	2.5G tributary signal rate

    .. data:: trib_rate10g = 2

    	10G tributary signal rate

    .. data:: trib_rate40g = 3

    	40G tributary signal rate

    .. data:: trib_rate100g = 4

    	100G tributary signal rate

    .. data:: trib_rate_unknown = 5

    	Unknown tributary signal rate

    """

    trib_rate1g = 0

    trib_rate25g = 1

    trib_rate10g = 2

    trib_rate40g = 3

    trib_rate100g = 4

    trib_rate_unknown = 5


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_openconfig_terminal_device_oper as meta
        return meta._meta_table['TribRateClassEnum']



class OpticalInterface(object):
    """
    System\-wide view of interface operational data
    
    .. attribute:: operational_modes
    
    	The Operational Mode Table
    	**type**\:   :py:class:`OperationalModes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_oper.OpticalInterface.OperationalModes>`
    
    .. attribute:: optical_client_interfaces
    
    	The operational attributes table for Client Port
    	**type**\:   :py:class:`OpticalClientInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_oper.OpticalInterface.OpticalClientInterfaces>`
    
    .. attribute:: optical_logical_interfaces
    
    	The operational attributes for a particular interface
    	**type**\:   :py:class:`OpticalLogicalInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_oper.OpticalInterface.OpticalLogicalInterfaces>`
    
    

    """

    _prefix = 'openconfig-terminal-device-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.operational_modes = OpticalInterface.OperationalModes()
        self.operational_modes.parent = self
        self.optical_client_interfaces = OpticalInterface.OpticalClientInterfaces()
        self.optical_client_interfaces.parent = self
        self.optical_logical_interfaces = OpticalInterface.OpticalLogicalInterfaces()
        self.optical_logical_interfaces.parent = self


    class OpticalClientInterfaces(object):
        """
        The operational attributes table for Client Port
        
        .. attribute:: optical_client_interface
        
        	The operational attributes for Client Port
        	**type**\: list of    :py:class:`OpticalClientInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_oper.OpticalInterface.OpticalClientInterfaces.OpticalClientInterface>`
        
        

        """

        _prefix = 'openconfig-terminal-device-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.optical_client_interface = YList()
            self.optical_client_interface.parent = self
            self.optical_client_interface.name = 'optical_client_interface'


        class OpticalClientInterface(object):
            """
            The operational attributes for Client Port
            
            .. attribute:: name  <key>
            
            	The name of the client interface
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: optical_client_logical_channel_assignments
            
            	The operational attributes for a Underline Ether Interface
            	**type**\:   :py:class:`OpticalClientLogicalChannelAssignments <ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_oper.OpticalInterface.OpticalClientInterfaces.OpticalClientInterface.OpticalClientLogicalChannelAssignments>`
            
            

            """

            _prefix = 'openconfig-terminal-device-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.name = None
                self.optical_client_logical_channel_assignments = OpticalInterface.OpticalClientInterfaces.OpticalClientInterface.OpticalClientLogicalChannelAssignments()
                self.optical_client_logical_channel_assignments.parent = self


            class OpticalClientLogicalChannelAssignments(object):
                """
                The operational attributes for a Underline
                Ether Interface
                
                .. attribute:: optical_client_logical_channel_assignment
                
                	The operational attributes for a Underline Ether Interface
                	**type**\: list of    :py:class:`OpticalClientLogicalChannelAssignment <ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_oper.OpticalInterface.OpticalClientInterfaces.OpticalClientInterface.OpticalClientLogicalChannelAssignments.OpticalClientLogicalChannelAssignment>`
                
                

                """

                _prefix = 'openconfig-terminal-device-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.optical_client_logical_channel_assignment = YList()
                    self.optical_client_logical_channel_assignment.parent = self
                    self.optical_client_logical_channel_assignment.name = 'optical_client_logical_channel_assignment'


                class OpticalClientLogicalChannelAssignment(object):
                    """
                    The operational attributes for a Underline
                    Ether Interface
                    
                    .. attribute:: index  <key>
                    
                    	The index of the interface
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: allocation
                    
                    	Allocation
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: is_logical_link
                    
                    	IsLogicalLink
                    	**type**\:  bool
                    
                    .. attribute:: logical_channel
                    
                    	LogicalChannel
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: optical_channel
                    
                    	OpticalChannel
                    	**type**\:  str
                    
                    	**length:** 0..128
                    
                    

                    """

                    _prefix = 'openconfig-terminal-device-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.index = None
                        self.allocation = None
                        self.is_logical_link = None
                        self.logical_channel = None
                        self.optical_channel = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.index is None:
                            raise YPYModelError('Key property index is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-openconfig-terminal-device-oper:optical-client-logical-channel-assignment[Cisco-IOS-XR-openconfig-terminal-device-oper:index = ' + str(self.index) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.index is not None:
                            return True

                        if self.allocation is not None:
                            return True

                        if self.is_logical_link is not None:
                            return True

                        if self.logical_channel is not None:
                            return True

                        if self.optical_channel is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_openconfig_terminal_device_oper as meta
                        return meta._meta_table['OpticalInterface.OpticalClientInterfaces.OpticalClientInterface.OpticalClientLogicalChannelAssignments.OpticalClientLogicalChannelAssignment']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-openconfig-terminal-device-oper:optical-client-logical-channel-assignments'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.optical_client_logical_channel_assignment is not None:
                        for child_ref in self.optical_client_logical_channel_assignment:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_openconfig_terminal_device_oper as meta
                    return meta._meta_table['OpticalInterface.OpticalClientInterfaces.OpticalClientInterface.OpticalClientLogicalChannelAssignments']['meta_info']

            @property
            def _common_path(self):
                if self.name is None:
                    raise YPYModelError('Key property name is None')

                return '/Cisco-IOS-XR-openconfig-terminal-device-oper:optical-interface/Cisco-IOS-XR-openconfig-terminal-device-oper:optical-client-interfaces/Cisco-IOS-XR-openconfig-terminal-device-oper:optical-client-interface[Cisco-IOS-XR-openconfig-terminal-device-oper:name = ' + str(self.name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.name is not None:
                    return True

                if self.optical_client_logical_channel_assignments is not None and self.optical_client_logical_channel_assignments._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_openconfig_terminal_device_oper as meta
                return meta._meta_table['OpticalInterface.OpticalClientInterfaces.OpticalClientInterface']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-openconfig-terminal-device-oper:optical-interface/Cisco-IOS-XR-openconfig-terminal-device-oper:optical-client-interfaces'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.optical_client_interface is not None:
                for child_ref in self.optical_client_interface:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_openconfig_terminal_device_oper as meta
            return meta._meta_table['OpticalInterface.OpticalClientInterfaces']['meta_info']


    class OperationalModes(object):
        """
        The Operational Mode Table
        
        .. attribute:: operational_mode
        
        	Mode supported on Device
        	**type**\: list of    :py:class:`OperationalMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_oper.OpticalInterface.OperationalModes.OperationalMode>`
        
        

        """

        _prefix = 'openconfig-terminal-device-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.operational_mode = YList()
            self.operational_mode.parent = self
            self.operational_mode.name = 'operational_mode'


        class OperationalMode(object):
            """
            Mode supported on Device
            
            .. attribute:: mode_id  <key>
            
            	Mode\-id for supported mode on Device
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: operational_mode_attributes
            
            	The operational attributes for mxp driver fec\-mode
            	**type**\:   :py:class:`OperationalModeAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_oper.OpticalInterface.OperationalModes.OperationalMode.OperationalModeAttributes>`
            
            

            """

            _prefix = 'openconfig-terminal-device-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.mode_id = None
                self.operational_mode_attributes = OpticalInterface.OperationalModes.OperationalMode.OperationalModeAttributes()
                self.operational_mode_attributes.parent = self


            class OperationalModeAttributes(object):
                """
                The operational attributes for mxp driver
                fec\-mode
                
                .. attribute:: description
                
                	Description
                	**type**\:  str
                
                	**length:** 0..128
                
                .. attribute:: vendor_id
                
                	VendorId
                	**type**\:  str
                
                	**length:** 0..64
                
                

                """

                _prefix = 'openconfig-terminal-device-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.description = None
                    self.vendor_id = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-openconfig-terminal-device-oper:operational-mode-attributes'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.description is not None:
                        return True

                    if self.vendor_id is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_openconfig_terminal_device_oper as meta
                    return meta._meta_table['OpticalInterface.OperationalModes.OperationalMode.OperationalModeAttributes']['meta_info']

            @property
            def _common_path(self):
                if self.mode_id is None:
                    raise YPYModelError('Key property mode_id is None')

                return '/Cisco-IOS-XR-openconfig-terminal-device-oper:optical-interface/Cisco-IOS-XR-openconfig-terminal-device-oper:operational-modes/Cisco-IOS-XR-openconfig-terminal-device-oper:operational-mode[Cisco-IOS-XR-openconfig-terminal-device-oper:mode-id = ' + str(self.mode_id) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.mode_id is not None:
                    return True

                if self.operational_mode_attributes is not None and self.operational_mode_attributes._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_openconfig_terminal_device_oper as meta
                return meta._meta_table['OpticalInterface.OperationalModes.OperationalMode']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-openconfig-terminal-device-oper:optical-interface/Cisco-IOS-XR-openconfig-terminal-device-oper:operational-modes'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.operational_mode is not None:
                for child_ref in self.operational_mode:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_openconfig_terminal_device_oper as meta
            return meta._meta_table['OpticalInterface.OperationalModes']['meta_info']


    class OpticalLogicalInterfaces(object):
        """
        The operational attributes for a particular
        interface
        
        .. attribute:: optical_logical_interface
        
        	The operational attributes for a particular interface
        	**type**\: list of    :py:class:`OpticalLogicalInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_oper.OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface>`
        
        

        """

        _prefix = 'openconfig-terminal-device-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.optical_logical_interface = YList()
            self.optical_logical_interface.parent = self
            self.optical_logical_interface.name = 'optical_logical_interface'


        class OpticalLogicalInterface(object):
            """
            The operational attributes for a particular
            interface
            
            .. attribute:: index  <key>
            
            	The index of the logical\-channel
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: optical_logical_interface_attr
            
            	The operational attributes for a particular interface
            	**type**\:   :py:class:`OpticalLogicalInterfaceAttr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_oper.OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceAttr>`
            
            .. attribute:: optical_logical_interface_logical_channel_assignments
            
            	The operational attributes for a particular interface
            	**type**\:   :py:class:`OpticalLogicalInterfaceLogicalChannelAssignments <ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_oper.OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments>`
            
            

            """

            _prefix = 'openconfig-terminal-device-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.index = None
                self.optical_logical_interface_attr = OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceAttr()
                self.optical_logical_interface_attr.parent = self
                self.optical_logical_interface_logical_channel_assignments = OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments()
                self.optical_logical_interface_logical_channel_assignments.parent = self


            class OpticalLogicalInterfaceAttr(object):
                """
                The operational attributes for a particular
                interface
                
                .. attribute:: protocol_type
                
                	ProtocolType
                	**type**\:   :py:class:`LogicalProtocolEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_oper.LogicalProtocolEnum>`
                
                .. attribute:: trib_protocol
                
                	TribProtocol
                	**type**\:   :py:class:`TribProtocolEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_oper.TribProtocolEnum>`
                
                .. attribute:: trib_rate_class
                
                	TribRateClass
                	**type**\:   :py:class:`TribRateClassEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_oper.TribRateClassEnum>`
                
                

                """

                _prefix = 'openconfig-terminal-device-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.protocol_type = None
                    self.trib_protocol = None
                    self.trib_rate_class = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-openconfig-terminal-device-oper:optical-logical-interface-attr'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.protocol_type is not None:
                        return True

                    if self.trib_protocol is not None:
                        return True

                    if self.trib_rate_class is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_openconfig_terminal_device_oper as meta
                    return meta._meta_table['OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceAttr']['meta_info']


            class OpticalLogicalInterfaceLogicalChannelAssignments(object):
                """
                The operational attributes for a particular
                interface
                
                .. attribute:: optical_logical_interface_logical_channel_assignment
                
                	The operational attributes for a particular interface
                	**type**\: list of    :py:class:`OpticalLogicalInterfaceLogicalChannelAssignment <ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_oper.OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments.OpticalLogicalInterfaceLogicalChannelAssignment>`
                
                

                """

                _prefix = 'openconfig-terminal-device-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.optical_logical_interface_logical_channel_assignment = YList()
                    self.optical_logical_interface_logical_channel_assignment.parent = self
                    self.optical_logical_interface_logical_channel_assignment.name = 'optical_logical_interface_logical_channel_assignment'


                class OpticalLogicalInterfaceLogicalChannelAssignment(object):
                    """
                    The operational attributes for a particular
                    interface
                    
                    .. attribute:: index  <key>
                    
                    	The index of the interface
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: allocation
                    
                    	Allocation
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: is_logical_link
                    
                    	IsLogicalLink
                    	**type**\:  bool
                    
                    .. attribute:: logical_channel
                    
                    	LogicalChannel
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: optical_channel
                    
                    	OpticalChannel
                    	**type**\:  str
                    
                    	**length:** 0..128
                    
                    

                    """

                    _prefix = 'openconfig-terminal-device-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.index = None
                        self.allocation = None
                        self.is_logical_link = None
                        self.logical_channel = None
                        self.optical_channel = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.index is None:
                            raise YPYModelError('Key property index is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-openconfig-terminal-device-oper:optical-logical-interface-logical-channel-assignment[Cisco-IOS-XR-openconfig-terminal-device-oper:index = ' + str(self.index) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.index is not None:
                            return True

                        if self.allocation is not None:
                            return True

                        if self.is_logical_link is not None:
                            return True

                        if self.logical_channel is not None:
                            return True

                        if self.optical_channel is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_openconfig_terminal_device_oper as meta
                        return meta._meta_table['OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments.OpticalLogicalInterfaceLogicalChannelAssignment']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-openconfig-terminal-device-oper:optical-logical-interface-logical-channel-assignments'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.optical_logical_interface_logical_channel_assignment is not None:
                        for child_ref in self.optical_logical_interface_logical_channel_assignment:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_openconfig_terminal_device_oper as meta
                    return meta._meta_table['OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments']['meta_info']

            @property
            def _common_path(self):
                if self.index is None:
                    raise YPYModelError('Key property index is None')

                return '/Cisco-IOS-XR-openconfig-terminal-device-oper:optical-interface/Cisco-IOS-XR-openconfig-terminal-device-oper:optical-logical-interfaces/Cisco-IOS-XR-openconfig-terminal-device-oper:optical-logical-interface[Cisco-IOS-XR-openconfig-terminal-device-oper:index = ' + str(self.index) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.index is not None:
                    return True

                if self.optical_logical_interface_attr is not None and self.optical_logical_interface_attr._has_data():
                    return True

                if self.optical_logical_interface_logical_channel_assignments is not None and self.optical_logical_interface_logical_channel_assignments._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_openconfig_terminal_device_oper as meta
                return meta._meta_table['OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-openconfig-terminal-device-oper:optical-interface/Cisco-IOS-XR-openconfig-terminal-device-oper:optical-logical-interfaces'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.optical_logical_interface is not None:
                for child_ref in self.optical_logical_interface:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_openconfig_terminal_device_oper as meta
            return meta._meta_table['OpticalInterface.OpticalLogicalInterfaces']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-openconfig-terminal-device-oper:optical-interface'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.operational_modes is not None and self.operational_modes._has_data():
            return True

        if self.optical_client_interfaces is not None and self.optical_client_interfaces._has_data():
            return True

        if self.optical_logical_interfaces is not None and self.optical_logical_interfaces._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_openconfig_terminal_device_oper as meta
        return meta._meta_table['OpticalInterface']['meta_info']


