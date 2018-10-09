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

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class NvSatelliteGlobal(Entity):
    """
    nV Satellite Global configuration
    
    .. attribute:: chassis_mac
    
    	Chassis MAC address
    	**type**\:  :py:class:`ChassisMac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_cfg.NvSatelliteGlobal.ChassisMac>`
    
    

    """

    _prefix = 'icpe-infra-cfg'
    _revision = '2017-09-30'

    def __init__(self):
        super(NvSatelliteGlobal, self).__init__()
        self._top_entity = None

        self.yang_name = "nv-satellite-global"
        self.yang_parent_name = "Cisco-IOS-XR-icpe-infra-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("chassis-mac", ("chassis_mac", NvSatelliteGlobal.ChassisMac))])
        self._leafs = OrderedDict()

        self.chassis_mac = NvSatelliteGlobal.ChassisMac()
        self.chassis_mac.parent = self
        self._children_name_map["chassis_mac"] = "chassis-mac"
        self._segment_path = lambda: "Cisco-IOS-XR-icpe-infra-cfg:nv-satellite-global"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(NvSatelliteGlobal, [], name, value)


    class ChassisMac(Entity):
        """
        Chassis MAC address
        
        .. attribute:: mac1
        
        	First two bytes of MAC address
        	**type**\: int
        
        	**range:** 0..2147483647
        
        	**units**\: byte
        
        .. attribute:: mac2
        
        	Second two bytes of MAC address
        	**type**\: int
        
        	**range:** 0..2147483647
        
        	**units**\: byte
        
        .. attribute:: mac3
        
        	Third two bytes of MAC address
        	**type**\: int
        
        	**range:** 0..2147483647
        
        	**units**\: byte
        
        

        """

        _prefix = 'icpe-infra-cfg'
        _revision = '2017-09-30'

        def __init__(self):
            super(NvSatelliteGlobal.ChassisMac, self).__init__()

            self.yang_name = "chassis-mac"
            self.yang_parent_name = "nv-satellite-global"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('mac1', (YLeaf(YType.uint32, 'mac1'), ['int'])),
                ('mac2', (YLeaf(YType.uint32, 'mac2'), ['int'])),
                ('mac3', (YLeaf(YType.uint32, 'mac3'), ['int'])),
            ])
            self.mac1 = None
            self.mac2 = None
            self.mac3 = None
            self._segment_path = lambda: "chassis-mac"
            self._absolute_path = lambda: "Cisco-IOS-XR-icpe-infra-cfg:nv-satellite-global/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(NvSatelliteGlobal.ChassisMac, [u'mac1', u'mac2', u'mac3'], name, value)

    def clone_ptr(self):
        self._top_entity = NvSatelliteGlobal()
        return self._top_entity

