""" Cisco_IOS_XR_icpe_infra_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR icpe\-infra package configuration.

This module contains definitions
for the following management objects\:
  nv\-satellites\: Satellite Configuration table
  nv\-satellite\-global\: nv satellite global

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg,
  Cisco\-IOS\-XR\-rgmgr\-cfg,
modules with configuration data.

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError




class NvSatellites(object):
    """
    Satellite Configuration table
    
    .. attribute:: nv_satellite
    
    	Satellite Configuration
    	**type**\: list of :py:class:`NvSatellite <ydk.models.icpe.Cisco_IOS_XR_icpe_infra_cfg.NvSatellites.NvSatellite>`
    
    

    """

    _prefix = 'icpe-infra-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.nv_satellite = YList()
        self.nv_satellite.parent = self
        self.nv_satellite.name = 'nv_satellite'


    class NvSatellite(object):
        """
        Satellite Configuration
        
        .. attribute:: satellite_id  <key>
        
        	Satellite ID
        	**type**\: int
        
        	**range:** 100..65534
        
        .. attribute:: candidate_fabric_ports
        
        	Enable interfaces on the satellite to be used as fabric ports table
        	**type**\: :py:class:`CandidateFabricPorts <ydk.models.icpe.Cisco_IOS_XR_icpe_infra_cfg.NvSatellites.NvSatellite.CandidateFabricPorts>`
        
        .. attribute:: connection_info
        
        	Satellite User
        	**type**\: :py:class:`ConnectionInfo <ydk.models.icpe.Cisco_IOS_XR_icpe_infra_cfg.NvSatellites.NvSatellite.ConnectionInfo>`
        
        .. attribute:: redundancy
        
        	Redundancy submode
        	**type**\: :py:class:`Redundancy <ydk.models.icpe.Cisco_IOS_XR_icpe_infra_cfg.NvSatellites.NvSatellite.Redundancy>`
        
        .. attribute:: vrf
        
        	VRF for Satellite IP Address
        	**type**\: str
        
        .. attribute:: upgrade_on_connect
        
        	Satellite Upgrade on Connection
        	**type**\: int
        
        	**range:** 0..255
        
        .. attribute:: device_name
        
        	Satellite Name
        	**type**\: str
        
        .. attribute:: description
        
        	Satellite Description
        	**type**\: str
        
        .. attribute:: type
        
        	Satellite Type
        	**type**\: str
        
        .. attribute:: enable
        
        	Enable
        	**type**\: :py:class:`Empty <ydk.types.Empty>`
        
        .. attribute:: disc_timeout
        
        	Discovery timeout for the satellite
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: serial_number
        
        	Satellite Serial Number
        	**type**\: str
        
        .. attribute:: secret
        
        	Encrypted password for the Satellite
        	**type**\: str
        
        	**pattern:** (!.+)\|([^!].+)
        
        .. attribute:: ip_address
        
        	Satellite IP Address
        	**type**\: one of the below types:
        
        	**type**\: str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        
        ----
        	**type**\: str
        
        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
        
        
        ----
        

        """

        _prefix = 'icpe-infra-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.satellite_id = None
            self.candidate_fabric_ports = NvSatellites.NvSatellite.CandidateFabricPorts()
            self.candidate_fabric_ports.parent = self
            self.connection_info = NvSatellites.NvSatellite.ConnectionInfo()
            self.connection_info.parent = self
            self.redundancy = NvSatellites.NvSatellite.Redundancy()
            self.redundancy.parent = self
            self.vrf = None
            self.upgrade_on_connect = None
            self.device_name = None
            self.description = None
            self.type = None
            self.enable = None
            self.disc_timeout = None
            self.serial_number = None
            self.secret = None
            self.ip_address = None


        class CandidateFabricPorts(object):
            """
            Enable interfaces on the satellite to be used
            as fabric ports table
            
            .. attribute:: candidate_fabric_port
            
            	Enable interfaces on the satellite to be used as fabric ports
            	**type**\: list of :py:class:`CandidateFabricPort <ydk.models.icpe.Cisco_IOS_XR_icpe_infra_cfg.NvSatellites.NvSatellite.CandidateFabricPorts.CandidateFabricPort>`
            
            

            """

            _prefix = 'icpe-infra-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.candidate_fabric_port = YList()
                self.candidate_fabric_port.parent = self
                self.candidate_fabric_port.name = 'candidate_fabric_port'


            class CandidateFabricPort(object):
                """
                Enable interfaces on the satellite to be used
                as fabric ports
                
                .. attribute:: port_type  <key>
                
                	Port type
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: slot  <key>
                
                	Slot
                	**type**\: int
                
                	**range:** 0..8
                
                .. attribute:: sub_slot  <key>
                
                	Sub slot
                	**type**\: int
                
                	**range:** 0..8
                
                .. attribute:: port_range
                
                	Port range
                	**type**\: str
                
                

                """

                _prefix = 'icpe-infra-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.port_type = None
                    self.slot = None
                    self.sub_slot = None
                    self.port_range = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')
                    if self.port_type is None:
                        raise YPYDataValidationError('Key property port_type is None')
                    if self.slot is None:
                        raise YPYDataValidationError('Key property slot is None')
                    if self.sub_slot is None:
                        raise YPYDataValidationError('Key property sub_slot is None')

                    return self.parent._common_path +'/Cisco-IOS-XR-icpe-infra-cfg:candidate-fabric-port[Cisco-IOS-XR-icpe-infra-cfg:port-type = ' + str(self.port_type) + '][Cisco-IOS-XR-icpe-infra-cfg:slot = ' + str(self.slot) + '][Cisco-IOS-XR-icpe-infra-cfg:sub-slot = ' + str(self.sub_slot) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.port_type is not None:
                        return True

                    if self.slot is not None:
                        return True

                    if self.sub_slot is not None:
                        return True

                    if self.port_range is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.icpe._meta import _Cisco_IOS_XR_icpe_infra_cfg as meta
                    return meta._meta_table['NvSatellites.NvSatellite.CandidateFabricPorts.CandidateFabricPort']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/Cisco-IOS-XR-icpe-infra-cfg:candidate-fabric-ports'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.candidate_fabric_port is not None:
                    for child_ref in self.candidate_fabric_port:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.icpe._meta import _Cisco_IOS_XR_icpe_infra_cfg as meta
                return meta._meta_table['NvSatellites.NvSatellite.CandidateFabricPorts']['meta_info']


        class ConnectionInfo(object):
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
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.username = None
                self.password = None

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/Cisco-IOS-XR-icpe-infra-cfg:connection-info'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.username is not None:
                    return True

                if self.password is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.icpe._meta import _Cisco_IOS_XR_icpe_infra_cfg as meta
                return meta._meta_table['NvSatellites.NvSatellite.ConnectionInfo']['meta_info']


        class Redundancy(object):
            """
            Redundancy submode
            
            .. attribute:: host_priority
            
            	Priority for this host for the given satellite
            	**type**\: int
            
            	**range:** 0..255
            
            

            """

            _prefix = 'icpe-infra-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.host_priority = None

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/Cisco-IOS-XR-icpe-infra-cfg:redundancy'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.host_priority is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.icpe._meta import _Cisco_IOS_XR_icpe_infra_cfg as meta
                return meta._meta_table['NvSatellites.NvSatellite.Redundancy']['meta_info']

        @property
        def _common_path(self):
            if self.satellite_id is None:
                raise YPYDataValidationError('Key property satellite_id is None')

            return '/Cisco-IOS-XR-icpe-infra-cfg:nv-satellites/Cisco-IOS-XR-icpe-infra-cfg:nv-satellite[Cisco-IOS-XR-icpe-infra-cfg:satellite-id = ' + str(self.satellite_id) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.satellite_id is not None:
                return True

            if self.candidate_fabric_ports is not None and self.candidate_fabric_ports._has_data():
                return True

            if self.connection_info is not None and self.connection_info._has_data():
                return True

            if self.redundancy is not None and self.redundancy._has_data():
                return True

            if self.vrf is not None:
                return True

            if self.upgrade_on_connect is not None:
                return True

            if self.device_name is not None:
                return True

            if self.description is not None:
                return True

            if self.type is not None:
                return True

            if self.enable is not None:
                return True

            if self.disc_timeout is not None:
                return True

            if self.serial_number is not None:
                return True

            if self.secret is not None:
                return True

            if self.ip_address is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.icpe._meta import _Cisco_IOS_XR_icpe_infra_cfg as meta
            return meta._meta_table['NvSatellites.NvSatellite']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-icpe-infra-cfg:nv-satellites'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.nv_satellite is not None:
            for child_ref in self.nv_satellite:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.icpe._meta import _Cisco_IOS_XR_icpe_infra_cfg as meta
        return meta._meta_table['NvSatellites']['meta_info']


class NvSatelliteGlobal(object):
    """
    nv satellite global
    
    .. attribute:: chassis_mac
    
    	Chassis MAC address
    	**type**\: :py:class:`ChassisMac <ydk.models.icpe.Cisco_IOS_XR_icpe_infra_cfg.NvSatelliteGlobal.ChassisMac>`
    
    

    """

    _prefix = 'icpe-infra-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.chassis_mac = NvSatelliteGlobal.ChassisMac()
        self.chassis_mac.parent = self


    class ChassisMac(object):
        """
        Chassis MAC address
        
        .. attribute:: mac1
        
        	First two bytes of MAC address
        	**type**\: int
        
        	**range:** 0..2147483647
        
        .. attribute:: mac2
        
        	Second two bytes of MAC address
        	**type**\: int
        
        	**range:** 0..2147483647
        
        .. attribute:: mac3
        
        	Third two bytes of MAC address
        	**type**\: int
        
        	**range:** 0..2147483647
        
        

        """

        _prefix = 'icpe-infra-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.mac1 = None
            self.mac2 = None
            self.mac3 = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-icpe-infra-cfg:nv-satellite-global/Cisco-IOS-XR-icpe-infra-cfg:chassis-mac'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.mac1 is not None:
                return True

            if self.mac2 is not None:
                return True

            if self.mac3 is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.icpe._meta import _Cisco_IOS_XR_icpe_infra_cfg as meta
            return meta._meta_table['NvSatelliteGlobal.ChassisMac']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-icpe-infra-cfg:nv-satellite-global'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.chassis_mac is not None and self.chassis_mac._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.icpe._meta import _Cisco_IOS_XR_icpe_infra_cfg as meta
        return meta._meta_table['NvSatelliteGlobal']['meta_info']


