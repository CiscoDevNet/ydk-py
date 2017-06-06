""" Cisco_IOS_XR_terminal_device_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR terminal\-device package operational data.

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
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_terminal_device_oper as meta
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
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_terminal_device_oper as meta
        return meta._meta_table['TribProtocolEnum']


class TribRateClassEnum(Enum):
    """
    TribRateClassEnum

    Trib rate class

    .. data:: trib_rate_unknown = 0

    	Unknown tributary signal rate

    .. data:: trib_rate1g = 1

    	1G tributary signal rate

    .. data:: trib_rate25g = 2

    	2.5G tributary signal rate

    .. data:: trib_rate10g = 3

    	10G tributary signal rate

    .. data:: trib_rate40g = 4

    	40G tributary signal rate

    .. data:: trib_rate100g = 5

    	100G tributary signal rate

    """

    trib_rate_unknown = 0

    trib_rate1g = 1

    trib_rate25g = 2

    trib_rate10g = 3

    trib_rate40g = 4

    trib_rate100g = 5


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_terminal_device_oper as meta
        return meta._meta_table['TribRateClassEnum']



class OpticalInterface(object):
    """
    System\-wide view of interface operational data
    
    .. attribute:: config_status
    
    	Table containing status information
    	**type**\:   :py:class:`ConfigStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper.OpticalInterface.ConfigStatus>`
    
    .. attribute:: graph
    
    	Table containing Graph Structure and related info
    	**type**\:   :py:class:`Graph <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper.OpticalInterface.Graph>`
    
    .. attribute:: operational_modes
    
    	The Operational Mode Table
    	**type**\:   :py:class:`OperationalModes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper.OpticalInterface.OperationalModes>`
    
    .. attribute:: optical_channel_interfaces
    
    	The operational attributes for a particular optical channel
    	**type**\:   :py:class:`OpticalChannelInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper.OpticalInterface.OpticalChannelInterfaces>`
    
    .. attribute:: optical_logical_interfaces
    
    	The operational attributes for a logical channel
    	**type**\:   :py:class:`OpticalLogicalInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper.OpticalInterface.OpticalLogicalInterfaces>`
    
    

    """

    _prefix = 'terminal-device-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.config_status = OpticalInterface.ConfigStatus()
        self.config_status.parent = self
        self.graph = OpticalInterface.Graph()
        self.graph.parent = self
        self.operational_modes = OpticalInterface.OperationalModes()
        self.operational_modes.parent = self
        self.optical_channel_interfaces = OpticalInterface.OpticalChannelInterfaces()
        self.optical_channel_interfaces.parent = self
        self.optical_logical_interfaces = OpticalInterface.OpticalLogicalInterfaces()
        self.optical_logical_interfaces.parent = self


    class ConfigStatus(object):
        """
        Table containing status information
        
        .. attribute:: partial_config
        
        	The bag containing partial config status
        	**type**\:   :py:class:`PartialConfig <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper.OpticalInterface.ConfigStatus.PartialConfig>`
        
        .. attribute:: slice_tables
        
        	The container containing slice status information
        	**type**\:   :py:class:`SliceTables <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper.OpticalInterface.ConfigStatus.SliceTables>`
        
        

        """

        _prefix = 'terminal-device-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.partial_config = OpticalInterface.ConfigStatus.PartialConfig()
            self.partial_config.parent = self
            self.slice_tables = OpticalInterface.ConfigStatus.SliceTables()
            self.slice_tables.parent = self


        class PartialConfig(object):
            """
            The bag containing partial config status
            
            .. attribute:: partial_config
            
            	PartialConfig
            	**type**\:  int
            
            	**range:** 0..255
            
            

            """

            _prefix = 'terminal-device-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.partial_config = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-terminal-device-oper:optical-interface/Cisco-IOS-XR-terminal-device-oper:config-status/Cisco-IOS-XR-terminal-device-oper:partial-config'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.partial_config is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_terminal_device_oper as meta
                return meta._meta_table['OpticalInterface.ConfigStatus.PartialConfig']['meta_info']


        class SliceTables(object):
            """
            The container containing slice status
            information
            
            .. attribute:: slice_table
            
            	The table contains list of slices present
            	**type**\: list of    :py:class:`SliceTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper.OpticalInterface.ConfigStatus.SliceTables.SliceTable>`
            
            

            """

            _prefix = 'terminal-device-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.slice_table = YList()
                self.slice_table.parent = self
                self.slice_table.name = 'slice_table'


            class SliceTable(object):
                """
                The table contains list of slices present
                
                .. attribute:: index  <key>
                
                	The index of slice
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: slice_status_attr
                
                	The bag containing slice config status
                	**type**\:   :py:class:`SliceStatusAttr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper.OpticalInterface.ConfigStatus.SliceTables.SliceTable.SliceStatusAttr>`
                
                

                """

                _prefix = 'terminal-device-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.index = None
                    self.slice_status_attr = OpticalInterface.ConfigStatus.SliceTables.SliceTable.SliceStatusAttr()
                    self.slice_status_attr.parent = self


                class SliceStatusAttr(object):
                    """
                    The bag containing slice config status
                    
                    .. attribute:: err_str
                    
                    	ErrStr
                    	**type**\:  str
                    
                    	**length:** 0..1024
                    
                    .. attribute:: err_timestamp
                    
                    	ErrTimestamp
                    	**type**\:  str
                    
                    	**length:** 0..32
                    
                    .. attribute:: past_config
                    
                    	PastConfig
                    	**type**\:  str
                    
                    	**length:** 0..32
                    
                    .. attribute:: past_timestamp
                    
                    	PastTimestamp
                    	**type**\:  str
                    
                    	**length:** 0..32
                    
                    .. attribute:: present_config
                    
                    	PresentConfig
                    	**type**\:  str
                    
                    	**length:** 0..32
                    
                    .. attribute:: present_timestamp
                    
                    	PresentTimestamp
                    	**type**\:  str
                    
                    	**length:** 0..32
                    
                    .. attribute:: prov_status
                    
                    	ProvStatus
                    	**type**\:  str
                    
                    	**length:** 0..32
                    
                    .. attribute:: slice
                    
                    	Slice
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'terminal-device-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.err_str = None
                        self.err_timestamp = None
                        self.past_config = None
                        self.past_timestamp = None
                        self.present_config = None
                        self.present_timestamp = None
                        self.prov_status = None
                        self.slice = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-terminal-device-oper:slice-status-attr'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.err_str is not None:
                            return True

                        if self.err_timestamp is not None:
                            return True

                        if self.past_config is not None:
                            return True

                        if self.past_timestamp is not None:
                            return True

                        if self.present_config is not None:
                            return True

                        if self.present_timestamp is not None:
                            return True

                        if self.prov_status is not None:
                            return True

                        if self.slice is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_terminal_device_oper as meta
                        return meta._meta_table['OpticalInterface.ConfigStatus.SliceTables.SliceTable.SliceStatusAttr']['meta_info']

                @property
                def _common_path(self):
                    if self.index is None:
                        raise YPYModelError('Key property index is None')

                    return '/Cisco-IOS-XR-terminal-device-oper:optical-interface/Cisco-IOS-XR-terminal-device-oper:config-status/Cisco-IOS-XR-terminal-device-oper:slice-tables/Cisco-IOS-XR-terminal-device-oper:slice-table[Cisco-IOS-XR-terminal-device-oper:index = ' + str(self.index) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.index is not None:
                        return True

                    if self.slice_status_attr is not None and self.slice_status_attr._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_terminal_device_oper as meta
                    return meta._meta_table['OpticalInterface.ConfigStatus.SliceTables.SliceTable']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-terminal-device-oper:optical-interface/Cisco-IOS-XR-terminal-device-oper:config-status/Cisco-IOS-XR-terminal-device-oper:slice-tables'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.slice_table is not None:
                    for child_ref in self.slice_table:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_terminal_device_oper as meta
                return meta._meta_table['OpticalInterface.ConfigStatus.SliceTables']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-terminal-device-oper:optical-interface/Cisco-IOS-XR-terminal-device-oper:config-status'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.partial_config is not None and self.partial_config._has_data():
                return True

            if self.slice_tables is not None and self.slice_tables._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_terminal_device_oper as meta
            return meta._meta_table['OpticalInterface.ConfigStatus']['meta_info']


    class OpticalChannelInterfaces(object):
        """
        The operational attributes for a particular
        optical channel
        
        .. attribute:: optical_channel_interface
        
        	The operational attributes for an optical channel
        	**type**\: list of    :py:class:`OpticalChannelInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper.OpticalInterface.OpticalChannelInterfaces.OpticalChannelInterface>`
        
        

        """

        _prefix = 'terminal-device-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.optical_channel_interface = YList()
            self.optical_channel_interface.parent = self
            self.optical_channel_interface.name = 'optical_channel_interface'


        class OpticalChannelInterface(object):
            """
            The operational attributes for an optical
            channel
            
            .. attribute:: location  <key>
            
            	The name of the optical\-channel
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: optical_channel_interface_attr
            
            	The operational attributes for an optical channel
            	**type**\:   :py:class:`OpticalChannelInterfaceAttr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper.OpticalInterface.OpticalChannelInterfaces.OpticalChannelInterface.OpticalChannelInterfaceAttr>`
            
            

            """

            _prefix = 'terminal-device-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.location = None
                self.optical_channel_interface_attr = OpticalInterface.OpticalChannelInterfaces.OpticalChannelInterface.OpticalChannelInterfaceAttr()
                self.optical_channel_interface_attr.parent = self


            class OpticalChannelInterfaceAttr(object):
                """
                The operational attributes for an optical
                channel
                
                .. attribute:: frequency
                
                	Frequency
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: index
                
                	Index
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: line_port
                
                	LinePort
                	**type**\:  str
                
                	**length:** 0..128
                
                .. attribute:: name
                
                	Name
                	**type**\:  str
                
                	**length:** 0..128
                
                .. attribute:: oper_mode
                
                	OperMode
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: power
                
                	Power
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'terminal-device-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.frequency = None
                    self.index = None
                    self.line_port = None
                    self.name = None
                    self.oper_mode = None
                    self.power = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-terminal-device-oper:optical-channel-interface-attr'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.frequency is not None:
                        return True

                    if self.index is not None:
                        return True

                    if self.line_port is not None:
                        return True

                    if self.name is not None:
                        return True

                    if self.oper_mode is not None:
                        return True

                    if self.power is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_terminal_device_oper as meta
                    return meta._meta_table['OpticalInterface.OpticalChannelInterfaces.OpticalChannelInterface.OpticalChannelInterfaceAttr']['meta_info']

            @property
            def _common_path(self):
                if self.location is None:
                    raise YPYModelError('Key property location is None')

                return '/Cisco-IOS-XR-terminal-device-oper:optical-interface/Cisco-IOS-XR-terminal-device-oper:optical-channel-interfaces/Cisco-IOS-XR-terminal-device-oper:optical-channel-interface[Cisco-IOS-XR-terminal-device-oper:location = ' + str(self.location) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.location is not None:
                    return True

                if self.optical_channel_interface_attr is not None and self.optical_channel_interface_attr._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_terminal_device_oper as meta
                return meta._meta_table['OpticalInterface.OpticalChannelInterfaces.OpticalChannelInterface']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-terminal-device-oper:optical-interface/Cisco-IOS-XR-terminal-device-oper:optical-channel-interfaces'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.optical_channel_interface is not None:
                for child_ref in self.optical_channel_interface:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_terminal_device_oper as meta
            return meta._meta_table['OpticalInterface.OpticalChannelInterfaces']['meta_info']


    class Graph(object):
        """
        Table containing Graph Structure and related
        info
        
        .. attribute:: adj_list_path
        
        	The path containg file which has adjacency list stored
        	**type**\:   :py:class:`AdjListPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper.OpticalInterface.Graph.AdjListPath>`
        
        .. attribute:: graph_structure_path
        
        	The path containg file which has graph structure stored
        	**type**\:   :py:class:`GraphStructurePath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper.OpticalInterface.Graph.GraphStructurePath>`
        
        

        """

        _prefix = 'terminal-device-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.adj_list_path = OpticalInterface.Graph.AdjListPath()
            self.adj_list_path.parent = self
            self.graph_structure_path = OpticalInterface.Graph.GraphStructurePath()
            self.graph_structure_path.parent = self


        class AdjListPath(object):
            """
            The path containg file which has adjacency list
            stored
            
            .. attribute:: path
            
            	Path
            	**type**\:  str
            
            	**length:** 0..256
            
            

            """

            _prefix = 'terminal-device-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.path = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-terminal-device-oper:optical-interface/Cisco-IOS-XR-terminal-device-oper:graph/Cisco-IOS-XR-terminal-device-oper:adj-list-path'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.path is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_terminal_device_oper as meta
                return meta._meta_table['OpticalInterface.Graph.AdjListPath']['meta_info']


        class GraphStructurePath(object):
            """
            The path containg file which has graph
            structure stored
            
            .. attribute:: path
            
            	Path
            	**type**\:  str
            
            	**length:** 0..256
            
            

            """

            _prefix = 'terminal-device-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.path = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-terminal-device-oper:optical-interface/Cisco-IOS-XR-terminal-device-oper:graph/Cisco-IOS-XR-terminal-device-oper:graph-structure-path'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.path is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_terminal_device_oper as meta
                return meta._meta_table['OpticalInterface.Graph.GraphStructurePath']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-terminal-device-oper:optical-interface/Cisco-IOS-XR-terminal-device-oper:graph'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.adj_list_path is not None and self.adj_list_path._has_data():
                return True

            if self.graph_structure_path is not None and self.graph_structure_path._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_terminal_device_oper as meta
            return meta._meta_table['OpticalInterface.Graph']['meta_info']


    class OperationalModes(object):
        """
        The Operational Mode Table
        
        .. attribute:: operational_mode
        
        	Mode supported on Device
        	**type**\: list of    :py:class:`OperationalMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper.OpticalInterface.OperationalModes.OperationalMode>`
        
        

        """

        _prefix = 'terminal-device-oper'
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
            	**type**\:   :py:class:`OperationalModeAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper.OpticalInterface.OperationalModes.OperationalMode.OperationalModeAttributes>`
            
            

            """

            _prefix = 'terminal-device-oper'
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

                _prefix = 'terminal-device-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.description = None
                    self.vendor_id = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-terminal-device-oper:operational-mode-attributes'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.description is not None:
                        return True

                    if self.vendor_id is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_terminal_device_oper as meta
                    return meta._meta_table['OpticalInterface.OperationalModes.OperationalMode.OperationalModeAttributes']['meta_info']

            @property
            def _common_path(self):
                if self.mode_id is None:
                    raise YPYModelError('Key property mode_id is None')

                return '/Cisco-IOS-XR-terminal-device-oper:optical-interface/Cisco-IOS-XR-terminal-device-oper:operational-modes/Cisco-IOS-XR-terminal-device-oper:operational-mode[Cisco-IOS-XR-terminal-device-oper:mode-id = ' + str(self.mode_id) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.mode_id is not None:
                    return True

                if self.operational_mode_attributes is not None and self.operational_mode_attributes._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_terminal_device_oper as meta
                return meta._meta_table['OpticalInterface.OperationalModes.OperationalMode']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-terminal-device-oper:optical-interface/Cisco-IOS-XR-terminal-device-oper:operational-modes'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.operational_mode is not None:
                for child_ref in self.operational_mode:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_terminal_device_oper as meta
            return meta._meta_table['OpticalInterface.OperationalModes']['meta_info']


    class OpticalLogicalInterfaces(object):
        """
        The operational attributes for a logical channel
        
        .. attribute:: optical_logical_interface
        
        	The operational attributes for a logical channel
        	**type**\: list of    :py:class:`OpticalLogicalInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper.OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface>`
        
        

        """

        _prefix = 'terminal-device-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.optical_logical_interface = YList()
            self.optical_logical_interface.parent = self
            self.optical_logical_interface.name = 'optical_logical_interface'


        class OpticalLogicalInterface(object):
            """
            The operational attributes for a logical
            channel
            
            .. attribute:: index  <key>
            
            	The index of the logical\-channel
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: optical_logical_interface_attr
            
            	The operational attributes for a particular logical channel
            	**type**\:   :py:class:`OpticalLogicalInterfaceAttr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper.OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceAttr>`
            
            .. attribute:: optical_logical_interface_logical_channel_assignments
            
            	The operational attributes for a particular interface
            	**type**\:   :py:class:`OpticalLogicalInterfaceLogicalChannelAssignments <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper.OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments>`
            
            

            """

            _prefix = 'terminal-device-oper'
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
                logical channel
                
                .. attribute:: admin_state
                
                	AdminState
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: ingress_client_port
                
                	IngressClientPort
                	**type**\:  str
                
                	**length:** 0..128
                
                .. attribute:: ingress_physical_channel
                
                	IngressPhysicalChannel
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: logical_channel_ifname
                
                	LogicalChannelIfname
                	**type**\:  str
                
                	**length:** 0..128
                
                .. attribute:: logical_channel_index
                
                	LogicalChannelIndex
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: loopback_mode
                
                	LoopbackMode
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: protocol_type
                
                	ProtocolType
                	**type**\:   :py:class:`LogicalProtocolEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper.LogicalProtocolEnum>`
                
                .. attribute:: trib_protocol
                
                	TribProtocol
                	**type**\:   :py:class:`TribProtocolEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper.TribProtocolEnum>`
                
                .. attribute:: trib_rate_class
                
                	TribRateClass
                	**type**\:   :py:class:`TribRateClassEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper.TribRateClassEnum>`
                
                .. attribute:: tti_expected
                
                	TtiExpected
                	**type**\:  str
                
                	**length:** 0..256
                
                .. attribute:: tti_transmit
                
                	TtiTransmit
                	**type**\:  str
                
                	**length:** 0..256
                
                .. attribute:: type
                
                	Type
                	**type**\:  str
                
                	**length:** 0..32
                
                

                """

                _prefix = 'terminal-device-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.admin_state = None
                    self.ingress_client_port = None
                    self.ingress_physical_channel = None
                    self.logical_channel_ifname = None
                    self.logical_channel_index = None
                    self.loopback_mode = None
                    self.protocol_type = None
                    self.trib_protocol = None
                    self.trib_rate_class = None
                    self.tti_expected = None
                    self.tti_transmit = None
                    self.type = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-terminal-device-oper:optical-logical-interface-attr'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.admin_state is not None:
                        return True

                    if self.ingress_client_port is not None:
                        return True

                    if self.ingress_physical_channel is not None:
                        return True

                    if self.logical_channel_ifname is not None:
                        return True

                    if self.logical_channel_index is not None:
                        return True

                    if self.loopback_mode is not None:
                        return True

                    if self.protocol_type is not None:
                        return True

                    if self.trib_protocol is not None:
                        return True

                    if self.trib_rate_class is not None:
                        return True

                    if self.tti_expected is not None:
                        return True

                    if self.tti_transmit is not None:
                        return True

                    if self.type is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_terminal_device_oper as meta
                    return meta._meta_table['OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceAttr']['meta_info']


            class OpticalLogicalInterfaceLogicalChannelAssignments(object):
                """
                The operational attributes for a particular
                interface
                
                .. attribute:: optical_logical_interface_logical_channel_assignment
                
                	The operational attributes for a logical channel assignment
                	**type**\: list of    :py:class:`OpticalLogicalInterfaceLogicalChannelAssignment <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper.OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments.OpticalLogicalInterfaceLogicalChannelAssignment>`
                
                

                """

                _prefix = 'terminal-device-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.optical_logical_interface_logical_channel_assignment = YList()
                    self.optical_logical_interface_logical_channel_assignment.parent = self
                    self.optical_logical_interface_logical_channel_assignment.name = 'optical_logical_interface_logical_channel_assignment'


                class OpticalLogicalInterfaceLogicalChannelAssignment(object):
                    """
                    The operational attributes for a logical
                    channel assignment
                    
                    .. attribute:: index  <key>
                    
                    	The index of the logical\-channel
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: optical_logical_interface_logical_channel_assignment_attr
                    
                    	The operational attributes for a logical channel assignment
                    	**type**\:   :py:class:`OpticalLogicalInterfaceLogicalChannelAssignmentAttr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper.OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments.OpticalLogicalInterfaceLogicalChannelAssignment.OpticalLogicalInterfaceLogicalChannelAssignmentAttr>`
                    
                    

                    """

                    _prefix = 'terminal-device-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.index = None
                        self.optical_logical_interface_logical_channel_assignment_attr = OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments.OpticalLogicalInterfaceLogicalChannelAssignment.OpticalLogicalInterfaceLogicalChannelAssignmentAttr()
                        self.optical_logical_interface_logical_channel_assignment_attr.parent = self


                    class OpticalLogicalInterfaceLogicalChannelAssignmentAttr(object):
                        """
                        The operational attributes for a logical
                        channel assignment
                        
                        .. attribute:: allocation
                        
                        	Allocation
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: assignment_type
                        
                        	AssignmentType
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: index
                        
                        	Index
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_logical_link
                        
                        	IsLogicalLink
                        	**type**\:  bool
                        
                        .. attribute:: logical_channel
                        
                        	LogicalChannel
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: name
                        
                        	Name
                        	**type**\:  str
                        
                        	**length:** 0..128
                        
                        .. attribute:: optical_channel
                        
                        	OpticalChannel
                        	**type**\:  str
                        
                        	**length:** 0..128
                        
                        

                        """

                        _prefix = 'terminal-device-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.allocation = None
                            self.assignment_type = None
                            self.index = None
                            self.is_logical_link = None
                            self.logical_channel = None
                            self.name = None
                            self.optical_channel = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-terminal-device-oper:optical-logical-interface-logical-channel-assignment-attr'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.allocation is not None:
                                return True

                            if self.assignment_type is not None:
                                return True

                            if self.index is not None:
                                return True

                            if self.is_logical_link is not None:
                                return True

                            if self.logical_channel is not None:
                                return True

                            if self.name is not None:
                                return True

                            if self.optical_channel is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_terminal_device_oper as meta
                            return meta._meta_table['OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments.OpticalLogicalInterfaceLogicalChannelAssignment.OpticalLogicalInterfaceLogicalChannelAssignmentAttr']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.index is None:
                            raise YPYModelError('Key property index is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-terminal-device-oper:optical-logical-interface-logical-channel-assignment[Cisco-IOS-XR-terminal-device-oper:index = ' + str(self.index) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.index is not None:
                            return True

                        if self.optical_logical_interface_logical_channel_assignment_attr is not None and self.optical_logical_interface_logical_channel_assignment_attr._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_terminal_device_oper as meta
                        return meta._meta_table['OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments.OpticalLogicalInterfaceLogicalChannelAssignment']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-terminal-device-oper:optical-logical-interface-logical-channel-assignments'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.optical_logical_interface_logical_channel_assignment is not None:
                        for child_ref in self.optical_logical_interface_logical_channel_assignment:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_terminal_device_oper as meta
                    return meta._meta_table['OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments']['meta_info']

            @property
            def _common_path(self):
                if self.index is None:
                    raise YPYModelError('Key property index is None')

                return '/Cisco-IOS-XR-terminal-device-oper:optical-interface/Cisco-IOS-XR-terminal-device-oper:optical-logical-interfaces/Cisco-IOS-XR-terminal-device-oper:optical-logical-interface[Cisco-IOS-XR-terminal-device-oper:index = ' + str(self.index) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.index is not None:
                    return True

                if self.optical_logical_interface_attr is not None and self.optical_logical_interface_attr._has_data():
                    return True

                if self.optical_logical_interface_logical_channel_assignments is not None and self.optical_logical_interface_logical_channel_assignments._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_terminal_device_oper as meta
                return meta._meta_table['OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-terminal-device-oper:optical-interface/Cisco-IOS-XR-terminal-device-oper:optical-logical-interfaces'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.optical_logical_interface is not None:
                for child_ref in self.optical_logical_interface:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_terminal_device_oper as meta
            return meta._meta_table['OpticalInterface.OpticalLogicalInterfaces']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-terminal-device-oper:optical-interface'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.config_status is not None and self.config_status._has_data():
            return True

        if self.graph is not None and self.graph._has_data():
            return True

        if self.operational_modes is not None and self.operational_modes._has_data():
            return True

        if self.optical_channel_interfaces is not None and self.optical_channel_interfaces._has_data():
            return True

        if self.optical_logical_interfaces is not None and self.optical_logical_interfaces._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_terminal_device_oper as meta
        return meta._meta_table['OpticalInterface']['meta_info']


