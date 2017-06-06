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

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class NvSatelliteGlobal(object):
    """
    nV Satellite Global configuration
    
    .. attribute:: chassis_mac
    
    	Chassis MAC address
    	**type**\:   :py:class:`ChassisMac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_cfg.NvSatelliteGlobal.ChassisMac>`
    
    

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
            if self.mac1 is not None:
                return True

            if self.mac2 is not None:
                return True

            if self.mac3 is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_icpe_infra_cfg as meta
            return meta._meta_table['NvSatelliteGlobal.ChassisMac']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-icpe-infra-cfg:nv-satellite-global'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.chassis_mac is not None and self.chassis_mac._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_icpe_infra_cfg as meta
        return meta._meta_table['NvSatelliteGlobal']['meta_info']


class NvSatellites(object):
    """
    nv satellites
    
    .. attribute:: nv_satellite
    
    	Satellite Configuration
    	**type**\: list of    :py:class:`NvSatellite <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_cfg.NvSatellites.NvSatellite>`
    
    

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
            self.parent = None
            self.satellite_id = None
            self.candidate_fabric_ports = NvSatellites.NvSatellite.CandidateFabricPorts()
            self.candidate_fabric_ports.parent = self
            self.connection_info = NvSatellites.NvSatellite.ConnectionInfo()
            self.connection_info.parent = self
            self.delayed_switchback = None
            self.description = None
            self.device_name = None
            self.disc_timeout = None
            self.enable = None
            self.ip_address = None
            self.redundancy = NvSatellites.NvSatellite.Redundancy()
            self.redundancy.parent = self
            self.secret = None
            self.serial_number = None
            self.timeout_warning = None
            self.type = None
            self.upgrade_on_connect = NvSatellites.NvSatellite.UpgradeOnConnect()
            self.upgrade_on_connect.parent = self
            self.vrf = None


        class UpgradeOnConnect(object):
            """
            Satellite auto\-upgrade capability
            
            .. attribute:: connect_type
            
            	When to upgrade the satellite
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: reference
            
            	Reference name
            	**type**\:  str
            
            

            """

            _prefix = 'icpe-infra-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.connect_type = None
                self.reference = None

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/Cisco-IOS-XR-icpe-infra-cfg:upgrade-on-connect'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.connect_type is not None:
                    return True

                if self.reference is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_icpe_infra_cfg as meta
                return meta._meta_table['NvSatellites.NvSatellite.UpgradeOnConnect']['meta_info']


        class CandidateFabricPorts(object):
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
                    self.parent = None
                    self.port_type = None
                    self.slot = None
                    self.sub_slot = None
                    self.port_range = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.port_type is None:
                        raise YPYModelError('Key property port_type is None')
                    if self.slot is None:
                        raise YPYModelError('Key property slot is None')
                    if self.sub_slot is None:
                        raise YPYModelError('Key property sub_slot is None')

                    return self.parent._common_path +'/Cisco-IOS-XR-icpe-infra-cfg:candidate-fabric-port[Cisco-IOS-XR-icpe-infra-cfg:port-type = ' + str(self.port_type) + '][Cisco-IOS-XR-icpe-infra-cfg:slot = ' + str(self.slot) + '][Cisco-IOS-XR-icpe-infra-cfg:sub-slot = ' + str(self.sub_slot) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
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
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_icpe_infra_cfg as meta
                    return meta._meta_table['NvSatellites.NvSatellite.CandidateFabricPorts.CandidateFabricPort']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/Cisco-IOS-XR-icpe-infra-cfg:candidate-fabric-ports'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.candidate_fabric_port is not None:
                    for child_ref in self.candidate_fabric_port:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_icpe_infra_cfg as meta
                return meta._meta_table['NvSatellites.NvSatellite.CandidateFabricPorts']['meta_info']


        class ConnectionInfo(object):
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
                self.parent = None
                self.password = None
                self.username = None

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/Cisco-IOS-XR-icpe-infra-cfg:connection-info'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.password is not None:
                    return True

                if self.username is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_icpe_infra_cfg as meta
                return meta._meta_table['NvSatellites.NvSatellite.ConnectionInfo']['meta_info']


        class Redundancy(object):
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
                self.parent = None
                self.host_priority = None

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/Cisco-IOS-XR-icpe-infra-cfg:redundancy'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.host_priority is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_icpe_infra_cfg as meta
                return meta._meta_table['NvSatellites.NvSatellite.Redundancy']['meta_info']

        @property
        def _common_path(self):
            if self.satellite_id is None:
                raise YPYModelError('Key property satellite_id is None')

            return '/Cisco-IOS-XR-icpe-infra-cfg:nv-satellites/Cisco-IOS-XR-icpe-infra-cfg:nv-satellite[Cisco-IOS-XR-icpe-infra-cfg:satellite-id = ' + str(self.satellite_id) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.satellite_id is not None:
                return True

            if self.candidate_fabric_ports is not None and self.candidate_fabric_ports._has_data():
                return True

            if self.connection_info is not None and self.connection_info._has_data():
                return True

            if self.delayed_switchback is not None:
                return True

            if self.description is not None:
                return True

            if self.device_name is not None:
                return True

            if self.disc_timeout is not None:
                return True

            if self.enable is not None:
                return True

            if self.ip_address is not None:
                return True

            if self.redundancy is not None and self.redundancy._has_data():
                return True

            if self.secret is not None:
                return True

            if self.serial_number is not None:
                return True

            if self.timeout_warning is not None:
                return True

            if self.type is not None:
                return True

            if self.upgrade_on_connect is not None and self.upgrade_on_connect._has_data():
                return True

            if self.vrf is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_icpe_infra_cfg as meta
            return meta._meta_table['NvSatellites.NvSatellite']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-icpe-infra-cfg:nv-satellites'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.nv_satellite is not None:
            for child_ref in self.nv_satellite:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_icpe_infra_cfg as meta
        return meta._meta_table['NvSatellites']['meta_info']