class NvSatellites(Entity):
    """
    nv satellites
    
    .. attribute:: nv_satellite
    
    	Satellite Configuration
    	**type**\: list of  		 :py:class:`NvSatellite <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_cfg.NvSatellites.NvSatellite>`
    
    

    """

    _prefix = 'icpe-infra-cfg'
    _revision = '2017-09-30'

    def __init__(self):
        super(NvSatellites, self).__init__()
        self._top_entity = None

        self.yang_name = "nv-satellites"
        self.yang_parent_name = "Cisco-IOS-XR-icpe-infra-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("nv-satellite", ("nv_satellite", NvSatellites.NvSatellite))])
        self._leafs = OrderedDict()

        self.nv_satellite = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-icpe-infra-cfg:nv-satellites"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(NvSatellites, [], name, value)


    class NvSatellite(Entity):
        """
        Satellite Configuration
        
        .. attribute:: satellite_id  (key)
        
        	Satellite ID
        	**type**\: int
        
        	**range:** 100..65534
        
        .. attribute:: upgrade_on_connect
        
        	Satellite auto\-upgrade capability
        	**type**\:  :py:class:`UpgradeOnConnect <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_cfg.NvSatellites.NvSatellite.UpgradeOnConnect>`
        
        .. attribute:: candidate_fabric_ports
        
        	Enable interfaces on the satellite to be used as fabric ports table
        	**type**\:  :py:class:`CandidateFabricPorts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_cfg.NvSatellites.NvSatellite.CandidateFabricPorts>`
        
        .. attribute:: connection_info
        
        	Satellite User
        	**type**\:  :py:class:`ConnectionInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_cfg.NvSatellites.NvSatellite.ConnectionInfo>`
        
        .. attribute:: redundancy
        
        	Redundancy submode
        	**type**\:  :py:class:`Redundancy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_cfg.NvSatellites.NvSatellite.Redundancy>`
        
        .. attribute:: vrf
        
        	VRF for Satellite IP Address
        	**type**\: str
        
        .. attribute:: timeout_warning
        
        	Discovery timeout warning for the satellite
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: device_name
        
        	Satellite Name
        	**type**\: str
        
        .. attribute:: description
        
        	Satellite Description
        	**type**\: str
        
        .. attribute:: type
        
        	Satellite Type
        	**type**\: str
        
        	**mandatory**\: True
        
        .. attribute:: enable
        
        	Enable
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        	**mandatory**\: True
        
        .. attribute:: disc_timeout
        
        	Discovery timeout for the satellite
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: delayed_switchback
        
        	Timer (in seconds) for delaying switchback in a dual home setup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: second
        
        .. attribute:: serial_number
        
        	Satellite Serial Number
        	**type**\: str
        
        .. attribute:: secret
        
        	Encrypted password for the Satellite
        	**type**\: str
        
        	**pattern:** (!.+)\|([^!].+)
        
        .. attribute:: ip_address
        
        	Satellite IP Address
        	**type**\: union of the below types:
        
        		**type**\: str
        
        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        		**type**\: str
        
        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
        
        

        """

        _prefix = 'icpe-infra-cfg'
        _revision = '2017-09-30'

        def __init__(self):
            super(NvSatellites.NvSatellite, self).__init__()

            self.yang_name = "nv-satellite"
            self.yang_parent_name = "nv-satellites"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['satellite_id']
            self._child_classes = OrderedDict([("upgrade-on-connect", ("upgrade_on_connect", NvSatellites.NvSatellite.UpgradeOnConnect)), ("candidate-fabric-ports", ("candidate_fabric_ports", NvSatellites.NvSatellite.CandidateFabricPorts)), ("connection-info", ("connection_info", NvSatellites.NvSatellite.ConnectionInfo)), ("redundancy", ("redundancy", NvSatellites.NvSatellite.Redundancy))])
            self._leafs = OrderedDict([
                ('satellite_id', (YLeaf(YType.uint32, 'satellite-id'), ['int'])),
                ('vrf', (YLeaf(YType.str, 'vrf'), ['str'])),
                ('timeout_warning', (YLeaf(YType.uint32, 'timeout-warning'), ['int'])),
                ('device_name', (YLeaf(YType.str, 'device-name'), ['str'])),
                ('description', (YLeaf(YType.str, 'description'), ['str'])),
                ('type', (YLeaf(YType.str, 'type'), ['str'])),
                ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                ('disc_timeout', (YLeaf(YType.uint32, 'disc-timeout'), ['int'])),
                ('delayed_switchback', (YLeaf(YType.uint32, 'delayed-switchback'), ['int'])),
                ('serial_number', (YLeaf(YType.str, 'serial-number'), ['str'])),
                ('secret', (YLeaf(YType.str, 'secret'), ['str'])),
                ('ip_address', (YLeaf(YType.str, 'ip-address'), ['str','str'])),
            ])
            self.satellite_id = None
            self.vrf = None
            self.timeout_warning = None
            self.device_name = None
            self.description = None
            self.type = None
            self.enable = None
            self.disc_timeout = None
            self.delayed_switchback = None
            self.serial_number = None
            self.secret = None
            self.ip_address = None

            self.upgrade_on_connect = NvSatellites.NvSatellite.UpgradeOnConnect()
            self.upgrade_on_connect.parent = self
            self._children_name_map["upgrade_on_connect"] = "upgrade-on-connect"

            self.candidate_fabric_ports = NvSatellites.NvSatellite.CandidateFabricPorts()
            self.candidate_fabric_ports.parent = self
            self._children_name_map["candidate_fabric_ports"] = "candidate-fabric-ports"

            self.connection_info = NvSatellites.NvSatellite.ConnectionInfo()
            self.connection_info.parent = self
            self._children_name_map["connection_info"] = "connection-info"

            self.redundancy = NvSatellites.NvSatellite.Redundancy()
            self.redundancy.parent = self
            self._children_name_map["redundancy"] = "redundancy"
            self._segment_path = lambda: "nv-satellite" + "[satellite-id='" + str(self.satellite_id) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-icpe-infra-cfg:nv-satellites/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(NvSatellites.NvSatellite, [u'satellite_id', u'vrf', u'timeout_warning', u'device_name', u'description', u'type', u'enable', u'disc_timeout', u'delayed_switchback', u'serial_number', u'secret', u'ip_address'], name, value)


        class UpgradeOnConnect(Entity):
            """
            Satellite auto\-upgrade capability
            
            .. attribute:: connect_type
            
            	When to upgrade the satellite
            	**type**\:  :py:class:`ConnectType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_cfg.NvSatellites.NvSatellite.UpgradeOnConnect.ConnectType>`
            
            .. attribute:: reference
            
            	Reference name
            	**type**\: str
            
            .. attribute:: image_reference
            
            	Image Reference name
            	**type**\: str
            
            

            """

            _prefix = 'icpe-infra-cfg'
            _revision = '2017-09-30'

            def __init__(self):
                super(NvSatellites.NvSatellite.UpgradeOnConnect, self).__init__()

                self.yang_name = "upgrade-on-connect"
                self.yang_parent_name = "nv-satellite"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('connect_type', (YLeaf(YType.enumeration, 'connect-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_cfg', 'NvSatellites', 'NvSatellite.UpgradeOnConnect.ConnectType')])),
                    ('reference', (YLeaf(YType.str, 'reference'), ['str'])),
                    ('image_reference', (YLeaf(YType.str, 'image-reference'), ['str'])),
                ])
                self.connect_type = None
                self.reference = None
                self.image_reference = None
                self._segment_path = lambda: "upgrade-on-connect"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(NvSatellites.NvSatellite.UpgradeOnConnect, [u'connect_type', u'reference', u'image_reference'], name, value)

            class ConnectType(Enum):
                """
                ConnectType (Enum Class)

                When to upgrade the satellite

                .. data:: on_connection = 1

                	Satellite Upgrade on Connection

                .. data:: on_first_connection = 2

                	Satellite Upgrade on First Connection after

                	configuration or host boot

                """

                on_connection = Enum.YLeaf(1, "on-connection")

                on_first_connection = Enum.YLeaf(2, "on-first-connection")



        class CandidateFabricPorts(Entity):
            """
            Enable interfaces on the satellite to be used
            as fabric ports table
            
            .. attribute:: candidate_fabric_port
            
            	Enable interfaces on the satellite to be used as fabric ports
            	**type**\: list of  		 :py:class:`CandidateFabricPort <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_cfg.NvSatellites.NvSatellite.CandidateFabricPorts.CandidateFabricPort>`
            
            

            """

            _prefix = 'icpe-infra-cfg'
            _revision = '2017-09-30'

            def __init__(self):
                super(NvSatellites.NvSatellite.CandidateFabricPorts, self).__init__()

                self.yang_name = "candidate-fabric-ports"
                self.yang_parent_name = "nv-satellite"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("candidate-fabric-port", ("candidate_fabric_port", NvSatellites.NvSatellite.CandidateFabricPorts.CandidateFabricPort))])
                self._leafs = OrderedDict()

                self.candidate_fabric_port = YList(self)
                self._segment_path = lambda: "candidate-fabric-ports"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(NvSatellites.NvSatellite.CandidateFabricPorts, [], name, value)


            class CandidateFabricPort(Entity):
                """
                Enable interfaces on the satellite to be used
                as fabric ports
                
                .. attribute:: port_type  (key)
                
                	Port type
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: slot  (key)
                
                	Slot
                	**type**\: int
                
                	**range:** 0..8
                
                .. attribute:: sub_slot  (key)
                
                	Sub slot
                	**type**\: int
                
                	**range:** 0..8
                
                .. attribute:: port_range
                
                	Port range
                	**type**\: str
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'icpe-infra-cfg'
                _revision = '2017-09-30'

                def __init__(self):
                    super(NvSatellites.NvSatellite.CandidateFabricPorts.CandidateFabricPort, self).__init__()

                    self.yang_name = "candidate-fabric-port"
                    self.yang_parent_name = "candidate-fabric-ports"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['port_type','slot','sub_slot']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('port_type', (YLeaf(YType.str, 'port-type'), ['str'])),
                        ('slot', (YLeaf(YType.uint32, 'slot'), ['int'])),
                        ('sub_slot', (YLeaf(YType.uint32, 'sub-slot'), ['int'])),
                        ('port_range', (YLeaf(YType.str, 'port-range'), ['str'])),
                    ])
                    self.port_type = None
                    self.slot = None
                    self.sub_slot = None
                    self.port_range = None
                    self._segment_path = lambda: "candidate-fabric-port" + "[port-type='" + str(self.port_type) + "']" + "[slot='" + str(self.slot) + "']" + "[sub-slot='" + str(self.sub_slot) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(NvSatellites.NvSatellite.CandidateFabricPorts.CandidateFabricPort, [u'port_type', u'slot', u'sub_slot', u'port_range'], name, value)


        class ConnectionInfo(Entity):
            """
            Satellite User
            
            .. attribute:: username
            
            	Satellite Username
            	**type**\: str
            
            .. attribute:: password
            
            	Encrypted password for the user
            	**type**\: str
            
            	**pattern:** (!.+)\|([^!].+)
            
            

            """

            _prefix = 'icpe-infra-cfg'
            _revision = '2017-09-30'

            def __init__(self):
                super(NvSatellites.NvSatellite.ConnectionInfo, self).__init__()

                self.yang_name = "connection-info"
                self.yang_parent_name = "nv-satellite"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('username', (YLeaf(YType.str, 'username'), ['str'])),
                    ('password', (YLeaf(YType.str, 'password'), ['str'])),
                ])
                self.username = None
                self.password = None
                self._segment_path = lambda: "connection-info"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(NvSatellites.NvSatellite.ConnectionInfo, [u'username', u'password'], name, value)


        class Redundancy(Entity):
            """
            Redundancy submode
            
            .. attribute:: host_priority
            
            	Priority for this host for the given satellite
            	**type**\: int
            
            	**range:** 0..255
            
            

            """

            _prefix = 'icpe-infra-cfg'
            _revision = '2017-09-30'

            def __init__(self):
                super(NvSatellites.NvSatellite.Redundancy, self).__init__()

                self.yang_name = "redundancy"
                self.yang_parent_name = "nv-satellite"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('host_priority', (YLeaf(YType.uint32, 'host-priority'), ['int'])),
                ])
                self.host_priority = None
                self._segment_path = lambda: "redundancy"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(NvSatellites.NvSatellite.Redundancy, [u'host_priority'], name, value)

    def clone_ptr(self):
        self._top_entity = NvSatellites()
        return self._top_entity

