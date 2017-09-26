""" Cisco_IOS_XR_icpe_infra_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR icpe\-infra package configuration.

This module contains definitions
for the following management objects\:
  nv\-satellite\-global\: nV Satellite Global configuration
  nv\-satellites\: nv satellites

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg,
  Cisco\-IOS\-XR\-rgmgr\-cfg,
modules with configuration data.

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class NvSatelliteGlobal(Entity):
    """
    nV Satellite Global configuration
    
    .. attribute:: chassis_mac
    
    	Chassis MAC address
    	**type**\:   :py:class:`ChassisMac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_cfg.NvSatelliteGlobal.ChassisMac>`
    
    

    """

    _prefix = 'icpe-infra-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(NvSatelliteGlobal, self).__init__()
        self._top_entity = None

        self.yang_name = "nv-satellite-global"
        self.yang_parent_name = "Cisco-IOS-XR-icpe-infra-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"chassis-mac" : ("chassis_mac", NvSatelliteGlobal.ChassisMac)}
        self._child_list_classes = {}

        self.chassis_mac = NvSatelliteGlobal.ChassisMac()
        self.chassis_mac.parent = self
        self._children_name_map["chassis_mac"] = "chassis-mac"
        self._children_yang_names.add("chassis-mac")
        self._segment_path = lambda: "Cisco-IOS-XR-icpe-infra-cfg:nv-satellite-global"


    class ChassisMac(Entity):
        """
        Chassis MAC address
        
        .. attribute:: mac1
        
        	First two bytes of MAC address
        	**type**\:  int
        
        	**range:** 0..2147483647
        
        	**units**\: byte
        
        .. attribute:: mac2
        
        	Second two bytes of MAC address
        	**type**\:  int
        
        	**range:** 0..2147483647
        
        	**units**\: byte
        
        .. attribute:: mac3
        
        	Third two bytes of MAC address
        	**type**\:  int
        
        	**range:** 0..2147483647
        
        	**units**\: byte
        
        

        """

        _prefix = 'icpe-infra-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(NvSatelliteGlobal.ChassisMac, self).__init__()

            self.yang_name = "chassis-mac"
            self.yang_parent_name = "nv-satellite-global"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.mac1 = YLeaf(YType.uint32, "mac1")

            self.mac2 = YLeaf(YType.uint32, "mac2")

            self.mac3 = YLeaf(YType.uint32, "mac3")
            self._segment_path = lambda: "chassis-mac"
            self._absolute_path = lambda: "Cisco-IOS-XR-icpe-infra-cfg:nv-satellite-global/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(NvSatelliteGlobal.ChassisMac, ['mac1', 'mac2', 'mac3'], name, value)

    def clone_ptr(self):
        self._top_entity = NvSatelliteGlobal()
        return self._top_entity

class NvSatellites(Entity):
    """
    nv satellites
    
    .. attribute:: nv_satellite
    
    	Satellite Configuration
    	**type**\: list of    :py:class:`NvSatellite <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_cfg.NvSatellites.NvSatellite>`
    
    

    """

    _prefix = 'icpe-infra-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(NvSatellites, self).__init__()
        self._top_entity = None

        self.yang_name = "nv-satellites"
        self.yang_parent_name = "Cisco-IOS-XR-icpe-infra-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {}
        self._child_list_classes = {"nv-satellite" : ("nv_satellite", NvSatellites.NvSatellite)}

        self.nv_satellite = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-icpe-infra-cfg:nv-satellites"

    def __setattr__(self, name, value):
        self._perform_setattr(NvSatellites, [], name, value)


    class NvSatellite(Entity):
        """
        Satellite Configuration
        
        .. attribute:: satellite_id  <key>
        
        	Satellite ID
        	**type**\:  int
        
        	**range:** 100..65534
        
        .. attribute:: candidate_fabric_ports
        
        	Enable interfaces on the satellite to be used as fabric ports table
        	**type**\:   :py:class:`CandidateFabricPorts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_cfg.NvSatellites.NvSatellite.CandidateFabricPorts>`
        
        .. attribute:: connection_info
        
        	Satellite User
        	**type**\:   :py:class:`ConnectionInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_cfg.NvSatellites.NvSatellite.ConnectionInfo>`
        
        .. attribute:: delayed_switchback
        
        	Timer (in seconds) for delaying switchback in a dual home setup
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: second
        
        .. attribute:: description
        
        	Satellite Description
        	**type**\:  str
        
        .. attribute:: device_name
        
        	Satellite Name
        	**type**\:  str
        
        .. attribute:: disc_timeout
        
        	Discovery timeout for the satellite
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: enable
        
        	Enable
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: ip_address
        
        	Satellite IP Address
        	**type**\: one of the below types:
        
        	**type**\:  str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        
        ----
        	**type**\:  str
        
        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
        
        
        ----
        .. attribute:: redundancy
        
        	Redundancy submode
        	**type**\:   :py:class:`Redundancy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_cfg.NvSatellites.NvSatellite.Redundancy>`
        
        .. attribute:: secret
        
        	Encrypted password for the Satellite
        	**type**\:  str
        
        	**pattern:** (!.+)\|([^!].+)
        
        .. attribute:: serial_number
        
        	Satellite Serial Number
        	**type**\:  str
        
        .. attribute:: timeout_warning
        
        	Discovery timeout warning for the satellite
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: type
        
        	Satellite Type
        	**type**\:  str
        
        .. attribute:: upgrade_on_connect
        
        	Satellite auto\-upgrade capability
        	**type**\:   :py:class:`UpgradeOnConnect <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_cfg.NvSatellites.NvSatellite.UpgradeOnConnect>`
        
        .. attribute:: vrf
        
        	VRF for Satellite IP Address
        	**type**\:  str
        
        

        """

        _prefix = 'icpe-infra-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(NvSatellites.NvSatellite, self).__init__()

            self.yang_name = "nv-satellite"
            self.yang_parent_name = "nv-satellites"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"candidate-fabric-ports" : ("candidate_fabric_ports", NvSatellites.NvSatellite.CandidateFabricPorts), "connection-info" : ("connection_info", NvSatellites.NvSatellite.ConnectionInfo), "redundancy" : ("redundancy", NvSatellites.NvSatellite.Redundancy), "upgrade-on-connect" : ("upgrade_on_connect", NvSatellites.NvSatellite.UpgradeOnConnect)}
            self._child_list_classes = {}

            self.satellite_id = YLeaf(YType.uint32, "satellite-id")

            self.delayed_switchback = YLeaf(YType.uint32, "delayed-switchback")

            self.description = YLeaf(YType.str, "description")

            self.device_name = YLeaf(YType.str, "device-name")

            self.disc_timeout = YLeaf(YType.uint32, "disc-timeout")

            self.enable = YLeaf(YType.empty, "enable")

            self.ip_address = YLeaf(YType.str, "ip-address")

            self.secret = YLeaf(YType.str, "secret")

            self.serial_number = YLeaf(YType.str, "serial-number")

            self.timeout_warning = YLeaf(YType.uint32, "timeout-warning")

            self.type = YLeaf(YType.str, "type")

            self.vrf = YLeaf(YType.str, "vrf")

            self.candidate_fabric_ports = NvSatellites.NvSatellite.CandidateFabricPorts()
            self.candidate_fabric_ports.parent = self
            self._children_name_map["candidate_fabric_ports"] = "candidate-fabric-ports"
            self._children_yang_names.add("candidate-fabric-ports")

            self.connection_info = NvSatellites.NvSatellite.ConnectionInfo()
            self.connection_info.parent = self
            self._children_name_map["connection_info"] = "connection-info"
            self._children_yang_names.add("connection-info")

            self.redundancy = NvSatellites.NvSatellite.Redundancy()
            self.redundancy.parent = self
            self._children_name_map["redundancy"] = "redundancy"
            self._children_yang_names.add("redundancy")

            self.upgrade_on_connect = NvSatellites.NvSatellite.UpgradeOnConnect()
            self.upgrade_on_connect.parent = self
            self._children_name_map["upgrade_on_connect"] = "upgrade-on-connect"
            self._children_yang_names.add("upgrade-on-connect")
            self._segment_path = lambda: "nv-satellite" + "[satellite-id='" + self.satellite_id.get() + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-icpe-infra-cfg:nv-satellites/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(NvSatellites.NvSatellite, ['satellite_id', 'delayed_switchback', 'description', 'device_name', 'disc_timeout', 'enable', 'ip_address', 'secret', 'serial_number', 'timeout_warning', 'type', 'vrf'], name, value)


        class CandidateFabricPorts(Entity):
            """
            Enable interfaces on the satellite to be used
            as fabric ports table
            
            .. attribute:: candidate_fabric_port
            
            	Enable interfaces on the satellite to be used as fabric ports
            	**type**\: list of    :py:class:`CandidateFabricPort <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_cfg.NvSatellites.NvSatellite.CandidateFabricPorts.CandidateFabricPort>`
            
            

            """

            _prefix = 'icpe-infra-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(NvSatellites.NvSatellite.CandidateFabricPorts, self).__init__()

                self.yang_name = "candidate-fabric-ports"
                self.yang_parent_name = "nv-satellite"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self._child_container_classes = {}
                self._child_list_classes = {"candidate-fabric-port" : ("candidate_fabric_port", NvSatellites.NvSatellite.CandidateFabricPorts.CandidateFabricPort)}

                self.candidate_fabric_port = YList(self)
                self._segment_path = lambda: "candidate-fabric-ports"

            def __setattr__(self, name, value):
                self._perform_setattr(NvSatellites.NvSatellite.CandidateFabricPorts, [], name, value)


            class CandidateFabricPort(Entity):
                """
                Enable interfaces on the satellite to be used
                as fabric ports
                
                .. attribute:: port_type  <key>
                
                	Port type
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: slot  <key>
                
                	Slot
                	**type**\:  int
                
                	**range:** 0..8
                
                .. attribute:: sub_slot  <key>
                
                	Sub slot
                	**type**\:  int
                
                	**range:** 0..8
                
                .. attribute:: port_range
                
                	Port range
                	**type**\:  str
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'icpe-infra-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(NvSatellites.NvSatellite.CandidateFabricPorts.CandidateFabricPort, self).__init__()

                    self.yang_name = "candidate-fabric-port"
                    self.yang_parent_name = "candidate-fabric-ports"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.port_type = YLeaf(YType.str, "port-type")

                    self.slot = YLeaf(YType.uint32, "slot")

                    self.sub_slot = YLeaf(YType.uint32, "sub-slot")

                    self.port_range = YLeaf(YType.str, "port-range")
                    self._segment_path = lambda: "candidate-fabric-port" + "[port-type='" + self.port_type.get() + "']" + "[slot='" + self.slot.get() + "']" + "[sub-slot='" + self.sub_slot.get() + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(NvSatellites.NvSatellite.CandidateFabricPorts.CandidateFabricPort, ['port_type', 'slot', 'sub_slot', 'port_range'], name, value)


        class ConnectionInfo(Entity):
            """
            Satellite User
            
            .. attribute:: password
            
            	Encrypted password for the user
            	**type**\:  str
            
            	**pattern:** (!.+)\|([^!].+)
            
            .. attribute:: username
            
            	Satellite Username
            	**type**\:  str
            
            

            """

            _prefix = 'icpe-infra-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(NvSatellites.NvSatellite.ConnectionInfo, self).__init__()

                self.yang_name = "connection-info"
                self.yang_parent_name = "nv-satellite"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.password = YLeaf(YType.str, "password")

                self.username = YLeaf(YType.str, "username")
                self._segment_path = lambda: "connection-info"

            def __setattr__(self, name, value):
                self._perform_setattr(NvSatellites.NvSatellite.ConnectionInfo, ['password', 'username'], name, value)


        class Redundancy(Entity):
            """
            Redundancy submode
            
            .. attribute:: host_priority
            
            	Priority for this host for the given satellite
            	**type**\:  int
            
            	**range:** 0..255
            
            

            """

            _prefix = 'icpe-infra-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(NvSatellites.NvSatellite.Redundancy, self).__init__()

                self.yang_name = "redundancy"
                self.yang_parent_name = "nv-satellite"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.host_priority = YLeaf(YType.uint32, "host-priority")
                self._segment_path = lambda: "redundancy"

            def __setattr__(self, name, value):
                self._perform_setattr(NvSatellites.NvSatellite.Redundancy, ['host_priority'], name, value)


        class UpgradeOnConnect(Entity):
            """
            Satellite auto\-upgrade capability
            
            .. attribute:: connect_type
            
            	When to upgrade the satellite
            	**type**\:   :py:class:`ConnectType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_cfg.NvSatellites.NvSatellite.UpgradeOnConnect.ConnectType>`
            
            .. attribute:: reference
            
            	Reference name
            	**type**\:  str
            
            

            """

            _prefix = 'icpe-infra-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(NvSatellites.NvSatellite.UpgradeOnConnect, self).__init__()

                self.yang_name = "upgrade-on-connect"
                self.yang_parent_name = "nv-satellite"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.connect_type = YLeaf(YType.enumeration, "connect-type")

                self.reference = YLeaf(YType.str, "reference")
                self._segment_path = lambda: "upgrade-on-connect"

            def __setattr__(self, name, value):
                self._perform_setattr(NvSatellites.NvSatellite.UpgradeOnConnect, ['connect_type', 'reference'], name, value)

            class ConnectType(Enum):
                """
                ConnectType

                When to upgrade the satellite

                .. data:: on_connection = 1

                	Satellite Upgrade on Connection

                .. data:: on_first_connection = 2

                	Satellite Upgrade on First Connection after

                	configuration or host boot

                """

                on_connection = Enum.YLeaf(1, "on-connection")

                on_first_connection = Enum.YLeaf(2, "on-first-connection")


    def clone_ptr(self):
        self._top_entity = NvSatellites()
        return self._top_entity

